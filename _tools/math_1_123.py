# -*- coding: utf-8 -*-
"""1. klase, 123. stunda: «Par cik viens stabiņš augstāks?»

Pēc diagrammas nosaka, par cik viens lielums lielāks nekā otrs:
nolasa abus skaitļus un atņem - tieši kā ar sloksnītēm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, kolonnas)

TEMA = "Par cik viens stabiņš augstāks?"

MERKIS = ("Šodien pēc diagrammas noteiksim, par cik viens lielums ir "
          "lielāks nekā otrs.")

_SPORTS = kolonnas([("futbols", 12), ("peldēšana", 7), ("dejas", 9),
                    ("šahs", 4)])

SATURS = [
    Sakums("Par cik futbolistu vairāk nekā peldētāju?",
           zimejums=_SPORTS,
           paraksts="12 − 7 = 5.",
           fakti=["Nolasi abus skaitļus.",
                  "Atņem mazāko no lielākā.",
                  "Stabiņi - tās pašas sloksnītes."]),

    Doma("Starpība diagrammā",
         "Par cik augstāks - lielākais skaitlis mīnus mazākais.",
         soli=[
             "Atrodi abus stabiņus.",
             "Nolasi skaitļus.",
             "Atņem: lielākais − mazākais.",
         ]),

    Ievadi("Par cik?", [
        {"jaut": "Par cik futbolistu vairāk nekā peldētāju?",
         "zim": _SPORTS, "atb": ["5"], "padoms": "12 − 7."},
        {"jaut": "Par cik dejotāju vairāk nekā šahistu?", "zim": _SPORTS,
         "atb": ["5"], "padoms": "9 − 4."},
        {"jaut": "Par cik peldētāju mazāk nekā dejotāju?", "zim": _SPORTS,
         "atb": ["2"], "padoms": "9 − 7."},
        {"jaut": "Par cik futbolistu vairāk nekā šahistu?", "zim": _SPORTS,
         "atb": ["8"], "padoms": "12 − 4."},
    ]),

    Varianti("Patiess?", [
        {"jaut": "Dejotāju ir par 2 vairāk nekā peldētāju.", "zim": _SPORTS,
         "opcijas": ["Patiess", "Aplams"], "jaukt": False, "pareizi": 0,
         "padoms": "9 − 7."},
        {"jaut": "Šahistu ir par 3 mazāk nekā peldētāju.", "zim": _SPORTS,
         "opcijas": ["Patiess", "Aplams"], "jaukt": False, "pareizi": 0,
         "padoms": "7 − 4."},
    ]),

    Pasaule("Lasīšanas sacensības",
            Ievadi("", [
                {"jaut": "Par cik grāmatu vairāk izlasīja Liene nekā Oskars?",
                 "zim": kolonnas([("Liene", 15), ("Oskars", 8),
                                  ("Mia", 11)]),
                 "atb": ["7"], "padoms": "15 − 8."},
            ]),
            pavediens="skola",
            konteksts="Klasē skaita izlasītās grāmatas.",
            kapec="Diagramma parāda, kas jāpanāk."),

    Kopsavilkums([
        "Pēc diagrammas nosaku starpību.",
        "Lietoju atņemšanu.",
        "Pārbaudu apgalvojumus.",
    ]),

    Majas([
        "Uzzīmē diagrammu par ģimenes augumiem.",
        "Par cik garākais garāks nekā īsākais?",
        "Izdomā jautājumu «par cik».",
    ]),
]
