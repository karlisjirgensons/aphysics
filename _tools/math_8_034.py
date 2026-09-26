# -*- coding: utf-8 -*-
"""8. klase, 34. stunda: «Kā no normālformas iegūt parasto pierakstu?»

Pretējais virziens: kāpinātājs pasaka, par cik vietām un uz kuru pusi
pārvietot komatu. Trūkstošās vietas aizpilda ar nullēm. Kalkulatora ekrāns
(3.2E-5) ir tā pati normālforma citā pierakstā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā no normālformas iegūt parasto pierakstu?"

MERKIS = ("Pārveidosim normālformā pierakstītu skaitli parastajā "
          "pierakstā.")

SATURS = [
    Sakums("Ko rāda kalkulators?",
           zimejums=restis([["ekrānā", "nozīmē", "skaitlis"],
                            ["4.5E6", "4,5 · 10⁶", "4 500 000"],
                            ["3.2E-5", "3,2 · 10⁻⁵", "0,000032"]]),
           paraksts="E nozīmē «reizināt ar 10 pakāpē».",
           fakti=["Pozitīvs kāpinātājs - komats pa labi.",
                  "Negatīvs - komats pa kreisi.",
                  "Tukšās vietas aizpilda ar nullēm."]),

    Doma("Atpakaļ uz parasto pierakstu",
         "Kāpinātājs n pasaka, par cik vietām pārvietot komatu skaitlī a.",
         soli=[
             "n > 0: komatu pārvieto n vietas pa labi.",
             "n < 0: komatu pārvieto |n| vietas pa kreisi.",
             "Trūkstošos ciparus aizpilda ar nullēm.",
             "Pārbaude: lielam skaitlim ir n + 1 cipars pirms komata.",
         ]),

    Paraugs("Pārveido",
            uzd="Pieraksti parastajā pierakstā 2,07 · 10^5 un 8,1 · 10^−3.",
            soli=[
                ("2,07 → 207 000", "5 vietas pa labi: 2 cipari + 3 nulles."),
                ("8,1 → 0,0081", "3 vietas pa kreisi."),
            ],
            atbilde="207 000; 0,0081"),

    Ievadi("Pieraksti parasti", [
        {"jaut": "3 · 10^4", "atb": ["30000", "30 000"],
         "padoms": "4 nulles."},
        {"jaut": "5,6 · 10^3", "atb": ["5600", "5 600"],
         "padoms": "3 vietas."},
        {"jaut": "7 · 10^−2", "atb": ["0,07", "0.07"],
         "padoms": "2 vietas pa kreisi."},
        {"jaut": "1,25 · 10^−4", "atb": ["0,000125", "0.000125"],
         "padoms": "4 vietas pa kreisi."},
        {"jaut": "9,99 · 10^0", "atb": ["9,99", "9.99"],
         "padoms": "10^0 = 1."},
        {"jaut": "6.02E23 - cik ciparu ir šim skaitlim pirms komata?",
         "atb": ["24"], "padoms": "n + 1."},
    ], pamats=4),

    Varianti("Salīdzini", [
        {"jaut": "Kurš skaitlis ir lielāks: 3 · 10^−2 vai 5 · 10^−3?",
         "opcijas": ["3 · 10^−2 = 0,03", "5 · 10^−3 = 0,005", "Vienādi",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "Lielāks kāpinātājs."},
        {"jaut": "Sakārto augošā secībā: 2 · 10^3, 9 · 10^2, 1 · 10^4.",
         "opcijas": ["9 · 10^2; 2 · 10^3; 1 · 10^4",
                     "1 · 10^4; 2 · 10^3; 9 · 10^2",
                     "2 · 10^3; 9 · 10^2; 1 · 10^4",
                     "9 · 10^2; 1 · 10^4; 2 · 10^3"],
         "pareizi": 0, "padoms": "900; 2000; 10 000."},
    ]),

    Pasaule("Vīrusi un šūnas",
            Ievadi("", [
                {"jaut": "Gripas vīrusa diametrs ir 1 · 10^−7 m. Cik mm? "
                         "(1 m = 1000 mm)",
                 "atb": ["0,0001", "0.0001"], "padoms": "10^−7 · 10^3."},
                {"jaut": "Sarkanais asinsķermenītis ir 7 · 10^−6 m. Cik reižu "
                         "lielāks par vīrusu?",
                 "atb": ["70"], "padoms": "{7 · 10^−6|10^−7}."},
                {"jaut": "Cilvēka ķermenī ir apmēram 3 · 10^{13} šūnu. Cik "
                         "triljonu? (triljons = 10^{12})",
                 "atb": ["30"], "padoms": "3 · 10."},
            ]),
            pavediens="daba",
            konteksts="Mikrobioloģijā un medicīnā skaitļi ir gan niecīgi "
                      "(izmēri), gan milzīgi (šūnu skaits).",
            kapec="Normālforma ļauj salīdzināt tos vienā rindā."),

    Kopsavilkums([
        "Pārveidoju normālformu parastajā pierakstā.",
        "Lasu kalkulatora E pierakstu.",
        "Salīdzinu skaitļus normālformā.",
    ]),

    Majas([
        "Pieraksti parasti: 4,3 · 10^6, 2 · 10^−5, 7,77 · 10^1.",
        "Uz kalkulatora izrēķini 2^{50} un pieraksti rezultātu normālformā.",
        "Sakārto: 3,1 · 10^5, 9 · 10^4, 3 · 10^5.",
    ]),
]
