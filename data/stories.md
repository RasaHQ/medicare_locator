## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_noworries

## hi
* greet
 - utter_greet

## happy path
* search_hospital
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - find_hospital
* thankyou
    - utter_noworries

## happy path 2
* greet
    - utter_greet
    - find_provider_types
* search_hospital
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
    - find_hospital
    - utter_found_hospitals
* thankyou
    - utter_noworries
    
    
## happy path 3
* greet
    - utter_greet
    - find_provider_types
* search_hospital
    - hospital_form
    - slot{"requested_slot":"zip"}
* inform{"number":"77494"}
    - hospital_form
    - slot{"zip":"77494"}
    - slot{"requested_slot":null}
    - find_hospital
    - slot{"hospitals":[["MEMORIAL HERMANN KATY HOSPITAL"],["SPANISH MEADOWS NURSING & REHAB"],["THE GRACE CARE CENTER OF KATY"],["HEALING HANDS HEALTHCARE"],["HUCKEYE HEALTH SERVICES, LLC"],["MIRACLE NURSES HEALTHCARE SERVICES INC"],["PATHFINDER HOME HEALTH"],["SANCTIFIED HOME HEALTH SERVICES INC"],["YOUR QUALITY REHAB INC"]]}
    - utter_found_hospitals
* thank
    - utter_noworries

