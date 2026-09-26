# -*- coding: utf-8 -*-
"""2. klase, 36. stunda: «Cik apmēram sanāks?»

Pirms rēķina summu novērtē, noapaļojot saskaitāmos līdz desmitiem:
38 + 45 ir apmēram 40 + 50 = 90. Novērtējums nepasaka precīzu atbildi, bet
noķer lielas kļūdas - piemēram, aizmirstu desmitu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, taisne)

TEMA = "Cik apmēram sanāks?"

MERKIS = ("Šodien prognozēsim summas aptuveno lielumu un izmantosim to "
          "atbildes pārbaudei.")

SATURS = [
    Sakums("Vai 38 + 45 var būt 713?",
           zimejums=taisne(30, 50, 10, atzimes=[(38, "38")]),
           paraksts="38 ir tuvāk 40 nekā 30.",
           fakti=["38 ≈ 40, 45 ≈ 50.",
                  "Apmēram 40 + 50 = 90.",
                  "713 ir daudz par lielu - kļūda!"]),

    Doma("Apaļi desmiti",
         "Skaitli aizstāj ar tuvāko apaļo desmitu un rēķina galvā.",
         soli=[
             "Atrodi tuvāko desmitu: 38 → 40, 23 → 20.",
             "Ja beidzas ar 5, ņem lielāko: 45 → 50.",
             "Saskaiti apaļos desmitus.",
             "Precīzai atbildei jābūt tuvu šim skaitlim.",
         ],
         pieze="Zīme ≈ nozīmē «apmēram vienāds»."),

    Ievadi("Uz tuvāko desmitu", [
        {"jaut": "27 ≈ ?", "atb": ["30"], "padoms": "27 ir tuvāk 30."},
        {"jaut": "62 ≈ ?", "atb": ["60"], "padoms": "62 ir tuvāk 60."},
        {"jaut": "85 ≈ ?", "atb": ["90"], "padoms": "Beidzas ar 5 - uz augšu."},
        {"jaut": "14 ≈ ?", "atb": ["10"], "padoms": "Tuvāk 10."},
        {"jaut": "49 ≈ ?", "atb": ["50"], "padoms": "Gandrīz 50."},
        {"jaut": "71 ≈ ?", "atb": ["70"], "padoms": "Tuvāk 70."},
    ], pamats=4),

    Varianti("Apmēram cik?", [
        {"jaut": "29 + 42 ir apmēram...", "opcijas": ["70", "50", "90"],
         "pareizi": 0, "padoms": "30 + 40."},
        {"jaut": "51 + 38 ir apmēram...", "opcijas": ["90", "80", "60"],
         "pareizi": 0, "padoms": "50 + 40."},
        {"jaut": "Kura atbilde uz 47 + 26 noteikti ir kļūdaina?",
         "opcijas": ["613", "73", "apmēram 80"], "pareizi": 0,
         "padoms": "50 + 30 = 80 - tālu no 613."},
        {"jaut": "Kura summa ir mazāka par 50?",
         "opcijas": ["21 + 18", "32 + 29", "44 + 13"], "pareizi": 0,
         "padoms": "20 + 20 = 40."},
    ]),

    Pasaule("Vai nauda pietiks?",
            Varianti("", [
                {"jaut": "Grāmata maksā 18 €, spēle - 29 €. Tev ir 50 €. "
                         "Vai pietiks?",
                 "opcijas": ["Jā, apmēram 20 + 30 = 50, tieši rēķinot 47",
                             "Nē"], "jaukt": False, "pareizi": 0,
                 "padoms": "18 + 29 = 47."},
                {"jaut": "Kurai pirkuma summai 50 € noteikti nepietiks?",
                 "opcijas": ["38 € + 24 €", "19 € + 21 €", "11 € + 12 €"],
                 "pareizi": 0, "padoms": "40 + 20 = 60."},
            ]),
            pavediens="veikals",
            konteksts="Grāmatnīcā izvēlies dāvanas brālim un māsai.",
            kapec="Pie kases apmērs pasaka, vai vērts tālāk rēķināt."),

    Kopsavilkums([
        "Noapaļoju skaitli līdz tuvākajam desmitam.",
        "Novērtēju summu galvā.",
        "Pārbaudu, vai precīzā atbilde ir tuvu novērtējumam.",
    ]),

    Majas([
        "Veikalā novērtē 2 preču kopējo cenu.",
        "Pēc tam saskaiti precīzi.",
        "Cik tuvu bija tavs novērtējums?",
    ]),
]
