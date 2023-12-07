## Sovelluksen asennus ja käyttö
Sovellus on kehitetty ja testattu ubuntu-käyttöjärjelmässä ja Chrome-selaimella. Sovelluksen käyttö vaatii, että koneella on myös asennettuna [PostgreSQL](https://hy-tsoha.github.io/materiaali/osa-2/#tietokannan-k%C3%A4ytt%C3%A4minen). Robot-automaattitestien suorittaminen vaatii lisäksi, että koneella on asennettuna [ChromeDriver](https://chromedriver.chromium.org/).

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
Avaa toinenkin terminaali-ikkuna ja käynnistä tietokanta. Jätä tämä terminaali-ikkuna auki ja palaa ensimmäiseen. Siirry ensimmäisessä terminaali-ikkunassa hakemistoon src/flaskapp ja sovelluksen käynnistämiseksi, anna tässä hakemistossa komento
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
Jos haluat kokeilla automaattitestien suorittamista, tulee sinulla olla kaksi terminaali-ikkunaa auki. Yksi terminaali tarvitaan tietokantaa varten ja toinen testien ajamista varten. Automaattitestit, jotka testaavat selaimen toimintaa, käynnistyvät projektin päähakemistossa komennolla
```
bash run_robot_tests.sh
```
ja edellyttävät, että olet siirtynyt tässäkin terminaali-ikkunassa kehitysympäristöön komennolla
```
poetry shell
```
Sovelluksen logiikkakerrosta testaavat yksikkötestit eivät tarvitse selainta ja tietokantaa, joten niiden ajamiseen tarvitaan vain yksi terminaali. Testit käynnistyvät päähakemistossa komennolla
```
pytest src
```
