# -*- coding: utf-8 -*-
"""7. klase, 161. stunda: «Kā atrisināt sistēmu?»

Nevienādību sistēmas atrisinājums ir abu nevienādību atrisinājumu šķēlums -
tā pati kopu operācija, ko mācījāmies gada sākumā. Uz skaitļu taisnes
to redz kā vietu, kur abi svītrojumi pārklājas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, taisne)

TEMA = "Kā atrisināt sistēmu?"

MERKIS = ("Atrisināsim lineāru nevienādību sistēmu, nosakot atrisinājumu "
          "kopu šķēlumu.")

SATURS = [
    Sakums("Šķēlums - kur abi svītrojumi pārklājas",
           zimejums=taisne(-3, 6, 1, intervali=[(-1, None, False, True),
                                                (None, 4, False, True)]),
           paraksts="x ≥ −1 un x ≤ 4: kopīgā daļa [−1; 4].",
           fakti=["Sistēma - visām nevienādībām jāizpildās vienlaikus.",
                  "Tas ir kopu šķēlums (1. temats!).",
                  "Uz taisnes - dubultais svītrojums."]),

    Doma("Atrisini katru, tad šķēlums",
         "Lai atrisinātu nevienādību sistēmu, atrisina katru nevienādību "
         "atsevišķi, attēlo atrisinājumus uz vienas skaitļu taisnes un atrod "
         "to šķēlumu.",
         soli=[
             "Atrisini pirmo nevienādību.",
             "Atrisini otro.",
             "Attēlo abas uz vienas taisnes (dažādi svītrojumi).",
             "Kopīgā daļa ir atbilde; ja kopīgā nav - sistēmai nav "
             "atrisinājumu.",
         ]),

    Slidnis("Solis pa solim", [
        {"v": "1. nevienādība", "teksts": "2x + 1 > 3 ⇒ x > 1",
         "zim": taisne(-2, 7, 1, intervali=[(1, None, False, False)])},
        {"v": "2. nevienādība", "teksts": "x − 4 ≤ 1 ⇒ x ≤ 5",
         "zim": taisne(-2, 7, 1, intervali=[(None, 5, False, True)])},
        {"v": "Šķēlums", "teksts": "1 < x ≤ 5",
         "zim": taisne(-2, 7, 1, intervali=[(1, None, False, False),
                                            (None, 5, False, True)])},
    ]),

    Paraugs("Sistēma",
            uzd="Atrisini sistēmu: 2x + 1 > 3 un x − 4 ≤ 1.",
            soli=[
                ("2x > 2 ⇒ x > 1", "Pirmā."),
                ("x ≤ 5", "Otrā."),
                ("Šķēlums: 1 < x ≤ 5", "Kopīgā daļa."),
            ],
            atbilde="x ∈ (1; 5]"),

    Varianti("Šķēlums", [
        {"jaut": "x > 2 un x > 5",
         "opcijas": ["x > 5", "x > 2", "2 < x < 5", "Nav"],
         "pareizi": 0, "padoms": "Jāizpilda abas."},
        {"jaut": "x < 3 un x < 0",
         "opcijas": ["x < 0", "x < 3", "0 < x < 3", "Nav"],
         "pareizi": 0, "padoms": "Stingrākā."},
        {"jaut": "x > 4 un x < 1",
         "opcijas": ["Atrisinājumu nav", "1 < x < 4", "x > 4", "x < 1"],
         "pareizi": 0, "padoms": "Nepārklājas."},
        {"jaut": "x ≥ −2 un x < 3",
         "opcijas": ["[−2; 3)", "(−2; 3]", "(−2; 3)", "[−2; 3]"],
         "pareizi": 0, "padoms": "Iekavas no katras."},
    ], pamats=4),

    Ievadi("Atrisini", [
        {"jaut": "3x ≥ 6 un x + 1 < 6. Cik veselu atrisinājumu?",
         "atb": ["3"], "padoms": "2 ≤ x < 5: 2; 3; 4."},
        {"jaut": "x − 2 > 0 un 2x < 10. Mazākais vesels?",
         "atb": ["3"], "padoms": "2 < x < 5."},
        {"jaut": "−x < 1 un x ≤ 4. Mazākais vesels?",
         "atb": ["0"], "padoms": "x > −1."},
    ]),

    Pasaule("Istabas augs",
            Ievadi("", [
                {"jaut": "Augam vajag temperatūru virs 15 °C un ne vairāk par "
                         "28 °C. Cik veselu grādu vērtību der?",
                 "atb": ["13"], "padoms": "16; 17; ...; 28."},
                {"jaut": "Otram augam 20-35 °C. Cik veselu grādu der abiem "
                         "(20 ≤ t ≤ 28)?",
                 "atb": ["9"], "padoms": "20; 21; ...; 28."},
                {"jaut": "Kāda ir zemākā temperatūra, kas der abiem (°C)?",
                 "atb": ["20"], "padoms": "Šķēluma sākums."},
            ]),
            pavediens="daba",
            konteksts="Divus augus vienā telpā var turēt tikai temperatūrā, "
                      "kas der abiem - šķēlumā.",
            kapec="Sistēma = abu prasību šķēlums."),

    Kopsavilkums([
        "Atrisinu katru sistēmas nevienādību.",
        "Attēloju abas uz vienas taisnes.",
        "Atrodu šķēlumu.",
        "Zinu, ka šķēlums var būt tukšs.",
    ]),

    Majas([
        "Atrisini sistēmu: 4x − 3 > 5 un 2x + 1 ≤ 11.",
        "Izdomā sistēmu bez atrisinājumiem.",
        "Atrodi divu ierīču kopīgo darba temperatūru.",
    ]),
]
