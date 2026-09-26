# -*- coding: utf-8 -*-
"""9. klase, 161. stunda: «Kas ir regulārs daudzstūris?»

Regulāram daudzstūrim visas malas un visi leņķi vienādi. Leņķu summa
(n − 2) · 180°, tāpēc viens leņķis (n − 2) · 180° : n; ārējais leņķis
360° : n. Rombs un taisnstūris nav regulāri - vienādas ir tikai malas vai
tikai leņķi. Stāsts: bišu šūnas un futbola bumba.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija, regulars)

TEMA = "Kas ir regulārs daudzstūris?"

MERKIS = ("Definēsim regulāru daudzstūri un aprēķināsim tā leņķa lielumu.")


def _lenkis(n):
    return (n - 2) * 180 // n


def _zim(n):
    punkti, malas = regulars(n)
    return geometrija(punkti, nogriezni=malas,
                      lenki=[("ABC", "%d°" % _lenkis(n))])


SATURS = [
    Sakums("Bišu šūnas - kāpēc sešstūri?",
           zimejums=_zim(6),
           paraksts="Regulārs sešstūris: 6 vienādas malas, katrs leņķis 120°.",
           fakti=["Regulāram daudzstūrim vienādas visas malas un leņķi.",
                  "Leņķis = (n − 2) · 180° : n.",
                  "Trīs sešstūri pie virsotnes: 3 · 120° = 360°."]),

    Slidnis("Leņķis aug līdz ar n", [
        {"v": "n = 3", "teksts": "Vienādmalu trijstūris: 60°", "zim": _zim(3)},
        {"v": "n = 4", "teksts": "Kvadrāts: 90°", "zim": _zim(4)},
        {"v": "n = 5", "teksts": "3 · 180° : 5 = 108°", "zim": _zim(5)},
        {"v": "n = 6", "teksts": "4 · 180° : 6 = 120°", "zim": _zim(6)},
        {"v": "n = 8", "teksts": "6 · 180° : 8 = 135°", "zim": _zim(8)},
    ]),

    Doma("Regulārs daudzstūris",
         "Daudzstūri sauc par regulāru, ja visas tā malas ir vienādas un "
         "visi leņķi ir vienādi.",
         soli=[
             "No vienas virsotnes diagonāles dala to n − 2 trijstūros.",
             "Leņķu summa: (n − 2) · 180°.",
             "Viens leņķis: (n − 2) · 180° : n.",
             "Ārējais leņķis: 360° : n.",
         ],
         pieze="Rombam vienādas malas, taisnstūrim - leņķi, bet regulārs "
               "ir tikai kvadrāts."),

    Paraugs("Cik malu?",
            uzd="Regulāra daudzstūra leņķis ir 140°. Cik tam malu?",
            soli=[
                ("180° − 140° = 40°", "Ārējais leņķis."),
                ("n = 360° : 40° = 9", "Ārējo leņķu summa 360°."),
            ],
            atbilde="9 malas"),

    Ievadi("Aprēķini", [
        {"jaut": "Regulāra desmitstūra leņķis (°)?", "atb": ["144"],
         "padoms": "8 · 180 : 10."},
        {"jaut": "Regulāra divpadsmitstūra leņķu summa (°)?",
         "atb": ["1800"], "padoms": "10 · 180."},
        {"jaut": "Leņķis 150°. Cik malu?", "atb": ["12"],
         "padoms": "360 : 30."},
        {"jaut": "Ārējais leņķis 72°. Cik malu?", "atb": ["5"],
         "padoms": "360 : 72."},
    ]),

    Varianti("Regulārs?", [
        {"jaut": "Kvadrāts", "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "Malas un leņķi vienādi."},
        {"jaut": "Rombs ar leņķi 70°", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 1, "padoms": "Leņķi nav vienādi."},
        {"jaut": "Taisnstūris 2 × 3", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 1, "padoms": "Malas nav vienādas."},
        {"jaut": "Vienādmalu trijstūris", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Vienādas malas dod vienādus leņķus."},
    ]),

    Pasaule("Futbola bumba",
            Ievadi("", [
                {"jaut": "Bumbā pie katras virsotnes satiekas piecstūris un "
                         "divi sešstūri. Leņķu summa (°)?", "atb": ["348"],
                 "padoms": "108 + 120 + 120."},
                {"jaut": "Cik grādu «pietrūkst» līdz 360°?", "atb": ["12"],
                 "padoms": "360 − 348."},
            ]),
            pavediens="sports",
            konteksts="Klasiskā futbola bumba sašūta no 12 regulāriem "
                      "piecstūriem un 20 sešstūriem.",
            kapec="Tieši šie trūkstošie grādi liek virsmai izliekties - "
                  "plakne kļūst par lodi."),

    Kopsavilkums([
        "Definēju regulāru daudzstūri.",
        "Aprēķinu leņķi: (n − 2) · 180° : n.",
        "No leņķa atrodu malu skaitu.",
    ]),

    Majas([
        "Ceļa zīme STOP ir regulārs astoņstūris. Aprēķini tās leņķi.",
        "Vai var būt regulārs daudzstūris ar leņķi 100°? Pamato.",
        "Atrodi mājās vai uz ielas trīs regulārus daudzstūrus.",
    ]),
]
