# -*- coding: utf-8 -*-
"""7. klase, 103. stunda: «Kā no leņķiem spriest par malām?»

Apgrieztā sakarība: pret lielāku leņķi atrodas lielāka mala. Zinot leņķus
(vai aprēķinot trešo no summas), var sakārtot malas pēc garuma - bez
mērīšanas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā no leņķiem spriest par malām?"

MERKIS = ("Salīdzināsim trijstūra malas, ja doti tā leņķu lielumi.")

SATURS = [
    Sakums("Leņķi 30°, 60°, 90° - kura mala garākā?",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 6, 3.46)],
                               nogriezni=["AB", "BC", "CA"],
                               taisni=["ABC"],
                               lenki=[("BAC", "30°"), ("ACB", "60°")]),
           paraksts="Pret 90° - garākā mala AC.",
           fakti=["Lielākais leņķis ir 90° pie B.",
                  "Pretī tam - mala AC.",
                  "Īsākā mala BC - pret 30°."]),

    Doma("Pret lielāku leņķi - lielāka mala",
         "Trijstūrī pret lielāku leņķi atrodas lielāka mala. Ja leņķi ir "
         "vienādi, arī malas pret tiem ir vienādas.",
         soli=[
             "Ja dotas tikai divi leņķi, aprēķini trešo.",
             "Sakārto leņķus.",
             "Katram leņķim atrodi pretmalu.",
             "Malas sakārtojas tāpat.",
         ],
         pieze="Tā var pierādīt, ka taisnleņķa trijstūrī hipotenūza ir "
               "garākā mala - pret 90° nav lielāka leņķa."),

    Paraugs("Sakārto malas",
            uzd="△ABC: ∠A = 70°, ∠B = 45°. Sakārto malas augošā secībā.",
            soli=[
                ("∠C = 180° − 70° − 45° = 65°", "(leņķu summa)"),
                ("∠B < ∠C < ∠A", "45° < 65° < 70°."),
                ("Pret ∠B - AC, pret ∠C - AB, pret ∠A - BC", "Pretmalas."),
                ("AC < AB < BC", "Tā pati secība."),
            ],
            atbilde="AC < AB < BC"),

    Varianti("Kura mala garākā?", [
        {"jaut": "△ABC: ∠A = 50°, ∠B = 60°, ∠C = 70°.",
         "opcijas": ["AB", "BC", "AC", "Visas vienādas"],
         "pareizi": 0, "padoms": "Pret ∠C."},
        {"jaut": "△KLM: ∠K = 100°, ∠L = 30°.",
         "opcijas": ["LM", "KL", "KM", "Nevar zināt"],
         "pareizi": 0, "padoms": "Pret ∠K."},
        {"jaut": "△PQR: ∠P = ∠Q = 50°.",
         "opcijas": ["PQ", "QR", "PR", "Visas vienādas"],
         "pareizi": 0, "padoms": "∠R = 80°, pret to PQ."},
        {"jaut": "Visi leņķi 60°. Kura mala garākā?",
         "opcijas": ["Visas vienādas", "AB", "BC", "AC"],
         "pareizi": 0, "padoms": "Vienādmalu."},
    ], pamats=4),

    Ievadi("Spried", [
        {"jaut": "△ABC: ∠A = 40°, ∠B = 40°. Kura mala vienāda ar AC? "
                 "Raksti divus burtus.",
         "atb": ["BC", "CB"], "padoms": "Pret vienādiem leņķiem.",
         "tastatura": "text"},
        {"jaut": "Tajā pašā trijstūrī - cik grādu ir ∠C?",
         "atb": ["100"], "padoms": "180 − 80."},
        {"jaut": "Kura mala ir garākā? Raksti divus burtus.",
         "atb": ["AB", "BA"], "padoms": "Pret ∠C.",
         "tastatura": "text"},
    ]),

    Pasaule("Kurš ceļš garāks?",
            Varianti("", [
                {"jaut": "No torņa T redz divas mājas A un B. ∠TAB = 70°, "
                         "∠TBA = 50°. Kura māja tuvāk tornim?",
                 "opcijas": ["A (TA pret 50°)", "B (TB pret 70°)",
                             "Vienādi", "Nevar zināt"],
                 "pareizi": 0, "padoms": "Pret mazāku leņķi - īsāka mala."},
                {"jaut": "Kāds ir leņķis pie torņa?",
                 "opcijas": ["60°", "120°", "70°", "50°"],
                 "pareizi": 0, "padoms": "180 − 120."},
                {"jaut": "Kurš attālums garākais - TA, TB vai AB?",
                 "opcijas": ["TB", "TA", "AB", "Vienādi"],
                 "pareizi": 0, "padoms": "Pret 70° - TB."},
            ]),
            pavediens="celojums",
            konteksts="Ģeodēzisti no leņķiem nosaka, kurš objekts ir tuvāk, "
                      "vēl pirms attāluma mērīšanas.",
            kapec="Leņķu secība = malu secība."),

    Kopsavilkums([
        "Zinu: pret lielāku leņķi - lielāka mala.",
        "Aprēķinu trešo leņķi un sakārtoju malas.",
        "Zinu, ka pret vienādiem leņķiem - vienādas malas.",
        "Pamatoju, ka hipotenūza ir garākā.",
    ]),

    Majas([
        "△ABC: ∠A = 35°, ∠C = 85°. Sakārto malas.",
        "Uzzīmē un pārbaudi ar lineālu.",
        "Pamato, ka platleņķa trijstūrī garākā mala ir pret plato leņķi.",
    ]),
]
