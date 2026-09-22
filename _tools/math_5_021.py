# -*- coding: utf-8 -*-
"""5. klase, 21. stunda: «Kā pierakstīt nezināmo ar burtu?»

Burts nezināmā vietā - pirmais solis uz vienādojumiem. Pati rēķināšana te
nav jauna (18. stundā trūkstošo saskaitāmo jau meklēja), jauns ir pieraksts:
vispirms uzraksti vienādību, tikai tad rēķini.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pierakstīt nezināmo ar burtu?"

MERKIS = ("Iemācīsimies apzīmēt nezināmo skaitli ar burtu, uzrakstīt "
          "vienādību un atrast nezināmā vērtību.")

SATURS = [
    Sakums("Kā uzrakstīt to, ko vēl nezini?",
           fakti=["Somā bija dažas grāmatas, ieliku vēl 3 - sanāca 11.",
                  "Cik bija sākumā? Skaitli vēl nezinām, bet pierakstīt "
                  "varam.",
                  "Nezināmo apzīmē ar burtu: x + 3 = 11."]),

    Doma("Vispirms vienādība, tikai tad rēķins",
         "Burts ir vieta, kurā skaitlis vēl nav ierakstīts - ar to drīkst "
         "rīkoties kā ar skaitli.",
         soli=[
             "Apzīmē nezināmo ar burtu un pasaki, ko tas nozīmē.",
             "Uzraksti vienādību tieši pēc teksta.",
             "Padomā, kurš darbības loceklis ir nezināms.",
             "Atrodi to: saskaitāmo - ar atņemšanu, mazināmo - ar "
             "saskaitīšanu.",
             "Ieraksti atrasto vērtību vienādībā un pārbaudi.",
         ],
         pieze="Nezināmo saskaitāmo atrod, no summas atņemot zināmo "
               "saskaitāmo; nezināmo mazināmo - starpībai pieskaitot "
               "mazinātāju; nezināmo mazinātāju - no mazināmā atņemot "
               "starpību."),

    Paraugs("No teksta uz vienādību",
            uzd="Somā bija dažas grāmatas. Ieliekot vēl 3, sanāca 11. Cik "
                "grāmatu bija sākumā?",
            soli=[
                ("x - grāmatu skaits sākumā",
                 "Vispirms pasaka, ko burts nozīmē."),
                ("x + 3 = 11",
                 "Vienādību raksta tieši pēc teksta."),
                ("x = 11 − 3 = 8",
                 "Nezināms ir saskaitāmais, tāpēc atņem."),
                ("Pārbaude: 8 + 3 = 11",
                 "Vienādība ir patiesa."),
            ],
            atbilde="sākumā bija 8 grāmatas"),

    Ievadi("Atrodi x", [
        {"jaut": "x + 3 = 11. Cik ir x?", "atb": ["8"],
         "padoms": "11 − 3."},
        {"jaut": "x + 27 = 60. Cik ir x?", "atb": ["33"],
         "padoms": "60 − 27."},
        {"jaut": "x − 15 = 40. Cik ir x?", "atb": ["55"],
         "padoms": "Nezināms ir mazināmais: 40 + 15."},
        {"jaut": "80 − x = 32. Cik ir x?", "atb": ["48"],
         "padoms": "Nezināms ir mazinātājs: 80 − 32."},
        {"jaut": "125 + x = 300. Cik ir x?", "atb": ["175"],
         "padoms": "300 − 125."},
        {"jaut": "x − 250 = 750. Cik ir x?", "atb": ["1000"],
         "padoms": "750 + 250."},
        {"jaut": "1 000 − x = 640. Cik ir x?", "atb": ["360"],
         "padoms": "1 000 − 640."},
        {"jaut": "x + x = 46. Cik ir x?", "atb": ["23"],
         "padoms": "Divi vienādi saskaitāmie: 46 : 2."},
    ], pamats=4,
        ievads="Vispirms padomā, kurš darbības loceklis ir nezināms."),

    Varianti("Kurš loceklis ir nezināms?", [
        {"jaut": "Vienādībā x + 27 = 60 nezināms ir...",
         "opcijas": ["saskaitāmais", "summa", "mazināmais", "starpība"],
         "pareizi": 0,
         "padoms": "x ir viens no diviem, ko saskaita."},
        {"jaut": "Vienādībā 80 − x = 32 nezināms ir...",
         "opcijas": ["mazinātājs", "mazināmais", "summa", "saskaitāmais"],
         "pareizi": 0,
         "padoms": "x ir tas, ko atņem."},
        {"jaut": "Kā atrod nezināmo mazināmo?",
         "opcijas": ["Starpībai pieskaita mazinātāju",
                     "No starpības atņem mazinātāju",
                     "Starpību dala ar 2",
                     "Mazinātājam pieskaita starpību un dala"],
         "pareizi": 0,
         "padoms": "Pārbaudi ar x − 15 = 40."},
        {"jaut": "«Domāju skaitli, atņēmu 12 un sanāca 30.» Kura vienādība "
                 "atbilst?",
         "opcijas": ["x − 12 = 30", "12 − x = 30", "x + 12 = 30",
                     "30 − 12 = x"],
         "pareizi": 0,
         "padoms": "No nezināmā skaitļa atņem 12."},
        {"jaut": "Kāpēc atbildi ieraksta atpakaļ vienādībā?",
         "opcijas": ["Lai pārbaudītu, vai vienādība ir patiesa",
                     "Lai atbilde izskatītos garāka",
                     "Tā prasa kārtula",
                     "Lai burts pazustu"],
         "pareizi": 0,
         "padoms": "Pārbaude pamana kļūdu, pirms to pamana kāds cits."},
        {"jaut": "Ko vispirms uzraksta, risinot teksta uzdevumu ar burtu?",
         "opcijas": ["Ko burts nozīmē", "Atbildi", "Pārbaudi",
                     "Aprēķinu"],
         "pareizi": 0,
         "padoms": "Citādi neviens nesaprot, kas ir x."},
    ], pamats=4),

    Pasaule("Cik skolēnu bija sākumā?",
            Ievadi("", [
                {"jaut": "Klasē bija x skolēni, atnāca vēl 4, sanāca 28. Cik "
                         "ir x?",
                 "atb": ["24"], "padoms": "28 − 4."},
                {"jaut": "Bibliotēkā bija x grāmatas, izsniedza 35, palika "
                         "418. Cik ir x?",
                 "atb": ["453"], "padoms": "418 + 35."},
                {"jaut": "Ēdnīcā pagatavoja 260 porcijas, palika x, izsniedza "
                         "245. Cik ir x?",
                 "atb": ["15"], "padoms": "260 − 245."},
                {"jaut": "Skolā ir x skolēni; 148 mācās sākumskolā, pārējie "
                         "312 - vecākajās klasēs. Cik ir x?",
                 "atb": ["460"], "padoms": "148 + 312."},
            ]),
            pavediens="skola",
            konteksts="Skolas skaitļi bieži zināmi no otra gala: zini "
                      "rezultātu, bet ne to, ar ko sākās.",
            kapec="Burts ļauj pierakstīt uzdevumu, pirms zini atbildi."),

    Kopsavilkums([
        "Apzīmēju nezināmo skaitli ar burtu un pasaku, ko tas nozīmē.",
        "Uzrakstu vienādību tieši pēc uzdevuma teksta.",
        "Atrodu nezināmo saskaitāmo, mazināmo vai mazinātāju.",
        "Pārbaudu atbildi, ierakstot to atpakaļ vienādībā.",
    ]),

    Majas([
        "Izdomā uzdevumu «domāju skaitli...» un uzraksti tam vienādību.",
        "Atrisini to un pārbaudi, ierakstot atbildi atpakaļ.",
        "Atrodi mājās situāciju, kurā zini rezultātu, bet ne sākumu, un "
        "pieraksti to ar burtu.",
    ]),
]
