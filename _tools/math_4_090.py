# -*- coding: utf-8 -*-
"""4. klase, 90. stunda: «Cik maksās klases brauciens?»

Praktiska problēma ar visām 4.4. prasmēm: budžets klases braucienam.
Skolēns veido izteiksmes, rēķina, salīdzina variantus un izlemj - tieši
tas, ko eksāmenā prasa situāciju uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, restis)

TEMA = "Cik maksās klases brauciens?"

MERKIS = ("Plānosim pasākuma vai ceļojuma budžetu, veidojot izteiksmes un "
          "veicot aprēķinus.")

SATURS = [
    Sakums("Kurp brauksim: Līgatne vai Ventspils?",
           zimejums=restis([["", "Līgatne", "Ventspils"],
                            ["autobuss", "360 €", "540 €"],
                            ["ieeja 1 sk.", "8 €", "5 €"],
                            ["pusdienas 1 sk.", "7 €", "7 €"]],
                           "26 skolēni"),
           fakti=["Autobusu maksā visa klase kopā.",
                  "Ieeju un pusdienas maksā katrs."]),

    Doma("Kopīgās izmaksas + izmaksas katram · skaits",
         "Budžets = kopīgās izmaksas + (izmaksas vienam) · skolēnu skaits; "
         "tad dala ar skolēnu skaitu, lai zinātu, cik katram.",
         soli=[
             "Atdali kopīgās (autobuss) no individuālajām (ieeja, pusdienas).",
             "Individuālās saskaiti vienam: 8 + 7 = 15 €.",
             "Budžets: 360 + 15 · 26.",
             "Katram: budžets : 26.",
         ],
         pieze="Līgatne: 360 + 15 · 26 = 360 + 390 = 750 €."),

    Paraugs("Ventspils budžets",
            uzd="Aprēķini Ventspils brauciena budžetu 26 skolēniem.",
            soli=[
                ("5 + 7 = 12", "Katram."),
                ("12 · 26 = 312", None),
                ("540 + 312 = 852", "Visa klase."),
            ],
            atbilde="852 €"),

    Ievadi("Salīdzini", [
        {"jaut": "Līgatnes budžets: 360 + 15 · 26 = ?", "atb": ["750"],
         "padoms": "360 + 390."},
        {"jaut": "Par cik Ventspils (852 €) dārgāka?", "atb": ["102"],
         "padoms": "852 − 750."},
        {"jaut": "Cik katram skolēnam Līgatnē? 750 : 26 ≈ ? (noapaļo līdz "
                 "veseliem eiro uz augšu)", "atb": ["29"],
         "padoms": "26 · 28 = 728, 26 · 29 = 754."},
        {"jaut": "Ja brauc 30 skolēni, Līgatnes budžets = 360 + 15 · 30 = ?",
         "atb": ["810"], "padoms": "360 + 450."},
    ]),

    Varianti("Kura izteiksme pareiza?", [
        {"jaut": "Autobuss 400 €, katram 12 €, 25 skolēni. Budžets?",
         "opcijas": ["400 + 12 · 25", "(400 + 12) · 25", "400 · 12 + 25"],
         "pareizi": 0, "padoms": "Autobusu maksā vienreiz."},
        {"jaut": "Cik katram, ja budžets 700 € un 28 skolēni?",
         "opcijas": ["700 : 28", "700 · 28", "700 − 28"], "pareizi": 0,
         "padoms": "Sadala vienādi."},
        {"jaut": "Cik ir 700 : 28?",
         "opcijas": ["25", "24", "28", "20"], "pareizi": 0,
         "padoms": "28 · 25 = 700."},
    ]),

    Pasaule("Klase lemj",
            Ievadi("", [
                {"jaut": "Klase krāj 12 € mēnesī katrs, 26 skolēni, 3 mēneši. "
                         "Cik sakrāj? (12 · 26 · 3)",
                 "atb": ["936"], "padoms": "312 · 3."},
                {"jaut": "Vai pietiek Ventspilij (852 €)? Cik paliek?",
                 "atb": ["84"], "padoms": "936 − 852."},
                {"jaut": "Par atlikumu pērk saldējumu pa 3 €. Cik saldējumu?",
                 "atb": ["28"], "padoms": "84 : 3."},
                {"jaut": "Vai katram no 26 skolēniem pietiek pa saldējumam? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "tastatura": "text",
                 "padoms": "28 > 26."},
            ]),
            pavediens="celojums",
            konteksts="Klases braucienu plāno kopā - un katram jāzina, cik "
                      "jāiemaksā.",
            kapec="Budžets pārvērš sapni plānā."),

    Petijums("Mūsu klases brauciens",
             soli=[
                 "Izvēlieties galamērķi un uzziniet cenas (autobuss, ieeja, "
                 "ēdiens).",
                 "Sadaliet izmaksās: kopīgās un katram.",
                 "Uzrakstiet budžeta izteiksmi un aprēķiniet.",
                 "Aprēķiniet, cik katram jāmaksā.",
             ],
             vajag="internets vai skolotājas dotās cenas",
             secinajums="Budžets parāda, vai sapnis ir iespējams un cik "
                        "jākrāj."),

    Kopsavilkums([
        "Nošķiru kopīgās un individuālās izmaksas.",
        "Veidoju budžeta izteiksmi.",
        "Salīdzinu variantus un aprēķinu summu katram.",
    ]),

    Majas([
        "Izplāno ģimenes brīvdienu braucienu un aprēķini budžetu.",
        "Aprēķini, cik katram jāmaksā, ja brauc 4 ģimenes locekļi.",
        "Pastāsti, kuru variantu izvēlētos un kāpēc.",
    ]),
]
