# -*- coding: utf-8 -*-
"""8. klase, 86. stunda: «Kā pierādīt paralelitāti?»

Pierādījums ir ķēde, kurā katram solim ir pamatojums: krustleņķi,
blakusleņķi un beigās pazīme. Paraugā ∠1 un ∠7 nav tiešs pazīmes pāris,
tāpēc starpā vajag krustleņķus 5 un 7.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, paralelas)

TEMA = "Kā pierādīt paralelitāti?"

MERKIS = ("Pierādīsim divu taišņu paralelitāti, izmantojot leņķu "
          "sakarības.")

SATURS = [
    Sakums("∠1 = 50° un ∠7 = 50°. Vai a ∥ b?",
           zimejums=paralelas(radit=(1, 7), uzraksti={1: "50°", 7: "50°"},
                              slipums=50),
           paraksts="∠1 un ∠7 nav tiešs pazīmes pāris - vajag starpsoli.",
           fakti=["Pierādījums ir ķēde: dots → likums → secinājums.",
                  "Katram solim min pamatojumu.",
                  "Beigās nosauc pazīmi, kas dod paralelitāti."]),

    Doma("Pierādījuma soļi",
         "Starp doto un pazīmi atrod leņķi, kas tos savieno.",
         soli=[
             "Pieraksti, kas dots un kas jāpierāda.",
             "Atrodi starpleņķi: krustleņķis ir vienāds, blakusleņķis dod "
             "180°.",
             "Katrai vienādībai uzraksti pamatojumu.",
             "Noslēdz: «tātad a ∥ b pēc ... pazīmes».",
         ],
         pieze="Nedrīkst lietot to, kas jāpierāda: «a ∥ b, tāpēc ∠1 = ∠5, "
               "tāpēc a ∥ b» neko nepierāda."),

    Paraugs("Pierādi",
            uzd="Dots: ∠1 = 50°, ∠7 = 50°. Pierādi, ka a ∥ b.",
            soli=[
                ("∠5 = ∠7 = 50°", "Krustleņķi ir vienādi."),
                ("∠1 = ∠5 = 50°", "Kāpšļu leņķi ir vienādi."),
                ("a ∥ b", "Pēc kāpšļu leņķu pazīmes."),
            ],
            atbilde="a ∥ b"),

    Varianti("Kurš pamatojums der?", [
        {"jaut": "∠5 = ∠7, jo...",
         "opcijas": ["tie ir krustleņķi", "tie ir kāpšļu leņķi",
                     "tie ir blakusleņķi", "a ∥ b"],
         "pareizi": 0, "padoms": "Pretējie leņķi vienā krustpunktā."},
        {"jaut": "∠1 + ∠2 = 180°, jo...",
         "opcijas": ["tie ir blakusleņķi", "tie ir krustleņķi", "a ∥ b",
                     "tie ir šķērsleņķi"],
         "pareizi": 0, "padoms": "Kopīga mala, kopā taisne."},
        {"jaut": "Dots ∠2 = 120°, ∠5 = 60°. Secinājums?",
         "opcijas": ["a ∥ b, jo ∠1 = 60° = ∠5", "a un b krustojas",
                     "Nevar noteikt", "a ⊥ b"],
         "pareizi": 0, "padoms": "∠1 = 180° − 120°."},
        {"jaut": "Kur kļūda: «a ∥ b, tāpēc ∠1 = ∠5, tāpēc a ∥ b»?",
         "opcijas": ["Pierāda ar to, kas jāpierāda", "Kļūdas nav",
                     "Jāmin krustleņķi", "Trūkst zīmējuma"],
         "pareizi": 0, "padoms": "Apburtais loks."},
    ]),

    Ievadi("Aprēķini, lai a ∥ b", [
        {"jaut": "∠6 = 125°. Cik grādu jābūt ∠1?", "atb": ["55"],
         "padoms": "∠5 = 180° − 125°, tad kāpšļu leņķi."},
        {"jaut": "∠8 = 70°. Cik grādu jābūt ∠3?", "atb": ["110"],
         "padoms": "∠6 = ∠8 = 70°, ∠5 = 110°, ∠3 = ∠5."},
        {"jaut": "∠4 = 2x, ∠5 = x. Kāds x dod a ∥ b?", "atb": ["60"],
         "padoms": "Vienpusleņķi: 3x = 180°."},
    ]),

    Pasaule("Sliežu pārbaude",
            Ievadi("", [
                {"jaut": "Gulsnis ar vienu sliedi veido 90°. Cik grādu jābūt "
                         "ar otru sliedi, lai tās būtu paralēlas?",
                 "atb": ["90"], "padoms": "Kāpšļu leņķi."},
                {"jaut": "Izmērīja 89°. Vai sliedes paralēlas? (1 - jā, "
                         "0 - nē)",
                 "atb": ["0"], "padoms": "89° ≠ 90°."},
                {"jaut": "Cik grādu ir vienpusleņķu summai pie paralēlām "
                         "sliedēm?",
                 "atb": ["180"], "padoms": "90° + 90°."},
            ]),
            pavediens="celojums",
            konteksts="Sliežu ceļa mērītāji pārbauda, vai sliedes visur ir "
                      "paralēlas.",
            kapec="Viens leņķu pāris, kas atbilst pazīmei, pierāda "
                  "paralelitāti."),

    Kopsavilkums([
        "Veidoju pierādījumu kā ķēdi ar pamatojumiem.",
        "Lietoju krustleņķus un blakusleņķus kā starpsoļus.",
        "Pamanu, ja pierādījumā lietots tas, kas jāpierāda.",
    ]),

    Majas([
        "Pierādi: ja ∠2 = ∠8, tad a ∥ b.",
        "Izdomā uzdevumu ar ∠6 un ∠3 un atrisini to.",
        "Paskaidro draugam, kāpēc krustleņķi ir vienādi.",
    ]),
]
