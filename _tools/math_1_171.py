# -*- coding: utf-8 -*-
"""1. klase, 171. stunda: «Kā risinu uzdevumu ar zīmējumu?»

Sadzīves uzdevumu vispirms uzzīmē (sloksnes vai mājiņa), tad pieraksta
darbību, aprēķina un paskaidro risinājumu klasesbiedram.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, majina, sloksnes)

TEMA = "Kā risinu uzdevumu ar zīmējumu?"

MERKIS = ("Šodien risināsim sadzīves uzdevumu, vispirms to uzzīmējot, un "
          "izskaidrosim risinājumu.")

SATURS = [
    Sakums("Annai 9 uzlīmes, Ievai par 5 vairāk. Cik Ievai?",
           zimejums=sloksnes([("Anna", 9), ("Ieva", 14, "?")]),
           paraksts="Ievas josla - tikpat un vēl 5.",
           fakti=["1. Uzzīmē.",
                  "2. Pieraksti darbību.",
                  "3. Aprēķini un atbildi."]),

    Paraugs("No zīmējuma uz atbildi",
            uzd="Annai 9 uzlīmes, Ievai par 5 vairāk. Cik uzlīmju Ievai?",
            soli=[
                ("Zīmējums: Ievas josla garāka par 5", "Par vairāk - garāka."),
                ("9 + 5", "Darbība."),
                ("9 + 5 = 14", "9 + 1 + 4."),
            ],
            atbilde="Ievai ir 14 uzlīmes."),

    Doma("Trīs soļi",
         "Zīmējums palīdz izvēlēties darbību.",
         soli=[
             "Uzzīmē: sloksnes salīdzināšanai, mājiņu - kopā/daļa.",
             "Pieraksti darbību ar «?».",
             "Aprēķini un atbildi teikumā.",
         ]),

    Ievadi("Atrisini", [
        {"jaut": "Kopā 16 bumbas, 9 sarkanas. Cik zilas?",
         "zim": majina(16, [(9, None)]), "atb": ["7"], "padoms": "16 − 9."},
        {"jaut": "Tomam 12 kastaņi, Jurim par 4 mazāk. Cik Jurim?",
         "zim": sloksnes([("Toms", 12), ("Juris", 8, "?")]), "atb": ["8"],
         "padoms": "12 − 4."},
        {"jaut": "Dažiem bērniem pievienojās 6, tagad 15. Cik bija?",
         "zim": majina(15, [(None, 6)]), "atb": ["9"], "padoms": "15 − 6."},
    ]),

    Petijums("Paskaidro klasesbiedram", [
        "Atrisini uzdevumu ar zīmējumu.",
        "Parādi zīmējumu pārim.",
        "Paskaidro trīs soļus.",
        "Pāris saka, vai saprata.",
    ], vajag="burtnīca, krāsu zīmuļi"),

    Pasaule("Zemenes",
            Ievadi("", [
                {"jaut": "Vecmāmiņa salasīja 18 zemeņu, tu - par 6 mazāk. "
                         "Cik salasīji tu?",
                 "zim": sloksnes([("vecmāmiņa", 18), ("tu", 12, "?")]),
                 "atb": ["12"], "padoms": "18 − 6."},
            ]),
            pavediens="daba",
            konteksts="Vasarā lasām zemenes.",
            kapec="Zīmējums parāda, ka tev ir mazāk."),

    Kopsavilkums([
        "Uzzīmēju uzdevumu.",
        "Izvēlos darbību pēc zīmējuma.",
        "Paskaidroju risinājumu.",
    ]),

    Majas([
        "Izdomā uzdevumu un uzzīmē to.",
        "Palūdz mājiniekam atrisināt pēc zīmējuma.",
        "Pārbaudi.",
    ]),
]
