# -*- coding: utf-8 -*-
"""7. klase, 99. stunda: «Kā aprēķināt trijstūra leņķus?»

Leņķu summa ir vienādojums ar trim nezināmajiem - ja zināmas attiecības
starp leņķiem, tos var atrast visus. Stunda risina uzdevumus ar attiecību,
starpību un «reizes lielāks» un pieraksta risinājumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā aprēķināt trijstūra leņķus?"

MERKIS = ("Aprēķināsim nezināmos leņķus trijstūrī, veidojot risinājuma "
          "pierakstu.")

SATURS = [
    Sakums("Leņķi attiecas kā 2 : 3 : 4",
           zimejums=geometrija([("A", 0, 0), ("B", 7, 0), ("C", 4.72, 3.96)],
                               nogriezni=["AB", "BC", "CA"],
                               lenki=[("BAC", "2x"), ("CBA", "3x"),
                                      ("ACB", "4x")]),
           paraksts="2x + 3x + 4x = 180°.",
           fakti=["Deviņas daļas kopā - 180°.",
                  "Viena daļa - 20°.",
                  "Leņķi: 40°, 60°, 80°."]),

    Doma("Apzīmē un sastādi vienādojumu",
         "Ja leņķi saistīti ar attiecību vai starpību, vienu apzīmē ar x, "
         "pārējos izsaka ar x un sastāda vienādojumu no leņķu summas.",
         soli=[
             "Apzīmē mazāko (vai vienu) leņķi ar x.",
             "Izsaki pārējos: 2x, x + 20°, 3x ...",
             "Uzraksti: summa = 180°.",
             "Atrisini un aprēķini visus leņķus.",
             "Pārbaudi summu.",
         ]),

    Paraugs("Starpība",
            uzd="Trijstūrī ∠B par 30° lielāks nekā ∠A, ∠C divreiz lielāks "
                "nekā ∠A. Aprēķini leņķus.",
            soli=[
                ("∠A = x, ∠B = x + 30°, ∠C = 2x", "Apzīmē."),
                ("x + x + 30° + 2x = 180°", "(leņķu summa)"),
                ("4x = 150°, x = 37,5°", "Atrisina."),
                ("∠A = 37,5°, ∠B = 67,5°, ∠C = 75°", "Pārbaude: 180°."),
            ],
            atbilde="37,5°; 67,5°; 75°"),

    Ievadi("Aprēķini", [
        {"jaut": "Leņķi attiecas kā 1 : 2 : 3. Lielākais (°)?",
         "atb": ["90"], "padoms": "6 daļas, viena 30°."},
        {"jaut": "Leņķi attiecas kā 3 : 4 : 5. Mazākais (°)?",
         "atb": ["45"], "padoms": "12 daļas, viena 15°."},
        {"jaut": "∠A = 50°, ∠B = ∠C. Cik ir ∠B?",
         "atb": ["65"], "padoms": "(180 − 50) : 2."},
        {"jaut": "∠C = ∠A + ∠B. Cik ir ∠C?",
         "atb": ["90"], "padoms": "2∠C = 180."},
        {"jaut": "∠A = x, ∠B = 3x, ∠C = 5x. Cik ir x?",
         "atb": ["20"], "padoms": "9x = 180."},
        {"jaut": "Viens leņķis 40°, otrs 3 reizes lielāks par trešo. "
                 "Trešais (°)?",
         "atb": ["35"], "padoms": "4x = 140."},
    ], pamats=4),

    Zimejums("Trijstūris ar ∠C = ∠A + ∠B",
             geometrija([("A", 0, 0), ("B", 7, 0), ("C", 2, 3.16)],
                        nogriezni=["AB", "BC", "CA"],
                        taisni=["ACB"]),
             paskaidro="Ja viens leņķis ir abu pārējo summa, tas ir 90°."),

    Varianti("Pārbaudi", [
        {"jaut": "Aprēķināja leņķus 50°, 60°, 80°. Ko teikt?",
         "opcijas": ["Kļūda - summa 190°", "Pareizi", "Tas ir taisnleņķa",
                     "Nevar zināt"],
         "pareizi": 0, "padoms": "Saskaiti."},
        {"jaut": "Leņķi attiecas kā 1 : 1 : 1. Kāds trijstūris?",
         "opcijas": ["Vienādmalu (visi 60°)", "Taisnleņķa",
                     "Platleņķa", "Neeksistē"],
         "pareizi": 0, "padoms": "180 : 3."},
    ]),

    Pasaule("Jumta slīpums",
            Ievadi("", [
                {"jaut": "Jumta frontonā leņķis pie kores 110°, abi leņķi "
                         "pie pamata vienādi. Katrs (°)?",
                 "atb": ["35"], "padoms": "(180 − 110) : 2."},
                {"jaut": "Snieg daudz - jumtam jābūt stāvākam: leņķi pie "
                         "pamata 50°. Leņķis pie kores (°)?",
                 "atb": ["80"], "padoms": "180 − 100."},
                {"jaut": "Par cik grādiem kores leņķis kļuva šaurāks?",
                 "atb": ["30"], "padoms": "110 − 80."},
            ]),
            pavediens="maja",
            konteksts="Latvijā jumtus būvē stāvus - lai sniegs noslīd.",
            kapec="Leņķu summa saista kori un slīpumu."),

    Kopsavilkums([
        "Apzīmēju leņķi ar x un izsaku pārējos.",
        "Sastādu vienādojumu no leņķu summas.",
        "Risinu uzdevumus ar attiecību un starpību.",
        "Pārbaudu rezultātu ar summu 180°.",
    ]),

    Majas([
        "Leņķi attiecas kā 2 : 5 : 11. Aprēķini tos.",
        "Izdomā uzdevumu ar starpību starp leņķiem.",
        "Izmēri mājas jumta leņķi fotogrāfijā.",
    ]),
]
