*** Settings ***
Library  OperatingSystem
Library  Collections
Library  /home/korbut/PycharmProjects/pet_store/api_requests/pet_store_api.py
Library  pet_store_api.Store  WITH NAME  Store
Library  /home/korbut/PycharmProjects/pet_store/helpers/parse_json_store_data.py

*** Variables ***
${pet_name}  Boris
${pet_id}  9222968140498034000
${pet_status}  available
${order_id}  10

*** Test Cases ***
Add new oder for purchasing pet
    [Documentation]  Add new order and check it

    ${add_order_post_response}  Store.store_post_requests  ${order_id}  ${pet_id}

    ${added_order_id}  Get Order Id  ${add_order_post_response}
    Should Be Equal  ${added_order_id}  ${${order_id}}

    ${added_order_pet_id}  Get Pet Id  ${add_order_post_response}
    Should Be Equal  ${added_order_pet_id}  ${${pet_id}}

    ${get_order_response}  Store.store_get_requests  order  ${added_order_id}
    ${order_id_from_get_order_response}  Get Order Id  ${get_order_response}
    ${pet_id_from_get_order_response}  Get Pet Id  ${get_order_response}
    Should Be Equal  ${order_id_from_get_order_response}  ${${order_id}}
    Should Be Equal  ${pet_id_from_get_order_response}  ${${pet_id}}

Delete new order
    [Documentation]  Add new order, delete and check it

    ${add_order_post_response}  Store.store_post_requests  ${order_id}  ${pet_id}

    ${delete_order_response}  Store.store_delete_requests  ${order_id}
    ${delete_order_message}  Get Order Message  ${delete_order_response}
    Should Be Equal  ${delete_order_message}  ${order_id}
