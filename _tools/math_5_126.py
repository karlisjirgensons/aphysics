# -*- coding: utf-8 -*-
"""5. klase, 126. stunda: «Kā sadalīt kombinētu figūru?»

Kombinētai figūrai laukuma formulas nav, un tieši tāpēc tā ir interesanta:
jāizdomā pašam, kā to sadalīt gabalos, kuriem formula ir. Sadalījumu parasti
var izvēlēties vairākos veidos, un visi dod vienu atbildi - tāpēc stundā
prasa ne tikai sadalīt, bet arī pamatot izvēli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kā sadalīt kombinētu figūru?"

MERKIS = ("Mācīsimies sadalīt kombinētu figūru taisnstūros un taisnleņķa "
          "trijstūros.")

SATURS = [
    Sakums("Burta L formas grīda",
           zimejums=figura([(0, 0), (6, 0), (6, 2), (3, 2), (3, 5), (0, 5)],
                           virsraksts="Kombinēta figūra"),
           paraksts="Vienas formulas te nav - bet ir divas taisnstūra "
                    "formulas.",
           fakti=["Šai figūrai laukuma formulas nav.",
                  "Bet to var sagriezt divos taisnstūros.",
                  "Katram taisnstūrim formula ir zināma."]),

    Doma("Sagriez gabalos, kuriem formula ir",
         "Kombinētu figūru sadala taisnstūros un taisnleņķa trijstūros; katra "
         "gabala laukumu aprēķina atsevišķi un tad saskaita.",
         soli=[
             "Apskati figūru un atrodi ieliektās vietas.",
             "Novelc līniju, kas figūru sadala taisnstūros.",
             "Apzīmē katru gabalu ar numuru.",
             "Pieraksti katra gabala malas.",
             "Pārbaudi, vai gabali nepārklājas un nekas nav palicis pāri.",
         ],
         pieze="To pašu figūru var arī papildināt līdz lielam taisnstūrim un "
               "no tā laukuma atņemt iztrūkstošo gabalu. Abi ceļi ir "
               "pareizi - izvēlas to, kurā mazāk rēķinu."),

    Paraugs("Sadali L formas figūru",
            uzd="Figūras malas ir 6, 2, 3, 3, 3 un 5 rūtiņas. Kā to sadalīt?",
            soli=[
                ("Novelc horizontālu līniju augstumā 2",
                 "Pirmais sadalījums."),
                ("Apakšējais gabals: 6 x 2",
                 "Pirmais taisnstūris."),
                ("Augšējais gabals: 3 x 3",
                 "Otrais taisnstūris."),
                ("Gabali nepārklājas",
                 "Katra rūtiņa pieder tieši vienam gabalam."),
                ("Cits ceļš: vertikāla līnija dod 3 x 5 un 3 x 2",
                 "Arī pareizi."),
            ],
            atbilde="Der abi sadalījumi: 6 x 2 un 3 x 3 vai 3 x 5 un 3 x 2"),

    Ievadi("Cik liels ir katrs gabals?", [
        {"jaut": "Taisnstūris 6 x 2. Cik rūtiņu ir tā laukums?",
         "atb": ["12"], "padoms": "6 · 2."},
        {"jaut": "Taisnstūris 3 x 3. Cik rūtiņu ir tā laukums?",
         "atb": ["9"], "padoms": "3 · 3."},
        {"jaut": "Cik rūtiņu ir abu gabalu laukums kopā?",
         "atb": ["21"], "padoms": "12 + 9."},
        {"jaut": "Otrs sadalījums: 3 x 5. Cik rūtiņu?",
         "atb": ["15"], "padoms": "3 · 5."},
        {"jaut": "Otrs gabals: 3 x 2. Cik rūtiņu?",
         "atb": ["6"], "padoms": "3 · 2."},
        {"jaut": "Cik rūtiņu ir abu šo gabalu laukums kopā?",
         "atb": ["21"], "padoms": "15 + 6."},
        {"jaut": "Liels taisnstūris 6 x 5. Cik rūtiņu?",
         "atb": ["30"], "padoms": "6 · 5."},
        {"jaut": "No 30 rūtiņām atņem iztrūkstošo gabalu 3 x 3. Cik paliek?",
         "atb": ["21"], "padoms": "30 - 9."},
    ], pamats=4,
        ievads="Visi trīs ceļi dod vienu un to pašu skaitli."),

    Zimejums("Tā pati figūra, cits sadalījums",
             figura([(0, 0), (3, 0), (3, 5), (0, 5)],
                    platums=7, augstums=6,
                    virsraksts="Vertikālais gabals 3 x 5"),
             paskaidro="Ja līniju velk vertikāli, pirmais gabals ir 3 x 5, "
                       "bet otrs - 3 x 2. Kopā tās pašas 21 rūtiņas.",
             ievads="Sadalījumu izvēlas pats, atbilde nemainās."),

    Varianti("Kā sadala figūru?", [
        {"jaut": "Kādos gabalos sadala kombinētu figūru?",
         "opcijas": ["Taisnstūros un taisnleņķa trijstūros",
                     "Riņķos",
                     "Vienādos gabalos",
                     "Jebkādos gabalos"],
         "pareizi": 0,
         "padoms": "Tajos, kuriem ir formula."},
        {"jaut": "Ko pārbauda pēc sadalīšanas?",
         "opcijas": ["Vai gabali nepārklājas un nekas nav palicis pāri",
                     "Vai gabali ir vienādi",
                     "Vai gabalu ir divi",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Katra rūtiņa - tieši vienam gabalam."},
        {"jaut": "Cik veidos var sadalīt L formas figūru?",
         "opcijas": ["Vismaz divos", "Tikai vienā", "Nevienā", "Tieši trīs"],
         "pareizi": 0,
         "padoms": "Horizontāli vai vertikāli."},
        {"jaut": "Kāds ir otrs ceļš, ja negrib sadalīt?",
         "opcijas": ["Papildināt līdz lielam taisnstūrim un atņemt",
                     "Mērīt ar lineālu",
                     "Skaitīt rūtiņas",
                     "Tāda nav"],
         "pareizi": 0,
         "padoms": "Atņemšana, nevis saskaitīšana."},
        {"jaut": "Vai dažādi sadalījumi dod dažādus laukumus?",
         "opcijas": ["Nē, laukums ir viens", "Jā", "Reizēm",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Figūra nemainās."},
        {"jaut": "Kurš sadalījums ir labāks?",
         "opcijas": ["Tas, kurā mazāk rēķinu", "Vienmēr horizontālais",
                     "Vienmēr vertikālais", "Tas ir vienalga"],
         "pareizi": 0,
         "padoms": "Mazāk gabalu - mazāk kļūdu."},
    ], pamats=4),

    Pasaule("Kā aprēķināt istabas grīdu?",
            Ievadi("", [
                {"jaut": "Istaba ir L formas: 6 m x 2 m un 3 m x 3 m. Cik "
                         "kvadrātmetru ir pirmais gabals?",
                 "atb": ["12"], "padoms": "6 · 2."},
                {"jaut": "Cik kvadrātmetru ir otrais gabals?",
                 "atb": ["9"], "padoms": "3 · 3."},
                {"jaut": "Cik kvadrātmetru ir visa grīda?",
                 "atb": ["21"], "padoms": "12 + 9."},
                {"jaut": "Cik kvadrātmetru būtu lielajam taisnstūrim 6 m x "
                         "5 m?",
                 "atb": ["30"], "padoms": "6 · 5."},
            ]),
            pavediens="maja",
            konteksts="Istabas reti ir taisnstūri; parasti tām ir izcilnis "
                      "vai niša.",
            kapec="Sadalot gabalos, laukumu var izrēķināt ar zināmajām "
                  "formulām."),

    Kopsavilkums([
        "Sadalu kombinētu figūru taisnstūros.",
        "Pārbaudu, vai gabali nepārklājas un nekas nav palicis pāri.",
        "Zinu, ka to pašu figūru var sadalīt vairākos veidos.",
        "Lietoju arī otru ceļu: papildinu līdz taisnstūrim un atņemu.",
    ]),

    Majas([
        "Uzzīmē L formas figūru un sadali to divos veidos.",
        "Aprēķini laukumu abos veidos un salīdzini.",
        "Atrodi mājās telpu, kas nav taisnstūris.",
    ]),
]
