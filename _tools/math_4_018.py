# -*- coding: utf-8 -*-
"""4. klase, 18. stunda: «Ko stāsta infogramma?»

Infogramma ir skaitļi, kas pārvērsti attēlā. Stabiņu diagrammu var
organizēt dažādi - stateniski, guļus, ar mērogu, kurā viena iedaļa ir 100
vai 1000. Stunda māca vispirms izlasīt virsrakstu un mērogu, un tikai tad
skaitļus - tieši to prasa eksāmena datu uzdevumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Ko stāsta infogramma?"

MERKIS = ("Nolasīsim datus no infogrammām un dažādi organizētām stabiņu "
          "diagrammām un salīdzināsim tos.")

SATURS = [
    Sakums("Kurš dzīvnieks dzīvo visilgāk?",
           zimejums=kolonnas([("suns", 13), ("zirgs", 30), ("zilonis", 70),
                              ("bruņurupucis", 150)], " g."),
           paraksts="Vidējais mūža ilgums gados.",
           fakti=["Bruņurupuči var nodzīvot vairāk nekā 150 gadus.",
                  "Infogramma to parāda vienā mirklī - bez tabulas."]),

    Doma("Vispirms virsraksts un mērogs, tad skaitļi",
         "Diagrammu lasa trīs soļos: par ko tā ir, ko nozīmē iedaļa, un tikai "
         "tad - cik ir katrā stabiņā.",
         soli=[
             "Izlasi virsrakstu: par ko ir dati?",
             "Atrodi mērvienību un mērogu: vai iedaļa ir 1, 10 vai 1000?",
             "Nolasi katra stabiņa vērtību.",
             "Salīdzini: kurš lielākais, kurš mazākais, par cik atšķiras?",
         ],
         pieze="Ja stabiņš beidzas starp iedaļām, vērtību novērtē - tāpat "
               "kā uz skaitļu taisnes."),

    Zimejums("Latvijas upju garums",
             kolonnas([("Gauja", 452), ("Venta", 178), ("Daugava", 352),
                       ("Lielupe", 119)], " km"),
             paskaidro="Daugava kopumā ir 1020 km, bet Latvijā tecē tikai "
                       "352 km no tās.",
             ievads="Garums Latvijas teritorijā kilometros."),

    Paraugs("Par cik Gauja garāka nekā Venta?",
            uzd="No diagrammas: Gauja 452 km, Venta 178 km. Par cik Gauja ir "
                "garāka?",
            soli=[
                ("452 − 178", "«Par cik» - atņemšana."),
                ("452 − 178 = 274", None),
            ],
            atbilde="par 274 km"),

    Ievadi("Nolasi un salīdzini", [
        {"jaut": "Kura upe diagrammā ir visgarākā Latvijā? Ieraksti tās "
                 "garumu km.", "atb": ["452"], "padoms": "Augstākais "
                 "stabiņš."},
        {"jaut": "Par cik Daugava Latvijā ir garāka nekā Venta?",
         "atb": ["174"], "padoms": "352 − 178."},
        {"jaut": "Cik km ir visu četru upju garumu summa?",
         "atb": ["1101"], "padoms": "452 + 178 + 352 + 119."},
        {"jaut": "Par cik bruņurupucis dzīvo ilgāk nekā zilonis (gados)?",
         "atb": ["80"], "padoms": "150 − 70."},
    ]),

    Varianti("Kas nav no diagrammas?", [
        {"jaut": "Ko var uzzināt no upju diagrammas?",
         "opcijas": ["kura upe Latvijā ir garākā", "kura upe ir dziļākā",
                     "kurā upē ir vairāk zivju", "kura upe ir tīrākā"],
         "pareizi": 0, "padoms": "Diagrammā ir tikai garums."},
        {"jaut": "Ko nozīmē «km» pie skaitļiem?",
         "opcijas": ["garums kilometros", "cik upju", "gadi", "platums"],
         "pareizi": 0, "padoms": "Mērvienība."},
        {"jaut": "Kāpēc Lielupes stabiņš ir zemākais?",
         "opcijas": ["tā ir īsākā no četrām", "tā ir šaurākā",
                     "tā ir seklākā", "tā ir jaunākā"],
         "pareizi": 0, "padoms": "Stabiņa augstums ir garums."},
        {"jaut": "Cik reižu apmēram Gauja garāka par Lielupi?",
         "opcijas": ["apmēram 4 reizes", "2 reizes", "10 reizes",
                     "vienādas"], "pareizi": 0,
         "padoms": "450 : 120 ≈ 4."},
    ], pamats=4),

    Pasaule("Cik ātri skrien dzīvnieki?",
            Ievadi("", [
                {"jaut": "Gepards skrien 110 km/h, zirgs 70 km/h. Par cik "
                         "km/h gepards ātrāks?",
                 "atb": ["40"], "padoms": "110 − 70."},
                {"jaut": "Strauss skrien 70 km/h, cilvēks rekordā 44 km/h. "
                         "Par cik strauss ātrāks?",
                 "atb": ["26"], "padoms": "70 − 44."},
                {"jaut": "Kuram ir vienāds ātrums ar zirgu - gepardam vai "
                         "strausam? Raksti vārdu.",
                 "atb": ["strausam", "strauss"], "tastatura": "text",
                 "padoms": "Abiem 70 km/h."},
                {"jaut": "Cik km/h ir geparda un cilvēka ātrumu starpība?",
                 "atb": ["66"], "padoms": "110 − 44."},
            ]),
            pavediens="daba",
            zimejums=kolonnas([("gepards", 110), ("zirgs", 70),
                               ("strauss", 70), ("cilvēks", 44)], ""),
            konteksts="Maksimālais ātrums km/h. Dabas filmās infogrammas "
                      "parāda rekordus vienā bildē.",
            kapec="Infogrammu izlasa ātrāk nekā tabulu - ja zina, kā."),

    Kopsavilkums([
        "Izlasu diagrammas virsrakstu un mērvienību.",
        "Nolasu stabiņu vērtības.",
        "Salīdzinu vērtības, izmantojot atņemšanu.",
        "Pasaku, ko diagramma *nestāsta*.",
    ]),

    Majas([
        "Atrodi avīzē, žurnālā vai internetā infogrammu un pastāsti, ko tā "
        "rāda.",
        "Izdomā vienu jautājumu, uz kuru var atbildēt ar upju diagrammu.",
        "Pajautā mājiniekiem, cik gadu dzīvo jūsu mājdzīvnieks, un salīdzini "
        "ar diagrammu.",
    ]),
]
