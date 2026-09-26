# -*- coding: utf-8 -*-
"""4. klase, 91. stunda: «Vai uzdevumam ir viena atbilde?»

4.4. temata pēdējā stunda pirms PD. Atvērta problēma: dažiem uzdevumiem
ir vairākas pareizas atbildes (kā sadalīt 60 skolēnus vienādās grupās?),
un svarīgi ir atrast visas un pamatot izvēli. Tā ir dalītāju meklēšana -
5. klases tēma, bet dzīves valodā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Vai uzdevumam ir viena atbilde?"

MERKIS = ("Risināsim atvērtu problēmu ar vairākiem iespējamiem "
          "risinājumiem un pamatosim savu izvēli.")

SATURS = [
    Sakums("Kā sadalīt 24 skolēnus vienādās komandās?",
           zimejums=restis([["komandas", "skolēni komandā"],
                            [2, 12], [3, 8], [4, 6], [6, 4], [8, 3]],
                           "vairākas pareizas atbildes"),
           paraksts="Visi varianti pareizi - bet kurš labākais spēlei?",
           fakti=["Dažiem uzdevumiem ir vairākas atbildes.",
                  "Tad jāatrod visas un jāizvēlas labākā."]),

    Doma("Atrodi visas atbildes, tad izvēlies",
         "Atvērtā uzdevumā sistemātiski uzskaiti visus variantus un "
         "pamato, kurš der vislabāk.",
         soli=[
             "Uzskaiti variantus pēc kārtas (1, 2, 3, ...).",
             "Pārbaudi katru: vai tas der?",
             "Izveido tabulu - tā neviens nepazūd.",
             "Izvēlies labāko un pasaki, kāpēc.",
         ],
         pieze="Basketbolam der komandas pa 6 (5 laukumā un 1 rezervē) - tad "
               "no 24 sanāk 4 komandas."),

    Paraugs("Vairāki veidi samaksāt",
            uzd="Kā samaksāt 50 € ar 10 € un 20 € banknotēm?",
            soli=[
                ("20 + 20 + 10 = 50", "Divas 20 un viena 10."),
                ("20 + 10 + 10 + 10 = 50", "Viena 20 un trīs 10."),
                ("10 + 10 + 10 + 10 + 10 = 50", "Piecas 10."),
            ],
            atbilde="3 veidi"),

    Ievadi("Cik variantu?", [
        {"jaut": "Cik veidos 24 skolēnus sadalīt vienādās komandās (vismaz 2 "
                 "komandas, vismaz 2 skolēni)?", "atb": ["6"],
         "padoms": "2, 3, 4, 6, 8, 12 komandas."},
        {"jaut": "Cik veidos 36 krēslus salikt vienādās rindās pa vismaz 2 "
                 "(un vismaz 2 rindās)?", "atb": ["7"],
         "padoms": "2, 3, 4, 6, 9, 12, 18 rindas."},
        {"jaut": "Taisnstūris ar laukumu 12 rūtiņas - cik dažādu malu pāru "
                 "(1 × 12 un 12 × 1 skaita kā vienu)?", "atb": ["3"],
         "padoms": "1 × 12, 2 × 6, 3 × 4."},
        {"jaut": "Cik veidos samaksāt 30 € ar 5 € un 10 € banknotēm?",
         "atb": ["4"], "padoms": "0, 1, 2 vai 3 desmitnieki."},
    ]),

    Varianti("Kura atbilde labākā?", [
        {"jaut": "60 skolēni ekskursijā, autobusos pa 20, 30 vai 60 vietām. "
                 "Ja visi autobusi maksā vienādi, kuru ņemt?",
         "opcijas": ["vienu 60 vietu", "trīs pa 20", "divus pa 30"],
         "pareizi": 0, "padoms": "Mazāk autobusu - lētāk."},
        {"jaut": "Futbola komandā laukumā 11. Cik pilnu komandu no 24?",
         "opcijas": ["2", "3", "1", "11"], "pareizi": 0,
         "padoms": "24 : 11 = 2 (atl. 2)."},
        {"jaut": "Vai uzdevumam «uzraksti 10 kā summu» ir viena atbilde?",
         "opcijas": ["nē, daudz", "jā", "divas"], "pareizi": 0,
         "padoms": "5 + 5, 3 + 7, 1 + 9, ..."},
    ]),

    Pasaule("Sporta dienas plānošana",
            Ievadi("", [
                {"jaut": "48 skolēni, komandās pa vienādi. Ja komandā 6, cik "
                         "komandu?",
                 "atb": ["8"], "padoms": "48 : 6."},
                {"jaut": "Ja komandā 8, cik komandu?", "atb": ["6"],
                 "padoms": "48 : 8."},
                {"jaut": "Turnīrā katra komanda spēlē ar katru. Cik spēļu, ja "
                         "komandu 4?",
                 "atb": ["6"], "padoms": "3 + 2 + 1 - kā leņķi 61. stundā."},
                {"jaut": "Cik spēļu, ja komandu 6?", "atb": ["15"],
                 "padoms": "5 + 4 + 3 + 2 + 1."},
            ]),
            pavediens="sports",
            konteksts="Organizators izvēlas komandu skaitu tā, lai turnīrs "
                      "nav par garu - 6 komandas nozīmē 15 spēles.",
            kapec="Vairākas atbildes nozīmē izvēli - un izvēle jāpamato."),

    Kopsavilkums([
        "Zinu, ka uzdevumam var būt vairākas atbildes.",
        "Uzskaitu visus variantus sistemātiski.",
        "Izvēlos labāko un pamatoju.",
        "Esmu gatavs 4.4. temata pārbaudes darbam.",
    ]),

    Majas([
        "Atrodi visus veidus, kā samaksāt 1 € ar 20 ct un 50 ct monētām.",
        "Atrodi, cik dažādos taisnstūros var salikt 24 flīzes.",
        "Atkārto: stabiņš, stūrītis ar divciparu dalītāju, novērtējums.",
    ], ievads="Nākamajā stundā - pārbaudes darbs par 4.4. tematu."),
]
