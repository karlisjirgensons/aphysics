# -*- coding: utf-8 -*-
"""7. klase, 31. stunda: «Kas ir viduspunkts?»

Nogriežņa viduspunkts sadala to divos vienādos nogriežņos. Stunda to
definē, pieraksta ar vienādībām un lieto aprēķinos - arī uz skaitļu
taisnes, kur viduspunkts ir abu galu vidējais aritmētiskais.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija,
                         taisne)

TEMA = "Kas ir viduspunkts?"

MERKIS = ("Definēsim nogriežņa viduspunktu un lietosim tā īpašību "
          "aprēķinos.")

SATURS = [
    Sakums("Kur satikties pa vidu?",
           zimejums=geometrija([("A", 0, 0), ("M", 5, 0), ("B", 10, 0)],
                               nogriezni=["AB"],
                               svitras=[("AM", 1), ("MB", 1)]),
           paraksts="AM = MB - vienādas svītriņas nozīmē vienādus "
                    "nogriežņus.",
           fakti=["Divi draugi dzīvo 10 km attālumā.",
                  "Ja katrs iet vienādu ceļu, viņi satiekas viduspunktā.",
                  "Katrs noiet 5 km."]),

    Doma("Viduspunkts dala nogriezni uz pusēm",
         "Nogriežņa AB viduspunkts ir tāds nogriežņa punkts M, ka AM = MB. "
         "Tad AM = MB = {1|2}AB un AB = 2AM.",
         soli=[
             "Pārbaudi, vai punkts pieder nogrieznim.",
             "Pārbaudi, vai abas daļas ir vienādas.",
             "Zīmējumā vienādas daļas atzīmē ar vienādām svītriņām.",
             "Uz skaitļu taisnes: viduspunkts ir (a + b) : 2.",
         ],
         pieze="Abi nosacījumi ir svarīgi: punkts, kas ir vienādā attālumā "
               "no A un B, bet nav uz AB, nav viduspunkts."),

    Paraugs("Viduspunkti uz taisnes",
            uzd="C ir AB viduspunkts, D - CB viduspunkts. AB = 12 cm. Cik "
                "garš ir AD?",
            soli=[
                ("AC = CB = 12 : 2 = 6 (cm)", "C - AB viduspunkts."),
                ("CD = DB = 6 : 2 = 3 (cm)", "D - CB viduspunkts."),
                ("AD = AC + CD = 6 + 3 = 9 (cm)", "Daļas saskaita."),
            ],
            atbilde="AD = 9 cm"),

    Zimejums("Viduspunkts uz skaitļu taisnes",
             taisne(0, 10, 1, [(2, "2"), (5, "5"), (8, "8")]),
             paskaidro="Nogriežņa no 2 līdz 8 viduspunkts: (2 + 8) : 2 = 5."),

    Ievadi("Aprēķini", [
        {"jaut": "M - AB viduspunkts, AM = 3,5 cm. Cik cm ir AB?",
         "atb": ["7"], "padoms": "AB = 2AM."},
        {"jaut": "M - AB viduspunkts, AB = 9 cm. Cik cm ir MB?",
         "atb": ["4,5"], "padoms": "9 : 2."},
        {"jaut": "Uz skaitļu taisnes: kāds ir nogriežņa no −4 līdz 10 "
                 "viduspunkts?",
         "atb": ["3"], "padoms": "(−4 + 10) : 2."},
        {"jaut": "Viduspunkts ir 6, viens gals 2. Kur ir otrs gals?",
         "atb": ["10"], "padoms": "No 2 līdz 6 ir 4; vēl 4 tālāk."},
        {"jaut": "C - AB viduspunkts, D - AC viduspunkts, AB = 20 cm. "
                 "Cik cm ir DB?",
         "atb": ["15"], "padoms": "DC = 5, CB = 10."},
        {"jaut": "Uz skaitļu taisnes: viduspunkts starp −7 un −1?",
         "atb": ["−4", "-4"], "padoms": "(−7 + (−1)) : 2."},
    ], pamats=4),

    Varianti("Vai tas ir viduspunkts?", [
        {"jaut": "Punkts K: AK = 4 cm, KB = 4 cm, bet K nav uz AB.",
         "opcijas": ["Nav viduspunkts", "Ir viduspunkts", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Viduspunktam jāpieder nogrieznim."},
        {"jaut": "Punkts K ∈ AB, AK = 3 cm, AB = 6 cm.",
         "opcijas": ["Ir viduspunkts", "Nav viduspunkts", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "KB = 3 cm."},
        {"jaut": "Cik viduspunktu ir nogrieznim?",
         "opcijas": ["Tieši viens", "Divi", "Bezgalīgi daudz", "Neviens"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Pusi var atlikt tikai vienā vietā."},
    ]),

    Pasaule("Uzlādes stacija pa vidu",
            Ievadi("", [
                {"jaut": "Elektroauto brauc no Rīgas (0 km) uz Liepāju "
                         "(220 km). Uzlādes stacija ir tieši pusceļā. Pie "
                         "kura km?",
                 "atb": ["110"], "padoms": "220 : 2."},
                {"jaut": "Auto nobrauc 250 km ar vienu uzlādi. Vai var "
                         "aizbraukt līdz Liepājai un atpakaļ līdz stacijai "
                         "bez uzlādes? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "220 + 110 = 330 > 250."},
                {"jaut": "Starp stāciju pusceļā un Liepāju vēl viena stacija "
                         "pašā vidū. Pie kura km?",
                 "atb": ["165"], "padoms": "(110 + 220) : 2."},
            ]),
            pavediens="celojums",
            konteksts="Uzlādes stacijas liek tā, lai starp tām nebūtu "
                      "pārāk tālu - bieži tieši posma vidū.",
            kapec="Viduspunkts ir vidējais aritmētiskais."),

    Kopsavilkums([
        "Definēju viduspunktu: M ∈ AB un AM = MB.",
        "Lietoju AM = {1|2}AB un AB = 2AM.",
        "Uz skaitļu taisnes atrodu viduspunktu: (a + b) : 2.",
        "Zīmējumā atzīmēju vienādus nogriežņus ar svītriņām.",
    ]),

    Majas([
        "Atrodi kartē pusceļu starp savu māju un kādu pilsētu.",
        "Uzraksti uzdevumu ar diviem viduspunktiem un atrisini.",
        "Paskaidro, kāpēc punkts 5 cm no A un 5 cm no B var nebūt "
        "viduspunkts.",
    ]),
]
