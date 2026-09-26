# -*- coding: utf-8 -*-
"""7. klase, 105. stunda: «Kā aprēķināt ar ārējo leņķi?»

Ārējā leņķa īpašība saīsina daudzus aprēķinus: vienādojumā ir tikai divi
iekšējie leņķi, nevis trīs. Stunda risina uzdevumus ar attiecībām, ar
vienādsānu trijstūri un kombinētos zīmējumos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā aprēķināt ar ārējo leņķi?"

MERKIS = ("Aprēķināsim nezināmos lielumus, lietojot ārējā leņķa īpašību.")

SATURS = [
    Sakums("Viens vienādojums, nevis divi",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 3, 3.58),
                                ("_D", 9, 0)],
                               nogriezni=["AB", "BC", "CA"],
                               stari=[("B", "_D")],
                               svitras=[("AC", 1), ("BC", 1)],
                               lenki=[(("_D", "B", "C"), "130°", 2)]),
           paraksts="Vienādsānu (AC = BC), ārējais pie B - 130°.",
           fakti=["∠B = 180° − 130° = 50°.",
                  "∠A = ∠B = 50° (vienādsānu).",
                  "∠C = 130° − 50° = 80° (ārējais leņķis)."]),

    Doma("Izvēlies īsāko ceļu",
         "Ja dots ārējais leņķis, var lietot vai nu blakusleņķi (iekšējais = "
         "180° − ārējais), vai ārējā leņķa īpašību (ārējais = divu pārējo "
         "summa). Bieži otrā dod atbildi uzreiz.",
         soli=[
             "Atzīmē ārējo leņķi un abus «nesaistītos» iekšējos.",
             "Uzraksti: ārējais = ∠1 + ∠2.",
             "Ja leņķi saistīti ar attiecību - apzīmē ar x.",
             "Atrisini un pārbaudi ar leņķu summu.",
         ]),

    Paraugs("Attiecība",
            uzd="Ārējais leņķis pie C ir 120°. Iekšējie ∠A un ∠B attiecas "
                "kā 1 : 3. Aprēķini visus trīs iekšējos leņķus.",
            soli=[
                ("∠A = x, ∠B = 3x", "Apzīmē."),
                ("x + 3x = 120°", "(ārējā leņķa īpašība)"),
                ("x = 30°: ∠A = 30°, ∠B = 90°", "Atrisina."),
                ("∠C = 180° − 120° = 60°", "(blakusleņķi)"),
            ],
            atbilde="30°, 90°, 60°"),

    Ievadi("Aprēķini", [
        {"jaut": "Ārējais leņķis 110°, viens nesaistītais iekšējais 45°. "
                 "Otrs (°)?",
         "atb": ["65"], "padoms": "110 − 45."},
        {"jaut": "Ārējais 100°, abi nesaistītie vienādi. Katrs (°)?",
         "atb": ["50"], "padoms": "100 : 2."},
        {"jaut": "Vienādsānu trijstūrī ārējais pie virsotnes (starp sānu "
                 "malām) 80°. Leņķis pie pamata (°)?",
         "atb": ["40"], "padoms": "Leņķi pie pamata ir tie nesaistītie."},
        {"jaut": "Ārējais leņķis 3 reizes lielāks par savu iekšējo "
                 "blakusleņķi. Ārējais (°)?",
         "atb": ["135"], "padoms": "4 daļas = 180°."},
        {"jaut": "Ārējie leņķi pie A un B: 120° un 130°. Iekšējais ∠C (°)?",
         "atb": ["70"], "padoms": "∠A = 60, ∠B = 50."},
        {"jaut": "Taisnleņķa trijstūrī ārējais leņķis pie šaurā leņķa ir "
                 "150°. Šis šaurais leņķis (°)?",
         "atb": ["30"], "padoms": "180 − 150."},
    ], pamats=4),

    Varianti("Pārbaudi", [
        {"jaut": "Ārējais leņķis 70°, nesaistītais iekšējais 80°. "
                 "Iespējams?",
         "opcijas": ["Nē - ārējais lielāks par katru nesaistīto", "Jā",
                     "Tikai platleņķa trijstūrī"],
         "pareizi": 0, "jaukt": False, "padoms": "70 < 80."},
        {"jaut": "Kurš ceļš ātrāk dod ∠C, zinot ārējo pie B un ∠A?",
         "opcijas": ["∠C = ārējais − ∠A",
                     "Vispirms ∠B, tad summa", "Abi vienādi ātri",
                     "Nav iespējams"],
         "pareizi": 0, "padoms": "Viens solis."},
    ]),

    Pasaule("Velotrase ar pagriezieniem",
            Ievadi("", [
                {"jaut": "Trase ir trijstūris. Pagrieziens pie A ir 140° "
                         "(ārējais). Iekšējais leņķis (°)?",
                 "atb": ["40"], "padoms": "180 − 140."},
                {"jaut": "Pagrieziens pie B 110°. Iekšējais pie C (°)?",
                 "atb": ["70"], "padoms": "Iekšējie: A 40, B 70; C = 180 − 110."},
                {"jaut": "Pagrieziens pie C (°)?",
                 "atb": ["110"], "padoms": "360 − 140 − 110."},
            ]),
            pavediens="sports",
            konteksts="Riteņbraucējs pagriežas par ārējo leņķi - un visā "
                      "aplī pagriežas par 360°.",
            kapec="Ārējie leņķi ir pagriezieni."),

    Kopsavilkums([
        "Lietoju ārējā leņķa īpašību aprēķinos.",
        "Izvēlos īsāko ceļu līdz atbildei.",
        "Risinu uzdevumus ar attiecībām.",
        "Pārbaudu ar leņķu summu.",
    ]),

    Majas([
        "Ārējais leņķis 150°, iekšējie nesaistītie attiecas 2 : 3. Atrodi "
        "tos.",
        "Uzraksti uzdevumu ar vienādsānu trijstūra ārējo leņķi.",
        "Uzzīmē velotrasi un aprēķini pagriezienus.",
    ]),
]
