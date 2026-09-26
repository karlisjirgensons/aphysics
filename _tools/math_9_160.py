# -*- coding: utf-8 -*-
"""9. klase, 160. stunda: «Kuros četrstūros var ievilkt riņķa līniju?»

Četrstūrī var ievilkt riņķa līniju tad un tikai tad, ja pretējo malu
summas ir vienādas: a + c = b + d. Pamatojums - pieskaru nogriežņi no
katras virsotnes ir vienādi (156. stunda). Zīmējumā vienādsānu trapece
4, 10, 16, 10 ar augstumu 8 un r = 4.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kuros četrstūros var ievilkt riņķa līniju?"

MERKIS = ("Pētīsim un pamatosim, kuros četrstūros var ievilkt riņķa "
          "līniju.")

_TRAPECE = geometrija([("A", -8, 0, -135), ("B", 8, 0, -45),
                       ("C", 2, 8, 45), ("D", -2, 8, 135), ("O", 0, 4, 0),
                       ("_K", 0, 0)],
                      nogriezni=["AB", "BC", "CD", "DA", ("O", "_K")],
                      taisni=[("O", "_K", "B")],
                      malas=[("AB", "16"), ("DC", "4"), ("BC", "10"),
                             ("AD", "10")],
                      rinki=[("O", 4)])

SATURS = [
    Sakums("Aplis, kas pieskaras visām četrām malām",
           zimejums=_TRAPECE,
           paraksts="16 + 4 = 10 + 10 - pretējo malu summas vienādas.",
           fakti=["Ievilktai riņķa līnijai: a + c = b + d.",
                  "Der rombs un kvadrāts; neder taisnstūris 3 × 5.",
                  "Augstums = diametrs: h = 2r."]),

    Doma("Apvilkts četrstūris",
         "Četrstūrī var ievilkt riņķa līniju tad un tikai tad, ja tā "
         "pretējo malu summas ir vienādas.",
         soli=[
             "No katras virsotnes divi pieskaru nogriežņi ir vienādi: x, y, "
             "z, w.",
             "AB = x + y, BC = y + z, CD = z + w, DA = w + x.",
             "AB + CD = x + y + z + w = BC + DA.",
         ],
         pieze="Tādu četrstūri sauc par apvilktu ap riņķa līniju."),

    Paraugs("Trūkstošā mala",
            uzd="Četrstūrī ABCD ievilkta riņķa līnija; AB = 7, BC = 9, "
                "CD = 11. Atrodi AD.",
            soli=[
                ("AB + CD = BC + AD", "Pretējo malu summas."),
                ("7 + 11 = 9 + AD", "Ievieto."),
                ("AD = 9", "Aprēķins."),
            ],
            atbilde="AD = 9"),

    Ievadi("Aprēķini", [
        {"jaut": "AB + CD = 20. Perimetrs?", "atb": ["40"],
         "padoms": "Arī BC + AD = 20."},
        {"jaut": "Rombā ievilkta riņķa līnija, perimetrs 36. Mala?",
         "atb": ["9"], "padoms": "36 : 4."},
        {"jaut": "Vienādsānu trapece ar pamatiem 2 un 8 ir apvilkta. Sānu "
                 "mala?", "atb": ["5"], "padoms": "2 · sāns = 2 + 8."},
        {"jaut": "Tai pašai trapecei augstums? (sānu mala 5, pamatu starpības "
                 "puse 3)", "atb": ["4"], "padoms": "√(25 − 9)."},
        {"jaut": "Ievilktās riņķa līnijas rādiuss tai trapecei?",
         "atb": ["2"], "padoms": "h = 2r."},
    ]),

    Varianti("Vai var ievilkt?", [
        {"jaut": "Rombs", "opcijas": ["Var", "Nevar"], "jaukt": False,
         "pareizi": 0, "padoms": "Visas malas vienādas."},
        {"jaut": "Taisnstūris 3 × 5", "opcijas": ["Var", "Nevar"],
         "jaukt": False, "pareizi": 1, "padoms": "3 + 3 ≠ 5 + 5."},
        {"jaut": "Četrstūris ar malām 5, 7, 8, 6 (pēc kārtas)",
         "opcijas": ["Var", "Nevar"], "jaukt": False, "pareizi": 0,
         "padoms": "5 + 8 = 7 + 6."},
        {"jaut": "Kurā četrstūrī var gan ievilkt, gan apvilkt riņķa līniju?",
         "opcijas": ["kvadrātā", "rombā", "taisnstūrī", "paralelogramā"],
         "pareizi": 0, "padoms": "Vajag abus nosacījumus."},
    ]),

    Pasaule("Apaļa vitrāža logā",
            Ievadi("", [
                {"jaut": "Logs - vienādsānu trapece ar pamatiem 60 un 240 cm; "
                         "tajā ievilkta apaļa vitrāža. Sānu mala (cm)?",
                 "atb": ["150"], "padoms": "(60 + 240) : 2."},
                {"jaut": "Loga augstums (cm)?", "atb": ["120"],
                 "padoms": "√(150^2 − 90^2)."},
                {"jaut": "Vitrāžas diametrs (cm)?", "atb": ["120"],
                 "padoms": "Diametrs = augstums."},
            ]),
            pavediens="maja",
            konteksts="Baznīcas logā apaļa vitrāža pieskaras visām četrām "
                      "trapeces malām.",
            kapec="Pretējo malu summu vienādība dod sānu malu, bet augstums "
                  "- vitrāžas diametru.",
            zimejums=_TRAPECE),

    Kopsavilkums([
        "Zinu: ievilkt var, ja pretējo malu summas vienādas.",
        "Pamatoju to ar pieskaru nogriežņiem.",
        "Aprēķinu trūkstošo malu, augstumu un rādiusu.",
    ]),

    Majas([
        "Uzzīmē rombu un konstruē tajā ievilktu riņķa līniju.",
        "Vienādsānu trapece ar pamatiem 8 un 18 ir apvilkta. Atrodi r.",
        "Salīdzini 159. un 160. stundas nosacījumus tabulā.",
    ]),
]
