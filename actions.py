# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os

import typing
from typing import Dict, Text, Any, List, Union

from rasa_core_sdk import ActionExecutionRejection
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, FollowupAction
import mysql.connector

if typing.TYPE_CHECKING:
    from rasa_core_sdk import Tracker
    from rasa_core_sdk.executor import CollectingDispatcher


class FindProviderTypes(Action):
    def name(self):
        return "find_provider_types"

    def run(self, dispatcher, tracker, domain):
        user = os.environ['DB_USER']
        passwd = os.environ['PASSWD']
        host = os.environ['HOST']
        db = mysql.connector.connect(host=host, user=user, passwd=passwd,
                                     db="natlhcentities")
        cursor = db.cursor(buffered=True)
        q = "select * from  hcentitytype"
        cursor.execute(q)
        result = cursor.fetchall()
        buttons = []
        for r in result:
            payload = "/inform{\"selected_type_slot\":"+str(r[0])+"}"
            buttons.append(
                {"title": "{}".format(r[1]), "payload": payload})
        dispatcher.utter_button_template("utter_greet", buttons, tracker)
        return [SlotSet("provider_types_slot",
                        result if result is not None else [])]


class FindHospital(Action):

    def name(self):
        return "find_hospital"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
        user = os.environ['DB_USER']
        passwd = os.environ['PASSWD']
        host = os.environ['HOST']
        db = mysql.connector.connect(host=host, user=user, passwd=passwd,
                                     db="natlhcentities")
        cursor = db.cursor(buffered=True)
        zip = tracker.get_slot('zip')
        type = tracker.get_slot('selected_type_slot')
        q = "select HCProviderID, HCProviderName from healthcareprovider where " \
            "HCProviderZipcode = {} and HCEntityTypeID = {}".format(
            zip, type)
        cursor.execute(q)
        results = cursor.fetchall()
        buttons = []
        print("found {} providers".format(len(results)))
        for r in results:
            payload = "/inform{\"selected_id\":"+str(r[0])+"}"
            buttons.append(
                {"title": "{}".format(r[1]), "payload": payload})
        dispatcher.utter_button_message("Here is a list of healthcare providers near you", buttons)

        return []


class FindHealthCareAddress(Action):

    def name(self):
        return "find_healthcare_address"

    def run(self,
            dispatcher,  # type: CollectingDispatcher
            tracker,  # type: Tracker
            domain  # type:  Dict[Text, Any]
            ):
        user = os.environ['DB_USER']
        passwd = os.environ['PASSWD']
        host = os.environ['HOST']
        db = mysql.connector.connect(host=host, user=user, passwd=passwd,
                                     db="natlhcentities")
        cursor = db.cursor(buffered=True)
        healthcare_id = tracker.get_slot("selected_id")
        q = "select HCProviderAddress, HCProviderCity, HCProviderState from " \
            "healthcareprovider where HCProviderID = {}".format(
            healthcare_id)
        cursor.execute(q)
        results = cursor.fetchall()[0]

        address = "{}, {}, {}".format(results[0], results[1], results[2])
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

        return ["zip"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {"zip": self.from_entity(entity="number", intent="inform")
                }

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
