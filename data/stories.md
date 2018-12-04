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
* thankyou
    - utter_noworries

## happy path 2
* greet
    - utter_greet
* search_hospital
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
* thankyou
    - utter_noworries
## happy path 3
* search_hospital{"zip":"10119"}
    - hospital_form

## happy path 4
* search_treatment_center
    - center_form
    - form{"name":"center_form"}
    - form{"name":null}
* thankyou
    - utter_noworries
## Generated Story -6770035372518111269
* greet
    - utter_greet
* search_hospital
    - hospital_form
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
* form: inform{"number": "10119"}
    - form: hospital_form
    - slot{"zip": "10119"}
    - slot{"requested_slot": "specialty"}

## Generated Story 851605932364523814
* search_treatment_center
    - center_form
    - form{"name": "center_form"}
    - action_listen
    - slot{"requested_slot": "zip"}
* form: inform
* form: inform{"number": "10119"}
    - center_form
    - slot{"zip": "10119"}
    - slot{"requested_slot": "type"}
* form: inform{"type": "nursery home"}
    - slot{"type": "nursery home"}
    - form: center_form
    - slot{"type": "nursery home"}
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -6797132430972190218
* search_treatment_center
    - center_form
    - form{"name": "center_form"}
    - action_listen
    - slot{"requested_slot": "zip"}
* form: inform
* form: inform{"number": "10119"}
    - center_form
    - action_listen
    - slot{"zip": "10119"}
    - slot{"requested_slot": "type"}
* form: inform
* form: inform{"type": "nursery home"}
    - slot{"type": "nursery home"}
    - center_form
    - slot{"type": "nursery home"}
    - form{"name": null}
    - slot{"requested_slot": null}

