# -*- coding: utf-8 -*-
"""7. klase, 153. stunda: «Kas ir atrisinājumu kopa?»

Nevienādības atrisinājumu parasti ir bezgalīgi daudz, tāpēc tos nevar
uzskaitīt - tos pieraksta kā kopu: ar nevienādību (x > 3), uz skaitļu
taisnes vai ar intervālu. Atrisināt nevienādību nozīmē atrast visus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kas ir atrisinājumu kopa?"

MERKIS = ("Paskaidrosim, ka atrisināt nevienādību nozīmē atrast visus tās "
          "atrisinājumus.")

SATURS = [
    Sakums("x > 3: cik atrisinājumu?",
           zimejums=taisne(-2, 8, 1, intervali=[(3, None, False, False)]),
           paraksts="3,1; 4; 100; 3,0001 - visi der. 3 neder.",
           fakti=["Atrisinājumu ir bezgalīgi daudz.",
                  "Tos visus apraksta viena nevienādība x > 3.",
                  "Uz taisnes - svītrots stars."]),

    Doma("Atrisinājumu kopa",
         "Atrisināt nevienādību nozīmē atrast visu tās atrisinājumu kopu. "
         "Lineārai nevienādībai tā ir stars uz skaitļu taisnes: x > a, "
         "x ≥ a, x < a vai x ≤ a.",
         soli=[
             "Atrodi robežskaitli.",
             "Nosaki virzienu: lielāki vai mazāki.",
             "Nosaki, vai robeža ietilpst (≤, ≥ - pilns punkts).",
             "Pieraksti: x > 3 jeb x ∈ (3; +∞).",
         ],
         pieze="Iekavas: apaļā «(» - robeža neietilpst, kvadrātiskā «[» - "
               "ietilpst. Pie bezgalības vienmēr apaļā."),

    Paraugs("Trīs pieraksti",
            uzd="Pieraksti visus skaitļus, kas nav lielāki par 2.",
            soli=[
                ("Nevienādība: x ≤ 2", "«Nav lielāki» = mazāki vai vienādi."),
                ("Taisne: pilns punkts pie 2, svītrots pa kreisi", "Attēls."),
                ("Intervāls: x ∈ (−∞; 2]", "Kvadrātiskā iekava pie 2."),
            ],
            atbilde="x ≤ 2; x ∈ (−∞; 2]"),

    Zimejums("x ≤ 2",
             taisne(-4, 6, 1, intervali=[(None, 2, False, True)]),
             paskaidro="Pilns punkts - 2 pieder kopai."),

    Varianti("Kurš pieraksts?", [
        {"jaut": "x ≥ −1",
         "opcijas": ["[−1; +∞)", "(−1; +∞)", "(−∞; −1]", "(−∞; −1)"],
         "pareizi": 0, "padoms": "Ieskaitot −1, uz labo."},
        {"jaut": "x < 5",
         "opcijas": ["(−∞; 5)", "(−∞; 5]", "(5; +∞)", "[5; +∞)"],
         "pareizi": 0, "padoms": "Neieskaitot, uz kreiso."},
        {"jaut": "«Vismaz 18 gadi»",
         "opcijas": ["x ≥ 18", "x > 18", "x ≤ 18", "x < 18"],
         "pareizi": 0, "padoms": "18 der."},
        {"jaut": "«Mazāk nekā 10 €»",
         "opcijas": ["x < 10", "x ≤ 10", "x > 10", "x ≥ 10"],
         "pareizi": 0, "padoms": "10 neder."},
    ], pamats=4),

    Ievadi("Skaiti atrisinājumus", [
        {"jaut": "Cik naturālu skaitļu apmierina x < 6?",
         "atb": ["5"], "padoms": "1; 2; 3; 4; 5."},
        {"jaut": "Cik naturālu skaitļu apmierina x ≤ 6?",
         "atb": ["6"], "padoms": "Arī 6."},
        {"jaut": "Mazākais vesels skaitlis, kas apmierina x > −2,5?",
         "atb": ["−2", "-2"], "padoms": "−2 > −2,5."},
    ]),

    Pasaule("Filmas vecuma ierobežojums",
            Ievadi("", [
                {"jaut": "Filma «12+». Vai 12 gadus vecs var skatīties? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "x ≥ 12."},
                {"jaut": "Cik veselu gadu vecumu no 5 līdz 18 (ieskaitot) "
                         "atļauj «12+»?",
                 "atb": ["7"], "padoms": "12; 13; ...; 18."},
                {"jaut": "Ja «vecāki par 12», vai 12 gadnieks var? (jā/nē)",
                 "atb": ["nē", "ne"], "padoms": "x > 12."},
            ]),
            pavediens="skola",
            konteksts="Vecuma ierobežojumi ir nevienādības - un svarīgi, vai "
                      "robeža ieskaitīta.",
            kapec="≥ un > atšķiras tieši robežā."),

    Kopsavilkums([
        "Zinu, ka atrisinājumu kopa bieži ir bezgalīga.",
        "Pierakstu kopu ar nevienādību un intervālu.",
        "Attēloju to uz skaitļu taisnes.",
        "Lietoju apaļās un kvadrātiskās iekavas.",
    ]),

    Majas([
        "Pieraksti 3 veidos: «ne mazāk kā −3».",
        "Atrodi ierobežojumus sabiedriskajā transportā un pieraksti.",
        "Uzzīmē x < 0 un x ≥ 0 uz vienas taisnes.",
    ]),
]
