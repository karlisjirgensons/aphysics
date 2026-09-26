# -*- coding: utf-8 -*-
"""9. klase, 89. stunda: «Kā rīkoties ar daļām vienādojumā?»

Daļas un iekavas vispirms pazūd: reizina ar kopsaucēju, atver iekavas,
pārnes - tikai tad sakņu formula. Tā atbrīvojas no daļskaitļu rēķiniem,
kuros visvieglāk kļūdīties.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, saknes)

TEMA = "Kā rīkoties ar daļām vienādojumā?"

MERKIS = ("Atrisināsim vienādojumu, kurā ir daļas vai iekavas, veicot "
          "pārveidojumus.")

_T = "text"

SATURS = [
    Sakums("{x^2|6} − {x|2} = {2|3} - kur sākt?",
           fakti=["Kopsaucējs 6: reizina visus locekļus ar 6.",
                  "x^2 − 3x = 4 ⇒ x^2 − 3x − 4 = 0.",
                  "Saknes: −1 un 4 - bez daļām."]),

    Doma("Daļas prom",
         "Reizini abas puses ar visu saucēju mazāko kopīgo dalāmo - daļas "
         "pazūd, saknes paliek tās pašas.",
         soli=[
             "Atrodi kopsaucēju.",
             "Reizini KATRU locekli (arī labajā pusē!).",
             "Atver iekavas, pārnes, savelc.",
             "Atrisini un pārbaudi sākotnējā vienādojumā.",
         ]),

    Slidnis("Piemērs pa soļiem", [
        {"v": "Dots", "teksts": "{x(x − 1)|2} − {x + 3|4} = 1"},
        {"v": "· 4", "teksts": "2x(x − 1) − (x + 3) = 4"},
        {"v": "Iekavas", "teksts": "2x^2 − 2x − x − 3 = 4"},
        {"v": "Standarts", "teksts": "2x^2 − 3x − 7 = 0; D = 9 + 56 = 65"},
        {"v": "Saknes", "teksts": "x_{1;2} = {3 ± √65|4}"},
    ]),

    Paraugs("Iekavas abās pusēs",
            uzd="Atrisini (x − 2)^2 = 2(x + 2).",
            soli=[
                ("x^2 − 4x + 4 = 2x + 4", "Atver."),
                ("x^2 − 6x = 0", "Pārnes."),
                ("x(x − 6) = 0 ⇒ x = 0 vai x = 6", "Nepilnais - bez D."),
            ],
            atbilde="0; 6"),

    Ievadi("Atrisini", [
        {"jaut": "{x^2|2} = x + 4", "atb": saknes("−2", "4"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "x^2 − 2x − 8 = 0."},
        {"jaut": "{x^2|3} − {x|3} = 2", "atb": saknes("−2", "3"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "x^2 − x − 6 = 0."},
        {"jaut": "(x + 1)(x − 1) = 2x + 2", "atb": saknes("−1", "3"),
         "tastatura": _T, "vieta": "x₁; x₂", "padoms": "x^2 − 2x − 3 = 0."},
        {"jaut": "x(x + 5) = 3(x + 5)", "atb": saknes("−5", "3"),
         "tastatura": _T, "vieta": "x₁; x₂",
         "padoms": "(x + 5)(x − 3) = 0 - nedali ar x + 5!"},
    ]),

    Varianti("Kur kļūda?", [
        {"jaut": "{x^2|4} − x = 3 ⇒ · 4 ⇒ x^2 − x = 12",
         "opcijas": ["−x arī jāreizina: x^2 − 4x = 12", "Pareizi",
                     "3 nav jāreizina", "Jāreizina ar 2"],
         "pareizi": 0, "padoms": "Katrs loceklis."},
        {"jaut": "2 − (x − 3)^2 = 0 ⇒ 2 − x^2 − 6x + 9 = 0",
         "opcijas": ["Zīmes: 2 − x^2 + 6x − 9", "Pareizi",
                     "Jābūt 2 − x^2 − 9", "Jābūt −x^2 + 3"],
         "pareizi": 0, "padoms": "−(x^2 − 6x + 9)."},
    ]),

    Pasaule("Kopīgs darbs",
            Ievadi("", [
                {"jaut": "Viens sūknis piepilda baseinu x h, otrs x + 2 h, "
                         "kopā 2,4 h: {1|x} + {1|x + 2} = {1|2,4}. Tas dod "
                         "x^2 − 2,8x − 4,8 = 0. Pozitīvā sakne?", "atb": ["4"],
                 "padoms": "D = 7,84 + 19,2 = 27,04 = 5,2^2."},
                {"jaut": "Cik h vajag otrajam sūknim?", "atb": ["6"],
                 "padoms": "4 + 2."},
            ]),
            pavediens="tehnika",
            konteksts="Darba uzdevumos daļas rodas pašas - tās jānovāc ar "
                      "kopsaucēju.",
            kapec="Bez daļām kvadrātvienādojums kļūst parasts."),

    Kopsavilkums([
        "Reizinu ar kopsaucēju, lai atbrīvotos no daļām.",
        "Atveru iekavas un pārvēršu standartformā.",
        "Nedalu ar izteiksmi ar x.",
    ]),

    Majas([
        "Atrisini: {x^2|5} + {x|2} = {3|10}.",
        "Atrisini: (2x − 1)^2 − 3 = x(x + 2).",
        "Pārbaudi saknes sākotnējā vienādojumā.",
    ]),
]
