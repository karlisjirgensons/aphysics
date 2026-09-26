# -*- coding: utf-8 -*-
"""1. klase, 144. stunda: «Kā pierakstīt mērījumus?»

Mērījumus pieraksta tabulā: kas, cik, mērvienība. Rezultātam vienmēr
pieliek mērvienību (18 cm, 3 kg, 2 l). No tabulas aprēķina starpības un
summas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā pierakstīt mērījumus?"

MERKIS = ("Šodien veidosim tabulu mērījumiem un pierakstīsim rezultātus ar "
          "mērvienību.")

_MERIJUMI = restis([["ko mērīja", "cik"], ["grāmata", "20 cm"],
                    ["pudele", "1 l"], ["soma", "3 kg"],
                    ["sols", "70 cm"]])

SATURS = [
    Sakums("Kā pierakstīt, lai pēc nedēļas saprastu?",
           zimejums=_MERIJUMI,
           paraksts="Katram mērījumam - skaitlis un mērvienība.",
           fakti=["Tabulā: kas un cik.",
                  "Bez mērvienības skaitlis neko nesaka.",
                  "No tabulas var rēķināt."]),

    Doma("Mērījumu tabula",
         "Katrā rindā - viens mērījums ar mērvienību.",
         soli=[
             "Uzraksti virsrakstus: ko mērīja, cik.",
             "Katru mērījumu jaunā rindā.",
             "Pie skaitļa - cm, kg vai l.",
         ]),

    Ievadi("Nolasi un aprēķini", [
        {"jaut": "Cik cm gara grāmata?", "zim": _MERIJUMI, "atb": ["20"],
         "padoms": "Rinda grāmata."},
        {"jaut": "Par cik cm sols garāks nekā grāmata?", "zim": _MERIJUMI,
         "atb": ["50"], "padoms": "70 − 20."},
        {"jaut": "Cik kg sver soma?", "zim": _MERIJUMI, "atb": ["3"],
         "padoms": "Rinda soma."},
    ]),

    Varianti("Pareizs pieraksts?", [
        {"jaut": "Grāmata ir 20 ...", "opcijas": ["cm", "kg", "l"],
         "pareizi": 0, "padoms": "Garums."},
        {"jaut": "Kurš pieraksts ir pilnīgs?",
         "opcijas": ["pudele - 1 l", "pudele - 1", "1 l"], "pareizi": 0,
         "padoms": "Kas un cik ar mērvienību."},
    ]),

    Petijums("Mūsu mērījumi", [
        "Izmēri 3 lietas: garumu, masu vai tilpumu.",
        "Ieraksti tabulā ar mērvienību.",
        "Aprēķini vienu starpību.",
        "Parādi tabulu pārim.",
    ], vajag="lineāls, svari, mērtrauks, lapa"),

    Pasaule("Augšana",
            Ievadi("", [
                {"jaut": "Septembrī tavs augums 118 cm, maijā 123 cm. Par cik "
                         "cm izaugi?", "atb": ["5"], "padoms": "123 − 118."},
            ]),
            pavediens="sports",
            konteksts="Skolas māsa pieraksta bērnu augumu tabulā.",
            kapec="Tabulā redz izmaiņas laikā."),

    Kopsavilkums([
        "Pierakstu mērījumus tabulā.",
        "Vienmēr pielieku mērvienību.",
        "Aprēķinu no tabulas.",
    ]),

    Majas([
        "Izveido mājās mērījumu tabulu (3 lietas).",
        "Pieraksti ar mērvienībām.",
        "Kas ir garākais, smagākais?",
    ]),
]
