# -*- coding: utf-8 -*-
"""7. klase, 74. stunda: «Kā trijstūrī sauc katru elementu?»

Trijstūrim ir trīs virsotnes, trīs malas un trīs leņķi. Katrai malai ir
pretleņķis un divi pieleņķi; katram leņķim - pretmala un divas piemalas.
Šie vārdi būs vajadzīgi vienādības pazīmēs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā trijstūrī sauc katru elementu?"

MERKIS = ("Lietosim jēdzienus mala, leņķis, pretmala, piemala, pretleņķis "
          "un pieleņķi.")

_ABC = geometrija([("A", 0, 0), ("B", 7, 0), ("C", 2, 4)],
                  nogriezni=["AB", "BC", "CA"],
                  lenki=[("CAB", "∠A"), ("ABC", "∠B"), ("BCA", "∠C")],
                  malas=[("AB", "c"), ("BC", "a"), ("CA", "b")])

SATURS = [
    Sakums("Trīs virsotnes, trīs malas, trīs leņķi",
           zimejums=_ABC,
           paraksts="Mala a ir pretī virsotnei A, b - pretī B, c - pretī C.",
           fakti=["Mazais burts malai - tas pats, kas pretējai virsotnei.",
                  "Tā uzreiz redz, kurš leņķis ir pretī kurai malai."]),

    Doma("Pretī un pie",
         "Trijstūrī katram leņķim ir pretmala (mala, kas nesatur leņķa "
         "virsotni) un divas piemalas (leņķa malas). Katrai malai ir "
         "pretleņķis un divi pieleņķi (leņķi tās galos).",
         soli=[
             "∠A piemalas: AB un AC; pretmala: BC.",
             "Malas AB pieleņķi: ∠A un ∠B; pretleņķis: ∠C.",
             "Vārds «pie» - pieskaras; «pret» - pretējā pusē.",
             "Apzīmē: △ABC, malas a, b, c, leņķi ∠A, ∠B, ∠C.",
         ],
         pieze="Pēc šiem vārdiem formulē trijstūru vienādības pazīmes: "
               "divas malas un leņķis starp tām."),

    Paraugs("Nosauc elementus",
            uzd="△KLM. Nosauc ∠L piemalas un pretmalu un malas KM "
                "pieleņķus.",
            soli=[
                ("∠L piemalas: LK un LM", "Iziet no L."),
                ("∠L pretmala: KM", "Bez L."),
                ("KM pieleņķi: ∠K un ∠M", "Malas galos."),
            ],
            atbilde="LK, LM; KM; ∠K un ∠M"),

    Varianti("Nosauc", [
        {"jaut": "△ABC. Kura mala ir pretmala ∠B?",
         "opcijas": ["AC", "AB", "BC", "Visas"],
         "pareizi": 0, "padoms": "Bez burta B."},
        {"jaut": "△ABC. Kurš leņķis ir malas AB pretleņķis?",
         "opcijas": ["∠C", "∠A", "∠B", "Nav"],
         "pareizi": 0, "padoms": "Trešā virsotne."},
        {"jaut": "△PQR. Kuri ir malas QR pieleņķi?",
         "opcijas": ["∠Q un ∠R", "∠P un ∠Q", "∠P", "∠P un ∠R"],
         "pareizi": 0, "padoms": "Galos."},
        {"jaut": "△PQR. Kuras ir ∠P piemalas?",
         "opcijas": ["PQ un PR", "QR", "PQ un QR", "PR un QR"],
         "pareizi": 0, "padoms": "Iziet no P."},
    ], pamats=4),

    Ievadi("Saskaiti", [
        {"jaut": "Cik elementu (malas un leņķi) ir trijstūrim kopā?",
         "atb": ["6"], "padoms": "3 + 3."},
        {"jaut": "Cik pieleņķu ir vienai malai?",
         "atb": ["2"], "padoms": "Divos galos."},
        {"jaut": "△ABC: a = 5, b = 7, c = 9. Kurš leņķis ir pretī garākajai "
                 "malai? Raksti burtu.",
         "atb": ["C"], "padoms": "c pretī C.", "tastatura": "text"},
    ]),

    Pasaule("Jumta kopne",
            Varianti("", [
                {"jaut": "Jumta kopne △ABC, AB - pamats (griesti), C - "
                         "kore. Kuri leņķi ir pamata pieleņķi?",
                 "opcijas": ["∠A un ∠B", "∠C", "∠A un ∠C", "Visi"],
                 "pareizi": 0, "padoms": "Pamata galos."},
                {"jaut": "Kurš leņķis ir pie kores?",
                 "opcijas": ["∠C - pamata pretleņķis", "∠A", "∠B",
                             "Nav tāda"],
                 "pareizi": 0, "padoms": "Pretī pamatam."},
                {"jaut": "Jumta slīpums ir leņķis starp slīpo malu un "
                         "pamatu. Kurš tas ir kreisajā pusē?",
                 "opcijas": ["∠A", "∠C", "∠B", "Nevar zināt"],
                 "pareizi": 0, "padoms": "Starp AC un AB."},
            ]),
            pavediens="maja",
            konteksts="Būvinženieri rasējumos lieto tieši šos vārdus: pamats, "
                      "pieleņķi, pretleņķis.",
            kapec="Precīzi vārdi - bez pārpratumiem būvlaukumā."),

    Kopsavilkums([
        "Nosaucu trijstūra malas un leņķus.",
        "Atrodu leņķa pretmalu un piemalas.",
        "Atrodu malas pretleņķi un pieleņķus.",
        "Lietoju apzīmējumus a, b, c un ∠A, ∠B, ∠C.",
    ]),

    Majas([
        "Uzzīmē △XYZ un uzraksti visus pieleņķus un pretleņķus.",
        "Atrodi mājās trīsstūrveida priekšmetu un nosauc tā elementus.",
        "Uzraksti 3 jautājumus par elementiem un atbildi.",
    ]),
]
