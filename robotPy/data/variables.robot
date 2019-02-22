
*** Keywords ***
Precondiotions
    [Arguments]     ${URL}   ${BROWSER}= chrome
    Open Browser    ${URL}   ${BROWSER}
    Maximize Browser Window

Postconditions
    Close Browser

Check User Got Registered
    [Arguments]     ${USER_EMAIL}

    Input Text      //input[@name='q']      ${USER_EMAIL}
    Click Button    //button[@type='submit']
    Element Text Should Be      //table/tbody[@class='ajax_load_row']//td[1]    ${USER_EMAIL}