# -*- coding: utf-8 -*-
"""9. klase, 61. stunda: «Kāpēc sadalīšana noder?»

Trīs darbi, kurus bez sadalīšanas reizinātājos izdarīt nevar vai ir
grūti: saīsināt daļu, atrisināt vienādojumu ar reizinājumu nulle un
izrēķināt galvā. Katram - piemērs un uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kāpēc sadalīšana noder?"

MERKIS = ("Skaidrosim, kā sadalīšana reizinātājos palīdz saīsināt daļu vai "
          "atrisināt vienādojumu.")

_T = "text"

SATURS = [
    Sakums("47 · 53 + 47 · 47 - galvā 5 sekundēs?",
           zimejums=restis([["47 · 53 + 47 · 47"], ["= 47 · (53 + 47)"],
                            ["= 47 · 100 = 4700"]]),
           paraksts="Iznešana pārvērš garu rēķinu vienā reizinājumā.",
           fakti=["Reizinājumu var saīsināt daļā - summu nevar.",
                  "Reizinājums ir 0 tikai, ja kāds reizinātājs ir 0.",
                  "Reizinājums parāda dalītājus."]),

    Slidnis("Trīs darbi", [
        {"v": "Saīsināt", "teksts": "{x^2 + 3x|x} = {x(x + 3)|x} = x + 3 "
                                    "(x ≠ 0)"},
        {"v": "Atrisināt", "teksts": "x^2 − 5x = 0 ⇒ x(x − 5) = 0 ⇒ x = 0 vai "
                                     "x = 5"},
        {"v": "Rēķināt", "teksts": "23 · 19 − 23 · 9 = 23 · 10 = 230"},
    ]),

    Doma("Reizinājums ir ērtāks",
         "Summā locekļi ir «savienoti ar +», un tos saīsināt vai atdalīt "
         "nevar; reizinājumā katrs reizinātājs ir atsevišķs.",
         soli=[
             "Daļā saīsina tikai kopīgus reizinātājus - ne saskaitāmos!",
             "Vienādojumā ar «= 0» katru reizinātāju pielīdzina nullei.",
             "Rēķinos iznes kopīgo skaitli un saskaita iekavās.",
         ],
         pieze="{x + 3|x} NEVAR saīsināt uz 3 - x nav reizinātājs "
               "skaitītājā."),

    Ievadi("Saīsini daļu", [
        {"jaut": "{5x + 10|5} = ?", "atb": ["x + 2", "2 + x"],
         "tastatura": _T, "padoms": "5(x + 2) : 5."},
        {"jaut": "{a^2 − 4a|a} = ? (a ≠ 0)", "atb": ["a − 4"],
         "tastatura": _T, "padoms": "a(a − 4) : a."},
        {"jaut": "{3x|6x + 9} = {x|? + 3}", "atb": ["2x"], "tastatura": _T,
         "padoms": "6x + 9 = 3(2x + 3)."},
        {"jaut": "{2a + 2b|a + b} = ?", "atb": ["2"],
         "padoms": "2(a + b) : (a + b)."},
    ]),

    Ievadi("Rēķini galvā", [
        {"jaut": "36 · 57 + 36 · 43 = ?", "atb": ["3600", "3 600"],
         "padoms": "36 · 100."},
        {"jaut": "8,3 · 12 − 8,3 · 2 = ?", "atb": ["83"],
         "padoms": "8,3 · 10."},
        {"jaut": "125 · 7 + 125 = ?", "atb": ["1000", "1 000"],
         "padoms": "125 · 8."},
    ]),

    Varianti("Pareizi saīsināts?", [
        {"jaut": "{x + 5|5} = x",
         "opcijas": ["Nē - 5 nav reizinātājs skaitītājā", "Jā",
                     "Jā, ja x > 0", "Jā, ja x = 5"],
         "pareizi": 0, "padoms": "Pārbaudi ar x = 1: {6|5} ≠ 1."},
        {"jaut": "{4x + 8|4} = x + 2",
         "opcijas": ["Jā", "Nē, jābūt x + 8", "Nē, jābūt 4x + 2",
                     "Nē, jābūt x"],
         "pareizi": 0, "padoms": "4(x + 2) : 4."},
    ]),

    Pasaule("Kinoteātra biļetes",
            Ievadi("", [
                {"jaut": "Biļete 7,50 €. Pirmdien pārdoja 86, otrdien 114. "
                         "Ieņēmumi = 7,50 · (86 + 114) = ? €",
                 "atb": ["1500"], "padoms": "7,50 · 200."},
                {"jaut": "Popkorns 4,20 € : 35 + 65 pārdoti. Ieņēmumi (€)?",
                 "atb": ["420"], "padoms": "4,20 · 100."},
            ]),
            pavediens="veikals",
            konteksts="Kinoteātra vadītājs saskaita dienu apmeklējumu un "
                      "reizina ar cenu vienreiz.",
            kapec="Iznesot cenu, rēķins kļūst galvā izdarāms."),

    Kopsavilkums([
        "Saīsinu daļu pēc sadalīšanas reizinātājos.",
        "Zinu, ka saīsina tikai reizinātājus.",
        "Rēķinu izdevīgi ar iznešanu.",
    ]),

    Majas([
        "Saīsini: {6x^2 − 9x|3x}; {7a + 7b|14}.",
        "Aprēķini galvā: 99 · 17 + 17.",
        "Atrisini: x^2 − 7x = 0.",
    ]),
]
