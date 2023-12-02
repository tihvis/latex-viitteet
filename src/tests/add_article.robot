*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add New Article Page

*** Test Cases ***
Add Article With No Title Should Fail
    Set Authors  John Smith
    Set Journal  Journal
    Set Year  1990
    Set Volume  6
    Set Pages  40-43
    Submit Citation
    Add Citation Should Fail With Message  Artikkelin otsikon tulee olla 1-80 merkkiä pitkä.

Add Article With No Year Should Fail
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Volume  6
    Set Pages  42-44
    Submit Citation
    Add Citation Should Fail With Message  Vuosiluku ei kelpaa.

Add Article With No Author Should Fail
    Set Title  Sepon sienipaikat
    set Journal  Journal
    Set Year  1990
    Set Volume  6
    Set Pages  42-44
    Submit Citation
    Add Citation Should Fail With Message  Viitteeseen tulee lisätä vähintään yksi kirjailija.

Add Article With No Journal Should Fail
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    Set Year  2015
    Set Volume  10
    Set Pages  42-44
    Submit Citation
    Add Citation Should Fail With Message  Lehden nimen tulee olla 1-80 merkkiä pitkä.

Add Article With No Volume Should Fail
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Year  2013
    Set Pages  42-44
    Submit Citation
    Add Citation Should Fail With Message  Lehden numero ei kelpaa.

Add Article With No Pages Should Fail
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Year  2020
    Set Volume  6
    Submit Citation
    Add Citation Should Fail With Message  Ilmoita sivunumerot muodossa 38-42 tai 42.

# Add Article With Only First Name Of Author Should Fail
#     Set Title  Aapelin ankat
#     Set Authors  Kauko
#     Set Journal  Publisher
#     Set Year  1990
#     Set Volume  5
#     Set Pages  10-18
#     Submit Citation
#     Add Citation Should Fail With Message  Jokaisen kirjailijan nimessä tulee olla vähintään kaksi nimeä.

Add Already Existing Article Should Fail
    Set Title  Tuijan sienipiirakan ohje
    Set Authors  Tuija Sienestäjä
    set Journal  Journal
    Set Year  2020
    Set Volume  6
    Set Pages  100-102
    Submit Citation
    
    Starting Page Should Be Open
    Go To Add New Article Page
    Add New Article Page Should Be Open
    Set Title  Tuijan sienipiirakan ohje
    Set Authors  Tuija Sienestäjä
    set Journal  Journal
    Set Year  2020
    Set Volume  6
    Set Pages  100-102
    Submit Citation
    Add Citation Should Fail With Message  Kyseinen artikkeli on jo lisätty tietokantaan,    

Add Article With One Author And Valid Inputs Should Succeed
    Set Title  Martan marjapiirakan ohje
    Set Authors  Seppo Sienestäjä
    set Journal  Journal
    Set Year  2020
    Set Volume  6
    Set Pages  100-102
    Submit Citation
    Add Citation Should Succeed
    Starting Page Should Be Open
    
    Go To Citation List Page
    List All Citings Page Should Be Open
    Page Should Contain  Martan marjapiirakan ohje

Add Article With Multiple Authors And Valid Inputs Should Succeed
    Set Title  Keijon marjapiirakan ohje
    Set Authors  Keijo Sienestäjä  Marja Metsästäjä
    set Journal  Journal
    Set Year  1990
    Set Volume  6
    Set Pages  100-102
    Submit Citation
    Add Citation Should Succeed

    Go To Add New Article Page
    Set Title  Tarjan marjapiirakan ohje
    Set Authors  Tarja Sienestäjä  Tuija Metsästäjä  Seppo Sienestäjä
    set Journal  Journal
    Set Year  1995
    Set Volume  6
    Set Pages  10-11
    Submit Citation
    Add Citation Should Succeed

    Starting Page Should Be Open
    Go To Citation List Page
    List All Citings Page Should Be Open
    Page Should Contain  Keijon marjapiirakan ohje
    Page Should Contain  Tarjan marjapiirakan ohje
    
*** Keywords ***
Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}