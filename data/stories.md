## story_goodbye
* goodbye
 - utter_goodbye

## story_thankyou
* thankyou
 - utter_noworries

## hi
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
    
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
    

## Generated Story 8889143365291626450
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
    - find_hospital
* inform{"selected_id": 1824}
    - slot{"selected_id": 1824}
    - find_healthcare_address
    - slot{"selected_address": [["309 JACKSON STREET", "MONROE", "LA"]]}
    - utter_address
* thankyou
    - utter_noworries
    
    
## Generated Story 3596090009641184692
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 1}
    - slot{"selected_type_slot": 1}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "71201"}
    - form: hospital_form
    - slot{"zip": "71201"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
    - utter_found_hospitals
* inform{"selected_id": 1824}
    - slot{"selected_id": 1824}
    - find_healthcare_address
    - slot{"selected_address": [["309 JACKSON STREET", "MONROE", "LA"]]}
    - utter_address
* thankyou
    - utter_noworries
    
    
## Generated Story 7674029564932382471
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 2}
    - slot{"selected_type_slot": 2}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "77036"}
    - form: hospital_form
    - slot{"zip": "77036"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": 31960}
    - slot{"selected_id": 31960}
    - find_healthcare_address
    - slot{"selected_address": [["8700 COMMERCE PARK SUITE 239", "HOUSTON", "TX"]]}
    - utter_address
* thankyouyou
    - utter_noworries


## Generated Story 6282813005111987042
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]} 
* inform{"selected_type_slot": 3}
    - slot{"selected_type_slot": 3}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "75098"}
    - form: hospital_form
    - slot{"zip": "75098"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": 11259}
    - slot{"selected_id": 11259}
    - find_healthcare_address
    - slot{"selected_address": [["300 E BROWN ST", "WYLIE", "TX"]]}
    - utter_address
* thankyou
    - utter_noworries


## Generated Story 229878229825540836
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 1}
    - slot{"selected_type_slot": 1}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "75098"}
    - form: hospital_form
    - slot{"zip": "75098"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital


## Generated Story -1566701766864683675
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 1}
    - slot{"selected_type_slot": 1}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "99362"}
    - form: hospital_form
    - slot{"zip": "99362"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": 4504}
    - slot{"selected_id": 4504}
    - find_healthcare_address
    - slot{"selected_address": "1025 S SECOND AVE, WALLA WALLA, WA"}
    - utter_address
* thankyou
    - utter_noworries
* bye
    - utter_goodbye


## Generated Story -6867115558197069050
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 3}
    - slot{"selected_type_slot": 3}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "97030"}
    - form: hospital_form
    - slot{"zip": "97030"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": 10002}
    - slot{"selected_id": 10002}
    - find_healthcare_address
    - slot{"selected_address": "3457 NE DIVISION, GRESHAM, OR"}
    - utter_address
* thank
    - utter_noworries
* bye
    - utter_goodbye


## Generated Story -2270219906225362893
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 1}
    - slot{"selected_type_slot": 1}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "90806"}
    - form: hospital_form
    - slot{"zip": "90806"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform
* inform{"selected_id": 467}
    - slot{"selected_id": 467}
    - find_healthcare_address
    - slot{"selected_address": "2801 ATLANTIC AVE, LONG BEACH, CA"}
    - utter_address
* thank
    - utter_noworries
* bye
    - utter_goodbye


## Generated Story -6009271244998140385
* greet
    - utter_greet
    - find_provider_types
    - slot{"provider_types_slot": [[1, "HOSPITAL"], [2, "HOME HEALTH AGENCY"], [3, "Nursing Home"]]}
* inform{"selected_type_slot": 3}
    - slot{"selected_type_slot": 3}
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "91335"}
    - form: hospital_form
    - slot{"zip": "91335"}
    - form: followup{"name": "find_hospital"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": 8618}
    - slot{"selected_id": 8618}
    - find_healthcare_address
    - slot{"selected_address": "18855 VICTORY BL, RESEDA, CA"}
    - utter_address
* thank
    - utter_noworries
* bye
    - utter_goodbye


## Generated Story 2043303852060503113
* search_provider{"selected_type_slot": "1"}
    - slot{"selected_type_slot": "1"}
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

## Generated Story -2842815382131361445
* search_provider{"selected_type_slot": "1"}
    - slot{"selected_type_slot": "1"}
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
* inform{"selected_id": 4245}
    - slot{"selected_id": 4245}
    - find_healthcare_address
    - slot{"selected_address": "23900 KATY FREEWAY, KATY, TX"}
    - utter_address
* thank
    - utter_noworries

## Generated Story -9043472467572151351
* search_provider{"selected_type_slot": "1", "zip": "77494"}
    - slot{"selected_type_slot": "1"}
    - slot{"zip": "77494"}
    - hospital_form
    - form{"name": "hospital_form"}
    - form: followup{"name": "find_hospital"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": 4245}
    - slot{"selected_id": 4245}
    - find_healthcare_address
    - slot{"selected_address": "23900 KATY FREEWAY, KATY, TX"}
    - utter_address
* thank
    - utter_noworries

## Generated Story 6802955161856017335
* search_provider{"selected_type_slot": "3", "zip": "77494"}
    - slot{"selected_type_slot": "3"}
    - slot{"zip": "77494"}
    - hospital_form
    - form{"name": "hospital_form"}
    - form: followup{"name": "find_hospital"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - find_hospital
* inform{"selected_id": 18582}
    - slot{"selected_id": 18582}
    - find_healthcare_address
    - slot{"selected_address": "23553 WEST FERNHURST DRIVE, KATY, TX"}
    - utter_address
* thank
    - utter_noworries

