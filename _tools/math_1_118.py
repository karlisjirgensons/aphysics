# -*- coding: utf-8 -*-
"""1. klase, 118. stunda: «Kāds jautājums der šim stāstam?»

Stāstam bez jautājuma matemātiskais uzdevums vēl nav. Skolēns izdomā
jautājumu, uz kuru var atbildēt ar dotajiem skaitļiem, un atbild.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kāds jautājums der šim stāstam?"

MERKIS = ("Šodien izdomāsim matemātisku jautājumu tekstā dotai situācijai "
          "un atbildēsim uz to.")

SATURS = [
    Sakums("«Dārzā 8 tulpes un 6 narcises.» - Kāds jautājums?",
           fakti=["«Cik puķu kopā?» - 8 + 6.",
                  "«Par cik tulpju vairāk?» - 8 − 6.",
                  "Jautājumam jābūt atbildamam ar skaitļiem."]),

    Doma("Labs jautājums",
         "Labs jautājums sākas ar «cik» vai «par cik» un izmanto stāsta "
         "skaitļus.",
         soli=[
             "Izlasi, kādi skaitļi ir stāstā.",
             "Izdomā: cik kopā? par cik vairāk? cik palika?",
             "Pārbaudi, vai vari atbildēt.",
         ]),

    Varianti("Vai jautājums der?", [
        {"jaut": "Stāsts: «Plauktā 12 grāmatas, 4 paņēma.» Jautājums: "
                 "«Cik grāmatu palika?»",
         "opcijas": ["der", "neder"], "jaukt": False, "pareizi": 0,
         "padoms": "12 − 4."},
        {"jaut": "Tas pats stāsts. «Kādā krāsā grāmatas?»",
         "opcijas": ["neder - nav skaitļu", "der"], "jaukt": False,
         "pareizi": 0, "padoms": "To nevar izrēķināt."},
        {"jaut": "«Anna 9 gadi, Juris 6.» «Par cik Anna vecāka?»",
         "opcijas": ["der", "neder"], "jaukt": False, "pareizi": 0,
         "padoms": "9 − 6."},
    ]),

    Ievadi("Atbildi uz jautājumu", [
        {"jaut": "Dārzā 8 tulpes un 6 narcises. Cik puķu kopā?",
         "atb": ["14"], "padoms": "8 + 6."},
        {"jaut": "Par cik tulpju vairāk nekā narcišu?", "atb": ["2"],
         "padoms": "8 − 6."},
        {"jaut": "Plauktā 12 grāmatas, 4 paņēma. Cik palika?",
         "atb": ["8"], "padoms": "12 − 4."},
    ]),

    Pasaule("Pastaiga mežā",
            Varianti("", [
                {"jaut": "«Mežā redzējām 5 vāveres un 9 putnus.» Kurš "
                         "jautājums der?",
                 "opcijas": ["Cik dzīvnieku redzējām kopā?",
                             "Kā sauc mežu?", "Vai bija jautri?"],
                 "pareizi": 0, "padoms": "Jautājums ar «cik»."},
            ]),
            pavediens="daba",
            konteksts="Pēc pastaigas klase stāsta, ko redzēja.",
            kapec="Jautājums pārvērš stāstu uzdevumā."),

    Kopsavilkums([
        "Izdomāju jautājumu stāstam.",
        "Pārbaudu, vai uz to var atbildēt.",
        "Atbildu uz savu jautājumu.",
    ]),

    Majas([
        "Izdomā 2 dažādus jautājumus stāstam par savu istabu.",
        "Atbildi uz tiem.",
        "Palūdz mājiniekam izdomāt trešo.",
    ]),
]
