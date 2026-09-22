# -*- coding: utf-8 -*-
"""5. klase, 108. stunda: «Kāds leņķis ir lielāks nekā plats?»

Jauna temata pirmā stunda. Šauru, taisnu un platu leņķi skolēns jau zina no
4. klases; te sarakstam pievienojas vēl trīs - izstiepts, atvērts un pilns.
Visu kārto viena skala no 0 līdz 360 grādiem, tāpēc stunda nemāca sešus
jaunus vārdus, bet vienu asi ar sešām atzīmēm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         lenkis, taisne)

TEMA = "Kāds leņķis ir lielāks nekā plats?"

MERKIS = ("Iemācīsimies raksturot izstieptu, pilnu un atvērtu leņķi un "
          "nosaukt to lielumu grādos.")

SATURS = [
    Sakums("Leņķis, kas izlocīts taisnē",
           zimejums=lenkis([(0, "A"), (180, "B")], loki=[(0, 180, "180°")],
                           virsraksts="Izstiepts leņķis"),
           paraksts="Abi stari veido taisni, bet tas joprojām ir leņķis.",
           fakti=["Taisns leņķis ir 90°, plats - vairāk par 90°.",
                  "Izstiepts leņķis ir tieši 180°.",
                  "Pilns leņķis ir 360° - viss apgrieziens."]),

    Doma("Visi leņķi ir uz vienas skalas",
         "Leņķa veidu nosaka tā lielums grādos: šaurs līdz 90°, taisns 90°, "
         "plats līdz 180°, izstiepts 180°, atvērts līdz 360°, pilns 360°.",
         soli=[
             "Nosaki leņķa lielumu grādos.",
             "Salīdzini to ar 90°, 180° un 360°.",
             "Izvēlies nosaukumu pēc tā, starp kurām atzīmēm tas iekrīt.",
             "Pārbaudi: taisnam un izstieptam ir tieši viens lielums.",
         ],
         pieze="Atvērts leņķis skolēnam šķiet dīvains, jo tas izskatās pēc "
               "«ārpuses». Tomēr tas ir īsts leņķis: 270° ir trīs "
               "ceturtdaļas no pilna apgrieziena."),

    Slidnis("Viens stars griežas",
            [{"v": "45°", "teksts": "šaurs leņķis", "josla": 12,
              "zim": lenkis([(0, ""), (45, "")], loki=[(0, 45, "45°")])},
             {"v": "90°", "teksts": "taisns leņķis", "josla": 25,
              "zim": lenkis([(0, ""), (90, "")], loki=[(0, 90, "90°")])},
             {"v": "135°", "teksts": "plats leņķis", "josla": 37,
              "zim": lenkis([(0, ""), (135, "")], loki=[(0, 135, "135°")])},
             {"v": "180°", "teksts": "izstiepts leņķis", "josla": 50,
              "zim": lenkis([(0, ""), (180, "")], loki=[(0, 180, "180°")])},
             {"v": "270°", "teksts": "atvērts leņķis", "josla": 75,
              "zim": lenkis([(0, ""), (270, "")],
                            loki=[(0, 270, "270°")])}],
            ievads="Spied soli pa solim: stars griežas, un leņķis pēc kārtas "
                   "iziet cauri visiem veidiem."),

    Paraugs("Kāds leņķis ir 210°?",
            uzd="Nosauc leņķa veidu, ja tā lielums ir 210°.",
            soli=[
                ("210° > 180°",
                 "Lielāks par izstieptu."),
                ("210° < 360°",
                 "Mazāks par pilnu."),
                ("Tātad tas ir atvērts leņķis",
                 "Starp izstieptu un pilnu."),
                ("210° ir mazliet vairāk nekā puse apgrieziena",
                 "180° ir tieši puse."),
            ],
            atbilde="210° ir atvērts leņķis"),

    Ievadi("Nosauc leņķa veidu", [
        {"jaut": "Cik grādu ir izstieptam leņķim?",
         "atb": ["180"], "padoms": "Puse apgrieziena."},
        {"jaut": "Cik grādu ir pilnam leņķim?",
         "atb": ["360"], "padoms": "Viss apgrieziens."},
        {"jaut": "Cik grādu ir taisnam leņķim?",
         "atb": ["90"], "padoms": "Ceturtdaļa apgrieziena."},
        {"jaut": "45° leņķis ir šaurs, taisns, plats vai atvērts? Raksti "
                 "vienu vārdu.",
         "atb": ["šaurs", "saurs"], "padoms": "Mazāks par 90°."},
        {"jaut": "135° leņķis ir šaurs, taisns, plats vai atvērts?",
         "atb": ["plats"], "padoms": "Starp 90° un 180°."},
        {"jaut": "270° leņķis ir šaurs, taisns, plats vai atvērts?",
         "atb": ["atvērts", "atverts"], "padoms": "Starp 180° un 360°."},
        {"jaut": "Cik grādu ir pusei no izstiepta leņķa?",
         "atb": ["90"], "padoms": "180 : 2."},
        {"jaut": "Cik grādu ir ceturtdaļai no pilna leņķa?",
         "atb": ["90"], "padoms": "360 : 4."},
    ], pamats=4,
        ievads="Salīdzini leņķi ar 90°, 180° un 360° - tas jau ir viss."),

    Zimejums("Pilns leņķis ir viss apgrieziens",
             taisne(0, 360, 90, [(90, "taisns"), (180, "izstiepts"),
                                 (360, "pilns")],
                    virsraksts="Skala no 0° līdz 360°"),
             paskaidro="Uz šīs skalas katram leņķa veidam ir sava vieta: "
                       "šauri pa kreisi no 90°, atvērti - pa labi no 180°.",
             ievads="Sešus nosaukumus var izvietot uz vienas ass."),

    Varianti("Kurš leņķis tas ir?", [
        {"jaut": "Kāds leņķis ir 180°?",
         "opcijas": ["Izstiepts", "Taisns", "Plats", "Pilns"],
         "pareizi": 0,
         "padoms": "Abi stari veido taisni."},
        {"jaut": "Kāds leņķis ir 300°?",
         "opcijas": ["Atvērts", "Plats", "Pilns", "Izstiepts"],
         "pareizi": 0,
         "padoms": "Starp 180° un 360°."},
        {"jaut": "Kāds leņķis ir 90°?",
         "opcijas": ["Taisns", "Šaurs", "Plats", "Izstiepts"],
         "pareizi": 0,
         "padoms": "Ceturtdaļa apgrieziena."},
        {"jaut": "Kurš leņķis ir lielāks par platu, bet mazāks par pilnu?",
         "opcijas": ["Atvērts", "Šaurs", "Taisns", "Tāda nav"],
         "pareizi": 0,
         "padoms": "Vairāk par 180°."},
        {"jaut": "Cik taisnu leņķu ietilpst pilnā leņķī?",
         "opcijas": ["4", "2", "3", "6"],
         "pareizi": 0,
         "padoms": "360 : 90."},
        {"jaut": "Cik taisnu leņķu ietilpst izstieptā leņķī?",
         "opcijas": ["2", "1", "3", "4"],
         "pareizi": 0,
         "padoms": "180 : 90."},
    ], pamats=4),

    Pasaule("Cik pagriežas robota roka?",
            Ievadi("", [
                {"jaut": "Roka pagriežas par ceturtdaļu apgrieziena. Cik "
                         "grādu tas ir?",
                 "atb": ["90"], "padoms": "360 : 4."},
                {"jaut": "Roka pagriežas par pusi apgrieziena. Cik grādu?",
                 "atb": ["180"], "padoms": "360 : 2."},
                {"jaut": "Roka pagriežas par trim ceturtdaļām. Cik grādu?",
                 "atb": ["270"], "padoms": "90 · 3."},
                {"jaut": "Roka pagriezās par 360°. Cik apgriezienu tas ir?",
                 "atb": ["1"], "padoms": "Pilns leņķis."},
            ]),
            pavediens="tehnika",
            konteksts="Robota rokai pagriezienu uzdod grādos, un 270° tur ir "
                      "tikpat parasta pavēle kā 90°.",
            kapec="Bez atvērta leņķa jēdziena pusi pagriezienu nosaukt "
                  "nevarētu."),

    Kopsavilkums([
        "Nosaucu izstiepta, pilna un atvērta leņķa lielumu grādos.",
        "Raksturoju leņķi pēc tā, starp kurām atzīmēm tas iekrīt.",
        "Zinu, ka taisnam un izstieptam leņķim ir tieši viens lielums.",
        "Saistu leņķi ar apgrieziena daļu.",
    ]),

    Majas([
        "Uzzīmē pa vienam katra veida leņķim un pieraksti to lielumu.",
        "Atrodi mājās trīs leņķus un nosauc to veidus.",
        "Padomā, cik grādu pagriežas pulksteņa stundu rādītājs 6 stundās.",
    ]),
]
