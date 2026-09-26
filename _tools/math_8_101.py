# -*- coding: utf-8 -*-
"""8. klase, 101. stunda: «Ar ko rombs atšķiras no paralelograma?»

Rombs - paralelograms ar vienādām blakus malām. Papildu īpašības:
diagonāles ir perpendikulāras un dala romba leņķus uz pusēm. Zīmējuma
rombam A(0; 0), B(5; 0), C(8; 4), D(3; 4) visas malas ir 5 un diagonāles
tiešām perpendikulāras.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Ar ko rombs atšķiras no paralelograma?"

MERKIS = "Definēsim rombu un formulēsim tā papildu īpašības."

SATURS = [
    Sakums("Kas rombam ir īpašs?",
           zimejums=geometrija([("A", 0, 0), ("B", 5, 0), ("C", 8, 4),
                                ("D", 3, 4), ("O", 4, 2, 300)],
                               nogriezni=["AB", "BC", "CD", "DA", "AC",
                                          "BD"],
                               svitras=[("AB", 1), ("BC", 1), ("CD", 1),
                                        ("DA", 1)],
                               taisni=["BOC"], iekrasot=[("ABCD", 0)]),
           paraksts="Visas malas vienādas, diagonāles perpendikulāras.",
           fakti=["Rombs - paralelograms ar vienādām blakus malām.",
                  "Romba diagonāles ir perpendikulāras.",
                  "Diagonāles dala romba leņķus uz pusēm."]),

    Doma("Romba īpašības",
         "Rombam ir visas paralelograma īpašības un vēl divas.",
         soli=[
             "Pretējās malas paralēlas, diagonāles dalās uz pusēm.",
             "Papildus: diagonāles ir perpendikulāras.",
             "Papildus: diagonāles ir leņķu bisektrises.",
             "Diagonāles sadala rombu četros vienādos taisnleņķa "
             "trijstūros.",
         ]),

    Paraugs("Kāpēc perpendikulāras?",
            uzd="Pierādi, ka romba ABCD diagonāles ir perpendikulāras.",
            soli=[
                ("AB = AD", "Romba malas."),
                ("BO = OD", "Diagonāles dalās uz pusēm."),
                ("AO - kopīga", "△ABO un △ADO."),
                ("△ABO = △ADO", "Pēc trim malām."),
                ("∠AOB = ∠AOD = 90°", "Tie ir vienādi blakusleņķi."),
            ],
            atbilde="AC ⊥ BD"),

    Ievadi("Aprēķini", [
        {"jaut": "Romba mala 7 cm. Perimetrs (cm)?", "atb": ["28"],
         "padoms": "4 · 7."},
        {"jaut": "P = 36 cm. Mala (cm)?", "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "∠A = 70°. ∠BAC?", "atb": ["35"],
         "padoms": "Diagonāle dala uz pusēm."},
        {"jaut": "∠A = 70°. ∠B?", "atb": ["110"], "padoms": "180 − 70."},
        {"jaut": "Diagonāles 6 cm un 8 cm. AO (cm)?", "atb": ["3"],
         "padoms": "Puse no 6."},
        {"jaut": "Leņķis starp diagonālēm (°)?", "atb": ["90"],
         "padoms": "Perpendikulāras."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Vai katrs rombs ir paralelograms?",
         "opcijas": ["Jā", "Nē", "Tikai kvadrāts", "Tikai šaurs"],
         "pareizi": 0, "padoms": "Pretējās malas paralēlas."},
        {"jaut": "Romba diagonāles krustojas leņķī...",
         "opcijas": ["90°", "60°", "45°", "atkarīgs no romba"],
         "pareizi": 0, "padoms": "Vienmēr perpendikulāras."},
        {"jaut": "Vai romba diagonāles ir vienādas?",
         "opcijas": ["Tikai kvadrātam", "Vienmēr", "Nekad",
                     "Tikai šauram rombam"],
         "pareizi": 0, "padoms": "Kvadrāts ir īpašs rombs."},
    ]),

    Pasaule("Galvenā ceļa zīme",
            Ievadi("", [
                {"jaut": "Galvenā ceļa zīme ir rombs ar malu 60 cm. "
                         "Perimetrs (cm)?",
                 "atb": ["240"], "padoms": "4 · 60."},
                {"jaut": "Leņķis starp tās diagonālēm (°)?", "atb": ["90"],
                 "padoms": "Romba īpašība."},
                {"jaut": "Zīmes leņķis ir 90°. Diagonāle to dala leņķos pa "
                         "cik grādiem?",
                 "atb": ["45"], "padoms": "Bisektrise."},
            ]),
            pavediens="celojums",
            konteksts="Galvenā ceļa zīme ir rombs; tāda pati forma ir "
                      "«kāravam» kāršu kārtīs.",
            kapec="Romba diagonāles ir perpendikulāras un dala leņķus uz "
                  "pusēm."),

    Kopsavilkums([
        "Definēju rombu.",
        "Formulēju un pierādu romba diagonāļu īpašības.",
        "Lietoju tās aprēķinos.",
    ]),

    Majas([
        "No diviem vienāda garuma salmiņiem, kas krustojas vidū taisnā "
        "leņķī, izveido rombu.",
        "Uzzīmē rombu un izmēri leņķi starp diagonālēm.",
        "Atrodi rombus rakstos un logos.",
    ]),
]
