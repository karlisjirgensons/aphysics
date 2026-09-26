# -*- coding: utf-8 -*-
"""7. klase, 36. stunda: «Kas ir blakusleņķi un krustleņķi?»

Divas taisnes, kas krustojas, veido četrus leņķus. Blakus esošie ir
blakusleņķi - to summa ir 180°. Pretējie ir krustleņķi. Stunda tos definē
un iemāca atrast zīmējumā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kas ir blakusleņķi un krustleņķi?"

MERKIS = ("Definēsim blakusleņķus un krustleņķus un atradīsim tos "
          "zīmējumā.")

_KRUSTS = geometrija(
    [("A", -4, -1.5), ("B", 4, 1.5), ("C", -2, 3), ("D", 2, -3),
     ("O", 0, 0, -90)],
    nogriezni=["AB", "CD"],
    lenki=[("BOC", "1"), ("COA", "2"), ("AOD", "3"), ("DOB", "4")])

SATURS = [
    Sakums("Šķēres - divi stieņi un četri leņķi",
           zimejums=_KRUSTS,
           paraksts="Taisnes AB un CD krustojas punktā O.",
           fakti=["Atverot šķēres, viens leņķis aug, blakus esošais sarūk.",
                  "Pretējie leņķi mainās vienādi.",
                  "Četri leņķi - divi pāri."]),

    Doma("Blakusleņķi un krustleņķi",
         "Blakusleņķi ir divi leņķi, kuriem viena mala ir kopīga, bet otras "
         "malas ir papildstari. Blakusleņķu summa ir 180°. Krustleņķi ir "
         "divi leņķi, kuru malas ir viena otras papildstari.",
         soli=[
             "Blakusleņķi kopā veido izstieptu leņķi: ∠1 + ∠2 = 180°.",
             "Zīmējumā blakusleņķi ir «blakus»: 1 un 2, 2 un 3, 3 un 4, "
             "4 un 1.",
             "Krustleņķi ir «pretī»: 1 un 3, 2 un 4.",
             "Katram leņķim ir divi blakusleņķi un viens krustleņķis.",
         ],
         pieze="Blakusleņķu summa ir 180°, jo tie kopā veido izstieptu "
               "leņķi - taisni."),

    Paraugs("Aprēķini blakusleņķi",
            uzd="∠1 = 35°. Aprēķini ∠2, ja ∠1 un ∠2 ir blakusleņķi.",
            soli=[
                ("∠1 + ∠2 = 180°", "(blakusleņķu īpašība)"),
                ("∠2 = 180° − 35°", "Izsaka nezināmo."),
                ("∠2 = 145°", "Aprēķins."),
            ],
            atbilde="∠2 = 145°"),

    Varianti("Atrodi zīmējumā", [
        {"jaut": "Sākuma zīmējumā: kurš leņķis ir ∠1 krustleņķis?",
         "opcijas": ["∠3", "∠2", "∠4", "Nav tāda"],
         "pareizi": 0,
         "padoms": "Pretī."},
        {"jaut": "Kuri ir ∠2 blakusleņķi?",
         "opcijas": ["∠1 un ∠3", "∠4 un ∠1", "∠3 un ∠4", "Tikai ∠4"],
         "pareizi": 0,
         "padoms": "Ar kopīgu malu."},
        {"jaut": "Vai ∠AOC un ∠BOD ir krustleņķi?",
         "opcijas": ["Jā", "Nē, blakusleņķi", "Nē, nekādi"],
         "pareizi": 0,
         "padoms": "OA un OB, OC un OD - papildstari."},
        {"jaut": "Divi leņķi ar summu 180°. Vai tie noteikti ir "
                 "blakusleņķi?",
         "opcijas": ["Nē - tiem var nebūt kopīgas malas",
                     "Jā, vienmēr", "Jā, ja abi ir asi",
                     "Nē, tie ir krustleņķi"],
         "pareizi": 0,
         "padoms": "Definīcijā ir arī kopīgā mala."},
    ], pamats=4),

    Ievadi("Blakusleņķis", [
        {"jaut": "Leņķis ir 72°. Cik grādu ir tā blakusleņķis?",
         "atb": ["108"], "padoms": "180 − 72."},
        {"jaut": "Leņķis ir 90°. Cik grādu ir tā blakusleņķis?",
         "atb": ["90"], "padoms": "180 − 90."},
        {"jaut": "Blakusleņķi ir vienādi. Cik grādu ir katrs?",
         "atb": ["90"], "padoms": "180 : 2."},
        {"jaut": "Viens blakusleņķis ir 4 reizes lielāks par otru. Cik "
                 "grādu ir mazākais?",
         "atb": ["36"], "padoms": "5 daļas = 180°."},
        {"jaut": "Viens blakusleņķis par 40° lielāks par otru. Cik grādu "
                 "ir lielākais?",
         "atb": ["110"], "padoms": "(180 + 40) : 2."},
        {"jaut": "Leņķis ir 123,5°. Blakusleņķis?",
         "atb": ["56,5"], "padoms": "180 − 123,5."},
    ], pamats=4),

    Pasaule("Klēpjdatora ekrāns",
            Ievadi("", [
                {"jaut": "Ekrāns atvērts 110° leņķī pret tastatūru. Cik "
                         "grādu leņķis ir starp ekrānu un galda virsmu aiz "
                         "datora?",
                 "atb": ["70"], "padoms": "Blakusleņķi: 180 − 110."},
                {"jaut": "Ekrānu atver līdz galam - 180°. Cik grādu leņķis "
                         "aiz tā?",
                 "atb": ["0"], "padoms": "Ekrāns guļ uz galda."},
                {"jaut": "Ergonomiski labs leņķis aiz ekrāna ir 75°. Cik "
                         "grādos jāatver ekrāns?",
                 "atb": ["105"], "padoms": "180 − 75."},
            ]),
            pavediens="dati",
            konteksts="Datora ekrāns un galds veido blakusleņķus - tastatūra "
                      "un galds ir uz vienas taisnes.",
            kapec="Blakusleņķu summa vienmēr 180°."),

    Kopsavilkums([
        "Definēju blakusleņķus un krustleņķus.",
        "Zinu, ka blakusleņķu summa ir 180°.",
        "Atrodu blakusleņķus un krustleņķus zīmējumā.",
        "Aprēķinu blakusleņķi.",
    ]),

    Majas([
        "Atrodi mājās 3 blakusleņķu piemērus (durvis, grāmata, šķēres).",
        "Izmēri ar transportieri leņķus, ko veido divas krustojošas līnijas.",
        "Uzraksti uzdevumu par blakusleņķiem ar attiecību 1 : 2.",
    ]),
]
