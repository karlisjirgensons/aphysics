# -*- coding: utf-8 -*-
"""6. klase, 114. stunda: «Ko var secināt starp mērījumiem?»

Grafiks rāda ne tikai punktus, bet arī to, kas notika starp tiem. Secinājumu
te formulē vārdiem, un galvenais jautājums ir: ko mēs tiešām zinām un ko
tikai pieņemam?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Ko var secināt starp mērījumiem?"

MERKIS = ("Formulēsim secinājumus par lieluma izmaiņām starp diviem "
          "mērījumiem.")

SATURS = [
    Sakums("Starp diviem punktiem līnija ir mūsu pieņēmums",
           zimejums=plakne(lauzta=[(0, -4), (6, 2)],
                           no_x=0, lidz_x=6, no_y=-6, lidz_y=4, solis=2,
                           x_nos="h", y_nos="°C"),
           paraksts="Mēs zinām tikai divus mērījumus. Līnija starp tiem "
                    "pieņem, ka izmaiņa bija vienmērīga.",
           fakti=["Punkti ir mērījumi, līnija - pieņēmums.",
                  "Starp diviem mērījumiem var secināt izmaiņas virzienu.",
                  "Precīzu vērtību starp mērījumiem nezina neviens."]),

    Doma("Secini virzienu un ātrumu, ne precīzu vērtību",
         "Starp diviem mērījumiem var pateikt, vai lielums auga vai sarūka "
         "un cik strauji, bet ne to, kāda tieši bija vērtība katrā brīdī.",
         soli=[
             "Salīdzini abu mērījumu vērtības.",
             "Nosaki virzienu: auga, sarūka vai palika tāds pats.",
             "Aprēķini izmaiņu: lielākā un mazākā starpību.",
             "Izdali izmaiņu ar laiku - tas ir izmaiņas ātrums.",
             "Pieraksti secinājumu ar skaitli un mērvienību.",
         ],
         pieze="Stāvāka līnija nozīmē straujāku izmaiņu. Divi grafiki ar "
               "vienādu sākumu un beigām var izskatīties pavisam dažādi - "
               "tāpēc starp mērījumiem secina tikai vidējo."),

    Paraugs("Ko zinām un ko pieņemam?",
            uzd="Pie 0 h bija −4 °C, pie 6 h - 2 °C. Ko var secināt?",
            soli=[
                ("Temperatūra auga",
                 "No −4 līdz 2."),
                ("Izmaiņa: 2 − (−4) = 6 grādi",
                 "Kopējais pieaugums."),
                ("6 grādi 6 stundās - vidēji 1 grāds stundā",
                 "Izmaiņas ātrums."),
                ("Pie 3 h *iespējams* bija −1 °C",
                 "Bet to mēs nezinām droši."),
            ],
            atbilde="auga par 6 grādiem, vidēji 1 grāds stundā"),

    Ievadi("Ko rāda izmaiņa?", [
        {"jaut": "No −4 °C līdz 2 °C. Par cik grādiem pieauga?",
         "atb": ["6"], "padoms": "2 − (−4)."},
        {"jaut": "Tas notika 6 stundās. Cik grādu stundā vidēji?",
         "atb": ["1"], "padoms": "6 : 6."},
        {"jaut": "No 3 °C līdz −5 °C. Par cik grādiem samazinājās?",
         "atb": ["8"], "padoms": "3 + 5."},
        {"jaut": "Tas notika 4 stundās. Cik grādu stundā vidēji?",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "No −10 °C līdz −2 °C 4 stundās. Cik grādu stundā vidēji?",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "No −6 °C līdz −6 °C 5 stundās. Cik grādu stundā vidēji?",
         "atb": ["0"], "padoms": "Izmaiņas nav."},
    ], pamats=4),

    Varianti("Ko drīkst secināt?", [
        {"jaut": "Zināmi divi mērījumi. Ko drīkst pateikt par vidu?",
         "opcijas": ["Tikai to, ka lielums kopumā auga vai sarūka",
                     "Precīzu vērtību", "Ka izmaiņa bija vienmērīga",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Līnija ir pieņēmums."},
        {"jaut": "Stāvāka līnija nozīmē...",
         "opcijas": ["straujāku izmaiņu", "lielāku vērtību",
                     "garāku laiku", "kļūdu"],
         "pareizi": 0,
         "padoms": "Vairāk izmaiņas vienā laika vienībā."},
        {"jaut": "Horizontāla līnija nozīmē...",
         "opcijas": ["lielums nemainījās", "lielums auga",
                     "lielums sarūka", "mērījumu trūkst"],
         "pareizi": 0,
         "padoms": "Vērtība palika tā pati."},
        {"jaut": "No −4 līdz 2 grādiem izmaiņa ir...",
         "opcijas": ["6 grādi", "2 grādi", "−2 grādi", "4 grādi"],
         "pareizi": 0,
         "padoms": "Attālums uz skaitļu taisnes."},
    ], pamats=4),

    Pasaule("Cik strauji mainījās?",
            Ievadi("", [
                {"jaut": "No 6:00 (−8 °C) līdz 12:00 (4 °C). Par cik grādiem "
                         "pieauga?",
                 "atb": ["12"], "padoms": "8 + 4."},
                {"jaut": "Cik stundas tas bija?",
                 "atb": ["6"], "padoms": "No 6 līdz 12."},
                {"jaut": "Cik grādu stundā vidēji?",
                 "atb": ["2"], "padoms": "12 : 6."},
                {"jaut": "No 12:00 (4 °C) līdz 18:00 (−2 °C). Cik grādu "
                         "stundā vidēji tā krita?",
                 "atb": ["1"], "padoms": "6 grādi 6 stundās."},
            ]),
            pavediens="planeta",
            konteksts="Meteorologi vērtē nevis atsevišķus mērījumus, bet to, "
                      "cik strauji temperatūra mainās.",
            kapec="Izmaiņas ātrums ir izmaiņa, dalīta ar laiku."),

    Zimejums("Divi ceļi starp tiem pašiem punktiem",
             plakne(lauzta=[(0, -4), (2, -3), (4, -3), (6, 2)],
                    no_x=0, lidz_x=6, no_y=-6, lidz_y=4, solis=2,
                    x_nos="h", y_nos="°C"),
             paskaidro="Sākums un beigas ir tie paši, kas stundas sākumā, "
                       "bet ceļš - pavisam cits. Abi atbilst mērījumiem.",
             ievads="Tāpēc starp mērījumiem secina tikai vidējo."),

    Kopsavilkums([
        "Nosaku izmaiņas virzienu starp diviem mērījumiem.",
        "Aprēķinu izmaiņas lielumu un vidējo ātrumu.",
        "Zinu, ka līnija starp punktiem ir pieņēmums.",
        "Formulēju secinājumu ar skaitli un mērvienību.",
    ]),

    Majas([
        "Atrodi laika ziņās divus mērījumus un aprēķini vidējo izmaiņu.",
        "Uzzīmē divus dažādus ceļus starp tiem pašiem punktiem.",
        "Pieraksti, ko no grafika zinām droši un ko tikai pieņemam.",
    ]),
]
