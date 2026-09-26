# -*- coding: utf-8 -*-
"""7. klase, 101. stunda: «Kādi leņķi ir vienādsānu trijstūrī?»

Apvienojot leņķu summu ar vienādsānu trijstūra īpašību (leņķi pie pamata
vienādi), no viena leņķa var aprēķināt visus. Svarīgi - noskaidrot, vai
dotais leņķis ir pie pamata vai virsotnē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kādi leņķi ir vienādsānu trijstūrī?"

MERKIS = ("Lietosim leņķu summu un vienādsānu trijstūra īpašības kopā.")

_VS = geometrija([("A", 0, 0), ("C", 6, 0), ("B", 3, 3.6)],
                 nogriezni=["AB", "BC", "CA"],
                 svitras=[("AB", 1), ("BC", 1)],
                 lenki=[("CAB", "α", 2), ("BCA", "α", 2), ("ABC", "β")])

SATURS = [
    Sakums("Viens leņķis - visi trīs",
           zimejums=_VS,
           paraksts="2α + β = 180°.",
           fakti=["Leņķi pie pamata α ir vienādi.",
                  "Virsotnes leņķis β.",
                  "Zinot vienu, aprēķina abus pārējos."]),

    Doma("2α + β = 180°",
         "Vienādsānu trijstūrī leņķi pie pamata ir vienādi (α), tāpēc "
         "2α + β = 180°, kur β ir virsotnes leņķis. Ja dots β, tad "
         "α = (180° − β) : 2; ja dots α, tad β = 180° − 2α.",
         soli=[
             "Noskaidro: dotais leņķis ir pie pamata vai virsotnē?",
             "Ja virsotnē - atņem no 180° un dali ar 2.",
             "Ja pie pamata - otrs pie pamata tāds pats, virsotne - "
             "180° − 2α.",
             "Ja nav zināms, kurš tas ir, - apskati abus gadījumus.",
         ],
         pieze="Leņķis pie pamata vienmēr ir šaurs: 2α < 180°."),

    Paraugs("Divi gadījumi",
            uzd="Vienādsānu trijstūrī viens leņķis ir 40°. Aprēķini pārējos.",
            soli=[
                ("1) 40° - virsotnē: α = (180° − 40°) : 2 = 70°",
                 "Leņķi 40°, 70°, 70°."),
                ("2) 40° - pie pamata: otrs 40°, β = 180° − 80° = 100°",
                 "Leņķi 40°, 40°, 100°."),
                ("Abi gadījumi iespējami", "Divas atbildes."),
            ],
            atbilde="70° un 70° vai 40° un 100°"),

    Ievadi("Aprēķini", [
        {"jaut": "Virsotnes leņķis 50°. Leņķis pie pamata (°)?",
         "atb": ["65"], "padoms": "(180 − 50) : 2."},
        {"jaut": "Leņķis pie pamata 35°. Virsotnes leņķis (°)?",
         "atb": ["110"], "padoms": "180 − 70."},
        {"jaut": "Viens leņķis 100°. Cik grādu ir katrs no pārējiem?",
         "atb": ["40"], "padoms": "100° var būt tikai virsotnē."},
        {"jaut": "Taisnleņķa vienādsānu trijstūris. Šaurais leņķis (°)?",
         "atb": ["45"], "padoms": "90 : 2."},
        {"jaut": "Vienādsānu trijstūrī viens leņķis 60°. Pārējie (°)?",
         "atb": ["60"], "padoms": "Abos gadījumos - vienādmalu."},
    ], pamats=3),

    Varianti("Iespējams?", [
        {"jaut": "Vienādsānu trijstūrim leņķis pie pamata 95°",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "95 · 2 > 180."},
        {"jaut": "Vienādsānu trijstūrim virsotnes leņķis 170°",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Pie pamata pa 5°."},
        {"jaut": "Vienādsānu trijstūrim visi leņķi dažādi",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "Divi vienādi."},
    ]),

    Zimejums("Vienādsānu taisnleņķa trijstūris",
             geometrija([("A", 0, 0), ("C", 4, 0), ("B", 0, 4)],
                        nogriezni=["AB", "BC", "CA"],
                        svitras=[("AB", 1), ("AC", 1)],
                        taisni=["BAC"],
                        lenki=[("ACB", "45°"), ("CBA", "45°")]),
             paskaidro="Kvadrāta puse - pa diagonāli."),

    Pasaule("Vienādmalu trijstūru flīzes",
            Ievadi("", [
                {"jaut": "Flīzes ir vienādmalu trijstūri. Cik flīzes "
                         "satiekas vienā punktā, aizpildot 360°?",
                 "atb": ["6"], "padoms": "360 : 60."},
                {"jaut": "Vienādsānu flīzes ar virsotnes leņķi 36°. Cik "
                         "tās satiekas virsotnēs vienā punktā?",
                 "atb": ["10"], "padoms": "360 : 36."},
                {"jaut": "Šīs flīzes leņķi pie pamata (°)?",
                 "atb": ["72"], "padoms": "(180 − 36) : 2."},
            ]),
            pavediens="maja",
            konteksts="Flīžu raksti bez spraugām iespējami tikai, ja leņķi "
                      "punktā kopā dod 360°.",
            kapec="Leņķi nosaka, vai raksts aizpilda plakni."),

    Kopsavilkums([
        "Lietoju 2α + β = 180° vienādsānu trijstūrī.",
        "Nosaku, vai dotais leņķis ir pie pamata vai virsotnē.",
        "Apskatu abus gadījumus, ja nav zināms.",
        "Zinu, ka leņķis pie pamata vienmēr ir šaurs.",
    ]),

    Majas([
        "Vienādsānu trijstūrī viens leņķis 70°. Atrodi abus variantus.",
        "Pārloki kvadrātveida papīru pa diagonāli un izmēri leņķus.",
        "Izdomā flīzes, kuras var salikt ap vienu punktu.",
    ]),
]
