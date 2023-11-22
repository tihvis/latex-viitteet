*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add New Book Page

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

#Tässä otettu huomioon vain yksi keyword
Add Book With One Author And One Keyword And Valid Inputs Should Succeed
    Input Credentials  Esimerkki kirja  Esimerkki kirjailija  12345  2019  Otava
    Submit Citation
    Add Book Should Succeed


*** Keywords ***
Add Book Should Succeed
    Starting Page Should Be Open
    Page Should Contain  Lisäys onnistui

Add Book Should Fail With Message
    [Arguments]  ${message}
    Add New Page Should Be Open
    Page Should Contain  ${message}

Input Credentials
    [Arguments]  ${title}  ${author}  ${isbn}  ${year}  ${publisher}
    Input Text  name=title  ${title}
    Input Text  name=author  ${author}
    Input Text  name=isbn  ${isbn}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}



