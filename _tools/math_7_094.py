# -*- coding: utf-8 -*-
"""7. klase, 94. stunda: «Kādas ir šo leņķu īpašības?»

Ja taisnes ir paralēlas, kāpšļu leņķi ir vienādi, iekšējie šķērsleņķi ir
vienādi, un iekšējo vienpusleņķu summa ir 180°. Stunda pieņem kāpšļu leņķu
īpašību un no tās pierāda pārējās divas ar krustleņķiem un blakusleņķiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, paralelas)

TEMA = "Kādas ir šo leņķu īpašības?"

MERKIS = ("Formulēsim un pierādīsim iekšējo šķērsleņķu un vienpusleņķu "
          "īpašības.")

SATURS = [
    Sakums("Paralēlas taisnes - vienādi leņķi",
           zimejums=paralelas(uzraksti={1: "60°", 5: "60°", 3: "60°",
                                        4: "120°"},
                              radit=(1, 3, 4, 5), loki={1: 2, 3: 2, 5: 2}),
           paraksts="a ∥ b: ∠1 = ∠5, ∠3 = ∠5, ∠4 + ∠5 = 180°.",
           fakti=["Krustotājs krusto abas paralēlās «vienādi».",
                  "Tāpēc leņķi pie abām taisnēm atkārtojas.",
                  "Zinot vienu leņķi, zina visus astoņus."]),

    Doma("Trīs īpašības",
         "Ja divas paralēlas taisnes krusto trešā, tad: 1) kāpšļu leņķi ir "
         "vienādi; 2) iekšējie šķērsleņķi ir vienādi; 3) iekšējo "
         "vienpusleņķu summa ir 180°.",
         soli=[
             "Kāpšļu leņķu īpašību pieņem (tā izriet no paralēlo aksiomas).",
             "Šķērsleņķi: ∠3 = ∠1 (krustleņķi) un ∠1 = ∠5 (kāpšļu).",
             "Tātad ∠3 = ∠5.",
             "Vienpusleņķi: ∠4 + ∠3 = 180° un ∠3 = ∠5, tātad ∠4 + ∠5 = 180°.",
         ],
         pieze="Tas ir tikai paralēlām taisnēm! Ja a un b nav paralēlas, "
               "neviena no šīm vienādībām negarantē."),

    Paraugs("Pierādi šķērsleņķu īpašību",
            uzd="a ∥ b, c - krustotājs. Pierādi, ka ∠3 = ∠5.",
            soli=[
                ("∠1 = ∠5", "(kāpšļu leņķi, a ∥ b)"),
                ("∠1 = ∠3", "(krustleņķi)"),
                ("∠3 = ∠5", "(abi vienādi ar ∠1)"),
            ],
            atbilde="Iekšējie šķērsleņķi ir vienādi."),

    Zimejums("Vienpusleņķi",
             paralelas(radit=(4, 5), uzraksti={4: "?", 5: "70°"}, slipums=70),
             paskaidro="∠4 = 180° − 70° = 110°."),

    Ievadi("Aprēķini (a ∥ b)", [
        {"jaut": "∠1 = 65°. Cik grādu ir ∠5?",
         "atb": ["65"], "padoms": "Kāpšļu leņķi."},
        {"jaut": "∠5 = 65°. Cik grādu ir ∠3?",
         "atb": ["65"], "padoms": "Šķērsleņķi."},
        {"jaut": "∠5 = 65°. Cik grādu ir ∠4?",
         "atb": ["115"], "padoms": "Vienpusleņķi: 180 − 65."},
        {"jaut": "∠6 = 130°. Cik grādu ir ∠4?",
         "atb": ["130"], "padoms": "Šķērsleņķi."},
    ]),

    Varianti("Kas vienāds?", [
        {"jaut": "a ∥ b. Kurš leņķis ir vienāds ar ∠2?",
         "opcijas": ["∠6", "∠5", "∠1", "∠3"],
         "pareizi": 0, "padoms": "Kāpšļu."},
        {"jaut": "a ∥ b. Kura summa ir 180°?",
         "opcijas": ["∠3 + ∠6", "∠3 + ∠5", "∠1 + ∠5", "∠2 + ∠6"],
         "pareizi": 0, "padoms": "Vienpusleņķi."},
        {"jaut": "a un b NAV paralēlas. Vai ∠1 = ∠5?",
         "opcijas": ["Nē, parasti nav", "Jā, vienmēr",
                     "Jā, ja c ir slīpa", "Nevar zināt"],
         "pareizi": 0, "padoms": "Īpašības tikai paralēlām."},
    ]),

    Pasaule("Saules stari",
            Ievadi("", [
                {"jaut": "Saules stari ir paralēli. Viens stars krīt uz "
                         "zemi 38° leņķī. Kādā leņķī krīt blakus stars (°)?",
                 "atb": ["38"], "padoms": "Kāpšļu leņķi."},
                {"jaut": "Cik grādu ir leņķis otrpus stara (blakusleņķis)?",
                 "atb": ["142"], "padoms": "180 − 38."},
                {"jaut": "Eratostens mērīja staru leņķi Aleksandrijā: 7,2°. "
                         "Kāda daļa no 360° tas ir? Atbildi: 360 : 7,2 = ?",
                 "atb": ["50"], "padoms": "Tik reižu Zemes apkārtmērs lielāks "
                                        "par attālumu."},
            ]),
            pavediens="kosmoss",
            konteksts="Pirms 2200 gadiem Eratostens ar paralēlu staru leņķiem "
                      "izmērīja Zemes apkārtmēru.",
            kapec="Šķērsleņķi deva viņam atbildi."),

    Kopsavilkums([
        "Zinu: a ∥ b - kāpšļu leņķi vienādi.",
        "Pierādu: iekšējie šķērsleņķi vienādi.",
        "Pierādu: vienpusleņķu summa 180°.",
        "Zinu, ka īpašības der tikai paralēlām taisnēm.",
    ]),

    Majas([
        "Pierādi vienpusleņķu īpašību ar pierakstu.",
        "Ja ∠7 = 50° un a ∥ b, aprēķini visus 8 leņķus.",
        "Uzzini vairāk par Eratostena eksperimentu.",
    ]),
]
