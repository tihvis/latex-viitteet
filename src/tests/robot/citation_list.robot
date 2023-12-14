*** Settings ***
Resource  resource.robot
Suite Setup  Run Keywords  Open And Configure Browser  Register First Test User
Suite Teardown  Run Keywords  Logout If Logged In  Close Browser
Test Setup  Go To Citation List Page

*** Test Cases ***
Citations In Table Format Visible
    Page Should Contain Element  xpath=//table

Citation Amount Matches DB
    ${value}=  Get Value  id=hidden
    ${value_as_int}=  Convert To Integer  ${value}
    ${row_count}=  Execute Javascript  return document.querySelectorAll(".citations tbody tr").length
    Should Be Equal As Numbers  ${value_as_int}  ${row_count}

Link To BibTeX File Should Be Visible
    Page Should Contain  Lataa BibTeX-muodossa

Users Will Only See Their Own Added Citations
    Logout If Logged In
    Click Link  Kirjaudu sisään
    Set Username  Testuser1
    Set Password  Testpassw0rd
    Click Button  Kirjaudu sisään
    Starting Page Should Be Open
    Add First Book Citation
    Add Second Book Citation
    Go To Citation List Page
    Page Should Contain  First Book Citation  Second Book Citation
    Page Should Not Contain  First Article Citation  First Inproceedings Citation
    Logout

    Register And Login Second Test User
    Add First Article Citation
    Add First Inproceedings Citation
    Go To Citation List Page
    Page Should Contain  First Article Citation  First Inproceedings Citation
    Page Should Not Contain  First Book Citation  Second Book Citation


*** Keywords ***
Register And Login Second Test User
    Go To Register Page
    Set Username  Testuser2
    Set Password  TESTpassw0RD
    Click Button  Rekisteröidy
    Go To Starting Page
    Click Link  Kirjaudu sisään
    Set Username  Testuser2
    Set Password  TESTpassw0RD
    Click Button  Kirjaudu sisään

Add First Book Citation
    Go To Add New Book Page
    Set Title  First Book Citation
    Set Authors  First Author  Second Author
    Set Year  2021
    Set Publisher  Publisher
    Submit Citation
    Add Citation Should Succeed

Add Second Book Citation
    Go To Add New Book Page
    Set Title  Second Book Citation
    Set Authors  Third Author
    Set Year  1990
    Set Publisher  Publisher
    Submit Citation
    Add Citation Should Succeed

Add First Article Citation
    Go To Add New Article Page
    Set Title  First Article Citation
    Set Authors  Fourth Author
    Set Journal  Journal
    Set Year  2000
    Set Volume  6
    Set Pages  100-102
    Submit Citation
    Add Citation Should Succeed

Add First Inproceedings Citation
    Go To Add New Inproceedings Page
    Set Title  First Inproceedings Citation
    Set Authors  Fifth Author
    Set Year  2001
    Set Booktitle  Conference
    Submit Citation
    Add Citation Should Succeed
