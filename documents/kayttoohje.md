## Sovelluksen asennus ja käyttö
Sovellus on kehitetty ja testattu ubuntu-käyttöjärjelmässä ja Chrome-selaimella. Sovelluksen käyttö vaatii, että koneella on myös asennettuna [PostgreSQL](https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen). Robot-automaattitestien suorittaminen vaatii lisäksi, että koneella on asennettuna [ChromeDriver](https://chromedriver.chromium.org/).

Kopioi koneellesi kaikki tiedostot hakemistorakenne säilyttäen. Luo ympäristömuuttujat sisältävä tiedosto .env, jossa on seuraavat rivit:
```bash
DATABASE_URL=postgresql:///user
SECRET_KEY=avain
```
Lisää tietokannan osoitteeseen "user" tilalle Postgres-tietokantasi nimi. Salaisen avaimen saa muodostettua esimerkiksi terminaalin komentorivillä seuraavilla komennoilla: 
```
$ python3
>>> import secrets
>>> secrets.token_hex(16)
```
Ohjelman riippuvuuksien asentamiseksi, anna terminaalissa projektin juuressa komento
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
Avaa toinenkin terminaali-ikkuna ja siirry samaan hakemistoon ja anna sielläkin komento
```
poetry shell
```
Tätä terminaalia käytetään tietokannan käynnistämiseen. Käynnistä tietokanta komennolla
```
start-pg.sh
```
ja toivo ihmettä. Jos tietokanta käynnistyy onnistuneesti, jätä terminaali-ikkuna auki ja siirry takaisin toiseen terminaaliin. Anna komentorivillä komento
```
psql
```
Nyt olet yhteydessä tietokantaan ja promptina näkyy >>>. Anna tietokannalle komento
```drop schema public cascade; create schema public;
```
ja katkaise tietokantayhteys komennolla
```
\q
```
ja olet takaisin terminaalin komentorivillä. Siirry siellä hakemistoon src/flaskapp komennolla
```
cd src/flaskapp
```
ja sovelluksen käynnistämiseksi, anna tässä hakemistossa komento
```
flask run
```
Jos kaikki menee hyvin, sovellus käynnistyy ja näet osoitteen, jossa ohjelma toimii:
```
Running on http://127.0.0.1:5000
```
Voit nyt siirtyä Chrome-selaimeen ja kirjoittaa kyseisen osoitteen selaimen osoitekenttään. Pääset selaimeen myös klikkaamalla terminaalissa näkyvää osoitelinkkiä hiiren oikealla näppäimellä ja valitsemalla 'open link'. Sovelluksen suorituksen voi lopettaa terminaalin antamalla ohjeella
```
Press CTRL+C to quit
```
ja kehitysympäristöstä pääset poistumaan komennolla
```
exit
```
Kun olet lopettanut sovelluksen käytön, muista myös sulkea tietokantaohjelma toisesta terminaalista. Sekin onnistuu komennolla
```
Press CTRL+C to quit
```
minkä jälkeen voit poistua kehitysympäristöstä komennolla
```
exit
```
Jos haluat kokeilla automaattitestien suorittamista, tulee sinulla olla kolme terminaali-ikkunaa auki. Yksi terminaali tarvitaan tietokantaa varten, toinen sovellusta varten ja kolmas testien ajamista varten. Automaattitestit, jotka testaavat selaimen toimintaa, käynnistyvät projektin päähakemistossa komennolla
```
robot src/tests
```
ja edellyttävät, että olet siirtynyt tässäkin terminaali-ikkunassa kehitysympäristöön komennolla
```
poetry shell
```
Sovelluksen logiikkakerrosta testaavat yksikkötestit eivät tarvitse selainta ja tietokantaa, joten niiden ajamiseen tarvitaan vain yksi terminaali. Testit käynnistyvät päähakemistossa komennolla
```
pytest src
```
