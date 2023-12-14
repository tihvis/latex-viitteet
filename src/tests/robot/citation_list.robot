*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Logout  Close Browser
Test Setup  Go To Citation List Page

*** Test Cases ***
Citation Amount Matches DB
    ${value}=  Get Value  id=hidden
    ${value_as_int}=  Convert To Integer  ${value}
    ${row_count}=  Execute Javascript  return document.querySelectorAll(".citations tbody tr").length
    Should Be Equal As Numbers  ${value_as_int}  ${row_count}

Link To BibTeX File Should Be Visible
    Page Should Contain  Lataa BibTeX-muodossa

Citations In Table Format Visible
    Page Should Contain Element  xpath=//table