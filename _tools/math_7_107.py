# -*- coding: utf-8 -*-
"""7. klase, 107. stunda: «Kādas ir taisnleņķa trijstūra īpašības?»

Taisnleņķa trijstūrī malas pie taisnā leņķa sauc par katetēm, malu pretī
tam - par hipotenūzu. Abi šaurie leņķi kopā ir 90°, un hipotenūza ir garākā
mala. Stunda lieto šīs īpašības un gatavo 8. klases Pitagora teorēmai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kādas ir taisnleņķa trijstūra īpašības?"

MERKIS = ("Nosauksim katetes un hipotenūzu un lietosim leņķu summu "
          "taisnleņķa trijstūrī.")

_TT = geometrija([("C", 0, 0), ("A", 6, 0), ("B", 0, 4)],
                 nogriezni=["CA", "AB", "BC"], taisni=["BCA"],
                 malas=[("CA", "katete"), ("BC", "katete"),
                        ("AB", "hipotenūza")],
                 lenki=[("CAB", "α"), ("ABC", "β")])

SATURS = [
    Sakums("Katetes un hipotenūza",
           zimejums=_TT,
           paraksts="α + β = 90°.",
           fakti=["Pie taisnā leņķa - divas katetes.",
                  "Pretī taisnajam leņķim - hipotenūza, garākā mala.",
                  "Šaurie leņķi kopā - 90°."]),

    Doma("Trīs īpašības",
         "Taisnleņķa trijstūrī: 1) šauro leņķu summa ir 90°; 2) hipotenūza "
         "ir garāka par katru kateti; 3) ja viens šaurais leņķis ir 30°, "
         "katete pretī tam ir puse no hipotenūzas.",
         soli=[
             "Atrodi taisno leņķi - tā malas ir katetes.",
             "Hipotenūza - pretī taisnajam leņķim.",
             "Otrs šaurais leņķis = 90° − pirmais.",
             "30° gadījumā: pretējā katete = hipotenūza : 2.",
         ],
         pieze="Īpašība par 30° izriet no tā, ka divi šādi trijstūri kopā "
               "veido vienādmalu trijstūri."),

    Paraugs("Leņķis 30°",
            uzd="Taisnleņķa trijstūrī ∠A = 30°, hipotenūza AB = 14 cm. "
                "Atrodi ∠B un kateti BC.",
            soli=[
                ("∠B = 90° − 30° = 60°", "(šauro leņķu summa)"),
                ("BC ir pretī ∠A = 30°", "Pretmala."),
                ("BC = 14 : 2 = 7 (cm)", "(katete pretī 30°)"),
            ],
            atbilde="∠B = 60°, BC = 7 cm"),

    Zimejums("Divi trijstūri ar 30° - vienādmalu",
             geometrija([("A", 0, 0), ("B", 3.46, 2), ("C", 3.46, 0),
                         ("D", 3.46, -2)],
                        nogriezni=["AB", "BD", "DA", "AC"],
                        taisni=["BCA"],
                        lenki=[("CAB", "30°")],
                        svitras=[("BC", 1), ("CD", 1)]),
             paskaidro="BD = AB, tāpēc BC = AB : 2."),

    Ievadi("Aprēķini", [
        {"jaut": "Taisnleņķa trijstūrī viens šaurais leņķis 37°. Otrs (°)?",
         "atb": ["53"], "padoms": "90 − 37."},
        {"jaut": "Šaurie leņķi attiecas kā 1 : 2. Mazākais (°)?",
         "atb": ["30"], "padoms": "3 daļas = 90°."},
        {"jaut": "Leņķis 30°, hipotenūza 20 cm. Katete pretī 30° (cm)?",
         "atb": ["10"], "padoms": "20 : 2."},
        {"jaut": "Katete pretī 30° ir 8 cm. Hipotenūza (cm)?",
         "atb": ["16"], "padoms": "2 · 8."},
    ]),

    Varianti("Patiess vai aplams?", [
        {"jaut": "Katete var būt garāka par hipotenūzu.",
         "opcijas": ["Aplams", "Patiess"], "pareizi": 0, "jaukt": False,
         "padoms": "Pret 90° - garākā mala."},
        {"jaut": "Taisnleņķa trijstūra šaurie leņķi var būt 45° un 45°.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "Vienādsānu taisnleņķa."},
        {"jaut": "Taisnleņķa trijstūrī var būt plats leņķis.",
         "opcijas": ["Aplams", "Patiess"], "pareizi": 0, "jaukt": False,
         "padoms": "90 + plats > 180."},
    ]),

    Pasaule("Kāpnes pie sienas",
            Ievadi("", [
                {"jaut": "Kāpnes 6 m garas veido ar zemi 60° leņķi. Cik m no "
                         "sienas ir kāpņu pamats?",
                 "atb": ["3"], "padoms": "Leņķis pie sienas 30°; katete "
                                        "pretī tam - 6 : 2."},
                {"jaut": "Cik grādu leņķis ir starp kāpnēm un sienu?",
                 "atb": ["30"], "padoms": "90 − 60."},
                {"jaut": "Droši ir, ja kāpnes pret zemi ir ap 75°. Vai 60° "
                         "ir pietiekami stāvi? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"],
                 "padoms": "60° < 75° - kāpnes var aizslīdēt."},
            ]),
            pavediens="maja",
            konteksts="Kāpnes, siena un zeme veido taisnleņķa trijstūri - "
                      "un leņķis izšķir drošību.",
            kapec="30° likums dod attālumu bez mērīšanas."),

    Kopsavilkums([
        "Nosaucu katetes un hipotenūzu.",
        "Lietoju: šaurie leņķi kopā 90°.",
        "Lietoju: katete pretī 30° ir puse hipotenūzas.",
        "Zinu, ka hipotenūza ir garākā mala.",
    ]),

    Majas([
        "Uzzīmē taisnleņķa trijstūri ar 30° un pārbaudi īpašību.",
        "Atrodi mājās taisnleņķa trijstūrus.",
        "Uzzini, ko saka Pitagora teorēma (8. klase).",
    ]),
]
