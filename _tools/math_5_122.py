# -*- coding: utf-8 -*-
"""5. klase, 122. stunda: «Kāds leņķis var būt lielāks nekā izstiepts?»

Šeit satiekas abi šī temata mikrotemati: 108. stundas atvērtais leņķis
atrod savu vietu figūrā. Ieliektā četrstūrī viens iekšējais leņķis ir
lielāks par 180°, un tieši tas padara figūru ieliektu. Skolēnam tas ir
pirmais gadījums, kad «leņķis figūrā» nozīmē vairāk par pusapgriezienu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura, lenkis)

TEMA = "Kāds leņķis var būt lielāks nekā izstiepts?"

MERKIS = ("Mācīsimies raksturot ieliekta četrstūra īpašības un tā leņķus.")

SATURS = [
    Sakums("Viens leņķis iespiests uz iekšu",
           zimejums=figura([(0, 0), (6, 0), (3, 2), (6, 5)],
                           virsraksts="Ieliekts četrstūris"),
           paraksts="Pie iespiestās virsotnes iekšējais leņķis ir lielāks "
                    "par 180°.",
           fakti=["Izliektā figūrā visi leņķi ir mazāki par 180°.",
                  "Ieliektā vismaz viens ir lielāks.",
                  "Tas ir 108. stundas atvērtais leņķis."]),

    Doma("Ieliekta figūra un atvērts leņķis",
         "Četrstūri sauc par ieliektu, ja vismaz viens tā iekšējais leņķis "
         "ir lielāks par izstieptu, tas ir, lielāks par 180°.",
         soli=[
             "Apskati katru virsotni pēc kārtas.",
             "Pārbaudi, vai leņķis ir iespiests uz iekšu.",
             "Ja ir, tas ir atvērts leņķis - vairāk par 180°.",
             "Viens tāds leņķis padara visu figūru ieliektu.",
             "Pārējie leņķi paliek mazāki par 180°.",
         ],
         pieze="Četrstūrī ieliekts var būt tikai viens leņķis. Ja divi būtu "
               "lielāki par 180°, to summa jau pārsniegtu 360°, bet visu "
               "četru leņķu summa četrstūrī ir tieši 360°."),

    Paraugs("Trīs leņķi zināmi",
            uzd="Ieliektā četrstūrī trīs leņķi ir 40°, 50° un 60°. Cik liels "
                "ir ceturtais?",
            soli=[
                ("Četrstūra leņķu summa ir 360°",
                 "Zināma sakarība."),
                ("40 + 50 + 60 = 150",
                 "Zināmo summa."),
                ("360 - 150 = 210",
                 "Ceturtais leņķis."),
                ("210° > 180°",
                 "Tas ir atvērts leņķis - figūra ir ieliekta."),
            ],
            atbilde="Ceturtais leņķis ir 210°, un tas ir atvērts"),

    Ievadi("Aprēķini ceturto leņķi", [
        {"jaut": "Četrstūra leņķu summa. Cik grādu tā ir?",
         "atb": ["360"], "padoms": "Divi trijstūri pa 180°."},
        {"jaut": "Trīs leņķi ir 40°, 50° un 60°. Cik grādu ir ceturtais?",
         "atb": ["210"], "padoms": "360 - 150."},
        {"jaut": "Trīs leņķi ir 90°, 90° un 90°. Cik grādu ir ceturtais?",
         "atb": ["90"], "padoms": "360 - 270."},
        {"jaut": "Trīs leņķi ir 30°, 40° un 80°. Cik grādu ir ceturtais?",
         "atb": ["210"], "padoms": "360 - 150."},
        {"jaut": "Trīs leņķi ir 100°, 80° un 60°. Cik grādu ir ceturtais?",
         "atb": ["120"], "padoms": "360 - 240."},
        {"jaut": "Ceturtais leņķis ir 210°. Vai figūra ir ieliekta? Raksti "
                 "«jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "210 > 180."},
        {"jaut": "Ceturtais leņķis ir 120°. Vai figūra ir ieliekta?",
         "atb": ["nē", "ne"], "padoms": "Visi leņķi zem 180°."},
        {"jaut": "Cik ieliektu leņķu var būt vienam četrstūrim?",
         "atb": ["1"], "padoms": "Divi pārsniegtu 360°."},
    ], pamats=4,
        ievads="Četru leņķu summa vienmēr ir 360° - no tās arī rēķina."),

    Zimejums("Atvērts leņķis figūrā",
             lenkis([(0, ""), (210, "")], loki=[(0, 210, "210°")],
                    virsraksts="Tāds izskatās 210° leņķis"),
             paskaidro="Tieši tāds leņķis ir pie ieliektā četrstūra "
                       "iespiestās virsotnes - vairāk par izstieptu.",
             ievads="Atvērtu leņķi var uzzīmēt arī atsevišķi."),

    Varianti("Kad figūra ir ieliekta?", [
        {"jaut": "Kad četrstūri sauc par ieliektu?",
         "opcijas": ["Kad viens leņķis ir lielāks par 180°",
                     "Kad visas malas ir dažādas",
                     "Kad tam nav taisnu leņķu",
                     "Kad tas ir mazs"],
         "pareizi": 0,
         "padoms": "Atvērts iekšējais leņķis."},
        {"jaut": "Cik grādu ir četrstūra leņķu summa?",
         "opcijas": ["360°", "180°", "270°", "540°"],
         "pareizi": 0,
         "padoms": "Divi trijstūri."},
        {"jaut": "Cik ieliektu leņķu var būt četrstūrim?",
         "opcijas": ["Viens", "Divi", "Trīs", "Neviens"],
         "pareizi": 0,
         "padoms": "Divi pārsniegtu summu."},
        {"jaut": "Trīs leņķi ir 20°, 30° un 40°. Kāds ir ceturtais?",
         "opcijas": ["270°", "90°", "180°", "210°"],
         "pareizi": 0,
         "padoms": "360 - 90."},
        {"jaut": "Vai taisnstūris var būt ieliekts?",
         "opcijas": ["Nevar, visi leņķi ir 90°", "Var",
                     "Var, ja tas ir garens", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "90° nav lielāks par 180°."},
        {"jaut": "Kas notiek ar diagonāli ieliektā četrstūrī?",
         "opcijas": ["Viena iziet ārpus figūras", "Abas paliek iekšā",
                     "Diagonāļu nav", "Tās ir vienādas"],
         "pareizi": 0,
         "padoms": "121. stundas atklājums."},
    ], pamats=4),

    Pasaule("Kāda forma ir skolas pagalmam?",
            Ievadi("", [
                {"jaut": "Pagalma četri leņķi ir 90°, 90°, 90° un x. Cik "
                         "grādu ir x?",
                 "atb": ["90"], "padoms": "360 - 270."},
                {"jaut": "Cita pagalma leņķi ir 60°, 70°, 80° un x. Cik "
                         "grādu ir x?",
                 "atb": ["150"], "padoms": "360 - 210."},
                {"jaut": "Vai šis pagalms ir ieliekts? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "150 < 180."},
                {"jaut": "Trešā pagalma leņķi ir 30°, 40°, 50° un x. Cik "
                         "grādu ir x?",
                 "atb": ["240"], "padoms": "360 - 120."},
            ]),
            pavediens="skola",
            konteksts="Skolas pagalms reti ir taisnstūris; bieži tam ir "
                      "viens stūris iespiests uz iekšu.",
            kapec="Leņķu summa ļauj pārbaudīt plānu, neejot uz vietas."),

    Kopsavilkums([
        "Raksturoju ieliektu četrstūri un tā leņķus.",
        "Zinu, ka četrstūra leņķu summa ir 360°.",
        "Aprēķinu nezināmo leņķi un nosaku, vai tas ir atvērts.",
        "Zinu, ka ieliekts var būt tikai viens četrstūra leņķis.",
    ]),

    Majas([
        "Uzzīmē ieliektu četrstūri un atzīmē tā atvērto leņķi.",
        "Aprēķini ceturto leņķi, ja trīs ir 55°, 65° un 75°.",
        "Padomā, vai ieliekts var būt arī trijstūris.",
    ]),
]
