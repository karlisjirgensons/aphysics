# -*- coding: utf-8 -*-
"""6. klase, 160. stunda: «Kāda ir darbību secība?»

Darbību secība ir zināma no 5. klases, bet tagad tajā ir arī negatīvi
skaitļi un kāpināšana. Stunda salikt visu vienā sarakstā, un galvenā kļūda -
reizināšana pirms iekavas - tiek izspēlēta atsevišķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāda ir darbību secība?"

MERKIS = ("Lietosim darbību secību izteiksmēs ar visu veidu skaitļiem.")

SATURS = [
    Sakums("Četri līmeņi, viena kārtība",
           zimejums=restis([["1.", "2.", "3.", "4."],
                            ["iekavas", "pakāpes", "reiz. un dal.",
                             "sask. un atņ."]]),
           paraksts="Katrs līmenis tiek izpildīts pilnībā, pirms sākas "
                    "nākamais.",
           fakti=["Iekavas vienmēr ir pirmās.",
                  "Reizināšana un dalīšana ir pirms saskaitīšanas.",
                  "Vienāda līmeņa darbības veic no kreisās uz labo."]),

    Doma("Līmenis pēc līmeņa",
         "Izteiksmes vērtību aprēķina četros līmeņos: iekavas, pakāpes, "
         "reizināšana un dalīšana, saskaitīšana un atņemšana.",
         soli=[
             "Atrodi un izrēķini visas iekavas.",
             "Izrēķini pakāpes.",
             "Veic reizināšanu un dalīšanu no kreisās uz labo.",
             "Veic saskaitīšanu un atņemšanu no kreisās uz labo.",
             "Pārbaudi, vai neviena darbība nav izlaista.",
         ],
         pieze="Mīnuss skaitļa priekšā nav darbība - tā ir skaitļa zīme. "
               "Tāpēc (−3) otrajā pakāpē kāpina visu skaitli, bet "
               "−3 otrajā pakāpē - tikai trijnieku."),

    Paraugs("Četri līmeņi vienā izteiksmē",
            uzd="Izrēķini (−2 + 5) · (−4) : 2 + 3.",
            soli=[
                ("Iekavas: −2 + 5 = 3",
                 "Pirmais līmenis."),
                ("3 · (−4) = −12",
                 "Reizināšana, no kreisās uz labo."),
                ("−12 : 2 = −6",
                 "Dalīšana tajā pašā līmenī."),
                ("−6 + 3 = −3",
                 "Saskaitīšana pēdējā."),
            ],
            atbilde="−3"),

    Ievadi("Ievēro secību", [
        {"jaut": "Cik ir (−2 + 5) · (−4) : 2 + 3?",
         "atb": ["-3", "−3"], "padoms": "3 · (−4) : 2 + 3."},
        {"jaut": "Cik ir 4 + 6 · (−2)?",
         "atb": ["-8", "−8"], "padoms": "Vispirms reizināšana."},
        {"jaut": "Cik ir (4 + 6) · (−2)?",
         "atb": ["-20", "−20"], "padoms": "Iekavas maina secību."},
        {"jaut": "Cik ir (−3) otrajā pakāpē + 1?",
         "atb": ["10"], "padoms": "9 + 1."},
        {"jaut": "Cik ir 10 − 4 · (−2) : 8?",
         "atb": ["11"], "padoms": "10 − (−1)."},
        {"jaut": "Cik ir (−6) : 3 · 2?",
         "atb": ["-4", "−4"], "padoms": "No kreisās uz labo."},
    ], pamats=4,
        ievads="Vispirms pasaki, kura darbība ir pirmā."),

    Varianti("Kura darbība ir pirmā?", [
        {"jaut": "Izteiksmē 4 + 6 · (−2) pirmā ir...",
         "opcijas": ["reizināšana", "saskaitīšana",
                     "no kreisās uz labo", "nav svarīgi"],
         "pareizi": 0,
         "padoms": "Augstāks līmenis."},
        {"jaut": "Izteiksmē (−6) : 3 · 2 darbības veic...",
         "opcijas": ["no kreisās uz labo", "vispirms reizināšanu",
                     "vispirms dalīšanu vienmēr", "jebkurā secībā"],
         "pareizi": 0,
         "padoms": "Viens līmenis."},
        {"jaut": "Kurš līmenis ir otrais?",
         "opcijas": ["pakāpes", "iekavas", "reizināšana", "saskaitīšana"],
         "pareizi": 0,
         "padoms": "Pēc iekavām."},
        {"jaut": "Cik ir (−6) : 3 · 2, ja secību ievēro pareizi?",
         "opcijas": ["−4", "−1", "4", "1"],
         "pareizi": 0,
         "padoms": "−2 · 2."},
    ], pamats=4),

    Pasaule("Kāda ir gala summa?",
            Ievadi("", [
                {"jaut": "4 biļetes pa 8 € un atlaide 6 €. Cik eiro jāmaksā?",
                 "atb": ["26"], "padoms": "4 · 8 − 6."},
                {"jaut": "Ja atlaide būtu pirms reizināšanas jeb (8 − 6) · 4, "
                         "cik eiro būtu?",
                 "atb": ["8"], "padoms": "2 · 4."},
                {"jaut": "Kurš rezultāts ir pareizais, ja atlaide ir vienreiz "
                         "par visu pasūtījumu? Ieraksti summu.",
                 "atb": ["26"], "padoms": "Atlaide atņemama beigās."},
                {"jaut": "Cik eiro būtu 6 biļetēm ar to pašu atlaidi?",
                 "atb": ["42"], "padoms": "6 · 8 − 6."},
            ]),
            pavediens="celojums",
            konteksts="Viena un tā pati atlaide, atņemta pirms vai pēc "
                      "reizināšanas, dod pavisam citu summu.",
            kapec="Darbību secība te maina cenu, ne tikai atbildi."),

    Kopsavilkums([
        "Ievēroju darbību secību visu veidu skaitļiem.",
        "Izrēķinu iekavas un pakāpes pirms pārējā.",
        "Vienāda līmeņa darbības veicu no kreisās uz labo.",
        "Atšķiru skaitļa zīmi no darbības zīmes.",
    ]),

    Majas([
        "Izrēķini 12 − (−3) · 2 un (12 − (−3)) · 2.",
        "Pieraksti, kāpēc atbildes atšķiras.",
        "Izdomā izteiksmi, kurā iekavas maina rezultātu.",
    ]),
]
