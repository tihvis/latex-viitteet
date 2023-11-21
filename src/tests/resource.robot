*** Settings ***
Library  SeleniumLibrary
Library  ..//Library.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0.5 seconds
${HOME_URL}  http://${SERVER}

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --no-sandbox
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  ETUSIVU

Add New Page Should Be Open
    Title Should Be  Lisää uusi kirja (book)
