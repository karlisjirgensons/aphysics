# -*- coding: utf-8 -*-
"""3. klase, 26. stunda: «Kāpēc drīkst reizināt pa daļām?»

Iepriekšējā stundā paņēmienu lietoja, šajā to pamato. Modelis ir taisnstūris,
ko pārgriež ar vienu līniju: rūtiņu skaits nemainās, tāpēc (a + b) · c ir tas
pats, kas a · c + b · c. Šo īpašību skolēns formulē saviem vārdiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāpēc drīkst reizināt pa daļām?"

MERKIS = ("Ar modeli formulēsim īpašību (a + b) · c = a · c + b · c saviem "
          "vārdiem.")

SATURS = [
    Sakums("Kas notiek, ja taisnstūri pārgriež uz pusēm?",
           zimejums=restis([["", "", "", "|", "", ""],
                            ["", "", "", "|", "", ""],
                            ["", "", "", "|", "", ""]],
                           "3 rindas pa 6 = 3 · 3 + 3 · 3"),
           paraksts="Griežot pa vidu, rūtiņu skaits nemainās.",
           fakti=["Taisnstūri var pārgriezt jebkurā vietā.",
                  "Abu gabalu rūtiņas kopā ir tikpat, cik bija sākumā."]),

    Doma("Sadalīts reizinātājs - sadalīts reizinājums",
         "(a + b) · c = a · c + b · c - ja vienu reizinātāju sadala, tad abas "
         "daļas reizina atsevišķi un rezultātus saskaita.",
         soli=[
             "Uzzīmē taisnstūri ar malām (a + b) un c.",
             "Pārgriez to ar vienu līniju: sanāk a · c un b · c.",
             "Saskaiti abu gabalu rūtiņas.",
             "Salīdzini ar visa taisnstūra rūtiņu skaitu - tas ir tas pats.",
         ],
         pieze="Tieši tāpēc drīkst rēķināt 23 · 2 = 20 · 2 + 3 · 2. Sadalīt "
               "var arī citādi: 23 = 25 − 2, un tad 23 · 2 = 50 − 4."),

    Paraugs("Kāpēc 14 · 3 = 10 · 3 + 4 · 3?",
            uzd="Pamato ar taisnstūri, kāpēc 14 · 3 var rēķināt pa daļām.",
            soli=[
                ("Taisnstūris 14 x 3",
                 "Tajā ir 14 rūtiņas rindā un 3 rindas."),
                ("Pārgriež pēc desmitās kolonnas",
                 "Sanāk divi gabali: 10 x 3 un 4 x 3."),
                ("30 + 12 = 42",
                 "Abu gabalu rūtiņas kopā."),
                ("14 · 3 = 42",
                 "Tikpat, cik bija visā taisnstūrī - griezums neko "
                 "nemainīja."),
            ],
            atbilde="42"),

    Petijums("Pārgriez taisnstūri pats",
             vajag="rūtiņu lapa, šķēres un zīmulis",
             soli=[
                 "Uzzīmē un izgriez taisnstūri 12 rūtiņas platu un 4 augstu.",
                 "Saskaiti rūtiņas un pieraksti reizinājumu.",
                 "Pārgriez to pēc septītās kolonnas.",
                 "Saskaiti abu gabalu rūtiņas atsevišķi un saskaiti kopā.",
             ],
             secinajums="12 · 4 = 7 · 4 + 5 · 4 - griezuma vieta neko "
                        "nemaina, kopskaits paliek 48."),

    Ievadi("Rēķini pa daļām", [
        {"jaut": "13 · 4 = 10 · 4 + 3 · 4. Cik tas ir?", "atb": ["52"],
         "padoms": "40 + 12."},
        {"jaut": "17 · 3 = 10 · 3 + 7 · 3. Cik tas ir?", "atb": ["51"],
         "padoms": "30 + 21."},
        {"jaut": "19 · 5 = 20 · 5 − 1 · 5. Cik tas ir?", "atb": ["95"],
         "padoms": "100 − 5."},
        {"jaut": "16 · 6 = 10 · 6 + 6 · 6. Cik tas ir?", "atb": ["96"],
         "padoms": "60 + 36."},
        {"jaut": "29 · 3 = 30 · 3 − 1 · 3. Cik tas ir?", "atb": ["87"],
         "padoms": "90 − 3."},
        {"jaut": "21 · 4 = 20 · 4 + 1 · 4. Cik tas ir?", "atb": ["84"],
         "padoms": "80 + 4."},
    ], pamats=4),

    Zimejums("Divi gabali, viens taisnstūris",
             restis([["10 · 3 = 30", "4 · 3 = 12"],
                     ["kreisais gabals", "labais gabals"]],
                    "14 · 3 = 42"),
             paskaidro="Griezuma vietu var izvēlēties pats - svarīgi tikai, "
                       "lai abas daļas kopā dotu sākotnējo skaitli.",
             ievads="Tas pats taisnstūris, sadalīts divās daļās."),

    Varianti("Vai sadalījums ir pareizs?", [
        {"jaut": "Kurš rēķins ir vienāds ar 15 · 4?",
         "opcijas": ["10 · 4 + 5 · 4", "10 · 4 + 5", "15 + 4 · 4",
                     "1 · 4 + 5 · 4"],
         "pareizi": 0, "padoms": "Abas daļas reizina ar 4."},
        {"jaut": "Kurš rēķins ir vienāds ar 18 · 5?",
         "opcijas": ["20 · 5 − 2 · 5", "20 · 5 − 2", "18 + 5 · 5",
                     "10 · 5 + 8"],
         "pareizi": 0, "padoms": "18 = 20 − 2, un abas daļas reizina."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Sadalīt drīkst jebkurā vietā",
                     "Sadalīt drīkst tikai pa vidu",
                     "Sadalīt drīkst tikai desmitos un vienos",
                     "Sadalīt nedrīkst"],
         "pareizi": 0, "padoms": "Griezuma vieta neko nemaina."},
        {"jaut": "Cik ir 11 · 7?",
         "opcijas": ["77", "70", "18", "87"],
         "pareizi": 0, "padoms": "70 + 7."},
    ], pamats=4),

    Pasaule("Cik maksā pirkums, ja cena ir neveikla?",
            Ievadi("", [
                {"jaut": "Prece maksā 19 ct. Cik maksā 4 gabali? (Rēķini "
                         "20 · 4 − 4.)",
                 "atb": ["76"], "padoms": "80 − 4."},
                {"jaut": "Prece maksā 29 ct. Cik maksā 3 gabali?",
                 "atb": ["87"], "padoms": "90 − 3."},
                {"jaut": "Prece maksā 21 ct. Cik maksā 5 gabali?",
                 "atb": ["105"], "padoms": "100 + 5."},
                {"jaut": "Par cik lētāk iznāk 4 preces pa 19 ct nekā pa "
                         "21 ct?",
                 "atb": ["8"], "padoms": "84 − 76."},
            ]),
            pavediens="veikals",
            konteksts="Cenas veikalā bieži ir tuvu apaļam skaitlim - 19, 29, "
                      "99 -, un tieši tad noder sadalīšana.",
            kapec="Rēķinot no apaļa skaitļa, summu var pateikt galvā."),

    Kopsavilkums([
        "Formulēju savos vārdos īpašību (a + b) · c = a · c + b · c.",
        "Pamatoju to ar pārgrieztu taisnstūri.",
        "Sadalu reizinātāju sev ērtākajā vietā.",
        "Rēķinu arī no apaļa skaitļa, atņemot lieko.",
    ]),

    Majas([
        "Izrēķini 18 · 4 divos veidos: no 10 + 8 un no 20 − 2.",
        "Uzzīmē taisnstūri 13 x 3 un sadali to divos gabalos.",
        "Pastāsti mājiniekiem, kāpēc griezuma vieta neko nemaina.",
    ]),
]
