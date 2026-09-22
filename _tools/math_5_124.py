# -*- coding: utf-8 -*-
"""5. klase, 124. stunda: «Vai apgalvojums par figūrām ir patiess?»

Mikrotemata noslēgums un 113. stundas pāriniece: tur apgalvojumi bija par
leņķiem, te - par figūrām. Paņēmiens ir tas pats, un tieši tāpēc to ir vērts
atkārtot citā vietā: pretpiemērs strādā vienmēr, lai par ko būtu runa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Vai apgalvojums par figūrām ir patiess?"

MERKIS = ("Mācīsimies noteikt un pamatot apgalvojuma par daudzstūru "
          "lielumiem patiesumu.")

SATURS = [
    Sakums("Divas figūras, viens perimetrs",
           zimejums=figura([(0, 0), (6, 0), (6, 2), (0, 2)],
                           virsraksts="Taisnstūris 6 x 2"),
           paraksts="Perimetrs 16, laukums 12. Kvadrātam 4 x 4 perimetrs ir "
                    "tāds pats, bet laukums 16.",
           fakti=["«Vienāds perimetrs nozīmē vienādu laukumu» - vai tā ir?",
                  "6 x 2 un 4 x 4 abiem perimetrs ir 16.",
                  "Bet laukumi ir 12 un 16."]),

    Doma("Pretpiemērs der arī figūrām",
         "Apgalvojumu par figūrām pārbauda ar piemēriem; viens pretpiemērs to "
         "apgāž, bet pierādīt var tikai ar sakarību.",
         soli=[
             "Izlasi apgalvojumu un saproti, par ko tas ir.",
             "Pamēģini to ar divām trim figūrām.",
             "Ja atrodi neatbilstošu - apgalvojums ir nepatiess.",
             "Ja neatrodi, pamato ar zināmu sakarību.",
             "Pieraksti pamatojumu vienā teikumā.",
         ],
         pieze="Perimetrs un laukums ir divi dažādi lielumi, un viens otru "
               "nenosaka. Tieši tāpēc lielākā daļa apgalvojumu, kas tos "
               "saista, izrādās nepatiesi."),

    Paraugs("«Vienāds perimetrs - vienāds laukums»",
            uzd="Nosaki, vai apgalvojums ir patiess, un pamato.",
            soli=[
                ("Taisnstūris 6 x 2: P = 16, S = 12",
                 "Pirmā figūra."),
                ("Kvadrāts 4 x 4: P = 16, S = 16",
                 "Otrā figūra."),
                ("Perimetri ir vienādi",
                 "Abiem 16."),
                ("Laukumi atšķiras: 12 un 16",
                 "Apgalvojums ir nepatiess."),
            ],
            atbilde="Apgalvojums ir nepatiess"),

    Ievadi("Aprēķini un salīdzini", [
        {"jaut": "Taisnstūris 6 x 2. Cik ir perimetrs?",
         "atb": ["16"], "padoms": "(6 + 2) · 2."},
        {"jaut": "Taisnstūris 6 x 2. Cik ir laukums?",
         "atb": ["12"], "padoms": "6 · 2."},
        {"jaut": "Kvadrāts 4 x 4. Cik ir perimetrs?",
         "atb": ["16"], "padoms": "4 · 4."},
        {"jaut": "Kvadrāts 4 x 4. Cik ir laukums?",
         "atb": ["16"], "padoms": "4 · 4."},
        {"jaut": "Taisnstūris 7 x 1. Cik ir perimetrs?",
         "atb": ["16"], "padoms": "(7 + 1) · 2."},
        {"jaut": "Taisnstūris 7 x 1. Cik ir laukums?",
         "atb": ["7"], "padoms": "7 · 1."},
        {"jaut": "Taisnstūris 5 x 3. Cik ir perimetrs?",
         "atb": ["16"], "padoms": "(5 + 3) · 2."},
        {"jaut": "Taisnstūris 5 x 3. Cik ir laukums?",
         "atb": ["15"], "padoms": "5 · 3."},
    ], pamats=4,
        ievads="Visiem šiem taisnstūriem perimetrs ir 16 - salīdzini "
               "laukumus."),

    Zimejums("Tas pats perimetrs, cits laukums",
             figura([(0, 0), (4, 0), (4, 4), (0, 4)],
                    virsraksts="Kvadrāts 4 x 4"),
             paskaidro="Perimetrs arī šeit ir 16, bet laukums ir 16, nevis "
                       "12. Ar šo vienu zīmējumu pietiek, lai apgalvojumu "
                       "apgāztu.",
             ievads="Otra figūra ar to pašu perimetru."),

    Varianti("Patiess vai nepatiess?", [
        {"jaut": "«Vienāds perimetrs nozīmē vienādu laukumu.»",
         "opcijas": ["Nepatiess", "Patiess", "Tikai kvadrātiem",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "6 x 2 un 4 x 4."},
        {"jaut": "«Kvadrāts ir taisnstūris.»",
         "opcijas": ["Patiess", "Nepatiess", "Tikai reizēm",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Visi leņķi taisni."},
        {"jaut": "«Katrs taisnstūris ir kvadrāts.»",
         "opcijas": ["Nepatiess", "Patiess", "Tikai maziem",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "6 x 2 nav kvadrāts."},
        {"jaut": "«Lielāks laukums nozīmē lielāku perimetru.»",
         "opcijas": ["Nepatiess", "Patiess", "Tikai kvadrātiem",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "4 x 4 un 7 x 1 - salīdzini."},
        {"jaut": "«Četrstūra leņķu summa ir 360°.»",
         "opcijas": ["Patiess", "Nepatiess", "Tikai izliektiem",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Divi trijstūri."},
        {"jaut": "Kā apgāž apgalvojumu par figūrām?",
         "opcijas": ["Ar vienu pretpiemēru", "Ar desmit piemēriem",
                     "Ar mērījumu", "Apgāzt nevar"],
         "pareizi": 0,
         "padoms": "Tāpat kā ar leņķiem."},
    ], pamats=4),

    Pasaule("Kurš dārziņš ir izdevīgāks?",
            Ievadi("", [
                {"jaut": "Dārziņš 6 m x 2 m. Cik metru žoga vajag?",
                 "atb": ["16"], "padoms": "(6 + 2) · 2."},
                {"jaut": "Cik kvadrātmetru ir tā laukums?",
                 "atb": ["12"], "padoms": "6 · 2."},
                {"jaut": "Dārziņš 4 m x 4 m. Cik kvadrātmetru ir laukums?",
                 "atb": ["16"], "padoms": "4 · 4."},
                {"jaut": "Cik metru žoga vajag otrajam dārziņam?",
                 "atb": ["16"], "padoms": "4 · 4."},
            ]),
            pavediens="skola",
            konteksts="Skolas dārziņam žogu pērk metros, bet stādus - pēc "
                      "laukuma.",
            kapec="Ar vienādu žogu var iegūt dažāda lieluma dārziņu."),

    Kopsavilkums([
        "Nosaku, vai apgalvojums par figūrām ir patiess.",
        "Apgāžu nepatiesu apgalvojumu ar pretpiemēru.",
        "Aprēķinu perimetru un laukumu, lai pamatotu atbildi.",
        "Zinu, ka perimetrs un laukums viens otru nenosaka.",
    ]),

    Majas([
        "Atrodi visus taisnstūrus ar perimetru 20 un veselām malām.",
        "Pieraksti, kuram no tiem ir vislielākais laukums.",
        "Uzraksti vienu patiesu un vienu nepatiesu apgalvojumu par figūrām.",
    ]),
]
