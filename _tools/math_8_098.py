# -*- coding: utf-8 -*-
"""8. klase, 98. stunda: «Kad četrstūris ir paralelograms?»

Pazīmes - apgrieztas īpašībām: pretējās malas pa pāriem vienādas; viens
malu pāris paralēls un vienāds; diagonāles dalās uz pusēm; pretējie leņķi
vienādi. Pretpiemērs: AB ∥ CD un AD = BC der arī vienādsānu trapecei.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, geometrija)

TEMA = "Kad četrstūris ir paralelograms?"

MERKIS = ("Lietosim paralelograma pazīmes, lai pamatotu, ka četrstūris ir "
          "paralelograms.")

SATURS = [
    Sakums("Pretējās malas vienādas - vai tas ir paralelograms?",
           zimejums=geometrija([("A", 0, 0), ("B", 5, 0), ("C", 6.5, 3),
                                ("D", 1.5, 3)],
                               nogriezni=["AB", "BC", "CD", "DA"],
                               svitras=[("AB", 1), ("CD", 1), ("BC", 2),
                                        ("DA", 2)],
                               iekrasot=[("ABCD", 0)]),
           paraksts="Jā - to garantē pazīme.",
           fakti=["Pazīme ļauj secināt, ka četrstūris ir paralelograms.",
                  "Pietiek ar vienu pazīmi.",
                  "Īpašība un pazīme ir apgriezti apgalvojumi."]),

    Doma("Paralelograma pazīmes",
         "Četrstūris ir paralelograms, ja izpildās kaut viena pazīme.",
         soli=[
             "Pretējās malas pa pāriem vienādas.",
             "Viens malu pāris ir gan paralēls, gan vienāds.",
             "Diagonāles krustpunktā dalās uz pusēm.",
             "Pretējie leņķi pa pāriem vienādi.",
         ],
         pieze="Uzmanies: AB ∥ CD un AD = BC nav pazīme - tā var būt "
               "vienādsānu trapece."),

    Varianti("Vai noteikti paralelograms?", [
        {"jaut": "AB = CD un AD = BC.",
         "opcijas": ["Jā", "Nē - var būt trapece", "Nevar noteikt",
                     "Tikai rombs"],
         "pareizi": 0, "padoms": "1. pazīme."},
        {"jaut": "AB ∥ CD un AB = CD.",
         "opcijas": ["Jā", "Nē", "Tikai taisnstūris", "Nevar noteikt"],
         "pareizi": 0, "padoms": "2. pazīme."},
        {"jaut": "AB ∥ CD un AD = BC.",
         "opcijas": ["Ne vienmēr - der arī vienādsānu trapece", "Jā, vienmēr",
                     "Tas ir rombs", "Tas ir kvadrāts"],
         "pareizi": 0, "padoms": "Pretpiemērs."},
        {"jaut": "Diagonāles krustpunktā dalās uz pusēm.",
         "opcijas": ["Jā", "Nē", "Tikai ja tās vienādas",
                     "Tikai ja perpendikulāras"],
         "pareizi": 0, "padoms": "3. pazīme."},
    ]),

    Ievadi("Pārbaudi koordinātēs", [
        {"jaut": "A(1; 1), B(5; 2), C(6; 5), D(2; 4). No A uz B: cik pa "
                 "labi?", "atb": ["4"], "padoms": "5 − 1."},
        {"jaut": "No D uz C: cik pa labi?", "atb": ["4"], "padoms": "6 − 2."},
        {"jaut": "AC viduspunkta x koordināte?", "atb": ["3,5"],
         "padoms": "(1 + 6) : 2."},
        {"jaut": "BD viduspunkta x koordināte?", "atb": ["3,5"],
         "padoms": "(5 + 2) : 2 - sakrīt, tātad paralelograms."},
    ]),

    Pasaule("Mērnieka pārbaude",
            Ievadi("", [
                {"jaut": "Zemes gabala pretējās malas: 40 m un 40 m, 25 m un "
                         "25 m. Vai tas noteikti ir paralelograms? (1 - jā, "
                         "0 - nē)",
                 "atb": ["1"], "padoms": "1. pazīme."},
                {"jaut": "Vai tas noteikti ir taisnstūris? (1/0)",
                 "atb": ["0"], "padoms": "Leņķi nav zināmi."},
                {"jaut": "Perimetrs (m)?", "atb": ["130"],
                 "padoms": "2 · (40 + 25)."},
            ]),
            pavediens="maja",
            konteksts="Mērnieks mēra malas; pēc pazīmes no tām var secināt "
                      "formu.",
            kapec="Pretējo malu pāri vienādi ⇒ paralelograms."),

    Kopsavilkums([
        "Formulēju paralelograma pazīmes.",
        "Nošķiru īpašību no pazīmes.",
        "Ar pretpiemēru parādu, ka apgalvojums nav pazīme.",
    ]),

    Majas([
        "Pieraksti katru pazīmi kā «ja ..., tad četrstūris ir "
        "paralelograms».",
        "Uzzīmē vienādsānu trapeci un parādi, kāpēc tā ir pretpiemērs.",
        "Ar diviem vienāda garuma zīmuļiem izveido paralelogramu.",
    ]),
]
