# Team Agilen loppuraportti
*Olli Haapasalo, Riku Johansson, Jussi Kinanen, Riitta Pessi ja Mira Tihveräinen*

Tässä raportissa käydään läpi eri sprinttien aikana kohdattuja ongelmia, reflektoidaan onnistumisia ja
pohditaan, mitä voisi seuraavalla kerralla tehdä paremmin.

## Sprinttien aikana kohdattuja ongelmia

### Sprint 1
- Työnjako ensimmäisen sprintin aikana oli hieman epäselvä.
- Yhteydenpito jäsenten välillä ei ollut niin tiivistä kuin myöhemmin ja välillä oli vaikea tietää, mitä muut ovat tekemässä.
- CI-pipelinen konfiguraatiossa oli suuria ongelmia lähinnä Postgresin vuoksi
- Sovelluksen käynnistämisessä oli välillä Postgresin käyttöön liittyviä haasteita
- Sovelluksen suunnitteluun käytettiin liian vähän aikaa, eikä ensimmäisen sprintin aikana ollut vielä selvää visiota
  sovelluksen arkkitehtuurista

### Sprint 2
- Postgresiin liittyvät vaikeudet pipelinen konfiguraatiossa jatkuivat, mutta saatiin lopulta ratkaistua
- Versionhallinnassa oli sekä suoraan päähaaraan pushaamista että liian pitkäikäisiä kehityshaaroja, jotka yhdistettiin
  päähaaraan vasta sprintin lopulla
- Työtunnit painottuivat liikaa sprintin lopulle
- Kaikkia sprintin arvosteluperusteita ei muistettu tarkistaa ajoissa ja tästä koitui meille pistevähennyksiä

### Sprint 3
- Käyttäjäominaisuuksien lisääminen osoittautui ennakoitua työläämmäksi ja valmistui vasta sprintin lopulla
- Käyttäjien lisääminen sovellukseen aiheutti paljon muutoksia eri puolilla sovellusta
- Luvattujen user storyjen saaminen valmiiksi vei niin kauan, että aiottu tuontantoon vieminen siirtyi seuraavaan sprinttiin

### Sprint 4
- Koko ajan kysymysmerkkinä ollut Flask-testaus osoittautui liian vaikeaksi asiaksi opetella lyhyessä ajassa ja
  aiotut Flask-testit jäivät toteuttamatta
- Kaikki lopulliset ominaisuudet eivät ehtineet valmistua demotilaisuuteen mennessä
- Sovellukseen jäi jonkin verran copypaste-koodia, jonka refaktorointiin ei jäänyt aikaa

## Mieleen jääneitä onnistumisia
- Ensimmäinen tapaaminen saatiin sovittua nopeasti ja projektin parissa työskentely starttasi innostuneessa ilmapiirissä
- Ryhmähenki oli jo alusta lähtien hyvä ja parani vielä projektin aikana
- Yhteydenpito tiivistyi projektin edetessä ja ongelmatilanteissa ei kenenkään tarvinnut jäädä yksin
- Yhden sprintin aikana yksi tiimin jäsenistä oli ulkomaanlomalla perheensä kanssa, mutta tämäkään ei estänyt hyvää
  yhteydenpitoa ja projektin etenemistä
- Osasimme antaa itsellemme ja toisille tiimiläisille tunnustusta hyvin tehdystä työstä
- Kerroimme avoimesti omista vahvuusalueistamme ja myös heikommin hallinnassa olevista osaamisalueista ja
  uskalsimme pyytää ongelmatilanteissa toisilta apua
- Löysimme jokaisessa retrospektiivissä onnistumisia ja kehitettävää ja pyrimme aktiivisesti parempaan toimintaan
- Projektin edetessä irtaannuimme turhasta stressistä ja suorittamisesta ja siirryimme rennompaan tekemiseen,
  viimeinen sprinttin sujui hyvissä tunnelmissa sovellusta viimeistellessä
- Demoa varten pidettiin kenraaliharjoitus, missä pääesiintyjä sai vinkkien lisäksi tukea ja kannustusta

## Parannettavaa seuraavalle kerralle
- Projektin alussa olisi hyvä käyttää enemmän aikaa projektin suunnitteluun ja myös tiimiläisiin tutustumiseen
- Sovelluksen runko ja arkkitehtuuri olisi hyvä miettiä alussa, jotta myöhemmin ei tule suurta tarvetta
  refaktoroinnille ja kansiorakenteen muutoksille
- Sprintin aikana tulisi paremmin huomioida toisistaan riippuvat taskit ja varmistaa, että ne valmistuvat
  oikeassa järjestyksessä, jotta kaikki ehditään saada valmiiksi
- Parikoodausta kannattaisi hyödyntää erityisesti tiimiläisten osaamisalueiden laajentamiseen

## Projektin aikana opittuja asioita
- Opimme työskentelemään ennestään vieraiden ihmisten kanssa ja tutustumaan tiimiläisiin siinä määrin, mitä
  onnistunut yhdessä työskentely edellyttää.
- Opimme, että luottamus tiimin jäsenten tekemiseen rakentuu ajan kanssa ja onnistuneiden kokemusten myötä.
- Opimme, että onnistunut yhteistyö edellyttää selkeää työnjakoa ja tiivistä yhteydenpitoa.
- Opimme myös vaikeuksista ja epäonnistumisista, löysimme ratkaisuja vaikeuksien selättämiseen ja
  epäonnistumisten ennaltaehkäisemiseen.
- Huomasimme, että jo neljässä viikossa tiimi ehtii hitsautua hyvin yhteen, kun kaikki ovat halukkaita tekemään osansa.
- Huomasimme, että konfigurointiin ja muuhun tekniseen säätöön voi mennä ohjelmoinnin ohella yllättävänkin
  paljon aikaa.
- Opimme pilkkomaan laajan ohjelman user storyiksi ja user storyt pienemmiksi taskeiksi.
- Opimme käyttämään versionhallinnan työkaluja aiempaa laajemmin ja hyödyntämään sen ominaisuuksia useamman
  kehittäjän projektissa.
