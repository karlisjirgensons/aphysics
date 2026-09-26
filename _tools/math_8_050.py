# -*- coding: utf-8 -*-
"""8. klase, 50. stunda: «Ko nozīmē vilkt kvadrātsakni?»

Kvadrātsakne ir kāpināšanas kvadrātā pretējā darbība: pēc laukuma atrod
kvadrāta malu. Definīcijā svarīgs ir vārds «nenegatīvs» - tāpēc √25 = 5,
nevis −5, lai gan arī (−5)^2 = 25.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, figura, kvadrats)

TEMA = "Ko nozīmē vilkt kvadrātsakni?"

MERKIS = ("Sapratīsim aritmētiskās kvadrātsaknes definīciju un minēsim "
          "piemērus.")

SATURS = [
    Sakums("Kvadrāta laukums 36 m² - cik gara mala?",
           zimejums=kvadrats(6, 6, paraksts="S = 36"),
           paraksts="Mala 6, jo 6 · 6 = 36.",
           fakti=["No malas uz laukumu - kāpina kvadrātā.",
                  "No laukuma uz malu - velk kvadrātsakni.",
                  "√36 = 6."]),

    Doma("Aritmētiskā kvadrātsakne",
         "Skaitļa a aritmētiskā kvadrātsakne √a ir tāds nenegatīvs skaitlis, "
         "kura kvadrāts ir a: √a = b, ja b ≥ 0 un b^2 = a.",
         soli=[
             "a sauc par zemsaknes izteiksmi.",
             "√a ≥ 0 vienmēr - sakne nekad nav negatīva.",
             "(√a)^2 = a, ja a ≥ 0.",
             "Pārbaude: sareizini atbildi pašu ar sevi.",
         ],
         pieze="Arī (−6)^2 = 36, bet aritmētiskā sakne ir tikai 6. Kur "
               "vajag abus skaitļus, raksta ±√36 = ±6."),

    Slidnis("Kvadrāts un sakne - divi virzieni", [
        {"v": "3 → 9", "teksts": "Kāpina: 3^2 = 9"},
        {"v": "9 → 3", "teksts": "Velk sakni: √9 = 3"},
        {"v": "0,5 → 0,25", "teksts": "0,5^2 = 0,25"},
        {"v": "0,25 → 0,5", "teksts": "√(0,25) = 0,5"},
        {"v": "{2|3} → {4|9}", "teksts": "Un atpakaļ: √{4|9} = {2|3}"},
    ]),

    Paraugs("Pārbaudi ar definīciju",
            uzd="Vai √(1,21) = 1,1? Vai √16 = −4?",
            soli=[
                ("1,1 ≥ 0 un 1,1^2 = 1,21", "Abi nosacījumi izpildās."),
                ("√(1,21) = 1,1 - pareizi", "Definīcija izpildās."),
                ("−4 < 0", "Sakne nevar būt negatīva."),
                ("√16 = 4, nevis −4", "Ņem nenegatīvo."),
            ],
            atbilde="pirmais pareizi, otrais - nē"),

    Ievadi("Izvelc sakni", [
        {"jaut": "√49", "atb": ["7"], "padoms": "7 · 7."},
        {"jaut": "√121", "atb": ["11"], "padoms": "11 · 11."},
        {"jaut": "√(0,09)", "atb": ["0,3", "0.3"], "padoms": "0,3 · 0,3."},
        {"jaut": "√{16|25} - atbildi raksti kā a/b",
         "atb": ["{4|5}", "4/5", "0,8"], "padoms": "{√16|√25}."},
        {"jaut": "(√7)^2", "atb": ["7"], "padoms": "Definīcija."},
        {"jaut": "√0", "atb": ["0"], "padoms": "0 · 0 = 0."},
    ], pamats=4),

    Varianti("Pareizi vai nē?", [
        {"jaut": "√100 = ±10",
         "opcijas": ["Nē - √100 = 10", "Jā", "Nē - √100 = 50",
                     "Nē - nav definēts"],
         "pareizi": 0, "padoms": "Sakne nav negatīva."},
        {"jaut": "√(0,4) = 0,2",
         "opcijas": ["Nē - 0,2^2 = 0,04", "Jā", "Nē - √(0,4) = 0,02",
                     "Nē - nav definēts"],
         "pareizi": 0, "padoms": "Pārbaudi kvadrātu."},
        {"jaut": "Kvadrāta laukums 81 cm². Mala ir...",
         "opcijas": ["9 cm", "40,5 cm", "20,25 cm", "−9 cm"],
         "pareizi": 0, "padoms": "√81."},
    ]),

    Pasaule("Kvadrātveida flīzes",
            Ievadi("", [
                {"jaut": "Flīze ir kvadrāts ar laukumu 900 cm². Cik cm gara "
                         "mala?",
                 "atb": ["30"], "padoms": "√900."},
                {"jaut": "Kvadrātveida terase 16 m². Cik flīžu 30 × 30 cm "
                         "vienā rindā gar malu? (veselas, uz augšu)",
                 "atb": ["14"], "padoms": "4 m : 0,3 m ≈ 13,3."},
                {"jaut": "Cik flīžu kopā (rindas × kolonnas)?",
                 "atb": ["196"], "padoms": "14 · 14."},
            ]),
            pavediens="maja",
            konteksts="Flīžu veikalā raksta laukumu, bet liekot vajag malas "
                      "garumu - to dod kvadrātsakne.",
            kapec="Kvadrātsakne pārvērš laukumu atpakaļ par garumu.",
            zimejums=figura([(1, 1), (5, 1), (5, 5), (1, 5)],
                            [(3, 0.4, "4 m"), (5.8, 3, "4 m")],
                            platums=7, augstums=6)),

    Kopsavilkums([
        "Zinu aritmētiskās kvadrātsaknes definīciju.",
        "Zinu, ka √a ≥ 0.",
        "Pārbaudu sakni, kāpinot kvadrātā.",
        "Atrodu kvadrāta malu no laukuma.",
    ]),

    Majas([
        "Iemācies kvadrātus no 11^2 līdz 20^2.",
        "Izvelc: √144, √(0,64), √{1|81}.",
        "Nomēri kvadrātveida priekšmetu mājās un pārbaudi √S = a.",
    ]),
]
