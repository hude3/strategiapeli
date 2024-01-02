# Strategiapeli (STRAT)


## Esittely

Projektissa on luotu vuoropohjainen strategiapeli, jossa vastustajana on älykäs tietokonevastustaja. 
Inspiraation lähteenä projektissa on käytetty Civilization-pelisarjan pelejä ja sen ominaisuuksia. 
Tavoitteenani oli luoda maailma, joka perustuu neliönmuotoisiin palasiin (tile) ja luoda maailma siten, että siihen on helppo lisätä eri mahdollisuuksia.
Loin useampia erilaisia käytettäviä hahmoja (unit) ja lisäsin näille eri ominaisuuksiksi liikkua, hyökätä ja tietylle hahmolle mahdollisuuden rakentaa kaupunkeja.
Loin pelikartan siten, että ne muodostuvat satunnaisesti. Tavoitteena oli myös lisätä peliin karttaeditori, eli pelaaja voi itse luoda oman pelikartan, mutta tähän tavoitteeseen ei päästy, vaan kartan muokkaaminen onnistuu vain tallennustiedostoista.

## Tiedosto- ja kansiorakenne

Scr-kansiosta löytyy pelin koodi ja doc-kansiosta löytyy pelin dokumentaatio. Kaikki koodi on allekirjoittaneen omaa koodia.
Peliä ajetaan main2.py tiedostolla ja
konfiguroitaan muokkaamalla configuring.txt tiedostoa.



## Asennusohje

Tämän pelin käyttöön tarvitset vain PyQt6 ja Python tulkin (sekä mieluiten PyCharmin)



## Käyttöohje

Ohjelmaa ajetaan PyCharmissa game-kansiossa olevan main.py tiedoston avulla.
PyCharmin ulkopuolella peliä voi ajaa main2.py funktiolla joka on suoraan projektikansiossa, mutta tämän kanssa on ollut hankaluuksia.

Ohjelmaa ajettaessa sinun tulee valita, että aloitatko vai jatkatko peliä. Peliä aloittaessa annat
ohjelmalle nimesi sekä pelin kartan leveyden ja pituuden, jonka jälkeen ohjelma generoi kartan ja aloitushahmot
sinulle ja vastustajallesi. Löydät oman hahmosi kartan vasemmasta yläkulmasta.

Tavoitteenasi on tuhota vastustaja. Alussa teet Settlerillä kaupungin, joka alkaa tuottaa yhden kolikon per vuoro.
Jokainen kaupunki tuottaa yhden kolikon vuorossa. Tämän jälkeen tavoitteenasi on luoda sotajoukko sekä lisää kaupunkeja,
joilla voit lyödä vastustajasi. Configuring-tiedostosta voit löytää jokaisen hahmon tiedot ja niitä voi halutessa muokata.
Jokainen hahmo voi liikkua kerran vuorossa ja hyökätä kerran vuorossa. Tämän jälkeen täytyy klikata "next turn" painiketta, jotta
vuoro vaihtuu.

Ohjelman tallennus toimii file-valikosta ja sieltä save ja tähän kirjoitat haluamasi nimen tallennustiedostolle. Tämän jälkeen
voit sulkea pelin. Voit jatkaa tallentamastasi tilanteesta alkuvalikossa valitsemalla "continue a match"
ja kirjoittamalla tallennustiedoston nimen.







