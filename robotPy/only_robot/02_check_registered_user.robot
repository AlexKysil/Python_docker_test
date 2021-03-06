*** Settings ***
Documentation    Suite description
Library     Selenium2Library
Library     Collections
Library     ../python_methods/help_python_methods.py
Resource    ../data/variables.robot

Suite Setup      Precondiotions  ${URL}
Suite Teardown   Postconditions

*** Variables ***
${URL}          http://users.bugred.ru/
${USERS_COUNT}   ${5}
${FILE_NAME}   chrome_users

*** Test Cases ***
Test user registered
    [Documentation]    This test check if user registered
    [Tags]             chrome

    :FOR  ${i}  IN RANGE   1   ${USERS_COUNT}+1
    \   ${user}=    get user from list    ${FILE_NAME}     user${i}
    \   ${USER_EMAIL}=  set user email  ${user}
    \   Check User Got Registered   ${USER_EMAIL}
