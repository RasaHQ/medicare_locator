# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_core_sdk import Action
from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk.events import SlotSet, FollowupAction
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT

# We use the medicore.gov database to find information about 3 different
# healthcare facility types, given a city name, zip code or facility ID
# the identifiers for each facility type is given by the medicare database
# rbry-mqwu is for hospitals
# b27b-2uc7 is for nursing homes
# 9wzi-peqs is for home health agencies

ENDPOINTS = {
    "base": "https://data.medicare.gov/resource/{}.json",
    "rbry-mqwu": {
        "city_query": "?city={}",
        "zip_code_query": "?zip_code={}",
        "id_query": "?provider_id={}"
    },
    "b27b-2uc7": {
        "city_query": "?provider_city={}",
        "zip_code_query": "?provider_zip_code={}",
        "id_query": "?federal_provider_number={}"
    },
    "9wzi-peqs": {
        "city_query": "?city={}",
        "zip_code_query": "?zip={}",
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
        }
}


class FindFacilityTypes(Action):
    '''This action class allows to display buttons for each facility type
    for the user to chose from to fill the facility_type entity slot.'''

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_facility_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        buttons = []
        for t in FACILITY_TYPES:
            facility_type = FACILITY_TYPES[t]
            payload = "/inform{\"facility_type\": \"" + facility_type.get(
                "resource") + "\"}"

            buttons.append(
                {"title": "{}".format(facility_type.get("name").title()),
                 "payload": payload})

        dispatcher.utter_button_template("utter_greet", buttons, tracker,
                                         button_type="custom")
        return []


def _create_path(base: Text, resource: Text,
                 query: Text, values: Text) -> Text:
    '''Creates a path to find provider using the endpoints.'''

    if isinstance(values, list):
        return (base + query).format(
            resource, ', '.join('"{0}"'.format(w) for w in values))
    else:
        return (base + query).format(resource, values)


def _find_facilities(location: Text, resource: Text) -> List[Dict]:
    '''Returns json of facilities matching the search criteria.'''

    if str.isdigit(location):
        full_path = _create_path(ENDPOINTS["base"], resource,
                                 ENDPOINTS[resource]["zip_code_query"],
                                 location)
    else:
        full_path = _create_path(ENDPOINTS["base"], resource,
                                 ENDPOINTS[resource]["city_query"],
                                 location.upper())

    results = requests.get(full_path).json()
    return results


def _resolve_name(facility_types, resource) ->Text:
    for key, value in facility_types.items():
        if value.get("resource") == resource:
            return value.get("name")
    return ""


class FindFacilities(Action):
    '''This action class retrieves a list of all facilities matching
    the supplied search criteria and displays buttons of random search
    results to the user to pick from.'''

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_facilities"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

        location = tracker.get_slot('location')
        facility_type = tracker.get_slot('facility_type')

        results = _find_facilities(location, facility_type)
        button_name = _resolve_name(FACILITY_TYPES, facility_type)
        if len(results) == 0:
            dispatcher.utter_message(
                "Sorry, we could not find a {} in {}.".format(button_name,
                                                              location))
            return []

        buttons = []
        print("found {} facilities".format(len(results)))
        for r in results:
            if facility_type == FACILITY_TYPES["hospital"]["resource"]:
                facility_id = r.get("provider_id")
                name = r["hospital_name"]
            elif facility_type == FACILITY_TYPES["nursing_home"]["resource"]:
                facility_id = r["federal_provider_number"]
                name = r["provider_name"]
            else:
                facility_id = r["provider_number"]
                name = r["provider_name"]

            payload = "/inform{\"facility_id\":\"" + facility_id + "\"}"
            buttons.append(
                {"title": "{}".format(name.title()), "payload": payload})

        # limit number of buttons to 3 here for clear presentation purpose
        dispatcher.utter_button_message(
            "Here is a list of {} {}s near you".format(len(buttons[:3]),
                                                       button_name),
            buttons[:3], button_type="custom")
        # todo: note: button options are not working BUG in rasa_core

        return []


class FindHealthCareAddress(Action):
    '''This action class retrieves the address of the users
    healthcare facility choice to display it to the user.'''

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "find_healthcare_address"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        facility_type = tracker.get_slot('facility_type')
        healthcare_id = tracker.get_slot("facility_id")
        full_path = _create_path(ENDPOINTS["base"], facility_type,
                                 ENDPOINTS[facility_type]["id_query"],
                                 healthcare_id)
        results = requests.get(full_path).json()
        selected = results[0]
        if facility_type == FACILITY_TYPES["hospital"]["resource"]:
            address = "{}, {}, {}".format(selected["address"].title(),
                                          selected["zip_code"].title(),
                                          selected["city"].title())
        elif facility_type == FACILITY_TYPES["nursing_home"]["resource"]:
            address = "{}, {}, {}".format(selected["provider_address"].title(),
                                          selected["provider_zip_code"].title(),
                                          selected["provider_city"].title())
        else:
            address = "{}, {}, {}".format(selected["address"].title(),
                                          selected["zip"].title(),
                                          selected["city"].title())

        return [
            SlotSet("facility_address", address if results is not None else "")]


class FacilityForm(FormAction):
    """Custom form action to fill all slots required to find specific type
    of healthcare facilities in a certain city or zip code."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "facility_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["facility_type", "location"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {
            "facility_type": self.from_entity(entity="facility_type",
                                              intent=["inform",
                                                      "search_provider"]),
            "location": self.from_entity(entity="location",
                                         intent=["inform",
                                                 "search_provider"])}

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]
                 ) -> List[Dict]:

        """Validate extracted requested slot
        else reject the execution of the form action"""

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

        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return [FollowupAction('find_facilities')]


class ActionChitchat(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self) -> Text:
        """Unique identifier of the action"""

        return "action_chitchat"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List:

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
