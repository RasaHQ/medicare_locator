# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import typing
from typing import Dict, Text, Any, List, Union

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
        dispatcher.utter_button_template("utter_greet", buttons,
                                         tracker, button_type="vertical")
        return [SlotSet("provider_types_slot",
                        FACILITY_TYPES if FACILITY_TYPES is not None else [])]


def create_path(base, resource, query, values):
    if isinstance(values, list):
        return (base + query).format(resource,
                                     ', '.join(
                                         '"{0}"'.format(w) for w in values))
    else:
        return (base + query).format(resource, values)


def find_provider(city, resource):
    if city is not None:
        full_path = create_path(ENDPOINTS["base"], resource,
                                ENDPOINTS[resource]["city_query"], city.upper())
        results = requests.get(full_path).json()

    return results


def _resolve_name(facility_types, resource):
    for k, v in FACILITY_TYPES.items():
        if v.get("resource") == resource:
            return v.get("name")
    return ""


class FindHospital(Action):

    def name(self):
        return "find_hospital"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker,
        # Dict[Text, Any]) -> List[Dict[Text, Any]]
        city = tracker.get_slot('city')
        type = tracker.get_slot('selected_type_slot')
        results = find_provider(city, type)
        name = _resolve_name(FACILITY_TYPES, type)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(name, city))
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
            payload = "/inform{\"selected_id\":\"" + provider_id + "\"}"
            buttons.append(
                {"title": "{}".format(name.title()), "payload": payload})

        dispatcher.utter_button_message(
            "Here is a list of the first 3 {} near you".format(name),
            buttons[:3], button_type="vertical")
        # todo: vertical is not working + limit button number make it rule based

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

        return ["selected_type_slot", "city"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {
            "city": self.from_entity(entity="city", intent="inform"),
            "selected_type_slot": self.from_entity(entity="provider_type",
                                                   intent="inform")
        }

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
            if slot == 'city':
                if not self.is_city(value):
                    dispatcher.utter_message("Please enter a valid city")
                    slot_values[slot] = None
        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict]
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return [FollowupAction('find_hospital')]


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
