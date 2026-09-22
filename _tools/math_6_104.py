# -*- coding: utf-8 -*-
"""6. klase, 104. stunda: «Kāds vispārīgs apgalvojums ir patiess?»

Mikrotemata noslēgums. Līdz šim skolēni salīdzināja konkrētus skaitļus;
tagad jāpasaka, kas ir patiess par *visiem* skaitļiem. Viens pretpiemērs
apgāž apgalvojumu - un tieši to arī jāiemācās meklēt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kāds vispārīgs apgalvojums ir patiess?"

MERKIS = ("Formulēsim vispārīgus spriedumus par skaitļu salīdzināšanu un "
          "pamatosim tos.")

SATURS = [
    Sakums("Viens pretpiemērs apgāž visu",
           zimejums=taisne(-4, 4, 2, [(-3, "−3"), (2, "2")]),
           paraksts="«Skaitlis ar lielāku moduli ir lielāks» - nepatiess: "
                    "−3 modulis ir lielāks, bet pats skaitlis mazāks.",
           fakti=["Vispārīgs apgalvojums der visiem skaitļiem, bez "
                  "izņēmumiem.",
                  "Lai to apgāztu, pietiek ar vienu pretpiemēru.",
                  "Lai to pierādītu, jāpamato ar skaitļu taisni."]),

    Doma("Meklē pretpiemēru, pirms tici",
         "Vispārīgs apgalvojums par skaitļiem ir patiess tikai tad, ja tam "
         "nav neviena pretpiemēra; viens pretpiemērs to apgāž.",
         soli=[
             "Izlasi apgalvojumu un saproti, par kuriem skaitļiem tas runā.",
             "Pamēģini to ar pozitīviem skaitļiem.",
             "Pamēģini to ar negatīviem skaitļiem.",
             "Pamēģini to ar nulli un ar daļām.",
             "Ja kaut viens gadījums neiederas, apgalvojums ir nepatiess.",
         ],
         pieze="Nulle un daļas ir tās vietas, kur apgalvojumi visbiežāk "
               "salūst. «Katrs skaitlis ir mazāks par savu kvadrātu» ir "
               "nepatiess tieši nulles un daļu dēļ."),

    Paraugs("Patiess vai nepatiess?",
            uzd="Vai apgalvojums «jebkurš negatīvs skaitlis ir mazāks par "
                "jebkuru pozitīvu» ir patiess?",
            soli=[
                ("Negatīvie ir pa kreisi no nulles",
                 "Visi bez izņēmuma."),
                ("Pozitīvie ir pa labi no nulles",
                 "Arī visi."),
                ("Tāpēc negatīvais vienmēr ir vairāk pa kreisi",
                 "Un tātad mazāks."),
                ("Pretpiemēru nav",
                 "Apgalvojums ir patiess."),
            ],
            atbilde="patiess"),

    Ievadi("Atrodi pretpiemēru", [
        {"jaut": "«Skaitlis ar lielāku moduli ir lielāks.» Ieraksti "
                 "pretpiemēru: skaitli, kuram modulis 3, bet kurš ir mazāks "
                 "par 2.",
         "atb": ["-3", "−3"], "padoms": "Negatīvs skaitlis."},
        {"jaut": "«Jebkurš negatīvs skaitlis ir mazāks par nulli.» Patiess "
                 "vai nepatiess? Raksti «patiess» vai «nepatiess».",
         "atb": ["patiess"], "padoms": "Visi negatīvie ir pa kreisi."},
        {"jaut": "«Jebkurš skaitlis ir lielāks par savu pretējo skaitli.» "
                 "Patiess vai nepatiess?",
         "atb": ["nepatiess"], "padoms": "−5 nav lielāks par 5."},
        {"jaut": "«Nulle ir lielāka par visiem negatīvajiem skaitļiem.» "
                 "Patiess vai nepatiess?",
         "atb": ["patiess"], "padoms": "Nulle ir robeža."},
        {"jaut": "«Ja modulis ir vienāds, skaitļi ir vienādi.» Patiess vai "
                 "nepatiess?",
         "atb": ["nepatiess"], "padoms": "5 un −5."},
        {"jaut": "«Starp diviem skaitļiem vienmēr ir vēl viens skaitlis.» "
                 "Patiess vai nepatiess?",
         "atb": ["patiess"], "padoms": "Vienmēr der vidus."},
    ], pamats=4,
        ievads="Pirms atbildēt, pamēģini apgalvojumu ar negatīviem "
               "skaitļiem."),

    Varianti("Kurš apgalvojums ir patiess?", [
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Jebkurš pozitīvs skaitlis ir lielāks par jebkuru "
                     "negatīvu",
                     "Skaitlis ar lielāku moduli ir lielāks",
                     "Negatīvs skaitlis var būt lielāks par pozitīvu",
                     "Nulle ir mazāka par visiem skaitļiem"],
         "pareizi": 0,
         "padoms": "Pārbaudi katru ar piemēru."},
        {"jaut": "Kāpēc pietiek ar vienu pretpiemēru?",
         "opcijas": ["Jo vispārīgam apgalvojumam jāder visiem gadījumiem",
                     "Jo viens piemērs ir svarīgāks",
                     "Jo skaitļu ir daudz", "Nepietiek"],
         "pareizi": 0,
         "padoms": "«Visiem» nozīmē bez izņēmumiem."},
        {"jaut": "Kur apgalvojumi visbiežāk salūst?",
         "opcijas": ["Pie nulles un daļām", "Pie lieliem skaitļiem",
                     "Pie pozitīviem skaitļiem", "Nekur"],
         "pareizi": 0,
         "padoms": "Tos aizmirst pārbaudīt."},
        {"jaut": "«Katrs skaitlis ir mazāks par to, kas ir pa labi no tā.» "
                 "Šis apgalvojums ir...",
         "opcijas": ["patiess", "nepatiess",
                     "patiess tikai pozitīviem", "nezināms"],
         "pareizi": 0,
         "padoms": "Tā ir skaitļu taisnes īpašība."},
    ], pamats=4),

    Pasaule("Vai ziņu apgalvojums ir patiess?",
            Ievadi("", [
                {"jaut": "«Šī nakts bija aukstākā: −15 °C.» Vakar bija "
                         "−18 °C. Vai apgalvojums patiess? Raksti «jā» vai "
                         "«nē».",
                 "atb": ["nē", "ne"], "padoms": "−18 ir mazāks."},
                {"jaut": "Par cik grādiem vakardiena bija aukstāka?",
                 "atb": ["3"], "padoms": "18 − 15."},
                {"jaut": "«Temperatūra pieauga par 10 grādiem no −4 °C.» Cik "
                         "grādu ir tagad?",
                 "atb": ["6"], "padoms": "−4 + 10."},
                {"jaut": "Vai apgalvojums «temperatūra kļuva pozitīva» ir "
                         "patiess? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "6 ir virs nulles."},
            ]),
            pavediens="planeta",
            konteksts="Ziņās apgalvojumus par rekordiem pārbauda tieši tā - "
                      "salīdzinot skaitļus ar zīmi.",
            kapec="Viens pretpiemērs atspēko arī visskaļāko apgalvojumu."),

    Zimejums("Kur apgalvojums salūst",
             taisne(-5, 5, 1, [(-4, "−4"), (0, "0"), (4, "4")]),
             paskaidro="−4 un 4 moduļi ir vienādi, bet skaitļi nav. Tas ir "
                       "pretpiemērs apgalvojumam par moduļiem.",
             ievads="Pretpiemēru visbiežāk atrod uz taisnes."),

    Kopsavilkums([
        "Formulēju vispārīgus apgalvojumus par skaitļiem.",
        "Pārbaudu tos ar pozitīviem, negatīviem skaitļiem, nulli un daļām.",
        "Atrodu pretpiemēru un ar to apgāžu nepatiesu apgalvojumu.",
        "Pamatoju patiesu apgalvojumu ar skaitļu taisni.",
    ]),

    Majas([
        "Pārbaudi apgalvojumu «jebkurš skaitlis ir mazāks par 100».",
        "Izdomā vienu patiesu un vienu nepatiesu apgalvojumu par negatīviem "
        "skaitļiem.",
        "Katram nepatiesajam pieraksti pretpiemēru.",
    ]),
]
