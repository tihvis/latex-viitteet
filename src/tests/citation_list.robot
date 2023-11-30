*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Citation List Page

*** Test Cases ***
Citation Amount Matches DB
    ${actual_value}=  Get Element Attribute  xpath=//input  attribute=value
    Page Should Contain Element  name:amount  limit=${actual_value}

Link To BibTeX File Should Be Visible
    Page Should Contain  Lataa BibTeX-muodossa