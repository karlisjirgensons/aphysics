# -*- coding: utf-8 -*-
"""1. klase, 2. stunda: «Kā uzraksta skaitli, ko redzi?»

Pirmajā stundā skaitu parādīja ar ripiņām; tagad to pieraksta ar ciparu.
Ciparu ir tikai desmit (0-9), un katrs aizņem vienu rūtiņu. Nulle ir
«necik» - tukša paplāte arī ir skaits.
"""

from math_saturs import (Doma, Ievadi, Izvele, Josla, Kopsavilkums, Majas,
                         Pasaule, Petijums, Sakums, Varianti, bildes)

TEMA = "Kā uzraksta skaitli, ko redzi?"

MERKIS = ("Šodien iemācīsimies saskaitīt lietas un uzrakstīt, cik to ir, ar "
          "ciparu.")

SATURS = [
    Sakums("Trīs āboli - kā to uzrakstīt ātri?",
           zimejums=bildes([[("abols", 3)]]),
           paraksts="Trīs āboli. Ar ciparu: 3.",
           fakti=["Ciparu ir tikai desmit: 0 1 2 3 4 5 6 7 8 9.",
                  "Katrs cipars aizņem vienu rūtiņu.",
                  "0 nozīmē - nav neviena."]),

    Doma("Cipars pieraksta skaitu",
         "Vispirms saskaiti, tad uzraksti ciparu, kas pasaka, cik ir.",
         soli=[
             "Saskaiti lietas, rādot ar pirkstu.",
             "Atrodi skaitļu joslā to pašu skaitli.",
             "Uzraksti ciparu rūtiņā - no augšas uz leju.",
         ],
         pieze="Ja lietu nav nemaz, raksta 0."),

    Josla("Cipari no 0 līdz 10", lidz=10,
          ievads="Pieskaries ciparam un paskaties, cik daudz tas nozīmē."),

    Izvele("Saskaiti un atrodi ciparu", [
        {"ikona": "zvaigzne", "skaits": 5, "jaut": "Cik zvaigžņu?"},
        {"ikona": "zivs", "skaits": 3, "jaut": "Cik zivju?"},
        {"ikona": "putns", "skaits": 7, "jaut": "Cik putnu?"},
        {"ikona": "sirds", "skaits": 9, "jaut": "Cik siržu?"},
        {"ikona": "masina", "skaits": 4, "jaut": "Cik mašīnu?"},
        {"ikona": "klucis", "skaits": 8, "jaut": "Cik klucīšu?"},
    ], pamats=4, lidz=10,
        ievads="Saskaiti un pieskaries ciparam."),

    Ievadi("Uzraksti ciparu", [
        {"jaut": "Cik ābolu?", "zim": bildes([[("abols", 6)]]),
         "atb": ["6"], "padoms": "Skaiti ar pirkstu."},
        {"jaut": "Cik bumbu?", "zim": bildes([[("bumba", 2)]]),
         "atb": ["2"], "padoms": "Viena, divas."},
        {"jaut": "Cik zivju ir tukšā akvārijā?", "atb": ["0"],
         "padoms": "Nav nevienas - to raksta ar 0."},
        {"jaut": "Cik puķu?", "zim": bildes([[("puke", 5)], [("puke", 4)]]),
         "atb": ["9"], "padoms": "Skaiti abās rindās."},
    ]),

    Varianti("Kurš cipars?", [
        {"jaut": "Septiņi", "opcijas": ["7", "1", "4", "9"], "pareizi": 0,
         "padoms": "Septiņi ir pēc sešiem."},
        {"jaut": "Nulle", "opcijas": ["0", "6", "8", "9"], "pareizi": 0,
         "padoms": "Nulle ir apaļa un tukša."},
        {"jaut": "Seši", "opcijas": ["6", "9", "8", "3"], "pareizi": 0,
         "padoms": "6 un 9 ir līdzīgi - 6 ir ar vēderu apakšā."},
    ]),

    Petijums("Cipari rūtiņu lapā", [
        "Uzraksti rindā visus ciparus no 0 līdz 9.",
        "Katram ciparam - viena rūtiņa, starp tiem - tukša rūtiņa.",
        "Blakus katram ciparam uzzīmē tik aplīšu, cik tas nozīmē.",
    ], vajag="rūtiņu burtnīca, zīmulis"),

    Pasaule("Klases saraksts",
            Ievadi("", [
                {"jaut": "Cik somu ir pie durvīm?",
                 "zim": bildes([[("soma", 4)]]), "atb": ["4"],
                 "padoms": "Skaiti somas."},
                {"jaut": "Cik grāmatu ir plauktā?",
                 "zim": bildes([[("gramata", 7)]]), "atb": ["7"],
                 "padoms": "Skaiti grāmatas."},
                {"jaut": "Cik krēslu ir pie galda?",
                 "zim": bildes([[("kresls", 3)]]), "atb": ["3"],
                 "padoms": "Skaiti krēslus."},
            ]),
            pavediens="skola",
            konteksts="Skolotāja lūdz pierakstīt, cik lietu ir klasē. Vārdus "
                      "rakstīt ir ilgi - ar cipariem ātrāk.",
            kapec="Cipars ir īss pieraksts: 7 ir ātrāk nekā «septiņas»."),

    Kopsavilkums([
        "Zinu visus ciparus no 0 līdz 9.",
        "Saskaitu lietas un uzrakstu, cik to ir.",
        "Zinu, ka 0 nozīmē - nav neviena.",
    ]),

    Majas([
        "Saskaiti karotes virtuvē un uzraksti ciparu.",
        "Uzraksti rūtiņās savu vecumu ar ciparu.",
        "Atrodi mājās 3 vietas, kur redzi ciparus.",
    ]),
]
