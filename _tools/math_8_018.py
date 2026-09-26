# -*- coding: utf-8 -*-
"""8. klase, 18. stunda: «Kā reizina pakāpes ar vienādām bāzēm?»

Īpašību neiemācās no galvas - to atklāj, izrakstot reizinātājus: 2^3 · 2^4
ir septiņi divnieki pēc kārtas. Slīdnis to parāda, un formula a^m · a^n =
a^{m + n} ir tikai pieraksts tam, kas jau redzēts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā reizina pakāpes ar vienādām bāzēm?"

MERKIS = ("Atklāsim un lietosim pakāpju reizināšanas īpašību.")

SATURS = [
    Sakums("Cik ir 2³ · 2⁴?",
           zimejums=restis([["2", "2", "2", "2", "2", "2", "2"]]),
           paraksts="Trīs divnieki un vēl četri - kopā septiņi.",
           fakti=["2³ · 2⁴ = 2⁷ = 128.",
                  "Kāpinātājus saskaita.",
                  "Bāze paliek tā pati."]),

    Slidnis("Izraksti reizinātājus", [
        {"v": "a^2 · a^3", "teksts": "(a · a) · (a · a · a)"},
        {"v": "a · a · a · a · a", "teksts": "Pieci reizinātāji"},
        {"v": "a^5", "teksts": "2 + 3 = 5"},
        {"v": "a^m · a^n = a^{m + n}", "teksts": "Tas pats jebkuriem m un n"},
    ], ievads="Iekavas reizināšanā var noņemt - reizinātāji paliek."),

    Doma("Reizināšanas īpašība",
         "Reizinot pakāpes ar vienādām bāzēm, bāzi atstāj to pašu, bet "
         "kāpinātājus saskaita: a^m · a^n = a^{m + n}.",
         soli=[
             "Pārbaudi, vai bāzes ir vienādas.",
             "Bāzi pārraksti.",
             "Kāpinātājus saskaiti.",
             "a = a^1 - kāpinātājs 1 nav rakstīts, bet ir.",
         ],
         pieze="Ar dažādām bāzēm tā nedrīkst: 2^3 · 3^2 = 8 · 9 = 72, un to "
               "nevar pierakstīt kā vienu pakāpi ar bāzi 2 vai 3."),

    Paraugs("Vienkāršo",
            uzd="Vienkāršo x^8 · x^2, a · a^5 · a^3 un 3^4 · 3.",
            soli=[
                ("x^8 · x^2 = x^{10}", "8 + 2."),
                ("a · a^5 · a^3 = a^9", "1 + 5 + 3."),
                ("3^4 · 3 = 3^5 = 243", "4 + 1."),
            ],
            atbilde="x^{10}; a^9; 3^5"),

    Ievadi("Pieraksti kā vienu pakāpi", [
        {"jaut": "x^8 · x^2", "atb": ["x^10", "x^{10}"],
         "padoms": "8 + 2.", "tastatura": "text"},
        {"jaut": "a^4 · a", "atb": ["a^5"], "padoms": "a = a^1.",
         "tastatura": "text"},
        {"jaut": "5^3 · 5^7", "atb": ["5^10", "5^{10}"],
         "padoms": "3 + 7.", "tastatura": "text"},
        {"jaut": "y^2 · y^3 · y^4", "atb": ["y^9"], "padoms": "2 + 3 + 4.",
         "tastatura": "text"},
        {"jaut": "2^5 · 2^? = 2^{12}. Kāds kāpinātājs trūkst?",
         "atb": ["7"], "padoms": "12 − 5."},
        {"jaut": "2 · 2^3 · 2^2 - aprēķini vērtību",
         "atb": ["64"], "padoms": "2^6."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "a^3 · a^4 = a^{12}",
         "opcijas": ["Kļūda: jābūt a^7", "Pareizi", "Kļūda: jābūt 2a^7",
                     "Kļūda: jābūt a^1"],
         "pareizi": 0, "padoms": "Saskaita, nereizina."},
        {"jaut": "2^3 · 2^2 = 4^5",
         "opcijas": ["Kļūda: jābūt 2^5", "Pareizi", "Kļūda: jābūt 4^6",
                     "Kļūda: jābūt 2^6"],
         "pareizi": 0, "padoms": "Bāze nemainās."},
        {"jaut": "x^2 · y^3 = (xy)^5",
         "opcijas": ["Kļūda: bāzes dažādas, vienkāršot nevar", "Pareizi",
                     "Kļūda: jābūt xy^5", "Kļūda: jābūt (xy)^6"],
         "pareizi": 0, "padoms": "Īpašība der tikai vienādām bāzēm."},
    ]),

    Pasaule("Baktērijas dalās",
            Ievadi("", [
                {"jaut": "Baktēriju skaits divkāršojas ik 20 minūtes. Cik "
                         "reižu tas pieaug 1 stundā (2^3)?",
                 "atb": ["8"], "padoms": "3 dalīšanās."},
                {"jaut": "Un vēl 2 stundās (2^6)? Cik reižu pavisam 3 "
                         "stundās? Pieraksti kā 2^?",
                 "atb": ["2^9", "512"], "padoms": "2^3 · 2^6.",
                 "tastatura": "text"},
                {"jaut": "Cik tas ir skaitlī?",
                 "atb": ["512"], "padoms": "2^9 = 512."},
            ]),
            pavediens="daba",
            konteksts="Tāpēc piens ledusskapī stāv dienām, bet siltumā "
                      "saskābst pāris stundās - baktērijas dalās ātrāk.",
            kapec="Laiku intervāli saskaitās, kāpinātāji arī."),

    Kopsavilkums([
        "Pamatoju a^m · a^n = a^{m + n}, izrakstot reizinātājus.",
        "Reizinu pakāpes ar vienādām bāzēm.",
        "Neaizmirstu, ka a = a^1.",
        "Zinu, ka ar dažādām bāzēm īpašība neder.",
    ]),

    Majas([
        "Pieraksti kā vienu pakāpi: 7^2 · 7^5, b · b^9, 10^3 · 10^4.",
        "Aprēķini 10^3 · 10^4 un pārbaudi ar nullu skaitu.",
        "Izdomā vienu kļūdu, ko varētu izdarīt, un paskaidro to.",
    ]),
]
