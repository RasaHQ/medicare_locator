## just chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_provider_types
    
## chitchat form 1
* greet
    - utter_greet
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot":"selected_type_slot"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_provider_types
* inform{"selected_type_slot": "rbry-mqwu"}
    - slot{"selected_type_slot": "rbry-mqwu"}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "city"}
* inform{"city": "san francisco"}
    - slot{"city": "san francisco"}
    - find_hospital
* inform{"selected_id": "050407"}
    - slot{"selected_id": "050407"}
    - find_healthcare_address
    - slot{"selected_address": "845 Jackson St, 94133, San Francisco"}
    - utter_address
* thank
    - utter_noworries 

