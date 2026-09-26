# -*- coding: utf-8 -*-
"""7. klase, 97. stunda: «Cik ir trijstūra leņķu summa?»

Jebkura trijstūra leņķu summa ir 180°. Stunda to atklāj praktiski:
noplēš trijstūra stūrus un saliek tos kopā - tie veido izstieptu leņķi.
Tad to pārbauda ar mērījumiem un spriedumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         geometrija, lenkis)

TEMA = "Cik ir trijstūra leņķu summa?"

MERKIS = ("Praktiski un ar spriedumu iegūsim, ka trijstūra leņķu summa ir "
          "180°.")

SATURS = [
    Sakums("Noplēs stūrus - un saliec kopā",
           zimejums=lenkis([(0, ""), (50, ""), (120, ""), (180, "")],
                           loki=[(0, 50, "∠A"), (50, 120, "∠B"),
                                 (120, 180, "∠C")]),
           paraksts="Trīs stūri kopā veido izstieptu leņķi - 180°.",
           fakti=["Jebkurš papīra trijstūris - vienāds rezultāts.",
                  "Mazs vai liels, šaurs vai plats - vienmēr 180°.",
                  "Tā ir viena no svarīgākajām teorēmām."]),

    Petijums("Stūru eksperiments",
             ["Izgriez no papīra jebkuru trijstūri.",
              "Iekrāso visus trīs stūrus un noplēs tos.",
              "Saliec stūrus ar virsotnēm vienā punktā, malas kopā.",
              "Ko veido ārējās malas? Pārbaudi ar lineālu.",
              "Atkārto ar citu formu trijstūri."],
             vajag="papīrs, šķēres, krāsainais zīmulis, lineāls",
             secinajums="Trīs leņķi kopā vienmēr veido taisni - izstieptu "
                         "leņķi 180°."),

    Doma("∠A + ∠B + ∠C = 180°",
         "Jebkura trijstūra iekšējo leņķu summa ir 180°. Tāpēc, zinot divus "
         "leņķus, trešo aprēķina: ∠C = 180° − ∠A − ∠B.",
         soli=[
             "Saskaiti divus zināmos leņķus.",
             "Atņem summu no 180°.",
             "Pārbaudi: visu trīs summa ir 180°.",
         ],
         pieze="Mērot ar transportieri, summa var iznākt 178° vai 182° - tā "
               "ir mērīšanas kļūda. Pierādījums (nākamā stunda) dod tieši "
               "180°."),

    Paraugs("Aprēķini trešo leņķi",
            uzd="Trijstūrī ∠A = 48°, ∠B = 77°. Aprēķini ∠C.",
            soli=[
                ("∠A + ∠B + ∠C = 180°", "(leņķu summa)"),
                ("∠C = 180° − 48° − 77°", "Izsaka."),
                ("∠C = 55°", "Aprēķina."),
            ],
            atbilde="∠C = 55°"),

    Zimejums("Trijstūris ar leņķiem",
             geometrija([("A", 0, 0), ("B", 7, 0), ("C", 2.7, 3)],
                        nogriezni=["AB", "BC", "CA"],
                        lenki=[("BAC", "48°"), ("CBA", "35°"),
                               ("ACB", "?")]),
             paskaidro="? = 180° − 48° − 35° = 97°."),

    Ievadi("Aprēķini", [
        {"jaut": "∠A = 60°, ∠B = 60°. ∠C = ?",
         "atb": ["60"], "padoms": "180 − 120."},
        {"jaut": "∠A = 90°, ∠B = 35°. ∠C = ?",
         "atb": ["55"], "padoms": "180 − 125."},
        {"jaut": "∠A = 110°, ∠B = 25°. ∠C = ?",
         "atb": ["45"], "padoms": "180 − 135."},
        {"jaut": "Visi trīs leņķi vienādi. Katrs = ?",
         "atb": ["60"], "padoms": "180 : 3."},
    ]),

    Varianti("Iespējams?", [
        {"jaut": "Trijstūris ar leņķiem 90°, 90°, 0°",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "Leņķis nevar būt 0°."},
        {"jaut": "Trijstūris ar diviem taisniem leņķiem",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "Trešajam paliktu 0°."},
        {"jaut": "Trijstūris ar leņķiem 100°, 50°, 30°",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Summa 180°."},
        {"jaut": "Trijstūris ar leņķiem 70°, 70°, 50°",
         "opcijas": ["Nē", "Jā"], "pareizi": 0, "jaukt": False,
         "padoms": "Summa 190°."},
    ], pamats=4),

    Pasaule("Bermudu trijstūris",
            Ievadi("", [
                {"jaut": "Kartē Bermudu trijstūra leņķi: pie Maiami 57°, pie "
                         "Bermudām 63°. Leņķis pie Puertoriko (°)?",
                 "atb": ["60"], "padoms": "180 − 120."},
                {"jaut": "Vai tas ir gandrīz vienādmalu? Raksti «jā» vai "
                         "«nē».",
                 "atb": ["jā", "ja"], "padoms": "Visi ap 60°."},
                {"jaut": "Cik grādu starpība starp lielāko un mazāko leņķi?",
                 "atb": ["6"], "padoms": "63 − 57."},
            ]),
            pavediens="celojums",
            konteksts="Bermudu trijstūris kartē ir gandrīz vienādmalu "
                      "trijstūris ar ~1600 km malām.",
            kapec="Leņķu summa der arī lieliem trijstūriem kartē."),

    Kopsavilkums([
        "Zinu, ka trijstūra leņķu summa ir 180°.",
        "Pārbaudu to eksperimentā.",
        "Aprēķinu trešo leņķi.",
        "Pamatoju, kāpēc trijstūrim nevar būt divi taisni leņķi.",
    ]),

    Majas([
        "Izgriez 2 dažādus trijstūrus un saliec stūrus.",
        "Izmēri leņķus 3 trijstūros un saskaiti.",
        "Paskaidro, kāpēc summa neiznāk tieši 180°.",
    ]),
]
