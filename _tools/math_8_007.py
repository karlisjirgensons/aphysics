# -*- coding: utf-8 -*-
"""8. klase, 7. stunda: «Kas ir mediāna?»

Mediāna ir vidējā vērtība sakārtotā rindā - pusē datu ir mazākas, pusē
lielākas. Divi gadījumi: nepāra skaitam tā ir viena vērtība, pāra skaitam -
divu vidējo vērtību vidējais. Slīdnis parāda, kā to atrod no abiem galiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kas ir mediāna?"

MERKIS = ("Noteiksim sakārtotas datu kopas mediānu un sapratīsim, ko tā "
          "parāda.")


def _rinda(vertibas, izcelt=()):
    """Sakārtota rinda; izsvītrotās no galiem aizstāj ar «·»."""
    return restis([[("·" if i in izcelt else str(v))
                    for i, v in enumerate(vertibas)]])


_AUGUMI = [152, 158, 160, 163, 165, 171, 176]

SATURS = [
    Sakums("Kurš stāv tieši vidū?",
           zimejums=restis([[str(v) for v in _AUGUMI]]),
           paraksts="Septiņi skolēni augumu secībā (cm).",
           fakti=["Vidū ir ceturtais - 163 cm.",
                  "Trīs ir īsāki, trīs garāki.",
                  "Šī vērtība ir mediāna."]),

    Doma("Mediāna - sakārtotas rindas vidus",
         "Mediāna ir vērtība sakārtotas datu kopas vidū: pusē vērtību ir "
         "mazākas vai vienādas, pusē - lielākas vai vienādas.",
         soli=[
             "Sakārto datus augošā secībā.",
             "Ja n ir nepāra - mediāna ir vērtība vietā {n + 1|2}.",
             "Ja n ir pāra - mediāna ir abu vidējo vērtību vidējais.",
             "Pārbaude: abās pusēs mediānai ir vienādi daudz vērtību.",
         ],
         pieze="Izklājlapā: =MEDIAN(B2:B20). Kārtot pirms tam nav "
               "vajadzīgs - to izdara formula."),

    Slidnis("Svītro no abiem galiem", [
        {"v": "7 vērtības", "teksts": "Sakārtotas", "zim": _rinda(_AUGUMI)},
        {"v": "1. solis", "teksts": "Izsvītro mazāko un lielāko",
         "zim": _rinda(_AUGUMI, (0, 6))},
        {"v": "2. solis", "teksts": "Atkal abus galus",
         "zim": _rinda(_AUGUMI, (0, 1, 5, 6))},
        {"v": "Mediāna 163", "teksts": "Paliek viena vērtība",
         "zim": _rinda(_AUGUMI, (0, 1, 2, 4, 5, 6))},
    ], ievads="Tā mediānu atrod bez formulas."),

    Paraugs("Pāra skaits vērtību",
            uzd="Atrodi mediānu: 12, 7, 15, 9, 20, 10.",
            soli=[
                ("7; 9; 10; 12; 15; 20", "Sakārto."),
                ("Vidū ir divas: 10 un 12", "n = 6 - pāra."),
                ("(10 + 12) : 2 = 11", "Abu vidējais."),
            ],
            atbilde="mediāna ir 11"),

    Ievadi("Atrodi mediānu", [
        {"jaut": "5, 8, 3, 9, 6",
         "atb": ["6"], "padoms": "3; 5; 6; 8; 9."},
        {"jaut": "14, 11, 18, 13",
         "atb": ["13,5", "13.5"], "padoms": "11; 13; 14; 18."},
        {"jaut": "2, 2, 3, 7, 7, 7, 9",
         "atb": ["7"], "padoms": "Ceturtā vērtība."},
        {"jaut": "−4, 1, −2, 0",
         "atb": ["−1", "-1"], "padoms": "(−2 + 0) : 2."},
        {"jaut": "Kopā 25 vērtības. Kurā vietā ir mediāna?",
         "atb": ["13"], "padoms": "(25 + 1) : 2."},
        {"jaut": "Kopā 40 vērtības. Mediāna ir 20. un kuras vērtības "
                 "vidējais?",
         "atb": ["21"], "padoms": "Divas vidējās."},
    ], pamats=4),

    Varianti("Mediāna vai nē?", [
        {"jaut": "Kopā 1, 2, 3, 4, 100 nomaina 100 ar 1000. Mediāna...",
         "opcijas": ["nemainās", "palielinās", "samazinās", "kļūst 1000"],
         "pareizi": 0, "padoms": "Vidus vērtība paliek 3."},
        {"jaut": "Mediāna ir 50 punkti. Ko tas nozīmē?",
         "opcijas": ["Puse ieguva ne vairāk par 50, puse - ne mazāk",
                     "Visi ieguva 50", "Vidēji ieguva 50",
                     "Visbiežāk ieguva 50"],
         "pareizi": 0, "padoms": "Puse zem, puse virs."},
    ]),

    Pasaule("Mājokļu cenas",
            Ievadi("", [
                {"jaut": "Pārdoto dzīvokļu cenas (tūkst. €): 62, 75, 80, "
                         "88, 240. Kāda ir mediāna?",
                 "atb": ["80"], "padoms": "Trešā vērtība."},
                {"jaut": "Kāds ir aritmētiskais vidējais?",
                 "atb": ["109"], "padoms": "545 : 5."},
                {"jaut": "Cik no pieciem dzīvokļiem maksā vairāk par "
                         "vidējo?",
                 "atb": ["1"], "padoms": "Tikai 240."},
            ]),
            pavediens="maja",
            konteksts="Nekustamo īpašumu ziņās bieži rāda mediānas cenu: "
                      "viens dārgs dzīvoklis to nesabojā.",
            kapec="Mediāna labāk parāda «parasto» cenu."),

    Kopsavilkums([
        "Atrodu mediānu nepāra un pāra skaitam vērtību.",
        "Zinu, kurā vietā sakārtotā rindā ir mediāna.",
        "Saprotu, ka viena ļoti liela vērtība mediānu nemaina.",
    ]),

    Majas([
        "Pieraksti ģimenes locekļu vecumus un atrodi mediānu.",
        "Salīdzini to ar vidējo vecumu.",
        "Izdomā 6 skaitļus, kuru mediāna ir 10, bet vidējais 12.",
    ]),
]
