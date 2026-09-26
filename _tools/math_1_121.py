# -*- coding: utf-8 -*-
"""1. klase, 121. stunda: «Ko var uzzināt no tabulas?»

Tabulā dati sakārtoti rindās un ailēs. Nolasa vienu skaitli (rinda +
aile), salīdzina un saskaita. Katrai atbildei - teikums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Ko var uzzināt no tabulas?"

MERKIS = ("Šodien nolasīsim datus no tabulas un atbildēsim uz jautājumiem "
          "par tiem.")

_TABULA = restis([["", "zēni", "meitenes"], ["1.a", 9, 11],
                  ["1.b", 12, 8]])

SATURS = [
    Sakums("Cik meiteņu ir 1.a klasē?",
           zimejums=_TABULA,
           paraksts="Rinda «1.a», aile «meitenes» - 11.",
           fakti=["Atrodi rindu.",
                  "Atrodi aili.",
                  "Krustpunktā - skaitlis."]),

    Doma("Rinda un aile",
         "Katrs skaitlis tabulā pieder vienai rindai un vienai ailei.",
         soli=[
             "Izlasi jautājumu: kas meklējams?",
             "Atrodi pareizo rindu un aili.",
             "Nolasi skaitli; ja vajag - saskaiti vai atņem.",
         ]),

    Ievadi("Nolasi", [
        {"jaut": "Cik zēnu 1.b klasē?", "zim": _TABULA, "atb": ["12"],
         "padoms": "Rinda 1.b, aile zēni."},
        {"jaut": "Cik bērnu 1.a klasē?", "zim": _TABULA, "atb": ["20"],
         "padoms": "9 + 11."},
        {"jaut": "Cik meiteņu abās klasēs?", "zim": _TABULA, "atb": ["19"],
         "padoms": "11 + 8."},
        {"jaut": "Par cik 1.b zēnu vairāk nekā 1.a zēnu?", "zim": _TABULA,
         "atb": ["3"], "padoms": "12 − 9."},
    ]),

    Varianti("Patiess?", [
        {"jaut": "1.a klasē meiteņu vairāk nekā zēnu.", "zim": _TABULA,
         "opcijas": ["Patiess", "Aplams"], "jaukt": False, "pareizi": 0,
         "padoms": "11 > 9."},
        {"jaut": "1.b klasē ir 21 bērns.", "zim": _TABULA,
         "opcijas": ["Aplams", "Patiess"], "jaukt": False, "pareizi": 0,
         "padoms": "12 + 8 = 20."},
    ]),

    Pasaule("Ēdnīcas izvēle",
            Ievadi("", [
                {"jaut": "Cik bērnu izvēlējās zupu?",
                 "zim": restis([["zupa", "makaroni", "rīsi"], [6, 9, 4]]),
                 "atb": ["6"], "padoms": "Aile zupa."},
                {"jaut": "Cik bērnu kopā?", "atb": ["19"],
                 "padoms": "6 + 9 + 4."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīca pieraksta, ko bērni izvēlas.",
            kapec="No tabulas pavārs zina, cik gatavot."),

    Kopsavilkums([
        "Nolasu skaitli no tabulas.",
        "Salīdzinu un saskaitu datus.",
        "Atbildu teikumā.",
    ]),

    Majas([
        "Izveido tabulu: cik karošu un dakšu ir mājās.",
        "Uzdod mājiniekam 2 jautājumus par to.",
        "Pārbaudi atbildes.",
    ]),
]
