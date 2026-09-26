# -*- coding: utf-8 -*-
"""7. klase, 156. stunda: «Kas ir skaitļu intervāls?»

Intervāls ir visi skaitļi starp diviem galiem - ar vai bez galapunktiem.
Stunda iemāca četrus pierakstus: nevienādība (2 ≤ x < 5), intervāls
[2; 5), skaitļu taisne un vārdi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Kas ir skaitļu intervāls?"

MERKIS = ("Attēlosim intervālu uz skaitļu taisnes un pierakstīsim to ar "
          "nevienādību.")

SATURS = [
    Sakums("Ķermeņa temperatūra: normāla no 36 līdz 37 °C",
           zimejums=taisne(35, 39, 1, intervali=[(36, 37, True, True)],
                           sikas=2),
           paraksts="36 ≤ t ≤ 37 jeb t ∈ [36; 37].",
           fakti=["Intervāls - visi skaitļi starp diviem galiem.",
                  "Galus var ieskaitīt vai neieskaitīt.",
                  "Arī 36,6 pieder - intervālā ir arī daļskaitļi."]),

    Doma("Četri intervāla veidi",
         "Intervāls ir skaitļu kopa starp a un b. Nogrieznis [a; b]: "
         "a ≤ x ≤ b; intervāls (a; b): a < x < b; pusintervāli [a; b) un "
         "(a; b].",
         soli=[
             "Kvadrātiskā iekava - gals pieder (pilns punkts).",
             "Apaļā iekava - gals nepieder (tukšs punkts).",
             "Mazākais skaitlis vienmēr pa kreisi.",
             "Starp galiem - semikols.",
         ],
         pieze="Latviešu pierakstā starp galiem raksta semikolu: [2; 5), jo "
               "komats ir decimāldaļai."),

    Zimejums("Pieraksti",
             restis([["nevienādība", "intervāls"],
                     ["2 ≤ x ≤ 5", "[2; 5]"],
                     ["2 < x < 5", "(2; 5)"],
                     ["2 ≤ x < 5", "[2; 5)"],
                     ["x > 2", "(2; +∞)"]]),
             paskaidro="Pie bezgalības vienmēr apaļā iekava."),

    Paraugs("Attēlo",
            uzd="Attēlo un pieraksti ar nevienādību: x ∈ (−1; 3].",
            soli=[
                ("−1 < x ≤ 3", "Nevienādība."),
                ("Pie −1 - tukšs punkts, pie 3 - pilns", "Taisne."),
                ("Veseli skaitļi: 0; 1; 2; 3", "Piemēri."),
            ],
            atbilde="−1 < x ≤ 3"),

    Varianti("Kurš intervāls?", [
        {"jaut": "−3 ≤ x < 4",
         "opcijas": ["[−3; 4)", "(−3; 4]", "[−3; 4]", "(−3; 4)"],
         "pareizi": 0, "padoms": "−3 pieder, 4 - nē."},
        {"jaut": "x ≤ 0",
         "opcijas": ["(−∞; 0]", "(−∞; 0)", "[0; +∞)", "(0; +∞)"],
         "pareizi": 0, "padoms": "Līdz 0 ieskaitot."},
        {"jaut": "Vai 5 pieder (2; 5)?",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "Apaļā iekava."},
        {"jaut": "Vai 2,5 pieder [2; 3]?",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Starp 2 un 3."},
    ], pamats=4),

    Ievadi("Skaiti", [
        {"jaut": "Cik veselu skaitļu pieder [−2; 3]?",
         "atb": ["6"], "padoms": "−2; −1; 0; 1; 2; 3."},
        {"jaut": "Cik veselu skaitļu pieder (−2; 3)?",
         "atb": ["4"], "padoms": "−1; 0; 1; 2."},
        {"jaut": "Intervāla [4; 10] garums?",
         "atb": ["6"], "padoms": "10 − 4."},
    ]),

    Pasaule("Ideālā temperatūra",
            Ievadi("", [
                {"jaut": "Ledusskapī jābūt no 2 līdz 6 °C (ieskaitot). "
                         "Cik veselu grādu vērtību ir šajā intervālā?",
                 "atb": ["5"], "padoms": "2; 3; 4; 5; 6."},
                {"jaut": "Vai 6,5 °C ir pieļaujams? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "6,5 > 6."},
                {"jaut": "Intervāla garums (grādi)?",
                 "atb": ["4"], "padoms": "6 − 2."},
            ]),
            pavediens="virtuve",
            konteksts="Pārtikas drošības noteikumos temperatūras ir "
                      "intervāli - [2; 6] ledusskapim.",
            kapec="Intervāls ir «drošā zona»."),

    Kopsavilkums([
        "Pierakstu intervālu ar iekavām un nevienādību.",
        "Attēloju to uz skaitļu taisnes.",
        "Atšķiru apaļās un kvadrātiskās iekavas.",
        "Saskaitu veselos skaitļus intervālā.",
    ]),

    Majas([
        "Atrodi 3 intervālus dzīvē (temperatūra, vecums, cena).",
        "Pieraksti katru 3 veidos.",
        "Uzzīmē (−2; 4] uz skaitļu taisnes.",
    ]),
]
