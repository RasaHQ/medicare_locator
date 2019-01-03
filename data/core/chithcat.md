## just chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_provider_types


## happy path 3 1
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
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

## happy path 3 2
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot":1}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
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
    
## happy path 3 3
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_hospital
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
    
## happy path 4 1
* search_provider{"selected_type_slot":2}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"zip"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
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
    
    
## happy path 4 2
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
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_hospital
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
