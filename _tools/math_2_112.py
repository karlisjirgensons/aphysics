# -*- coding: utf-8 -*-
"""2. klase, 112. stunda: «Cik metru žoga vajag?»

Perimetrs situācijās: žogs, apmale, lente. Svarīgi pamanīt, kad kāda mala
nav jāņem (vārti, siena) un pie atbildes rakstīt mērvienību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, figura)

TEMA = "Cik metru žoga vajag?"

MERKIS = ("Šodien risināsim situāciju uzdevumus par perimetru, lietojot "
          "mērvienības.")

_DARZS = figura([(1, 1), (9, 1), (9, 6), (1, 6)],
                uzraksti=[(5, 0.4, "20 m"), (10, 3.5, "10 m")],
                platums=11, augstums=7)

SATURS = [
    Sakums("Dārzs 20 m garš un 10 m plats. Cik metru žoga?",
           zimejums=_DARZS,
           paraksts="P = 20 + 10 + 20 + 10 = 60 m.",
           fakti=["Žoga garums ir perimetrs.",
                  "Ja vārti 3 m, žoga vajag mazāk: 57 m.",
                  "Ja viena mala ir māja - to nežogo."]),

    Doma("Perimetrs dzīvē",
         "Vispirms perimetrs, tad atņem to, kam žogs nav vajadzīgs.",
         soli=[
             "Uzzīmē plānu un ieraksti malas.",
             "Aprēķini perimetru.",
             "Atņem vārtus vai sienu, ja tādi ir.",
             "Atbilde ar mērvienību.",
         ]),

    Paraugs("Žogs ar vārtiem",
            uzd="Dārzs 20 m un 10 m, vārti 3 m platumā.",
            soli=[("P = 20 + 10 + 20 + 10 = 60 m", "Viss perimetrs."),
                  ("60 − 3 = 57 m", "Bez vārtiem.")],
            atbilde="57 m žoga"),

    Ievadi("Rēķini", [
        {"jaut": "Kvadrātveida laukums ar malu 15 m. Cik m žoga?",
         "atb": ["60"], "mers": "m", "padoms": "15 + 15 + 15 + 15."},
        {"jaut": "Taisnstūra dārzs 25 m un 15 m, vārti 4 m. Cik m žoga?",
         "atb": ["76"], "mers": "m", "padoms": "80 − 4."},
        {"jaut": "Dārzs 30 m un 10 m, viena garā mala ir mājas siena. Cik m "
                 "žoga?", "atb": ["50"], "mers": "m",
         "padoms": "30 + 10 + 10."},
        {"jaut": "Bilde 20 cm un 15 cm. Cik cm rāmja līstes?",
         "atb": ["70"], "mers": "cm", "padoms": "35 + 35."},
    ]),

    Varianti("Vai pietiks?", [
        {"jaut": "Ir 50 m žoga. Laukums 15 m un 10 m. Pietiks?",
         "opcijas": ["Jā, vajag tieši 50 m", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "25 + 25."},
        {"jaut": "Ir 30 m lentes. Laukums 10 m un 8 m. Pietiks?",
         "opcijas": ["Nē, vajag 36 m", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "18 + 18."},
    ]),

    Pasaule("Aploks trusim",
            Ievadi("", [
                {"jaut": "Aploks kvadrāts ar malu 3 m. Cik metru sieta?",
                 "atb": ["12"], "mers": "m", "padoms": "3 + 3 + 3 + 3."},
                {"jaut": "Siets maksā 2 € par metru. Cik maksā viss? "
                         "(12 reizes pa 2 €)", "atb": ["24"], "mers": "€",
                 "padoms": "Skaiti pa 2 līdz 12 reizēm."},
            ]),
            pavediens="daba",
            konteksts="Trusim pagalmā taisa aploku.",
            kapec="Perimetrs pasaka, cik sieta pirkt."),

    Kopsavilkums([
        "Risinu uzdevumus par perimetru.",
        "Atņemu vārtus vai sienu, ja vajag.",
        "Rakstu atbildi ar mērvienību.",
    ]),

    Majas([
        "Izmēri ar soļiem pagalma vai istabas perimetru.",
        "Pārvērt soļus metros (1 solis apmēram 50 cm).",
        "Cik metru lentes vajadzētu ap istabu?",
    ]),
]
