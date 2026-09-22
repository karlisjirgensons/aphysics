# -*- coding: utf-8 -*-
"""6. klase, 119. stunda: «Kāda figūra sanāks?»

Uzdevums ar atvērtu atbildi: doti nosacījumi, figūra jāizdomā pašam. Te
satiekas koordinātas un ģeometrijas zināšanas no iepriekšējām klasēm - un
atbilžu parasti ir vairākas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kāda figūra sanāks?"

MERKIS = ("Veidosim figūru pēc dotiem nosacījumiem un raksturosim tās "
          "īpašības.")

SATURS = [
    Sakums("Nosacījumi ir doti, figūra - nav",
           zimejums=plakne(lauzta=[(-2, 2), (2, 2), (2, -2), (-2, -2)],
                           aizpildi=True, no_x=-4, lidz_x=4, no_y=-4,
                           lidz_y=4, solis=1),
           paraksts="Kvadrāts ar malu 4, kura centrs ir sākumpunktā. "
                    "Nosacījumiem atbilst tikai viena šāda figūra.",
           fakti=["Nosacījumi var atstāt vienu vai vairākas iespējas.",
                  "Vienmēr jāpārbauda, vai figūra tiešām atbilst visiem.",
                  "Simetriska figūra ap sākumpunktu ir viegli aprakstāma."]),

    Doma("Vispirms zīmē, tad pārbaudi visus nosacījumus",
         "Figūru pēc nosacījumiem veido pakāpeniski: izvēlas pirmo virsotni, "
         "pārējās atrod pēc nosacījumiem un beigās pārbauda visu.",
         soli=[
             "Izlasi visus nosacījumus un pasvītro katru atsevišķi.",
             "Sāc ar to nosacījumu, kas visvairāk ierobežo.",
             "Atliec virsotnes un savieno tās.",
             "Pārbaudi katru nosacījumu pēc kārtas.",
             "Pieraksti figūras īpašības: malas, laukumu, simetriju.",
         ],
         pieze="Ja nosacījumi neierobežo visu, atbilžu ir vairākas - un tad "
               "der jebkura no tām. Svarīgi ir pamatot, kāpēc izvēlētā "
               "figūra atbilst."),

    Paraugs("Uzzīmē pēc nosacījumiem",
            uzd="Uzzīmē kvadrātu, kura centrs ir sākumpunktā un mala ir "
                "4 vienības.",
            soli=[
                ("Centrs sākumpunktā nozīmē simetriju",
                 "Virsotnes ir simetriskas pret abām asīm."),
                ("Mala 4 nozīmē, ka no centra līdz malai ir 2",
                 "Puse no malas."),
                ("Virsotnes: (−2; 2), (2; 2), (2; −2), (−2; −2)",
                 "Visas četras."),
                ("Pārbaude: malas garums no −2 līdz 2 ir 4",
                 "Nosacījums izpildīts."),
            ],
            atbilde="kvadrāts ar virsotnēm (±2; ±2)"),

    Ievadi("Pārbaudi nosacījumus", [
        {"jaut": "Kvadrāta mala ir 4, centrs sākumpunktā. Cik vienības no "
                 "centra līdz malai?",
         "atb": ["2"], "padoms": "Puse no malas."},
        {"jaut": "Kāds ir šī kvadrāta laukums kvadrātvienībās?",
         "atb": ["16"], "padoms": "4 · 4."},
        {"jaut": "Kāds ir tā perimetrs?",
         "atb": ["16"], "padoms": "4 · 4."},
        {"jaut": "Taisnstūra virsotnes ir (−3; 1), (3; 1), (3; −1), (−3; −1). "
                 "Cik vienības gara ir garākā mala?",
         "atb": ["6"], "padoms": "No −3 līdz 3."},
        {"jaut": "Kāds ir tā laukums?",
         "atb": ["12"], "padoms": "6 · 2."},
        {"jaut": "Trīsstūris ar virsotnēm (0; 0), (6; 0), (0; 4). Kāds ir tā "
                 "laukums?",
         "atb": ["12"], "padoms": "Puse no 6 · 4."},
    ], pamats=4),

    Petijums("Izdomā figūru pēc nosacījumiem",
             vajag="rūtiņu lapa",
             soli=[
                 "Uzzīmē taisnstūri, kura laukums ir 12 kvadrātvienības.",
                 "Pieraksti tā virsotņu koordinātas.",
                 "Atrodi vēl vienu taisnstūri ar to pašu laukumu.",
                 "Salīdzini abu perimetrus.",
                 "Pieraksti, kuram perimetrs ir mazāks un kāpēc.",
             ],
             secinajums="Pie vienāda laukuma mazākais perimetrs ir tam "
                        "taisnstūrim, kura malas ir tuvāk viena otrai."),

    Varianti("Vai figūra atbilst?", [
        {"jaut": "Kvadrāta centrs ir sākumpunktā, mala 6. Kāda ir viena "
                 "virsotne?",
         "opcijas": ["(3; 3)", "(6; 6)", "(3; 0)", "(0; 6)"],
         "pareizi": 0,
         "padoms": "Puse no malas katrā virzienā."},
        {"jaut": "Cik taisnstūru ar veselām virsotnēm var uzzīmēt ar laukumu "
                 "12?",
         "opcijas": ["Vairāki", "Tikai viens", "Neviens", "Tieši divi"],
         "pareizi": 0,
         "padoms": "1 x 12, 2 x 6, 3 x 4."},
        {"jaut": "Figūra ar virsotnēm (0; 0), (4; 0), (4; 4), (0; 4) ir...",
         "opcijas": ["kvadrāts", "taisnstūris, kas nav kvadrāts",
                     "trīsstūris", "rombs, kas nav kvadrāts"],
         "pareizi": 0,
         "padoms": "Abas malas ir 4."},
        {"jaut": "Ja nosacījumiem atbilst vairākas figūras, tad...",
         "opcijas": ["der jebkura no tām", "uzdevums ir kļūdains",
                     "jāizvēlas lielākā", "atbildes nav"],
         "pareizi": 0,
         "padoms": "Galvenais ir pamatot izvēli."},
    ], pamats=4),

    Pasaule("Kā iezīmēt laukumu?",
            Ievadi("", [
                {"jaut": "Spēles laukumam jābūt 24 kvadrātvienības ar malām "
                         "6 un 4. Kāds ir tā perimetrs?",
                 "atb": ["20"], "padoms": "2 · (6 + 4)."},
                {"jaut": "Cits laukums ar to pašu laukumu, malas 8 un 3. "
                         "Kāds ir tā perimetrs?",
                 "atb": ["22"], "padoms": "2 · (8 + 3)."},
                {"jaut": "Kuram vajag mazāk marķēšanas lentes? Ieraksti "
                         "mazāko perimetru.",
                 "atb": ["20"], "padoms": "Salīdzina abus."},
                {"jaut": "Trešais variants ar malām 12 un 2. Kāds ir tā "
                         "perimetrs?",
                 "atb": ["28"], "padoms": "2 · (12 + 2)."},
            ]),
            pavediens="sports",
            konteksts="Spēles laukumu var iezīmēt dažādi, bet lentes "
                      "patēriņš atšķiras.",
            kapec="Vienāds laukums nenozīmē vienādu perimetru."),

    Zimejums("Divi taisnstūri ar vienādu laukumu",
             plakne(lauzta=[(-3, 2), (3, 2), (3, -2), (-3, -2)],
                    aizpildi=True, no_x=-5, lidz_x=5, no_y=-4, lidz_y=4,
                    solis=1),
             paskaidro="Šim taisnstūrim malas ir 6 un 4, laukums 24. "
                       "Taisnstūrim 8 x 3 laukums ir tāds pats, bet perimetrs "
                       "lielāks.",
             ievads="Laukums viens, forma cita."),

    Kopsavilkums([
        "Veidoju figūru pēc dotiem nosacījumiem.",
        "Pārbaudu katru nosacījumu atsevišķi.",
        "Raksturoju figūras malas, laukumu un perimetru.",
        "Zinu, ka nosacījumiem var atbilst vairākas figūras.",
    ]),

    Majas([
        "Uzzīmē taisnstūri ar laukumu 18 kvadrātvienības.",
        "Atrodi vēl divus taisnstūrus ar to pašu laukumu.",
        "Pieraksti, kuram no tiem ir vismazākais perimetrs.",
    ]),
]
