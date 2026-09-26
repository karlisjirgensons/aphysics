# -*- coding: utf-8 -*-
"""8. klase, 114. stunda: «Kā polinomu pieraksta normālformā?»

Normālformā polinomam savilkti līdzīgie locekļi un locekļi sakārtoti
dilstošās pakāpēs. Polinoma pakāpe ir lielākā locekļa pakāpe.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā polinomu pieraksta normālformā?"

MERKIS = "Pārveidosim polinomu normālformā un noteiksim tā pakāpi."

_T = "text"

SATURS = [
    Sakums("Kā to saīsināt?",
           zimejums=restis([["3x² + 5x − x² + 2 − 7x"],
                            ["2x² − 2x + 2"]]),
           paraksts="Līdzīgie locekļi savilkti, pakāpes dilst.",
           fakti=["Normālformā savelk līdzīgos locekļus.",
                  "Locekļus sakārto dilstošās pakāpēs.",
                  "Polinoma pakāpe - lielākā locekļa pakāpe."]),

    Doma("Normālforma",
         "Līdzīgi locekļi - ar vienādu burtu daļu; tos savelk kā vienu.",
         soli=[
             "Katru locekli pieraksti normālformā.",
             "Atrodi līdzīgos locekļus un saskaiti to koeficientus.",
             "Sakārto: vispirms augstākā pakāpe, beigās brīvais loceklis.",
             "Nosaki pakāpi pēc lielākā locekļa.",
         ]),

    Paraugs("Savelc",
            uzd="Pārveido normālformā 3x^2 + 5x − x^2 + 2 − 7x.",
            soli=[
                ("3x^2 − x^2 = 2x^2", "Kvadrāti."),
                ("5x − 7x = −2x", "Pirmās pakāpes."),
                ("2x^2 − 2x + 2", "Brīvais loceklis beigās."),
                ("Pakāpe 2", "Lielākā pakāpe."),
            ],
            atbilde="2x^2 − 2x + 2, pakāpe 2"),

    Ievadi("Normālformā", [
        {"jaut": "3a + 5 − a + 2", "atb": ["2a + 7"], "tastatura": _T,
         "padoms": "3a − a; 5 + 2."},
        {"jaut": "x^2 + 3x − x^2 + x", "atb": ["4x"], "tastatura": _T,
         "padoms": "Kvadrāti saīsinās."},
        {"jaut": "5x^3 − 2x + x^4: pakāpe?", "atb": ["4"],
         "padoms": "x^4."},
        {"jaut": "2ab − 3ab + ab", "atb": ["0"], "padoms": "2 − 3 + 1."},
        {"jaut": "x^2y + xy − 3: pakāpe?", "atb": ["3"],
         "padoms": "x^2y: 2 + 1."},
        {"jaut": "a^2 + 2a − 3 + a^2 − 2a", "atb": ["2a^2 − 3"],
         "tastatura": _T, "padoms": "2a − 2a = 0."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "Kuri locekļi ir līdzīgi?",
         "opcijas": ["4x^2y un −x^2y", "4x^2y un 4xy^2", "x^2 un x",
                     "3a un 3b"],
         "pareizi": 0, "padoms": "Tā pati burtu daļa."},
        {"jaut": "Polinoma 7 − 2x + x^3 normālforma:",
         "opcijas": ["x^3 − 2x + 7", "7 − 2x + x^3", "x^3 + 2x + 7",
                     "−2x + x^3 + 7"],
         "pareizi": 0, "padoms": "Dilstošās pakāpēs."},
        {"jaut": "Polinoma 3x^2 − 5x^4 + 1 pakāpe:",
         "opcijas": ["4", "2", "6", "3"],
         "pareizi": 0, "padoms": "Lielākā."},
    ]),

    Pasaule("Trijstūra perimetrs",
            Ievadi("", [
                {"jaut": "Trijstūra malas: 2x + 1, 3x − 2 un x + 4. "
                         "Perimetrs = ?x + 3",
                 "atb": ["6"], "padoms": "2x + 3x + x."},
                {"jaut": "x = 5. Perimetrs?", "atb": ["33"],
                 "padoms": "6 · 5 + 3."},
                {"jaut": "Perimetra polinoma pakāpe?", "atb": ["1"],
                 "padoms": "Tikai x."},
            ]),
            pavediens="maja",
            konteksts="Kad malas atkarīgas no x, perimetru vienkāršo vienreiz "
                      "un tad ievieto jebkuru x.",
            kapec="Normālforma - īsākais pieraksts rēķināšanai."),

    Kopsavilkums([
        "Savelku līdzīgos locekļus.",
        "Sakārtoju polinomu dilstošās pakāpēs.",
        "Nosaku polinoma pakāpi.",
    ]),

    Majas([
        "Pārveido normālformā: 4a − 3 + a^2 − 2a + 5.",
        "Uzraksti četrstūra perimetru, ja malas ir x, x + 1, 2x, 2x − 3.",
        "Izdomā polinomu, kas pēc savilkšanas kļūst par 0.",
    ]),
]
