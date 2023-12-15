*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Program Should Be Deployed
    Go To  ${DEPLOYED_HOME_URL}
    Title Should Be  Latex-viitteet
    Click Link  Kirjaudu sisään
    Title Should Be  Kirjaudu sisään
    Click Link  Etusivulle
    Click Link  Rekisteröidy
    Title Should Be  Luo uusi käyttäjätunnus

Deployed Citation Pages Should Be Accessible
    Go To  ${DEPLOYED_ADD_BOOK_URL}
    Page Should Contain  ${PLEASE_LOG_IN}
    Go To  ${DEPLOYED_ADD_ARTICLE_URL}
    Page Should Contain  ${PLEASE_LOG_IN}
    Go To  ${DEPLOYED_ADD_INPROCEEDINGS_URL}
    Page Should Contain  ${PLEASE_LOG_IN}
    Go To  ${DEPLOYED_CITATIONS_LIST_URL}
    Page Should Contain  ${PLEASE_LOG_IN}