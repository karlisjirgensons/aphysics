# -*- coding: utf-8 -*-
"""7. klase, 95. stunda: «Kā aprēķināt nezināmo leņķi?»

Ar paralēlu taišņu īpašībām un krustleņķiem, blakusleņķiem var aprēķināt
leņķus sarežģītākos zīmējumos. Stunda trenē ķēdi: katrā solī - viens
leņķis un viena īpašība.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija,
                         paralelas)

TEMA = "Kā aprēķināt nezināmo leņķi?"

MERKIS = ("Aprēķināsim leņķu lielumus, lietojot paralēlu taišņu leņķu "
          "īpašības.")

SATURS = [
    Sakums("Viens leņķis - un visi pārējie",
           zimejums=paralelas(uzraksti={2: "x", 8: "55°"}, radit=(2, 8),
                              slipums=125),
           paraksts="a ∥ b. ∠8 = 55°. Cik ir x?",
           fakti=["∠8 un ∠2 ir tālu viens no otra.",
                  "Bet ķēde palīdz: ∠8 → ∠6 → ∠2.",
                  "Katrā solī - viena īpašība."]),

    Doma("Ķēde no zināmā līdz meklētajam",
         "Nezināmo leņķi aprēķina ar ķēdi: no zināmā leņķa uz blakus esošu, "
         "katrā solī lietojot vienu īpašību - krustleņķi, blakusleņķi, "
         "kāpšļu, šķērsleņķi vai vienpusleņķi.",
         soli=[
             "Atzīmē zināmo leņķi zīmējumā.",
             "Atrodi leņķi, kas ar to saistīts ar kādu īpašību.",
             "Turpini, līdz nonāc pie meklētā.",
             "Katru soli pieraksti ar pamatojumu.",
         ],
         pieze="Bieži ir vairāki ceļi - izvēlies īsāko."),

    Paraugs("Ķēde",
            uzd="a ∥ b, ∠8 = 55°. Atrodi ∠2.",
            soli=[
                ("∠6 = ∠8 = 55°", "(krustleņķi)"),
                ("∠2 = ∠6 = 55°", "(kāpšļu leņķi, a ∥ b)"),
            ],
            atbilde="∠2 = 55°"),

    Zimejums("Leņķis starp paralēlām",
             geometrija([("_a1", 0, 0), ("_a2", 8, 0), ("_b1", 0, 4),
                         ("_b2", 8, 4), ("A", 1.5, 4, 90), ("B", 1.5, 0, -90),
                         ("M", 5, 2, 0)],
                        taisnes=[("_a1", "_a2"), ("_b1", "_b2")],
                        nogriezni=["AM", "BM"],
                        lenki=[(("_b2", "A", "M"), ""),
                               (("M", "B", "_a2"), "", 2),
                               (("A", "M", "B"), "?")],
                        uzraksti=[(8.5, 4.3, "b"), (8.5, 0.3, "a")]),
             ievads="Paraugs grūtākam uzdevumam: a ∥ b, lauzta līnija AMB.",
             paskaidro="∠AMB = ∠A + ∠B: caur M novelk paralēlu taisni un "
                       "lieto šķērsleņķus divreiz."),

    Ievadi("Aprēķini (a ∥ b)", [
        {"jaut": "∠1 = 72°. Cik grādu ir ∠7?",
         "atb": ["72"], "padoms": "∠1 = ∠5 = ∠7."},
        {"jaut": "∠3 = 48°. Cik grādu ir ∠8?",
         "atb": ["132"], "padoms": "∠3 = ∠5, ∠8 = 180 − ∠5."},
        {"jaut": "∠4 un ∠5 attiecas kā 2 : 3. Cik grādu ir ∠5?",
         "atb": ["108"], "padoms": "5 daļas = 180°."},
        {"jaut": "∠6 par 40° lielāks nekā ∠3. Cik grādu ir ∠3?",
         "atb": ["70"], "padoms": "∠3 + ∠6 = 180; (180 − 40) : 2."},
        {"jaut": "Lauztā līnija starp paralēlām: ∠A = 30°, ∠B = 45°. "
                 "Cik grādu ir ∠AMB?",
         "atb": ["75"], "padoms": "30 + 45."},
        {"jaut": "∠2 = 3 · ∠1. Cik grādu ir ∠1?",
         "atb": ["45"], "padoms": "Blakusleņķi: 4 daļas = 180°."},
    ], pamats=4),

    Varianti("Pārbaudi ceļu", [
        {"jaut": "Kurš ceļš der no ∠1 uz ∠8?",
         "opcijas": ["∠1 = ∠5 (kāpšļu), ∠8 = 180° − ∠5 (blakus)",
                     "∠1 = ∠8 (krustleņķi)",
                     "∠1 + ∠8 = 90°", "Nav ceļa"],
         "pareizi": 0, "padoms": "Divi soļi."},
        {"jaut": "Ja a nav paralēla b, vai ∠1 = ∠5?",
         "opcijas": ["Nevar apgalvot", "Jā", "Vienmēr 180°", "Jā, ja c ⊥ a"],
         "pareizi": 0, "padoms": "Nav paralēlas - nav īpašības."},
    ]),

    Pasaule("Kāpnes starp stāviem",
            Ievadi("", [
                {"jaut": "Griesti un grīda ir paralēli. Kāpnes veido ar grīdu "
                         "37°. Kādu leņķi tās veido ar griestiem (iekšpusē, "
                         "vienā pusē) (°)?",
                 "atb": ["143"], "padoms": "Vienpusleņķi."},
                {"jaut": "Kāds ir šķērsleņķis pie griestiem (°)?",
                 "atb": ["37"], "padoms": "Šķērsleņķi vienādi."},
                {"jaut": "Ja kāpnes būtu 45°, kāds vienpusleņķis (°)?",
                 "atb": ["135"], "padoms": "180 − 45."},
            ]),
            pavediens="maja",
            konteksts="Kāpņu meistars zāģē kāpņu sānu dēļu galus tā, lai tie "
                      "gultos uz paralēlām grīdām.",
            kapec="Viens leņķis nosaka abus zāģējumus."),

    Kopsavilkums([
        "Veidoju leņķu ķēdi no zināmā līdz meklētajam.",
        "Katrā solī lietoju vienu īpašību.",
        "Aprēķinu leņķus ar attiecībām.",
        "Risinu lauztās līnijas uzdevumu starp paralēlām.",
    ]),

    Majas([
        "a ∥ b, ∠7 = 115°. Atrodi visus leņķus.",
        "Pierādi, ka ∠AMB = ∠A + ∠B lauztajai līnijai.",
        "Izdomā savu ķēdes uzdevumu.",
    ]),
]
