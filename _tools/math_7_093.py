# -*- coding: utf-8 -*-
"""7. klase, 93. stunda: «Kādi leņķi veidojas pie paralēlām taisnēm?»

Ja divas taisnes krusto trešā (krustotāja), veidojas astoņi leņķi. Tos
sauc pāros: kāpšļu leņķi (vienādā vietā pie abām taisnēm), iekšējie
šķērsleņķi (starp taisnēm, pretējās pusēs) un iekšējie vienpusleņķi
(starp taisnēm, vienā pusē).
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, paralelas)

TEMA = "Kādi leņķi veidojas pie paralēlām taisnēm?"

MERKIS = ("Nosauksim kāpšļu leņķus, iekšējos šķērsleņķus un iekšējos "
          "vienpusleņķus.")

SATURS = [
    Sakums("Astoņi leņķi - četri veidi pāru",
           zimejums=paralelas(),
           paraksts="Taisni c sauc par krustotāju.",
           fakti=["Pie katra krustpunkta - 4 leņķi.",
                  "Leņķus salīdzina pa pāriem.",
                  "Pāru nosaukumi palīdz ātri atrast vienādos."]),

    Doma("Trīs pāru veidi",
         "Kāpšļu leņķi atrodas vienādā vietā pie abām taisnēm (1 un 5). "
         "Iekšējie šķērsleņķi atrodas starp taisnēm krustotāja pretējās "
         "pusēs (3 un 5, 4 un 6). Iekšējie vienpusleņķi atrodas starp "
         "taisnēm krustotāja vienā pusē (4 un 5, 3 un 6).",
         soli=[
             "Iekšējie - starp taisnēm a un b; ārējie - ārpusē.",
             "Kāpšļu: viens iekšējs, otrs ārējs, vienā pusē no c.",
             "Šķērsleņķi: abi iekšēji, dažādās pusēs no c («Z» forma).",
             "Vienpusleņķi: abi iekšēji, vienā pusē no c («C» forma).",
         ],
         pieze="Kāpšļu pāri ir četri: 1 un 5, 2 un 6, 3 un 7, 4 un 8."),

    Slidnis("Pāru veidi", [
        {"v": "Kāpšļu", "teksts": "∠1 un ∠5 - vienādā vietā.",
         "zim": paralelas(radit=(1, 5))},
        {"v": "Šķērsleņķi", "teksts": "∠3 un ∠5 - «Z» forma.",
         "zim": paralelas(radit=(3, 5))},
        {"v": "Vienpusleņķi", "teksts": "∠4 un ∠5 - «C» forma.",
         "zim": paralelas(radit=(4, 5))},
        {"v": "Krustleņķi", "teksts": "∠1 un ∠3 - pie viena krustpunkta.",
         "zim": paralelas(radit=(1, 3))},
    ]),

    Varianti("Nosauc pāri", [
        {"jaut": "∠2 un ∠6",
         "opcijas": ["Kāpšļu leņķi", "Iekšējie šķērsleņķi",
                     "Iekšējie vienpusleņķi", "Blakusleņķi"],
         "pareizi": 0, "padoms": "Vienādā vietā."},
        {"jaut": "∠4 un ∠6",
         "opcijas": ["Iekšējie šķērsleņķi", "Kāpšļu leņķi",
                     "Iekšējie vienpusleņķi", "Krustleņķi"],
         "pareizi": 0, "padoms": "Starp taisnēm, pretējās pusēs."},
        {"jaut": "∠3 un ∠6",
         "opcijas": ["Iekšējie vienpusleņķi", "Kāpšļu leņķi",
                     "Iekšējie šķērsleņķi", "Krustleņķi"],
         "pareizi": 0, "padoms": "Starp taisnēm, vienā pusē."},
        {"jaut": "∠1 un ∠2",
         "opcijas": ["Blakusleņķi", "Kāpšļu leņķi", "Krustleņķi",
                     "Šķērsleņķi"],
         "pareizi": 0, "padoms": "Pie viena krustpunkta, blakus."},
        {"jaut": "∠3 un ∠7",
         "opcijas": ["Kāpšļu leņķi", "Iekšējie šķērsleņķi",
                     "Iekšējie vienpusleņķi", "Blakusleņķi"],
         "pareizi": 0, "padoms": "Vienādā vietā."},
        {"jaut": "Cik iekšējo leņķu ir pavisam?",
         "opcijas": ["4", "2", "8", "6"],
         "pareizi": 0, "padoms": "3, 4, 5, 6."},
    ], pamats=4),

    Pasaule("Ielu krustojumi",
            Varianti("", [
                {"jaut": "Divas paralēlas ielas krusto slīpa aleja. Kurš "
                         "leņķis pie otras ielas ir kā «kāpšļu» pāris "
                         "leņķim pie pirmās?",
                 "opcijas": ["Tas pats stūris - tajā pašā pusē",
                             "Pretējais stūris",
                             "Jebkurš", "Neviens"],
                 "pareizi": 0, "padoms": "Vienādā vietā."},
                {"jaut": "Kāpēc šos leņķus sauc «kāpšļu»?",
                 "opcijas": ["Tie izskatās kā kāpnes pakāpieni - viens "
                             "virs otra",
                             "Tie ir asi", "Tie ir lieli",
                             "Tā gadās"],
                 "pareizi": 0, "padoms": "Viens «uzkāpj» otram."},
            ]),
            pavediens="celojums",
            konteksts="Pilsētu kartēs paralēlas ielas un diagonālas alejas "
                      "veido tieši šos leņķu pārus.",
            kapec="Nosaukumi palīdz runāt par leņķiem precīzi."),

    Kopsavilkums([
        "Nosaucu kāpšļu leņķus.",
        "Nosaucu iekšējos šķērsleņķus («Z»).",
        "Nosaucu iekšējos vienpusleņķus («C»).",
        "Atrodu pārus zīmējumā.",
    ]),

    Majas([
        "Uzzīmē divas taisnes un krustotāju, numurē 8 leņķus.",
        "Uzraksti visus kāpšļu, šķērsleņķu un vienpusleņķu pārus.",
        "Atrodi kartē ielu krustojumu ar šādiem leņķiem.",
    ]),
]
