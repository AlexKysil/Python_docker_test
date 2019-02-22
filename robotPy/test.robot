*** Variables ***
${status}=  Fail

*** Test Cases ***
Test title
    log     ${status}
    run keyword if    '${status}' == 'fail'    Fail  bitch

