# -*- coding: utf-8 -*-
"""2. klase, 90. stunda: «Kā salīdzināt summu ar skaitli?»

48 + 29 ☐ 80 - nerēķinot precīzi: 48 < 50 un 29 < 30, tātad summa < 80.
Novērtējums ar apaļiem skaitļiem ļauj salīdzināt ātri. Mikrotemata
noslēgums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kā salīdzināt summu ar skaitli?"

MERKIS = ("Šodien salīdzināsim summu vai starpību ar skaitli, lietojot «<», "
          "«>», «=», neveicot precīzus aprēķinus.")

_ZIMES = ["<", ">", "="]

SATURS = [
    Sakums("Vai 48 + 29 ir vairāk vai mazāk nekā 80?",
           fakti=["48 ir mazāk nekā 50, 29 - mazāk nekā 30.",
                  "50 + 30 = 80, tātad 48 + 29 < 80.",
                  "Precīzi rēķināt nevajadzēja!"]),

    Doma("Spried ar apaļiem skaitļiem",
         "Aizstāj saskaitāmos ar apaļiem un paskaties, uz kuru pusi mainīji.",
         soli=[
             "Ja abus palielināji - īstā summa ir mazāka.",
             "Ja abus samazināji - īstā summa ir lielāka.",
             "Starpībā: atņemot mazāk, paliek vairāk.",
             "Ja nevar izlemt - izrēķini precīzi.",
         ]),

    Varianti("Liec zīmi", [
        {"jaut": "48 + 29 ☐ 80", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 0, "padoms": "Abi mazāki par 50 un 30."},
        {"jaut": "52 + 31 ☐ 80", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 1, "padoms": "Abi lielāki par 50 un 30."},
        {"jaut": "70 − 19 ☐ 50", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 1, "padoms": "Atņem mazāk nekā 20."},
        {"jaut": "60 − 25 ☐ 40", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 0, "padoms": "Atņem vairāk nekā 20."},
        {"jaut": "35 + 45 ☐ 80", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 2, "padoms": "5 + 5 = 10."},
        {"jaut": "99 − 50 ☐ 50", "opcijas": _ZIMES, "jaukt": False,
         "pareizi": 0, "padoms": "99 < 100."},
    ], pamats=4),

    Ievadi("Pārbaudi precīzi", [
        {"jaut": "48 + 29 = ?", "atb": ["77"], "padoms": "77 < 80."},
        {"jaut": "52 + 31 = ?", "atb": ["83"], "padoms": "83 > 80."},
        {"jaut": "70 − 19 = ?", "atb": ["51"], "padoms": "51 > 50."},
        {"jaut": "60 − 25 = ?", "atb": ["35"], "padoms": "35 < 40."},
    ]),

    Pasaule("Vai pietiks ar 50 €?",
            Varianti("", [
                {"jaut": "Grozā preces par 19 € un 28 €. Vai pietiks ar "
                         "50 €?", "opcijas": ["Jā, 19 + 28 < 50", "Nē"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "20 + 30 = 50, bet abas cenas mazākas."},
                {"jaut": "Preces par 24 € un 31 €. Vai pietiks ar 50 €?",
                 "opcijas": ["Nē, 24 + 31 > 50", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "Vairāk nekā 20 + 30."},
            ]),
            pavediens="veikals",
            konteksts="Pie kases nav laika rēķināt precīzi.",
            kapec="Novērtējums pasaka atbildi dažās sekundēs."),

    Kopsavilkums([
        "Salīdzinu summu ar skaitli, nerēķinot precīzi.",
        "Izmantoju apaļus skaitļus.",
        "Pārbaudu ar precīzu aprēķinu, ja vajag.",
    ]),

    Majas([
        "Veikalā novērtē, vai 2 preces maksā vairāk vai mazāk nekā 10 €.",
        "Pēc tam pārbaudi čekā.",
        "Vai novērtējums bija pareizs?",
    ]),
]
