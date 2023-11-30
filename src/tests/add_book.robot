*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add New Book Page

*** Test Cases ***
Add Book With No Title
    Set Authors  John Smith
    #Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Kirjan otsikon tulee olla 1-80 merkkiä pitkä.

Add Book With Too Long Title
    Set Title  Aaaaaa aaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    Set Authors  John Smith
    #Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Kirjan otsikon tulee olla 1-80 merkkiä pitkä.

#Tähän puuttuu tarkistus validator-modulissa
#Add Book With Only First Name Of Author
#    Set Title  Aapelin ankat
#    Set Authors  Kauko
    #Set ISBN  999-99999
#    Set Year  1990
#    Set Publisher  Otava
#    Submit Citation
#    Add Book Should Fail With Message  Jokaisen kirjailijan nimessä tulee olla vähintään kaksi nimeä

#Add Book With Too Short ISBN
#    Set Title  Maijan mansikkapaikka
#    Set Authors  Maija Mehiläinen
    #Set ISBN  99
#    Set Year  1990
#    Set Publisher  Otava
#    Submit Citation
#    Add Book Should Fail With Message  ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.

#Add Book With Too Long ISBN
#    Set Title  Kallen kalapaikat
#    Set Authors  Kalle Kalastaja
#    Set ISBN  999-999999999999999999
#    Set Year  1990
#    Set Publisher  Otava
#    Submit Citation
#    Add Book Should Fail With Message  ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.

#Add Book With Invalid ISBN
#    Set Title  Pirjon mustikka-apajat
#    Set Authors  Pirjo Pirreli
#    Set ISBN  a4gg-22
#    Set Year  1990
#    Set Publisher  Otava
#    Submit Citation
#    Add Book Should Fail With Message  ISBN-koodin tulee olla 5-17 merkkiä pitkä, ja koostua vain numeroista ja viivoista.

Add Book With Invalid Year
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    #Set ISBN  999-99999
    Set Year  -500
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Vuosiluku ei kelpaa.

Add Book With Too Short Publisher
    Set Title  Kaunon kukkapaikat
    Set Authors  Kauno Kukkamäki
    #Set ISBN  999-99998
    Set Year  1990
    Set Publisher  j
    Submit Citation
    Add Book Should Fail With Message  Kustantajan nimen tulee olla 2-40 merkkiä pitkä.

Add Book With Too Long Publisher
    Set Title  Sallan salapaikat
    Set Authors  Salla Salainen
    #Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Aalto & Tuuli & Laine & Myrsky & Kaatosade
    Submit Citation
    Add Book Should Fail With Message  Kustantajan nimen tulee olla 2-40 merkkiä pitkä.

Add Book With No Author
    Set Title  ABC ja muut aakkoset
    #Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Viitteeseen tulee lisätä vähintään yksi kirjailija

Add Book With No Year
    Set Title  Sallan salapaikat
    Set Authors  Salla Salainen
    #Set ISBN  999-99999
    Set Publisher  Aalto
    Submit Citation
    Add Book Should Fail With Message  Vuosiluku ei kelpaa

Add Book With No Publisher
    Set Title  Kaunon kukkapaikat
    Set Authors  Kauno Kukkamäki
    #Set ISBN  999-99998
    Set Year  1990
    Submit Citation
    Add Book Should Fail With Message  Kustantajan nimen tulee olla 2-40 merkkiä pitkä.

# Add Already Existing Book
#     Set Title  ABC ja muut aakkoset
#     Set Authors  Olli Opettaja
#     Set ISBN  999-99999
#     Set Year  1990
#     Set Publisher  Otava
#     Submit Citation
#     Add Book Should Fail With Message  Viite on jo lisätty

#tämä testi feilaa lokaalisti, koska on jo tietokannassa
Add Book With One Author And Valid Inputs Should Succeed 
    Set Title  Esimerkki kirja kakkonen
    Set Authors  Esimerkki Kirjailija
    #Set ISBN  12345
    Set Year  2019
    Set Publisher  Otava
    Submit Citation
    Add Book Should Succeed

#tämä testi feilaa lokaalisti, koska on jo tietokannassa
Add Book With Valid Credentials
    Set Title  ABC ja niiden frendit
    Set Authors  Olli Opettaja
    #Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Succeed


*** Keywords ***
Add Book Should Succeed
    Starting Page Should Be Open
    Page Should Contain  Lisäys onnistui

Add Book Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}




