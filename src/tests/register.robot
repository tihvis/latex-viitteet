*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Logout If Logged In  Go To Register Page

*** Test Cases ***
Click Register Link On Starting Page Should Work
    Go To Starting Page
    Click Link  Rekisteröidy
    Register Page Should Be Open

Register With Valid Credentials Should Succeed
    Set Username  Testi.kayttaja
    Set Password  Testitesti1
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username Should Fail
    Set Username  Testi
    Set Password  Testitesti1
    Submit Credentials
    Registeration Should Fail With Message  Käyttäjätunnuksen on oltava 6-30 merkkiä pitkä.

Register With Too Long Username Should Fail
    Set Username  Testitestitestitestitestitestit
    Set Password  Testitesti1
    Submit Credentials
    Registeration Should Fail With Message  Käyttäjätunnuksen on oltava 6-30 merkkiä pitkä.

Register Too Short Password Should Fail
    Set Username  Testi.kayttaja
    Set Password  testi1
    Submit Credentials
    Registeration Should Fail With Message  Salasanan on oltava 8-30 merkkiä pitkä.

Register With Too Long Password Should Fail
    Set Username  Testi.kayttaja
    Set Password  Testitestitestitestitestitestit1
    Submit Credentials
    Registeration Should Fail With Message  Salasanan on oltava 8-30 merkkiä pitkä.

Register With Weak Password Should Fail
    Set Username  Testi.kayttaja
    Set Password  salasana
    Submit Credentials
    Registeration Should Fail With Message  Salasanan tulee sisältää vähintään yksi pieni kirjain, yksi iso kirjain sekä yksi numero.

    Go To Register Page
    Set Username  Testi.kayttaja
    Set Password  Salasana
    Submit Credentials
    Registeration Should Fail With Message  Salasanan tulee sisältää vähintään yksi pieni kirjain, yksi iso kirjain sekä yksi numero.

    Go To Register Page
    Set Username  Testi.kayttaja
    Set Password  s4lasana
    Submit Credentials
    Registeration Should Fail With Message  Salasanan tulee sisältää vähintään yksi pieni kirjain, yksi iso kirjain sekä yksi numero.

Register With Existing Username Should Fail
    Set Username  Testi.kayttaja2
    Set Password  S4lasana
    Submit Credentials
    Registration Should Succeed

    Go To Register Page
    Set Username  Testi.kayttaja
    Set Password  S4lasana2Invalid
    Submit Credentials
    Registeration Should Fail With Message  Käyttäjätunnus on jo olemassa, kokeile rekisteröitymistä toisella käyttäjätunnuksella.

    Go To Register Page
    Set Username  testi.KAYTTAJA
    Set Password  S4lasana1
    Submit Credentials
    Registeration Should Fail With Message  Käyttäjätunnus on jo olemassa, kokeile rekisteröitymistä toisella käyttäjätunnuksella.        

*** Keywords ***
Registration Should Succeed
    Starting Page Should Be Open
    Page Should Contain  Rekisteröityminen onnistui, voit nyt kirjautua sisään!

Registeration Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Rekisteröidy