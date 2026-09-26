# -*- coding: utf-8 -*-
"""2. klase, 41. stunda: «Kad desmits jāsasmalcina?»

63 − 28: no 3 vienu nevar atņemt 8. Tad vienu desmitu «sasmalcina» 10
vienos: 63 = 50 + 13. Tagad 13 − 8 = 5 un 50 − 20 = 30, kopā 35. Kubiņu
modelis rāda, ka skaitlis nemainās - mainās tikai tā sadalījums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, desmiti)

TEMA = "Kad desmits jāsasmalcina?"

MERKIS = ("Šodien modelēsim atņemšanu, kurā viens desmits jāsadala, un "
          "paskaidrosim soļus.")

SATURS = [
    Sakums("Kā no 3 kubiņiem atņemt 8?",
           zimejums=desmiti(6, 3),
           paraksts="63: 6 stieņi un tikai 3 kubiņi.",
           fakti=["Vienu stieni sadala 10 kubiņos.",
                  "Tagad ir 5 stieņi un 13 kubiņi - joprojām 63.",
                  "No 13 var atņemt 8!"]),

    Doma("Sadala vienu desmitu",
         "Ja vienu nepietiek, vienu desmitu pārvērš 10 vienos.",
         soli=[
             "63 − 28: no 3 nevar atņemt 8.",
             "63 = 50 + 13.",
             "Vieni: 13 − 8 = 5. Desmiti: 50 − 20 = 30.",
             "Kopā: 30 + 5 = 35.",
         ]),

    Slidnis("63 − 28 ar kubiņiem", [
        {"v": "63", "teksts": "6 stieņi, 3 kubiņi.", "zim": desmiti(6, 3)},
        {"v": "50 + 13", "teksts": "Vienu stieni sadala.",
         "zim": desmiti(5, 13)},
        {"v": "− 28", "teksts": "Noņem 2 stieņus un 8 kubiņus.",
         "zim": desmiti(3, 5)},
        {"v": "35", "teksts": "Palika 3 stieņi un 5 kubiņi.",
         "zim": desmiti(3, 5)},
    ]),

    Paraugs("Cik ir 52 − 17?",
            uzd="Sadala vienu desmitu.",
            soli=[("52 = 40 + 12", "No 2 nevar atņemt 7."),
                  ("12 − 7 = 5", "Vieni."), ("40 − 10 = 30", "Desmiti."),
                  ("30 + 5 = 35", "Kopā.")],
            atbilde="35"),

    Ievadi("Atņem", [
        {"jaut": "42 − 18 = ?", "atb": ["24"], "padoms": "42 = 30 + 12: 12 − 8, 30 − 10."},
        {"jaut": "71 − 36 = ?", "atb": ["35"], "padoms": "71 = 60 + 11."},
        {"jaut": "55 − 29 = ?", "atb": ["26"], "padoms": "55 = 40 + 15."},
        {"jaut": "80 − 47 = ?", "atb": ["33"], "padoms": "80 = 70 + 10."},
        {"jaut": "93 − 58 = ?", "atb": ["35"], "padoms": "93 = 80 + 13."},
        {"jaut": "64 − 45 = ?", "atb": ["19"], "padoms": "64 = 50 + 14."},
    ], pamats=4),

    Varianti("Kā sadala?", [
        {"jaut": "74 sadala, lai atņemtu 9. Kā?",
         "opcijas": ["60 + 14", "70 + 14", "7 + 4"], "pareizi": 0,
         "padoms": "Viens desmits pāriet pie vieniem."},
        {"jaut": "Toms: 63 − 28 = 45. Kas noticis?",
         "opcijas": ["Atņēma 3 no 8, nevis sadalīja desmitu",
                     "Pareizi", "Saskaitīja"], "pareizi": 0,
         "padoms": "8 − 3 = 5 ir otrādi."},
    ]),

    Pasaule("Cik kilogramu palika noliktavā?",
            Ievadi("", [
                {"jaut": "Noliktavā bija 82 kg kartupeļu. Ēdnīcai aizveda "
                         "37 kg. Cik palika?", "atb": ["45"], "mers": "kg",
                 "padoms": "82 = 70 + 12."},
                {"jaut": "Vēl aizveda 19 kg. Cik palika?", "atb": ["26"],
                 "mers": "kg", "padoms": "45 − 19."},
            ]),
            pavediens="virtuve",
            konteksts="Skolas ēdnīca katru nedēļu ņem kartupeļus no "
                      "noliktavas.",
            kapec="Pavārs zina, kad jāpasūta vēl."),

    Kopsavilkums([
        "Pamanu, kad vieni nepietiek.",
        "Sadalu vienu desmitu 10 vienos.",
        "Atņemu un saliku rezultātu kopā.",
    ]),

    Majas([
        "No 5 zīmuļu saišķiem pa 10 un 2 zīmuļiem parādi 52 − 17.",
        "Kad vajag, izjauc vienu saišķi.",
        "Izrēķini: 61 − 24, 83 − 56.",
    ]),
]
