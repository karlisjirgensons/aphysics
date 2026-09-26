# -*- coding: utf-8 -*-
"""4. klase, 35. stunda: «Ko atlikums nozīmē dzīvē?»

Tas pats 50 : 8 = 6 (atl. 2) dod dažādas atbildes: 6 pilnas kastes, 7
kastes, lai viss ietilpst, vai 2 paliek pāri. Stunda māca izlasīt
jautājumu un izlemt, ko atlikums dara ar atbildi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Ko atlikums nozīmē dzīvē?"

MERKIS = ("Risināsim praktiskus uzdevumus ar atlikumu un paskaidrosim, ko "
          "izsaka dalījums un ko - atlikums.")

SATURS = [
    Sakums("Cik laivu vajag 26 bērniem?",
           zimejums=restis([["jautājums", "atbilde"],
                            ["cik pilnu laivu", "6"],
                            ["cik laivu vajag", "7"],
                            ["cik bērnu pēdējā", "2"]],
                           "26 : 4 = 6 (atl. 2)"),
           paraksts="Viens rēķins - trīs dažādas atbildes.",
           fakti=["Laivā sēž 4 bērni.",
                  "Divus bērnus krastā atstāt nedrīkst!"]),

    Doma("Atbildi nosaka jautājums",
         "Pēc dalīšanas ar atlikumu izlem: vai atlikumu atmet, vai tā dēļ "
         "vajag vēl vienu, vai tas pats ir atbilde.",
         soli=[
             "«Cik pilnu...?» - atlikumu atmet.",
             "«Cik vajag, lai visiem pietiek?» - dalījumam pieskaita 1.",
             "«Cik paliek pāri?» - atbilde ir atlikums.",
             "Pārbaudi, vai atbilde der dzīvē.",
         ],
         pieze="Ja atlikums ir 0, «cik vajag» un «cik pilnu» atbilde ir "
               "vienāda."),

    Paraugs("Autobusi uz sporta spēlēm",
            uzd="130 līdzjutēji, autobusā 50 vietu. Cik autobusu vajag?",
            soli=[
                ("130 : 50 = 2 (atl. 30)", None),
                ("30 līdzjutēji paliek", "Viņiem vajag vēl vienu autobusu."),
                ("2 + 1 = 3", None),
            ],
            atbilde="3 autobusi"),

    Ievadi("Izlasi jautājumu", [
        {"jaut": "50 cepumi, kastē 8. Cik *pilnu* kastu?", "atb": ["6"],
         "padoms": "50 : 8 = 6 (atl. 2)."},
        {"jaut": "50 cepumi, kastē 8. Cik kastu *vajag* visiem?",
         "atb": ["7"], "padoms": "6 pilnas + 1 ar diviem."},
        {"jaut": "50 cepumi, kastē 8. Cik cepumu paliek ārpus pilnām "
                 "kastēm?", "atb": ["2"], "padoms": "Atlikums."},
        {"jaut": "Lentes 45 m, vienam tērpam 6 m. Cik tērpu var pašūt?",
         "atb": ["7"], "padoms": "45 : 6 = 7 (atl. 3) - pilni tērpi."},
        {"jaut": "27 grāmatas, plauktā 5. Cik plauktu vajag?",
         "atb": ["6"], "padoms": "27 : 5 = 5 (atl. 2)."},
        {"jaut": "Ir 20 €, biļete maksā 3 €. Cik biļešu var nopirkt?",
         "atb": ["6"], "padoms": "20 : 3 = 6 (atl. 2)."},
    ], pamats=4),

    Varianti("Uz augšu, uz leju vai atlikums?", [
        {"jaut": "Cik taksometru vajag 11 cilvēkiem, ja vienā 4 vietas?",
         "opcijas": ["3", "2", "2 (atl. 3)"], "pareizi": 0,
         "padoms": "Visiem jāaizbrauc."},
        {"jaut": "Cik pilnu dēļu pa 3 m var nozāģēt no 14 m?",
         "opcijas": ["4", "5", "2"], "pareizi": 0,
         "padoms": "14 : 3 = 4 (atl. 2)."},
        {"jaut": "Cik metru paliek no 14 m dēļa?",
         "opcijas": ["2", "4", "3"], "pareizi": 0, "padoms": "Atlikums."},
        {"jaut": "Kāds jautājums prasa noapaļot uz augšu?",
         "opcijas": ["Cik mašīnu vajag visiem?",
                     "Cik pilnu kastu sanāk?",
                     "Cik paliek pāri?"], "pareizi": 0,
         "padoms": "Visiem jāietilpst."},
    ], pamats=4),

    Pasaule("Futbola turnīra plānošana",
            Ievadi("", [
                {"jaut": "Turnīram pieteicās 58 spēlētāji; komandā 7. Cik "
                         "pilnu komandu?",
                 "atb": ["8"], "padoms": "58 : 7 = 8 (atl. 2)."},
                {"jaut": "Cik spēlētāju paliek bez komandas?",
                 "atb": ["2"], "padoms": "Atlikums."},
                {"jaut": "Cik vēl spēlētāju vajag, lai būtu 9 pilnas "
                         "komandas?",
                 "atb": ["5"], "padoms": "9 · 7 = 63; 63 − 58."},
                {"jaut": "Mikroautobusā 9 vietas. Cik mikroautobusu vajag "
                         "58 spēlētājiem?",
                 "atb": ["7"], "padoms": "58 : 9 = 6 (atl. 4)."},
            ]),
            pavediens="sports",
            konteksts="Organizatori vienmēr rēķina ar atlikumu - kādam "
                      "vienmēr jāatrod vieta.",
            kapec="Viens rēķins, bet dzīvē trīs dažādas atbildes."),

    Kopsavilkums([
        "Izlasu jautājumu un izlemju, ko darīt ar atlikumu.",
        "Zinu, kad atbildi noapaļo uz augšu un kad uz leju.",
        "Pārbaudu, vai atbilde ir iespējama dzīvē.",
    ]),

    Majas([
        "Izrēķini, cik mašīnu vajag visai ģimenei uz svētkiem (pa 5 vietām).",
        "Izdomā vienu uzdevumu, kurā atbilde ir atlikums.",
        "Izrēķini, cik pilnu nedēļu ir līdz Ziemassvētkiem.",
    ]),
]
