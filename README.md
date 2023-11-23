# Latex viitteet
Ohjelmistotuotannon miniprojekti, jossa toteutetaan ohjelmisto LaTeX-viitteiden hallintaan.

[Product ja sprint backlog](https://docs.google.com/spreadsheets/d/1_GrzhJGGQyghViQuldFHEWCykgaDoEYmzQ-qJ1aEf-k/edit?usp=sharing)

![GHA workflow badge](https://github.com/tihvis/latex-viitteet/workflows/CI/badge.svg)

# Sovelluksen asennus ja käyttö
Sovellus on kehitetty ja testattu ubuntu-käyttöjärjelmässä ja Chrome-selaimella. Sovelluksen käyttö vaatii, että koneella on myös asennettuna [PostgreSQL](https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen). Robot-automaattitestien suorittaminen vaatii lisäksi, että koneella on asennettuna [ChromeDriver](https://chromedriver.chromium.org/).

Kopioi koneellesi kaikki tiedostot hakemistorakenne säilyttäen. Näiden tiedostojen lisäksi tarvitaan projektin päähakemistoon tiedosto, johon talletetaan ympäristömuuttujat. Tiedoston nimeksi tulee antaa .env ja tiedoston sisällön tulee olla seuraava:
```bash
DATABASE_URL=postgresql:///user
SECRET_KEY=<itsemuodostettu salasana>
```
Salasanan saa muodostettua esimerkiksi terminaalin komentorivillä seuraavilla komennoilla: 
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
ja toivo ihmettä. Jos tietokanta käynnistyy onnistuneesti, jätä terminaali-ikkuna auki ja siirry takaisin toiseen terminaaliin. Siirry siellä hakemistoon src/flask ja anna komento
```
flask run
```
Jos olet syntynyt onnellisten tähtien alla, sovellus käynnistyy ja saat pelottavan varoituksen seuraavan kaltaisen ilmoituksen:
```
Running on http://127.0.0.1:5000
```
Voit nyt siirtyä Chrome-selaimeen ja kirjoittaa kyseisen osoitteen selaimen osoitekenttään.
Sovelluksen suorituksen voi lopettaa terminaalin antamalla ohjeella
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
Jos haluat kokeilla automaattitestien suorittamista, tulee sinulla olla kolme terminaali-ikkunaa auki. Yksi terminaali tarvitaan tietokantaa varten, toinen sovellusta varten ja kolmas testien ajamista varten. Automaattitestit käynnistyvät projektin päähakemistossa komennolla
```
robot src/tests
```
ja edellyttävät, että olet siirtynyt tässäkin terminaali-ikkunassa kehitys-ympäristöön komennolla
```
poetry shell
```
