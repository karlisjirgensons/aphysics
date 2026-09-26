# -*- coding: utf-8 -*-
"""7. klase, 38. stunda: «Kā aprēķināt nezināmo leņķi?»

Ar divām īpašībām - blakusleņķu summa 180° un krustleņķi vienādi - var
aprēķināt visus leņķus pie taišņu krustpunkta. Stunda trenē aprēķinus ar
pierakstu un uzdevumus, kuros vienu leņķi izsaka ar otru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā aprēķināt nezināmo leņķi?"

MERKIS = ("Aprēķināsim leņķus, lietojot blakusleņķu un krustleņķu "
          "īpašības.")

_TRIS = geometrija(
    [("A", -4, 0), ("B", 4, 0), ("C", -2.3, 3.3), ("D", 2.3, -3.3),
     ("E", 3, 3), ("O", 0, 0, -90)],
    nogriezni=["AB", "CD"], stari=["OE"],
    lenki=[("BOE", "45°"), ("EOC", "x")])

SATURS = [
    Sakums("Viens zināms leņķis - visi pārējie",
           fakti=["Divas taisnes krustojas - 4 leņķi.",
                  "Pietiek zināt vienu, lai aprēķinātu visus.",
                  "Divas īpašības: 180° un krustleņķi."]),

    Doma("Katram solim - īpašība",
         "Nezināmo leņķi aprēķina, atrodot tā saistību ar zināmu leņķi: "
         "blakusleņķi kopā ir 180°, krustleņķi ir vienādi, un leņķis, kas "
         "sadalīts daļās, ir daļu summa.",
         soli=[
             "Atzīmē zīmējumā zināmos leņķus.",
             "Meklē pāri: nezināmais un zināmais ir blakusleņķi vai "
             "krustleņķi?",
             "Uzraksti vienādību ar pamatojumu.",
             "Ja divi nezināmie saistīti ar attiecību - apzīmē vienu ar x.",
         ]),

    Paraugs("Attiecība",
            uzd="Divi blakusleņķi attiecas kā 2 : 7. Aprēķini tos.",
            soli=[
                ("Leņķi: 2x un 7x", "Apzīmē vienu daļu ar x."),
                ("2x + 7x = 180°", "(blakusleņķi)"),
                ("9x = 180°, x = 20°", "Atrisina."),
                ("2x = 40°, 7x = 140°", "Aprēķina leņķus."),
            ],
            atbilde="40° un 140°"),

    Zimejums("Trešais stars",
             _TRIS,
             ievads="Taisnes AB un CD krustojas punktā O, ∠BOC = 125°, "
                    "∠BOE = 45°.",
             paskaidro="x = ∠BOC − ∠BOE = 125° − 45° = 80°."),

    Ievadi("Aprēķini", [
        {"jaut": "Divas taisnes krustojas; viens leņķis 38°. Cik grādu ir "
                 "lielākais no četriem leņķiem?",
         "atb": ["142"], "padoms": "180 − 38."},
        {"jaut": "Blakusleņķi attiecas kā 1 : 2. Cik grādu ir mazākais?",
         "atb": ["60"], "padoms": "3 daļas = 180°."},
        {"jaut": "Starpība starp blakusleņķiem ir 50°. Cik grādu ir "
                 "mazākais?",
         "atb": ["65"], "padoms": "(180 − 50) : 2."},
        {"jaut": "Divi no četriem leņķiem pie krustpunkta kopā ir 210°. "
                 "Cik grādu ir mazākais leņķis?",
         "atb": ["75"], "padoms": "210° ir divi vienādi krustleņķi (105°)."},
        {"jaut": "Blakusleņķi attiecas kā 4 : 5. Cik grādu ir lielākais?",
         "atb": ["100"], "padoms": "9 daļas = 180°, 1 daļa = 20°."},
        {"jaut": "Viens leņķis pie krustpunkta ir 3 reizes lielāks par "
                 "savu blakusleņķi. Cik grādu tas ir?",
         "atb": ["135"], "padoms": "4 daļas = 180°."},
    ], pamats=4),

    Varianti("Pārbaudi spriedumu", [
        {"jaut": "Marta saka: «Pie krustpunkta leņķi ir 50°, 130°, 50°, "
                 "140°.» Kur kļūda?",
         "opcijas": ["140° - jābūt 130°", "Nav kļūdas",
                     "50° nevar būt", "Jābūt 4 vienādiem"],
         "pareizi": 0,
         "padoms": "Krustleņķi vienādi."},
        {"jaut": "Vai divi blakusleņķi var būt abi asi?",
         "opcijas": ["Nē - summa būtu mazāka par 180°",
                     "Jā", "Tikai, ja vienādi", "Jā, ja 89° un 89°"],
         "pareizi": 0,
         "padoms": "Divi asi leņķi kopā < 180°."},
    ]),

    Pasaule("Saules paneļa leņķis",
            Ievadi("", [
                {"jaut": "Panelis uz jumta ir 35° leņķī pret horizontāli. "
                         "Cik grādu leņķis ir starp paneli un horizontāli "
                         "otrā pusē?",
                 "atb": ["145"], "padoms": "Blakusleņķi: 180 − 35."},
                {"jaut": "Latvijā labākais slīpums ir ap 40°. Par cik "
                         "grādiem panelis jāpaceļ?",
                 "atb": ["5"], "padoms": "40 − 35."},
                {"jaut": "Paneļa atbalsta stienis ir perpendikulārs "
                         "panelim. Cik grādu leņķis starp stieni un "
                         "horizontāli, ja panelis 40°?",
                 "atb": ["50"], "padoms": "90 − 40."},
            ]),
            pavediens="planeta",
            konteksts="Saules paneļi dod visvairāk enerģijas, ja to "
                      "slīpums atbilst ģeogrāfiskajam platumam.",
            kapec="Leņķu īpašības ļauj aprēķināt, nemērot katru leņķi."),

    Kopsavilkums([
        "Aprēķinu leņķus pie taišņu krustpunkta.",
        "Lietoju attiecību: apzīmēju daļu ar x.",
        "Lietoju leņķu saskaitīšanu, ja leņķis sadalīts.",
        "Pamatoju katru soli.",
    ]),

    Majas([
        "Blakusleņķi attiecas kā 5 : 13. Aprēķini tos.",
        "Uzzīmē zīmējumu ar 3 taisnēm caur vienu punktu un aprēķini visus "
        "leņķus, ja divi ir zināmi.",
        "Izdomā savu uzdevumu ar leņķu attiecību.",
    ]),
]
