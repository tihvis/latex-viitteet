*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Logout  Close Browser
Test Setup  Go To Add New Book Page

*** Test Cases ***
Add Book With No Title Should Fail
    Set Authors  John Smith
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Citation Should Fail With Message  Kirjan otsikon on oltava 1-80 merkkiä pitkä.

Add Book With No Author Should Fail
    Set Title  ABC ja muut aakkoset
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Citation Should Fail With Message  Viitteeseen tulee lisätä vähintään yksi kirjailija

Add Book With No Year Should Fail
    Set Title  Sallan salapaikat
    Set Authors  Salla Salainen
    Set Publisher  Aalto
    Submit Citation
    Add Citation Should Fail With Message  Vuosiluku ei kelpaa

Add Book With No Publisher Should Fail
    Set Title  Kaunon kukkapaikat
    Set Authors  Kauno Kukkamäki
    Set Year  1990
    Submit Citation
    Add Citation Should Fail With Message  Kustantajan nimen on oltava 2-40 merkkiä pitkä.

Add Already Existing Book Should Fail
     Set Title  ABC ja muut aakkoset
     Set Authors  Olli Opettaja
     Set Year  1990
     Set Publisher  Otava
     Submit Citation
     Add Citation Should Succeed

     Starting Page Should Be Open
     Go To Add New Book Page
     Add New Book Page Should Be Open
     Set Title  ABC ja muut aakkoset
     Set Authors  Olli Opettaja
     Set Year  1990
     Set Publisher  Otava
     Submit Citation
     Add Citation Should Fail With Message  Kyseinen kirja on jo lisätty tietokantaan

Add Book With One Author And Valid Inputs Should Succeed 
    Set Title  Esimerkki kirja kakkonen
    Set Authors  Esimerkki Kirjailija
    Set Year  2019
    Set Publisher  Otava
    Submit Citation
    Add Citation Should Succeed
    
    Starting Page Should Be Open
    Go To Citation List Page
    List All Citings Page Should Be Open
    Page Should Contain  Esimerkki kirja kakkonen

Add Book With Multiple Authors And Valid Inputs Should Succeed
    Set title  Esimerkki kirja kolmonen
    Set Authors  Eka Kirjailija  Toka Kirjailija
    Set Year  2022
    Set Publisher  Julkaisija
    Submit Citation
    Add Citation Should Succeed

    Go To Add New Book Page
    Set Title  Esimerkki kirja nelonen
    Set Authors  Eka Kirjailija  Toka Kirjailija  Kolmas Kirjailija
    Set Year  2022
    Set Publisher  Julkaisija
    Submit Citation
    Add Citation Should Succeed

    Starting Page Should Be Open
    Go To Citation List Page
    List All Citings Page Should Be Open
    Page Should Contain  Esimerkki kirja kolmonen
    Page Should Contain  Esimerkki kirja nelonen




