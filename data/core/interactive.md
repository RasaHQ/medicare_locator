## Generated Story 6487586636610894716
* greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 2}
    - slot{"selected_type_slot": 2}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "77494"}
    - form: hospital_form
    - slot{"zip": "77494"}
    - form: followup{"name": "find_hospital"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* ask_howold
    - action_chitchat
    - find_hospital
* inform{"selected_id": 29450}
    - slot{"selected_id": 29450}
    - find_healthcare_address
    - slot{"selected_address": "1260 PIN OAK DRIVE, SUITE #209, KATY, TX"}
    - utter_address
* ask_builder
    - action_chitchat

