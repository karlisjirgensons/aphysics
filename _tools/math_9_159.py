# -*- coding: utf-8 -*-
"""9. klase, 159. stunda: «Ap kuriem četrstūriem var apvilkt riņķa līniju?»

Ievilktā četrstūrī pretējo leņķu summa ir 180°: katrs ir puse no loka, uz
kura balstās, un abi loki kopā ir 360°. Apgrieztais arī ir patiess, tāpēc
ap taisnstūri un vienādsānu trapeci riņķa līniju var apvilkt, ap rombu
(ne kvadrātu) un paralelogramu - nevar.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, uz_rinka)

TEMA = "Ap kuriem četrstūriem var apvilkt riņķa līniju?"

MERKIS = ("Pētīsim un pamatosim, ap kuriem četrstūriem var apvilkt riņķa "
          "līniju.")

_ZIM = geometrija([("O", 0, 0, 90), uz_rinka("A", 200), uz_rinka("B", 320),
                   uz_rinka("C", 40), uz_rinka("D", 110)],
                  nogriezni=["AB", "BC", "CD", "DA"],
                  lenki=[("DAB", "75°"), ("BCD", "105°")],
                  rinki=[("O", 5)])

_TAISNSTURIS = geometrija([("O", 0, 0, -90), ("A", -12, -5, -135),
                           ("B", 12, -5, -45), ("C", 12, 5, 45),
                           ("D", -12, 5, 135)],
                          nogriezni=["AB", "BC", "CD", "DA", "AC"],
                          malas=[("AB", "120"), ("BC", "50")],
                          rinki=[("O", 13)])

SATURS = [
    Sakums("Četras virsotnes uz vienas riņķa līnijas",
           zimejums=_ZIM,
           paraksts="75° + 105° = 180° - pretējie leņķi.",
           fakti=["Ievilktā četrstūrī ∠A + ∠C = 180°.",
                  "Tāpat ∠B + ∠D = 180°.",
                  "Ja summa nav 180°, riņķa līniju apvilkt nevar."]),

    Doma("Ievilkts četrstūris",
         "Ap četrstūri var apvilkt riņķa līniju tad un tikai tad, ja tā "
         "pretējo leņķu summa ir 180°.",
         soli=[
             "∠A ir ievilktais leņķis uz loka BCD: ∠A = {1|2} loka BCD.",
             "∠C balstās uz loka BAD: ∠C = {1|2} loka BAD.",
             "Abi loki kopā - visa riņķa līnija, 360°.",
             "∠A + ∠C = {1|2} · 360° = 180°.",
         ],
         pieze="Der: kvadrāts, taisnstūris, vienādsānu trapece. Neder: rombs "
               "un paralelograms bez taisniem leņķiem."),

    Paraugs("Trūkstošais leņķis",
            uzd="Četrstūris ABCD ievilkts riņķa līnijā; ∠A = 70°, "
                "∠B = 95°. Atrodi ∠C un ∠D.",
            soli=[
                ("∠C = 180° − 70° = 110°", "Pretējie leņķi."),
                ("∠D = 180° − 95° = 85°", "Pretējie leņķi."),
                ("70° + 95° + 110° + 85° = 360°", "Pārbaude."),
            ],
            atbilde="∠C = 110°, ∠D = 85°"),

    Ievadi("Aprēķini", [
        {"jaut": "∠A = 64°. ∠C = ?°", "atb": ["116"], "padoms": "180 − 64."},
        {"jaut": "∠B = 2 · ∠D. ∠D = ?°", "atb": ["60"],
         "padoms": "3∠D = 180°."},
        {"jaut": "∠A : ∠C = 2 : 3. ∠A = ?°", "atb": ["72"],
         "padoms": "180 : 5 · 2."},
        {"jaut": "Vienādsānu trapecē ∠A = 55°. Lielākais leņķis (°)?",
         "atb": ["125"], "padoms": "180 − 55."},
    ]),

    Varianti("Vai var apvilkt?", [
        {"jaut": "Taisnstūris", "opcijas": ["Var", "Nevar"], "jaukt": False,
         "pareizi": 0, "padoms": "90° + 90° = 180°."},
        {"jaut": "Rombs ar leņķiem 60° un 120°", "opcijas": ["Var", "Nevar"],
         "jaukt": False, "pareizi": 1, "padoms": "60° + 60° ≠ 180°."},
        {"jaut": "Vienādsānu trapece", "opcijas": ["Var", "Nevar"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Leņķi pie pamata vienādi, blakus leņķi dod 180°."},
        {"jaut": "Četrstūris ar leņķiem 80°, 90°, 100°, 90° (pēc kārtas)",
         "opcijas": ["Var", "Nevar"], "jaukt": False, "pareizi": 0,
         "padoms": "80 + 100 = 180."},
    ]),

    Pasaule("Apaļš galdauts",
            Ievadi("", [
                {"jaut": "Galds 120 × 50 cm. Galdauts tieši aizsniedz visus "
                         "četrus stūrus. Tā diametrs (cm)?", "atb": ["130"],
                 "padoms": "Diametrs = diagonāle: √(14 400 + 2500)."},
                {"jaut": "Kvadrātisks galds ar malu 60 cm. Galdauta diametrs "
                         "(cm)? Noapaļo līdz veselam.", "atb": ["85"],
                 "padoms": "60√2 ≈ 84,9."},
            ]),
            pavediens="maja",
            konteksts="Taisnstūra galdu apklāj ar apaļu galdautu, kura mala "
                      "iet caur galda stūriem.",
            kapec="Taisnstūrim apvilktās riņķa līnijas diametrs ir tā "
                  "diagonāle - taisnais leņķis balstās uz diametra.",
            zimejums=_TAISNSTURIS),

    Kopsavilkums([
        "Zinu, ka ievilktā četrstūrī pretējo leņķu summa ir 180°.",
        "Pamatoju to ar ievilktā leņķa īpašību.",
        "Nosaku, ap kuriem četrstūriem var apvilkt riņķa līniju.",
    ]),

    Majas([
        "Uzzīmē riņķa līniju, ievelc četrstūri un izmēri pretējos leņķus.",
        "Pamato, kāpēc ap paralelogramu var apvilkt riņķa līniju tikai tad, "
        "ja tas ir taisnstūris.",
        "Izmēri savu galdu un aprēķini apaļa galdauta diametru.",
    ]),
]
