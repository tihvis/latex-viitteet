*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Run Keywords  Go To Starting Page  Reset Application

*** Test Cases ***
Click Add New Book Link
    Click Link  Lisää kirja
    Add New Book Page Should Be Open

Click Add New Article Link
    Click Link  Lisää artikkeli
    Add New Article Page Should Be Open

Click Add New Inproceedings Link
    Click Link  Lisää konferenssiartikkeli
    Add New Inproceedings Page Should Be Open

Click List All Citations Link
    Click Link  Hae lisäämäsi viitteet
    List All Citings Page Should Be Open

