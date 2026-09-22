# -*- coding: utf-8 -*-
"""5. klase, 113. stunda: «Vai apgalvojums par leņķiem ir patiess?»

Mikrotemata noslēgums, un tas ir 25. stundas turpinājums: tur pārbaudīja
vienādības, te - apgalvojumus. Atbilde «jā» vai «nē» pati par sevi neko
nedod; vērtība ir pamatojumā. Tāpēc katram nepatiesam apgalvojumam te prasa
pretpiemēru - vienu leņķi, ar kuru pietiek, lai to apgāztu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis)

TEMA = "Vai apgalvojums par leņķiem ir patiess?"

MERKIS = ("Mācīsimies noteikt apgalvojuma par leņķu lielumiem patiesumu un "
          "to pamatot.")

SATURS = [
    Sakums("Divi apgalvojumi, viens nepatiess",
           zimejums=lenkis([(0, "A"), (95, "C"), (180, "B")],
                           loki=[(0, 95, "95°"), (95, 180, "85°")],
                           virsraksts="Viens plats, otrs šaurs"),
           paraksts="Ja viens blakusleņķis ir plats, otrs noteikti ir šaurs.",
           fakti=["«Abi blakusleņķi var būt plati» - vai tā ir taisnība?",
                  "«Divi šauri leņķi kopā vienmēr ir šauri» - arī nē.",
                  "Lai apgāztu apgalvojumu, pietiek ar vienu piemēru."]),

    Doma("Pamato vai apgāz ar piemēru",
         "Apgalvojums ir patiess tad, ja tas izpildās vienmēr; lai to "
         "apgāztu, pietiek atrast vienu piemēru, kurā tas neizpildās.",
         soli=[
             "Izlasi apgalvojumu un saproti, par ko tas ir.",
             "Pamēģini to ar dažiem leņķiem.",
             "Ja atrodi vienu neatbilstošu - apgalvojums ir nepatiess.",
             "Ja neatrodi, pamato ar sakarību, nevis ar piemēriem.",
             "Pieraksti pamatojumu vienā teikumā.",
         ],
         pieze="Viens piemērs apgalvojumu nepierāda, bet viens pretpiemērs "
               "to apgāž. Tā ir nesimetrija, ko der atcerēties: pierādīt ir "
               "grūtāk nekā apgāzt."),

    Paraugs("«Abi blakusleņķi var būt plati»",
            uzd="Nosaki, vai apgalvojums ir patiess, un pamato.",
            soli=[
                ("Plats leņķis ir lielāks par 90°",
                 "Ko nozīmē «plats»."),
                ("Ja abi būtu plati, summa būtu lielāka par 180°",
                 "90 + 90 = 180, bet abi ir vēl lielāki."),
                ("Blakusleņķu summa ir tieši 180°",
                 "Zināmā sakarība."),
                ("Tātad abi plati būt nevar",
                 "Apgalvojums ir nepatiess."),
            ],
            atbilde="Apgalvojums ir nepatiess"),

    Ievadi("Patiess vai nepatiess?", [
        {"jaut": "«Izstiepts leņķis ir 180°.» Raksti «patiess» vai "
                 "«nepatiess».",
         "atb": ["patiess"], "padoms": "Tā ir definīcija."},
        {"jaut": "«Taisns leņķis ir lielāks par platu.»",
         "atb": ["nepatiess"], "padoms": "Plats ir lielāks par 90°."},
        {"jaut": "«Abi blakusleņķi var būt plati.»",
         "atb": ["nepatiess"], "padoms": "Summa būtu lielāka par 180°."},
        {"jaut": "«Abi blakusleņķi var būt taisni.»",
         "atb": ["patiess"], "padoms": "90° + 90° = 180°."},
        {"jaut": "«Pilns leņķis ir divi izstiepti leņķi.»",
         "atb": ["patiess"], "padoms": "180 · 2 = 360."},
        {"jaut": "«Atvērts leņķis ir mazāks par izstieptu.»",
         "atb": ["nepatiess"], "padoms": "Atvērts ir lielāks par 180°."},
        {"jaut": "«Divi šauri leņķi kopā vienmēr ir šauri.»",
         "atb": ["nepatiess"], "padoms": "80° + 80° = 160°."},
        {"jaut": "«Ja viens blakusleņķis ir šaurs, otrs ir plats.»",
         "atb": ["patiess"], "padoms": "180 mīnus mazāk par 90."},
    ], pamats=4,
        ievads="Pirms atbildi, pamēģini apgalvojumu ar diviem trim "
               "skaitļiem."),

    Zimejums("Pretpiemērs vienā zīmējumā",
             lenkis([(0, ""), (80, ""), (160, "")],
                    loki=[(0, 80, "80°"), (80, 160, "80°")],
                    virsraksts="Divi šauri leņķi, kopā plats"),
             paskaidro="80° un 80° abi ir šauri, bet to summa ir 160° - "
                       "plats leņķis. Ar šo vienu zīmējumu pietiek, lai "
                       "apgalvojumu apgāztu.",
             ievads="Pretpiemērs ir īsākais pamatojums."),

    Varianti("Kā pamato atbildi?", [
        {"jaut": "Ar ko var apgāzt apgalvojumu?",
         "opcijas": ["Ar vienu pretpiemēru", "Ar vienu piemēru",
                     "Ar desmit piemēriem", "Apgāzt nevar"],
         "pareizi": 0,
         "padoms": "Pietiek ar vienu neatbilstošu gadījumu."},
        {"jaut": "Vai viens piemērs pierāda apgalvojumu?",
         "opcijas": ["Nē, jāpamato ar sakarību", "Jā",
                     "Jā, ja piemērs ir liels", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Vienmēr - tas nozīmē visos gadījumos."},
        {"jaut": "«Abi blakusleņķi var būt šauri.» Vai tas ir patiess?",
         "opcijas": ["Nē, summa būtu mazāka par 180°", "Jā",
                     "Jā, ja tie ir vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Divi leņķi zem 90° kopā ir zem 180°."},
        {"jaut": "«Pilns leņķis ir četri taisni leņķi.»",
         "opcijas": ["Patiess", "Nepatiess", "Tikai reizēm",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "90 · 4 = 360."},
        {"jaut": "Kurš pretpiemērs apgāž apgalvojumu «divi šauri leņķi kopā "
                 "vienmēr ir šauri»?",
         "opcijas": ["80° un 80°", "10° un 20°", "30° un 40°", "5° un 5°"],
         "pareizi": 0,
         "padoms": "Summai jāsanāk vairāk par 90°."},
        {"jaut": "Kas jāpieraksta pie atbildes?",
         "opcijas": ["Pamatojums", "Tikai «jā» vai «nē»", "Zīmējums",
                     "Nekas"],
         "pareizi": 0,
         "padoms": "Atbilde bez pamatojuma neko nepierāda."},
    ], pamats=4),

    Pasaule("Vai rasējums ir iespējams?",
            Ievadi("", [
                {"jaut": "Rasējumā abi blakusleņķi atzīmēti kā 100°. Vai tas "
                         "ir iespējams? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "100 + 100 = 200."},
                {"jaut": "Rasējumā blakusleņķi ir 120° un 60°. Vai tas ir "
                         "iespējams?",
                 "atb": ["jā", "ja"], "padoms": "120 + 60 = 180."},
                {"jaut": "Ap punktu atzīmēti leņķi 90°, 90°, 90° un 100°. Vai "
                         "tas ir iespējams?",
                 "atb": ["nē", "ne"], "padoms": "Summa ir 370."},
                {"jaut": "Ap punktu atzīmēti 120°, 120° un 120°. Vai tas ir "
                         "iespējams?",
                 "atb": ["jā", "ja"], "padoms": "Summa ir 360."},
            ]),
            pavediens="tehnika",
            konteksts="Rasējumā kļūdainus leņķus pamana tieši tā - saskaitot "
                      "un salīdzinot ar 180° vai 360°.",
            kapec="Pirms detaļu izgatavo, pārbauda, vai tā vispār ir "
                  "iespējama."),

    Kopsavilkums([
        "Nosaku, vai apgalvojums par leņķiem ir patiess.",
        "Apgāžu nepatiesu apgalvojumu ar pretpiemēru.",
        "Pamatoju patiesu apgalvojumu ar zināmu sakarību.",
        "Zinu, ka viens piemērs apgalvojumu nepierāda.",
    ]),

    Majas([
        "Nosaki, vai patiess ir apgalvojums «divi plati leņķi kopā ir "
        "vairāk par izstieptu».",
        "Uzraksti vienu patiesu un vienu nepatiesu apgalvojumu par leņķiem.",
        "Atrodi pretpiemēru apgalvojumam «leņķis, lielāks par taisnu, "
        "vienmēr ir plats».",
    ]),
]
