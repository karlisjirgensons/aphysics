# -*- coding: utf-8 -*-
"""2. klase, 110. stunda: «Cik gara ir figūras apmale?»

Perimetrs ir visu malu garumu summa - cik garš ceļš, ja apiet figūrai
apkārt. To aprēķina ar izteiksmi: P = 3 cm + 4 cm + 5 cm = 12 cm. Mērvienība
tā pati, kas malām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, figura)

TEMA = "Cik gara ir figūras apmale?"

MERKIS = ("Šodien izmērīsim daudzstūra malas, aprēķināsim perimetru un "
          "pierakstīsim to ar izteiksmi.")

_TRIJST = figura([(1, 1), (5, 1), (1, 4)],
                 uzraksti=[(3, 0.4, "4 cm"), (0.1, 2.5, "3 cm"),
                           (3.6, 2.9, "5 cm")], platums=7, augstums=5)
_CETR = figura([(1, 1), (6, 1), (7, 4), (2, 4)],
               uzraksti=[(3.5, 0.4, "5 cm"), (4.5, 4.6, "5 cm"),
                         (0.7, 2.5, "3 cm"), (7.6, 2.5, "3 cm")],
               platums=9, augstums=5)

SATURS = [
    Sakums("Cik garu lenti vajag, lai aplīmētu apsveikuma kartīti?",
           zimejums=_TRIJST,
           paraksts="Apkārt: 3 + 4 + 5 = 12 cm.",
           fakti=["Apmales garumu sauc par perimetru.",
                  "Tā ir visu malu garumu summa.",
                  "Perimetru apzīmē ar burtu P."]),

    Doma("Perimetrs",
         "Perimetrs ir visu malu garumu summa.",
         soli=[
             "Izmēri katru malu.",
             "Pieraksti summu: 3 cm + 4 cm + 5 cm.",
             "Saskaiti.",
             "Atbildei pieraksti mērvienību: P = 12 cm.",
         ]),

    Paraugs("Četrstūra perimetrs",
            uzd="Malas: 5 cm, 3 cm, 5 cm, 3 cm.",
            soli=[("P = 5 cm + 3 cm + 5 cm + 3 cm", "Visu malu summa."),
                  ("P = 16 cm", "Saskaitīts.")],
            atbilde="16 cm"),

    Ievadi("Aprēķini perimetru", [
        {"jaut": "Trijstūra perimetrs?", "zim": _TRIJST, "atb": ["12"],
         "mers": "cm", "padoms": "3 + 4 + 5."},
        {"jaut": "Četrstūra perimetrs?", "zim": _CETR, "atb": ["16"],
         "mers": "cm", "padoms": "5 + 3 + 5 + 3."},
        {"jaut": "Trijstūris ar malām 6 cm, 6 cm un 6 cm. P = ?",
         "atb": ["18"], "mers": "cm", "padoms": "6 + 6 + 6."},
        {"jaut": "Piecstūris, katra mala 4 cm. P = ?", "atb": ["20"],
         "mers": "cm", "padoms": "4 + 4 + 4 + 4 + 4."},
        {"jaut": "Četrstūris: 12 cm, 8 cm, 10 cm, 15 cm. P = ?",
         "atb": ["45"], "mers": "cm", "padoms": "20 + 25."},
        {"jaut": "Trijstūra P = 20 cm, divas malas 7 cm un 8 cm. Trešā?",
         "atb": ["5"], "mers": "cm", "padoms": "20 − 15."},
    ], pamats=4),

    Varianti("Kas ir perimetrs?", [
        {"jaut": "Ko nozīmē aprēķināt perimetru?",
         "opcijas": ["saskaitīt visu malu garumus",
                     "saskaitīt rūtiņas iekšā", "izmērīt garāko malu"],
         "pareizi": 0, "padoms": "Apmale."},
        {"jaut": "Kurā mērvienībā perimetrs, ja malas cm?",
         "opcijas": ["cm", "rūtiņās", "kg"], "pareizi": 0,
         "padoms": "Tā pati, kas malām."},
    ]),

    Pasaule("Žogs ap dobi",
            Ievadi("", [
                {"jaut": "Trijstūra dobes malas: 3 m, 4 m, 5 m. Cik metru "
                         "apmales vajag?", "atb": ["12"], "mers": "m",
                 "padoms": "3 + 4 + 5."},
                {"jaut": "Veikalā apmale ir 10 m gabalos. Cik metru "
                         "pietrūks, ja nopērk vienu gabalu?", "atb": ["2"],
                 "mers": "m", "padoms": "12 − 10."},
            ]),
            pavediens="maja",
            konteksts="Dobi grib apjozt ar koka apmali.",
            kapec="Perimetrs pasaka, cik materiāla pirkt."),

    Kopsavilkums([
        "Zinu, ka perimetrs ir malu garumu summa.",
        "Pierakstu perimetru ar izteiksmi.",
        "Atbildē rakstu mērvienību.",
    ]),

    Majas([
        "Izmēri grāmatas malas un aprēķini perimetru.",
        "Izmēri galda malas.",
        "Kuram perimetrs lielāks?",
    ]),
]
