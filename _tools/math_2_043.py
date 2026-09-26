# -*- coding: utf-8 -*-
"""2. klase, 43. stunda: «Kā pārbaudīt starpību?»

Starpību pārbauda ar saskaitīšanu: starpība + atņēmējs = mazināmais.
Ja 63 − 28 = 35, tad 35 + 28 jābūt 63. Šī sakarība vēlāk ļaus atrast
nezināmo darbības locekli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, majina)

TEMA = "Kā pārbaudīt starpību?"

MERKIS = ("Šodien pārbaudīsim atņemšanu ar saskaitīšanu un atradīsim "
          "kļūdas.")

SATURS = [
    Sakums("Kā pārliecināties, ka 63 − 28 tiešām ir 35?",
           zimejums=majina(63, [(28, 35)]),
           paraksts="28 un 35 kopā dod 63.",
           fakti=["Ja no 63 atņem 28, paliek 35.",
                  "Tad 35 + 28 jāatdod 63.",
                  "Saskaitīšana ir atņemšanas pārbaude."]),

    Doma("Pārbaude ar saskaitīšanu",
         "Starpība + atņēmējs = mazināmais.",
         soli=[
             "Izrēķini: 72 − 45 = 27.",
             "Saskaiti rezultātu ar atņemto: 27 + 45.",
             "Ja sanāk 72 - pareizi.",
             "Ja nesanāk - meklē kļūdu.",
         ],
         pieze="Mazināmais - no kā atņem, atņēmējs - ko atņem, starpība - "
               "kas paliek."),

    Paraugs("Pārbaudi 81 − 36 = 55",
            uzd="Vai pareizi?",
            soli=[("55 + 36 = 91", "Pārbaude ar saskaitīšanu."),
                  ("91 nav 81", "Nesakrīt - kļūda!"),
                  ("81 − 36 = 45", "Pārbaude: 45 + 36 = 81.")],
            atbilde="nepareizi, jābūt 45"),

    Ievadi("Pārbaudi", [
        {"jaut": "54 − 26 = 28. Cik ir 28 + 26?", "atb": ["54"],
         "padoms": "Jāsanāk 54."},
        {"jaut": "90 − 37 = 53. Cik ir 53 + 37?", "atb": ["90"],
         "padoms": "Jāsanāk 90."},
        {"jaut": "Izlabo: 70 − 26 = 54. Cik pareizi?", "atb": ["44"],
         "padoms": "44 + 26 = 70."},
        {"jaut": "Izlabo: 62 − 17 = 55. Cik pareizi?", "atb": ["45"],
         "padoms": "45 + 17 = 62."},
    ]),

    Varianti("Pareizi vai nē?", [
        {"jaut": "84 − 29 = 55", "opcijas": ["pareizi", "nepareizi"],
         "jaukt": False, "pareizi": 0, "padoms": "55 + 29 = 84."},
        {"jaut": "66 − 38 = 38", "opcijas": ["pareizi", "nepareizi"],
         "jaukt": False, "pareizi": 1, "padoms": "38 + 38 = 76."},
        {"jaut": "Kā pārbaudīt 50 − 18 = 32?",
         "opcijas": ["32 + 18", "32 − 18", "50 + 18"], "pareizi": 0,
         "padoms": "Starpība + atņēmējs."},
        {"jaut": "45 − 19 = 26", "opcijas": ["pareizi", "nepareizi"],
         "jaukt": False, "pareizi": 0, "padoms": "26 + 19 = 45."},
    ]),

    Pasaule("Vai atlikums pareizs?",
            Ievadi("", [
                {"jaut": "Tev bija 50 €, velosipēda zvans maksāja 17 €. "
                         "Pārdevējs izdeva 33 €. Cik ir 33 + 17?",
                 "atb": ["50"], "mers": "€", "padoms": "Jāsanāk 50."},
                {"jaut": "Ķivere maksāja 38 €, samaksāji 50 €, izdeva 22 €. "
                         "Cik vajadzēja izdot?", "atb": ["12"], "mers": "€",
                 "padoms": "12 + 38 = 50."},
            ]),
            pavediens="veikals",
            konteksts="Velosipēdu veikalā pērk piederumus.",
            kapec="Atlikumu pārbauda ar saskaitīšanu - ātri un droši."),

    Kopsavilkums([
        "Pārbaudu atņemšanu ar saskaitīšanu.",
        "Zinu vārdus: mazināmais, atņēmējs, starpība.",
        "Atrodu un izlaboju kļūdu.",
    ]),

    Majas([
        "Izrēķini 4 starpības un pārbaudi katru.",
        "Mājinieks lai atrisina vienu ar kļūdu - atrodi to.",
        "Nākamreiz veikalā pārbaudi atlikumu.",
    ]),
]
