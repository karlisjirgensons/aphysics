# -*- coding: utf-8 -*-
"""4. klase, 142. stunda: «Vai apgalvojums ir patiess?»

Mikrotemata noslēgums. «Lielāks laukums - lielāks perimetrs» izklausās
loģiski, bet ir aplams: 1 × 12 un 3 × 4. Viens pretpiemērs pietiek - tā
pati spriešanas metode, ko 68. stundā lietoja leņķiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Vai apgalvojums ir patiess?"

MERKIS = ("Ar pretpiemēru pamatosim, ka apgalvojums par laukumu un "
          "perimetru nav patiess.")

SATURS = [
    Sakums("Vai vienlieliem taisnstūriem vienāds perimetrs?",
           zimejums=restis([["taisnstūris", "laukums", "perimetrs"],
                            ["1 × 12", 12, 26],
                            ["2 × 6", 12, 16],
                            ["3 × 4", 12, 14]],
                           "viens laukums - trīs perimetri"),
           fakti=["Visiem laukums 12, perimetri dažādi.",
                  "Tātad apgalvojums ir aplams."]),

    Doma("Pretpiemērs atspēko",
         "Lai pierādītu, ka apgalvojums par laukumu un perimetru nav "
         "vienmēr patiess, pietiek ar vienu gadījumu, kurā tas neizpildās.",
         soli=[
             "Izlasi apgalvojumu: «vienmēr», «katrs».",
             "Izmēģini dažādus taisnstūrus.",
             "Atrodi gadījumu, kur apgalvojums neizpildās.",
             "Uzraksti pretpiemēru ar skaitļiem.",
         ],
         pieze="Kvadrātam ir mazākais perimetrs starp vienlieliem "
               "taisnstūriem."),

    Paraugs("Atspēko",
            uzd="«Ja laukums lielāks, arī perimetrs lielāks.» Patiess?",
            soli=[
                ("1 × 10: S = 10, P = 22", None),
                ("4 × 4: S = 16, P = 16", None),
                ("16 > 10, bet 16 < 22", "Pretpiemērs."),
            ],
            atbilde="aplams"),

    Varianti("Patiess vai aplams?", [
        {"jaut": "Vienlieliem taisnstūriem vienmēr vienāds perimetrs.",
         "opcijas": ["aplams", "patiess"], "pareizi": 0,
         "padoms": "1 × 12 un 3 × 4."},
        {"jaut": "Kvadrātam ar malu 4 laukums un perimetrs ir vienādi "
                 "skaitļi.",
         "opcijas": ["patiess", "aplams"], "pareizi": 0,
         "padoms": "16 un 16."},
        {"jaut": "Ja taisnstūra malas palielina, laukums palielinās.",
         "opcijas": ["patiess", "aplams"], "pareizi": 0,
         "padoms": "Vairāk rūtiņu."},
        {"jaut": "Taisnstūriem ar vienādu perimetru ir vienāds laukums.",
         "opcijas": ["aplams", "patiess"], "pareizi": 0,
         "padoms": "1 × 5 un 3 × 3: P = 12, S = 5 un 9."},
    ], pamats=4),

    Ievadi("Pretpiemēri", [
        {"jaut": "Taisnstūra 1 × 12 perimetrs?", "atb": ["26"],
         "padoms": "1 + 12 + 1 + 12."},
        {"jaut": "Taisnstūra 3 × 4 perimetrs?", "atb": ["14"],
         "padoms": "3 + 4 + 3 + 4."},
        {"jaut": "Perimetrs 12. Kvadrāta laukums?", "atb": ["9"],
         "padoms": "Mala 3."},
        {"jaut": "Perimetrs 12, malas 1 un 5. Laukums?", "atb": ["5"],
         "padoms": "1 · 5."},
    ]),

    Pasaule("Žogs aitu aplokam",
            Ievadi("", [
                {"jaut": "Zemniekam 20 m žoga. Aploks 1 × 9 m. Laukums m²?",
                 "atb": ["9"], "padoms": "1 · 9."},
                {"jaut": "Tas pats žogs, aploks 5 × 5 m. Laukums?",
                 "atb": ["25"], "padoms": "5 · 5."},
                {"jaut": "Tas pats žogs, aploks 4 × 6 m. Laukums?",
                 "atb": ["24"], "padoms": "4 · 6."},
                {"jaut": "Kurš aploks aitām labākais? Ieraksti laukumu.",
                 "atb": ["25"], "padoms": "Kvadrāts - lielākais laukums."},
            ]),
            pavediens="daba",
            konteksts="Ar vienu un to pašu žoga garumu var iežogot ļoti "
                      "atšķirīgu laukumu.",
            kapec="Perimetrs un laukums ir dažādas lietas."),

    Kopsavilkums([
        "Atrodu pretpiemēru apgalvojumam par laukumu un perimetru.",
        "Zinu, ka vienlieliem taisnstūriem perimetrs var atšķirties.",
        "Zinu, ka kvadrātam perimetrs ir mazākais.",
    ]),

    Majas([
        "Ar 24 sērkociņiem saliec dažādus taisnstūrus - kuram lielākais "
        "laukums?",
        "Izdomā vienu aplamu apgalvojumu par laukumu un atspēko to.",
        "Atkārto: vienlielas figūras, sadalīšana, trijstūris.",
    ]),
]
