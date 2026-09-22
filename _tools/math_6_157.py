# -*- coding: utf-8 -*-
"""6. klase, 157. stunda: «Kuri apgalvojumi ir patiesi?»

Mikrotemata noslēgums. Apgalvojumi par skaitļu kopām jāpārbauda tāpat kā
apgalvojumi par salīdzināšanu: ar pretpiemēru. Un pretpiemērs te parasti
slēpjas pie nulles vai negatīvajiem skaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kuri apgalvojumi ir patiesi?"

MERKIS = ("Izvērtēsim apgalvojumus par skaitļu kopām un pamatosim tos.")

SATURS = [
    Sakums("Pretpiemērs slēpjas pie nulles",
           fakti=["«Katrs vesels skaitlis ir naturāls» - nepatiess: nulle.",
                  "«Katrs naturāls skaitlis ir vesels» - patiess.",
                  "Secība apgalvojumā maina visu."]),

    Doma("Pārbaudi ar nulli un ar negatīvajiem",
         "Apgalvojumu par skaitļu kopām pārbauda, meklējot pretpiemēru; "
         "visbiežāk tas ir nulle, negatīvs skaitlis vai daļa.",
         soli=[
             "Izlasi apgalvojumu un saproti, par kuru kopu tas runā.",
             "Pārbaudi to ar pozitīvu veselu skaitli.",
             "Pārbaudi ar nulli.",
             "Pārbaudi ar negatīvu skaitli un ar daļu.",
             "Ja kaut viens neiederas, apgalvojums ir nepatiess.",
         ],
         pieze="Apgalvojumi «katrs A ir B» un «katrs B ir A» ir divi dažādi "
               "apgalvojumi. Viens var būt patiess, otrs - nē, un tieši tur "
               "rodas lielākā daļa kļūdu."),

    Paraugs("Patiess vai nepatiess?",
            uzd="Vai apgalvojums «katrs vesels skaitlis ir naturāls» ir "
                "patiess?",
            soli=[
                ("Pārbaude ar 5: 5 ir vesels un naturāls",
                 "Pagaidām der."),
                ("Pārbaude ar 0: 0 ir vesels, bet nav naturāls",
                 "Pretpiemērs atrasts."),
                ("Apgalvojums ir nepatiess",
                 "Viens pretpiemērs pietiek."),
                ("Pretējais apgalvojums ir patiess",
                 "Katrs naturāls skaitlis ir vesels."),
            ],
            atbilde="nepatiess; pretpiemērs ir 0"),

    Ievadi("Patiess vai nepatiess?", [
        {"jaut": "«Katrs vesels skaitlis ir naturāls.» Raksti «patiess» vai "
                 "«nepatiess».",
         "atb": ["nepatiess"], "padoms": "Nulle."},
        {"jaut": "«Katrs naturāls skaitlis ir vesels.»",
         "atb": ["patiess"], "padoms": "Naturālie ietilpst veselajos."},
        {"jaut": "«Katrs vesels skaitlis ir racionāls.»",
         "atb": ["patiess"], "padoms": "Saucējs 1."},
        {"jaut": "«Katrs racionāls skaitlis ir vesels.»",
         "atb": ["nepatiess"], "padoms": "{1|2}."},
        {"jaut": "«Nulle ir vesels skaitlis.»",
         "atb": ["patiess"], "padoms": "Veselo vidū."},
        {"jaut": "«Katrs negatīvs skaitlis ir vesels.»",
         "atb": ["nepatiess"], "padoms": "−0,5."},
    ], pamats=4,
        ievads="Pirms atbildēt, pārbaudi ar nulli un ar daļu."),

    Varianti("Kur slēpjas pretpiemērs?", [
        {"jaut": "«Katrs vesels skaitlis ir naturāls.» Pretpiemērs ir...",
         "opcijas": ["0", "5", "12", "100"],
         "pareizi": 0,
         "padoms": "Naturālie sākas ar 1."},
        {"jaut": "«Katrs racionāls skaitlis ir vesels.» Pretpiemērs ir...",
         "opcijas": ["{1|2}", "3", "−4", "0"],
         "pareizi": 0,
         "padoms": "Daļa, kas nav vesels."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Katrs naturāls skaitlis ir racionāls",
                     "Katrs racionāls skaitlis ir naturāls",
                     "Katrs vesels skaitlis ir naturāls",
                     "Nulle ir naturāls skaitlis"],
         "pareizi": 0,
         "padoms": "Šaurākā kopa ietilpst plašākajā."},
        {"jaut": "Cik pretpiemēru vajag, lai apgāztu apgalvojumu?",
         "opcijas": ["Vienu", "Divus", "Visus", "Nevienu"],
         "pareizi": 0,
         "padoms": "«Katrs» nozīmē bez izņēmumiem."},
    ], pamats=4),

    Pasaule("Vai noteikums ir pareizs?",
            Ievadi("", [
                {"jaut": "«Skolēnu skaits vienmēr ir naturāls skaitlis.» "
                         "Raksti «patiess» vai «nepatiess».",
                 "atb": ["nepatiess"], "padoms": "Var būt arī nulle."},
                {"jaut": "«Temperatūra vienmēr ir vesels skaitlis.»",
                 "atb": ["nepatiess"], "padoms": "−2,5 °C."},
                {"jaut": "«Stāva numurs vienmēr ir vesels skaitlis.»",
                 "atb": ["patiess"], "padoms": "Arī pagrabstāvi."},
                {"jaut": "«Masa kilogramos vienmēr ir racionāls skaitlis.»",
                 "atb": ["patiess"], "padoms": "Mērījumu var pierakstīt kā "
                                               "daļu."},
            ]),
            pavediens="skola",
            konteksts="Noteikumos par datiem bieži ir vārds «vienmēr» - un "
                      "tieši to vērts pārbaudīt.",
            kapec="Viens pretpiemērs apgāž arī visdrošāko noteikumu."),

    Kopsavilkums([
        "Izvērtēju apgalvojumus par skaitļu kopām.",
        "Pārbaudu tos ar nulli, negatīviem skaitļiem un daļām.",
        "Atrodu pretpiemēru nepatiesam apgalvojumam.",
        "Zinu, ka «katrs A ir B» un «katrs B ir A» ir dažādi apgalvojumi.",
    ]),

    Majas([
        "Pārbaudi: «katrs daļskaitlis ir racionāls».",
        "Pārbaudi: «katrs racionāls skaitlis ir pozitīvs».",
        "Katram nepatiesajam pieraksti pretpiemēru.",
    ]),
]
