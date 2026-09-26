# -*- coding: utf-8 -*-
"""2. klase, 35. stunda: «Kā pierakstīt stabiņā?»

Saskaitīšana stabiņā ar pāreju jaunā desmitā: vieni dod 13 - zem svītras
raksta 3, bet 1 desmitu «atceras» un pieraksta mazu virs desmitiem. Katrs
solis ir tas pats, ko iepriekšējā stundā darīja ar kubiņiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, stabins)

TEMA = "Kā pierakstīt stabiņā?"

MERKIS = ("Šodien saskaitīsim divciparu skaitļus stabiņā un paskaidrosim "
          "katru soli.")

SATURS = [
    Sakums("Kur paslēpt jauno desmitu, rakstot stabiņā?",
           zimejums=stabins(38, 25, virs="1"),
           paraksts="Mazais 1 virs desmitiem - tas ir jaunais desmits.",
           fakti=["8 + 5 = 13: raksta 3, 1 desmitu atceras.",
                  "3 + 2 + 1 = 6 desmiti.",
                  "38 + 25 = 63."]),

    Doma("Saskaitīšana stabiņā",
         "Sāk ar vieniem; ja sanāk 10 vai vairāk, desmitu pārnes.",
         soli=[
             "Uzraksti skaitļus: vieni zem vieniem.",
             "Saskaiti vienus. Ja ir 10 vai vairāk, raksti tikai vienus.",
             "Desmitu pieraksti mazu virs desmitu kolonnas.",
             "Saskaiti desmitus kopā ar pārnesto.",
         ]),

    Slidnis("47 + 36 soli pa solim", [
        {"v": "47 + 36", "teksts": "Uzraksta stabiņā.",
         "zim": stabins(47, 36, rezultats=False)},
        {"v": "7 + 6 = 13", "teksts": "Raksta 3, 1 pārnes.",
         "zim": stabins(47, 36, rezultats=False, virs="1")},
        {"v": "4 + 3 + 1 = 8", "teksts": "Desmiti ar pārnesto: 83.",
         "zim": stabins(47, 36, virs="1")},
    ]),

    Ievadi("Rēķini stabiņā", [
        {"jaut": "Cik ir?", "zim": stabins(29, 34, rezultats=False),
         "atb": ["63"], "padoms": "9 + 4 = 13, pārnes 1."},
        {"jaut": "Cik ir?", "zim": stabins(56, 18, rezultats=False),
         "atb": ["74"], "padoms": "6 + 8 = 14."},
        {"jaut": "Cik ir?", "zim": stabins(45, 45, rezultats=False),
         "atb": ["90"], "padoms": "5 + 5 = 10: raksta 0."},
        {"jaut": "Cik ir?", "zim": stabins(67, 26, rezultats=False),
         "atb": ["93"], "padoms": "7 + 6 = 13."},
        {"jaut": "Cik ir?", "zim": stabins(38, 49, rezultats=False),
         "atb": ["87"], "padoms": "8 + 9 = 17."},
        {"jaut": "Cik ir?", "zim": stabins(19, 72, rezultats=False),
         "atb": ["91"], "padoms": "9 + 2 = 11."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "Juris: 46 + 38 = 74. Kas aizmirsts?",
         "zim": stabins(46, 38, rezultats=False),
         "opcijas": ["pārnestais desmits", "vieni", "nekas"],
         "pareizi": 0, "padoms": "Jābūt 84."},
        {"jaut": "Kas jāraksta zem svītras vienu vietā, ja 9 + 7?",
         "opcijas": ["6", "16", "7"], "pareizi": 0,
         "padoms": "16: raksta 6, 1 pārnes."},
    ]),

    Pasaule("Cik lapu izlasīju?",
            Ievadi("", [
                {"jaut": "Sestdien Līva izlasīja 28 lapas, svētdien - 35. "
                         "Cik kopā?", "atb": ["63"], "padoms": "Stabiņā."},
                {"jaut": "Grāmatā ir 90 lapu. Cik vēl jāizlasa?",
                 "atb": ["27"], "padoms": "90 − 63."},
            ]),
            pavediens="skola",
            konteksts="Līva lasa grāmatu lasīšanas maratonam.",
            kapec="Stabiņā lielus skaitļus saskaita bez kļūdām."),

    Kopsavilkums([
        "Saskaitu divciparu skaitļus stabiņā.",
        "Pārnesu desmitu, ja vienu ir 10 vai vairāk.",
        "Paskaidroju katru soli.",
    ]),

    Majas([
        "Izrēķini stabiņā: 37 + 48, 26 + 57, 59 + 33.",
        "Pie katra atzīmē pārnesto desmitu.",
        "Pārbaudi ar kubiņiem vai zīmējumu.",
    ]),
]
