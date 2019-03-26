## story_goodbye
* goodbye
 - utter_goodbye

## story_thankyou
* thankyou
 - utter_noworries

## hi
* greet
    - find_facility_types
    - slot{"facility_type": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}

## new facility_form story
* greet
    - facility_form
    - form{"name": "facility_form"}
    - slot{"requested_slot":"facility_type"}
* inform{"facility_type":1}
    - facility_form
    - form{"name": "facility_form"}
    - form{"name": null}
    - slot{"requested_slot":"city"}
* inform{"facility_id":4245}
    - find_healthcare_address
    - utter_address
* thankyou
    - utter_noworries
    
    
## Generated Story -4480193758190304006
* greet
    - find_facility_types
    - slot{"facility_types": {"home_health": {"name": "Home Health Agency", "resource": "9wzi-peqs"}, "hospital": {"name": "hospital", "resource": "rbry-mqwu"}, "nursing_home": {"name": "nursing home", "resource": "b27b-2uc7"}}}
* inform{"facility_type": "9wzi-peqs"}
    - slot{"facility_type": "9wzi-peqs"}
    - facility_form
    - form{"name": "facility_form"}
    - slot{"requested_slot": "city"}
* form: inform{"city": "austin"}
    - slot{"city": "austin"}
    - form: facility_form
    - slot{"city": "austin"}
    - form: followup{"name": "find_facilities"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_facilities
* inform{"facility_id": "747604"}
    - slot{"facility_id": "747604"}
    - find_healthcare_address
    - slot{"facility_address": "1508 Dessau Ridge Lane, Suite # 705, 78754, Austin"}
    - utter_address
* thankyou
    - utter_noworries
    
## Generated Story -5318182399020957170
* search_provider{"city": "Austin", "facility_type": "rbry-mqwu"}
    - slot{"city": "Austin"}
    - slot{"facility_type": "rbry-mqwu"}
    - find_facilities
* inform{"facility_id": "450871"}
    - slot{"facility_id": "450871"}
    - find_healthcare_address
    - slot{"facility_address": "3003 Bee Caves Road, 78746, Austin"}
    - utter_address
* thankyou
    - utter_noworries
