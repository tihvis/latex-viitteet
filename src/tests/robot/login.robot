*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Logout If Logged In  Close Browser
Test Setup  Run Keywords  Logout If Logged In  Register First Test User

*** Test Cases ***
Click Login Link On Starting Page Should Work
    Click Link  Kirjaudu sisään
    Login Page Should Be Open

Login Should Succeed With Valid Credentials
    Click Link  Kirjaudu sisään
    Set Username  Testuser1
    Set Password  Testpassw0rd
    Click Button  Kirjaudu sisään
    Starting Page Should Be Open
    Page Should Contain  Sisäänkirjautuminen onnistui!

Login Should Fail Valid Username And Invalid Password
    Click Link  Kirjaudu sisään
    Set Username  Testuser1
    Set Password  testpassw0rD
    Click Button  Kirjaudu sisään
    Starting Page Should Be Open
    Page Should Contain  Sisäänkirjautuminen ei onnistunut.

Login With Non-Existing Username Should Fail
    Click Link  Kirjaudu sisään
    Set Username  Nonexisting.username
    Set Password  testPASSw0rd
    Click Button  Kirjaudu sisään
    Starting Page Should Be Open
    Page Should Contain  Sisäänkirjautuminen ei onnistunut.