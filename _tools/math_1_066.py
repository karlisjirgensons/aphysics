# -*- coding: utf-8 -*-
"""1. klase, 66. stunda: «Kā sakārtot pēc lieluma?»

Augošā secībā - no mazākā uz lielāko, dilstošā - otrādi. Kārtīgs veids:
vispirms atrod mazāko, izsvītro, tad nākamo mazāko... Pēc tam pastāsta
savu rīcības kārtību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kā sakārtot pēc lieluma?"

MERKIS = ("Šodien sakārtosim skaitļus augošā un dilstošā secībā un "
          "pastāstīsim, kā to darījām.")

SATURS = [
    Sakums("Kā sakārtot 47, 12, 74, 30?",
           zimejums=restis([[12, 30, 47, 74]]),
           paraksts="No mazākā uz lielāko - augošā secībā.",
           fakti=["Augošā - no mazākā uz lielāko.",
                  "Dilstošā - no lielākā uz mazāko.",
                  "Atrodi mazāko, izsvītro, meklē nākamo."]),

    Doma("Kārtošanas kārtība",
         "Katru reizi meklē mazāko no tiem, kas palikuši.",
         soli=[
             "Atrodi mazāko skaitli - tas pirmais.",
             "Izsvītro to.",
             "No palikušajiem atkal meklē mazāko.",
             "Dilstošai - meklē lielāko.",
         ]),

    Ievadi("Augošā secībā", [
        {"jaut": "56, 18, 81, 34. Kurš būs pirmais?", "atb": ["18"],
         "padoms": "Mazākais."},
        {"jaut": "56, 18, 81, 34. Kurš būs otrais?", "atb": ["34"],
         "padoms": "Nākamais mazākais."},
        {"jaut": "56, 18, 81, 34. Kurš būs pēdējais?", "atb": ["81"],
         "padoms": "Lielākais."},
    ]),

    Ievadi("Dilstošā secībā", [
        {"jaut": "29, 92, 50, 9. Kurš pirmais?", "atb": ["92"],
         "padoms": "Lielākais."},
        {"jaut": "29, 92, 50, 9. Kurš trešais?", "atb": ["29"],
         "padoms": "92, 50, ..."},
        {"jaut": "29, 92, 50, 9. Kurš pēdējais?", "atb": ["9"],
         "padoms": "Mazākais."},
    ]),

    Varianti("Vai sakārtots?", [
        {"jaut": "13, 31, 33, 30 - augošā?",
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "30 ir mazāks nekā 33."},
        {"jaut": "90, 72, 45, 8 - dilstošā?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Katrs nākamais mazāks."},
    ]),

    Pasaule("Rinda pēc auguma",
            Ievadi("", [
                {"jaut": "Bērnu augums cm: 121, 118, 125, 119. Kurš stāvēs "
                         "pirmais, ja sāk ar mazāko? (cm)", "atb": ["118"],
                 "padoms": "Mazākais."},
                {"jaut": "Kurš pēdējais? (cm)", "atb": ["125"],
                 "padoms": "Garākais."},
            ]),
            pavediens="sports",
            konteksts="Sporta stundā klase nostājas rindā pēc auguma.",
            kapec="Kārtošana pēc lieluma - ikdienas darbs."),

    Kopsavilkums([
        "Kārtoju skaitļus augošā un dilstošā secībā.",
        "Katru reizi meklēju mazāko (vai lielāko).",
        "Pastāstu savu kārtību.",
    ]),

    Majas([
        "Sakārto ģimenes locekļus pēc vecuma.",
        "Sakārto 5 grāmatas pēc lappušu skaita.",
        "Pastāsti, kā to izdarīji.",
    ]),
]
