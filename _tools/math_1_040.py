# -*- coding: utf-8 -*-
"""1. klase, 40. stunda: «Kāds stāsts der šim pierakstam?»

Otrādi nekā līdz šim: dota izteiksme (6 − 2), un skolēns izdomā stāstu no
dzīves, kas tai der. Pārbauda: vai stāstā kļūst vairāk vai mazāk?
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti)

TEMA = "Kāds stāsts der šim pierakstam?"

MERKIS = ("Šodien izdomāsim stāstus no dzīves, kas der dotam pierakstam.")

SATURS = [
    Sakums("6 − 2 - kāds stāsts te slēpjas?",
           fakti=["«Man bija 6 konfektes, 2 apēdu.»",
                  "«Stāvvietā 6 auto, 2 aizbrauca.»",
                  "Stāstā jābūt «mazāk» - jo ir «−»."]),

    Doma("No pieraksta uz stāstu",
         "Stāsts der, ja tajā ir tie paši skaitļi un tā pati darbība.",
         soli=[
             "Pirmais skaitlis - cik bija sākumā.",
             "«+» - kaut kas nāk klāt; «−» - aiziet.",
             "Otrais skaitlis - cik nāca vai gāja.",
             "Pajautā: cik tagad?",
         ]),

    Varianti("Kurš stāsts der?", [
        {"jaut": "6 − 2",
         "opcijas": ["Bija 6 baloni, 2 pārsprāga",
                     "Bija 6 baloni, nopirka vēl 2",
                     "Bija 2 baloni, 6 pārsprāga"],
         "pareizi": 0, "padoms": "Sākumā 6, kļūst mazāk."},
        {"jaut": "3 + 4",
         "opcijas": ["3 bērni šūpolēs, atnāca vēl 4",
                     "3 bērni aizgāja no 4",
                     "4 bērni aizgāja, palika 3"],
         "pareizi": 0, "padoms": "Nāk klāt."},
        {"jaut": "8 − 8",
         "opcijas": ["Uz šķīvja 8 pankūkas, visas apēda",
                     "8 pankūkas, izcepa vēl 8",
                     "Nebija nevienas pankūkas"],
         "pareizi": 0, "padoms": "Viss aizgāja - paliek 0."},
        {"jaut": "5 + 0",
         "opcijas": ["5 zivis akvārijā, nevienu nepielika",
                     "5 zivis, pielika vēl 5",
                     "Nebija zivju"],
         "pareizi": 0, "padoms": "Nekas nenāca klāt."},
    ]),

    Petijums("Izdomā pats", [
        "Paņem kartīti ar pierakstu (piem., 7 − 3).",
        "Izdomā stāstu par savu dzīvi.",
        "Uzzīmē stāstu.",
        "Pastāsti pārim - vai viņš uzmin pierakstu?",
    ], vajag="kartītes ar pierakstiem, krāsu zīmuļi"),

    Pasaule("Stāsts no virtuves",
            Varianti("", [
                {"jaut": "Kurš pieraksts der: «Uz galda 4 šķīvji, mamma "
                         "atnesa vēl 2»?",
                 "opcijas": ["4 + 2", "4 − 2", "2 − 4"], "pareizi": 0,
                 "padoms": "Atnesa - klāt."},
                {"jaut": "Un «No 7 olām 3 izlietoja pankūkām»?",
                 "opcijas": ["7 − 3", "7 + 3", "3 − 7"], "pareizi": 0,
                 "padoms": "Izlietoja - mazāk."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē katru dienu kaut kas nāk klāt un tiek "
                      "izlietots.",
            kapec="Katrs pieraksts ir īss stāsts."),

    Kopsavilkums([
        "Izdomāju stāstu dotam pierakstam.",
        "Pārbaudu, vai stāstā ir pareizā darbība.",
        "Atrodu pierakstu dotam stāstam.",
    ]),

    Majas([
        "Izdomā stāstu 9 − 4 par savu māju.",
        "Izdomā stāstu 2 + 5 par savu pagalmu.",
        "Pastāsti tos vakariņās un palūdz uzminēt pierakstu.",
    ]),
]
