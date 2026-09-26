# -*- coding: utf-8 -*-
"""3. klase, 118. stunda: «Vai dažādām figūrām var būt vienāds laukums?»

Atvērts uzdevums ar pilnības pamatojumu - tas pats paņēmiens, kas 55. stundā
darbojās ar perimetru. Dots laukums, meklē visus taisnstūrus; sistēma ir
dalītāju pāri, kurus skolēns jau prot atrast no 14. stundas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Vai dažādām figūrām var būt vienāds laukums?"

MERKIS = ("Zīmēsim dažādus taisnstūrus ar vienādu laukumu un pamatosim "
          "atbildi.")

SATURS = [
    Sakums("Cik dažādu taisnstūru ar laukumu 24 var uzzīmēt?",
           zimejums=restis([["a", 1, 2, 3, 4],
                            ["b", 24, 12, 8, 6]],
                           "a · b = 24"),
           paraksts="Katrs dalītāju pāris dod vienu taisnstūri.",
           fakti=["Viens laukums - daudzi dažādi taisnstūri.",
                  "Malu garumi ir laukuma dalītāji."]),

    Doma("Meklē dalītāju pārus",
         "Ja laukums ir 24, tad malas ir divi skaitļi, kuru reizinājums ir "
         "24 - un tādu pāru ir tieši tik, cik dalītāju.",
         soli=[
             "Sāc ar a = 1 un atrodi b.",
             "Palielini a par vienu un pārbaudi, vai laukums dalās.",
             "Turpini, līdz a kļūst lielāks par b.",
             "Katrs atrastais pāris ir viens taisnstūris.",
         ],
         pieze="Perimetri visiem šiem taisnstūriem ir dažādi: 1 x 24 dod 50, "
               "bet 4 x 6 tikai 20."),

    Petijums("Uzzīmē visus taisnstūrus",
             vajag="rūtiņu lapa un zīmulis",
             soli=[
                 "Izvēlies laukumu 24 rūtiņas.",
                 "Uzzīmē visus taisnstūrus ar veselām malām.",
                 "Pieraksti pie katra tā perimetru.",
                 "Atrodi to, kuram perimetrs ir vismazākais.",
             ],
             secinajums="Laukums visiem ir vienāds, bet perimetri atšķiras - "
                        "vismazākais ir tam, kas vistuvāk kvadrātam."),

    Paraugs("Kādi taisnstūri dod laukumu 24?",
            uzd="Atrodi visus taisnstūrus ar veselām malām un laukumu 24.",
            soli=[
                ("1 · 24, 2 · 12",
                 "Pirmie divi dalītāju pāri."),
                ("3 · 8, 4 · 6",
                 "Vēl divi pāri."),
                ("5 neder, 6 · 4 jau bija",
                 "Malas satikās - visi atrasti."),
            ],
            atbilde="četri taisnstūri"),

    Ievadi("Atrodi otru malu", [
        {"jaut": "Laukums 24, viena mala 4. Cik ir otra?", "atb": ["6"],
         "padoms": "24 : 4."},
        {"jaut": "Laukums 24, viena mala 3. Cik ir otra?", "atb": ["8"],
         "padoms": "24 : 3."},
        {"jaut": "Laukums 36, viena mala 6. Cik ir otra?", "atb": ["6"],
         "padoms": "36 : 6."},
        {"jaut": "Cik dažādu taisnstūru ar veselām malām dod laukumu 24?",
         "atb": ["4"], "padoms": "1·24, 2·12, 3·8, 4·6."},
        {"jaut": "Laukums 24, malas 4 un 6. Cik ir perimetrs?",
         "atb": ["20"], "padoms": "2 · 10."},
        {"jaut": "Laukums 24, malas 1 un 24. Cik ir perimetrs?",
         "atb": ["50"], "padoms": "2 · 25."},
    ], pamats=4),

    Zimejums("Viens laukums, dažādi perimetri",
             restis([["taisnstūris", "1 x 24", "2 x 12", "3 x 8", "4 x 6"],
                     ["perimetrs", 50, 28, 22, 20]],
                    "laukums visiem 24"),
             paskaidro="Jo tuvāk kvadrātam, jo mazāks perimetrs pie tā paša "
                       "laukuma.",
             ievads="Salīdzini apakšējo rindu."),

    Varianti("Cik taisnstūru ir?", [
        {"jaut": "Cik dažādu taisnstūru ar veselām malām dod laukumu 12?",
         "opcijas": ["3", "4", "2", "6"],
         "pareizi": 0, "padoms": "1·12, 2·6, 3·4."},
        {"jaut": "Kuram taisnstūrim ar laukumu 24 perimetrs ir vismazākais?",
         "opcijas": ["4 x 6", "1 x 24", "2 x 12", "3 x 8"],
         "pareizi": 0, "padoms": "Vistuvāk kvadrātam."},
        {"jaut": "Vai 3 x 8 un 8 x 3 ir divi dažādi taisnstūri?",
         "opcijas": ["Nē, tas ir viens, pagriezts", "Jā",
                     "Jā, jo malas citā secībā", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Pagriežot figūra nemainās."},
        {"jaut": "Cik dažādu taisnstūru dod laukumu 16?",
         "opcijas": ["3", "2", "4", "5"],
         "pareizi": 0, "padoms": "1·16, 2·8, 4·4."},
    ], pamats=4),

    Pasaule("Kāda forma dārzam ir izdevīgāka?",
            Ievadi("", [
                {"jaut": "Dārzs 4 m x 6 m. Cik kvadrātmetru ir laukums?",
                 "atb": ["24"], "padoms": "4 · 6."},
                {"jaut": "Cik metru žoga vajag? (perimetrs)", "atb": ["20"],
                 "padoms": "2 · 10."},
                {"jaut": "Dārzs 2 m x 12 m. Cik metru žoga vajag?",
                 "atb": ["28"], "padoms": "2 · 14."},
                {"jaut": "Par cik metriem mazāk žoga vajag pirmajam dārzam?",
                 "atb": ["8"], "padoms": "28 − 20."},
            ]),
            pavediens="maja",
            konteksts="Dārzam ar vienādu laukumu žoga var vajadzēt ļoti "
                      "dažādi - tas atkarīgs no formas.",
            kapec="Kvadrātiskam dārzam žoga vajag vismazāk."),

    Kopsavilkums([
        "Atrodu visus taisnstūrus ar dotu laukumu.",
        "Meklēju malas kā laukuma dalītāju pārus.",
        "Pamatoju, ka atrasti visi varianti.",
        "Zinu, ka vienādam laukumam perimetrs var būt dažāds.",
    ]),

    Majas([
        "Uzzīmē visus taisnstūrus ar laukumu 18 rūtiņas.",
        "Pieraksti pie katra perimetru.",
        "Atrodi to, kuram perimetrs ir vismazākais.",
    ]),
]
