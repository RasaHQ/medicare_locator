## Generated Story 3596572550729727581
* greet
    - utter_greet
* search_hospital{"type": "hospital"}
    - slot{"type": "hospital"}
    - slot{"type": "hospital"}
    - hospital_form   <!-- predicted: action_listen -->
    - form{"name": "hospital_form"}
    - slot{"requested_slot": "zip"}
    - slot{"zip": "10119"}
    - slot{"requested_slot": "specialty"}


## end-to-end story 2
* greet: hi
    - utter_greet   <!-- predicted: action_listen -->
* search_hospital: find me a nearby hospital
    - utter_ask_zip   <!-- predicted: action_listen -->
* inform: 
    - utter_found_hospitals   <!-- predicted: action_listen -->
    - utter_found_specialties   <!-- predicted: action_listen -->


## end-to-end story 1
* greet: hello
    - utter_greet   <!-- predicted: action_listen -->
* search_tratment_center: I need to find a treatment center
    - utter_ask_type   <!-- predicted: action_listen -->
* inform: 
    - utter_ask_zip   <!-- predicted: action_listen -->
* inform: 
    - utter_found_hospitals   <!-- predicted: action_listen -->
    - utter_found_specialties   <!-- predicted: action_listen -->


