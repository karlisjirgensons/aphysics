# -*- coding: utf-8 -*-
"""8. klase, 104. stunda: «Kas kvadrātam ir īpašs?»

Kvadrāts ir gan rombs, gan taisnstūris, tāpēc tam ir visu īpašības:
diagonāles vienādas, perpendikulāras, dalās uz pusēm un dala leņķus pa
45°. Laukumu var rēķināt arī ar diagonāli: S = {d^2|2}.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, geometrija)

TEMA = "Kas kvadrātam ir īpašs?"

MERKIS = "Raksturosim kvadrātu kā rombu un taisnstūri vienlaikus."

SATURS = [
    Sakums("Rombs vai taisnstūris?",
           zimejums=geometrija([("A", 0, 0), ("B", 4, 0), ("C", 4, 4),
                                ("D", 0, 4), ("O", 2, 2, 270)],
                               nogriezni=["AB", "BC", "CD", "DA", "AC",
                                          "BD"],
                               svitras=[("AB", 1), ("BC", 1), ("CD", 1),
                                        ("DA", 1)],
                               taisni=["BAD", "BOC"],
                               lenki=[("BAC", "45°")],
                               iekrasot=[("ABCD", 0)]),
           paraksts="Kvadrāts ir abi: malas vienādas un leņķi taisni.",
           fakti=["Kvadrāts ir gan rombs, gan taisnstūris.",
                  "Diagonāles ir vienādas un perpendikulāras.",
                  "Diagonāle dala kvadrāta leņķi pa 45°."]),

    Doma("Visas īpašības kopā",
         "Kvadrātam ir paralelograma, romba un taisnstūra īpašības.",
         soli=[
             "No paralelograma: diagonāles dalās uz pusēm.",
             "No romba: diagonāles perpendikulāras un dala leņķus uz pusēm.",
             "No taisnstūra: diagonāles vienādas.",
             "Laukums: S = a^2 vai S = {d^2|2}.",
         ],
         pieze="Pazīme: rombs ar taisnu leņķi vai taisnstūris ar "
               "perpendikulārām diagonālēm ir kvadrāts."),

    Ievadi("Aprēķini", [
        {"jaut": "Kvadrāta mala 6. S?", "atb": ["36"], "padoms": "6^2."},
        {"jaut": "Kvadrāta diagonāle 10. S?", "atb": ["50"],
         "padoms": "{100|2}."},
        {"jaut": "∠AOB kvadrātā (°)?", "atb": ["90"],
         "padoms": "Diagonāles perpendikulāras."},
        {"jaut": "∠OAB (°)?", "atb": ["45"], "padoms": "90 : 2."},
        {"jaut": "Kvadrāta P = 20. S?", "atb": ["25"],
         "padoms": "Mala 5."},
        {"jaut": "Kvadrāta diagonāle 8. AO?", "atb": ["4"],
         "padoms": "Puse."},
    ], pamats=4),

    Varianti("Kurš četrstūris?", [
        {"jaut": "Diagonāles vienādas un perpendikulāras, dalās uz pusēm.",
         "opcijas": ["Kvadrāts", "Rombs", "Taisnstūris", "Trapece"],
         "pareizi": 0, "padoms": "Abas papildu īpašības."},
        {"jaut": "Diagonāles perpendikulāras, dalās uz pusēm, bet nav "
                 "vienādas.",
         "opcijas": ["Rombs", "Kvadrāts", "Taisnstūris", "Trapece"],
         "pareizi": 0, "padoms": "Tikai romba īpašība."},
        {"jaut": "Diagonāles vienādas, dalās uz pusēm, nav perpendikulāras.",
         "opcijas": ["Taisnstūris", "Kvadrāts", "Rombs", "Trapece"],
         "pareizi": 0, "padoms": "Tikai taisnstūra īpašība."},
        {"jaut": "Rombs ar taisnu leņķi ir...",
         "opcijas": ["kvadrāts", "taisnstūris, ne kvadrāts", "trapece",
                     "deltoīds"],
         "pareizi": 0, "padoms": "Visas malas vienādas un leņķi taisni."},
    ]),

    Pasaule("Šaha galdiņš",
            Ievadi("", [
                {"jaut": "Šaha galdiņš ir kvadrāts 8 × 8 lauciņi, lauciņš "
                         "5 cm. Galdiņa mala (cm)?",
                 "atb": ["40"], "padoms": "8 · 5."},
                {"jaut": "Galdiņa laukums (cm²)?", "atb": ["1600"],
                 "padoms": "40^2."},
                {"jaut": "Diagonāle ir d. Pēc formulas S = {d^2|2} - cik ir "
                         "d^2?",
                 "atb": ["3200"], "padoms": "2 · 1600."},
            ]),
            pavediens="speles",
            konteksts="Laidnis šahā iet pa diagonālēm - kvadrāta diagonāle "
                      "dala leņķi pa 45°.",
            kapec="Kvadrāta laukumu var rēķināt ar malu vai ar diagonāli."),

    Kopsavilkums([
        "Raksturoju kvadrātu kā rombu un taisnstūri.",
        "Lietoju visas kvadrāta diagonāļu īpašības.",
        "Aprēķinu kvadrāta laukumu ar diagonāli.",
    ]),

    Majas([
        "Salokot kvadrātveida papīru pa diagonālēm, pārbaudi īpašības.",
        "Izmēri flīzes diagonāli un aprēķini laukumu ar S = {d^2|2}.",
        "Pieraksti kvadrāta pazīmes.",
    ]),
]
