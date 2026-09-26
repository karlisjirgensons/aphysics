# -*- coding: utf-8 -*-
"""7. klase, 102. stunda: «Kurš leņķis ir lielākais?»

Trijstūrī pret garāko malu atrodas lielākais leņķis, pret īsāko - mazākais.
Stunda to atklāj ar mērījumiem un lieto, lai sakārtotu leņķus, nezinot to
lielumus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kurš leņķis ir lielākais?"

MERKIS = ("Formulēsim un lietosim sakarību: pret garāko malu atrodas "
          "lielākais leņķis.")

_T = geometrija([("A", 0, 0), ("B", 8, 0), ("C", 2, 3)],
                nogriezni=["AB", "BC", "CA"],
                malas=[("AB", "8"), ("BC", "6,7"), ("CA", "3,6")],
                lenki=[("BCA", "lielākais")])

SATURS = [
    Sakums("Garākā mala - lielākais leņķis pretī",
           zimejums=_T,
           paraksts="AB ir garākā - pretī tai ∠C ir lielākais.",
           fakti=["Iedomājies šķēres: jo vairāk atver, jo tālāk gali.",
                  "Lielāks leņķis «atgrūž» pretējo malu garāku.",
                  "Pret īsāko malu - mazākais leņķis."]),

    Doma("Pret lielāku malu - lielāks leņķis",
         "Trijstūrī pret lielāku malu atrodas lielāks leņķis. Tāpēc "
         "lielākais leņķis ir pret garāko malu, mazākais - pret īsāko.",
         soli=[
             "Sakārto malas pēc garuma.",
             "Katrai malai atrodi pretleņķi.",
             "Leņķi sakārtojas tādā pašā secībā.",
         ],
         pieze="Vienādsānu trijstūris ir speciāls gadījums: pret vienādām "
               "malām - vienādi leņķi."),

    Paraugs("Sakārto leņķus",
            uzd="Trijstūrī KLM: KL = 5 cm, LM = 9 cm, KM = 7 cm. Sakārto "
                "leņķus augošā secībā.",
            soli=[
                ("KL < KM < LM", "Malas: 5 < 7 < 9."),
                ("Pret KL - ∠M, pret KM - ∠L, pret LM - ∠K",
                 "Pretleņķi."),
                ("∠M < ∠L < ∠K", "Tā pati secība."),
            ],
            atbilde="∠M < ∠L < ∠K"),

    Varianti("Kurš leņķis lielākais?", [
        {"jaut": "△ABC: AB = 4, BC = 7, AC = 5.",
         "opcijas": ["∠A", "∠B", "∠C", "Visi vienādi"],
         "pareizi": 0, "padoms": "Pret BC (7) - ∠A."},
        {"jaut": "△PQR: PQ = 10, QR = 6, PR = 9.",
         "opcijas": ["∠R", "∠P", "∠Q", "Visi vienādi"],
         "pareizi": 0, "padoms": "Pret PQ - ∠R."},
        {"jaut": "△ABC: AB = BC = 5, AC = 8.",
         "opcijas": ["∠B", "∠A", "∠C", "∠A un ∠C"],
         "pareizi": 0, "padoms": "Pret AC - ∠B."},
        {"jaut": "Kurš leņķis mazākais △ABC ar AB = 3, BC = 8, AC = 6?",
         "opcijas": ["∠C", "∠A", "∠B", "Nevar zināt"],
         "pareizi": 0, "padoms": "Pret AB (3) - ∠C."},
    ], pamats=4),

    Ievadi("Spried", [
        {"jaut": "Taisnleņķa trijstūrī - kura mala ir garākā: pretī 90° vai "
                 "pretī šaurajam? Raksti «90» vai «šaurajam».",
         "atb": ["90"], "padoms": "Lielākais leņķis - 90°."},
        {"jaut": "Trijstūrī ∠A = 100°. Pret kuru virsotni ir garākā mala? "
                 "Raksti burtu.",
         "atb": ["A"], "padoms": "Lielākais leņķis.",
         "tastatura": "text"},
        {"jaut": "Malas 6, 6, 6. Cik grādu ir lielākais leņķis?",
         "atb": ["60"], "padoms": "Visi vienādi."},
    ]),

    Pasaule("Kalna slīpums",
            Varianti("", [
                {"jaut": "Trijstūrveida zemes gabala malas: 40 m, 55 m, "
                         "70 m. Kur ir platākais stūris?",
                 "opcijas": ["Pretī 70 m malai", "Pretī 40 m malai",
                             "Pretī 55 m malai", "Visi vienādi"],
                 "pareizi": 0, "padoms": "Pret garāko malu."},
                {"jaut": "Kur ir šaurākais stūris (grūtāk iebraukt ar "
                         "traktoru)?",
                 "opcijas": ["Pretī 40 m malai", "Pretī 70 m malai",
                             "Pretī 55 m malai", "Nav šaura"],
                 "pareizi": 0, "padoms": "Pret īsāko malu."},
            ]),
            pavediens="maja",
            konteksts="Mērnieks no malu garumiem uzreiz zina, kur zemes "
                      "gabalā ir šaurākais stūris.",
            kapec="Malas un leņķi ir saistīti."),

    Kopsavilkums([
        "Zinu: pret garāko malu - lielākais leņķis.",
        "Sakārtoju leņķus pēc malām.",
        "Atrodu katras malas pretleņķi.",
        "Zinu, ka taisnleņķa trijstūrī garākā mala ir pret 90°.",
    ]),

    Majas([
        "Uzzīmē trijstūri ar malām 4, 6, 9 cm un izmēri leņķus.",
        "Pārbaudi, vai lielākais leņķis ir pret garāko malu.",
        "Paskaidro sakarību ar šķērēm.",
    ]),
]
