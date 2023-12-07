*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Login Page

*** Test Cases ***
Login With Valid Credentials Should Succeed
    Set Username  Testuser
    Set Password  Testpassword1
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Username  Testuser
    Set Password  Testpassword222
    Submit Credentials
    Login Should Fail With Message  Sisäänkirjautuminen ei onnistunut.

Login With Nonexistent Username
    Set Username  Missing
    Set Password  Testpassword1
    Submit Credentials
    Login Should Fail With Message  Sisäänkirjautuminen ei onnistunut.



*** Keywords ***
Login Should Succeed
    Starting Page Should Be Open
    Page Should Contain  Sisäänkirjautuminen onnistui!

Login Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Kirjaudu sisään