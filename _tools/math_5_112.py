# -*- coding: utf-8 -*-
"""5. klase, 112. stunda: «Kāda daļa no pilna leņķa?»

Stunda, kas savieno divus tematus: leņķus un daļas. Pilns leņķis te ir
veselais, un 90° kļūst par tā ceturtdaļu. Tas nav tikai skaists sakritums -
tieši tā vēlāk tiek zīmēta sektoru diagramma, tāpēc šī sakarība 5.7. tematā
atgriezīsies jau kā darbarīks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis, rinkis)

TEMA = "Kāda daļa no pilna leņķa?"

MERKIS = ("Mācīsimies noteikt daļu no izstiepta un pilna leņķa un formulēt "
          "sakarības.")

SATURS = [
    Sakums("Ceturtdaļa no apgrieziena",
           zimejums=rinkis(sektors=90, virsraksts="90° no 360°",
                           paraksts="ceturtdaļa no pilna leņķa"),
           paraksts="Taisns leņķis ir tieši ceturtdaļa no pilna leņķa.",
           fakti=["Pilns leņķis ir 360°.",
                  "360 : 4 = 90, tāpēc taisns leņķis ir {1|4}.",
                  "Izstiepts leņķis ir {1|2} no pilna."]),

    Doma("Leņķis ir daļa no veselā",
         "Leņķa daļu no pilna vai izstiepta leņķa atrod tāpat kā jebkuru "
         "citu daļu: leņķa lielumu raksta skaitītājā, veselo - saucējā.",
         soli=[
             "Nosaki, no kā ņem daļu: no 180° vai no 360°.",
             "Uzraksti daļu: dotais leņķis pār veselo.",
             "Saīsini daļu.",
             "Otrādi: daļas vērtību atrod, veselo dalot ar saucēju.",
             "Pārbaudi atbildi ar zīmējumu.",
         ],
         pieze="360 dalās ar ļoti daudz ko: 2, 3, 4, 5, 6, 8, 9, 10, 12... "
               "Tieši tāpēc riņķi ir ērti sadalīt vienādās daļās, un tieši "
               "tāpēc pilnam leņķim ir 360 grādu."),

    Paraugs("Kāda daļa no pilna leņķa ir 120°?",
            uzd="Izsaki 120° kā daļu no pilna leņķa.",
            soli=[
                ("Veselais ir 360°",
                 "Pilns leņķis."),
                ("{120|360}",
                 "Leņķis pār veselo."),
                ("{120 : 120|360 : 120} = {1|3}",
                 "Saīsina abus locekļus."),
                ("Pārbaude: 360 : 3 = 120",
                 "Trešdaļa tiešām ir 120°."),
            ],
            atbilde="120° ir {1|3} no pilna leņķa"),

    Ievadi("Leņķis un daļa", [
        {"jaut": "Cik grādu ir {1|4} no pilna leņķa?",
         "atb": ["90"], "padoms": "360 : 4."},
        {"jaut": "Cik grādu ir {1|3} no pilna leņķa?",
         "atb": ["120"], "padoms": "360 : 3."},
        {"jaut": "Cik grādu ir {1|6} no pilna leņķa?",
         "atb": ["60"], "padoms": "360 : 6."},
        {"jaut": "Cik grādu ir {1|2} no izstiepta leņķa?",
         "atb": ["90"], "padoms": "180 : 2."},
        {"jaut": "Cik grādu ir {1|3} no izstiepta leņķa?",
         "atb": ["60"], "padoms": "180 : 3."},
        {"jaut": "Kāda daļa no pilna leņķa ir 90°? Atbildi raksti kā a/b.",
         "atb": ["1/4", "90/360"], "padoms": "{90|360}."},
        {"jaut": "Kāda daļa no pilna leņķa ir 180°? Atbildi raksti kā a/b.",
         "atb": ["1/2", "180/360"], "padoms": "{180|360}."},
        {"jaut": "Kāda daļa no pilna leņķa ir 45°? Atbildi raksti kā a/b.",
         "atb": ["1/8", "45/360"], "padoms": "360 : 45 = 8."},
    ], pamats=4,
        ievads="Veselais ir 360° vai 180° - vispirms izlem, kurš."),

    Zimejums("Trešdaļa no pilna leņķa",
             lenkis([(0, ""), (120, "")], loki=[(0, 120, "120°")],
                    virsraksts="120° ir 1/3 no 360°"),
             paskaidro="Trīs tādi leņķi aizpilda visu apgriezienu, tāpēc "
                       "katrs no tiem ir trešdaļa.",
             ievads="Daļu var ieraudzīt, atliekot leņķi vairākas reizes."),

    Varianti("Kāda tā ir daļa?", [
        {"jaut": "Taisns leņķis ir...",
         "opcijas": ["{1|4} no pilna", "{1|2} no pilna", "{1|3} no pilna",
                     "{1|4} no izstiepta"],
         "pareizi": 0,
         "padoms": "360 : 4 = 90."},
        {"jaut": "Izstiepts leņķis ir...",
         "opcijas": ["{1|2} no pilna", "{1|4} no pilna", "{1|3} no pilna",
                     "Viss pilnais"],
         "pareizi": 0,
         "padoms": "360 : 2 = 180."},
        {"jaut": "Cik grādu ir {1|5} no pilna leņķa?",
         "opcijas": ["72°", "60°", "75°", "45°"],
         "pareizi": 0,
         "padoms": "360 : 5."},
        {"jaut": "Cik grādu ir {2|3} no pilna leņķa?",
         "opcijas": ["240°", "120°", "180°", "270°"],
         "pareizi": 0,
         "padoms": "360 : 3 · 2."},
        {"jaut": "Kāpēc pilnam leņķim ir tieši 360 grādu?",
         "opcijas": ["360 dalās ar ļoti daudziem skaitļiem",
                     "Tā ir dienu skaits gadā",
                     "Tas ir nejaušs skaitlis",
                     "Tā ir vienkāršāk rakstīt"],
         "pareizi": 0,
         "padoms": "Riņķi ērti sadalīt vienādās daļās."},
        {"jaut": "Taisns leņķis ir {1|2} no...",
         "opcijas": ["Izstiepta leņķa", "Pilna leņķa", "Šaura leņķa",
                     "Plata leņķa"],
         "pareizi": 0,
         "padoms": "180 : 2 = 90."},
    ], pamats=4),

    Pasaule("Cik pagriežas pulksteņa rādītājs?",
            Ievadi("", [
                {"jaut": "Minūšu rādītājs apiet riņķi 60 minūtēs. Cik grādu "
                         "tas pagriežas 15 minūtēs?",
                 "atb": ["90"], "padoms": "{1|4} no 360°."},
                {"jaut": "Cik grādu tas pagriežas 30 minūtēs?",
                 "atb": ["180"], "padoms": "{1|2} no 360°."},
                {"jaut": "Cik grādu tas pagriežas 20 minūtēs?",
                 "atb": ["120"], "padoms": "{1|3} no 360°."},
                {"jaut": "Cik grādu tas pagriežas 5 minūtēs?",
                 "atb": ["30"], "padoms": "360 : 12."},
            ]),
            pavediens="tehnika",
            konteksts="Pulksteņa ciparnīca ir riņķis, sadalīts 12 vienādās "
                      "daļās, tāpēc katra daļa ir 30°.",
            kapec="Leņķis un laiks te ir viena un tā pati daļa no veselā."),

    Kopsavilkums([
        "Izsaku leņķi kā daļu no pilna vai izstiepta leņķa.",
        "Aprēķinu, cik grādu ir dotā daļa no veselā leņķa.",
        "Saīsinu iegūto daļu.",
        "Skaidroju, kāpēc 360 ir ērts skaitlis riņķa dalīšanai.",
    ]),

    Majas([
        "Izsaki kā daļas no pilna leņķa: 60°, 72° un 270°.",
        "Aprēķini, cik grādu ir {3|4} no pilna leņķa.",
        "Padomā, cik grādu pagriežas stundu rādītājs vienā stundā.",
    ]),
]
