# -*- coding: utf-8 -*-
"""8. klase, 85. stunda: «Kad divas taisnes ir paralēlas?»

Temata 8.5. sākums. 7. klasē no paralēlām taisnēm secināja leņķus; tagad
otrādi - pēc leņķiem secina paralelitāti. Trīs pazīmes: kāpšļu leņķi,
iekšējie šķērsleņķi, iekšējie vienpusleņķi. Numerācija - paralelas():
1 un 5 kāpšļu, 3 un 5 šķērsleņķi, 4 un 5 vienpusleņķi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, paralelas)

TEMA = "Kad divas taisnes ir paralēlas?"

MERKIS = "Formulēsim un lietosim taišņu paralelitātes pazīmes."

SATURS = [
    Sakums("Vai taisnes a un b ir paralēlas?",
           zimejums=paralelas(radit=(1, 5), uzraksti={1: "70°", 5: "70°"},
                              slipums=70),
           paraksts="Kāpšļu leņķi ir vienādi, tātad a ∥ b.",
           fakti=["Ja kāpšļu leņķi ir vienādi, taisnes ir paralēlas.",
                  "Ja iekšējie šķērsleņķi ir vienādi - arī.",
                  "Ja iekšējo vienpusleņķu summa ir 180° - arī."]),

    Doma("Paralelitātes pazīmes",
         "Pazīme ļauj no leņķiem secināt, ka taisnes ir paralēlas.",
         soli=[
             "Kāpšļu leņķi vienādi (∠1 = ∠5) ⇒ a ∥ b.",
             "Iekšējie šķērsleņķi vienādi (∠3 = ∠5) ⇒ a ∥ b.",
             "Iekšējo vienpusleņķu summa 180° (∠4 + ∠5 = 180°) ⇒ a ∥ b.",
             "Pietiek ar vienu pāri - pārējie tad izriet paši.",
         ],
         pieze="Pazīme ir apgriezta īpašībai: 7. klasē no a ∥ b secināja "
               "leņķus, tagad no leņķiem secina a ∥ b."),

    Slidnis("Trīs pazīmes un viens pretpiemērs", [
        {"v": "∠1 = ∠5", "teksts": "Kāpšļu leņķi - a ∥ b",
         "zim": paralelas(radit=(1, 5), loki={1: 1, 5: 1})},
        {"v": "∠3 = ∠5", "teksts": "Iekšējie šķērsleņķi - a ∥ b",
         "zim": paralelas(radit=(3, 5), loki={3: 1, 5: 1})},
        {"v": "∠4 + ∠5 = 180°", "teksts": "Iekšējie vienpusleņķi - a ∥ b",
         "zim": paralelas(radit=(4, 5))},
        {"v": "∠1 ≠ ∠5", "teksts": "Taisnes nav paralēlas - kaut kur "
                                   "krustojas",
         "zim": paralelas(radit=(1, 5), paralelas=False)},
    ]),

    Varianti("Vai a ∥ b?", [
        {"jaut": "∠1 = 65°, ∠5 = 65°.",
         "opcijas": ["Jā - kāpšļu leņķi vienādi", "Nē", "Nevar noteikt",
                     "Tikai ja ∠2 = 65°"],
         "pareizi": 0, "padoms": "1 un 5 ir kāpšļu leņķi."},
        {"jaut": "∠3 = 110°, ∠5 = 70°.",
         "opcijas": ["Nē - šķērsleņķi nav vienādi", "Jā - summa 180°",
                     "Jā - tie ir vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "3 un 5 ir šķērsleņķi - tiem jābūt "
                                 "vienādiem."},
        {"jaut": "∠4 = 100°, ∠5 = 80°.",
         "opcijas": ["Jā - vienpusleņķu summa 180°", "Nē", "Nevar noteikt",
                     "Tikai ja ∠4 = ∠5"],
         "pareizi": 0, "padoms": "100° + 80° = 180°."},
    ]),

    Ievadi("Cik grādu jābūt ∠5, lai a ∥ b?", [
        {"jaut": "∠1 = 58°. ∠5 = ?", "atb": ["58"],
         "padoms": "Kāpšļu leņķi."},
        {"jaut": "∠4 = 123°. ∠5 = ?", "atb": ["57"],
         "padoms": "Vienpusleņķi: 180° − 123°."},
        {"jaut": "∠3 = 41°. ∠5 = ?", "atb": ["41"],
         "padoms": "Šķērsleņķi."},
        {"jaut": "∠2 = 130°. ∠5 = ?", "atb": ["50"],
         "padoms": "∠1 = 180° − 130°, tad kāpšļu leņķi."},
    ]),

    Pasaule("Plaukti pie slīpas sijas",
            Ievadi("", [
                {"jaut": "Pirmais plaukts ar slīpo siju veido 72°. Kādu "
                         "kāpšļu leņķi vajag otram, lai plaukti būtu "
                         "paralēli?",
                 "atb": ["72"], "padoms": "Kāpšļu leņķi vienādi."},
                {"jaut": "Ja otru leņķi mēra kā vienpusleņķi, cik grādu "
                         "jābūt?",
                 "atb": ["108"], "padoms": "180° − 72°."},
                {"jaut": "Izmērīja 71° un 72° kāpšļu vietā. Vai plaukti "
                         "paralēli? (1 - jā, 0 - nē)",
                 "atb": ["0"], "padoms": "Leņķi nav vienādi."},
            ]),
            pavediens="maja",
            konteksts="Galdnieks pārbauda paralelitāti ar leņķmēru - pietiek "
                      "ar vienu leņķu pāri.",
            kapec="Vienādi kāpšļu leņķi garantē paralēlas taisnes."),

    Kopsavilkums([
        "Formulēju trīs paralelitātes pazīmes.",
        "Pēc leņķiem nosaku, vai taisnes ir paralēlas.",
        "Nošķiru pazīmi no īpašības.",
    ]),

    Majas([
        "Uzzīmē divas taisnes un krustotāju; izmēri ∠1 un ∠5.",
        "Pārbaudi ar leņķmēru, vai logu rāmja malas ir paralēlas.",
        "Pieraksti pazīmi un īpašību kā divus teikumus «ja ..., tad ...».",
    ]),
]
