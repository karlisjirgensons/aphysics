# -*- coding: utf-8 -*-
"""2. klase, 22. stunda: «Kur ir puse un kur ceturtdaļa?»

Sloksni pārloka uz pusēm - locījums rāda vidu; pārloka vēlreiz - četras
vienādas daļas, katra ir ceturtdaļa. Garumos: 16 cm sloksnes puse ir 8 cm,
ceturtdaļa - 4 cm. Daļskaitļa pierakstu vēl neievieš, lieto vārdus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, vienibas)

TEMA = "Kur ir puse un kur ceturtdaļa?"

MERKIS = ("Šodien ar sloksnīti atzīmēsim nogriežņa pusi un ceturtdaļu, "
          "salokot to.")

SATURS = [
    Sakums("Kā atrast lentes vidu bez lineāla?",
           zimejums=vienibas(2),
           paraksts="Pārloki uz pusēm - locījums ir vidū.",
           fakti=["Puse - viena no divām vienādām daļām.",
                  "Ceturtdaļa - viena no četrām vienādām daļām.",
                  "Divas ceturtdaļas ir puse."]),

    Doma("Locījums atrod vidu",
         "Pārlokot uz pusēm, iegūst 2 vienādas daļas, vēlreiz - 4.",
         soli=[
             "Saliec sloksnes galus kopā un nogludini locījumu.",
             "Atloki - locījums ir sloksnes vidū.",
             "Pārloki vēlreiz uz pusēm - 3 locījumi, 4 daļas.",
             "Katra daļa ir ceturtdaļa.",
         ]),

    Slidnis("Locām 16 cm sloksni", [
        {"v": "16 cm", "teksts": "Vesela sloksne.", "zim": vienibas(1)},
        {"v": "puse - 8 cm", "teksts": "8 + 8 = 16.", "zim": vienibas(2)},
        {"v": "ceturtdaļa - 4 cm", "teksts": "4 + 4 + 4 + 4 = 16.",
         "zim": vienibas(4)},
    ]),

    Ievadi("Puse un ceturtdaļa", [
        {"jaut": "Sloksne ir 20 cm. Cik gara ir tās puse?", "atb": ["10"],
         "mers": "cm", "padoms": "10 + 10 = 20."},
        {"jaut": "Sloksne ir 20 cm. Cik gara ir ceturtdaļa?", "atb": ["5"],
         "mers": "cm", "padoms": "5 + 5 + 5 + 5 = 20."},
        {"jaut": "Sloksne ir 12 cm. Cik gara ir puse?", "atb": ["6"],
         "mers": "cm", "padoms": "6 + 6."},
        {"jaut": "Sloksne ir 12 cm. Cik gara ir ceturtdaļa?", "atb": ["3"],
         "mers": "cm", "padoms": "Pusi pārloki vēlreiz: 6 uz pusēm."},
        {"jaut": "Puse sloksnes ir 9 cm. Cik gara ir visa?", "atb": ["18"],
         "mers": "cm", "padoms": "9 + 9."},
        {"jaut": "Ceturtdaļa ir 2 cm. Cik gara ir visa sloksne?",
         "atb": ["8"], "mers": "cm", "padoms": "2 + 2 + 2 + 2."},
    ], pamats=4),

    Varianti("Vai tā ir puse?", [
        {"jaut": "Sloksni pārlocīja tā, ka viens gals ir garāks. Vai tā ir "
                 "puse?", "opcijas": ["Nē, daļas nav vienādas", "Jā"],
         "jaukt": False, "pareizi": 0, "padoms": "Pusēm jābūt vienādām."},
        {"jaut": "Cik ceturtdaļu ir vienā pusē?",
         "opcijas": ["2", "4", "1"], "pareizi": 0,
         "padoms": "Pusi pārloka vēlreiz uz pusēm."},
    ]),

    Petijums("Loki un mēri", [
        "Nogriez sloksni 16 cm garu.",
        "Pārloki uz pusēm un izmēri vienu daļu.",
        "Pārloki vēlreiz un izmēri vienu daļu.",
        "Pieraksti: puse = ... cm, ceturtdaļa = ... cm.",
    ], vajag="papīra sloksne, lineāls, šķēres"),

    Pasaule("Kā sadalīt kūkas lenti?",
            Ievadi("", [
                {"jaut": "Garā kūka ir 40 cm. To dala 4 draugiem vienādi. "
                         "Cik cm gabals katram?", "atb": ["10"], "mers": "cm",
                 "padoms": "Puse ir 20, ceturtdaļa - 10."},
                {"jaut": "Ja draugu būtu tikai 2?", "atb": ["20"],
                 "mers": "cm", "padoms": "Puse no 40."},
            ]),
            pavediens="virtuve",
            konteksts="Rulete - garā kūka - jāsagriež vienādos gabalos.",
            kapec="Puse un ceturtdaļa - godīga dalīšana."),

    Kopsavilkums([
        "Atrodu sloksnes pusi, pārlokot to.",
        "Atrodu ceturtdaļu, pārlokot vēlreiz.",
        "Aprēķinu puses un ceturtdaļas garumu.",
    ]),

    Majas([
        "Pārloki dvieli uz pusēm un vēlreiz.",
        "Cik daļu sanāca?",
        "Atrodi aukliņas vidu, to nemērot.",
    ]),
]
