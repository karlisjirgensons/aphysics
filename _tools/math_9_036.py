# -*- coding: utf-8 -*-
"""9. klase, 36. stunda: «Kā aprēķināt virsmas laukumu?»

Izklājums parāda formulu: četri sānu taisnstūri rindā veido vienu lielu
taisnstūri ar garumu = pamata perimetrs, un pie tā piestiprinātas divas
trapeces. S = 2S_pamata + P_pamata · H.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kā aprēķināt virsmas laukumu?"

MERKIS = ("Aprēķināsim prizmas virsmas laukumu, izmantojot pamata laukumu "
          "un izklājumu.")

# Pamats - vienādsānu trapece 10, 5, 4, 5 (augstums 4); prizmas augstums 6.
_A, _B, _S, _H, _Hp = 10.0, 4.0, 5.0, 4.0, 6.0


def _izklajums():
    xs = [0, _A, _A + _S, _A + _S + _B, _A + 2 * _S + _B]
    punkti = [("_a%d" % i, x, 0) for i, x in enumerate(xs)]
    punkti += [("_b%d" % i, x, _Hp) for i, x in enumerate(xs)]
    nob = (_A - _B) / 2.0
    punkti += [("_t1", nob + _B, _Hp + _H), ("_t2", nob, _Hp + _H),
               ("_u1", nob + _B, -_H), ("_u2", nob, -_H)]
    nogr = [("_a0", "_a4"), ("_b0", "_b4")]
    nogr += [("_a%d" % i, "_b%d" % i) for i in range(5)]
    nogr += [("_b0", "_t2"), ("_t2", "_t1"), ("_t1", "_b1"),
             ("_a0", "_u2"), ("_u2", "_u1"), ("_u1", "_a1")]
    return geometrija(
        punkti, nogriezni=nogr,
        iekrasot=[(("_a0", "_a4", "_b4", "_b0"), 0),
                  (("_b0", "_b1", "_t1", "_t2"), 1),
                  (("_a0", "_a1", "_u1", "_u2"), 1)],
        uzraksti=[(_A / 2, _Hp / 2, "10"), (_A + _S / 2, _Hp / 2, "5"),
                  (_A + _S + _B / 2, _Hp / 2, "4"),
                  (_A + 1.5 * _S + _B, _Hp / 2, "5"),
                  (_A / 2, _Hp + _H / 2, "pamats"),
                  (_A / 2, -_H / 2, "pamats")])


SATURS = [
    Sakums("Cik kartona vajag kastei?",
           zimejums=_izklajums(),
           paraksts="Sānu skaldnes rindā - viens taisnstūris 24 × H.",
           fakti=["Sānu virsma = pamata perimetrs · augstums.",
                  "Pilnā virsma = sānu virsma + 2 pamati.",
                  "Pamata laukums - trapeces formula."]),

    Doma("Prizmas virsmas laukums",
         "S_{sānu} = P_{pam} · H, S_{pilna} = S_{sānu} + 2 · S_{pam}.",
         soli=[
             "Pamata perimetrs: a + b + c + d.",
             "Sānu virsma: perimetrs reiz prizmas augstums H.",
             "Pamata laukums: {a + b|2} · h (h - trapeces augstums!).",
             "Saskaiti: sānu virsma + divi pamati.",
         ],
         pieze="Neapjauc divus augstumus: h - trapecei, H - prizmai."),

    Paraugs("Pilna virsma",
            uzd="Prizmas pamats - vienādsānu trapece ar pamatiem 10 cm un "
                "4 cm, sānu malu 5 cm; prizmas augstums 12 cm. Atrodi pilnās "
                "virsmas laukumu.",
            soli=[
                ("h = √(5^2 − 3^2) = 4", "Trapeces augstums (AH = 3)."),
                ("S_{pam} = {10 + 4|2} · 4 = 28", "Pamata laukums."),
                ("S_{sānu} = (10 + 4 + 5 + 5) · 12 = 288", "Sānu virsma."),
                ("S = 288 + 2 · 28 = 344", "Pilnā virsma."),
            ],
            atbilde="344 cm²"),

    Ievadi("Aprēķini", [
        {"jaut": "Pamata perimetrs 20, H = 7. S_{sānu} = ?", "atb": ["140"],
         "padoms": "20 · 7."},
        {"jaut": "S_{sānu} = 150, S_{pam} = 12. S_{pilna} = ?",
         "atb": ["174"], "padoms": "150 + 24."},
        {"jaut": "Pamats: trapece 6, 4, h = 3. S_{pam} = ?", "atb": ["15"],
         "padoms": "5 · 3."},
        {"jaut": "Pamats: trapece 8, 2, sānu malas 5 un 5; H = 10. "
                 "S_{sānu} = ?", "atb": ["200"], "padoms": "20 · 10."},
        {"jaut": "Tās pašas prizmas pilnā virsma?", "atb": ["240"],
         "padoms": "h = 4, S_{pam} = 20."},
    ], pamats=3),

    Varianti("Kas nepieder formulai?", [
        {"jaut": "Sānu virsmu aprēķina ar...",
         "opcijas": ["pamata perimetru un H", "pamata laukumu un H",
                     "trapeces augstumu h", "diagonālēm"],
         "pareizi": 0, "padoms": "Taisnstūri rindā."},
        {"jaut": "Cik pamatu skaita pilnajā virsmā?",
         "opcijas": ["2", "1", "4", "0"],
         "pareizi": 0, "padoms": "Augša un apakša."},
    ]),

    Pasaule("Siles krāsošana",
            Ievadi("", [
                {"jaut": "Siles gals - trapece: augšā 70 cm, apakšā 40 cm, "
                         "dziļums 20 cm. Viena gala laukums (cm²)?",
                 "atb": ["1100"], "padoms": "55 · 20."},
                {"jaut": "Slīpā siena: katete 15 cm (puse no 70 − 40) un "
                         "20 cm. Sienas platums (cm)?", "atb": ["25"],
                 "padoms": "√(225 + 400)."},
                {"jaut": "Sile 2 m gara, bez vāka. Iekšējā virsma ar galiem: "
                         "(40 + 25 + 25) · 200 + 2 · 1100 = ? cm²",
                 "atb": ["20200", "20 200"], "padoms": "18 000 + 2200."},
            ]),
            pavediens="maja",
            konteksts="Koka sile ir trapeces prizma bez augšējās skaldnes.",
            kapec="Krāsai vajag virsmas laukumu, nevis tilpumu."),

    Kopsavilkums([
        "Zīmēju prizmas izklājumu.",
        "Aprēķinu sānu virsmu un pilno virsmu.",
        "Atšķiru trapeces augstumu no prizmas augstuma.",
    ]),

    Majas([
        "Uzzīmē izklājumu prizmai ar pamatu 8, 4, 3, 3 (cm) un H = 5 cm.",
        "Aprēķini tās sānu virsmu.",
        "Izmēri kādu kasti mājās un aprēķini, cik papīra vajag tās "
        "iesaiņošanai.",
    ]),
]
