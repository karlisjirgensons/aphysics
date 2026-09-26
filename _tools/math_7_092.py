# -*- coding: utf-8 -*-
"""7. klase, 92. stunda: «Kā pārbaudīt, vai taisnes ir paralēlas?»

Paralēlas taisnes nekrustojas, bet to nevar pārbaudīt, ejot līdz
bezgalībai. Praktiski paralēlas taisnes konstruē un pārbauda ar stūreni:
divas taisnes, kas perpendikulāras vienai un tai pašai taisnei, ir
paralēlas.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā pārbaudīt, vai taisnes ir paralēlas?"

MERKIS = ("Konstruēsim paralēlas taisnes un pārbaudīsim paralelitāti.")

_PERP = geometrija([("_a1", 0, 0), ("_a2", 0, 5), ("_b1", 5, 0),
                    ("_b2", 5, 5), ("_c1", -1, 1), ("_c2", 6, 1),
                    ("_x", 0, 1), ("_y", 5, 1)],
                   taisnes=[("_a1", "_a2"), ("_b1", "_b2"), ("_c1", "_c2")],
                   taisni=[("_a2", "_x", "_c2"), ("_b2", "_y", "_c2")],
                   uzraksti=[(-0.5, 5, "a"), (5.5, 5, "b"), (6.3, 1.4, "c")])

SATURS = [
    Sakums("Sliedes nesatiekas nekad",
           zimejums=_PERP,
           paraksts="a ⊥ c un b ⊥ c, tāpēc a ∥ b.",
           fakti=["Līdz bezgalībai neaizbrauksi, lai pārbaudītu.",
                  "Bet var pārbaudīt leņķus ar trešo taisni.",
                  "Divas perpendikulāras vienai taisnei ir paralēlas."]),

    Doma("Paralelitāti pārbauda ar leņķiem",
         "Divas taisnes plaknē sauc par paralēlām, ja tās nekrustojas. "
         "Ja divas taisnes ir perpendikulāras vienai un tai pašai trešajai "
         "taisnei, tās ir paralēlas.",
         soli=[
             "Novelc trešo taisni c, kas krusto abas.",
             "Ar stūreni pārbaudi leņķus pie krustpunktiem.",
             "Ja abi ir 90° - taisnes ir paralēlas.",
             "Konstruējot: novelc divus perpendikulus pret vienu taisni.",
         ],
         pieze="Caur punktu ārpus taisnes var novilkt tikai vienu taisni, "
               "kas paralēla dotajai - tā ir Eiklīda aksioma."),

    Petijums("Konstruē paralēlu taisni ar stūreni",
             ["Uzzīmē taisni a un punktu P ārpus tās.",
              "Pieliec lineālu gar a, stūreni - pie lineāla.",
              "Slidini stūreni gar lineālu līdz punktam P.",
              "Novelc taisni caur P gar stūreņa malu.",
              "Pārbaudi: attālumi starp taisnēm divās vietās vienādi?"],
             vajag="lineāls, stūrenis, zīmulis",
             secinajums="Stūrenis saglabā vienu leņķi pret lineālu - tāpēc "
                         "jaunā taisne ir paralēla."),

    Paraugs("Pamato paralelitāti",
            uzd="Taisnstūrī ABCD pamato, ka AB ∥ CD.",
            soli=[
                ("AB ⊥ BC", "(taisnstūra leņķis B)"),
                ("CD ⊥ BC", "(taisnstūra leņķis C)"),
                ("AB ∥ CD", "(abas perpendikulāras BC)"),
            ],
            atbilde="AB ∥ CD"),

    Varianti("Paralēlas vai nē?", [
        {"jaut": "a ⊥ c, b ⊥ c.",
         "opcijas": ["a ∥ b", "a ⊥ b", "Krustojas", "Nevar zināt"],
         "pareizi": 0, "padoms": "Divas perpendikulāras vienai."},
        {"jaut": "a ∥ b, c ⊥ a.",
         "opcijas": ["c ⊥ b", "c ∥ b", "c = b", "Nevar zināt"],
         "pareizi": 0, "padoms": "Perpendikulārs arī otrai."},
        {"jaut": "Cik taisnes caur punktu P ir paralēlas taisnei a?",
         "opcijas": ["Tieši viena", "Divas", "Bezgalīgi daudz", "Neviena"],
         "pareizi": 0, "padoms": "Aksioma."},
        {"jaut": "Attālums starp taisnēm vienā vietā 3 cm, citā 3,5 cm. "
                 "Vai tās paralēlas?",
         "opcijas": ["Nē", "Jā", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Paralēlām attālums visur vienāds."},
    ], pamats=4),

    Pasaule("Stāvvietas līnijas",
            Varianti("", [
                {"jaut": "Stāvvietas līnijas krāso perpendikulāri ceļa "
                         "malai. Kāpēc tās būs paralēlas?",
                 "opcijas": ["Visas perpendikulāras vienai taisnei",
                             "Krāsotājs ir precīzs", "Tā ir tradīcija",
                             "Tās nebūs paralēlas"],
                 "pareizi": 0, "padoms": "Pazīme."},
                {"jaut": "Starp līnijām 2,5 m. Cik vietu ietilps 40 m?",
                 "opcijas": ["16", "40", "10", "25"],
                 "pareizi": 0, "padoms": "40 : 2,5."},
                {"jaut": "Ja viena līnija ir 85° leņķī, kas notiks?",
                 "opcijas": ["Vietas vienā galā šaurākas",
                             "Nekas", "Visas vietas lielākas",
                             "Līnijas būs paralēlas"],
                 "pareizi": 0, "padoms": "Līnijas saiet kopā."},
            ]),
            pavediens="celojums",
            konteksts="Ceļu krāsotāji līnijas atliek no vienas bāzes līnijas "
                      "ar vienādu leņķi.",
            kapec="Viens leņķis - visas līnijas paralēlas."),

    Kopsavilkums([
        "Zinu paralēlu taišņu definīciju.",
        "Konstruēju paralēlu taisni ar stūreni un lineālu.",
        "Pamatoju: divas perpendikulāras vienai - paralēlas.",
        "Zinu, ka caur punktu iet tikai viena paralēla taisne.",
    ]),

    Majas([
        "Konstruē 3 paralēlas taisnes ar 2 cm atstarpi.",
        "Atrodi mājās 3 paralēlu taišņu pārus.",
        "Paskaidro, kā pārbaudīt, vai grāmatplaukts ir taisns.",
    ]),
]
