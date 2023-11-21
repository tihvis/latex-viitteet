*** Settings ***
Library  SeleniumLibrary
Library  ..//Library.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0.5 seconds
${ADD_NEW}  add_new
${HOME_URL}  http://${SERVER}
${ADD_NEW_URL}  http://${SERVER}/{ADD_NEW}

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --no-sandbox
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Starting Page Should Be Open
    Title Should Be  latex-viitteet

Add New Page Should Be Open
    Title Should Be  Lisää uusi kirja (book)

Go To Starting Page
    Go To  ${HOME_URL}

Go To Add New Page
    Go To  ${ADD_NEW_URL}
