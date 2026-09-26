# -*- coding: utf-8 -*-
"""7. klase, 48. stunda: «Kā izskatās apgriezti proporcionāla sakarība?»

Taisnstūriem ar vienu un to pašu laukumu vienu malu palielinot, otra
samazinās tikpat reižu. Reizinājums paliek nemainīgs: ab = 24. Tā ir
apgriezti proporcionāla sakarība, un tās grafiks nav taisne, bet līkne.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         figura, plakne, restis)

TEMA = "Kā izskatās apgriezti proporcionāla sakarība?"

MERKIS = ("Apkoposim tabulā taisnstūra malas ar doto laukumu un attēlosim "
          "sakarību grafiski.")

_LIKNE = [(x / 4.0, 24 / (x / 4.0)) for x in range(4, 49)]

SATURS = [
    Sakums("24 flīzes - cik dažādu taisnstūru?",
           zimejums=restis([["a", "1", "2", "3", "4", "6", "8", "12", "24"],
                            ["b", "24", "12", "8", "6", "4", "3", "2", "1"]]),
           paraksts="Katrā kolonnā a · b = 24.",
           fakti=["Platāks taisnstūris - īsāks.",
                  "Divreiz platāks - divreiz īsāks."]),

    Doma("Reizinājums ir nemainīgs",
         "Lielumi x un y ir apgriezti proporcionāli, ja to reizinājums ir "
         "nemainīgs: xy = k jeb y = {k|x}. Ja x palielina n reizes, y "
         "samazinās n reizes.",
         soli=[
             "Tabulā sareizini x un y katrā kolonnā.",
             "Ja visur tas pats k - apgriezti proporcionāli.",
             "Formula: y = {k|x}.",
             "Grafiks ir līkne (hiperbolas zars), nevis taisne.",
         ],
         pieze="Salīdzini: tiešajā proporcionalitātē nemainīgs ir dalījums "
               "{y|x}, apgrieztajā - reizinājums xy."),

    Slidnis("Laukums paliek 24", [
        {"v": "a = 2, b = 12", "teksts": "2 · 12 = 24",
         "zim": figura([(0, 0), (2, 0), (2, 12), (0, 12)], platums=13,
                       augstums=13)},
        {"v": "a = 4, b = 6", "teksts": "4 · 6 = 24",
         "zim": figura([(0, 0), (4, 0), (4, 6), (0, 6)], platums=13,
                       augstums=13)},
        {"v": "a = 6, b = 4", "teksts": "6 · 4 = 24",
         "zim": figura([(0, 0), (6, 0), (6, 4), (0, 4)], platums=13,
                       augstums=13)},
        {"v": "a = 12, b = 2", "teksts": "12 · 2 = 24",
         "zim": figura([(0, 0), (12, 0), (12, 2), (0, 2)], platums=13,
                       augstums=13)},
    ], ievads="Spied soļus: taisnstūris izstiepjas, bet laukums nemainās."),

    Zimejums("Grafiks b = 24 : a",
             plakne(grafiki=[(_LIKNE, "")],
                    punkti=[(2, 12), (3, 8), (4, 6), (6, 4), (8, 3),
                            (12, 2)],
                    no_x=0, lidz_x=12, no_y=0, lidz_y=24, solis=2,
                    solis_y=4, x_nos="a", y_nos="b"),
             paskaidro="Punkti nav uz taisnes - tie veido līkni."),

    Paraugs("Pārbaudi un uzraksti formulu",
            uzd="x = 2; 5; 10, y = 15; 6; 3. Vai sakarība ir apgriezti "
                "proporcionāla?",
            soli=[
                ("2 · 15 = 30", "Pirmā kolonna."),
                ("5 · 6 = 30; 10 · 3 = 30", "Pārējās."),
                ("xy = 30", "Reizinājums nemainīgs."),
                ("y = {30|x}", "Formula."),
            ],
            atbilde="Jā, y = {30|x}"),

    Varianti("Tiešā vai apgrieztā?", [
        {"jaut": "Strādnieku skaits un laiks, kurā izrok grāvi",
         "opcijas": ["Apgriezti proporcionāli", "Tieši proporcionāli",
                     "Nav proporcionāli"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Divreiz vairāk strādnieku - divreiz ātrāk."},
        {"jaut": "Ātrums un laiks, lai nobrauktu 120 km",
         "opcijas": ["Apgriezti proporcionāli", "Tieši proporcionāli",
                     "Nav proporcionāli"],
         "pareizi": 0, "jaukt": False,
         "padoms": "vt = 120."},
        {"jaut": "Litru skaits un cena",
         "opcijas": ["Apgriezti proporcionāli", "Tieši proporcionāli",
                     "Nav proporcionāli"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Vairāk litru - lielāka cena."},
        {"jaut": "Vecums un augums",
         "opcijas": ["Apgriezti proporcionāli", "Tieši proporcionāli",
                     "Nav proporcionāli"],
         "pareizi": 2, "jaukt": False,
         "padoms": "Augšana nav vienmērīga."},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "xy = 36. Cik ir y, ja x = 9?",
         "atb": ["4"], "padoms": "36 : 9."},
        {"jaut": "4 strādnieki izdara darbu 6 dienās. Cik dienās to "
                 "izdarīs 8 strādnieki?",
         "atb": ["3"], "padoms": "4 · 6 = 24 cilvēkdienas."},
        {"jaut": "Ar 60 km/h brauc 2 h. Cik h ar 80 km/h?",
         "atb": ["1,5"], "padoms": "120 : 80."},
        {"jaut": "Taisnstūra laukums 48 cm², viena mala 6 cm. Otra (cm)?",
         "atb": ["8"], "padoms": "48 : 6."},
    ]),

    Pasaule("Picas dalīšana",
            Ievadi("", [
                {"jaut": "Pica 1200 g sadalīta vienādi starp n draugiem. "
                         "Cik g katram, ja n = 4?",
                 "atb": ["300"], "padoms": "1200 : 4."},
                {"jaut": "Cik g katram, ja atnāk vēl 2 draugi?",
                 "atb": ["200"], "padoms": "1200 : 6."},
                {"jaut": "Draugu skaits pieauga 1,5 reizes. Cik reizes "
                         "samazinājās porcija?",
                 "atb": ["1,5"], "padoms": "Apgriezti proporcionāli."},
            ]),
            pavediens="virtuve",
            konteksts="Vairāk viesu - mazākas porcijas: tā ir apgrieztā "
                      "proporcionalitāte.",
            kapec="Reizinājums (visa pica) nemainās."),

    Kopsavilkums([
        "Atpazīstu apgriezto proporcionalitāti pēc reizinājuma.",
        "Pierakstu formulu y = {k|x}.",
        "Zinu, ka grafiks ir līkne, nevis taisne.",
        "Atšķiru tiešo un apgriezto proporcionalitāti.",
    ]),

    Majas([
        "Izveido tabulu taisnstūriem ar laukumu 36 cm².",
        "Uzzīmē grafiku no šīs tabulas.",
        "Atrodi dzīvē vēl vienu apgriezti proporcionālu sakarību.",
    ]),
]
