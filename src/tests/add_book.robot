*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Add New Book Page

*** Test Cases ***
Add Book With Too Short Title
    Set Title  ABC
    Set Authors  John Smith
    Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Kirjan nimi on liian lyhyt
    #testi menee läpi

Add Book With Too Long Title
    Set Title  ABC ja kaikki muut maailman aakkoset, jotka eivät mahdu kirjan nimeen
    Set Authors  John Smith
    Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Kirjan nimi on liian pitkä
    #testi menee läpi

Add Book With Only First Name Of Author
    Set Title  Aapelin ankat
    Set Authors  Kauko
    Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Kirjailijan sukunimi puuttuu
    #testi meni ensin läpi, mutta aiheutti myöhemmin ongelmia, korjattava koodissa

Add Book With Too Short ISBN
    Set Title  Maijan mansikkapaikka
    Set Authors  Maija Mehiläinen
    Set ISBN  99
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  ISBN-numero on liian lyhyt
    #testi menee läpi

Add Book With Too Long ISBN
    Set Title  Kallen kalapaikat
    Set Authors  Kalle Kalastaja
    Set ISBN  999-999999999999999999
    Set Year  1990
    Set Publisher  "Otava"
    Submit Citation
    Add Book Should Fail With Message  ISBN-numero on liian pitkä
    #testi menee läpi

Add Book With Invalid Year
    Set Title  Sepon sienipaikat
    Set Authors  Seppo Sienestäjä
    Set ISBN  999-99999
    Set Year  -500
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Vuosiluku ei kelpaa
    #korjataan koodissa

Add Book With Too Short Publisher
    Set Title  Kaunon kukkapaikat
    Set Authors  Kauno Kukkamäki
    Set ISBN  999-99998
    Set Year  1990
    Set Publisher  O
    Submit Citation
    Add Book Should Fail With Message  Kustantajan nimi on liian lyhyt
    #korjataan koodissa

Add Book With Too Long Publisher
    Set Title  Sallan salapaikat
    Set Authors  Salla Salainen
    Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Aalto & Tuuli & Laine & Myrsky & Kaatosade
    Submit Citation
    Add Book Should Fail With Message  Kustantajan nimi liian pitkä
    #korjataan koodissa

Add Book With Valid Credentials
    Set Title  ABC ja muut aakkoset
    Set Authors  Olli Opettaja
    Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Succeed

Add Already Existing Book
    Set Title  ABC ja muut aakkoset
    Set Authors  Olli Opettaja
    Set ISBN  999-99999
    Set Year  1990
    Set Publisher  Otava
    Submit Citation
    Add Book Should Fail With Message  Viite on jo lisätty

Add Book With Missing Compulsory Inputs
#...

#Tässä otettu huomioon vain yksi keyword
Add Book With One Author And One Keyword And Valid Inputs Should Succeed
    Input Credentials  Esimerkki kirja  Esimerkki kirjailija  12345  2019  Otava
    Submit Citation
    Add Book Should Succeed


*** Keywords ***
Add Book Should Succeed
    Starting Page Should Be Open
    Page Should Contain  Lisäys onnistui

Add Book Should Fail With Message
    [Arguments]  ${message}
    Add New Book Page Should Be Open
    Page Should Contain  ${message}

Input Credentials
    [Arguments]  ${title}  ${author}  ${isbn}  ${year}  ${publisher}
    Input Text  name=title  ${title}
    Input Text  name=author  ${author}
    Input Text  name=isbn  ${isbn}
    Input Text  name=year  ${year}
    Input Text  name=publisher  ${publisher}



