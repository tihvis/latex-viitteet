*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add New Book Page

*** Test Cases ***
Add Book With Too Short Title
    Set Title  "ABC"
    Set Authors  "John Smith"
    Set ISBN  "999-99999"
    Set Year  1990
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  Kirjan nimi on liian lyhyt

Add Book With Too Long Title
    Set Title  "ABC"
    Set Authors  "John Smith"
    Set ISBN  "999-99999"
    Set Year  1990
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  eitoimi

Add Book With Only First Name Of Author
    Set Title  "ABC"
    Set Authors  "John"
    Set ISBN  "999-99999"
    Set Year  1990
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  eitoimi

Add Book With Too Short ISBN
    Set Title  "ABC ja muut aakkoset"
    Set Authors  "John Smith"
    Set ISBN  "99"
    Set Year  1990
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  eitoimi

Add Book With Too Long ISBN
Set Title  "ABC"
    Set Authors  "John Smith"
    Set ISBN  "999-999999999999999999"
    Set Year  1990
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  eitoimi

Add Book With Invalid Year
    Set Title  "ABC"
    Set Authors  "John Smith"
    Set ISBN  "999-99999"
    Set Year  -500
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  eitoimi

Add Book With Too Short Publisher
    Set Title  "ABC"
    Set Authors  "John Smith"
    Set ISBN  "999-99999"
    Set Year  1990
    Set Publisher  "O"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  eitoimi

Add Book With Too Long Publisher
    Set Title  "ABC"
    Set Authors  "John Smith"
    Set ISBN  "999-99999"
    Set Year  1990
    Set Publisher  "Aalto & Tuuli & Laine & Myrsky & Kaatosade"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  "eitoimi"

Add Book With Valid Credentials
    Set Title  "ABC ja muut aakkoset"
    Set Authors  "John Smith"
    Set ISBN  "999-99999"
    Set Year  1990
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Succeed

Add Already Existing Book
    Set Title  "ABC ja muut aakkoset"
    Set Authors  "John Smith"
    Set ISBN  "999-99999"
    Set Year  1990
    Set Publisher  "Otava"
    #Input Credentials
    Submit Citation
    Add Book Should Fail With Message  "on jo"

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
    Add New Book Page Should Be Open
    Page Should Contain  ${message}

Input Credentials
    [Arguments]  ${title}  ${author}  ${isbn}  ${year}  ${publisher}
    Input Text  name=title  ${title}
    Input Text  name=author  ${author}
    Input Text  name=isbn  ${isbn}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}



