# -*- coding: utf-8 -*-
"""9. klase, 6. stunda: «Kā lietot viduslīniju aprēķinos?»

Mikrotemata noslēgums: viduslīniju trijstūra perimetrs ir puse no lielā,
viduslīnija četrstūrī (Varinjona paralelograms) un eksāmena formāta
uzdevumi ar pamatojumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā lietot viduslīniju aprēķinos?"

MERKIS = ("Aprēķināsim nezināmos lielumus, lietojot viduslīnijas īpašību.")

SATURS = [
    Sakums("Cik garš ir mazā trijstūra perimetrs?",
           zimejums=geometrija([("A", 0, 0), ("B", 10, 0), ("C", 3, 7),
                                ("M", 1.5, 3.5), ("N", 6.5, 3.5),
                                ("K", 5, 0)],
                               nogriezni=["AB", "BC", "CA"],
                               izcelti=["MN", "NK", "KM"],
                               iekrasot=[("KNM", 1)]),
           paraksts="Katra viduslīnija ir puse no kādas malas.",
           fakti=["Viduslīniju trijstūra perimetrs = puse no P_{ABC}.",
                  "Tā laukums ir ceturtdaļa no S_{ABC}.",
                  "Viduslīnija palīdz arī četrstūrī."]),

    Doma("Ko var aprēķināt",
         "MN = {AB|2}, tāpēc no viena lieluma iegūst otru; leņķi pie MN ir "
         "tādi paši kā pie AB.",
         soli=[
             "Uzzīmē skici un atzīmē viduspunktus.",
             "Nosauc, pretī kurai malai ir viduslīnija.",
             "Pieraksti MN = {AB|2} ar konkrētiem burtiem.",
             "Leņķiem izmanto paralēlās taisnes MN ∥ AB.",
         ]),

    Paraugs("Četrstūra malu viduspunkti",
            uzd="Četrstūra ABCD diagonāles ir AC = 10 cm un BD = 8 cm. Malu "
                "viduspunkti ir K, L, M, N. Atrodi KLMN perimetru.",
            soli=[
                ("KL = {AC|2} = 5 cm, MN = {AC|2} = 5 cm",
                 "Viduslīnijas trijstūros ABC un ACD."),
                ("LM = {BD|2} = 4 cm, NK = {BD|2} = 4 cm",
                 "Viduslīnijas trijstūros BCD un ABD."),
                ("P = 5 + 4 + 5 + 4 = 18 cm", "Perimetrs = AC + BD."),
            ],
            atbilde="18 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Trijstūra malas 8, 10 un 12 cm. Viduslīniju trijstūra "
                 "perimetrs (cm)?", "atb": ["15"],
         "padoms": "Puse no 30."},
        {"jaut": "Viduslīniju trijstūra perimetrs 11 cm. Lielā trijstūra "
                 "perimetrs (cm)?", "atb": ["22"], "padoms": "Divreiz."},
        {"jaut": "Vienādmalu trijstūra mala 9 cm. Viduslīnija (cm)?",
         "atb": ["4,5"], "padoms": "9 : 2."},
        {"jaut": "Vienādsānu trijstūrī sānu mala 10 cm, pamats 12 cm. "
                 "Viduslīnija, kas paralēla pamatam (cm)?", "atb": ["6"],
         "padoms": "Puse no pamata."},
        {"jaut": "Trijstūra laukums 36 cm². Viduslīniju trijstūra laukums "
                 "(cm²)?", "atb": ["9"], "padoms": "4 vienādi trijstūri."},
        {"jaut": "Četrstūra diagonāles 7 cm un 9 cm. Viduspunktu "
                 "četrstūra perimetrs (cm)?", "atb": ["16"],
         "padoms": "AC + BD."},
    ], pamats=4),

    Varianti("Kurš secinājums ir pamatots?", [
        {"jaut": "MN - viduslīnija, MN = 7 cm. Kas der?",
         "opcijas": ["Pretējā mala ir 14 cm", "Visas malas ir 14 cm",
                     "Perimetrs ir 21 cm", "Pretējā mala ir 3,5 cm"],
         "pareizi": 0, "padoms": "Zinām tikai paralēlo malu."},
        {"jaut": "Četrstūra malu viduspunkti vienmēr veido...",
         "opcijas": ["paralelogramu", "kvadrātu", "taisnstūri", "trapeci"],
         "pareizi": 0, "padoms": "Pretējās malas ir paralēlas vienai "
                                 "diagonālei."},
    ]),

    Pasaule("Parka celiņi",
            Ievadi("", [
                {"jaut": "Trijstūra parka malas 120 m, 160 m un 200 m. Iekšējo "
                         "celiņu trijstūris savieno malu viduspunktus. Celiņu "
                         "kopgarums (m)?", "atb": ["240"],
                 "padoms": "Puse no 480."},
                {"jaut": "Bruģis maksā 45 € par metru. Cik € maksā celiņi?",
                 "atb": ["10800", "10 800"], "padoms": "240 · 45."},
                {"jaut": "Parka laukums ir 9600 m². Cik m² aizņem vidējais "
                         "trijstūris?", "atb": ["2400"],
                 "padoms": "Ceturtdaļa."},
            ]),
            pavediens="maja",
            konteksts="Pilsētas parks ir trijstūra formā; celiņi savieno "
                      "malu viduspunktus.",
            kapec="Tāmi sastāda bez mērīšanas dabā."),

    Kopsavilkums([
        "Aprēķinu viduslīniju un pretējo malu.",
        "Zinu viduslīniju trijstūra perimetru un laukumu.",
        "Lietoju viduslīnijas četrstūrī.",
    ]),

    Majas([
        "Trijstūra perimetrs 34 cm. Aprēķini viduslīniju trijstūra perimetru.",
        "Uzzīmē četrstūri, savieno malu viduspunktus un pārbaudi, ka iznāk "
        "paralelograms.",
        "Kāds četrstūris jāņem, lai viduspunkti veidotu taisnstūri?",
    ]),
]
