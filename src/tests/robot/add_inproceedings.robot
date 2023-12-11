*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Run Keywords  Logout  Close Browser
Test Setup  Go To Add New Inproceedings Page

*** Test Cases ***
Add Inproceedings With No Title Should Fail
    Set Authors  John Smith
    Set Year  1990
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Fail With Message  Artikkelin otsikon tulee olla 1-80 merkkiä pitkä.

Add Inproceedings With No Authors Should Fail
    Set Title  Otsikko
    Set Year  2020
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Fail With Message  Viitteeseen tulee lisätä vähintään yksi kirjailija.

Add Inproceedings With No Year Should Fail
    Set Title  Otsikko
    Set Authors  John Smith
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Fail With Message  Vuosiluku ei kelpaa.

Add Inproceedings With No Booktitle Should Fail
    Set Title  Aapelin ankat
    Set Authors  Kauko Matkaaja
    Set Year  2020
    Submit Citation
    Add Citation Should Fail With Message  Julkaisun nimen tulee olla 2-40 merkkiä pitkä.

# Add Inproceedings With Only First Name Of Author Should Fail
#     Set Title  Aapelin ankat
#     Set Authors  Kauko
#     Set Year  2020
#     Set Booktitle  Konferenssi
#     Submit Citation
#     Add Citation Should Fail With Message  Jokaisen kirjailijan nimessä tulee olla vähintään kaksi nimeä.

Add Already Existing Inproceedings Should Fail
    Set Title  Kolmas lisäys
    Set Authors  John Smith
    Set Year  2021
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Succeed

    Go To Add New Inproceedings Page
    Set Title  Kolmas lisäys
    Set Authors  John Smith
    Set Year  2021
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Fail With Message  Kyseinen konferenssiartikkeli on jo lisätty tietokantaan

Add Inproceeding With One Author And Valid Inputs Should Succeed
    Set Title  Onnistunut lisäys
    Set Authors  John Smith
    Set Year  1990
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Succeed

    Starting Page Should Be Open
    Go To Citation List Page
    List All Citings Page Should Be Open
    Page Should Contain  Onnistunut lisäys

Add Inproceeding With Multiple Authors And Valid Inputs Should Succeed
    Set Title  Toinen onnistunut lisäys
    Set Authors  John Smith  Paul Smith
    Set Year  2021
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Succeed

    Starting Page Should Be Open
    Go To Add New Inproceedings Page
    Set Title  Kolmas onnistunut lisäys
    Set Authors  John Smith  Paul Smith  Roger Moore
    Set Year  2022
    Set Booktitle  Konferenssi
    Submit Citation
    Add Citation Should Succeed

    Starting Page Should Be Open
    Go To Citation List Page
    List All Citings Page Should Be Open
    Page Should Contain  Toinen onnistunut lisäys
    Page Should Contain  Kolmas onnistunut lisäys