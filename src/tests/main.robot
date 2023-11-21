*** Settings ***
Resource  resource.robot
Suit Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Go To Starting Page
    Main Page Should Be Open
