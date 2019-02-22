*** Settings ***
Library     Selenium2Library
Library     Collections
Library     ../python_methods/help_python_methods.py
Resource    ../data/variables.robot

Suite Setup     Precondiotions    ${URL}    ${BROWSER}
Suite Teardown  Postconditions

*** Variables ***
${BROWSER}      firefox
${URL}      http://users.bugred.ru/user/login/index.html
${USERS_COUNT}    ${5}
${FILE_NAME}        firefox_users

*** Test Cases ***
Test REST Registration
   [Documentation]      This is a Registration test
   [Tags]               firefox

    Random Users Json   ${USERS_COUNT}   ${FILE_NAME}
    :FOR   ${i}   IN RANGE    1    ${USERS_COUNT}+1
    \   ${user}=    get user from list    ${FILE_NAME}     user${i}
    \   create new user on website    ${user}

