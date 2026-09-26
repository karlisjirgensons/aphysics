# -*- coding: utf-8 -*-
"""2. klase, 49. stunda: «Cik soļu ir šajā uzdevumā?»

Divu soļu uzdevums: lai atbildētu uz jautājumu, vispirms jāatrod kaut kas
cits. Katru soli pieraksta atsevišķi - ar darbību un tās jēgu - un tikai tad
atbildi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Cik soļu ir šajā uzdevumā?"

MERKIS = ("Šodien risināsim divu soļu situāciju uzdevumus un pierakstīsim "
          "katru darbību.")

SATURS = [
    Sakums("Autobusā bija 34 pasažieri. Pieturā izkāpa 12, iekāpa 9. Cik "
           "tagad?",
           fakti=["Uzreiz atbildēt nevar - vajag divus soļus.",
                  "1) 34 − 12 = 22.",
                  "2) 22 + 9 = 31."]),

    Doma("Soli pa solim",
         "Vispirms atrodi to, bez kā nevar atbildēt uz jautājumu.",
         soli=[
             "Izlasi jautājumu.",
             "Pajautā: ko vēl nezinu, lai atbildētu?",
             "1. solis - atrodi to.",
             "2. solis - atbildi uz jautājumu.",
         ]),

    Paraugs("Cik konfekšu palika?",
            uzd="Paciņā bija 40 konfektes. Anna apēda 8, Toms - 13. Cik "
                "palika?",
            soli=[("1) 8 + 13 = 21", "Cik apēda abi kopā."),
                  ("2) 40 − 21 = 19", "Cik palika.")],
            atbilde="19 konfektes"),

    Ievadi("Divi soļi", [
        {"jaut": "Plauktā 26 grāmatas. Ielika 15, paņēma 8. Cik tagad?",
         "atb": ["33"], "padoms": "26 + 15 = 41, 41 − 8."},
        {"jaut": "Annai 35 €, Līvai par 12 € vairāk. Cik abām kopā?",
         "atb": ["82"], "mers": "€", "padoms": "35 + 12 = 47, 47 + 35."},
        {"jaut": "Dārzā 50 tulpes. 17 sarkanas, 14 dzeltenas, pārējās "
                 "baltas. Cik balto?", "atb": ["19"],
         "padoms": "17 + 14 = 31, 50 − 31."},
        {"jaut": "Klasē 28 bērni. 5 slimo, 9 ekskursijā. Cik klasē?",
         "atb": ["14"], "padoms": "5 + 9 = 14, 28 − 14."},
        {"jaut": "Mārtiņam 43 kartītes. Viņš iedeva 18, saņēma 25. Cik "
                 "tagad?", "atb": ["50"], "padoms": "43 − 18 = 25, 25 + 25."},
        {"jaut": "Veikalā 60 maizes. No rīta pārdeva 27, pēcpusdienā 24. "
                 "Cik palika?", "atb": ["9"], "padoms": "27 + 24 = 51."},
    ], pamats=4),

    Varianti("Kāds ir pirmais solis?", [
        {"jaut": "Toms nopirka 3 grāmatas par 12 €, 15 € un 9 €. Cik "
                 "atlikums no 50 €?",
         "opcijas": ["12 + 15 + 9", "50 − 12", "50 + 9"], "pareizi": 0,
         "padoms": "Vispirms kopējā cena."},
        {"jaut": "Zēnam 23 pastmarkas, meitenei par 8 vairāk. Cik kopā?",
         "opcijas": ["23 + 8 - cik meitenei", "23 + 23", "23 − 8"],
         "pareizi": 0, "padoms": "Vispirms uzzini, cik meitenei."},
    ]),

    Pasaule("Vai pietiks vietu autobusā?",
            Ievadi("", [
                {"jaut": "Autobusā 50 vietas. Iekāpa 23 skolēni un 4 "
                         "skolotāji. Cik vietu brīvas?", "atb": ["23"],
                 "padoms": "23 + 4 = 27, 50 − 27."},
                {"jaut": "Nākamajā pieturā iekāpa vēl 18. Cik vietu "
                         "brīvas tagad?", "atb": ["5"], "padoms": "23 − 18."},
            ]),
            pavediens="celojums",
            konteksts="Skola brauc ekskursijā uz Siguldu.",
            kapec="Katrs solis pasaka kaut ko jaunu."),

    Kopsavilkums([
        "Atrodu, ko vēl vajag uzzināt, lai atbildētu.",
        "Risinu uzdevumu divos soļos.",
        "Pierakstu katru darbību.",
    ]),

    Majas([
        "Izdomā divu soļu uzdevumu par savu dienu.",
        "Atrisini to pa soļiem.",
        "Lai mājinieks pārbauda.",
    ]),
]
