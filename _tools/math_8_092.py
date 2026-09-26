# -*- coding: utf-8 -*-
"""8. klase, 92. stunda: «Kas ir izliekts un ieliekts četrstūris?»

Izliektā četrstūrī visi leņķi ir mazāki par 180° un abas diagonāles ir
iekšpusē; ieliektā viens leņķis ir lielāks par 180° un viena diagonāle ir
ārpusē. Leņķu summa abiem ir 360°.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija)

TEMA = "Kas ir izliekts un ieliekts četrstūris?"

MERKIS = ("Nošķirsim izliektus un ieliektus četrstūrus un raksturosim to "
          "diagonāles.")

_IELIEKTS = geometrija([("A", 0, 0), ("B", 3, 1.5, 270), ("C", 6, 0),
                        ("D", 3, 5)],
                       nogriezni=["AB", "BC", "CD", "DA", "BD"],
                       izcelti=["AC"], iekrasot=[("ABCD", 0)])
_IZLIEKTS = geometrija([("A", 0, 0), ("B", 6, 0), ("C", 7, 4),
                        ("D", 1, 3)],
                       nogriezni=["AB", "BC", "CD", "DA", "AC", "BD"],
                       iekrasot=[("ABCD", 0)])

SATURS = [
    Sakums("Kur palika diagonāle AC?",
           zimejums=_IELIEKTS,
           paraksts="Ieliekts četrstūris: ∠B > 180°, diagonāle AC ir ārpusē.",
           fakti=["Izliektā četrstūrī visi leņķi ir mazāki par 180°.",
                  "Ieliektā viens leņķis ir lielāks par 180°.",
                  "Izliektā abas diagonāles ir iekšpusē."]),

    Slidnis("Divi veidi", [
        {"v": "Izliekts", "teksts": "Abas diagonāles iekšpusē",
         "zim": _IZLIEKTS},
        {"v": "Ieliekts", "teksts": "Diagonāle AC ārpusē, ∠B > 180°",
         "zim": _IELIEKTS},
    ]),

    Doma("Kā atšķirt",
         "Pārbaudi diagonāles: ja kāda iziet ārā, četrstūris ir ieliekts.",
         soli=[
             "Novelc abas diagonāles.",
             "Abas iekšpusē - izliekts četrstūris.",
             "Viena ārpusē - ieliekts četrstūris.",
             "Leņķu summa abiem ir 360°.",
         ],
         pieze="Ieliektā četrstūrī diagonāle, kas ir iekšpusē, to sadala "
               "divos trijstūros - tāpēc summa arī tur ir 360°."),

    Varianti("Spried", [
        {"jaut": "Ieliektam četrstūrim trīs leņķi ir 30°, 40° un 50°. "
                 "Ceturtais?",
         "opcijas": ["240°", "120°", "60°", "Tāds nevar būt"],
         "pareizi": 0, "padoms": "360 − 120."},
        {"jaut": "Kurā četrstūrī abas diagonāles ir iekšpusē?",
         "opcijas": ["Izliektā", "Ieliektā", "Nevienā", "Abos"],
         "pareizi": 0, "padoms": "Skaties slīdni."},
        {"jaut": "Vai četrstūrim var būt divi leņķi, lielāki par 180°?",
         "opcijas": ["Nē - summa pārsniegtu 360°", "Jā",
                     "Tikai ieliektam", "Tikai trapecei"],
         "pareizi": 0, "padoms": "Jau divi dotu vairāk par 360°."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Ieliekts četrstūris: 25°, 35°, 40°. Ceturtais?",
         "atb": ["260"], "padoms": "360 − 100."},
        {"jaut": "Cik diagonāļu ir četrstūrim?", "atb": ["2"],
         "padoms": "AC un BD."},
        {"jaut": "Izliekts četrstūris ar leņķiem 3x, 3x, 2x, 2x. x?",
         "atb": ["36"], "padoms": "10x = 360."},
    ]),

    Pasaule("Pūķis un bumerangs",
            Ievadi("", [
                {"jaut": "Pūķis ir izliekts četrstūris ar leņķiem 60°, 110° un "
                         "80°. Ceturtais?",
                 "atb": ["110"], "padoms": "360 − 250."},
                {"jaut": "Bumerangs ir ieliekts četrstūris ar leņķiem 30°, 30° "
                         "un 60°. Lielākais leņķis?",
                 "atb": ["240"], "padoms": "360 − 120."},
                {"jaut": "Vai pūķa šķērskociņi (diagonāles) ir iekšpusē? "
                         "(1 - jā, 0 - nē)",
                 "atb": ["1"], "padoms": "Izliekts."},
            ]),
            pavediens="sports",
            konteksts="Pūķa šķērskociņi ir diagonāles - tos var ielikt tikai "
                      "izliektā četrstūrī.",
            kapec="Izliektā četrstūrī abas diagonāles ir iekšpusē."),

    Kopsavilkums([
        "Nošķiru izliektu un ieliektu četrstūri.",
        "Raksturoju diagonāles abos veidos.",
        "Lietoju leņķu summu 360° arī ieliektam četrstūrim.",
    ]),

    Majas([
        "Uzzīmē ieliektu četrstūri un izmēri tā leņķus.",
        "Atrodi burtu vai zīmi, kas ir ieliekts četrstūris.",
        "Paskaidro, kāpēc ieliektam četrstūrim nevar būt divi leņķi > 180°.",
    ]),
]
