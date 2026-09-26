# -*- coding: utf-8 -*-
"""1. klase, 22. stunda: «Kā skaitļa sastāvu uzrakstīt ar zīmēm?»

Mājiņas stāvu pieraksta kā vienādību: 8 = 3 + 5. Zīme «+» nozīmē «un»,
«=» - «ir tikpat, cik». Lasa abos virzienos: 8 ir 3 un 5; 3 un 5 ir 8.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes, majina)

TEMA = "Kā skaitļa sastāvu uzrakstīt ar zīmēm?"

MERKIS = ("Šodien pierakstīsim skaitļa sastāvu ar zīmēm «+» un «=» un "
          "izlasīsim to.")

SATURS = [
    Sakums("3 violetas un 5 oranžas - kā to uzrakstīt īsi?",
           zimejums=bildes([["ripina"] * 3 + ["ripina*"] * 5]),
           paraksts="8 = 3 + 5",
           fakti=["«+» lasa «un» vai «plus».",
                  "«=» lasa «ir» vai «ir vienāds ar».",
                  "8 = 3 + 5 un 3 + 5 = 8 ir tas pats."]),

    Doma("No mājiņas uz vienādību",
         "Katru mājiņas stāvu var uzrakstīt ar zīmēm: jumts = kreisā + labā.",
         soli=[
             "Uzraksti jumta skaitli.",
             "Uzraksti «=».",
             "Uzraksti abas daļas ar «+» starp tām.",
         ]),

    Ievadi("Uzraksti trūkstošo", [
        {"jaut": "8 = 3 + ?", "zim": majina(8, [(3, 5)]), "atb": ["5"],
         "padoms": "Paskaties mājiņā."},
        {"jaut": "6 = ? + 2", "atb": ["4"], "padoms": "Cik un 2 ir 6?"},
        {"jaut": "7 = 7 + ?", "atb": ["0"], "padoms": "Nekas vairs."},
        {"jaut": "? = 4 + 5", "atb": ["9"], "padoms": "4 un 5."},
        {"jaut": "10 = 6 + ?", "atb": ["4"], "padoms": "Cik un 6 ir 10?"},
        {"jaut": "5 = ? + 3", "atb": ["2"], "padoms": "Cik un 3 ir 5?"},
    ], pamats=4),

    Varianti("Kurš pieraksts der zīmējumam?", [
        {"jaut": "Kurš pieraksts der?",
         "zim": bildes([["ripina"] * 2 + ["ripina*"] * 4]),
         "opcijas": ["6 = 2 + 4", "6 = 3 + 3", "4 = 2 + 2"],
         "pareizi": 0, "padoms": "2 violetas, 4 oranžas."},
        {"jaut": "Kā izlasīt 9 = 5 + 4?",
         "opcijas": ["9 ir 5 un 4", "9 un 5 ir 4", "5 ir 9 un 4"],
         "pareizi": 0, "padoms": "«=» lasa «ir»."},
    ]),

    Pasaule("Zeķes veļas mašīnā",
            Ievadi("", [
                {"jaut": "Veļas mašīnā ir 7 zeķes: 4 baltas, pārējās "
                         "melnas. 7 = 4 + ?", "atb": ["3"],
                 "padoms": "Cik un 4 ir 7?"},
            ]),
            pavediens="maja",
            konteksts="Pēc mazgāšanas zeķes sašķiro pēc krāsas.",
            kapec="Vienādība īsi pastāsta, kā viss sadalījās."),

    Kopsavilkums([
        "Pierakstu skaitļa sastāvu: 8 = 3 + 5.",
        "Lasu zīmes «+» un «=».",
        "Atrodu trūkstošo skaitli vienādībā.",
    ]),

    Majas([
        "Pieraksti ar zīmēm, cik zēnu un meiteņu ir ģimenē.",
        "Uzraksti visus skaitļa 6 sastāvus ar zīmēm.",
        "Izlasi skaļi: 10 = 7 + 3.",
    ]),
]
