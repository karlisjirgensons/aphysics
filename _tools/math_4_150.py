# -*- coding: utf-8 -*-
"""4. klase, 150. stunda: «Kā sadalīt figūru taisnstūros?»

Kombinēta figūra («L», «T», «U» forma) sadalās taisnstūros; laukums ir to
laukumu summa. Griezumu var likt dažādi - atbildei jāsanāk vienādai. Tā ir
laukuma aditivitāte, ko lieto visā ģeometrijā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kā sadalīt figūru taisnstūros?"

MERKIS = ("Aprēķināsim kombinētas figūras laukumu kā divu taisnstūru "
          "laukumu summu.")

SATURS = [
    Sakums("Cik liela ir «L» formas istaba?",
           zimejums=figura([(0, 0), (8, 0), (8, 3), (3, 3), (3, 6), (0, 6),
                            (0, 3), (3, 3)],
                           uzraksti=[(4, -0.5, "8"), (8.6, 1.5, "3"),
                                     (1.5, 6.5, "3"), (-0.6, 4.5, "3")],
                           platums=9, augstums=7),
           paraksts="8 · 3 = 24 un 3 · 3 = 9. Kopā 33.",
           fakti=["«L» sadalās divos taisnstūros.",
                  "Laukumu summa ir visa figūras laukums."]),

    Doma("Sadali, aprēķini, saskaiti",
         "Kombinētas figūras laukums ir to taisnstūru laukumu summa, kuros "
         "figūru sadala.",
         soli=[
             "Novelc līniju, kas sadala figūru taisnstūros.",
             "Atrodi katra taisnstūra malas (dažas jāizrēķina!).",
             "Aprēķini katra laukumu.",
             "Saskaiti. Pārbaudi ar citu griezumu.",
         ],
         pieze="Trūkstošo malu atrod no zināmajām: ja visa mala 6 un daļa 3, "
               "otra daļa 3."),

    Paraugs("«L» divos veidos",
            uzd="Figūra «L»: apakšā 8 × 3, virs kreisās daļas 3 × 3. "
                "Laukums?",
            soli=[
                ("8 · 3 = 24", "Apakšējais taisnstūris."),
                ("3 · 3 = 9", "Augšējais."),
                ("24 + 9 = 33", "Kopā."),
                ("3 · 6 + 5 · 3 = 18 + 15 = 33", "Cits griezums - tas pats."),
            ],
            atbilde="33 rūtiņas"),

    Zimejums("«T» forma",
             figura([(0, 4), (9, 4), (9, 6), (0, 6), (0, 4), (3, 4), (3, 0),
                     (6, 0), (6, 4)],
                    platums=10, augstums=7, aizpildi=False),
             paskaidro="Augšējā josla 9 × 2 = 18, kāja 3 × 4 = 12. Kopā 30.",
             ievads="«T» - josla un kāja."),

    Ievadi("Kombinētas figūras", [
        {"jaut": "«L»: 10 × 2 un 2 × 4. Laukums?", "atb": ["28"],
         "padoms": "20 + 8."},
        {"jaut": "«T»: 9 × 2 un 3 × 4. Laukums?", "atb": ["30"],
         "padoms": "18 + 12."},
        {"jaut": "Divi taisnstūri 5 × 4 un 3 × 3 blakus. Laukums?",
         "atb": ["29"], "padoms": "20 + 9."},
        {"jaut": "«U»: trīs taisnstūri 2 × 5, 4 × 2, 2 × 5. Laukums?",
         "atb": ["28"], "padoms": "10 + 8 + 10."},
    ]),

    Varianti("Kā sadalīt?", [
        {"jaut": "Cik taisnstūros vismaz jāsadala «L»?",
         "opcijas": ["2", "1", "3", "4"], "pareizi": 0,
         "padoms": "Viens griezums."},
        {"jaut": "Cik taisnstūros vismaz jāsadala «U»?",
         "opcijas": ["3", "2", "1", "5"], "pareizi": 0,
         "padoms": "Divas sienas un pamats."},
        {"jaut": "Vai dažādi griezumi var dot dažādus laukumus?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "Figūra ir tā pati."},
    ]),

    Pasaule("Dzīvokļa grīdas segums",
            Ievadi("", [
                {"jaut": "«L» dzīvoklis: 8 m × 5 m un 4 m × 3 m. Cik m²?",
                 "atb": ["52"], "padoms": "40 + 12."},
                {"jaut": "Parkets 20 € par m². Cik maksā?", "atb": ["1040"],
                 "padoms": "52 · 20."},
                {"jaut": "Balkons 4 m × 1 m. Cik m² kopā ar dzīvokli?",
                 "atb": ["56"], "padoms": "52 + 4."},
                {"jaut": "Cik m² ir lielākajā taisnstūrī?", "atb": ["40"],
                 "padoms": "8 · 5."},
            ]),
            pavediens="maja",
            konteksts="Dzīvokļi reti ir taisnstūri - tos sadala istabās "
                      "un koridoros, katrs ir taisnstūris.",
            kapec="Sadalot taisnstūros, var aprēķināt jebkuras istabas "
                  "laukumu."),

    Kopsavilkums([
        "Sadalu kombinētu figūru taisnstūros.",
        "Atrodu trūkstošās malas.",
        "Saskaitu laukumus un pārbaudu ar citu griezumu.",
    ]),

    Majas([
        "Uzzīmē savas mājas plānu un aprēķini grīdas laukumu.",
        "Uzzīmē burtu «E» rūtiņās un aprēķini tā laukumu.",
        "Sadali to pašu figūru divos dažādos veidos.",
    ]),
]
