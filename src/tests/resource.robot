*** Settings ***
Library  SeleniumLibrary
Library    ../Library.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.01 seconds
${HOME_URL}  http://${SERVER}
${REGISTER_URL}  http://${SERVER}/register
${LOGIN_URL}  http://${SERVER}/login
${ADD_NEW_BOOK_URL}  http://${SERVER}/add_new_book
${ADD_NEW_ARTICLE_URL}  http://${SERVER}/add_new_article
${ADD_NEW_INPROCEEDINGS_URL}  http://${SERVER}/add_new_inproceedings
${CITATIONS_LIST_URL}  http://${SERVER}/list

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --no-sandbox
    Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}
    Register And Login Test User

Starting Page Should Be Open
    Title Should Be  Latex-viitteet

Add New Book Page Should Be Open
    Title Should Be  Lisää uusi kirja

Add New Article Page Should Be Open
    Title Should Be  Lisää uusi artikkeli

Add New Inproceedings Page Should Be Open
    Title Should Be  Lisää uusi konferenssiartikkeli

List All Citings Page Should Be Open
    Title Should Be  Lisäämäsi viitteet 

Register Page Should Be Open
    Title Should Be  Luo uusi käyttäjätunnus

Login Page Should Be Open
    Title Should Be  Kirjaudu sisään

Go To Starting Page
    Go To  ${HOME_URL}

Go To Add New Book Page
    Go To  ${ADD_NEW_BOOK_URL}

Go To Add New Article Page
    Go To  ${ADD_NEW_ARTICLE_URL}

Go To Add New Inproceedings Page
    Go To  ${ADD_NEW_INPROCEEDINGS_URL}

Go To Citation List Page
    Go To  ${CITATIONS_LIST_URL}

Go To Register Page
    Go To  ${REGISTER_URL}

Go To Login Page
    Go To  ${LOGIN_URL}

Set Authors
    [Arguments]    @{authors}
    FOR  ${author}  IN  @{authors}
        Input Text  author  ${author}
    END

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Keywords
    [Arguments]  ${keywords}
    Input Text  keywords  ${keywords}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}

Set Booktitle
    [Arguments]  ${booktitle}
    Input Text  booktitle  ${booktitle}

Submit Citation
    Click Button  Lisää

Add Citation Should Succeed
    Starting Page Should Be Open
    Page Should Contain  Lisäys onnistui

Add Citation Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Register And Login Test User
    Go To Register Page
    Set Username  Testuser
    Set Password  Testpassword1
    Click Button  Rekisteröidy

    Go To Login Page
    Set Username  Testuser
    Set Password  Testpassword1
    Click Button  Kirjaudu sisään
    Go To Starting Page

Logout
    Go To Starting Page
    Click Link  Kirjaudu ulos

Logout If Logged In
    Go To Starting Page
    ${logged_in} =  Run Keyword And Return Status  Page Should Contain  Kirjaudu ulos
    Run Keyword If  ${logged_in}  Logout
    Go To Starting Page
