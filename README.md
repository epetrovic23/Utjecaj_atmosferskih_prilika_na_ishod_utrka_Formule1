# Utjecaj atmosferskih prilika na ishod utrka Formule1

Formula 1 je jedan od tehnološki najnaprednijih sportova na svijetu, gdje o pobjedi često odlučuju milisekunde. Osim inženjerskih performansi bolida i vještine vozača, jedan od ključnih vanjskih faktora koji utječe na ishod utrke su vremenski uvjeti. **Temperatura staze** (*track temperature*) izravno diktira **prianjanje guma** (*grip*) i njihovu degradaciju, dok **temperatura zraka** utječe na hlađenje motora i aerodinamičku efikasnost.


Motivacija za ovaj projekt je istražiti postoji li korelacija između temperature staze i konačnog plasmana vozača u sezoni 2023.

Cilj projekta je razviti automatizirani sustav koji integrira:
* **Statičke povijesne podatke (CSV):** Podaci o utrkama i rezultatima (preuzeti s [Kaggle repozitorija](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)).
* **Dinamičke telemetrijske podatke (REST API):** Meteorološki podaci dohvaćeni putem OpenF1 API-ja.

Sustav pohranjuje ove podatke u strukturiranu bazu za daljnju analizu i ekspoziciju putem vlastitog REST API-ja, te vizualno prikazuje kako se performanse najboljih vozača mijenjaju u ovisnosti o ekstremnim uvjetima 
