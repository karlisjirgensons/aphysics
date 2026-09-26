# -*- coding: utf-8 -*-
"""2. klase, 111. stunda: «Kāpēc taisnstūrim nav jāmēra visas malas?»

Taisnstūrim pretējās malas ir vienādas, tāpēc pietiek izmērīt garumu un
platumu: P = a + b + a + b. Kvadrātam visas malas vienādas - pietiek ar
vienu: P = a + a + a + a.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, figura)

TEMA = "Kāpēc taisnstūrim nav jāmēra visas malas?"

MERKIS = ("Šodien paskaidrosim, kurus mērījumus pietiek veikt taisnstūra "
          "un kvadrāta perimetram.")

_TAISNST = figura([(1, 1), (7, 1), (7, 4), (1, 4)],
                  uzraksti=[(4, 0.4, "6 cm"), (7.8, 2.5, "3 cm")],
                  platums=9, augstums=5)

SATURS = [
    Sakums("Cik malas jāizmēra, lai atrastu taisnstūra perimetru?",
           zimejums=_TAISNST,
           paraksts="Pietiek ar divām - garumu un platumu.",
           fakti=["Taisnstūrim pretējās malas ir vienādas.",
                  "P = 6 + 3 + 6 + 3 = 18 cm.",
                  "Kvadrātam pietiek izmērīt vienu malu!"]),

    Doma("Vienādas malas",
         "Taisnstūrim ir divas malas pa a un divas pa b.",
         soli=[
             "Izmēri garumu a un platumu b.",
             "P = a + b + a + b.",
             "Var arī: vispirms a + b, tad divreiz.",
             "Kvadrātam: P = a + a + a + a.",
         ]),

    Paraugs("Taisnstūris 6 cm un 3 cm",
            uzd="Aprēķini perimetru.",
            soli=[("6 + 3 = 9", "Garums un platums."),
                  ("9 + 9 = 18", "Tas pats vēlreiz - pretējās malas."),
                  ("P = 18 cm", "")],
            atbilde="18 cm"),

    Ievadi("Aprēķini perimetru", [
        {"jaut": "Taisnstūris: 5 cm un 2 cm. P = ?", "atb": ["14"],
         "mers": "cm", "padoms": "7 + 7."},
        {"jaut": "Kvadrāts ar malu 4 cm. P = ?", "atb": ["16"],
         "mers": "cm", "padoms": "4 + 4 + 4 + 4."},
        {"jaut": "Taisnstūris: 10 cm un 5 cm. P = ?", "atb": ["30"],
         "mers": "cm", "padoms": "15 + 15."},
        {"jaut": "Kvadrāts ar malu 7 cm. P = ?", "atb": ["28"],
         "mers": "cm", "padoms": "14 + 14."},
        {"jaut": "Taisnstūris: 12 cm un 8 cm. P = ?", "atb": ["40"],
         "mers": "cm", "padoms": "20 + 20."},
        {"jaut": "Kvadrāta P = 20 cm. Cik gara mala?", "atb": ["5"],
         "mers": "cm", "padoms": "Četras vienādas malas: 5 + 5 + 5 + 5."},
    ], pamats=4),

    Varianti("Cik mērījumu vajag?", [
        {"jaut": "Kvadrātam", "opcijas": ["1", "2", "4"], "pareizi": 0,
         "padoms": "Visas malas vienādas."},
        {"jaut": "Taisnstūrim", "opcijas": ["2", "1", "4"], "pareizi": 0,
         "padoms": "Garums un platums."},
        {"jaut": "Trijstūrim ar dažādām malām",
         "opcijas": ["3", "1", "2"], "pareizi": 0,
         "padoms": "Visas dažādas."},
    ]),

    Pasaule("Futbola laukums",
            Ievadi("", [
                {"jaut": "Skolas laukums ir 40 m garš un 20 m plats. Cik m "
                         "līnijas jānovelk apkārt?", "atb": ["120"],
                 "mers": "m", "padoms": "60 + 60."},
                {"jaut": "Bērni skrien apkārt vienu apli. Cik metrus?",
                 "atb": ["120"], "mers": "m", "padoms": "Tas pats perimetrs."},
            ]),
            pavediens="sports",
            konteksts="Laukuma līnijas krāso katru pavasari.",
            kapec="Pietiek izmērīt divas malas - pārējās zināmas."),

    Kopsavilkums([
        "Zinu, ka taisnstūrim pretējās malas vienādas.",
        "Taisnstūrim mēru garumu un platumu.",
        "Kvadrātam pietiek ar vienu malu.",
    ]),

    Majas([
        "Izmēri tikai divas malas savam galdam.",
        "Aprēķini perimetru.",
        "Pārbaudi, izmērot visas četras.",
    ]),
]
