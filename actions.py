# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
import typing
from typing import Dict, Text, Any, List, Union

import mysql.connector
import requests
from rasa_core_sdk import Action
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk.events import SlotSet, FollowupAction
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

if typing.TYPE_CHECKING:
    from rasa_core_sdk import Tracker
    from rasa_core_sdk.executor import CollectingDispatcher

ENDPOINTS = {
    "base": "https://data.medicare.gov/resource/{}.json",
    "rbry-mqwu": {
        "city_query": "?city={}",
        "zip_code_query": "?$where=zip_code in({})",
        "id_query": "?provider_id={}"
    },
    "b27b-2uc7": {
        "city_query": "?provider_city={}",
        "zip_code_query": "?$where=provider_zip_code in({})",
        "id_query": "?federal_provider_number={}"

    },
    "9wzi-peqs": {
        "city_query": "?city={}",
        "zip_code_query": "?$where=zip in({})",
        "id_query": "?provider_number={}"
    }
}

FACILITY_TYPES = {

    "hospital":
        {
            "name": "hospital",
            "resource": "rbry-mqwu"
        },
    "nursing_home":
        {
            "name": "nursing home",
            "resource": "b27b-2uc7"
        },
    "home_health":
        {
            "name": "Home Health Agency",
            "resource": "9wzi-peqs"
        },
}


class FindProviderTypes(Action):
    def name(self):
        return "find_provider_types"

    def run(self, dispatcher, tracker, domain):
        buttons = []
        for t in FACILITY_TYPES:
            r = FACILITY_TYPES[t]
            payload = "/inform{\"selected_type_slot\": \"" + r.get(
                "resource") + "\"}"

            buttons.append(
                {"title": "{}".format(r.get("name").title()),
                 "payload": payload})
        dispatcher.utter_button_template("utter_greet", buttons, tracker)
        return [SlotSet("provider_types_slot",
                        FACILITY_TYPES if FACILITY_TYPES is not None else [])]


def create_path(base, resource, query, values):
    if isinstance(values, list):
        return (base + query).format(resource,
                                     ', '.join(
                                         '"{0}"'.format(w) for w in values))
    else:
        return (base + query).format(resource, values)


def find_provider(zips, city, resource, max_radius=20, min_results=3,
                  increment=5):
    if zips is not None:
        full_path = create_path(ENDPOINTS["base"], resource,
                                ENDPOINTS[resource]["zip_code_query"], [zips])
        results = requests.get(full_path).json()
        if len(results) == 0:

            radius = 5
            while radius < max_radius and len(results) < min_results:
                zips = find_near_zip_codes(zip, radius)
                zips.append(zip)
                full_path = create_path(ENDPOINTS["base"], resource,
                                        ENDPOINTS[resource]["zip_code_query"],
                                        zips)
                results = requests.get(full_path).json()
                radius += increment

    if city is not None:
        full_path = create_path(ENDPOINTS["base"], resource,
                                ENDPOINTS[resource]["city_query"], city.upper())
        results = requests.get(full_path).json()

    return results


def do_zip_code_exist(zip):
    user = os.environ['DB_USER']
    passwd = os.environ['PASSWD']
    host = os.environ['HOST']
    db = mysql.connector.connect(host=host, user=user, passwd=passwd,
                                 db="natlhcentities")
    cursor = db.cursor(buffered=True)
    q = "select exists (select * from  uszipcode where ZipCode = '{}')".format(
        zip)
    cursor.execute(q)
    results = cursor.fetchall()
    return results[0][0] == 1


def find_near_zip_codes(zip, radius):
    api_key = "v4hu7DhkF2wrTQ9JXYkOgT0V51DUuxVn6f4SBP8YXbcXqfuBbLdeoX3Vt8rnhLmS"
    base_url = "https://www.zipcodeapi.com/rest/{}/radius.json/{}/{}/miles?minimal"
    r = requests.get(base_url.format(api_key, zip, radius))
    return r.json().get("zip_codes")


def create_query(type, zips):
    q = "select HCProviderID, HCProviderName from healthcareprovider where " \
        "HCProviderZipcode in ({}) and HCEntityTypeID = {}".format(
        ",".join(zips), type)
    return q


