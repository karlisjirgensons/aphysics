# -*- coding: utf-8 -*-
"""3. klase, 5. stunda: «Kā izskatās reizināšana uz skaitļu taisnes?»

Trešais reizinājuma modelis pēc grupām un taisnstūra: vienādi lēcieni pa
skaitļu taisni. Tas ir modelis, kas vēlāk pārceļas uz mērvienībām un
koordinātām, tāpēc te to iemāca ar bultām, nevis ar vārdiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, Zimejums,
                         taisne)

TEMA = "Kā izskatās reizināšana uz skaitļu taisnes?"

MERKIS = ("Attēlosim reizināšanu uz skaitļu taisnes kā vienādus lēcienus un "
          "nolasīsim no tās rezultātu.")

SATURS = [
    Sakums("Cik lēcienu pa 6 vajag, lai nonāktu līdz 30?",
           zimejums=taisne(0, 36, 6, [(30, "30")],
                           bultas=[(0, 6, "6"), (6, 12, "6"),
                                   (12, 18, "6"), (18, 24, "6"),
                                   (24, 30, "6")]),
           paraksts="Pieci vienādi lēcieni pa 6 aizved tieši līdz 30.",
           fakti=["Uz skaitļu taisnes reizināšana ir vienādi lēcieni.",
                  "Lēcienu skaits ir viens reizinātājs, lēciena garums - "
                  "otrs."]),

    Doma("Reizināt nozīmē lēkt vienādus soļus",
         "5 · 6 uz taisnes ir pieci lēcieni pa 6 - un vieta, kur tu nonāc, "
         "ir atbilde.",
         soli=[
             "Sāc no nulles.",
             "Izvēlies lēciena garumu - tas ir viens reizinātājs.",
             "Izdari tik lēcienu, cik pasaka otrs reizinātājs.",
             "Nolasi skaitli, kurā apstājies - tas ir reizinājums.",
         ],
         pieze="Dalīšana uz tās pašas taisnes ir tas pats ceļš atpakaļ: cik "
               "lēcienu pa 6 vajag, lai no 30 nonāktu nullē?"),

    Paraugs("Kur nonāk četri lēcieni pa 7?",
            uzd="Uz skaitļu taisnes izdari četrus lēcienus pa 7. Kurā "
                "skaitlī apstāsies?",
            soli=[
                ("0 → 7 → 14",
                 "Pirmie divi lēcieni aizved līdz 14."),
                ("14 → 21 → 28",
                 "Vēl divi tādi paši lēcieni."),
                ("4 · 7 = 28",
                 "Četri lēcieni pa 7 ir 28 - tur arī apstājāmies."),
            ],
            atbilde="28"),

    Zimejums("Septiņnieku lēcieni",
             taisne(0, 42, 7, [(28, "28")],
                    bultas=[(0, 7, "7"), (7, 14, "7"), (14, 21, "7"),
                            (21, 28, "7")]),
             paskaidro="Četri lēcieni pa 7 - un pietura ir tieši 28.",
             ievads="Pārbaudi: saskaiti bultas."),

    Ievadi("Kur apstāsies?", [
        {"jaut": "Trīs lēcieni pa 6 no nulles. Kurā skaitlī apstāsies?",
         "atb": ["18"], "padoms": "6, 12, 18."},
        {"jaut": "Seši lēcieni pa 5. Kurā skaitlī apstāsies?",
         "atb": ["30"], "padoms": "6 · 5."},
        {"jaut": "Cik lēcienu pa 6 vajag, lai no 0 nonāktu 42?",
         "atb": ["7"], "padoms": "42 : 6."},
        {"jaut": "Cik garš ir viens lēciens, ja 4 lēcieni aizveda līdz 24?",
         "atb": ["6"], "padoms": "24 : 4."},
        {"jaut": "Pieci lēcieni pa 7. Kurā skaitlī apstāsies?",
         "atb": ["35"], "padoms": "5 · 7."},
        {"jaut": "No 36 atpakaļ pa 6. Cik lēcienu līdz nullei?",
         "atb": ["6"], "padoms": "36 : 6."},
    ], pamats=4),

    Kustiba("Palaid roveri līdz mērķim", [
        {"jaut": "Rovers lec pa 6 metriem. Cik tālu tas aizbrauks 5 "
                 "lēcienos?",
         "atb": 30, "beigas": 60, "iedala": 6, "mers": "metri",
         "merkis": "5 lēcieni", "objekts": "Rovers",
         "padoms": "5 · 6.",
         "stasts": "Rovers pārvietojas pa vienādiem soļiem - tieši tā, kā "
                   "reizina."},
        {"jaut": "Tagad lēciens ir 7 metri, un lēcienu ir 6. Cik tālu?",
         "atb": 42, "beigas": 70, "iedala": 7, "mers": "metri",
         "merkis": "6 lēcieni", "objekts": "Rovers",
         "padoms": "6 · 7."},
        {"jaut": "Rovers apstājās pie 24 m, katrs lēciens 6 m. Cik tālu "
                 "tas tiks vēl vienā lēcienā?",
         "atb": 30, "beigas": 60, "iedala": 6, "mers": "metri",
         "merkis": "vēl viens lēciens", "objekts": "Rovers",
         "padoms": "24 + 6."},
        {"jaut": "Lēciens ir 8 metri, lēcienu skaits 5. Cik tālu?",
         "atb": 40, "beigas": 80, "iedala": 8, "mers": "metri",
         "merkis": "5 lēcieni", "objekts": "Rovers",
         "padoms": "5 · 8."},
    ], pamats=2,
        ievads="Izrēķini attālumu un spied «Palaist». Ja rēķins bija "
               "pareizs, rovers apstāsies tieši pie karodziņa."),

    Varianti("Ko rāda bultas?", [
        {"jaut": "Uz taisnes ir 4 bultas pa 6. Kurš rēķins tas ir?",
         "opcijas": ["4 · 6", "6 : 4", "4 + 6", "6 − 4"],
         "pareizi": 0, "padoms": "Bultu skaits reizināts ar bultas garumu."},
        {"jaut": "Bultas iet no 30 atpakaļ uz 0, katra pa 6. Kurš rēķins?",
         "opcijas": ["30 : 6", "30 · 6", "30 + 6", "6 : 30"],
         "pareizi": 0, "padoms": "Ceļš atpakaļ ir dalīšana."},
        {"jaut": "Kurš skaitlis *nav* uz sešnieku lēcienu ceļa?",
         "opcijas": ["20", "18", "24", "30"],
         "pareizi": 0, "padoms": "Visas pieturas dalās ar 6."},
        {"jaut": "Septiņi lēcieni pa 6 - kurā skaitlī apstāsies?",
         "opcijas": ["42", "13", "36", "48"],
         "pareizi": 0, "padoms": "7 · 6."},
    ], pamats=4),

    Pasaule("Cik tālu aizlec vardīte?",
            Ievadi("", [
                {"jaut": "Varde lec pa 6 cm. Cik tālu tā tiks 4 lēcienos?",
                 "atb": ["24"], "padoms": "4 · 6.", "mers": "atbilde "
                                                            "centimetros"},
                {"jaut": "Cik tālu varde tiks 8 lēcienos?",
                 "atb": ["48"], "padoms": "8 · 6."},
                {"jaut": "Varde nokļuva 54 cm tālu. Cik lēcienu tā izdarīja?",
                 "atb": ["9"], "padoms": "54 : 6."},
                {"jaut": "Otra varde lec pa 7 cm un izdarīja 5 lēcienus. "
                         "Cik tālu tā ir?",
                 "atb": ["35"], "padoms": "5 · 7."},
            ]),
            pavediens="daba",
            konteksts="Vardes lēciens ir gandrīz vienāds katru reizi - tāpēc "
                      "ceļu var izrēķināt, nevis izmērīt.",
            kapec="Vienādi soļi vienmēr nozīmē reizināšanu."),

    Kopsavilkums([
        "Attēloju reizināšanu uz skaitļu taisnes ar vienādiem lēcieniem.",
        "Nolasu no taisnes reizinājumu un lēcienu skaitu.",
        "Zinu, ka ceļš atpakaļ pa tiem pašiem lēcieniem ir dalīšana.",
        "Pārbaudu rezultātu ar reizināšanas tabulu.",
    ]),

    Majas([
        "Uzzīmē skaitļu taisni no 0 līdz 60 un iezīmē uz tās sešnieku "
        "lēcienus.",
        "Izmēri savu soli un izrēķini, cik tālu tiksi 10 soļos.",
        "Uzzīmē taisni, kurā lēciens ir 7, un pieraksti visas pieturas.",
    ]),
]
