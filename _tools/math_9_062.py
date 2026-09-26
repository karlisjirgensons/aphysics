# -*- coding: utf-8 -*-
"""9. klase, 62. stunda: «Kā pārbaudīt sadalījumu?»

Divas pārbaudes: atvērt iekavas (drošā) un ievietot skaitli (ātrā, bet
viens skaitlis var «nejauši» sakrist). Mikrotemata noslēgums - jaukti
sadalīšanas uzdevumi ar pašpārbaudi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā pārbaudīt sadalījumu?"

MERKIS = ("Pārbaudīsim sadalījumu, atverot iekavas vai ievietojot skaitli.")

_T = "text"

SATURS = [
    Sakums("Vai 2x^2 + 6x = 2x(x + 6)?",
           zimejums=restis([["x", "2x² + 6x", "2x(x + 6)"],
                            ["1", "8", "14"]]),
           paraksts="Ar x = 1 vērtības atšķiras - sadalījums kļūdains.",
           fakti=["Pareizi: 2x(x + 3).",
                  "Ievietošana ātri atklāj kļūdu.",
                  "Atverot iekavas, pārbaude ir pilnīga."]),

    Doma("Divas pārbaudes",
         "Atver iekavas un salīdzini ar sākotnējo izteiksmi; ātrai pārbaudei "
         "ievieto vienu vai divus skaitļus.",
         soli=[
             "Atverot iekavas, jāiegūst tieši sākotnējā izteiksme.",
             "Ievietojot skaitli, abām pusēm jādod viena vērtība.",
             "Izvēlies «neparastu» skaitli (piem., 3), ne 0 vai 1.",
             "Ja vērtības atšķiras - kļūda noteikti ir.",
         ],
         pieze="Ja vērtības sakrīt vienam skaitlim, tas vēl nav pierādījums; "
               "iekavu atvēršana ir."),

    Paraugs("Pārbaude ar atvēršanu",
            uzd="Pārbaudi: ab − 3a + 2b − 6 = (a + 2)(b − 3).",
            soli=[
                ("(a + 2)(b − 3) = ab − 3a + 2b − 6", "Atver iekavas."),
                ("Sakrīt ar sākotnējo", "Sadalījums pareizs."),
                ("Ātrā pārbaude: a = 3, b = 5: 15 − 9 + 10 − 6 = 10; "
                 "5 · 2 = 10", "Arī sakrīt."),
            ],
            atbilde="pareizi"),

    Varianti("Pareizi vai nē?", [
        {"jaut": "9x^2 − 3x = 3x(3x − 1)",
         "opcijas": ["Pareizi", "Nē: 3x(3x − 3)", "Nē: 3(3x − x)",
                     "Nē: 9x(x − 3)"],
         "pareizi": 0, "padoms": "Atver: 9x^2 − 3x."},
        {"jaut": "x^2 + 2x + x + 2 = (x + 2)(x + 2)",
         "opcijas": ["Nē: (x + 2)(x + 1)", "Pareizi", "Nē: (x + 1)^2",
                     "Nē: x(x + 3)"],
         "pareizi": 0, "padoms": "x(x + 2) + 1(x + 2)."},
        {"jaut": "Ar x = 2 abas puses dod 12. Vai sadalījums noteikti pareizs?",
         "opcijas": ["Ne noteikti - var sakrist nejauši", "Jā, noteikti",
                     "Nē, noteikti nepareizs", "Jāņem x = 0"],
         "pareizi": 0, "padoms": "Pierādījums - atvēršana."},
    ]),

    Ievadi("Sadali un pārbaudi", [
        {"jaut": "4a^2 − 10a", "atb": ["2a(2a − 5)"], "tastatura": _T,
         "padoms": "LKD 2, burts a."},
        {"jaut": "Pārbaudi ar a = 3: 4 · 9 − 30 = ?", "atb": ["6"],
         "padoms": "36 − 30."},
        {"jaut": "x^2 − xy + 2x − 2y", "atb": ["(x − y)(x + 2)",
                                               "(x + 2)(x − y)"],
         "tastatura": _T, "padoms": "x(x − y) + 2(x − y)."},
        {"jaut": "6m^3 + 3m^2 − 9m", "atb": ["3m(2m^2 + m − 3)"],
         "tastatura": _T, "padoms": "Visos 3m."},
    ]),

    Pasaule("Kalkulatora kļūda?",
            Varianti("", [
                {"jaut": "Programma sadalīja 5x^2 − 20x = 5x(x − 20). Ievieto "
                         "x = 2: 20 − 40 = −20 un 10 · (−18) = −180. "
                         "Secinājums?",
                 "opcijas": ["Programmā kļūda: jābūt 5x(x − 4)",
                             "Viss pareizi", "Kļūda ievietošanā",
                             "Jāņem x = 0"],
                 "pareizi": 0, "padoms": "20x : 5x = 4."},
            ]),
            pavediens="dati",
            konteksts="Arī datori kļūdās, ja programmā ir kļūda; ātrā "
                      "pārbaude ar skaitli to atklāj.",
            kapec="Pārbaude ir ieradums, ne formalitāte."),

    Kopsavilkums([
        "Pārbaudu sadalījumu, atverot iekavas.",
        "Ātri pārbaudu, ievietojot skaitli.",
        "Zinu, kura pārbaude ir pierādījums.",
    ]),

    Majas([
        "Sadali un pārbaudi divos veidos: 8x^3 − 12x^2; ay + 4a − by − 4b.",
        "Atrodi kļūdu: 3x − 9 = 3(x − 9).",
        "Paskaidro, kāpēc x = 0 ir slikta pārbaudes vērtība.",
    ]),
]