class FindHospital(Action):

    def name(self):
        return "find_hospital"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
        zip = tracker.get_slot('zip')
        city = tracker.get_slot('city')
        type = tracker.get_slot('selected_type_slot')
        # if not do_zip_code_exist(zip):
        #     dispatcher.utter_message("Please, provide a valid zipcode.")
        #     return []
        results = find_provider(zip, city, type)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a heathcare provider within 20 miles from your ZIP code.")
            return []
        buttons = []
        print("found {} providers".format(len(results)))
        for r in results:
            if type == FACILITY_TYPES["hospital"]["resource"]:
                provider_id = r.get("provider_id")
                name = r["hospital_name"]
            elif type == FACILITY_TYPES["nursing_home"]["resource"]:
                provider_id = r["federal_provider_number"]
                name = r["provider_name"]
            else:
                provider_id = r["provider_number"]
                name = r["provider_name"]
            payload = "/inform{\"selected_id\":" + provider_id + "}"
            buttons.append(
                {"title": "{}".format(name.title()), "payload": payload})
        dispatcher.utter_button_message(
            "Here is a list of healthcare providers near you", buttons)

        return []


class FindHealthCareAddress(Action):

    def name(self):
        return "find_healthcare_address"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):
        type = tracker.get_slot('selected_type_slot')
        healthcare_id = tracker.get_slot("selected_id")
        full_path = create_path(ENDPOINTS["base"], type,
                                ENDPOINTS[type]["id_query"],
                                healthcare_id)
        results = requests.get(full_path).json()
        selected = results[0]
        if type == FACILITY_TYPES["hospital"]["resource"]:
            address = "{}, {}, {}".format(selected["address"].title(),
                                          selected["zip_code"].title(),
                                          selected["city"].title())
        elif type == FACILITY_TYPES["nursing_home"]["resource"]:
            address = "{}, {}, {}".format(selected["provider_address"].title(),
                                          selected["provider_zip_code"].title(),
                                          selected["provider_city"].title())
        else:
            address = "{}, {}, {}".format(selected["address"].title(),
                                          selected["zip"].title(),
                                          selected["city"].title())

        return [
            SlotSet("selected_address", address if results is not None else "")]


class HospitalForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "hospital_form"

    @staticmethod
    def required_slots(tracker):
        # type: (Tracker) -> List[Text]
        """A list of required slots that the form has to fill"""

        if tracker.get_slot("zip") is not None:
            return []
        elif tracker.get_slot("city") is not None:
            return []
        else:
            return ["zip", "city"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"zip": self.from_entity(entity="number", intent="inform")}

    @staticmethod
    def is_zip(string):
        # type: (Text) -> bool
        #       if tracker.get_slot("zip") is not None:

        #             return []
        #         elif tracker.get_slot("city") is not None:
        #             return []
        #         else:
        #             return ["zip", "city"]
        """Check if a string is an integer"""
        # try:
        #     int(string)
        #     return len(string) == 5
        # except ValueError:
        #     return False
        return do_zip_code_exist(string)

    @staticmethod
    def is_city(string):
        return True

    def validate(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'zip':
                if not self.is_zip(value):
                    dispatcher.utter_template('utter_wrong_num_people',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None
            elif slot == 'city':
                if not self.is_city(value):
                    dispatcher.utter_message("Please enter a valid city")
        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return [FollowupAction('find_hospital')]


class CenterForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "center_form"

    @staticmethod
    def required_slots(tracker):
        # type: (Tracker) -> List[Text]
        """A list of required slots that the form has to fill"""

        return ["zip", "type"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"zip": self.from_entity(entity="number"),
                "type": self.from_entity(entity="type")}

    @staticmethod
    def is_zip(string):
        # type: (Text) -> bool
        """Check if a string is an integer"""
        try:
            int(string)
            return len(string) == 5
        except ValueError:
            return False

    def validate(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'zip':
                if not self.is_zip(value):
                    dispatcher.utter_template('utter_wrong_num_people',
                                              tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_chitchat"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message['intent'].get('name')

        # retrieve the correct chitchat utterance dependent on the intent
        if intent in ['ask_builder', 'ask_weather', 'ask_howdoing',
                      'ask_whatspossible', 'ask_whatisrasa', 'ask_isbot',
                      'ask_howold', 'ask_languagesbot', 'ask_restaurant',
                      'ask_time', 'ask_wherefrom', 'ask_whoami',
                      'handleinsult', 'nicetomeeyou', 'telljoke',
                      'ask_whatismyname', 'howwereyoubuilt', 'ask_whoisit']:
            dispatcher.utter_template('utter_' + intent, tracker)
        return []
