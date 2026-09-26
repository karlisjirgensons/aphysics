# -*- coding: utf-8 -*-
"""2. klase, 13. stunda: «Kāpēc iznāk dažādi skaitļi?»

Vienu un to pašu galdu var izmērīt ar plaukstām, zīmuļiem vai
centimetriem, un skaitlis katru reizi ir cits. Jo mazāka vienība, jo vairāk
reižu tā ietilpst - tāpēc 1 m = 10 dm = 100 cm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, vienibas)

TEMA = "Kāpēc iznāk dažādi skaitļi?"

MERKIS = ("Šodien noskaidrosim, kāpēc, mērot ar mazāku vienību, sanāk "
          "lielāks skaitlis, un salīdzināsim m, dm un cm.")

SATURS = [
    Sakums("Galds ir 3 plaukstas vai 12 dzēšgumijas garš. Kurš mērīja "
           "pareizi?",
           zimejums=vienibas(3),
           paraksts="Tas pats galds - 3 plaukstas.",
           fakti=["Abi mērīja pareizi!",
                  "Dzēšgumija ir mazāka, tāpēc tā ietilpst vairāk reižu."]),

    Doma("Mazāka vienība - lielāks skaitlis",
         "Jo mazāka mērvienība, jo vairāk reižu tā ietilpst garumā.",
         soli=[
             "1 m = 10 dm - decimetrs ir desmit reizes mazāks par metru.",
             "1 dm = 10 cm.",
             "1 m = 100 cm.",
             "1 cm = 10 mm.",
         ],
         pieze="Tāpēc, salīdzinot garumus, vispirms jāpārliecinās, ka tie "
               "doti vienā mērvienībā."),

    Slidnis("Tas pats metrs", [
        {"v": "1 m", "teksts": "Viens metrs.", "zim": vienibas(1)},
        {"v": "2 puses", "teksts": "Puse metra - 50 cm.",
         "zim": vienibas(2)},
        {"v": "10 dm", "teksts": "Desmit decimetri.", "zim": vienibas(10)},
    ], ievads="Josla ir tikpat gara - mainās tikai vienība."),

    Ievadi("Pārveido", [
        {"jaut": "Cik dm ir 1 m?", "atb": ["10"], "padoms": "1 m = 10 dm."},
        {"jaut": "Cik cm ir 1 dm?", "atb": ["10"], "padoms": "1 dm = 10 cm."},
        {"jaut": "Cik cm ir 3 dm?", "atb": ["30"], "padoms": "10 + 10 + 10."},
        {"jaut": "Cik cm ir 1 m?", "atb": ["100"],
         "padoms": "10 dm, katrā 10 cm."},
        {"jaut": "Cik dm ir 70 cm?", "atb": ["7"],
         "padoms": "Cik reižu 10 ietilpst 70?"},
        {"jaut": "Cik cm ir 5 dm?", "atb": ["50"], "padoms": "Pa 10."},
    ], pamats=4),

    Varianti("Kurš garāks?", [
        {"jaut": "Kurš garums ir lielāks?", "opcijas": ["1 m", "90 cm"],
         "jaukt": False, "pareizi": 0, "padoms": "1 m = 100 cm."},
        {"jaut": "Kurš garums ir lielāks?", "opcijas": ["4 dm", "35 cm"],
         "jaukt": False, "pareizi": 0, "padoms": "4 dm = 40 cm."},
        {"jaut": "Kurš garums ir lielāks?", "opcijas": ["6 cm", "8 dm"],
         "jaukt": False, "pareizi": 1, "padoms": "8 dm = 80 cm."},
        {"jaut": "Mērot galdu ar zīmuli, sanāca 8, ar pildspalvu - 6. "
                 "Kura ir garāka?", "opcijas": ["pildspalva", "zīmulis"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Garāka vienība ietilpst mazāk reižu."},
    ]),

    Pasaule("Vai skapis ienāks pa durvīm?",
            Varianti("", [
                {"jaut": "Skapis ir 9 dm plats, durvis - 80 cm platas. Vai "
                         "skapis ienāks, neapgriežot to?",
                 "opcijas": ["Nē, 90 cm ir vairāk nekā 80 cm",
                             "Jā, 9 ir mazāk nekā 80"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "Vispirms pārvērt abus cm."},
                {"jaut": "Gulta ir 2 m gara, istaba - 3 m. Vai gulta "
                         "ietilps?", "opcijas": ["Jā", "Nē"],
                 "jaukt": False, "pareizi": 0, "padoms": "2 m < 3 m."},
            ]),
            pavediens="maja",
            konteksts="Pārceļoties mēbeles mēra dažādās vienībās.",
            kapec="Salīdzināt drīkst tikai vienā mērvienībā."),

    Kopsavilkums([
        "Zinu, ka mazāka vienība ietilpst vairāk reižu.",
        "Pārvēršu: 1 m = 10 dm = 100 cm, 1 dm = 10 cm.",
        "Salīdzinu garumus vienā mērvienībā.",
    ]),

    Majas([
        "Izmēri galdu ar plaukstām, pēc tam ar karotēm.",
        "Kurš skaitlis sanāca lielāks? Kāpēc?",
        "Izmēri to pašu galdu centimetros.",
    ]),
]
