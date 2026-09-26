# -*- coding: utf-8 -*-
"""7. klase, 123. stunda: «Kur radusies kļūda?»

Kļūdas pārveidojumos atkārtojas: aizmirsts pareizināt otro saskaitāmo,
nemainītas zīmes aiz mīnusa, savilkti nelīdzīgi saskaitāmie. Stunda
māca atrast kļūdu ar pārbaudi (ievietojot skaitli) un nosaukt tās cēloni.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kur radusies kļūda?"

MERKIS = ("Atradīsim kļūdu dotā pārveidojumā un izskaidrosim tās cēloni.")

SATURS = [
    Sakums("Trīs biežākās kļūdas",
           zimejums=restis([["kļūda", "pareizi"],
                            ["3(x + 2) = 3x + 2", "3x + 6"],
                            ["−(a − 5) = −a − 5", "−a + 5"],
                            ["2x + 3 = 5x", "nevar savilkt"]]),
           fakti=["Visas trīs var atrast ar vienu pārbaudi.",
                  "Ievieto skaitli abās pusēs - ja atšķiras, ir kļūda."]),

    Doma("Pārbaude ar skaitli atrod kļūdu",
         "Katrā pareizā pārveidojuma solī izteiksmes vērtība nemainās. Ja "
         "pēc kāda soļa, ievietojot to pašu skaitli, vērtība mainās, - kļūda "
         "ir tieši šajā solī.",
         soli=[
             "Izvēlies ērtu skaitli (ne 0 un ne 1): x = 2.",
             "Aprēķini vērtību katrā rindā.",
             "Rinda, kurā vērtība mainās, - tur kļūda.",
             "Nosauc cēloni un izlabo.",
         ],
         pieze="x = 0 un x = 1 dažas kļūdas neatklāj (piemēram, x² = x pie "
               "x = 1). Labāk ņemt 2 vai 3."),

    Paraugs("Atrodi kļūdu",
            uzd="Anna: 5 − 2(x − 3) = 5 − 2x − 6 = −2x − 1. Pārbaudi.",
            soli=[
                ("x = 2: 5 − 2 · (−1) = 7", "Sākotnējā."),
                ("5 − 4 − 6 = −5", "Pirmā rinda - jau atšķiras."),
                ("Kļūda: −2 · (−3) = +6, nevis −6", "Zīmju kļūda."),
                ("Pareizi: 5 − 2x + 6 = 11 − 2x", "Labojums."),
            ],
            atbilde="Kļūda iekavu atvēršanā: jābūt 11 − 2x."),

    Varianti("Kāds kļūdas cēlonis?", [
        {"jaut": "4(y − 3) = 4y − 3",
         "opcijas": ["Nav pareizināts otrais saskaitāmais",
                     "Zīmju kļūda", "Savilkti nelīdzīgie", "Kļūdas nav"],
         "pareizi": 0, "padoms": "4 · 3."},
        {"jaut": "7a − (2a + 1) = 5a + 1",
         "opcijas": ["Nav mainīta zīme pie 1", "Nav pareizināts",
                     "Savilkti nelīdzīgie", "Kļūdas nav"],
         "pareizi": 0, "padoms": "−(+1) = −1."},
        {"jaut": "3x + 4x² = 7x³",
         "opcijas": ["Savilkti nelīdzīgie", "Zīmju kļūda",
                     "Nav pareizināts", "Kļūdas nav"],
         "pareizi": 0, "padoms": "x un x² nav līdzīgi."},
        {"jaut": "−(−2m + 5) = 2m − 5",
         "opcijas": ["Kļūdas nav", "Zīmju kļūda", "Nav pareizināts",
                     "Savilkti nelīdzīgie"],
         "pareizi": 0, "padoms": "Abas zīmes mainītas pareizi."},
        {"jaut": "2(3x) = 6x · 2",
         "opcijas": ["Divreiz reizināts ar 2", "Kļūdas nav",
                     "Zīmju kļūda", "Savilkti nelīdzīgie"],
         "pareizi": 0, "padoms": "2 · 3x = 6x."},
        {"jaut": "(x + 3) − (x − 3) = 0",
         "opcijas": ["Jābūt 6 - nav mainīta zīme pie −3",
                     "Kļūdas nav", "Jābūt 2x", "Jābūt −6"],
         "pareizi": 0, "padoms": "x + 3 − x + 3."},
    ], pamats=4),

    Pasaule("Programmas kļūdas meklēšana",
            Varianti("", [
                {"jaut": "Programmētājs meklē kļūdu, izdrukājot vērtību "
                         "pēc katra soļa. Kā to sauc matemātikā?",
                 "opcijas": ["Pārbaude ar skaitli katrā rindā",
                             "Minēšana", "Pierādījums", "Konstrukcija"],
                 "pareizi": 0, "padoms": "Tā pati metode."},
                {"jaut": "Programma rēķina cenu ar atlaidi: cena − "
                         "(cena · 0,2 − 1). Kas notiek ar 1?",
                 "opcijas": ["Tas tiek pieskaitīts cenai",
                             "Tas tiek atņemts", "Tas pazūd",
                             "Tas reizinās ar 0,2"],
                 "pareizi": 0, "padoms": "−(−1) = +1."},
            ]),
            pavediens="dati",
            konteksts="Programmētāji kļūdas meklē tieši tā: pārbauda "
                      "vērtību pēc katra soļa («debugging»).",
            kapec="Kļūdas atrašana ir prasme, ne veiksme."),

    Kopsavilkums([
        "Atrodu kļūdu ar pārbaudi, ievietojot skaitli.",
        "Nosaku rindu, kurā kļūda radās.",
        "Nosaucu cēloni: reizināšana, zīmes vai nelīdzīgie.",
        "Izlaboju pārveidojumu.",
    ]),

    Majas([
        "Atrodi kļūdu: 3 − 4(2 − a) = 3 − 8 − 4a = −5 − 4a.",
        "Izdomā pārveidojumu ar vienu apzinātu kļūdu draugam.",
        "Pārbaudi savus mājas darbus ar x = 2.",
    ]),
]
