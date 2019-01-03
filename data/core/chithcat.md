## happy path 3
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_greet
    - find_provider_types
* inform{"selected_type_slot":1}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* inform{"number":"77494"}
    - hospital_form
    - slot{"zip":"77494"}
    - slot{"requested_slot":null}
    - find_hospital
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries

## happy path 3
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot":1}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* inform{"number":"77494"}
    - hospital_form
    - slot{"zip":"77494"}
    - slot{"requested_slot":null}
    - find_hospital
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
    
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot":1}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* inform{"number":"77494"}
    - hospital_form
    - slot{"zip":"77494"}
    - slot{"requested_slot":null}
    - find_hospital
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_languagesbot OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
    
## happy path 4
* search_provider{"selected_type_slot":2}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* inform{"number":"77494"}
    - hospital_form
    - slot{"zip":"77494"}
    - slot{"requested_slot":null}
    - find_hospital
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
    
    
## happy path 5
* search_provider{"selected_type_slot":2, "number":"77494"}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - find_hospital
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries

## Generated Story 4264792477705751069
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 1}
    - slot{"selected_type_slot": 1}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "44870"}
    - form: hospital_form
    - slot{"zip": "44870"}
    - form{"name": null}
    - slot{"requested_slot": null}
* inform{"selected_id": 1824}
    - slot{"selected_id": 1824}
    - find_healthcare_address
    - slot{"selected_address": [["309 JACKSON STREET", "MONROE", "LA"]]}
    - utter_address
* thankyou
    - utter_noworries