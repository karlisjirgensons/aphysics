# -*- coding: utf-8 -*-
"""5. klase, 154. stunda: «Kad aritmētiskais vidējais maldina?»

Temata pēdējā stunda pirms pārbaudes darba. Aritmētisko vidējo aprēķināt ir
viegli - saskaiti un izdali -, bet stundas jautājums ir cits: vai šis viens
skaitlis tiešām raksturo visus datus. Ja viens rezultāts ir daudz lielāks
par pārējiem, vidējais pastāsta vairāk par to, nekā par grupu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Kad aritmētiskais vidējais maldina?"

MERKIS = ("Iemācīsimies aprēķināt aritmētisko vidējo un argumentēt, kad tas "
          "datus raksturo atbilstoši.")

SATURS = [
    Sakums("Vidēji pieci, bet nevienam nav pieci",
           zimejums=kolonnas([("A", 2), ("B", 3), ("C", 3), ("D", 12)]),
           paraksts="Vidējais ir 5, bet trim no četriem ir mazāk par 4.",
           fakti=["Dati: 2, 3, 3 un 12.",
                  "Summa ir 20, vidējais - 5.",
                  "Bet neviens rezultāts nav tuvu pieciniekam."]),

    Doma("Saskaiti un izdali - bet tad paskaties",
         "Aritmētisko vidējo aprēķina, visus skaitļus saskaitot un summu "
         "dalot ar skaitļu daudzumu; tas raksturo datus labi tikai tad, ja "
         "skaitļi nav pārāk atšķirīgi.",
         soli=[
             "Saskaiti visus skaitļus.",
             "Izdali summu ar skaitļu daudzumu.",
             "Pieraksti iegūto vidējo.",
             "Salīdzini vidējo ar pašiem skaitļiem.",
             "Ja viens skaitlis ir daudz lielāks, vidējais maldina.",
         ],
         pieze="Vidējais vienmēr atrodas starp mazāko un lielāko skaitli, "
               "bet tas nenozīmē, ka tas ir tipisks. Ar datiem 2, 3, 3 un 12 "
               "vidējais 5 nav līdzīgs nevienam no tiem."),

    Paraugs("Aprēķini vidējo skaitļiem 2, 3, 3 un 12",
            uzd="Cik ir aritmētiskais vidējais un vai tas raksturo datus?",
            soli=[
                ("2 + 3 + 3 + 12 = 20",
                 "Visu skaitļu summa."),
                ("20 : 4 = 5",
                 "Dala ar skaitļu daudzumu."),
                ("Vidējais ir 5",
                 "Bet trīs skaitļi ir mazāki par 4."),
                ("Viens skaitlis - 12 - ir daudz lielāks",
                 "Tieši tas pavelk vidējo uz augšu."),
            ],
            atbilde="Vidējais ir 5, bet tas datus neraksturo labi"),

    Ievadi("Aprēķini vidējo", [
        {"jaut": "Skaitļi 2, 3, 3 un 12. Cik ir to summa?",
         "atb": ["20"], "padoms": "Saskaiti visus."},
        {"jaut": "Cik ir aritmētiskais vidējais?",
         "atb": ["5"], "padoms": "20 : 4."},
        {"jaut": "Skaitļi 4, 5 un 6. Cik ir vidējais?",
         "atb": ["5"], "padoms": "15 : 3."},
        {"jaut": "Skaitļi 10, 10, 10 un 10. Cik ir vidējais?",
         "atb": ["10"], "padoms": "40 : 4."},
        {"jaut": "Skaitļi 1, 2 un 9. Cik ir vidējais?",
         "atb": ["4"], "padoms": "12 : 3."},
        {"jaut": "Skaitļi 6, 8, 7 un 7. Cik ir vidējais?",
         "atb": ["7"], "padoms": "28 : 4."},
        {"jaut": "Atzīmes 5, 6, 7 un 6. Cik ir vidējā atzīme?",
         "atb": ["6"], "padoms": "24 : 4."},
        {"jaut": "Skaitļi 3, 3, 3 un 21. Cik ir vidējais?",
         "atb": ["7,5"], "padoms": "30 : 4."},
    ], pamats=4,
        ievads="Saskaiti, izdali un tad paskaties, vai atbilde ir tipiska."),

    Zimejums("Kad vidējais der",
             kolonnas([("A", 6), ("B", 8), ("C", 7), ("D", 7)]),
             paskaidro="Šeit skaitļi ir tuvu cits citam, un vidējais 7 "
                       "tiešām raksturo visus. Salīdzini ar stundas sākuma "
                       "stabiņiem.",
             ievads="Tas pats rēķins, bet dati ir līdzīgāki."),

    Varianti("Vai vidējais te der?", [
        {"jaut": "Kā aprēķina aritmētisko vidējo?",
         "opcijas": ["Saskaita un dala ar skaitļu daudzumu",
                     "Izvēlas vidējo skaitli",
                     "Saskaita lielāko un mazāko",
                     "Dala lielāko ar mazāko"],
         "pareizi": 0,
         "padoms": "Summa dalīta ar skaitu."},
        {"jaut": "Skaitļi 2, 3, 3 un 12. Cik ir vidējais?",
         "opcijas": ["5", "3", "20", "4"],
         "pareizi": 0,
         "padoms": "20 : 4."},
        {"jaut": "Kad vidējais maldina?",
         "opcijas": ["Kad viens skaitlis ir daudz lielāks par pārējiem",
                     "Kad skaitļu ir daudz",
                     "Kad skaitļi ir mazi",
                     "Nekad"],
         "pareizi": 0,
         "padoms": "Tas pavelk vidējo."},
        {"jaut": "Vai vidējais vienmēr ir kāds no dotajiem skaitļiem?",
         "opcijas": ["Nē", "Jā", "Tikai ar veseliem skaitļiem",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "4, 5 un 6 dod 5, bet 1, 2 un 9 dod 4."},
        {"jaut": "Skaitļi 10, 10, 10 un 10. Cik ir vidējais?",
         "opcijas": ["10", "40", "4", "20"],
         "pareizi": 0,
         "padoms": "Visi vienādi."},
        {"jaut": "Kur vienmēr atrodas vidējais?",
         "opcijas": ["Starp mazāko un lielāko skaitli",
                     "Virs lielākā",
                     "Zem mazākā",
                     "Tas var būt jebkur"],
         "pareizi": 0,
         "padoms": "Vidējais ir starp galējiem."},
    ], pamats=4),

    Pasaule("Kāda ir vidējā atzīme?",
            Ievadi("", [
                {"jaut": "Atzīmes 5, 6, 7 un 6. Cik ir vidējā?",
                 "atb": ["6"], "padoms": "24 : 4."},
                {"jaut": "Atzīmes 4, 4, 4 un 10. Cik ir vidējā?",
                 "atb": ["5,5"], "padoms": "22 : 4."},
                {"jaut": "Vai otrajā gadījumā vidējā atzīme raksturo darbu "
                         "labi? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "Trīs atzīmes ir 4."},
                {"jaut": "Cik skolēnu atzīmju ir pirmajā piemērā?",
                 "atb": ["4"], "padoms": "Saskaiti skaitļus."},
            ]),
            pavediens="skola",
            konteksts="Vidējā atzīme liecībā ir viens skaitlis par visu "
                      "gadu, un tas ne vienmēr stāsta visu.",
            kapec="Blakus vidējam vienmēr ir vērts paskatīties uz pašiem "
                  "datiem."),

    Kopsavilkums([
        "Aprēķinu aritmētisko vidējo.",
        "Salīdzinu vidējo ar pašiem datiem.",
        "Argumentēju, kad vidējais datus raksturo labi.",
        "Pamanu, kad viens liels skaitlis pavelk vidējo.",
    ]),

    Majas([
        "Aprēķini vidējo skaitļiem 3, 4, 4, 5 un 9.",
        "Pieraksti, vai tas raksturo datus labi.",
        "Sagatavojies pārbaudes darbam: pārskati 131.-153. stundas "
        "kopsavilkumus.",
    ]),
]
