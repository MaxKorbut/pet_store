*** Settings ***
Library  OperatingSystem
Library  Collections
Library  /home/korbut/PycharmProjects/pet_store/api_requests/pet_store_api.py
Library  pet_store_api.User  WITH NAME  User
Library  /home/korbut/PycharmProjects/pet_store/helpers/parse_json_user_data.py

*** Variables ***
${user_id}  9222968140498
${username}  Max_K
${firstname}  Max
${lastname}  Korbut
${email}  max@mail.com
${passwd}  1111
${user_phone_number}  +375 29 111-11-11
${new_email}  kkk@mail.net

*** Test Cases ***
Add new user
    [Documentation]  Add new user and find him by username

    ${add_user_post_response}  User.user_post_requests  ${user_id}  ${username}  ${firstname}  ${lastname}  ${email}  ${passwd}  ${user_phone_number}
    ${user_add_message}  Get User Message  ${add_user_post_response}
    Should Be Equal  ${user_add_message}  ${user_id}

    ${user_get_response}  User.user_get_requests  ${username}
    ${added_user_id}  Get User Id  ${user_get_response}
    Should Be Equal  ${added_user_id}  ${${user_id}}

Update user email
    [Documentation]  Add new user, login by new user, update his email, check it and logout

    ${add_user_post_response}  User.user_post_requests  ${user_id}  ${username}  ${firstname}  ${lastname}  ${email}  ${passwd}  ${user_phone_number}
    ${user_add_message}  Get User Message  ${add_user_post_response}
    Should Be Equal  ${user_add_message}  ${user_id}

    ${login_user}  User.get_login_user_requests  ${username}  ${passwd}

    ${user_put_response}  User.user_put_requests  ${user_id}  ${username}  ${firstname}  ${lastname}  ${new_email}  ${passwd}  ${user_phone_number}
    ${put_user_get_response}  User.user_get_requests  ${username}
    ${email_from_get_response}  Get User Email  ${put_user_get_response}
    Should Be Equal  ${new_email}  ${email_from_get_response}

Delete user
    [Documentation]  Add new user, login by new user and delete he

    ${add_user_post_response}  User.user_post_requests  ${user_id}  ${username}  ${firstname}  ${lastname}  ${email}  ${passwd}  ${user_phone_number}
    ${user_add_message}  Get User Message  ${add_user_post_response}
    Should Be Equal  ${user_add_message}  ${user_id}

    ${login_user}  User.get_login_user_requests  ${username}  ${passwd}

    ${user_delete_response}  User.user_delete_requests  ${username}
    ${user_delete_message}  Get User Message  ${user_delete_response}
    Should Be Equal  ${user_delete_message}  ${username}
