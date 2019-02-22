*** Settings ***
Library     Selenium2Library
Library     Collections
Library     ../python_methods/help_python_methods.py
Resource    ../data/variables.robot

Suite Setup     Precondiotions    ${URL}
Suite Teardown  Postconditions

*** Variables ***
${URL}      http://users.bugred.ru/user/login/index.html
${USERS_LIST}       chrome_users
${USERS_COUNT}    ${5}

*** Test Cases ***
Test REST Registration
   [Documentation]      This is a Registration test
   [Tags]               chrome

    Random Users Json   ${USERS_COUNT}
    :FOR   ${i}   IN RANGE    1    ${USERS_COUNT}+1
    \   ${user}=    get user from list    ${USERS_LIST}     user${i}
    \   create new user on website    ${user}

