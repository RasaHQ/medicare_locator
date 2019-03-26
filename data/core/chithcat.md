## just chitchat
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_facility_types
    
## chitchat form 1
* greet
    - utter_greet
    - facility_form
    - form{"name": "facility_form"}
    - slot{"requested_slot":"facility_type"}
* ask_weather OR ask_builder OR ask_howdoing OR ask_whoisit OR ask_isbot OR ask_howold OR ask_restaurant OR ask_time OR ask_wherefrom OR ask_whoami OR handleinsult OR nicetomeeyou OR telljoke OR ask_whatismyname OR howwereyoubuilt
    - action_chitchat
    - find_facility_types
* inform{"facility_type": "rbry-mqwu"}
    - slot{"facility_type": "rbry-mqwu"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"requested_slot": "city"}
* inform{"city": "san francisco"}
    - slot{"city": "san francisco"}
    - find_facilities
* inform{"facility_id": "050407"}
    - slot{"facility_id": "050407"}
    - find_healthcare_address
    - slot{"facility_address": "845 Jackson St, 94133, San Francisco"}
    - utter_address
* thankyou
    - utter_noworries 

