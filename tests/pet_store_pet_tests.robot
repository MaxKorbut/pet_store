*** Settings ***
Library  OperatingSystem
Library  Collections
Library  ../api_requests/pet_store_api.py
Library  pet_store_api.Pet  WITH NAME  Pet

Library  ../helpers/parse_json_pet_data.py
Library  ../resources/get_variable.py

Library  ../db/db_methods.py
Library  db_methods.PetTable  WITH NAME  PetTable

*** Test Cases ***
Add new pet
    [Documentation]  Add new pet, find him by id and check expected pet name and actual pet name
    ${pet_name}  Get Variable From Table  pet_name
    ${pet_id}  Get Variable From Table  pet_id
    ${pet_status}  Get Variable From Table  pet_status

    ${add_pet_response}  Pet.pet_post_requests  ${pet_id}  ${pet_name}  ${pet_status}
    ${added_pet_name}  Get Pet Name  ${add_pet_response}
    ${added_pet_id}  Get Pet Id  ${add_pet_response}

    ${get_new_pet_response}  Pet.pet_get_requests  id  ${added_pet_id}
    ${get_new_pet_name}  Get Pet Name  ${get_new_pet_response}
    Should Be Equal  ${pet_name}  ${get_new_pet_name}


Update pet status
    [Documentation]  Add new pet, update his status and check it
    ${pet_name}  Get Variable From Table  pet_name
    ${pet_id}  Get Variable From Table  pet_id
    ${pet_status}  Get Variable From Table  pet_status

    ${add_pet_response}  Pet.pet_post_requests  ${pet_id}  ${pet_name}  ${pet_status}
    ${added_pet_name}  Get Pet Name  ${add_pet_response}
    ${added_pet_id}  Get Pet Id  ${add_pet_response}
    ${added_pet_status}  Get Pet Status  ${add_pet_response}

    ${put_pet_response}  Pet.pet_put_requests  ${pet_id}  ${pet_name}  sold
    ${put_pet_status}  Get Pet Status  ${put_pet_response}
    Should Not Be Equal  ${added_pet_status}  ${put_pet_status}

Delete new pet
    [Documentation]  Add new pet, delete him and check it
    ${pet_name}  Get Variable From Table  pet_name
    ${pet_id}  Get Variable From Table  pet_id
    ${pet_status}  Get Variable From Table  pet_status

    ${add_pet_response}  Pet.pet_post_requests  ${pet_id}  ${pet_name}  ${pet_status}
    ${added_pet_id}  Get Pet Id  ${add_pet_response}

    ${delete_pet_response}  Pet.pet_delete_requests  ${added_pet_id}
    ${delete_pet_message}  Get Pet Message  ${delete_pet_response}
    Should Be Equal  ${added_pet_id}  ${${delete_pet_message}}
