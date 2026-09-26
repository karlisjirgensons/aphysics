# -*- coding: utf-8 -*-
"""2. klase, 95. stunda: «Kā algoritms palīdz rēķināt?»

Algoritmi, ko skolēns jau lieto, tikai nenosauc: skaitļu salīdzināšana
(vispirms desmiti, tad vieni) un izteiksmes vērtība (vispirms iekavas, tad
no kreisās). Tos pierakstot shēmā, redz, ka matemātika ir algoritmu pilna.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, algoritms)

TEMA = "Kā algoritms palīdz rēķināt?"

MERKIS = ("Šodien izmantosim algoritmu skaitļu salīdzināšanai un izteiksmes "
          "vērtības aprēķināšanai.")

_SALIDZINA = algoritms([
    ("Vai desmitu cipari vienādi?", "Salīdzini vienus",
     "Lielāks, kam vairāk desmitu"),
    "Pieraksti zīmi <, > vai =",
])

_IZTEIKSME = algoritms([
    ("Vai ir iekavas?", "Izrēķini iekavās", "Nekas"),
    "Rēķini no kreisās uz labo",
    "Pieraksti vērtību",
])

SATURS = [
    Sakums("Kā salīdzināt 47 un 43 - pēc algoritma?",
           zimejums=_SALIDZINA,
           fakti=["Desmiti vienādi - 4 un 4.",
                  "Salīdzina vienus: 7 > 3.",
                  "Tātad 47 > 43."]),

    Doma("Algoritmi, ko jau zini",
         "Daudzas rēķināšanas prasmes ir algoritmi.",
         soli=[
             "Salīdzināšana: vispirms desmiti, tad vieni.",
             "Izteiksme: vispirms iekavas, tad no kreisās.",
             "Stabiņš: vispirms vieni, tad desmiti.",
             "Algoritmu izpildot, nekļūdās.",
         ]),

    Varianti("Salīdzini pēc algoritma", [
        {"jaut": "56 ☐ 65", "zim": _SALIDZINA, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 0, "padoms": "5 desmiti < 6 desmiti."},
        {"jaut": "82 ☐ 28", "zim": _SALIDZINA, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 1, "padoms": "8 > 2 desmiti."},
        {"jaut": "39 ☐ 34", "zim": _SALIDZINA, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 1, "padoms": "Desmiti vienādi, 9 > 4."},
        {"jaut": "70 ☐ 70", "zim": _SALIDZINA, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 2, "padoms": "Viss vienāds."},
    ]),

    Ievadi("Izteiksme pēc algoritma", [
        {"jaut": "60 − (15 + 25) = ?", "zim": _IZTEIKSME, "atb": ["20"],
         "padoms": "Iekavas: 40."},
        {"jaut": "35 + 25 − 10 = ?", "zim": _IZTEIKSME, "atb": ["50"],
         "padoms": "Iekavu nav: 60 − 10."},
        {"jaut": "90 − 30 − 20 = ?", "zim": _IZTEIKSME, "atb": ["40"],
         "padoms": "No kreisās."},
        {"jaut": "90 − (30 − 20) = ?", "zim": _IZTEIKSME, "atb": ["80"],
         "padoms": "Iekavas: 10."},
    ]),

    Pasaule("Kurš skrēja ātrāk?",
            Varianti("", [
                {"jaut": "Laiki: Anna 48 s, Pēteris 45 s. Pēc algoritma - kurš "
                         "ātrāks?", "zim": _SALIDZINA,
                 "opcijas": ["Pēteris", "Anna", "vienādi"], "pareizi": 0,
                 "padoms": "45 < 48 - mazāks laiks uzvar."},
            ]),
            pavediens="sports",
            konteksts="Sacensībās rezultātus salīdzina pēc kārtības.",
            kapec="Algoritms salīdzina bez kļūdām arī lielus sarakstus."),

    Kopsavilkums([
        "Salīdzinu skaitļus pēc algoritma.",
        "Aprēķinu izteiksmi pēc algoritma.",
        "Redzu, ka rēķināšanas noteikumi ir algoritmi.",
    ]),

    Majas([
        "Uzzīmē algoritmu saskaitīšanai stabiņā.",
        "Izpildi to ar 38 + 45.",
        "Paskaidro mājiniekam katru soli.",
    ]),
]
