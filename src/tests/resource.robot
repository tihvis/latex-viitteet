*** Settings ***
Library  SeleniumLibrary
Library  ../Library.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.01 seconds
${HOME_URL}  http://${SERVER}
${ADD_NEW_BOOK_URL}  http://${SERVER}/add_new_book
${CITATIONS_LIST_URL}  http://${SERVER}/list

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --no-sandbox
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Starting Page Should Be Open
    Title Should Be  Latex-viitteet

Add New Book Page Should Be Open
    Title Should Be  Lisää uusi kirja

List All Citings Page Should Be Open
    Title Should Be  Lisäämäsi viitteet 

Go To Starting Page
    Go To  ${HOME_URL}

Go To Add New Book Page
    Go To  ${ADD_NEW_BOOK_URL}

Go To Citation List Page
    Go To  ${CITATIONS_LIST_URL}

Set Authors
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set ISBN
    [Arguments]  ${isbn}
    Input Text  isbn  ${isbn}

Set Keywords
    [Arguments]  ${keywords}
    Input Text  keywords  ${keywords}

Submit Citation
    Click Button  Lisää