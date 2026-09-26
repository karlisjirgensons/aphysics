# -*- coding: utf-8 -*-
"""2. klase, 161. stunda: «Kāda darbība jāizpilda vispirms?»

Jauns darbību secības noteikums: reizināšanu un dalīšanu izpilda pirms
saskaitīšanas un atņemšanas. 2 + 3 · 4 = 2 + 12 = 14, nevis 20. Iekavas
joprojām ir pirmās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti)

TEMA = "Kāda darbība jāizpilda vispirms?"

MERKIS = ("Šodien noteiksim darbību secību izteiksmē, kurā ir reizināšana un "
          "saskaitīšana.")

SATURS = [
    Sakums("2 + 3 · 4 = 20 vai 14?",
           fakti=["Reizināšanu izpilda pirms saskaitīšanas.",
                  "3 · 4 = 12, tad 2 + 12 = 14.",
                  "Pareizi ir 14."]),

    Doma("Darbību secība",
         "Iekavas - tad reizināšana un dalīšana - tad saskaitīšana un "
         "atņemšana.",
         soli=[
             "Vai ir iekavas? Rēķini tās.",
             "Vai ir «·» vai «:»? Rēķini tās.",
             "Tad «+» un «−» no kreisās uz labo.",
             "Atzīmē secību virs zīmēm: 1, 2.",
         ]),

    Slidnis("Tie paši skaitļi", [
        {"v": "2 + 3 · 4 = 14", "teksts": "Vispirms 3 · 4 = 12."},
        {"v": "(2 + 3) · 4 = 20", "teksts": "Iekavas - vispirms 5."},
        {"v": "14 un 20", "teksts": "Secība maina rezultātu."},
    ]),

    Varianti("Kura darbība pirmā?", [
        {"jaut": "10 + 4 · 5", "opcijas": ["4 · 5", "10 + 4"],
         "jaukt": False, "pareizi": 0, "padoms": "Reizināšana pirms."},
        {"jaut": "20 − 12 : 3", "opcijas": ["12 : 3", "20 − 12"],
         "jaukt": False, "pareizi": 0, "padoms": "Dalīšana pirms."},
        {"jaut": "(10 + 4) · 2", "opcijas": ["10 + 4", "4 · 2"],
         "jaukt": False, "pareizi": 0, "padoms": "Iekavas pirmās."},
        {"jaut": "3 · 5 + 2", "opcijas": ["3 · 5", "5 + 2"],
         "jaukt": False, "pareizi": 0, "padoms": "Reizināšana pirms."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "10 + 4 · 5 = ?", "atb": ["30"], "padoms": "10 + 20."},
        {"jaut": "20 − 12 : 3 = ?", "atb": ["16"], "padoms": "20 − 4."},
        {"jaut": "(10 + 4) · 2 = ?", "atb": ["28"], "padoms": "14 · 2."},
        {"jaut": "3 · 5 + 2 = ?", "atb": ["17"], "padoms": "15 + 2."},
        {"jaut": "40 − 5 · 5 = ?", "atb": ["15"], "padoms": "40 − 25."},
        {"jaut": "2 · 9 − 18 : 2 = ?", "atb": ["9"], "padoms": "18 − 9."},
    ], pamats=4),

    Pasaule("Pusdienas skolā",
            Ievadi("", [
                {"jaut": "Zupa 2 €, un 3 pankūkas pa 1 €. Cik kopā? "
                         "2 + 3 · 1 = ?", "atb": ["5"], "mers": "€",
                 "padoms": "Vispirms 3 · 1."},
                {"jaut": "Draugs: 4 pīrāgi pa 2 € un sula 1 €. 4 · 2 + 1 = ?",
                 "atb": ["9"], "mers": "€", "padoms": "8 + 1."},
            ]),
            pavediens="skola",
            konteksts="Skolas kafejnīcā pērk vairākas vienādas lietas.",
            kapec="Pareiza secība - pareiza cena."),

    Kopsavilkums([
        "Zinu, ka reizināšana un dalīšana ir pirms saskaitīšanas.",
        "Iekavas vienmēr pirmās.",
        "Aprēķinu izteiksmi pareizā secībā.",
    ]),

    Majas([
        "Aprēķini: 5 + 2 · 3 un (5 + 2) · 3.",
        "Paskaidro mājiniekam, kāpēc rezultāti atšķiras.",
        "Izdomā savu piemēru ar reizināšanu un saskaitīšanu.",
    ]),
]
