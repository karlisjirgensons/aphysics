# -*- coding: utf-8 -*-
"""7. klase, 24. stunda: «Kā pieraksta ar simboliem?»

Ģeometrijā īsu pierakstu lieto tāpat kā algebrā: A ∈ a, AB ∥ CD, a ⊥ b,
∠ABC, AB = 5 cm. Stunda iemāca lasīt un rakstīt šos simbolus un pārtulkot
teikumus zīmējumā un otrādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija,
                         restis)

TEMA = "Kā pieraksta ar simboliem?"

MERKIS = ("Iemācīsimies pierakstīt punktu, taišņu, staru un nogriežņu "
          "novietojumu ar simboliem.")

SATURS = [
    Sakums("Īsziņa matemātiķim",
           zimejums=restis([["A ∈ a", "punkts A pieder taisnei a"],
                            ["a ∥ b", "taisnes a un b ir paralēlas"],
                            ["a ⊥ b", "a ir perpendikulāra b"],
                            ["∠ABC", "leņķis ar virsotni B"]]),
           fakti=["Simbols ir īsāks par teikumu un nav divdomīgs.",
                  "Visā pasaulē šos simbolus lasa vienādi."]),

    Doma("Katram novietojumam - savs simbols",
         "Punktus apzīmē ar lielajiem burtiem, taisnes - ar mazajiem vai ar "
         "diviem punktiem. Novietojumu pieraksta ar simboliem ∈, ∉, ∥, ⊥, ∩.",
         soli=[
             "Punkts uz taisnes: A ∈ a; ārpus: B ∉ a.",
             "Paralēlas taisnes: a ∥ b; perpendikulāras: a ⊥ b.",
             "Krustpunkts: a ∩ b = {O} jeb a un b krustojas punktā O.",
             "Nogriežņa garums: AB = 5 cm; leņķis: ∠ABC = 40°.",
         ],
         pieze="Leņķa pierakstā ∠ABC virsotne vienmēr ir vidējais burts."),

    Paraugs("No teikuma uz simboliem",
            uzd="Pieraksti ar simboliem: «Taisnes a un b krustojas punktā "
                "O. Punkts M pieder taisnei a, bet nepieder taisnei b. "
                "Taisne c ir perpendikulāra taisnei a.»",
            soli=[
                ("a ∩ b = {O}", "Krustpunkts."),
                ("M ∈ a, M ∉ b", "Pieder un nepieder."),
                ("c ⊥ a", "Perpendikularitāte."),
            ],
            atbilde="a ∩ b = {O}; M ∈ a; M ∉ b; c ⊥ a"),

    Zimejums("Nolasi zīmējumu",
             geometrija([("A", 0, 0), ("B", 8, 0), ("C", 8, 4),
                         ("D", 0, 4)],
                        nogriezni=["AB", "BC", "CD", "DA"],
                        taisni=["DAB", "ABC"],
                        malas=[("AB", "8 cm"), ("BC", "4 cm")]),
             paskaidro="AB ∥ CD, AB ⊥ BC, AB = 8 cm, ∠ABC = 90°."),

    Varianti("Nolasi pierakstu", [
        {"jaut": "Ko nozīmē KL ⊥ MN?",
         "opcijas": ["Taisnes KL un MN ir perpendikulāras",
                     "KL un MN ir paralēlas", "KL = MN",
                     "K pieder MN"],
         "pareizi": 0,
         "padoms": "⊥ - taisns leņķis."},
        {"jaut": "Kura ir leņķa ∠PQR virsotne?",
         "opcijas": ["Q", "P", "R", "PR"],
         "pareizi": 0,
         "padoms": "Vidējais burts."},
        {"jaut": "Kā pierakstīt «punkts T nepieder taisnei m»?",
         "opcijas": ["T ∉ m", "T ∈ m", "m ∉ T", "T ⊥ m"],
         "pareizi": 0,
         "padoms": "Punkts pirmais."},
        {"jaut": "Taisnstūrī ABCD kurš apgalvojums ir aplams?",
         "opcijas": ["AB ∥ BC", "AB ∥ CD", "AB ⊥ AD", "BC ∥ AD"],
         "pareizi": 0,
         "padoms": "Blakus malas ir perpendikulāras."},
    ], pamats=4),

    Ievadi("Taisnstūris ABCD", [
        {"jaut": "Taisnstūrī ABCD AB = 8 cm. Cik cm ir CD?",
         "atb": ["8"], "padoms": "Pretējās malas vienādas."},
        {"jaut": "Cik grādu ir ∠BCD?",
         "atb": ["90"], "padoms": "Taisnstūra leņķis."},
        {"jaut": "Cik malu pāru ir paralēli (AB ∥ CD tipa)?",
         "atb": ["2"], "padoms": "AB ∥ CD un BC ∥ AD."},
        {"jaut": "Cik perpendikulāru malu pāru ir taisnstūrī?",
         "atb": ["4"], "padoms": "Katrā virsotnē viens pāris."},
    ]),

    Pasaule("Ielu karte",
            Varianti("", [
                {"jaut": "Brīvības iela ∥ Valdemāra iela. Ko tas nozīmē?",
                 "opcijas": ["Ielas nekrustojas", "Ielas krustojas taisnā "
                             "leņķī", "Tās ir viena iela",
                             "Tās krustojas vienā punktā"],
                 "pareizi": 0,
                 "padoms": "Paralēlas - kopīgu punktu nav."},
                {"jaut": "Elizabetes iela ⊥ Brīvības iela, un Brīvības "
                         "iela ∥ Valdemāra iela. Kā novietota Elizabetes "
                         "iela pret Valdemāra ielu?",
                 "opcijas": ["Arī perpendikulāri", "Paralēli",
                             "Nevar zināt", "Tās sakrīt"],
                 "pareizi": 0,
                 "padoms": "Perpendikuls vienai paralēlai ir "
                           "perpendikuls arī otrai."},
                {"jaut": "Veikals V atrodas uz Brīvības ielas b. Kā to "
                         "pierakstīt?",
                 "opcijas": ["V ∈ b", "V ∉ b", "b ∈ V", "V ∥ b"],
                 "pareizi": 0,
                 "padoms": "Punkts pieder taisnei."},
            ]),
            pavediens="celojums",
            konteksts="Ielu karte ir taisnes un punkti - un to novietojumu "
                      "var pierakstīt vienā rindā.",
            kapec="Simboli ir kartes valoda bez vārdiem."),

    Kopsavilkums([
        "Lietoju simbolus ∈, ∉, ∥, ⊥, ∩, ∠.",
        "Pārtulkoju teikumu simbolos un otrādi.",
        "Zinu, ka leņķa virsotni raksta vidū.",
        "Nolasu novietojumu no zīmējuma.",
    ]),

    Majas([
        "Uzzīmē savas istabas plānu un pieraksti 5 apgalvojumus ar "
        "simboliem.",
        "Pārtulko simbolus teikumos: AB ∥ CD, AC ⊥ BD, O ∈ AC.",
        "Atrodi pilsētas kartē divas paralēlas un divas perpendikulāras "
        "ielas.",
    ]),
]
