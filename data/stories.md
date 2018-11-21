## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks

## hi
* greet
 - utter_greet

## happy path
* request_hospital
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
* thankyou
    - utter_noworries

## happy path 2
* greet
    - utter_greet
* request_hospital
    - hospital_form
    - form{"name": "hospital_form"}
    - form{"name": null}
* thankyou
    - utter_noworries
