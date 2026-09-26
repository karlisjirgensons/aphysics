# -*- coding: utf-8 -*-
"""7. klase, 157. stunda: «Kā atrisināt nevienādību ekvivalenti pārveidojot?»

Lineāru nevienādību risina tāpat kā vienādojumu - pārnes, savelk, dala -
ar vienu atšķirību: dalot ar negatīvu skaitli, zīme mainās. Atbildi
pieraksta kā intervālu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā atrisināt nevienādību ekvivalenti pārveidojot?"

MERKIS = ("Atrisināsim lineāru nevienādību un pierakstīsim atrisinājumu "
          "kopu.")

SATURS = [
    Sakums("Kā vienādojums - ar vienu brīdinājumu",
           fakti=["3x − 5 < 7: 3x < 12, x < 4.",
                  "5 − 2x ≥ 1: −2x ≥ −4, x ≤ 2 (zīme mainījās!).",
                  "Atbilde - intervāls, nevis viens skaitlis."]),

    Doma("Soļi kā vienādojumam",
         "Lineāru nevienādību risina ar ekvivalentām pārveidošanām: atver "
         "iekavas, pārnes saskaitāmos (mainot zīmi saskaitāmajam), savelk un "
         "dala ar koeficientu. Dalot ar negatīvu koeficientu, nevienādības "
         "zīmi maina.",
         soli=[
             "Atver iekavas, atbrīvojies no daļām.",
             "x saskaitāmos pa kreisi, skaitļus pa labi.",
             "Savelc: ax < b.",
             "Dali ar a; ja a < 0 - maini zīmi.",
             "Pieraksti intervālu un pārbaudi ar vienu skaitli.",
         ]),

    Paraugs("Ar zīmes maiņu",
            uzd="Atrisini 2(x − 1) ≥ 5x + 4.",
            soli=[
                ("2x − 2 ≥ 5x + 4", "Atver iekavas."),
                ("2x − 5x ≥ 4 + 2", "Pārnes."),
                ("−3x ≥ 6", "Savelk."),
                ("x ≤ −2", "(: (−3), zīme mainās)"),
                ("Pārbaude x = −3: −8 ≥ −11 ✓", "Der."),
            ],
            atbilde="x ∈ (−∞; −2]"),

    Zimejums("x ≤ −2",
             taisne(-6, 3, 1, intervali=[(None, -2, False, True)]),
             paskaidro="Pilns punkts pie −2."),

    Ievadi("Atrisini - ieraksti robežu", [
        {"jaut": "4x + 3 > 19. x > ?",
         "atb": ["4"], "padoms": "4x > 16."},
        {"jaut": "7 − x ≤ 2. x ≥ ?",
         "atb": ["5"], "padoms": "−x ≤ −5."},
        {"jaut": "3(x + 2) < x. x < ?",
         "atb": ["−3", "-3"], "padoms": "2x < −6."},
        {"jaut": "{x|2} − 1 ≥ 3. x ≥ ?",
         "atb": ["8"], "padoms": "{x|2} ≥ 4."},
        {"jaut": "5 − 3x > 2x − 15. x < ?",
         "atb": ["4"], "padoms": "−5x > −20."},
        {"jaut": "0,2x + 1 ≤ 0,5x − 2. x ≥ ?",
         "atb": ["10"], "padoms": "−0,3x ≤ −3."},
    ], pamats=4),

    Varianti("Pareizā atbilde", [
        {"jaut": "−4x < 8",
         "opcijas": ["x > −2", "x < −2", "x > 2", "x < 2"],
         "pareizi": 0, "padoms": "Mainās."},
        {"jaut": "2x − 1 ≥ 2x + 3",
         "opcijas": ["Atrisinājumu nav", "Visi x", "x ≥ 2", "x ≤ 2"],
         "pareizi": 0, "padoms": "−1 ≥ 3 - aplams."},
        {"jaut": "x + 5 > x",
         "opcijas": ["Visi x", "Atrisinājumu nav", "x > 0", "x > 5"],
         "pareizi": 0, "padoms": "5 > 0 - vienmēr."},
    ]),

    Pasaule("Ietaupījuma mērķis",
            Ievadi("", [
                {"jaut": "Kontā 40 €, krāj 15 € nedēļā. Vajag vismaz 190 € "
                         "velosipēdam. Pēc cik nedēļām? (40 + 15n ≥ 190)",
                 "atb": ["10"], "padoms": "15n ≥ 150."},
                {"jaut": "Ja krātu 12 € nedēļā - cik pilnu nedēļu?",
                 "atb": ["13"], "padoms": "12n ≥ 150, n ≥ 12,5."},
                {"jaut": "Cik € jākrāj nedēļā, lai sasniegtu mērķi 6 nedēļās?",
                 "atb": ["25"], "padoms": "6x ≥ 150."},
            ]),
            pavediens="veikals",
            konteksts="Krāšanas plānā «vismaz» ir nevienādība - un "
                      "atbildi noapaļo uz augšu.",
            kapec="Nevienādība dod minimālo laiku."),

    Kopsavilkums([
        "Risinu nevienādību kā vienādojumu.",
        "Mainu zīmi, dalot ar negatīvu.",
        "Pierakstu atbildi kā intervālu.",
        "Pārbaudu ar skaitli no intervāla.",
    ]),

    Majas([
        "Atrisini: 3 − 2(x + 1) < 7; {x − 1|3} ≥ 2.",
        "Aprēķini, pēc cik nedēļām sasniegsi savu krāšanas mērķi.",
        "Pārbaudi atbildes ar skaitļiem.",
    ]),
]
