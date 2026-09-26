# -*- coding: utf-8 -*-
"""7. klase, 87. stunda: «Kādas īpašības ir vienādsānu trijstūrim?»

Vienādsānu trijstūrim leņķi pie pamata ir vienādi, un mediāna pret pamatu
ir arī bisektrise un augstums. Abas īpašības izriet no tā, ka trijstūris
sadalās divos vienādos trijstūros (pierādījām 83. stundā).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kādas īpašības ir vienādsānu trijstūrim?"

MERKIS = ("Lietosim vienādsānu trijstūra īpašības figūru lielumu "
          "aprēķināšanai.")

_VS = geometrija([("A", 0, 0), ("C", 6, 0), ("B", 3, 4.5),
                  ("M", 3, 0, -90)],
                 nogriezni=["AB", "BC", "CA"], izcelti=["BM"],
                 svitras=[("AB", 1), ("BC", 1), ("AM", 2), ("MC", 2)],
                 lenki=[("CAB", "", 2), ("BCA", "", 2), ("ABM", ""),
                        ("MBC", "")],
                 taisni=["BMC"])

SATURS = [
    Sakums("Simetrija pa vidu",
           zimejums=_VS,
           paraksts="BM ir mediāna, bisektrise un augstums vienlaikus.",
           fakti=["Salokot pa BM, A nonāk C.",
                  "Leņķi pie pamata sakrīt - tie ir vienādi.",
                  "BM ir simetrijas ass."]),

    Doma("Divas īpašības",
         "Vienādsānu trijstūrī: 1) leņķi pie pamata ir vienādi; 2) mediāna, "
         "kas novilkta pret pamatu, ir arī bisektrise un augstums.",
         soli=[
             "Ja AB = BC, tad ∠A = ∠C.",
             "Ja M - AC viduspunkts, tad BM ⊥ AC.",
             "Un ∠ABM = ∠CBM.",
             "Pamatojums: △ABM = △CBM (mmm).",
         ],
         pieze="Ir arī apgrieztā īpašība (pazīme): ja trijstūrī divi leņķi "
               "vienādi, tas ir vienādsānu."),

    Paraugs("Aprēķini, lietojot īpašības",
            uzd="Vienādsānu △ABC (AB = BC), BM - mediāna, AC = 10 cm, "
                "∠ABM = 35°, ∠A = 55°. Atrodi AM, ∠CBM, ∠C un ∠BMA.",
            soli=[
                ("AM = 10 : 2 = 5 (cm)", "(M - viduspunkts)"),
                ("∠CBM = ∠ABM = 35°", "(mediāna ir bisektrise)"),
                ("∠C = ∠A = 55°", "(leņķi pie pamata)"),
                ("∠BMA = 90°", "(mediāna ir augstums)"),
            ],
            atbilde="AM = 5 cm, ∠CBM = 35°, ∠C = 55°, ∠BMA = 90°"),

    Ievadi("Aprēķini", [
        {"jaut": "Vienādsānu trijstūrī leņķis pie pamata 47°. Otrs leņķis "
                 "pie pamata (°)?",
         "atb": ["47"], "padoms": "Vienādi."},
        {"jaut": "Mediāna pret pamatu dala virsotnes leņķi; viena daļa 28°. "
                 "Visa virsotnes leņķa lielums (°)?",
         "atb": ["56"], "padoms": "2 · 28."},
        {"jaut": "Pamats 14 cm. Cik cm no pamata gala ir augstuma pamats?",
         "atb": ["7"], "padoms": "Augstums ir arī mediāna."},
        {"jaut": "Leņķis starp mediānu pret pamatu un pamatu (°)?",
         "atb": ["90"], "padoms": "Tā ir arī augstums."},
    ]),

    Varianti("Vai īpašība der?", [
        {"jaut": "Trijstūrī ∠A = ∠C. Ko var secināt?",
         "opcijas": ["AB = BC - tas ir vienādsānu",
                     "AC = AB", "Tas ir vienādmalu", "Neko"],
         "pareizi": 0, "padoms": "Malas pretī vienādiem leņķiem."},
        {"jaut": "Daudzmalu trijstūrī mediāna ir arī augstums?",
         "opcijas": ["Parasti nē", "Vienmēr jā", "Tikai taisnleņķa",
                     "Vienmēr, ja pret garāko malu"],
         "pareizi": 0, "padoms": "Tikai vienādsānu - pret pamatu."},
        {"jaut": "Vienādmalu trijstūrī - cik ir «mediāna = bisektrise = "
                 "augstums» līniju?",
         "opcijas": ["3", "1", "0", "6"],
         "pareizi": 0, "padoms": "Katra mala var būt pamats."},
    ]),

    Pasaule("Jumta kore",
            Ievadi("", [
                {"jaut": "Mājas frontons - vienādsānu trijstūris ar pamatu "
                         "9 m. Cik m no mājas stūra ir kores balsts?",
                 "atb": ["4,5"], "padoms": "Balsts ir mediāna."},
                {"jaut": "Jumta slīpums pie viena stūra 40°. Pie otra (°)?",
                 "atb": ["40"], "padoms": "Leņķi pie pamata."},
                {"jaut": "Kādā leņķī balsts stāv pret griestiem (°)?",
                 "atb": ["90"], "padoms": "Augstums."},
            ]),
            pavediens="maja",
            konteksts="Vienādsānu jumts ir simetrisks - balsts vidū ir "
                      "vertikāls.",
            kapec="Viena līnija - trīs īpašības."),

    Kopsavilkums([
        "Zinu, ka vienādsānu trijstūrī leņķi pie pamata vienādi.",
        "Zinu, ka mediāna pret pamatu ir bisektrise un augstums.",
        "Lietoju īpašības aprēķinos.",
        "Zinu apgriezto pazīmi: vienādi leņķi - vienādas malas.",
    ]),

    Majas([
        "Izgriez vienādsānu trijstūri un pārbaudi īpašības ar locīšanu.",
        "Aprēķini elementus: pamats 12 cm, virsotnes leņķa puse 40°.",
        "Atrodi vienādsānu trijstūri arhitektūrā.",
    ]),
]
