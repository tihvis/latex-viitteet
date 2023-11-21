*** Settings ***
Resource  resource.robot
Suit Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Click Add New Link
    Click Link Add New
    Add New Page Should Be Open
