*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Click Add New Link
    Click Link  Lisää uusi
    Add New Page Should Be Open

Click Front Page Link
    Click Link  Etusivu
    Starting Page Should Be Open
