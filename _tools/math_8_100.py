# -*- coding: utf-8 -*-
"""8. klase, 100. stunda: «Kā aprēķina paralelograma laukumu?»

Bloka noslēgums: nogriež trijstūri AHD un pārliek pie BC - sanāk
taisnstūris ar to pašu pamatu un augstumu, tāpēc S = a · h. Slīpā mala nav
augstums. Slīdnis parāda pārlikšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā aprēķina paralelograma laukumu?"

MERKIS = "Iegūsim un lietosim paralelograma laukuma formulu."


def _zim(solis):
    punkti = [("A", 0, 0), ("B", 6, 0), ("C", 8, 3), ("D", 2, 3),
              ("H", 2, 0, 270)]
    nogr = ["AB", "BC", "CD", "DA", "DH"]
    krasa = [("HBCD", 0), ("AHD", 1)]
    if solis >= 3:
        punkti = [("H", 2, 0, 270), ("B", 6, 0), ("E", 8, 0, 270),
                  ("C", 8, 3), ("D", 2, 3)]
        nogr = ["HE", "EC", "CD", "DH", "BC"]
        krasa = [("HBCD", 0), ("BEC", 1)]
    return geometrija(punkti, nogriezni=nogr, iekrasot=krasa,
                      taisni=["DHB"], malas=[("CD", "a")],
                      uzraksti=[(2.4, 1.5, "h")])


SATURS = [
    Sakums("Kā paralelogramu pārvērst taisnstūrī?",
           zimejums=_zim(1),
           paraksts="Trijstūri AHD pārliek pie malas BC.",
           fakti=["S = a · h - mala reiz tai novilktais augstums.",
                  "Pārliekot trijstūri, laukums nemainās.",
                  "Slīpā mala nav augstums."]),

    Slidnis("Pārliec trijstūri", [
        {"v": "Paralelograms", "teksts": "Augstums DH nogriež trijstūri",
         "zim": _zim(1)},
        {"v": "Nogriež AHD", "teksts": "Tas ir vienāds ar BEC",
         "zim": _zim(2)},
        {"v": "Taisnstūris a × h", "teksts": "S = a · h",
         "zim": _zim(3)},
    ]),

    Doma("Paralelograma laukums",
         "Paralelograms un taisnstūris ar vienādu pamatu un augstumu ir "
         "vienlieli.",
         soli=[
             "Novelc augstumu pret malu a.",
             "Reizini malu ar augstumu: S = a · h.",
             "Var ņemt jebkuru malu - tad ar tai novilkto augstumu.",
             "Diagonāle sadala paralelogramu divos vienādos trijstūros.",
         ]),

    Paraugs("Otrs augstums",
            uzd="Paralelograma malas 10 cm un 5 cm; augstums pret 10 cm malu "
                "ir 4 cm. Atrodi laukumu un augstumu pret 5 cm malu.",
            soli=[
                ("S = 10 · 4 = 40 cm²", "Mala un tās augstums."),
                ("5 · h = 40", "Tas pats laukums ar otru malu."),
                ("h = 8 cm", "Atrisina."),
            ],
            atbilde="40 cm² un 8 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "a = 12 cm, h = 5 cm. S (cm²)?", "atb": ["60"],
         "padoms": "12 · 5."},
        {"jaut": "a = 7 m, h = 3,5 m. S (m²)?", "atb": ["24,5"],
         "padoms": "7 · 3,5."},
        {"jaut": "S = 48 cm², a = 8 cm. h (cm)?", "atb": ["6"],
         "padoms": "48 : 8."},
        {"jaut": "Rūtiņās: pamats 6 rūtiņas, augstums 4 rūtiņas. S?",
         "atb": ["24"], "padoms": "6 · 4."},
        {"jaut": "Paralelograms S = 30. Diagonāle to sadala divos "
                 "trijstūros. Viena laukums?", "atb": ["15"],
         "padoms": "Uz pusēm."},
    ]),

    Varianti("Spried", [
        {"jaut": "Kāpēc S = a · h, nevis a · b?",
         "opcijas": ["Slīpā mala nav augstums", "Tā ir vieglāk",
                     "a · b ir perimetrs", "Abas formulas vienādas"],
         "pareizi": 0, "padoms": "Taisnstūrim augstums ir h."},
        {"jaut": "Taisnstūrim un paralelogramam vienāds pamats un augstums. "
                 "Laukumi...",
         "opcijas": ["vienādi", "taisnstūrim lielāks",
                     "paralelogramam lielāks", "nevar salīdzināt"],
         "pareizi": 0, "padoms": "Skaties slīdni."},
        {"jaut": "Paralelograms un trijstūris ar vienādu pamatu un augstumu. "
                 "Paralelograma laukums ir...",
         "opcijas": ["divreiz lielāks", "vienāds", "puse", "četrreiz lielāks"],
         "pareizi": 0, "padoms": "Trijstūrim {a · h|2}."},
    ]),

    Pasaule("Slīpā stāvvieta",
            Ievadi("", [
                {"jaut": "Slīpa stāvvieta ir paralelograms: gar ceļu 3 m, "
                         "dziļums (⊥ ceļam) 5 m. Laukums (m²)?",
                 "atb": ["15"], "padoms": "3 · 5."},
                {"jaut": "Cik m² asfalta 20 vietām?", "atb": ["300"],
                 "padoms": "20 · 15."},
                {"jaut": "Taisna vieta ir 2,5 m × 5 m. Par cik m² tā ir "
                         "mazāka?",
                 "atb": ["2,5"], "padoms": "15 − 12,5."},
            ]),
            pavediens="celojums",
            konteksts="Slīpās stāvvietās iebraukt vieglāk; laukumu rēķina ar "
                      "dziļumu, ne slīpo malu.",
            kapec="S = a · h."),

    Kopsavilkums([
        "Pamatoju formulu S = a · h, pārliekot trijstūri.",
        "Aprēķinu laukumu ar jebkuru malu un tās augstumu.",
        "No laukuma atrodu augstumu.",
    ]),

    Majas([
        "Izgriez paralelogramu, nogriez trijstūri un saliec taisnstūri.",
        "Aprēķini paralelograma laukumu divos veidos ar divām malām.",
        "Atrodi paralelograma formas virsmu un aprēķini laukumu.",
    ]),
]
