# -*- coding: utf-8 -*-
"""3. klase, 55. stunda: «Cik taisnstūru ar vienādu perimetru?»

Atvērts ģeometrisks uzdevums ar pilnības pamatojumu - tas pats, ko 45. stunda
darīja ar izteiksmēm. Dots perimetrs, meklē visus taisnstūrus; sistēma ir
vienkārša, jo malu summa ir puse no perimetra, un to var pārstaigāt pa vienam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik taisnstūru ar vienādu perimetru?"

MERKIS = ("Zīmēsim rūtiņu tīklā visus taisnstūrus ar dotu perimetru un "
          "pamatosim, ka atrasti visi.")

SATURS = [
    Sakums("Cik dažādu taisnstūru var uzzīmēt ar perimetru 12?",
           zimejums=restis([["a", 1, 2, 3],
                            ["b", 5, 4, 3]],
                           "a + b = 6"),
           paraksts="Malu summa vienmēr ir 6, jo perimetra puse ir 6.",
           fakti=["Perimetra puse ir divu blakus malu summa.",
                  "Tāpēc pietiek atrast visus pārus ar šo summu."]),

    Doma("Meklē malu pārus, kuru summa ir perimetra puse",
         "Ja P = 12, tad a + b = 6 - un tādu pāru veselos skaitļos ir tikai "
         "daži.",
         soli=[
             "Izdali perimetru ar 2 - tā ir divu blakus malu summa.",
             "Sāc ar a = 1 un atrodi b.",
             "Palielini a par vienu un atkārto.",
             "Beidz, kad a kļūst lielāks par b - tālāk taisnstūri atkārtojas.",
         ],
         pieze="Taisnstūris 2 x 4 un 4 x 2 ir viens un tas pats, tikai "
               "pagriezts - tāpēc to skaita vienu reizi."),

    Paraugs("Visi taisnstūri ar perimetru 12",
            uzd="Atrodi visus taisnstūrus ar veselām malām un perimetru "
                "12 cm.",
            soli=[
                ("12 : 2 = 6",
                 "Divu blakus malu summa."),
                ("1 + 5, 2 + 4, 3 + 3",
                 "Visi pāri veselos skaitļos."),
                ("4 + 2 jau bija",
                 "Tālāk pāri atkārtojas, tikai apgriezti."),
                ("Trīs taisnstūri",
                 "1 x 5, 2 x 4 un 3 x 3."),
            ],
            atbilde="trīs taisnstūri"),

    Petijums("Uzzīmē visus taisnstūrus",
             vajag="rūtiņu lapa un zīmulis",
             soli=[
                 "Izvēlies perimetru 16 rūtiņas.",
                 "Izrēķini malu summu.",
                 "Uzzīmē visus taisnstūrus ar veselām malām.",
                 "Pieraksti pie katra tā laukumu un salīdzini.",
             ],
             secinajums="Perimetrs visiem ir vienāds, bet laukums - ne: "
                        "vislielākais laukums ir kvadrātam."),

    Ievadi("Cik taisnstūru?", [
        {"jaut": "P = 12 cm. Cik ir divu blakus malu summa?", "atb": ["6"],
         "padoms": "12 : 2."},
        {"jaut": "P = 12 cm. Cik dažādu taisnstūru ar veselām malām ir?",
         "atb": ["3"], "padoms": "1+5, 2+4, 3+3."},
        {"jaut": "P = 20 cm. Cik ir divu blakus malu summa?", "atb": ["10"],
         "padoms": "20 : 2."},
        {"jaut": "P = 20 cm. Cik dažādu taisnstūru ir?", "atb": ["5"],
         "padoms": "1+9, 2+8, 3+7, 4+6, 5+5."},
        {"jaut": "P = 14 cm, viena mala 5 cm. Cik ir otra?", "atb": ["2"],
         "padoms": "7 − 5."},
        {"jaut": "P = 16 cm. Cik dažādu taisnstūru ir?", "atb": ["4"],
         "padoms": "1+7, 2+6, 3+5, 4+4."},
    ], pamats=4),

    Zimejums("Viens perimetrs, dažādi laukumi",
             restis([["taisnstūris", "1 x 5", "2 x 4", "3 x 3"],
                     ["laukums", 5, 8, 9]],
                    "P = 12 visiem"),
             paskaidro="Vislielākais laukums ir tam taisnstūrim, kura malas "
                       "ir visvienādākās - kvadrātam.",
             ievads="Perimetrs vienāds, laukums - dažāds."),

    Varianti("Vai visi atrasti?", [
        {"jaut": "P = 18 cm. Cik ir malu summa?",
         "opcijas": ["9 cm", "18 cm", "36 cm", "4,5 cm"],
         "pareizi": 0, "padoms": "18 : 2."},
        {"jaut": "P = 18 cm. Cik dažādu taisnstūru ar veselām malām ir?",
         "opcijas": ["4", "3", "5", "9"],
         "pareizi": 0, "padoms": "1+8, 2+7, 3+6, 4+5."},
        {"jaut": "Vai 2 x 4 un 4 x 2 ir divi dažādi taisnstūri?",
         "opcijas": ["Nē, tas ir viens, pagriezts", "Jā, divi dažādi",
                     "Jā, jo malas ir citā secībā", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Pagriežot figūra nemainās."},
        {"jaut": "Kuram no vienāda perimetra taisnstūriem ir lielākais "
                 "laukums?",
         "opcijas": ["Kvadrātam", "Visgarākajam", "Visšaurākajam",
                     "Visiem vienāds"],
         "pareizi": 0, "padoms": "Vienādākas malas - lielāks laukums."},
    ], pamats=4),

    Pasaule("Kā izvēlēties dārza formu?",
            Ievadi("", [
                {"jaut": "Žoga ir 24 m. Cik metru ir divu blakus malu summa?",
                 "atb": ["12"], "padoms": "24 : 2."},
                {"jaut": "Ja viena mala ir 2 m, cik ir otra?",
                 "atb": ["10"], "padoms": "12 − 2."},
                {"jaut": "Cik kvadrātmetru ir šī dārza laukums?",
                 "atb": ["20"], "padoms": "2 · 10."},
                {"jaut": "Cik kvadrātmetru ir kvadrātveida dārzam ar to pašu "
                         "žogu?",
                 "atb": ["36"], "padoms": "6 · 6."},
            ]),
            pavediens="maja",
            konteksts="Ar vienu un to pašu žoga garumu dārzs var būt šaurs un "
                      "garš vai gandrīz kvadrātisks.",
            kapec="Kvadrātveida dārzā ietilpst gandrīz divreiz vairāk dobju."),

    Kopsavilkums([
        "Atrodu visus taisnstūrus ar dotu perimetru.",
        "Zinu, ka divu blakus malu summa ir perimetra puse.",
        "Pamatoju, ka atrasti visi varianti.",
        "Zinu, ka vienādam perimetram laukums var būt dažāds.",
    ]),

    Majas([
        "Uzzīmē visus taisnstūrus ar perimetru 14 rūtiņas.",
        "Pieraksti pie katra tā laukumu.",
        "Atrodi to, kuram laukums ir vislielākais.",
    ]),
]
