# -*- coding: utf-8 -*-
"""9. klase, 156. stunda: «Kādas ir pieskaru nogriežņu īpašības?»

No viena punkta P vilktie pieskaru nogriežņi ir vienādi: △OAP ≅ △OBP
(kopīga hipotenūza OP, OA = OB, taisni leņķi). OP ir leņķa APB bisektrise,
un četrstūrī OAPB ∠AOB + ∠APB = 180°. Tas pats dod ievilktās riņķa līnijas
pieskaršanās nogriežņus trijstūra malās.
"""

import math

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, uz_rinka)

TEMA = "Kādas ir pieskaru nogriežņu īpašības?"

MERKIS = ("Pierādīsim, ka no viena punkta vilktie pieskaru nogriežņi ir "
          "vienādi.")

_G = math.degrees(math.acos(5.0 / 13.0))


def _pieskares(lenki=(), izcelti=()):
    return geometrija([("O", 0, 0, 180), ("P", 13, 0, 0),
                       uz_rinka("A", _G), uz_rinka("B", -_G)],
                      nogriezni=["PA", "PB", "OA", "OB", "OP"],
                      izcelti=list(izcelti), taisni=["OAP", "OBP"],
                      svitras=[("PA", 1), ("PB", 1)], lenki=list(lenki),
                      rinki=[("O", 5)])


SATURS = [
    Sakums("Divas pieskares no viena punkta - kura garāka?",
           zimejums=_pieskares(),
           paraksts="PA un PB - pieskaru nogriežņi no punkta P.",
           fakti=["PA = PB - vienmēr.",
                  "OP dala leņķi APB uz pusēm.",
                  "∠AOB + ∠APB = 180°."]),

    Doma("Pieskaru nogriežņi",
         "No viena punkta vilktie pieskaru nogriežņi ir vienādi.",
         soli=[
             "OA ⊥ PA un OB ⊥ PB - pieskares īpašība.",
             "OA = OB - rādiusi; OP - kopīga hipotenūza.",
             "△OAP ≅ △OBP pēc hipotenūzas un katetes.",
             "Tātad PA = PB un ∠APO = ∠BPO.",
         ],
         pieze="Četrstūrī OAPB divi leņķi ir 90°, tāpēc pārējie divi kopā "
               "dod 180°."),

    Paraugs("Leņķis starp pieskarēm",
            uzd="No punkta P novilktas pieskares PA un PB; ∠APB = 50°. Atrodi "
                "∠AOB.",
            soli=[
                ("∠OAP = ∠OBP = 90°", "Pieskares ⊥ rādiusiem."),
                ("∠AOB = 360° − 90° − 90° − 50°", "Četrstūra leņķu summa."),
                ("∠AOB = 130°", "Aprēķins."),
            ],
            atbilde="130°"),

    Ievadi("Aprēķini", [
        {"jaut": "PA = 7 cm. PB = ? cm", "atb": ["7"],
         "padoms": "Nogriežņi vienādi."},
        {"jaut": "∠APB = 60°. ∠AOB = ?°", "atb": ["120"],
         "padoms": "180 − 60."},
        {"jaut": "∠APB = 60°. ∠APO = ?°", "atb": ["30"],
         "padoms": "OP ir bisektrise."},
        {"jaut": "R = 5, OP = 13. PA + PB = ?", "atb": ["24"],
         "padoms": "PA = 12."},
    ]),

    Ievadi("Trijstūrī ievilkta riņķa līnija", [
        {"jaut": "Ievilktā riņķa līnija pieskaras AB punktā K, AC punktā M. "
                 "AK = 4. AM = ?", "atb": ["4"],
         "padoms": "Pieskares no punkta A."},
        {"jaut": "AB = 7, BC = 8, AC = 9. Pieskaršanās punkts K uz AB. "
                 "AK = ?", "atb": ["4"],
         "padoms": "AK = (7 + 9 − 8) : 2."},
        {"jaut": "Pieskaru nogriežņi no virsotnēm: 2, 3 un 5. Perimetrs?",
         "atb": ["20"], "padoms": "Katrs nogrieznis ir divreiz."},
    ]),

    Varianti("Pamato", [
        {"jaut": "Kāpēc △OAP ≅ △OBP?",
         "opcijas": ["kopīga hipotenūza OP un OA = OB",
                     "abi ir vienādmalu", "PA ∥ PB", "OA ⊥ OB"],
         "pareizi": 0, "padoms": "Taisnleņķa trijstūru vienādība."},
        {"jaut": "Kāds ir leņķis starp OP un AB?",
         "opcijas": ["90°", "45°", "60°", "atkarīgs no R"],
         "pareizi": 0, "padoms": "△APB vienādsānu, OP - bisektrise."},
    ]),

    Pasaule("Bumba istabas stūrī",
            Ievadi("", [
                {"jaut": "Bumba (R = 11 cm) guļ stūrī un pieskaras abām "
                         "sienām. Cik cm no stūra ir katrs pieskaršanās "
                         "punkts?", "atb": ["11"],
                 "padoms": "OAPB ir kvadrāts."},
                {"jaut": "Cik cm no stūra līdz bumbas centram? Noapaļo līdz "
                         "veselam.", "atb": ["16"],
                 "padoms": "Kvadrāta diagonāle 11√2 ≈ 15,6."},
            ]),
            pavediens="sports",
            konteksts="Sienas no augšas izskatās kā divas pieskares no stūra "
                      "punkta P; starp sienām 90°.",
            kapec="Vienādi pieskaru nogriežņi - bumba ir vienādi tālu no "
                  "stūra pa abām sienām."),

    Kopsavilkums([
        "Pierādu, ka pieskaru nogriežņi no viena punkta ir vienādi.",
        "Zinu, ka OP ir leņķa starp pieskarēm bisektrise.",
        "Aprēķinu leņķus un nogriežņus ar pieskarēm.",
    ]),

    Majas([
        "Uzraksti pierādījumu PA = PB ar zīmējumu un pamatojumiem.",
        "∠AOB = 110°. Atrodi leņķi starp pieskarēm.",
        "Trijstūrī 5, 6, 7 atrodi pieskaru nogriežņus no katras virsotnes.",
    ]),
]
