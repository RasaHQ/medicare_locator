## chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    
## chitchat_mixed_in
* greet
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": "facility_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": null}
    - find_facilities
* inform{"facility_id": "050407"}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries 
    
## chitchat_continue_task
* greet
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": "facility_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_facility_types
    - facility_form
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_continue  
* affirm
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - facility_form 
    - form{"name": null}
    - find_facilities
* inform{"facility_id": "050407"}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
* goodbye
    - utter_goodbye
    
## chitchat_quit_task
* greet
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": "facility_form"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - facility_form
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - utter_continue  
* deny
    - form{"name": null}
    - utter_goodbye

