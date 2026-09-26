# -*- coding: utf-8 -*-
"""3. klase, 52. stunda: «Cik dažādi var aprēķināt perimetru?»

Perimetru skolēns jau prot saskaitīt; šeit viņš atklāj, ka to pašu var
izrēķināt trijos veidos, un salīdzina tos. No šī salīdzinājuma nākamajā
stundā izaugs formula - vispirms vārdos, tad ar burtiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Cik dažādi var aprēķināt perimetru?"

MERKIS = ("Aprēķināsim taisnstūra perimetru pa darbībām un kā vienu "
          "izteiksmi un salīdzināsim paņēmienus.")

SATURS = [
    Sakums("Cik metru līstes vajag gleznas rāmim?",
           zimejums=figura([(0, 0), (6, 0), (6, 4), (0, 4)],
                           [(3, -0.6, "6"), (6.8, 2, "4")],
                           "taisnstūris 6 x 4"),
           paraksts="Rāmim vajag visas četras malas - tas ir perimetrs.",
           fakti=["Perimetrs ir visu malu garumu summa.",
                  "Taisnstūrim pretējās malas ir vienādas."]),

    Doma("Perimetru var izrēķināt trijos veidos",
         "Saskaitīt visas četras malas, saskaitīt divas un dubultot vai "
         "izmantot izteiksmi 2 · (a + b).",
         soli=[
             "Pirmais veids: 6 + 4 + 6 + 4 = 20.",
             "Otrais veids: 2 · 6 + 2 · 4 = 12 + 8 = 20.",
             "Trešais veids: 2 · (6 + 4) = 2 · 10 = 20.",
             "Visi trīs dod vienu un to pašu skaitli.",
         ],
         pieze="Trešais veids ir visātrākais: vispirms saskaita divas "
               "blakus malas, tad dubulto. Tieši to dara galdnieks."),

    Paraugs("Cik ir taisnstūra 7 x 3 perimetrs?",
            uzd="Aprēķini taisnstūra ar malām 7 cm un 3 cm perimetru.",
            soli=[
                ("7 + 3 = 10",
                 "Divas blakus malas."),
                ("2 · 10 = 20",
                 "Pretējās malas ir tādas pašas, tāpēc summu dubulto."),
                ("P = 20 cm",
                 "Perimetru raksta kopā ar mērvienību."),
            ],
            atbilde="20 cm"),

    Ievadi("Aprēķini perimetru", [
        {"jaut": "Taisnstūris 5 cm un 3 cm. Cik ir perimetrs centimetros?",
         "atb": ["16"], "padoms": "2 · (5 + 3)."},
        {"jaut": "Taisnstūris 8 cm un 2 cm. Cik ir perimetrs?",
         "atb": ["20"], "padoms": "2 · 10."},
        {"jaut": "Kvadrāts ar malu 6 cm. Cik ir perimetrs?",
         "atb": ["24"], "padoms": "4 · 6."},
        {"jaut": "Taisnstūris 12 cm un 4 cm. Cik ir perimetrs?",
         "atb": ["32"], "padoms": "2 · 16."},
        {"jaut": "Kvadrāts ar malu 9 cm. Cik ir perimetrs?",
         "atb": ["36"], "padoms": "4 · 9."},
        {"jaut": "Taisnstūris 10 cm un 7 cm. Cik ir perimetrs?",
         "atb": ["34"], "padoms": "2 · 17."},
    ], pamats=4,
        ievads="Atbildi raksti centimetros - tikai skaitli."),

    Zimejums("Kvadrāts ir taisnstūris ar vienādām malām",
             figura([(0, 0), (5, 0), (5, 5), (0, 5)],
                    [(2.5, -0.6, "5"), (5.8, 2.5, "5")],
                    "kvadrāts ar malu 5"),
             paskaidro="Kvadrātam visas četras malas ir vienādas, tāpēc "
                       "perimetru var rēķināt arī kā 4 · a.",
             ievads="Tas ir īpašs taisnstūra gadījums."),

    Varianti("Kurš paņēmiens ir ātrākais?", [
        {"jaut": "Kurš rēķins dod taisnstūra 6 x 4 perimetru?",
         "opcijas": ["2 · (6 + 4)", "6 · 4", "6 + 4", "2 · 6 · 4"],
         "pareizi": 0, "padoms": "Perimetrs ir malu summa."},
        {"jaut": "Cik ir kvadrāta ar malu 7 cm perimetrs?",
         "opcijas": ["28 cm", "49 cm", "14 cm", "21 cm"],
         "pareizi": 0, "padoms": "4 · 7."},
        {"jaut": "Taisnstūra perimetrs ir 20 cm, viena mala 6 cm. Cik ir "
                 "otra?",
         "opcijas": ["4 cm", "14 cm", "10 cm", "8 cm"],
         "pareizi": 0, "padoms": "20 : 2 = 10; 10 − 6."},
        {"jaut": "Kas ir perimetrs?",
         "opcijas": ["Visu malu garumu summa", "Rūtiņu skaits figūrā",
                     "Divu malu reizinājums", "Lielākā mala"],
         "pareizi": 0, "padoms": "Tas ir apmales garums."},
    ], pamats=4),

    Pasaule("Cik līstes vajag grīdlīstei?",
            Ievadi("", [
                {"jaut": "Istaba ir 5 m un 4 m. Cik metru ir perimetrs?",
                 "atb": ["18"], "padoms": "2 · 9."},
                {"jaut": "Durvis aizņem 1 m. Cik metru grīdlīstes vajag?",
                 "atb": ["17"], "padoms": "18 − 1."},
                {"jaut": "Otra istaba ir 6 m un 3 m. Cik metru ir tās "
                         "perimetrs?",
                 "atb": ["18"], "padoms": "2 · 9."},
                {"jaut": "Cik metru grīdlīstes vajag abām istabām, ja katrā "
                         "durvis aizņem 1 m?",
                 "atb": ["34"], "padoms": "17 + 17."},
            ]),
            pavediens="maja",
            konteksts="Grīdlīsti pērk metros, un tās garums ir tieši istabas "
                      "perimetrs mīnus durvis.",
            kapec="Ja perimetru izrēķina nepareizi, līste vai nepietiek, vai "
                  "paliek pāri."),

    Kopsavilkums([
        "Aprēķinu taisnstūra perimetru trijos veidos.",
        "Zinu, ka visi trīs dod vienu un to pašu rezultātu.",
        "Izmantoju to, ka pretējās malas ir vienādas.",
        "Rakstu perimetru kopā ar mērvienību.",
    ]),

    Majas([
        "Izmēri savas istabas garumu un platumu un izrēķini perimetru.",
        "Izrēķini to trijos veidos un salīdzini atbildes.",
        "Atrodi mājās priekšmetu, kura perimetrs ir apmēram 1 metrs.",
    ]),
]
