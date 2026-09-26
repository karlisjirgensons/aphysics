# -*- coding: utf-8 -*-
"""7. klase, 23. stunda: «Kur atrodas visi šie punkti?»

Figūru var noteikt ar īpašību: visi punkti, kas ir 2 cm no dotā punkta,
veido riņķa līniju; visi punkti, kas vienādā attālumā no A un B, - nogriežņa
vidusperpendikulu. Stunda iemāca atrast šādu punktu kopu un formulēt to.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kur atrodas visi šie punkti?"

MERKIS = ("Noteiksim, kur atrodas visi punkti ar doto īpašību, un "
          "formulēsim apgalvojumu par tiem.")

_VIDUS = geometrija(
    [("A", 0, 0), ("B", 6, 0), ("M", 3, 0, -60), ("P", 3, 3.2, 180),
     ("_a", 3, -1.6), ("_b", 3, 4.2)],
    nogriezni=["AB", "PA", "PB"], taisnes=[("_a", "_b")],
    svitras=[("AM", 1), ("MB", 1), ("PA", 2), ("PB", 2)],
    taisni=[("A", "M", "_b")])

SATURS = [
    Sakums("Kur uzbūvēt veikalu vienādā attālumā no divām mājām?",
           zimejums=_VIDUS,
           paraksts="Visi šādi punkti ir uz vienas taisnes - "
                    "vidusperpendikula.",
           fakti=["Punkts P ir vienādā attālumā no A un B.",
                  "Tādu punktu ir bezgalīgi daudz - bet ne jebkur."]),

    Doma("Punktu kopa ar īpašību ir figūra",
         "Visi plaknes punkti, kas atrodas dotajā attālumā r no punkta O, "
         "veido riņķa līniju. Visi punkti, kas atrodas vienādā attālumā no "
         "punktiem A un B, veido nogriežņa AB vidusperpendikulu.",
         soli=[
             "Atrodi dažus punktus ar doto īpašību.",
             "Paskaties, uz kādas līnijas tie izvietojas.",
             "Formulē apgalvojumu: «visi punkti, kas ..., atrodas uz ...».",
             "Pārbaudi ar vēl vienu punktu.",
         ],
         pieze="Vidusperpendikuls ir taisne, kas iet caur nogriežņa "
               "viduspunktu un ir perpendikulāra nogrieznim."),

    Paraugs("Punkti noteiktā attālumā no taisnes",
            uzd="Kur atrodas visi punkti, kas ir 2 cm attālumā no taisnes a?",
            soli=[
                ("Atliec 2 cm uz augšu no vairākiem taisnes punktiem",
                 "Tie izvietojas uz taisnes, paralēlas a."),
                ("Tas pats uz leju", "Otrā pusē vēl viena taisne."),
                ("Divas taisnes, paralēlas a, 2 cm attālumā",
                 "Formulē apgalvojumu."),
            ],
            atbilde="Uz divām taisnēm, kas paralēlas a un atrodas 2 cm "
                    "attālumā no tās."),

    Zimejums("2 cm no taisnes abās pusēs",
             geometrija([("_1", 0, 0), ("_2", 10, 0), ("_3", 0, 2),
                         ("_4", 10, 2), ("_5", 0, -2), ("_6", 10, -2)],
                        taisnes=[("_1", "_2")],
                        izcelti=[("_3", "_4"), ("_5", "_6")],
                        uzraksti=[(10.6, 0.3, "a")]),
             paskaidro="Dzintara krāsas līnijas ir visi punkti 2 cm "
                       "attālumā no a."),

    Varianti("Kāda figūra sanāk?", [
        {"jaut": "Visi punkti 3 cm attālumā no punkta O",
         "opcijas": ["Riņķa līnija ar centru O un r = 3 cm",
                     "Riņķis ar r = 3 cm",
                     "Kvadrāts ar malu 3 cm",
                     "Taisne caur O"],
         "pareizi": 0,
         "padoms": "Tieši 3 cm - tikai līnija."},
        {"jaut": "Visi punkti, kas nav tālāk par 3 cm no punkta O",
         "opcijas": ["Riņķis ar r = 3 cm",
                     "Riņķa līnija ar r = 3 cm",
                     "Divi punkti", "Nogrieznis 3 cm"],
         "pareizi": 0,
         "padoms": "Ar iekšpusi."},
        {"jaut": "Visi punkti, kas vienādā attālumā no A un B",
         "opcijas": ["AB vidusperpendikuls", "Nogrieznis AB",
                     "AB viduspunkts", "Riņķa līnija"],
         "pareizi": 0,
         "padoms": "Skat. sākuma attēlu."},
        {"jaut": "Visi punkti 5 cm no O un 5 cm no taisnes caur O",
         "opcijas": ["4 punkti", "1 punkts", "2 punkti", "Riņķa līnija"],
         "pareizi": 0,
         "padoms": "Riņķa līnijas un divu taišņu šķēlums."},
    ], pamats=4),

    Petijums("Atrodi visus punktus ar cirkuli",
             ["Uzzīmē nogriezni AB = 6 cm.",
              "Ar cirkuli no A un no B novelc lokus ar vienādu rādiusu "
              "(piemēram, 4 cm), lai tie krustojas.",
              "Atkārto ar rādiusu 5 cm un 7 cm.",
              "Savieno visus krustpunktus. Kāda līnija sanāk?"],
             vajag="cirkulis, lineāls, zīmulis",
             secinajums="Visi krustpunkti ir uz vienas taisnes - AB "
                         "vidusperpendikula."),

    Pasaule("Mobilā tīkla zona",
            Varianti("", [
                {"jaut": "Tornis pārklāj 8 km rādiusā. Kur ir zonas robeža?",
                 "opcijas": ["Uz riņķa līnijas ar r = 8 km",
                             "Uz taisnes 8 km no torņa",
                             "Kvadrātā 8 × 8 km",
                             "Vienā punktā"],
                 "pareizi": 0,
                 "padoms": "Visi punkti 8 km attālumā."},
                {"jaut": "Tālrunis pārslēdzas uz tuvāko torni. Kur ir "
                         "robeža starp divu torņu zonām?",
                 "opcijas": ["Uz nogriežņa starp torņiem vidusperpendikula",
                             "Pie viena torņa",
                             "Uz riņķa līnijas",
                             "Nav robežas"],
                 "pareizi": 0,
                 "padoms": "Vienādā attālumā no abiem."},
                {"jaut": "Torņi ir 10 km viens no otra. Cik km no katra "
                         "robeža šķērso taisni starp tiem?",
                 "opcijas": ["5 km", "10 km", "8 km", "20 km"],
                 "pareizi": 0,
                 "padoms": "Viduspunkts."},
            ]),
            pavediens="dati",
            konteksts="Tālruņu tīkls sadala karti zonās pēc tā, kurš tornis "
                      "ir tuvāk.",
            kapec="Vidusperpendikuls ir «vienlīdz tuvu» robeža."),

    Kopsavilkums([
        "Nosaku, kur atrodas punkti ar doto īpašību.",
        "Zinu: punkti r attālumā no O - riņķa līnija.",
        "Zinu: punkti vienādā attālumā no A un B - vidusperpendikuls.",
        "Formulēju apgalvojumu par punktu kopu.",
    ]),

    Majas([
        "Atzīmē kartē savu māju un skolu. Kur būtu vieta vienādā attālumā?",
        "Uzzīmē visus punktus 1 cm attālumā no nogriežņa 4 cm.",
        "Apraksti šo figūru vārdiem.",
    ]),
]
