# -*- coding: utf-8 -*-
"""7. klase, 5. stunda: «Cik cilvēku ir kopā?»

Ja skaita divu kopu elementus kopā, kopīgie tiek saskaitīti divreiz. Tāpēc
apvienojuma elementu skaits ir abu kopu skaitu summa mīnus šķēluma
skaits. Stunda to parāda ar Venna diagrammu un aptaujām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, venna)

TEMA = "Cik cilvēku ir kopā?"

MERKIS = ("Iemācīsimies saskaitīt divu kopu elementus tā, lai kopīgos "
          "neskaitītu divreiz.")

SATURS = [
    Sakums("18 + 15 = 33? Bet klasē ir tikai 25!",
           fakti=["Aptaujā 18 skolēni skatās YouTube, 15 - TikTok.",
                  "Klasē ir 25 skolēni, un katrs lieto kaut vienu.",
                  "Tātad daži tika saskaitīti divreiz. Cik?"]),

    Doma("Kopīgos atņem vienu reizi",
         "Apvienojuma elementu skaits ir abu kopu elementu skaitu summa "
         "mīnus šķēluma elementu skaits: n(A ∪ B) = n(A) + n(B) − n(A ∩ B).",
         soli=[
             "Uzzīmē Venna diagrammu.",
             "Vispirms ieraksti šķēlumu - tos, kas ir abās kopās.",
             "Tad aprēķini «tikai A» un «tikai B».",
             "Saskaiti visas trīs daļas.",
         ],
         pieze="n(A) nozīmē kopas A elementu skaitu. Diagrammu aizpilda no "
               "vidus uz malām - tā kopīgie nekad netiek skaitīti divreiz."),

    Paraugs("Klases aptauja",
            uzd="Klasē ir 25 skolēni. 18 skatās YouTube, 15 - TikTok, katrs "
                "lieto kaut vienu. Cik skolēnu lieto abus?",
            soli=[
                ("n(A ∪ B) = n(A) + n(B) − n(A ∩ B)",
                 "Formula."),
                ("25 = 18 + 15 − n(A ∩ B)",
                 "Ievieto skaitļus."),
                ("n(A ∩ B) = 33 − 25 = 8",
                 "Tik daudz tika saskaitīti divreiz."),
                ("Tikai YouTube: 18 − 8 = 10; tikai TikTok: 15 − 8 = 7",
                 "Pārbaude: 10 + 8 + 7 = 25."),
            ],
            atbilde="Abus lieto 8 skolēni."),

    Slidnis("Aizpildi diagrammu no vidus", [
        {"v": "1. solis", "teksts": "Šķēlumā - 8 skolēni, kas lieto abus.",
         "zim": venna([], [], ["8"], ("YouTube", "TikTok"))},
        {"v": "2. solis", "teksts": "Tikai YouTube: 18 − 8 = 10.",
         "zim": venna(["10"], [], ["8"], ("YouTube", "TikTok"))},
        {"v": "3. solis", "teksts": "Tikai TikTok: 15 − 8 = 7.",
         "zim": venna(["10"], ["7"], ["8"], ("YouTube", "TikTok"))},
        {"v": "Kopā", "teksts": "10 + 8 + 7 = 25 - visa klase.",
         "zim": venna(["10"], ["7"], ["8"], ("YouTube", "TikTok"))},
    ], ievads="Spied soļus un skaties, kā diagramma piepildās."),

    Ievadi("Aprēķini", [
        {"jaut": "n(A) = 12, n(B) = 9, n(A ∩ B) = 4. Cik ir n(A ∪ B)?",
         "atb": ["17"], "padoms": "12 + 9 − 4."},
        {"jaut": "n(A) = 20, n(B) = 14, n(A ∪ B) = 28. Cik ir n(A ∩ B)?",
         "atb": ["6"], "padoms": "20 + 14 − 28."},
        {"jaut": "n(A) = 10, n(A ∩ B) = 3. Cik elementu ir tikai A?",
         "atb": ["7"], "padoms": "10 − 3."},
        {"jaut": "n(A ∪ B) = 30, n(A) = 30, n(B) = 12. Cik ir n(A ∩ B)?",
         "atb": ["12"], "padoms": "Tad B ⊂ A."},
        {"jaut": "Tikai A - 5, tikai B - 6, abās - 4. Cik ir n(A ∪ B)?",
         "atb": ["15"], "padoms": "5 + 6 + 4."},
        {"jaut": "Tikai A - 5, tikai B - 6, abās - 4. Cik ir n(B)?",
         "atb": ["10"], "padoms": "6 + 4."},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "Līga saka: «Sportā 12, mūzikā 9, tātad pulciņos ir 21 "
                 "skolēns.» Kas jāzina, lai to pārbaudītu?",
         "opcijas": ["Cik skolēnu apmeklē abus pulciņus",
                     "Cik skolēnu ir skolā",
                     "Kurš pulciņš ir populārāks",
                     "Nekas - 21 ir pareizi"],
         "pareizi": 0,
         "padoms": "Kopīgie ir saskaitīti divreiz."},
        {"jaut": "n(A) = 8, n(B) = 6. Kāds ir mazākais iespējamais "
                 "n(A ∪ B)?",
         "opcijas": ["8", "14", "6", "2"],
         "pareizi": 0,
         "padoms": "Ja visa B ir A iekšā."},
        {"jaut": "n(A) = 8, n(B) = 6. Kāds ir lielākais iespējamais "
                 "n(A ∪ B)?",
         "opcijas": ["14", "8", "48", "2"],
         "pareizi": 0,
         "padoms": "Ja kopīgu nav."},
    ]),

    Pasaule("Festivāla biļetes",
            Ievadi("", [
                {"jaut": "Festivālā 420 cilvēki nopirka biļeti uz pirmo "
                         "dienu, 350 - uz otro, 130 - uz abām. Cik "
                         "dažādu cilvēku bija festivālā?",
                 "atb": ["640"], "padoms": "420 + 350 − 130."},
                {"jaut": "Cik cilvēku bija tikai pirmajā dienā?",
                 "atb": ["290"], "padoms": "420 − 130."},
                {"jaut": "Aproces izdala katram apmeklētājam vienu. Cik "
                         "aproču vajag?",
                 "atb": ["640"], "padoms": "Katram cilvēkam vienu."},
            ]),
            pavediens="celojums",
            konteksts="Organizatoriem jāzina, cik dažādu cilvēku ieradīsies, "
                      "nevis cik biļešu pārdots.",
            kapec="Biļešu skaits un cilvēku skaits atšķiras par šķēlumu."),

    Kopsavilkums([
        "Lietoju n(A ∪ B) = n(A) + n(B) − n(A ∩ B).",
        "Aizpildu Venna diagrammu no vidus uz malām.",
        "Atrodu, cik ir «tikai A» un «tikai B».",
        "Pārbaudu: visu daļu summa ir apvienojums.",
    ]),

    Majas([
        "Aptaujā ģimeni: kurš mīl tēju, kurš kafiju. Uzzīmē diagrammu.",
        "Izdomā uzdevumu, kurā atbilde ir 5 cilvēki abās kopās.",
        "Kāpēc diagrammu aizpilda no vidus? Paskaidro draugam.",
    ]),
]
