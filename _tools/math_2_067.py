# -*- coding: utf-8 -*-
"""2. klase, 67. stunda: «Kā izskatās mana nedēļa?»

Nedēļas plāns ir tabula: dienas un nodarbības ar laikiem. No tā var
aprēķināt, cik laika nedēļā aiziet treniņiem, cik paliek brīvam laikam, un
stāstīt par to ar laika vienībām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā izskatās mana nedēļa?"

MERKIS = ("Šodien veidosim tabulu ar savu nedēļas plānu un stāstīsim par to, "
          "lietojot laika vienības.")

_PLANS = restis([["diena", "nodarbība", "laiks"],
                 ["pirmdiena", "peldēšana", "16:00-17:00"],
                 ["otrdiena", "mūzika", "15:30-16:15"],
                 ["trešdiena", "peldēšana", "16:00-17:00"],
                 ["ceturtdiena", "brīvs", "-"],
                 ["piektdiena", "futbols", "15:00-16:30"]])

SATURS = [
    Sakums("Cik stundu nedēļā tu pavadi treniņos?",
           zimejums=_PLANS,
           paraksts="Katrai dienai sava rinda.",
           fakti=["Plāns palīdz neaizmirst.",
                  "No tabulas var aprēķināt laiku.",
                  "Atpūtai arī vajag laiku!"]),

    Doma("Nedēļas plāns",
         "Katrai dienai - nodarbība ar sākuma un beigu laiku.",
         soli=[
             "Uzraksti dienas rindās.",
             "Katrai ieraksti nodarbību un laiku.",
             "Aprēķini katras nodarbības ilgumu.",
             "Saskaiti visu nedēļu.",
         ]),

    Ievadi("Rēķini pēc plāna", [
        {"jaut": "Cik minūšu ilgst mūzikas nodarbība?", "zim": _PLANS,
         "atb": ["45"], "mers": "min", "padoms": "15:30 līdz 16:15."},
        {"jaut": "Cik minūšu ilgst futbols?", "zim": _PLANS, "atb": ["90"],
         "mers": "min", "padoms": "1 h 30 min."},
        {"jaut": "Cik stundu nedēļā peldēšanā?", "zim": _PLANS,
         "atb": ["2"], "mers": "h", "padoms": "Pirmdiena un trešdiena."},
        {"jaut": "Cik dienu nedēļā ir nodarbības?", "zim": _PLANS,
         "atb": ["4"], "padoms": "Ceturtdiena brīva."},
    ]),

    Varianti("Kas ir patiesība?", [
        {"jaut": "Kura nodarbība ir visilgākā?", "zim": _PLANS,
         "opcijas": ["futbols", "mūzika", "peldēšana"], "pareizi": 0,
         "padoms": "90 min."},
        {"jaut": "Draugs aicina ciemos otrdien 16:00. Vai var?",
         "zim": _PLANS, "opcijas": ["Nē, līdz 16:15 mūzika",
                                    "Jā, otrdiena brīva"],
         "jaukt": False, "pareizi": 0, "padoms": "Paskaties otrdienu."},
    ]),

    Petijums("Mans nedēļas plāns", [
        "Uzzīmē tabulu ar 7 rindām - nedēļas dienām.",
        "Ieraksti savas nodarbības un laikus.",
        "Aprēķini, cik laika nedēļā aizņem nodarbības.",
        "Pastāsti klasesbiedram par savu nedēļu.",
    ], vajag="lapa, lineāls, zīmulis"),

    Pasaule("Kad satikties ar draugu?",
            Varianti("", [
                {"jaut": "Draugam treniņi pirmdien un ceturtdien. Kurā dienā "
                         "abi esat brīvi?", "zim": _PLANS,
                 "opcijas": ["nevienā darbdienā", "ceturtdienā",
                             "pirmdienā"], "pareizi": 0,
                 "padoms": "Tu esi brīvs tikai ceturtdien."},
                {"jaut": "Kurā dienā pēc 17:00 esat brīvi abi, ja draugam "
                         "treniņš beidzas 16:30?",
                 "opcijas": ["jebkurā", "nevienā", "tikai sestdien"],
                 "pareizi": 0, "padoms": "Tavas nodarbības beidzas līdz "
                                         "17:00."},
            ]),
            pavediens="maja",
            konteksts="Divi draugi salīdzina savus plānus.",
            kapec="Plāns ļauj atrast kopīgu brīvu laiku."),

    Kopsavilkums([
        "Veidoju sava nedēļas plāna tabulu.",
        "Aprēķinu nodarbību ilgumu.",
        "Stāstu par savu nedēļu, lietojot laika vienības.",
    ]),

    Majas([
        "Kopā ar ģimeni uzraksti nākamās nedēļas plānu.",
        "Aprēķini, cik stundu ir brīvas.",
        "Izplāno vienu kopīgu pastaigu.",
    ]),
]
