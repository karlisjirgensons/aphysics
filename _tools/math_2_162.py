# -*- coding: utf-8 -*-
"""2. klase, 162. stunda: «Kā pierakstīt divu darbību risinājumu?»

Situācijas uzdevumam veido divu darbību izteiksmi ar reizināšanu vai
dalīšanu un aprēķina tās vērtību: 3 grāmatas pa 4 € un pildspalva 2 € -
3 · 4 + 2 = 14 €.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pierakstīt divu darbību risinājumu?"

MERKIS = ("Šodien veidosim divu darbību izteiksmi situāciju uzdevumam un "
          "aprēķināsim tās vērtību.")

SATURS = [
    Sakums("3 grāmatas pa 4 € un pildspalva par 2 €. Kā to uzrakstīt vienā "
           "izteiksmē?",
           fakti=["Grāmatas: 3 · 4.",
                  "Pildspalva: + 2.",
                  "3 · 4 + 2 = 12 + 2 = 14 €."]),

    Doma("Izteiksme uzdevumam",
         "Katrai situācijas daļai atrodi darbību un saliec izteiksmē.",
         soli=[
             "Atrodi vienādas lietas - tās reizini.",
             "Atrodi, kas vēl nāk klāt vai tiek atņemts.",
             "Saliec izteiksmi.",
             "Aprēķini pareizā secībā.",
         ]),

    Paraugs("Konfektes klasei",
            uzd="Bija 30 konfektes. 4 bērni apēda pa 5. Cik palika?",
            soli=[("30 − 4 · 5", "Izteiksme."),
                  ("= 30 − 20 = 10", "Vispirms reizināšana.")],
            atbilde="10 konfektes"),

    Varianti("Kura izteiksme?", [
        {"jaut": "5 kastes pa 4 zīmuļiem un vēl 3 zīmuļi.",
         "opcijas": ["5 · 4 + 3", "5 + 4 · 3", "(5 + 4) · 3"],
         "pareizi": 0, "padoms": "5 kastes pa 4."},
        {"jaut": "40 € sadala 5 bērniem, katrs iztērē 3 €. Cik katram "
                 "paliek?", "opcijas": ["40 : 5 − 3", "40 − 5 · 3",
                                        "40 : (5 − 3)"],
         "pareizi": 0, "padoms": "Vispirms katra daļa."},
    ]),

    Ievadi("Uzraksti un aprēķini", [
        {"jaut": "5 kastes pa 4 zīmuļiem un vēl 3 zīmuļi. Cik zīmuļu?",
         "atb": ["23"], "padoms": "5 · 4 + 3."},
        {"jaut": "40 € sadala 5 bērniem, katrs iztērē 3 €. Cik katram "
                 "paliek?", "atb": ["5"], "mers": "€",
         "padoms": "40 : 5 − 3 = 8 − 3."},
        {"jaut": "Autobusā 6 rindas pa 4 vietām, aizņemtas 15. Cik brīvas?",
         "atb": ["9"], "padoms": "6 · 4 − 15."},
        {"jaut": "2 iepakojumi pa 10 olām un vēl 6 olas. Cik olu?",
         "atb": ["26"], "padoms": "2 · 10 + 6."},
        {"jaut": "Bija 50 €, nopirka 3 grāmatas pa 5 €. Cik palika?",
         "atb": ["35"], "mers": "€", "padoms": "50 − 3 · 5."},
        {"jaut": "24 ābolus sadala 4 grozos, katrā pieliek vēl 2. Cik "
                 "katrā?", "atb": ["8"], "padoms": "24 : 4 + 2."},
    ], pamats=4),

    Pasaule("Klases ekskursija",
            Ievadi("", [
                {"jaut": "Biļete 3 €, brauc 9 bērni un skolotāja par 5 €. "
                         "Cik maksā visas biļetes? 9 · 3 + 5 = ?",
                 "atb": ["32"], "mers": "€", "padoms": "27 + 5."},
            ]),
            pavediens="celojums",
            konteksts="Klase brauc uz muzeju.",
            kapec="Viena izteiksme apraksta visu aprēķinu."),

    Kopsavilkums([
        "Veidoju divu darbību izteiksmi uzdevumam.",
        "Izmantoju reizināšanu vienādām lietām.",
        "Aprēķinu pareizā secībā.",
    ]),

    Majas([
        "Izdomā uzdevumu par iepirkšanos ar vienādām precēm.",
        "Uzraksti izteiksmi un aprēķini.",
        "Lai mājinieks pārbauda.",
    ]),
]
