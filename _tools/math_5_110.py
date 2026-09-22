# -*- coding: utf-8 -*-
"""5. klase, 110. stunda: «Kādas sakarības veido vairāki stari?»

Ja staru ir trīs vai četri, leņķu kļūst daudz, un skolēns sāk mēģināt izmērīt
katru atsevišķi. Šī stunda māca otru ceļu: pierakstīt sakarības. Trīs stari
dod divas summas, četri - vēl vairāk, un no zināmajiem leņķiem pārējos var
izrēķināt, nepieliekot transportieri ne reizi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis)

TEMA = "Kādas sakarības veido vairāki stari?"

MERKIS = ("Mācīsimies formulēt sakarības starp leņķiem, ko veido trīs vai "
          "četri stari ar kopīgu sākumpunktu.")

SATURS = [
    Sakums("Trīs stari, trīs leņķi",
           zimejums=lenkis([(0, "A"), (50, "C"), (110, "D"), (180, "B")],
                           loki=[(0, 50, "50°"), (50, 110, "60°"),
                                 (110, 180, "70°")],
                           virsraksts="Izstiepts leņķis trijās daļās"),
           paraksts="50° + 60° + 70° = 180° - visas daļas kopā dod veselo.",
           fakti=["Katrs jauns stars pievieno vēl vienu leņķi.",
                  "Visu blakus esošo leņķu summa paliek nemainīga.",
                  "Tāpēc vienu nezināmo vienmēr var izrēķināt."]),

    Doma("Daļu summa ir viss leņķis",
         "Stari ar kopīgu sākumpunktu sadala leņķi daļās; visu daļu summa ir "
         "vienāda ar sadalāmo leņķi - 180° vai 360°.",
         soli=[
             "Nosaki, kāds leņķis tiek sadalīts: izstiepts vai pilns.",
             "Pieraksti visus zināmos leņķus.",
             "Saskaiti tos.",
             "Atņem summu no 180° vai 360°.",
             "Pieraksti sakarību vienā rindā.",
         ],
         pieze="Sakarību pieraksta ar leņķu apzīmējumiem: ∠AOC + ∠COD + "
               "∠DOB = 180°. Vidējais burts vienmēr ir virsotne, tāpēc no "
               "pieraksta redz, kurš leņķis ir domāts."),

    Paraugs("Trīs leņķi, viens nezināms",
            uzd="Izstieptu leņķi sadala divi stari. Divi leņķi ir 50° un "
                "60°. Cik liels ir trešais?",
            soli=[
                ("Visi trīs kopā ir 180°",
                 "Sadalāmais leņķis."),
                ("50° + 60° = 110°",
                 "Zināmo summa."),
                ("180° - 110° = 70°",
                 "Trešais leņķis."),
                ("Pārbaude: 50° + 60° + 70° = 180°",
                 "Summa sakrīt."),
            ],
            atbilde="Trešais leņķis ir 70°"),

    Ievadi("Atrodi nezināmo leņķi", [
        {"jaut": "Izstieptu leņķi sadala trīs daļās: 50°, 60° un x. Cik "
                 "grādu ir x?",
         "atb": ["70"], "padoms": "180 - 110."},
        {"jaut": "Daļas ir 40°, 70° un x. Cik grādu ir x?",
         "atb": ["70"], "padoms": "180 - 110."},
        {"jaut": "Daļas ir 30°, 30° un x. Cik grādu ir x?",
         "atb": ["120"], "padoms": "180 - 60."},
        {"jaut": "Pilnu leņķi sadala trīs daļās: 120°, 100° un x. Cik grādu "
                 "ir x?",
         "atb": ["140"], "padoms": "360 - 220."},
        {"jaut": "Pilnu leņķi sadala četrās vienādās daļās. Cik grādu ir "
                 "katra?",
         "atb": ["90"], "padoms": "360 : 4."},
        {"jaut": "Izstieptu leņķi sadala trīs vienādās daļās. Cik grādu ir "
                 "katra?",
         "atb": ["60"], "padoms": "180 : 3."},
        {"jaut": "Pilnu leņķi sadala daļās 90°, 90°, 90° un x. Cik grādu ir "
                 "x?",
         "atb": ["90"], "padoms": "360 - 270."},
        {"jaut": "Daļas ir 25°, 35°, 45° un x, un kopā tie ir izstiepts "
                 "leņķis. Cik grādu ir x?",
         "atb": ["75"], "padoms": "180 - 105."},
    ], pamats=4,
        ievads="Saskaiti zināmos un atņem no veselā leņķa."),

    Zimejums("Pilns leņķis četrās daļās",
             lenkis([(0, ""), (90, ""), (180, ""), (270, "")],
                    loki=[(0, 90, "90°"), (90, 180, "90°"),
                          (180, 270, "90°")],
                    virsraksts="Četri stari, četri taisni leņķi"),
             paskaidro="Četri taisni leņķi kopā dod 360°, tas ir, pilnu "
                       "leņķi. Ceturtā daļa zīmējumā ir starp pēdējo un "
                       "pirmo staru.",
             ievads="Ar četriem stariem sanāk četras daļas."),

    Varianti("Kāda sakarība te ir?", [
        {"jaut": "Ko dod visu blakus esošo leņķu summa izstieptā leņķī?",
         "opcijas": ["180°", "90°", "360°", "Tas atkarīgs no staru skaita"],
         "pareizi": 0,
         "padoms": "Sadalāmais leņķis nemainās."},
        {"jaut": "Ko dod visu leņķu summa ap vienu punktu?",
         "opcijas": ["360°", "180°", "90°", "Tas atkarīgs"],
         "pareizi": 0,
         "padoms": "Pilns leņķis."},
        {"jaut": "Izstieptu leņķi sadala divi stari. Cik leņķu izveidojas?",
         "opcijas": ["Trīs", "Divi", "Četri", "Viens"],
         "pareizi": 0,
         "padoms": "Divi stari starp diviem malējiem."},
        {"jaut": "Ko nozīmē pieraksts ∠AOB?",
         "opcijas": ["Leņķi ar virsotni O", "Leņķi ar virsotni A",
                     "Nogriezni AB", "Trijstūri"],
         "pareizi": 0,
         "padoms": "Vidējais burts ir virsotne."},
        {"jaut": "Pilnu leņķi sadala trīs vienādās daļās. Cik grādu katrā?",
         "opcijas": ["120°", "90°", "60°", "180°"],
         "pareizi": 0,
         "padoms": "360 : 3."},
        {"jaut": "Kā atrod nezināmo leņķi?",
         "opcijas": ["No veselā atņem zināmo summu",
                     "Saskaita visus zināmos",
                     "Dala veselo ar staru skaitu",
                     "Izmēra ar transportieri"],
         "pareizi": 0,
         "padoms": "Veselais mīnus daļas."},
    ], pamats=4),

    Pasaule("Cik leņķu ir zobratā?",
            Ievadi("", [
                {"jaut": "Zobrata spieķi sadala pilnu leņķi 6 vienādās "
                         "daļās. Cik grādu ir katra?",
                 "atb": ["60"], "padoms": "360 : 6."},
                {"jaut": "Citam zobratam ir 8 spieķi. Cik grādu ir katra "
                         "daļa?",
                 "atb": ["45"], "padoms": "360 : 8."},
                {"jaut": "Zobratam ir 5 spieķi. Cik grādu ir katra daļa?",
                 "atb": ["72"], "padoms": "360 : 5."},
                {"jaut": "Divi spieķi veido 120° leņķi. Cik grādu paliek "
                         "pārējiem?",
                 "atb": ["240"], "padoms": "360 - 120."},
            ]),
            pavediens="tehnika",
            konteksts="Zobrata spieķi iziet no viena centra, tāpēc tie ir "
                      "tie paši stari ar kopīgu sākumpunktu.",
            kapec="Vienādas daļas rēķina ar dalīšanu, nevis ar mērīšanu."),

    Kopsavilkums([
        "Formulēju sakarību starp leņķiem, ko veido vairāki stari.",
        "Zinu, ka leņķu summa ap punktu ir 360°.",
        "Aprēķinu nezināmo leņķi, no veselā atņemot zināmo summu.",
        "Lietoju leņķa apzīmējumu ∠AOB.",
    ]),

    Majas([
        "Uzzīmē četrus starus no viena punkta un pieraksti visas sakarības.",
        "Aprēķini leņķus, ja pilnu leņķi sadala 9 vienādās daļās.",
        "Atrodi mājās priekšmetu, kurā stari iziet no viena punkta.",
    ]),
]
