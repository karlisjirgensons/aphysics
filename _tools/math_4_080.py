# -*- coding: utf-8 -*-
"""4. klase, 80. stunda: «Kuri cipari trūkst?»

Mikrotemata noslēgums - loģikas uzdevums: stabiņā daži cipari paslēpti, un
tos atrod, spriežot no beigām. Tā pārbauda, vai skolēns saprot katru
stabiņa soli, nevis tikai atkārto algoritmu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kuri cipari trūkst?"

MERKIS = ("Noteiksim trūkstošos ciparus reizinājumā rakstos, spriežot no "
          "beigām.")

SATURS = [
    Sakums("Detektīvs stabiņā",
           zimejums=restis([["", "", "2", None],
                            ["·", "", "", "3"],
                            ["", "", "8", "1"]],
                           "2☐ · 3 = 81"),
           paraksts="Kurš cipars paslēpies?",
           fakti=["☐ · 3 beidzas ar 1 - tas var būt tikai 7.",
                  "Pārbaude: 27 · 3 = 81."]),

    Doma("Spried no vieniem",
         "Trūkstošo ciparu atrod, meklējot, kurš reizinājums beidzas ar "
         "vajadzīgo ciparu, un pārbauda ar visu reizinājumu.",
         soli=[
             "Paskaties uz vieniem: kāds cipars, reizināts, dod šo galu?",
             "Izraksti visas iespējas no reizināšanas tabulas.",
             "Pārbaudi katru iespēju ar visu reizinājumu.",
             "Atbilde der, ja viss stabiņš sakrīt.",
         ],
         pieze="Ar 5 reizinot, gals vienmēr ir 0 vai 5 - tas palīdz spriest."),

    Paraugs("☐4 · 6 = 384",
            uzd="Kurš cipars trūkst: ☐4 · 6 = 384?",
            soli=[
                ("4 · 6 = 24", "Vieni: 4, 2 prātā."),
                ("☐ · 6 + 2 = 38", "Desmiti un simti kopā ir 38."),
                ("☐ · 6 = 36 → ☐ = 6", None),
                ("64 · 6 = 384", "Pārbaude sakrīt."),
            ],
            atbilde="6"),

    Ievadi("Atrodi ciparu", [
        {"jaut": "2☐ · 3 = 81. Kāds ir ☐?", "atb": ["7"],
         "padoms": "☐ · 3 beidzas ar 1."},
        {"jaut": "☐4 · 6 = 384. Kāds ir ☐?", "atb": ["6"],
         "padoms": "Skat. paraugu."},
        {"jaut": "3☐ · 4 = 152. Kāds ir ☐?", "atb": ["8"],
         "padoms": "152 : 4 = 38."},
        {"jaut": "1☐ · 1☐ = 169 (abi cipari vienādi). Kāds ir ☐?",
         "atb": ["3"], "padoms": "☐ · ☐ beidzas ar 9: 3 vai 7."},
        {"jaut": "☐5 · 5 = 225. Kāds ir ☐?", "atb": ["4"],
         "padoms": "225 : 5 = 45."},
        {"jaut": "2☐ · 20 = 540. Kāds ir ☐?", "atb": ["7"],
         "padoms": "540 : 20 = 27."},
    ], pamats=4),

    Varianti("Kurš var būt?", [
        {"jaut": "☐ · 4 beidzas ar 2. Kuri cipari der?",
         "opcijas": ["3 vai 8", "tikai 3", "2 vai 7", "tikai 8"],
         "pareizi": 0, "padoms": "3 · 4 = 12, 8 · 4 = 32."},
        {"jaut": "☐ · 5 beidzas ar 3. Cik ciparu der?",
         "opcijas": ["neviens", "1", "2", "5"], "pareizi": 0,
         "padoms": "Ar 5 beidzas ar 0 vai 5."},
        {"jaut": "☐ · 9 beidzas ar 6. Kurš cipars?",
         "opcijas": ["4", "6", "9", "3"], "pareizi": 0,
         "padoms": "4 · 9 = 36."},
    ]),

    Pasaule("Seifa kods",
            Ievadi("", [
                {"jaut": "Seifa kods: divciparu skaitlis, kas reiz 7 dod 91. "
                         "Kāds kods?",
                 "atb": ["13"], "padoms": "91 : 7."},
                {"jaut": "Otrais kods: ☐☐ · 11 = 385. Kāds divciparu "
                         "skaitlis?",
                 "atb": ["35"], "padoms": "385 : 11."},
                {"jaut": "Trešais: skaitlis, kas reiz 25 dod 900.",
                 "atb": ["36"], "padoms": "900 : 25."},
                {"jaut": "Visu trīs kodu summa?", "atb": ["84"],
                 "padoms": "13 + 35 + 36."},
            ]),
            pavediens="dati",
            konteksts="Paroles un kodus lauž ar loģiku - un matemātiķi to "
                      "prot vislabāk.",
            kapec="Spriešana no beigām ir detektīva metode."),

    Kopsavilkums([
        "Atrodu trūkstošos ciparus reizinājumā.",
        "Spriežu no vieniem un pārbaudu visu stabiņu.",
        "Lietoju dalīšanu, lai atrastu nezināmo reizinātāju.",
    ]),

    Majas([
        "Izdomā «detektīva stabiņu» ar vienu paslēptu ciparu.",
        "Palūdz mājiniekiem to atrisināt.",
        "Atrisini: ☐8 · 4 = 192.",
    ]),
]
