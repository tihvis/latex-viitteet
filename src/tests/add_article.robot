*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add New Article Page

*** Test Cases ***
Add Article With No Title
    Set Authors  John Smith
    Set Journal  Journal
    Set Year  1990
    Set Volume  6
    Set Pages  40-43
    Submit Citation
    Add Article Should Fail With Message  Artikkelin otsikon tulee olla 1-80 merkkiä pitkä.

Add Article With Too Long Title
    Set Title  Aaaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    Set Authors  John Smith
    Set Journal  Journal
    Set Year  1990
    Set Volume  6
    Set Pages  42-44
    Submit Citation
    Add Article Should Fail With Message  Artikkelin otsikon tulee olla 1-80 merkkiä pitkä.

Add Article With Invalid Year
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Year  -500
    Set Volume  6
    Set Pages  42-44
    Submit Citation
    Add Article Should Fail With Message  Vuosiluku ei kelpaa.

Add Article With No Year
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Volume  6
    Set Pages  42-44
    Submit Citation
    Add Article Should Fail With Message  Vuosiluku ei kelpaa.

Add Article With No Author
    Set Title  Sepon sienipaikat
    set Journal  Journal
    Set Year  1990
    Set Volume  6
    Set Pages  42-44
    Submit Citation
    Add Article Should Fail With Message  Viitteeseen tulee lisätä vähintään yksi kirjailija.

Add Article With No Journal
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    Set Year  2015
    Set Volume  10
    Set Pages  42-44
    Submit Citation
    Add Article Should Fail With Message  Lehden nimen tulee olla 1-80 merkkiä pitkä.

Add Article With No Volume
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Year  2013
    Set Pages  42-44
    Submit Citation
    Add Article Should Fail With Message  Lehden numero ei kelpaa.

Add Article With No Pages
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Year  2020
    Set Volume  6
    Submit Citation
    Add Article Should Fail With Message  Ilmoita sivunumerot muodossa 38-42 tai 42.

Add Article With Valid Inputs Should Succeed
    Set Title  Martan marjapiirakan ohje
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Year  2020
    Set Volume  6
    Set Pages  100-102
    Submit Citation
    Add Article Should Succeed

    Go To Starting Page
    Starting Page Should Be Open
    Go To Citation List Page
    List All Citings Page Should Be Open
    Page Should Contain  Martan Marjapiirakka
    

*** Keywords ***
Add Article Should Succeed
    Starting Page Should Be Open
    Page Should Contain  Lisäys onnistui

Add Article Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
