# -*- coding: utf-8 -*-
"""4. klase, 68. stunda: «Vai apgalvojums par leņķiem ir patiess?»

4.3. temata pēdējā stunda pirms PD. Spriešana: apgalvojumu pārbauda ar
zīmējumu vai pretpiemēru. Viens pretpiemērs pietiek, lai apgalvojums
kristu - bet viens piemērs nepierāda, ka tas vienmēr patiess.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis)

TEMA = "Vai apgalvojums par leņķiem ir patiess?"

MERKIS = ("Noteiksim apgalvojuma par leņķiem patiesumu un pamatosim savu "
          "spriedumu.")

SATURS = [
    Sakums("«Divi šauri leņķi kopā vienmēr ir šaurs.» Taisnība?",
           zimejums=lenkis([(0, ""), (60, ""), (120, "")],
                           loki=[(0, 60, "60°"), (60, 120, "60°")]),
           paraksts="60° + 60° = 120° - plats! Apgalvojums aplams.",
           fakti=["Viens pretpiemērs pietiek, lai apgalvojums kristu.",
                  "Pretpiemērs - gadījums, kad apgalvojums nav spēkā."]),

    Doma("Meklē pretpiemēru",
         "Lai pārbaudītu «vienmēr» apgalvojumu, meklē gadījumu, kad tas nav "
         "spēkā; ja tādu nevar atrast un var paskaidrot kāpēc - tas patiess.",
         soli=[
             "Izlasi apgalvojumu un atrodi vārdu «vienmēr» vai «visi».",
             "Mēģini uzzīmēt gadījumu, kad tas nav spēkā.",
             "Ja izdodas - apgalvojums aplams.",
             "Ja neizdodas - meklē paskaidrojumu, kāpēc tas vienmēr ir tā.",
         ],
         pieze="«Taisns leņķis vienmēr ir 90°» - patiess pēc definīcijas."),

    Paraugs("Pārbaudi apgalvojumu",
            uzd="«Ja leņķa malas pagarina, leņķis kļūst lielāks.»",
            soli=[
                ("izmēra leņķi: 40°", None),
                ("pagarina malas, izmēra: 40°", "Pretpiemērs."),
            ],
            atbilde="aplams"),

    Varianti("Patiess vai aplams?", [
        {"jaut": "Plats leņķis vienmēr ir lielāks par taisnu.",
         "opcijas": ["patiess", "aplams"], "pareizi": 0,
         "padoms": "Pēc definīcijas > 90°."},
        {"jaut": "Divi taisni leņķi kopā veido izstieptu leņķi.",
         "opcijas": ["patiess", "aplams"], "pareizi": 0,
         "padoms": "90 + 90 = 180."},
        {"jaut": "Divi plati leņķi kopā ir mazāki par 180°.",
         "opcijas": ["aplams", "patiess"], "pareizi": 0,
         "padoms": "100° + 100° = 200°."},
        {"jaut": "Katrs kvadrāta leņķis ir taisns.",
         "opcijas": ["patiess", "aplams"], "pareizi": 0,
         "padoms": "Kvadrāts ir taisnstūris."},
        {"jaut": "Šaurs leņķis var būt 95°.",
         "opcijas": ["aplams", "patiess"], "pareizi": 0,
         "padoms": "Šaurs < 90°."},
        {"jaut": "Trijstūrim var būt divi plati leņķi.",
         "opcijas": ["aplams", "patiess"], "pareizi": 0,
         "padoms": "Pamēģini uzzīmēt - malas neaizvērsies."},
    ], pamats=4),

    Zimejums("Pretpiemērs zīmējumā",
             lenkis([(0, ""), (100, ""), (200, "")],
                    loki=[(0, 100, "100°"), (100, 200, "100°")]),
             paskaidro="Divi plati leņķi kopā - 200°, vairāk nekā izstiepts.",
             ievads="Apgalvojums «divi plati leņķi kopā < 180°» krīt."),

    Ievadi("Atrodi pretpiemēru", [
        {"jaut": "«Divi šauri leņķi kopā ir šaurs.» Uzraksti otru leņķi, lai "
                 "ar 50° kopā sanāktu taisns.", "atb": ["40"],
         "padoms": "90 − 50."},
        {"jaut": "Cik grādu jāpieskaita 50°, lai kopā būtu plats leņķis 130°?",
         "atb": ["80"], "padoms": "130 − 50 - un 80° ir šaurs!"},
        {"jaut": "Divi vienādi šauri leņķi kopā - 170°. Cik katrs?",
         "atb": ["85"], "padoms": "170 : 2."},
        {"jaut": "Trīs taisni leņķi kopā - cik grādu?", "atb": ["270"],
         "padoms": "3 · 90."},
    ]),

    Pasaule("Mītu grāvēji",
            Varianti("", [
                {"jaut": "Mīts: «Lielākā pica - lielāki gabala leņķi.» Picu "
                         "sagriež 8 daļās. Kāds leņķis katram gabalam?",
                 "opcijas": ["45° neatkarīgi no izmēra",
                             "atkarīgs no picas izmēra", "90°"],
                 "pareizi": 0, "padoms": "360 : 8, izmērs nav svarīgs."},
                {"jaut": "Mīts: «Pulksteņa rādītāji plkst. 3 un plkst. 9 "
                         "veido dažādus leņķus.»",
                 "opcijas": ["aplams - abi ir 90°", "patiess",
                             "atkarīgs no pulksteņa"], "pareizi": 0,
                 "padoms": "Abos gadījumos ceturtdaļa apļa."},
                {"jaut": "Mīts: «Lielam trijstūrim leņķi lielāki.»",
                 "opcijas": ["aplams", "patiess"], "pareizi": 0,
                 "padoms": "Palielinot figūru, leņķi nemainās."},
            ]),
            pavediens="skola",
            konteksts="Daudz «acīmredzamu» apgalvojumu ir aplami - matemātiķi "
                      "tos pārbauda ar pretpiemēriem.",
            kapec="Pretpiemērs ir ātrākais veids, kā atmaskot kļūdu."),

    Kopsavilkums([
        "Pārbaudu apgalvojumu par leņķiem ar zīmējumu.",
        "Atrodu pretpiemēru aplamam apgalvojumam.",
        "Pamatoju patiesu apgalvojumu ar definīciju.",
        "Esmu gatavs 4.3. temata pārbaudes darbam.",
    ]),

    Majas([
        "Izdomā vienu patiesu un vienu aplamu apgalvojumu par leņķiem.",
        "Palūdz mājiniekam atrast pretpiemēru tavam aplamam apgalvojumam.",
        "Atkārto: ∥, ⊥, leņķa veidi, transportieris.",
    ], ievads="Nākamajā stundā - pārbaudes darbs par 4.3. tematu."),
]
