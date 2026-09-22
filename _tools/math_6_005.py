# -*- coding: utf-8 -*-
"""6. klase, 5. stunda: «Kāda ir šo objektu attiecība?»

Mikrotemata pēdējā stunda: attiecība vairs nav dota tekstā - tā jāievāc
pašam. Vispirms novērtējums ar aci, tikai tad mērlente; šī secība ir pati
mācība, jo pārbaudīt savu minējumu ir vērtīgāk nekā uzreiz izmērīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Kāda ir šo objektu attiecība?"

MERKIS = ("Mācīsimies aptuveni noteikt apkārtnes objektu garumu vai laukumu "
          "attiecību un pārbaudīt savu novērtējumu ar mērījumiem.")

SATURS = [
    Sakums("Cik reižu durvis ir augstākas par galdu?",
           zimejums=kolonnas([("galds", 75), ("durvis", 200)], " cm"),
           paraksts="Ar aci teiktu «kādas trīs reizes». Mērlente saka citu "
                    "skaitli.",
           fakti=["Vispirms mini, tikai tad mēri.",
                  "Minējums, kas nepiepildās, iemāca visvairāk."]),

    Doma("Vispirms novērtē, tad izmēri, tad saīsini",
         "Attiecību var novērtēt ar aci, bet pārbaudīt - tikai ar mērījumu.",
         soli=[
             "Izvēlies divus objektus un vienu mērvienību abiem.",
             "Pieraksti savu minējumu: «apmēram ... pret ...».",
             "Izmēri abus un pieraksti abus skaitļus.",
             "Uzraksti attiecību ar kolu un saīsini to.",
             "Salīdzini ar minējumu: cik tālu biji?",
         ],
         pieze="Mērījumi reti dod skaistus skaitļus. 75 cm un 200 cm dod "
               "attiecību 3 : 8 - to var noapaļot līdz «apmēram 1 pret 3», "
               "ja vajag tikai priekšstatu."),

    Zimejums("Divi mērījumi blakus",
             kolonnas([("logs", 120), ("durvis", 200)], " cm"),
             paskaidro="120 : 200 = 3 : 5. Logs ir mazliet vairāk nekā puse "
                       "no durvju augstuma.",
             ievads="Tie paši soļi citiem diviem objektiem."),

    Paraugs("No mērījuma uz attiecību",
            uzd="Galds ir 75 cm augsts, durvis - 200 cm. Kāda ir to "
                "attiecība?",
            soli=[
                ("Abi mērīti centimetros",
                 "Viena mērvienība - attiecību drīkst rakstīt."),
                ("75 : 200",
                 "Pirmais nosauktais - galds."),
                ("Abus dala ar 25: 3 : 8",
                 "25 ir lielākais kopīgais dalītājs."),
                ("Aptuveni 1 pret 3",
                 "Ja vajag tikai priekšstatu, saīsināto var noapaļot."),
            ],
            atbilde="75 : 200 = 3 : 8, apmēram 1 pret 3"),

    Ievadi("Izrēķini attiecību", [
        {"jaut": "Logs 120 cm, durvis 200 cm. Attiecība ar kolu? (piem. 1:2)",
         "atb": ["3:5"], "padoms": "Abus dali ar 40."},
        {"jaut": "Krēsls 50 cm, galds 75 cm. Attiecība ar kolu?",
         "atb": ["2:3"], "padoms": "Abus dali ar 25."},
        {"jaut": "Grāmata 20 cm, plaukts 100 cm. Attiecība ar kolu?",
         "atb": ["1:5"], "padoms": "Abus dali ar 20."},
        {"jaut": "Paklājs 2 m, istaba 6 m. Attiecība ar kolu?",
         "atb": ["1:3"], "padoms": "Abus dali ar 2."},
        {"jaut": "Telefons 15 cm, planšete 25 cm. Attiecība ar kolu?",
         "atb": ["3:5"], "padoms": "Abus dali ar 5."},
        {"jaut": "Dobe 4 m² un dārzs 24 m². Attiecība ar kolu?",
         "atb": ["1:6"], "padoms": "Abus dali ar 4."},
    ], pamats=4,
        ievads="Vispirms saīsini, tikai tad raksti atbildi."),

    Varianti("Kā pareizi mērīt un salīdzināt?", [
        {"jaut": "Galdu izmērīji centimetros, istabu - metros. Ko darīt "
                 "vispirms?",
         "opcijas": ["Pārveidot vienā mērvienībā",
                     "Rakstīt attiecību tāpat",
                     "Izvēlēties lielāko skaitli",
                     "Mērīt vēlreiz"],
         "pareizi": 0,
         "padoms": "Attiecībā abiem jābūt vienā mērvienībā."},
        {"jaut": "Minēji 1 pret 3, izmērīji 3 : 8. Ko tas nozīmē?",
         "opcijas": ["Minējums bija gandrīz pareizs",
                     "Minējums bija pilnīgi nepareizs",
                     "Mērījums ir kļūdains",
                     "Attiecību nevar noteikt"],
         "pareizi": 0,
         "padoms": "3 : 8 ir mazliet vairāk nekā 3 : 9, un 3 : 9 ir 1 : 3."},
        {"jaut": "Kāpēc mērījumi reti dod skaistus skaitļus?",
         "opcijas": ["Lietas nav taisītas pēc attiecībām",
                     "Mērlente ir neprecīza",
                     "Skaistus skaitļus nedrīkst",
                     "Jo mēra centimetros"],
         "pareizi": 0,
         "padoms": "Durvis netaisa tā, lai tās būtu tieši trīs galdi."},
        {"jaut": "Ko dara ar attiecību 75 : 200, ja vajag tikai "
                 "priekšstatu?",
         "opcijas": ["Saīsina un noapaļo", "Atstāj, kā ir",
                     "Apmaina vietām", "Saskaita abus skaitļus"],
         "pareizi": 0,
         "padoms": "3 : 8 ir tuvu 1 : 3."},
    ], pamats=4),

    Pasaule("Kas ar ko samērojas istabā?",
            Ievadi("", [
                {"jaut": "Istaba 6 m gara un 3 m plata. Garuma attiecība "
                         "pret platumu ar kolu?",
                 "atb": ["2:1"], "padoms": "6 : 3."},
                {"jaut": "Tās pašas istabas laukums kvadrātmetros?",
                 "atb": ["18"], "padoms": "6 · 3."},
                {"jaut": "Paklājs 2 m x 3 m. Tā laukums kvadrātmetros?",
                 "atb": ["6"], "padoms": "2 · 3."},
                {"jaut": "Paklāja laukuma attiecība pret istabas laukumu ar "
                         "kolu?",
                 "atb": ["1:3"], "padoms": "6 : 18."},
            ]),
            pavediens="maja",
            konteksts="Pērkot paklāju vai skapi, vispirms salīdzina to ar "
                      "istabu - un tā ir attiecība.",
            kapec="Laukumus salīdzina tāpat kā garumus: abus vienā "
                  "mērvienībā."),

    Kopsavilkums([
        "Aptuveni novērtēju divu objektu attiecību ar aci.",
        "Izmēru abus vienā mērvienībā un uzrakstu attiecību.",
        "Saīsinu attiecību un salīdzinu to ar savu minējumu.",
        "Noapaļoju attiecību, ja vajag tikai priekšstatu.",
    ]),

    Majas([
        "Izvēlies divas lietas mājās, mini to attiecību un pēc tam izmēri.",
        "Pieraksti abus skaitļus un saīsināto attiecību.",
        "Atrodi mājās divas lietas, kuru attiecība ir tuvu 1 pret 2.",
    ]),
]
