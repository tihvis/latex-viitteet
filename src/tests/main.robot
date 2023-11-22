*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Starting Page

*** Test Cases ***
Click Add New Book Link
    Click Link  Lisää kirja
    Add New Book Page Should Be Open

#Click Front Page Link  #linkki toistaiseksi pois käytöstä
#    Click Link  Etusivu
#    Starting Page Should Be Open
