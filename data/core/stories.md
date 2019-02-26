## story_goodbye
* goodbye
 - utter_goodbye

## story_thankyou
* thankyou
 - utter_noworries

## hi
* greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}

## new form story 1
* greet
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot":"selected_type_slot"}
* inform{"selected_type_slot":1}
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - slot{"requested_slot":"city"}
* inform{"selected_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
    
    
## Generated Story -4480193758190304006
* greet
    - find_provider_types
    - slot{"provider_types_slot": {"home_health": {"name": "Home Health Agency", "resource": "9wzi-peqs"}, "hospital": {"name": "hospital", "resource": "rbry-mqwu"}, "nursing_home": {"name": "nursing home", "resource": "b27b-2uc7"}}}
* inform{"selected_type_slot": "9wzi-peqs"}
    - slot{"selected_type_slot": "9wzi-peqs"}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "austin"}
    - slot{"city": "austin"}
    - form: hospital_form
    - slot{"city": "austin"}
    - form: followup{"name": "find_hospital"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": "747604"}
    - slot{"selected_id": "747604"}
    - find_healthcare_address
    - slot{"selected_address": "1508 Dessau Ridge Lane, Suite # 705, 78754, Austin"}
    - utter_address
* thank
    - utter_noworries
    
## Generated Story -5318182399020957170
* search_provider{"city": "Austin", "selected_type_slot": "rbry-mqwu"}
    - slot{"city": "Austin"}
    - slot{"selected_type_slot": "rbry-mqwu"}
    - find_hospital
* inform{"selected_id": "450871"}
    - slot{"selected_id": "450871"}
    - find_healthcare_address
    - slot{"selected_address": "3003 Bee Caves Road, 78746, Austin"}
    - utter_address
* thank
    - utter_noworries
    

