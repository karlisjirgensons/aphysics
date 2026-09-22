# -*- coding: utf-8 -*-
"""5. klase, 145. stunda: «Kā decimāldaļu izteikt procentos?»

Pretējais virziens iepriekšējai stundai. Decimāldaļu līdz simtdaļām var
izlasīt procentos bez rēķina: 0,25 ir divdesmit piecas simtdaļas, tātad
25 %. Grūtākais te ir 0,3 - viens cipars aiz komata -, jo tas vispirms
jāpaplašina līdz simtdaļām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā decimāldaļu izteikt procentos?"

MERKIS = ("Iemācīsimies pierakstīt decimāldaļu līdz simtdaļām kā procentus.")

SATURS = [
    Sakums("Divi cipari aiz komata - gatavi procenti",
           zimejums=restis([["0,25", "25 %"],
                            ["0,3", "30 %"]],
                           virsraksts="No komata uz procentiem"),
           paraksts="0,3 = 0,30, tāpēc tas ir 30 %, nevis 3 %.",
           fakti=["Divi cipari aiz komata ir simtdaļas.",
                  "Simtdaļu skaits ir procentu skaits.",
                  "Vienu ciparu vispirms paplašina līdz diviem."]),

    Doma("Izlasi simtdaļas",
         "Decimāldaļu izsaka procentos, nolasot simtdaļu skaitu; ja aiz "
         "komata ir viens cipars, to vispirms paplašina ar nulli.",
         soli=[
             "Paskaties, cik ciparu ir aiz komata.",
             "Viens cipars - pieraksti nulli beigās.",
             "Izlasi skaitli, kas stāv aiz komata.",
             "Pieraksti to ar procentu zīmi.",
             "Pārbaudi: 1 vesels ir 100 %.",
         ],
         pieze="0,3 = 30 %, nevis 3 %. Trīs desmitdaļas ir trīsdesmit "
               "simtdaļas, tāpēc nulle beigās ir obligāta - citādi procenti "
               "iznāk desmitkārt mazāki."),

    Paraugs("Izsaki 0,3 procentos",
            uzd="Cik procentu ir 0,3?",
            soli=[
                ("0,3 ir viens cipars aiz komata",
                 "Desmitdaļas."),
                ("0,3 = 0,30",
                 "Paplašina līdz simtdaļām."),
                ("30 simtdaļas",
                 "Tik ir aiz komata."),
                ("0,3 = 30 %",
                 "Simtdaļu skaits ir procentu skaits."),
            ],
            atbilde="0,3 = 30 %"),

    Ievadi("Izsaki procentos", [
        {"jaut": "0,25 procentos. Ieraksti skaitli bez zīmes.",
         "atb": ["25"], "padoms": "25 simtdaļas."},
        {"jaut": "0,3 procentos. Ieraksti skaitli.",
         "atb": ["30"], "padoms": "0,30."},
        {"jaut": "0,07 procentos. Ieraksti skaitli.",
         "atb": ["7"], "padoms": "7 simtdaļas."},
        {"jaut": "0,5 procentos. Ieraksti skaitli.",
         "atb": ["50"], "padoms": "0,50."},
        {"jaut": "0,99 procentos. Ieraksti skaitli.",
         "atb": ["99"], "padoms": "99 simtdaļas."},
        {"jaut": "1 procentos. Ieraksti skaitli.",
         "atb": ["100"], "padoms": "Viss veselais."},
        {"jaut": "0,8 procentos. Ieraksti skaitli.",
         "atb": ["80"], "padoms": "0,80."},
        {"jaut": "0,04 procentos. Ieraksti skaitli.",
         "atb": ["4"], "padoms": "4 simtdaļas."},
    ], pamats=4,
        ievads="Vispirms divi cipari aiz komata, tikai tad lasi procentus."),

    Zimejums("Viens cipars vai divi",
             restis([["0,3", "0,30", "30 %"],
                     ["0,03", "0,03", "3 %"]],
                    virsraksts="Nulle maina visu"),
             paskaidro="Augšējā rindā nulle nāk klāt beigās un neko nemaina; "
                       "apakšējā tā jau stāv priekšā un padara skaitli "
                       "desmitkārt mazāku.",
             ievads="Vienīgā vieta, kur te var kļūdīties."),

    Varianti("Cik procentu tas ir?", [
        {"jaut": "0,3 procentos ir...",
         "opcijas": ["30 %", "3 %", "0,3 %", "300 %"],
         "pareizi": 0,
         "padoms": "0,30."},
        {"jaut": "0,07 procentos ir...",
         "opcijas": ["7 %", "70 %", "0,7 %", "7,0 %"],
         "pareizi": 0,
         "padoms": "7 simtdaļas."},
        {"jaut": "1 procentos ir...",
         "opcijas": ["100 %", "1 %", "10 %", "1000 %"],
         "pareizi": 0,
         "padoms": "Viss veselais."},
        {"jaut": "Ko dara, ja aiz komata ir viens cipars?",
         "opcijas": ["Pieraksta nulli beigās", "Atmet komatu",
                     "Reizina ar 10", "Neko"],
         "pareizi": 0,
         "padoms": "Vajag simtdaļas."},
        {"jaut": "0,5 procentos ir...",
         "opcijas": ["50 %", "5 %", "0,5 %", "500 %"],
         "pareizi": 0,
         "padoms": "0,50."},
        {"jaut": "Cik simtdaļu ir vienā veselā?",
         "opcijas": ["100", "10", "1000", "1"],
         "pareizi": 0,
         "padoms": "Tāpēc vesels ir 100 %."},
    ], pamats=4),

    Pasaule("Ko rāda akcijas uzlīme?",
            Ievadi("", [
                {"jaut": "Uzlīmē rakstīts «maksā 0,75 no cenas». Cik "
                         "procentu no cenas jāmaksā?",
                 "atb": ["75"], "padoms": "75 simtdaļas."},
                {"jaut": "Cik procentu ir atlaide?",
                 "atb": ["25"], "padoms": "100 - 75."},
                {"jaut": "Citur rakstīts «maksā 0,9 no cenas». Cik procentu "
                         "jāmaksā?",
                 "atb": ["90"], "padoms": "0,90."},
                {"jaut": "Cik procentu ir šī atlaide?",
                 "atb": ["10"], "padoms": "100 - 90."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmā raksta gan procentus, gan skaitļus ar komatu, "
                      "un abi nozīmē vienu.",
            kapec="Procentos atlaidi ir vieglāk salīdzināt."),

    Kopsavilkums([
        "Izsaku decimāldaļu līdz simtdaļām procentos.",
        "Paplašinu vienu ciparu aiz komata līdz diviem.",
        "Zinu, ka 1 vesels ir 100 %.",
        "Neapjūku starp 0,3 un 0,03.",
    ]),

    Majas([
        "Izsaki procentos 0,45; 0,6; 0,08 un 0,95.",
        "Pieraksti ar komatu 35 %, 4 % un 70 %.",
        "Atrodi reklāmu, kurā atlaide rakstīta ar komatu.",
    ]),
]
