# -*- coding: utf-8 -*-
"""5. klase, 117. stunda: «Cik garš loks vajadzīgs grozam?»

Sakarība jau ir atklāta; te tā tiek lietota uzdevumā, kurā nav pateikts,
kurus skaitļus ņemt. Grūtākais te nav rēķins, bet pirmais solis: saprast,
ka no visa apraksta vajadzīgs tikai diametrs. Tāpēc stunda māca arī izsvītrot
lieko.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, rinkis)

TEMA = "Cik garš loks vajadzīgs grozam?"

MERKIS = ("Mācīsimies lietot sakarību praktiskā uzdevumā, atrodot no apraksta "
          "vajadzīgos datus.")

SATURS = [
    Sakums("Grozam vajag stiepli apkārt",
           zimejums=rinkis(diametrs="d = 40 cm", virsraksts="Groza mala"),
           paraksts="Stieples garums ir riņķa līnijas garums: apmēram "
                    "120 cm.",
           fakti=["Groza augstums un krāsa te nav svarīgi.",
                  "Svarīgs ir tikai diametrs vai rādiuss.",
                  "Stieples garums ir apmēram trīs diametri."]),

    Doma("Vispirms izraksti vajadzīgo",
         "Praktiskā uzdevumā vispirms atrod, kurš skaitlis ir diametrs vai "
         "rādiuss, un tikai tad lieto sakarību C apmēram 3 · d.",
         soli=[
             "Izlasi uzdevumu un pasvītro skaitļus.",
             "Nosaki, kurš no tiem ir diametrs vai rādiuss.",
             "Ja dots rādiuss, pārrēķini to diametrā.",
             "Reizini diametru ar 3.",
             "Pieraksti atbildi ar mērvienību un vārdu «apmēram».",
         ],
         pieze="Praktiskā uzdevumā bieži der pielikt nedaudz vairāk: "
               "stieplei vajag arī savienojuma vietu. Matemātikas atbilde ir "
               "aptuvenais garums, bet meistars pieliek vēl dažus "
               "centimetrus."),

    Paraugs("Groza diametrs ir 40 cm",
            uzd="Cik gara stieple vajadzīga, lai apliktu grozam malu?",
            soli=[
                ("Vajadzīgais skaitlis ir diametrs, 40 cm",
                 "Pārējais aprakstā nav svarīgs."),
                ("C apmēram 3 · d",
                 "Sakarība."),
                ("3 · 40 = 120 (cm)",
                 "Aptuvenais garums."),
                ("Atbilde: apmēram 120 cm",
                 "Ar mērvienību."),
            ],
            atbilde="Vajag apmēram 120 cm stieples"),

    Ievadi("Cik garš loks vajadzīgs?", [
        {"jaut": "Groza diametrs 40 cm. Cik apmēram centimetru stieples "
                 "vajag?",
         "atb": ["120"], "padoms": "3 · 40."},
        {"jaut": "Groza rādiuss 25 cm. Cik apmēram centimetru stieples "
                 "vajag?",
         "atb": ["150"], "padoms": "6 · 25."},
        {"jaut": "Puķupoda diametrs 30 cm. Cik apmēram centimetru lentes "
                 "vajag?",
         "atb": ["90"], "padoms": "3 · 30."},
        {"jaut": "Apaļa galda rādiuss 50 cm. Cik apmēram centimetru maliņas "
                 "vajag?",
         "atb": ["300"], "padoms": "6 · 50."},
        {"jaut": "Ir 90 cm stieples. Ap kādu apmēram diametru tā aplieksies?",
         "atb": ["30"], "padoms": "90 : 3."},
        {"jaut": "Ir 60 cm lentes. Ap kādu apmēram rādiusu tā aplieksies?",
         "atb": ["10"], "padoms": "60 : 6."},
        {"jaut": "Grozam ar diametru 40 cm vajag divas kārtas stieples. Cik "
                 "apmēram centimetru?",
         "atb": ["240"], "padoms": "120 · 2."},
        {"jaut": "Apaļas segas diametrs ir 2 m. Cik apmēram metru apmales "
                 "vajag?",
         "atb": ["6"], "padoms": "3 · 2."},
    ], pamats=4,
        ievads="Vispirms atrodi diametru, tikai tad reizini."),

    Zimejums("Tikai viens skaitlis ir vajadzīgs",
             rinkis(radiuss="r = 25 cm", virsraksts="No rādiusa uz garumu"),
             paskaidro="Ja dots rādiuss, garumu iegūst, reizinot to ar 6; ja "
                       "diametrs - reizinot ar 3.",
             ievads="Abi ceļi ved uz vienu atbildi."),

    Varianti("Kurš skaitlis te vajadzīgs?", [
        {"jaut": "Grozam ir 30 cm augstums un 40 cm diametrs. Kurš skaitlis "
                 "vajadzīgs stieples garumam?",
         "opcijas": ["40 cm", "30 cm", "Abi", "Neviens"],
         "pareizi": 0,
         "padoms": "Loks iet ap malu."},
        {"jaut": "Dots rādiuss. Ar ko to reizina?",
         "opcijas": ["Ar 6", "Ar 3", "Ar 2", "Ar 12"],
         "pareizi": 0,
         "padoms": "Divi rādiusi ir diametrs."},
        {"jaut": "Dots diametrs. Ar ko to reizina?",
         "opcijas": ["Ar 3", "Ar 6", "Ar 2", "Ar 9"],
         "pareizi": 0,
         "padoms": "Apmēram trīs diametri."},
        {"jaut": "Groza diametrs ir 50 cm. Cik apmēram stieples vajag?",
         "opcijas": ["150 cm", "100 cm", "300 cm", "50 cm"],
         "pareizi": 0,
         "padoms": "3 · 50."},
        {"jaut": "Kāpēc atbildē raksta «apmēram»?",
         "opcijas": ["Attiecība ir tuvināta", "Mērvienība ir neprecīza",
                     "Grozs nav apaļš", "Tā nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "3 nav precīzs skaitlis."},
        {"jaut": "Kas jāpieliek praktiskā uzdevumā papildus?",
         "opcijas": ["Nedaudz uz savienojumu", "Divas reizes vairāk",
                     "Nekas", "Puse"],
         "pareizi": 0,
         "padoms": "Stiepli vajag arī sasiet."},
    ], pamats=4),

    Pasaule("Cik materiāla pirkt?",
            Ievadi("", [
                {"jaut": "Apaļas segas rādiuss ir 1 m. Cik apmēram metru "
                         "apmales vajag?",
                 "atb": ["6"], "padoms": "6 · 1."},
                {"jaut": "Apaļa paklāja diametrs ir 3 m. Cik apmēram metru "
                         "maliņas vajag?",
                 "atb": ["9"], "padoms": "3 · 3."},
                {"jaut": "Caurules diametrs ir 20 cm. Cik apmēram centimetru "
                         "lentes vajag apkārt?",
                 "atb": ["60"], "padoms": "3 · 20."},
                {"jaut": "Ir 12 m apmales. Ap kādu apmēram diametru tā "
                         "aplieksies?",
                 "atb": ["4"], "padoms": "12 : 3."},
            ]),
            pavediens="maja",
            konteksts="Veikalā materiālu pērk metros, bet lieta ir apaļa un "
                      "mērīta pa diametru.",
            kapec="Viens reizinājums pasaka, cik metru likt grozā."),

    Kopsavilkums([
        "Atrodu aprakstā vajadzīgo skaitli - diametru vai rādiusu.",
        "Lietoju sakarību, lai aprēķinātu aptuveno loka garumu.",
        "Pārrēķinu rādiusu diametrā, ja vajag.",
        "Pierakstu atbildi ar mērvienību un vārdu «apmēram».",
    ]),

    Majas([
        "Izmēri kāda apaļa trauka diametru un aprēķini, cik garu lenti tam "
        "vajag.",
        "Aprēķini, cik stieples vajag grozam ar rādiusu 15 cm.",
        "Padomā, cik daudz vairāk jāpieliek savienojumam.",
    ]),
]
