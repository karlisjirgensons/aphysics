# -*- coding: utf-8 -*-
"""4. klase, 53. stunda: «Kur paralēlas līnijas ir telpiskos ķermeņos?»

Mikrotemata noslēgums: no plaknes uz telpu. Kvadram (taisnstūra
paralēlskaldnim) šķautnes sagrupējas trīs četrinieku grupās - katrā grupā
visas paralēlas. Tas palīdz uzzīmēt kasti pareizi: paralēlās šķautnes
zīmējumā arī paliek paralēlas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis, restis)

TEMA = "Kur paralēlas līnijas ir telpiskos ķermeņos?"

MERKIS = ("Saskatīsim paralēlas šķautnes taisnstūra paralēlskaldnī un "
          "raksturosim tās.")

SATURS = [
    Sakums("Cik šķautņu ir kurpju kastei?",
           zimejums=kermenis("kvadrs"),
           paraksts="Taisnstūra paralēlskaldnis - 12 šķautnes.",
           fakti=["12 šķautnes sadalās 3 grupās pa 4.",
                  "Katrā grupā visas 4 šķautnes ir paralēlas.",
                  "Punktētās šķautnes ir aizmugurē - tās neredz."]),

    Doma("Trīs virzieni - trīs paralēlu šķautņu grupas",
         "Taisnstūra paralēlskaldnim ir 4 garuma, 4 platuma un 4 augstuma "
         "šķautnes; vienas grupas šķautnes ir paralēlas.",
         soli=[
             "Atrodi 4 šķautnes, kas iet «uz sāniem» - garums.",
             "Atrodi 4 šķautnes, kas iet «uz aizmuguri» - platums.",
             "Atrodi 4 šķautnes, kas iet «uz augšu» - augstums.",
             "Katrā virsotnē satiekas pa vienai no katras grupas - tās ir "
             "perpendikulāras.",
         ],
         pieze="Zīmējot kasti, paralēlās šķautnes zīmē paralēlas - tāpēc "
               "zīmējums izskatās telpisks."),

    Paraugs("Šķautņu garumu summa",
            uzd="Kastei garums 30 cm, platums 20 cm, augstums 10 cm. Cik "
                "garas ir visas šķautnes kopā?",
            soli=[
                ("4 · 30 = 120", "Garuma šķautnes."),
                ("4 · 20 = 80", "Platuma šķautnes."),
                ("4 · 10 = 40", "Augstuma šķautnes."),
                ("120 + 80 + 40 = 240", None),
            ],
            atbilde="240 cm"),

    Zimejums("Šķautņu grupas",
             restis([["grupa", "cik", "garums"],
                     ["garums", 4, "30 cm"],
                     ["platums", 4, "20 cm"],
                     ["augstums", 4, "10 cm"],
                     ["kopā", 12, "240 cm"]],
                    "kurpju kaste"),
             paskaidro="12 šķautnes = 3 grupas pa 4 paralēlām.",
             ievads="Tabula apkopo, cik šķautņu katrā virzienā."),

    Ievadi("Saskaiti", [
        {"jaut": "Cik virsotņu ir kvadram?", "atb": ["8"],
         "padoms": "4 augšā, 4 apakšā."},
        {"jaut": "Cik skaldņu ir kvadram?", "atb": ["6"],
         "padoms": "Augša, apakša, 4 sāni."},
        {"jaut": "Kubam šķautne 5 cm. Cik garas visas šķautnes kopā?",
         "atb": ["60"], "padoms": "12 · 5."},
        {"jaut": "Cik šķautņu ir paralēlas vienai dotajai šķautnei (bez "
                 "tās pašas)?",
         "atb": ["3"], "padoms": "Grupā 4, viena ir pati."},
    ]),

    Varianti("Paralēlas vai nē?", [
        {"jaut": "Kastes augšējā priekšējā šķautne un apakšējā priekšējā",
         "opcijas": ["paralēlas", "perpendikulāras", "krustojas slīpi"],
         "pareizi": 0, "padoms": "Abas iet uz sāniem."},
        {"jaut": "Augšējā priekšējā šķautne un kreisā priekšējā šķautne",
         "opcijas": ["perpendikulāras", "paralēlas", "nesatiekas"],
         "pareizi": 0, "padoms": "Satiekas virsotnē taisnā leņķī."},
        {"jaut": "Kurš ķermenis nav ar paralēlām šķautnēm visās grupās?",
         "opcijas": ["piramīda", "kubs", "kvadrs"], "pareizi": 0,
         "padoms": "Piramīdas sānu šķautnes satiekas virsotnē."},
    ]),

    Pasaule("Akvārija rāmis",
            Ievadi("", [
                {"jaut": "Akvārija rāmis: garums 60 cm, platums 30 cm, "
                         "augstums 40 cm. Cik cm alumīnija profila vajag?",
                 "atb": ["520"], "padoms": "4 · 60 + 4 · 30 + 4 · 40."},
                {"jaut": "Profils maksā 2 € par 10 cm. Cik maksā 520 cm?",
                 "atb": ["104"], "padoms": "520 : 10 · 2."},
                {"jaut": "Cik stūra savienojumu vajag (pa vienam katrā "
                         "virsotnē)?",
                 "atb": ["8"], "padoms": "Virsotņu skaits."},
                {"jaut": "Cik stikla plākšņu vajag, ja augšā vāka nav?",
                 "atb": ["5"], "padoms": "6 skaldnes − 1."},
            ]),
            pavediens="maja",
            konteksts="Akvārija rāmi būvē no 12 profiliem - trīs grupas pa "
                      "četriem vienādiem.",
            kapec="Paralēlo šķautņu grupas ļauj ātri saskaitīt materiālu."),

    Petijums("Kastes izpēte",
             soli=[
                 "Paņem kasti (piemēram, no apaviem vai tējas).",
                 "Ar krāsainiem uzlīmēm atzīmē 3 šķautņu grupas.",
                 "Izmēri katras grupas vienu šķautni.",
                 "Aprēķini visu šķautņu garumu summu.",
             ],
             vajag="kaste, lineāls, uzlīmes vai krāsaini zīmuļi",
             secinajums="Kastei ir tikai 3 dažādi šķautņu garumi."),

    Kopsavilkums([
        "Atrodu paralēlas šķautnes kvadrā.",
        "Zinu, ka 12 šķautnes veido 3 grupas pa 4.",
        "Aprēķinu visu šķautņu garumu summu.",
    ]),

    Majas([
        "Atrodi mājās 3 kastes un izmēri to šķautnes.",
        "Uzzīmē kasti, paralēlās šķautnes zīmējot paralēlas.",
        "Aprēķini, cik lentes vajag, lai aplīmētu visas kastes šķautnes.",
    ]),
]
