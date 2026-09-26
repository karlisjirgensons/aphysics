# -*- coding: utf-8 -*-
"""4. klase, 39. stunda: «Kā reizina rakstos?»

Stabiņš trīsciparu skaitlim: vieni, desmiti, simti - katrā solī «prātā»
paturētais pievienojas nākamajai šķirai. Skolēns komentē katru soli, jo
tieši komentārs atklāj aizmirstu pārnesumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kā reizina rakstos?"

MERKIS = ("Reizināsim rakstos trīsciparu skaitli ar viencipara skaitli, "
          "komentējot vienus, desmitus un simtus.")

SATURS = [
    Sakums("Cik kilogramu siena apēd 7 govis mēnesī?",
           zimejums=restis([["", "", "3", "6", "8"],
                            ["·", "", "", "", "7"],
                            ["", "2", "5", "7", "6"]],
                           "368 · 7 stabiņā"),
           paraksts="368 kg vienai govij - 7 govīm 2576 kg.",
           fakti=["Govs mēnesī var apēst vairākus simtus kilogramu siena.",
                  "Stabiņš ar pārnešanu - drošākais ceļš."]),

    Doma("No vieniem uz simtiem, paturot prātā",
         "Reizini katru šķiru; ja sanāk 10 vai vairāk, raksti vienus un "
         "desmitus pārnes uz nākamo šķiru.",
         soli=[
             "8 · 7 = 56: raksta 6, 5 prātā.",
             "6 · 7 = 42, 42 + 5 = 47: raksta 7, 4 prātā.",
             "3 · 7 = 21, 21 + 4 = 25: raksta 25.",
             "Rezultāts 2576. Aptuveni: 400 · 7 = 2800 - tuvu.",
         ],
         pieze="Pārnesto pieskaita *pēc* reizināšanas, nevis pirms tās."),

    Paraugs("457 · 6",
            uzd="Sareizini 457 · 6 stabiņā.",
            soli=[
                ("7 · 6 = 42", "Raksta 2, 4 prātā."),
                ("5 · 6 + 4 = 34", "Raksta 4, 3 prātā."),
                ("4 · 6 + 3 = 27", "Raksta 27."),
                ("457 · 6 = 2742", None),
            ],
            atbilde="2742"),

    Slidnis("Stabiņš soli pa solim: 238 · 4",
            soli=[
                {"v": "8 · 4 = 32", "teksts": "Raksta 2, prātā 3."},
                {"v": "3 · 4 + 3 = 15", "teksts": "Raksta 5, prātā 1."},
                {"v": "2 · 4 + 1 = 9", "teksts": "Raksta 9."},
                {"v": "238 · 4 = 952", "teksts": "Pārbaude: 240 · 4 = 960 "
                 "- tuvu."},
            ]),

    Ievadi("Stabiņā", [
        {"jaut": "238 · 4 = ?", "atb": ["952"], "padoms": "32, 15, 9."},
        {"jaut": "175 · 6 = ?", "atb": ["1050"], "padoms": "30, 45, 10."},
        {"jaut": "368 · 7 = ?", "atb": ["2576"], "padoms": "56, 47, 25."},
        {"jaut": "509 · 8 = ?", "atb": ["4072"],
         "padoms": "9 · 8 = 72; 0 · 8 + 7 = 7; 5 · 8 = 40."},
        {"jaut": "684 · 9 = ?", "atb": ["6156"], "padoms": "36, 75, 61."},
        {"jaut": "777 · 3 = ?", "atb": ["2331"], "padoms": "21, 23, 23."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "Rūta: 246 · 3 = 628. Kas nav kārtībā?",
         "opcijas": ["aizmirsa pārnesto no vieniem",
                     "sajauca šķiras", "viss pareizi"], "pareizi": 0,
         "padoms": "6 · 3 = 18 - 1 prātā. Pareizi 738."},
        {"jaut": "Kārlis: 135 · 4 = 5420. Kas nav kārtībā?",
         "opcijas": ["pārnesto uzrakstīja kā ciparu",
                     "viss pareizi", "reizināja ar 5"], "pareizi": 0,
         "padoms": "Pareizi 540."},
        {"jaut": "406 · 5: kas notiek desmitu šķirā?",
         "opcijas": ["0 · 5 + 3 = 3", "0 · 5 = 0", "6 · 5 = 30",
                     "4 · 5 = 20"], "pareizi": 0,
         "padoms": "No vieniem 30 - 3 prātā."},
    ]),

    Pasaule("Fermas aprēķini",
            Ievadi("", [
                {"jaut": "Viena govs dienā dod 26 l piena. Cik litru 7 "
                         "dienās?",
                 "atb": ["182"], "padoms": "26 · 7."},
                {"jaut": "Fermā 8 govis, katra nedēļā dod 182 l. Cik litru "
                         "visas?",
                 "atb": ["1456"], "padoms": "182 · 8."},
                {"jaut": "Vistas nedēļā izdēj 365 olas. Cik olu 4 nedēļās?",
                 "atb": ["1460"], "padoms": "365 · 4."},
                {"jaut": "Siena ķīpa sver 245 kg. Cik sver 6 ķīpas?",
                 "atb": ["1470"], "padoms": "245 · 6."},
            ]),
            pavediens="daba",
            konteksts="Saimnieki rēķina barību un produkciju nedēļām un "
                      "mēnešiem uz priekšu.",
            kapec="Stabiņā var sareizināt jebkurus skaitļus bez "
                  "kalkulatora."),

    Kopsavilkums([
        "Reizinu trīsciparu skaitli ar viencipara skaitli stabiņā.",
        "Komentēju katru soli un pārnesto.",
        "Pārbaudu ar aptuveno vērtību.",
    ]),

    Majas([
        "Izrēķini stabiņā, cik dienu ir četros parastos gados (365 · 4).",
        "Izdomā vienu stabiņu ar trim pārnesumiem.",
        "Paskaidro mājiniekiem, ko nozīmē «prātā».",
    ]),
]
