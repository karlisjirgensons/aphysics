# -*- coding: utf-8 -*-
"""9. klase, 122. stunda: «Kā to risinātu eksāmenā?»

Vienādojumu sistēmas eksāmena formātā: 2025. gada 2. daļas 3. uzdevums
(stallis, 5 punkti) ar pilnu noformējumu un 1. daļas stila īsie
uzdevumi. Par ko dod punktus: nezināmie, sistēma, atrisinājums, atbilde.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, paris, restis)

TEMA = "Kā to risinātu eksāmenā?"

MERKIS = ("Risināsim eksāmena formāta uzdevumus ar vienādojumu sistēmām.")

_T = "text"

SATURS = [
    Sakums("5 punkti par vienu uzdevumu - par ko?",
           zimejums=restis([["solis", "punkts"], ["nezināmo apzīmējumi", "1"],
                            ["sistēma", "1-2"], ["atrisināšana", "1"],
                            ["atbilde ar vārdiem", "1"]]),
           paraksts="Punktus dod arī par pusceļu - raksti visu.",
           fakti=["Pat ja kļūdies rēķinā, sistēma dod punktus.",
                  "Atbilde - uz uzdevuma jautājumu.",
                  "Pārbaude ar tekstu - ne tikai ar vienādojumiem."]),

    Doma("Noformējums",
         "x - ..., y - ... → sistēma → atrisinājums → pārbaude → atbilde.",
         soli=[
             "Apzīmējumi ar vārdiem un mērvienībām.",
             "Sistēma ar figūriekavu.",
             "Paņēmiens - katrs solis jaunā rindā.",
             "Pārbaude pēc uzdevuma teksta.",
             "Atbilde pilnā teikumā.",
         ]),

    Paraugs("Eksāmens 2025, 2. daļa, 3. uzdevums",
            uzd="Stallī 88 nodalījumi, aizņemti 75 %. Ponijs maksā 180 €, "
                "zirgs 270 € mēnesī; kopā 16 650 €. Cik zirgu?",
            soli=[
                ("0,75 · 88 = 66 dzīvnieki", "Aizņemtie nodalījumi."),
                ("x - poniji, y - zirgi: x + y = 66, 180x + 270y = 16 650",
                 "Sistēma."),
                ("180(66 − y) + 270y = 16 650 ⇒ 90y = 4770 ⇒ y = 53",
                 "Ievietošana."),
                ("x = 13; 13 · 180 + 53 · 270 = 2340 + 14 310 = 16 650 ✔",
                 "Pārbaude."),
            ],
            atbilde="stallī bija 53 zirgi"),

    Ievadi("1. daļa: atrisini sistēmu", [
        {"jaut": "x + y = 12 un x − y = 4", "atb": paris(8, 4),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "2x = 16."},
        {"jaut": "y = 2x − 1 un 3x + y = 14", "atb": paris(3, 5),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "5x − 1 = 14."},
        {"jaut": "2x + 3y = 13 un 2x − y = 1", "atb": paris(2, 3),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "Atņem: 4y = 12."},
    ]),

    Varianti("Atbilžu izvēle", [
        {"jaut": "Sistēmai 2x + y = 3 un 4x + 2y = 7...",
         "opcijas": ["nav atrisinājuma", "viens", "bezgalīgi daudz",
                     "divi"],
         "pareizi": 0, "padoms": "Paralēlas taisnes."},
        {"jaut": "Kurš pāris ir sistēmas x + y = 5, x − y = −1 atrisinājums?",
         "opcijas": ["(2; 3)", "(3; 2)", "(−1; 6)", "(5; 0)"],
         "pareizi": 0, "padoms": "2 − 3 = −1."},
    ]),

    Pasaule("Sporta zāles abonementi",
            Ievadi("", [
                {"jaut": "Pārdoti 150 abonementi: skolēnu 20 €, pieaugušo 35 €; "
                         "ieņēmumi 4050 €. Skolēnu abonementu?", "atb": ["80"],
                 "padoms": "20x + 35(150 − x) = 4050."},
                {"jaut": "Pieaugušo abonementu?", "atb": ["70"],
                 "padoms": "150 − 80."},
            ]),
            pavediens="sports",
            konteksts="Tipisks 2. daļas uzdevums: skaits, cenas, kopsumma.",
            kapec="Tā pati «stalla» struktūra - cita situācija."),

    Kopsavilkums([
        "Noformēju sistēmas uzdevumu eksāmena stilā.",
        "Zinu, par ko dod punktus.",
        "Pārbaudu atbildi pēc teksta.",
    ]),

    Majas([
        "Atkārto 9.6. tematu - nākamajā stundā pārbaudes darbs.",
        "Atrisini: 3x − 2y = 4, x + 4y = 13.",
        "Uzraksti un atrisini savu «stalla» tipa uzdevumu.",
    ]),
]
