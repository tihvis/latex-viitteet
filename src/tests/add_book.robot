*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add New Page

*** Test Cases ***
Add Book With Too Short Title
#...

Add Book With Too Long Title
#...

Add Book With Only First Name Of Author
#...

Add Book With Too Short ISBN
#...

Add Book With Too Long ISBN
#...

Add Book With Invalid Year
#...

Add Book With Too Short Publisher
#...

Add Book With Too Long Publisher
#...

Add Already Existing Book
#...

Add Book With Missing Compulsory Inputs
#...

Add Book With Valid Inputs
#...


*** Keywords ***
Add Book Should Succeed
    Starting Page Should Be Open
    #flash viestin tarkistus tähän?

Add Book Should Fail With Message
    [Arguments]  ${message}
    Add New Page Should Be Open
    Page Should Contain  ${message}



