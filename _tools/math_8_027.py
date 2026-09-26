# -*- coding: utf-8 -*-
"""8. klase, 27. stunda: «Kāds skaitlis sanāk?»

Bloka noslēgums: pakāpes skaitliskā vērtība ar jebkuru veselu kāpinātāju.
Tieši tāds ir eksāmena 1. uzdevums (5^3, 9^−2, (0,3)^2), tāpēc stundā ir
arī «eksāmena minūte» ar to pašu formu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kāds skaitlis sanāk?"

MERKIS = ("Aprēķināsim pakāpes skaitlisko vērtību, ja kāpinātājs ir vesels "
          "skaitlis.")

SATURS = [
    Sakums("Eksāmena 1. uzdevums",
           zimejums=restis([["5³ =", "?"], ["9⁻² =", "?"], ["(0,3)² =", "?"]]),
           paraksts="Trīs punkti - trīs pakāpes.",
           fakti=["Pozitīvs kāpinātājs - reizini.",
                  "Negatīvs - apgriez un reizini.",
                  "Decimāldaļa - skaiti ciparus aiz komata."]),

    Doma("Plāns jebkurai pakāpei",
         "Vispirms nosaki kāpinātāja veidu, tad bāzes zīmi un tikai tad "
         "rēķini.",
         soli=[
             "Kāpinātājs 0 - atbilde 1.",
             "Negatīvs kāpinātājs - pārraksti kā {1|a^n} vai apgriez daļu.",
             "Negatīva bāze: pāra kāpinātājs - pluss, nepāra - mīnuss.",
             "Decimāldaļa: ciparu skaits aiz komata reizinās ar kāpinātāju.",
             "Daļa: kāpini skaitītāju un saucēju.",
         ]),

    Ievadi("Eksāmena minūte", [
        {"jaut": "5^3", "atb": ["125"], "padoms": "25 · 5."},
        {"jaut": "9^−2 - atbildi raksti kā a/b",
         "atb": ["{1|81}", "1/81"], "padoms": "{1|9^2}."},
        {"jaut": "(0,3)^2", "atb": ["0,09", "0.09"],
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "(−1)^{101}", "atb": ["−1", "-1"], "padoms": "Nepāra."},
        {"jaut": "(0,1)^−3", "atb": ["1000"], "padoms": "10^3."},
        {"jaut": "({2|3})^−3 - atbildi raksti kā a/b",
         "atb": ["{27|8}", "27/8"], "padoms": "({3|2})^3."},
        {"jaut": "(−2)^−4 - atbildi raksti kā a/b",
         "atb": ["{1|16}", "1/16"], "padoms": "Pāra - pluss."},
        {"jaut": "0,2^3", "atb": ["0,008", "0.008"],
         "padoms": "Trīs cipari."},
    ], pamats=6),

    Ievadi("Izteiksmes vērtība", [
        {"jaut": "2^−1 + 2^0 + 2^1 - decimāldaļā",
         "atb": ["3,5", "3.5"], "padoms": "0,5 + 1 + 2."},
        {"jaut": "{3^4 · 3^−2|3^3} - atbildi raksti kā a/b",
         "atb": ["{1|3}", "1/3"], "padoms": "3^{−1}."},
        {"jaut": "(−3)^2 − 3^2", "atb": ["0"], "padoms": "9 − 9."},
        {"jaut": "10^−1 · 10^−2 - decimāldaļā", "atb": ["0,001", "0.001"],
         "padoms": "10^−3."},
    ]),

    Varianti("Salīdzini bez kalkulatora", [
        {"jaut": "Kurš ir lielāks: 2^−3 vai 3^−2?",
         "opcijas": ["2^−3 = {1|8}", "3^−2 = {1|9}", "Vienādi",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "{1|8} > {1|9}."},
        {"jaut": "Kura vērtība ir negatīva?",
         "opcijas": ["(−2)^3", "(−2)^−2", "(−2)^0", "(−2)^4"],
         "pareizi": 0, "padoms": "Nepāra kāpinātājs."},
        {"jaut": "(0,5)^−2 =",
         "opcijas": ["4", "0,25", "−0,25", "1"],
         "pareizi": 0, "padoms": "2^2."},
    ]),

    Pasaule("Skaņas skaļums",
            Ievadi("", [
                {"jaut": "Katri +10 dB nozīmē 10 reizes lielāku skaņas "
                         "intensitāti. Cik reižu intensīvāk ir +30 dB?",
                 "atb": ["1000"], "padoms": "10^3."},
                {"jaut": "Troksnis 90 dB, sarunas 60 dB. Cik reižu "
                         "intensīvāks ir troksnis?",
                 "atb": ["1000"], "padoms": "10^{9 − 6}."},
                {"jaut": "Austiņas ar trokšņu slāpēšanu samazina par 20 dB. "
                         "Kāda daļa intensitātes paliek? (decimāldaļā)",
                 "atb": ["0,01", "0.01"], "padoms": "10^−2."},
            ]),
            pavediens="tehnika",
            konteksts="Decibeli ir pakāpju skala: skaņa, kas skan 2 reizes "
                      "skaļāk, var būt 100 reizes intensīvāka.",
            kapec="Tāpēc ilgstošs 85 dB troksnis jau var bojāt dzirdi."),

    Kopsavilkums([
        "Aprēķinu pakāpi ar pozitīvu, nulles un negatīvu kāpinātāju.",
        "Nosaku zīmi pakāpei ar negatīvu bāzi.",
        "Kāpinu decimāldaļas un daļas.",
        "Salīdzinu pakāpes bez kalkulatora.",
    ]),

    Majas([
        "Aprēķini: 4^3, 6^−2, (0,4)^2, (−1)^−7, ({1|3})^−2.",
        "Pārbaudi atbildes ar kalkulatoru (poga ^ vai xʸ).",
        "Atrodi internetā, cik dB ir koncerts un cik - čuksts.",
    ]),
]
