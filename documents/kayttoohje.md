## Sovelluksen asennus ja automaattitestien ajaminen
Sovellus on kehitetty ja testattu ubuntu-käyttöjärjelmässä ja Chrome-selaimella. Automaattitestien ajaminen lokaalisti edellyttää, että koneella on myös asennettuna [PostgreSQL](https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen) ja [ChromeDriver](https://chromedriver.chromium.org/).

Kopioi koneellesi kaikki tiedostot hakemistorakenne säilyttäen. Ohjelman riippuvuuksien asentamiseksi, anna terminaalissa projektin juuressa komento
```
poetry install
```
Jos saat virheilmoituksen, voit antaa lisäksi virheilmoituksen mukaisen komennon
```
poetry install --no-root
```
Siirry sitten projektin ympäristöön komennolla
```
poetry shell
```
Yksikkötestit voi nyt ajaa komennolla 
```
pytest
```
Robot-testien ajaminen vaatii, että toisessa terminaali-ikkunassa on tietokanta käynnistettynä. Robot-testit käynnistyvät komennolla
```
bash run_robot_tests.sh
```
Kehitysympäristöstä pääset poistumaan komennolla
```
exit
```
