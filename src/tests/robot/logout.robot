*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Register And Login Test User

*** Test Cases ***
Click Logout Link On Starting Page Should Work
    Click Link  Kirjaudu ulos
    Starting Page Should Be Open
    Page Should Contain  Uloskirjautuminen onnistui!

Logout Should Succeed
    Click Link  Kirjaudu ulos
    Title Should Be  Latex-viitteet
    Page Should Contain  Kirjaudu sisään
    Page Should Contain  Rekisteröidy
    Page Should Not Contain  Lisää artikkeli
    Page Should Not Contain  Lisää kirja
    Page Should Not Contain  Lisää konferenssiartikkeli
    Page Should Not Contain  Hae lisäämäsi viitteet

After Logout User Should Not Be Able To Add Or View Citations
    Click Link  Kirjaudu ulos
    Go To Add New Book Page
    Page Should Contain  ${PLEASE_LOG_IN}
    Go To Add New Article Page
    Page Should Contain  ${PLEASE_LOG_IN}
    Go To Add New Inproceedings Page
    Page Should Contain  ${PLEASE_LOG_IN}
    Go To Citation List Page
    Page Should Contain  ${PLEASE_LOG_IN}

After Logout User Should Be Able To Login And Register New User
    Click Link  Kirjaudu ulos
    Starting Page Should Be Open
    Page Should Contain  Kirjaudu sisään
    Page Should Contain  Rekisteröidy
    
