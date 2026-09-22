# -*- coding: utf-8 -*-
"""6. klase, 118. stunda: «Kā uzzīmēt daudzstūri pēc koordinātām?»

Pretējais virziens: koordinātas ir dotas, figūra jāuzzīmē. Te parādās arī
secība - virsotnes savieno tādā kārtībā, kādā tās uzskaitītas, un cita
secība dod citu figūru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kā uzzīmēt daudzstūri pēc koordinātām?"

MERKIS = ("Iemācīsimies atlikt punktus un zīmēt nogriezni vai daudzstūri pēc "
          "virsotņu koordinātām.")

SATURS = [
    Sakums("Četri punkti, viens taisnstūris",
           zimejums=plakne(lauzta=[(-3, 2), (3, 2), (3, -2), (-3, -2)],
                           aizpildi=True, no_x=-4, lidz_x=4, no_y=-4,
                           lidz_y=4, solis=1),
           paraksts="Virsotnes (−3; 2), (3; 2), (3; −2), (−3; −2) savienotas "
                    "pēc kārtas dod taisnstūri.",
           fakti=["Virsotnes savieno tādā secībā, kādā tās uzskaitītas.",
                  "Pēdējo virsotni savieno ar pirmo.",
                  "Cita secība dod citu figūru."]),

    Doma("Atliec visas virsotnes, tad savieno",
         "Daudzstūri zīmē divos soļos: vispirms atliek visas virsotnes, tad "
         "savieno tās pēc kārtas un noslēdz figūru.",
         soli=[
             "Atliec katru virsotni un apzīmē to ar burtu.",
             "Pārbaudi, vai visas koordinātas ir pareizi nolasītas.",
             "Savieno virsotnes tādā secībā, kādā tās dotas.",
             "Savieno pēdējo ar pirmo.",
             "Nosaki, kāda figūra sanāca.",
         ],
         pieze="Ja virsotnes savieno citā secībā, var sanākt figūra ar "
               "krustotām malām. Tāpēc secība nav nejauša - tā ir daļa no "
               "uzdevuma."),

    Paraugs("Uzzīmē taisnstūri",
            uzd="Uzzīmē figūru ar virsotnēm A(−3; 2), B(3; 2), C(3; −2), "
                "D(−3; −2).",
            soli=[
                ("A ir 3 pa kreisi, 2 uz augšu",
                 "Pirmā virsotne."),
                ("B ir 3 pa labi, 2 uz augšu",
                 "AB ir horizontāls nogrieznis."),
                ("C ir 3 pa labi, 2 uz leju",
                 "BC ir vertikāls."),
                ("D ir 3 pa kreisi, 2 uz leju",
                 "CD horizontāls, DA vertikāls."),
                ("Sanāk taisnstūris 6 x 4",
                 "Malas ir 6 un 4 vienības."),
            ],
            atbilde="taisnstūris ar malām 6 un 4"),

    Ievadi("Aprēķini figūras izmērus", [
        {"jaut": "A(−3; 2) un B(3; 2). Cik vienības gara ir mala AB?",
         "atb": ["6"], "padoms": "No −3 līdz 3."},
        {"jaut": "B(3; 2) un C(3; −2). Cik vienības gara ir mala BC?",
         "atb": ["4"], "padoms": "No 2 līdz −2."},
        {"jaut": "Cik vienību ir taisnstūra perimetrs?",
         "atb": ["20"], "padoms": "2 · (6 + 4)."},
        {"jaut": "Cik kvadrātvienību ir tā laukums?",
         "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "Punkti (0; 0), (4; 0) un (0; 3). Cik vienības gara ir mala "
                 "uz horizontālās ass?",
         "atb": ["4"], "padoms": "No 0 līdz 4."},
        {"jaut": "Cik kvadrātvienību ir šī trīsstūra laukums?",
         "atb": ["6"], "padoms": "Puse no 4 · 3."},
    ], pamats=4),

    Petijums("Uzzīmē figūru pēc koordinātām",
             vajag="rūtiņu lapa, lineāls",
             soli=[
                 "Uzzīmē koordinātu plakni no −5 līdz 5.",
                 "Atliec punktus (−4; 1), (0; 4), (4; 1), (2; −3), (−2; −3).",
                 "Savieno tos pēc kārtas un noslēdz figūru.",
                 "Nosaki, cik malu ir figūrai.",
                 "Pamēģini savienot tos citā secībā un salīdzini.",
             ],
             secinajums="Tās pašas piecas virsotnes citā secībā dod figūru ar "
                        "krustotām malām - tāpēc secība ir svarīga."),

    Varianti("Kāda figūra sanāks?", [
        {"jaut": "Virsotnes (−3; 2), (3; 2), (3; −2), (−3; −2) dod...",
         "opcijas": ["taisnstūri", "trīsstūri", "kvadrātu", "rombu"],
         "pareizi": 0,
         "padoms": "Malas 6 un 4."},
        {"jaut": "Virsotnes (0; 0), (4; 0), (0; 3) dod...",
         "opcijas": ["trīsstūri", "taisnstūri", "nogriezni", "kvadrātu"],
         "pareizi": 0,
         "padoms": "Trīs virsotnes."},
        {"jaut": "Ja virsotnes savieno citā secībā, sanāk...",
         "opcijas": ["cita figūra", "tā pati figūra",
                     "nekas", "vienmēr trīsstūris"],
         "pareizi": 0,
         "padoms": "Malas var krustoties."},
        {"jaut": "Virsotnes (−2; 2), (2; 2), (2; −2), (−2; −2) dod...",
         "opcijas": ["kvadrātu", "taisnstūri, kas nav kvadrāts",
                     "trīsstūri", "piecstūri"],
         "pareizi": 0,
         "padoms": "Abas malas ir 4."},
    ], pamats=4),

    Pasaule("Kā uzzīmēt laukuma plānu?",
            Ievadi("", [
                {"jaut": "Laukuma stūri ir (0; 0), (8; 0), (8; 5), (0; 5). "
                         "Cik vienības garš ir laukums?",
                 "atb": ["8"], "padoms": "No 0 līdz 8."},
                {"jaut": "Cik vienības plats tas ir?",
                 "atb": ["5"], "padoms": "No 0 līdz 5."},
                {"jaut": "Cik kvadrātvienību ir tā laukums?",
                 "atb": ["40"], "padoms": "8 · 5."},
                {"jaut": "Ja viena vienība ir 10 m, cik kvadrātmetru ir "
                         "laukums?",
                 "atb": ["4000", "4 000"], "padoms": "80 m · 50 m."},
            ]),
            pavediens="sports",
            konteksts="Sporta laukuma plānu zīmē koordinātu plaknē, un no "
                      "virsotņu koordinātām uzreiz redz izmērus.",
            kapec="Malas garums ir koordinātu starpība."),

    Zimejums("Trīsstūris plaknē",
             plakne(lauzta=[(0, 0), (4, 0), (0, 3)], aizpildi=True,
                    no_x=-2, lidz_x=5, no_y=-2, lidz_y=4, solis=1),
             paskaidro="Trīs virsotnes un trīs malas. Katetes ir 4 un 3 "
                       "vienības garas.",
             ievads="Ar trim virsotnēm pietiek trīsstūrim."),

    Kopsavilkums([
        "Atlieku punktus pēc dotajām koordinātām.",
        "Savienoju virsotnes pareizā secībā un noslēdzu figūru.",
        "Nosaku malu garumus kā koordinātu starpības.",
        "Aprēķinu figūras perimetru un laukumu.",
    ]),

    Majas([
        "Uzzīmē figūru ar virsotnēm (−2; −1), (3; −1), (3; 2), (−2; 2).",
        "Aprēķini tās perimetru un laukumu.",
        "Izdomā četras virsotnes, kas dod kvadrātu.",
    ]),
]
