# -*- coding: utf-8 -*-
"""9. klase, 117. stunda: «Kā atrisināt sarežģītāku sistēmu?»

Sistēma ar iekavām un daļām: vispirms katru vienādojumu pārveido formā
ax + by = c (atver iekavas, reizina ar kopsaucēju, pārnes), un tikai tad
izvēlas paņēmienu. Tā pati kārtība kā kvadrātvienādojumiem 84. stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, paris)

TEMA = "Kā atrisināt sarežģītāku sistēmu?"

MERKIS = ("Atrisināsim sistēmu, kurā vispirms nepieciešami pārveidojumi.")

_T = "text"

SATURS = [
    Sakums("{x|2} + {y|3} = 4 un 2(x − y) = x − 4",
           fakti=["Pirmo reizina ar 6: 3x + 2y = 24.",
                  "Otrajā atver iekavas: x − 2y = −4.",
                  "Tagad - saskaitīšana: 4x = 20."]),

    Doma("Vispirms sakārto",
         "Pārveido katru vienādojumu formā ax + by = c; pēc tam risini kā "
         "parasti.",
         soli=[
             "Atver iekavas.",
             "Daļām - reizini ar kopsaucēju.",
             "x un y pa kreisi, skaitļi pa labi.",
             "Ja iespējams, izdali ar kopīgu reizinātāju.",
             "Izvēlies paņēmienu un atrisini.",
         ]),

    Slidnis("Sākuma sistēma līdz galam", [
        {"v": "1", "teksts": "{x|2} + {y|3} = 4 | · 6 ⇒ 3x + 2y = 24"},
        {"v": "2", "teksts": "2(x − y) = x − 4 ⇒ 2x − 2y − x = −4 ⇒ "
                             "x − 2y = −4"},
        {"v": "3", "teksts": "Saskaita: 4x = 20 ⇒ x = 5"},
        {"v": "4", "teksts": "5 − 2y = −4 ⇒ y = 4,5; atbilde (5; 4,5)"},
    ]),

    Paraugs("Iekavas abos",
            uzd="Atrisini: 3(x + 1) − y = 10 un x + 2(y − 3) = 1.",
            soli=[
                ("3x − y = 7 un x + 2y = 7", "Sakārtots."),
                ("y = 3x − 7; x + 6x − 14 = 7 ⇒ x = 3", "Ievietošana."),
                ("y = 9 − 7 = 2", "Otrs nezināmais."),
            ],
            atbilde="(3; 2)"),

    Ievadi("Sakārto un atrisini", [
        {"jaut": "2(x + y) = 14 un x − y = 1", "atb": paris(4, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "x + y = 7."},
        {"jaut": "{x|3} + y = 5 un x − y = 7", "atb": paris(9, 2),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "x + 3y = 15."},
        {"jaut": "{x + y|2} = 6 un {x − y|4} = 1", "atb": paris(8, 4),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "x + y = 12, x − y = 4."},
        {"jaut": "0,5x + 0,2y = 3 un x − y = −1", "atb": paris(4, 5),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "· 10: 5x + 2y = 30."},
    ], pamats=2),

    Varianti("Pirmais solis", [
        {"jaut": "{x|4} − {y|6} = 1. Ar ko reizināt?",
         "opcijas": ["12", "24", "4", "10"],
         "pareizi": 0, "padoms": "MKD(4; 6)."},
        {"jaut": "3(x − 2y) = 2(x + 1) pēc sakārtošanas:",
         "opcijas": ["x − 6y = 2", "x − 6y = 1", "5x − 6y = 2",
                     "x + 6y = 2"],
         "pareizi": 0, "padoms": "3x − 6y = 2x + 2."},
    ]),

    Pasaule("Maisījuma cena",
            Ievadi("", [
                {"jaut": "Tējas maisījums: x kg pa 20 €/kg un y kg pa 30 €/kg, "
                         "kopā 5 kg, vidējā cena 24 €/kg. {20x + 30y|5} = 24 ⇒ "
                         "2x + 3y = 12, x + y = 5. x = ?", "atb": ["3"],
                 "padoms": "Atņem 2(x + y) = 10: y = 2."},
                {"jaut": "y = ?", "atb": ["2"], "padoms": "5 − 3."},
            ]),
            pavediens="virtuve",
            konteksts="Tējnīca jauc lētu un dārgu tēju, lai iegūtu vidējās "
                      "cenas maisījumu.",
            kapec="Daļa ar vidējo cenu - vispirms jānovāc."),

    Kopsavilkums([
        "Sakārtoju vienādojumus formā ax + by = c.",
        "Atbrīvojos no daļām un iekavām.",
        "Atrisinu ar piemērotu paņēmienu.",
    ]),

    Majas([
        "Atrisini: {x|3} − {y|2} = 0 un 2x + y = 16.",
        "Atrisini: 5(x − y) = 2x + 1 un 3x − 4y = 2.",
        "Pārbaudi atbildes sākotnējā sistēmā.",
    ]),
]
