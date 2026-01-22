# Analiza utjecaja vremenskih uvjeta na ishod utrka Formule 1 🏎️🌦️

Ovaj projekt analizira povezanost između temperature staze i uspjeha vozača u F1 sezoni 2023. koristeći Python, OpenF1 API i povijesne podatke.

Formula 1 je jedan od tehnološki najnaprednijih sportova na svijetu, gdje o pobjedi često odlučuju milisekunde. Osim inženjerskih performansi bolida i vještine vozača, jedan od ključnih vanjskih faktora koji utječe na ishod utrke su vremenski uvjeti. **Temperatura staze** (*track temperature*) izravno diktira **prianjanje guma** (*grip*) i njihovu degradaciju, dok **temperatura zraka** utječe na hlađenje motora i aerodinamičku efikasnost.

## Opis projekta
Cilj projekta je integrirati statičke podatke (CSV) s dinamičkim telemetrijskim podacima (REST API) kako bi se utvrdilo utječu li ekstremni vremenski uvjeti na poredak vozača.

**Korištene tehnologije:**
* Python (Pandas, Requests, SQLAlchemy, Flask)
* Jupyter Notebook
* SQLite baza podataka
* OpenF1 API

## Kako pokrenuti projekt

### Opcija 1: Google Colab
1. Preuzmite datoteku `epetrovic23_F1_Project.ipynb`.
2. Otvorite je u [Google Colab](https://colab.research.google.com/).
3. Uploadajte CSV datoteke (`races.csv`, `drivers.csv`, `results.csv`) u Colab (lijeva strana, ikona mape).
4. Pokrenite ćelije redom ("Run All").

### Opcija 2: Lokalno na računalu
1. Klonirajte repozitorij:
   ```bash
   git clone [https://github.com/epetrovic23/f1-weather-analysis.git](https://github.com/epetrovic23/f1-weather-analysis.git)
