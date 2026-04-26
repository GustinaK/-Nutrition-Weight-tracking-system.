# Mitybos ir svorio sekimo sistema

## 1. Įvadas

### 1.1 Programos tikslas

Šio projekto tikslas – sukurti objektinio programavimo principais paremtą sistemą, leidžiančią vartotojui sekti savo mitybą ir kūno svorį. Programa skirta padėti geriau suprasti kasdienį maisto suvartojimą, analizuoti makroelementus ir stebėti progresą siekiant sveikatingumo tikslų.

---

### 1.2 Programos aprašymas

Sukurta aplikacija yra komandinės eilutės (CLI) programa, kuri leidžia vartotojui registruoti suvartotą maistą, apskaičiuoti kalorijas bei makroelementus (baltymus, angliavandenius ir skaidulas), taip pat sekti kūno svorio pokyčius.

Sistema palaiko porcijų dydžius, leidžia naudoti iš anksto apibrėžtą maisto duomenų bazę ir išsaugo duomenis tarp programos paleidimų. Tai leidžia vartotojui analizuoti informaciją ne tik vienos dienos, bet ir ilgesniu laikotarpiu.

---

### 1.3 Programos paleidimas

Programa paleidžiama naudojant Python programavimo kalbą. Norint ją paleisti, reikia terminale įvykdyti komandą:

python main.py

Programa veikia su Python 3 versija.

---

### 1.4 Programos naudojimas

Pirmo paleidimo metu vartotojas įveda savo pagrindinius duomenis: vardą, kūno svorį bei dienos tikslus (kalorijas, baltymus, angliavandenius ir skaidulas).

Toliau vartotojui pateikiamas paprastas meniu, leidžiantis:
- pridėti suvartotą maistą
- įvesti kūno svorį
- peržiūrėti dienos progresą
- išsaugoti duomenis

Maistas gali būti įvedamas naudojant duomenų bazę arba rankiniu būdu, o porcijos dydis leidžia tiksliau apskaičiuoti suvartotas maistines vertes.

---

## 2. Analizė

### 2.1 Funkcinių reikalavimų įgyvendinimas

Programa įgyvendina visus pagrindinius funkcinius reikalavimus. Vartotojas gali įvesti suvartotą maistą, pasirinkti porcijos dydį ir gauti automatiškai apskaičiuotas kalorijas bei makroelementus. Sistema leidžia palyginti šiuos duomenis su nustatytais dienos tikslais ir taip įvertinti progresą.

Be to, programa leidžia registruoti kūno svorį ir stebėti jo pokyčius laikui bėgant. Visi duomenys saugomi CSV failuose, todėl išlieka tarp programos paleidimų ir gali būti naudojami kelių dienų analizei.

---

### 2.2 Kompozicija (Composition)

Programoje naudojama kompozicija, nes pagrindinė sistema yra sudaryta iš kelių atskirų komponentų. Mitybos sistema naudoja maisto sekimo ir svorio sekimo objektus, kurie veikia kaip atskiros dalys.

Toks sprendimas leidžia lengvai keisti ar plėsti sistemą, nes kiekvienas komponentas yra nepriklausomas ir atsakingas už konkrečią funkciją.

---

### 2.3 Dizaino šablonas – Factory Method

Programoje naudojamas Factory Method dizaino šablonas, kuris atsakingas už objektų kūrimą. Vietoje tiesioginio objektų kūrimo, šis procesas yra centralizuotas, todėl sistema tampa lankstesnė.

Šis šablonas leidžia lengvai pridėti naujus sekimo tipus ateityje ir sumažina priklausomybes tarp skirtingų programos dalių.

---

### 2.4 Objektinio programavimo principai

Programoje įgyvendinti visi keturi pagrindiniai objektinio programavimo principai.

Inkapsuliacija pasireiškia tuo, kad duomenys saugomi privačiuose atributuose, o prieiga prie jų vykdoma tik per metodus. Tai padeda apsaugoti duomenis ir užtikrina jų teisingą naudojimą.

Abstrakcija realizuota naudojant bendrą sąsają, kuri apibrėžia sekimo objektų elgesį, bet slepia jų vidinę realizaciją.

Paveldėjimas naudojamas kuriant skirtingus sekimo tipus, kurie paveldi bendrą funkcionalumą ir jį pritaiko konkretiems atvejams.

Polimorfizmas leidžia naudoti tuos pačius metodus skirtingiems objektams, nors jų elgesys gali skirtis priklausomai nuo konteksto.

---

## 3. Rezultatai ir išvados

### 3.1 Rezultatai

Sukurta programa sėkmingai įgyvendina visas pagrindines funkcijas. Ji leidžia vartotojui registruoti maistą, apskaičiuoti kalorijas ir makroelementus bei stebėti dienos progresą.

Sistema palaiko kelių dienų duomenų saugojimą, todėl vartotojas gali analizuoti savo mitybą ilgesniu laikotarpiu. Porcijų dydžių naudojimas leidžia tiksliau modeliuoti realų maisto suvartojimą.

Vienas iš pagrindinių iššūkių buvo duomenų struktūros suderinimas tarp saugojimo ir atvaizdavimo, taip pat vartotojo įvesties validacija.

---

### 3.2 Išvados

Projektas sėkmingai pasiekė užsibrėžtus tikslus. Programa yra funkcionali, modulinė ir lengvai plečiama. Joje pritaikyti objektinio programavimo principai bei dizaino šablonas.

Galutinis rezultatas yra praktiška sistema, kuri gali būti naudojama kasdieniam mitybos ir svorio sekimui.

---

### 3.3 Ateities plėtra

Ateityje programa galėtų būti tobulinama:

- sukuriant grafinę vartotojo sąsają
- pridedant duomenų vizualizaciją (grafikus)
- naudojant duomenų bazę vietoj CSV failų
- įgyvendinant savaitinę ir mėnesinę analizę
