# -*- coding: utf-8 -*-
"""9. klase, 155. stunda: «Kas ir pieskare?»

Pieskare - taisne ar vienu kopīgu punktu. Īpašība: pieskare ir
perpendikulāra rādiusam pieskaršanās punktā; pazīme - apgrieztais
apgalvojums. Tāpēc no punkta P līdz pieskaršanās punktam T:
PT^2 = OP^2 − R^2. Stāsts: cik tālu redzams horizonts.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, uz_rinka)

TEMA = "Kas ir pieskare?"

MERKIS = ("Definēsim riņķa līnijas pieskari un formulēsim tās pazīmi un "
          "īpašību.")

_ZIM = geometrija([("O", 0, 0, -90), uz_rinka("T", 90), ("P", 12, 5, 0),
                   ("_K", -4, 5)],
                  nogriezni=["OT", "OP", ("_K", "P")], taisni=["OTP"],
                  malas=[("OT", "R = 5"), ("TP", "12"), ("OP", "13")],
                  rinki=[("O", 5)])

SATURS = [
    Sakums("Riteņa spieķis un ceļš - kādā leņķī?",
           zimejums=_ZIM,
           paraksts="Pieskare TP un rādiuss OT veido taisnu leņķi.",
           fakti=["Pieskarei un riņķa līnijai ir viens kopīgs punkts T.",
                  "Pieskare ⊥ rādiusam OT.",
                  "Tāpēc △OTP ir taisnleņķa: der Pitagors."]),

    Doma("Pieskares īpašība un pazīme",
         "Pieskare ir perpendikulāra rādiusam, kas novilkts uz "
         "pieskaršanās punktu.",
         soli=[
             "Īpašība: ja taisne ir pieskare, tā ⊥ rādiusam OT.",
             "Pazīme: ja taisne iet caur T un ⊥ OT, tā ir pieskare.",
             "Pamatojums: attālums no O līdz taisnei ir OT = R.",
         ],
         pieze="Pieskari konstruē ar pazīmi: caur T novelk perpendikulu "
               "rādiusam."),

    Paraugs("Pieskares nogrieznis",
            uzd="Punkts P ir 13 cm no centra, R = 5 cm. Cik garš ir pieskares "
                "nogrieznis PT?",
            soli=[
                ("OT ⊥ PT", "Pieskares īpašība - △OTP taisnleņķa."),
                ("PT^2 = OP^2 − OT^2 = 169 − 25 = 144", "Pitagors."),
                ("PT = 12 cm", "Sakne."),
            ],
            atbilde="12 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "OP = 10, R = 6. PT = ?", "atb": ["8"],
         "padoms": "√(100 − 36)."},
        {"jaut": "PT = 15, R = 8. OP = ?", "atb": ["17"],
         "padoms": "√(225 + 64)."},
        {"jaut": "PT = 24, OP = 25. R = ?", "atb": ["7"],
         "padoms": "√(625 − 576)."},
        {"jaut": "∠OPT = 35°. ∠POT = ?°", "atb": ["55"],
         "padoms": "∠T = 90°."},
    ]),

    Varianti("Patiess?", [
        {"jaut": "Pieskare ir perpendikulāra rādiusam pieskaršanās punktā.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 0, "padoms": "Īpašība."},
        {"jaut": "Katra taisne, kas ⊥ rādiusam, ir pieskare.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 1, "padoms": "Tai jāiet caur rādiusa galu T."},
        {"jaut": "Caur vienu riņķa līnijas punktu var novilkt tikai vienu "
                 "pieskari.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 0, "padoms": "Perpendikuls OT caur T ir viens."},
    ]),

    Pasaule("Cik tālu redzams horizonts?",
            Ievadi("", [
                {"jaut": "Zemes R ≈ 6370 km. No 0,2 km augsta torņa skatiens "
                         "pieskaras Zemei. Cik km līdz horizontam? "
                         "Noapaļo līdz veselam.",
                 "atb": ["50"], "padoms": "√(6370,2^2 − 6370^2) ≈ 50,5."},
                {"jaut": "Cilvēka acis 0,0018 km augstumā. Cik km līdz "
                         "horizontam? Noapaļo līdz veselam.",
                 "atb": ["5"], "padoms": "√(6370,0018^2 − 6370^2) ≈ 4,8."},
            ]),
            pavediens="kosmoss",
            konteksts="Skata līnija uz horizontu ir Zemes pieskare; "
                      "trijstūris centrs-acs-horizonts ir taisnleņķa.",
            kapec="Tā pati formula PT^2 = OP^2 − R^2 - tikai planētas "
                  "mērogā."),

    Kopsavilkums([
        "Zinu, ka pieskare ⊥ rādiusam pieskaršanās punktā.",
        "Atšķiru pieskares īpašību un pazīmi.",
        "Aprēķinu pieskares nogriezni ar Pitagora teorēmu.",
    ]),

    Majas([
        "Uzzīmē riņķa līniju un ar zīmēšanas trijstūri konstruē pieskari.",
        "OP = 26, R = 10. Aprēķini PT.",
        "Aprēķini, cik tālu redz no 100 m augsta skatu torņa.",
    ]),
]
