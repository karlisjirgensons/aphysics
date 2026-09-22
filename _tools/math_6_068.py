# -*- coding: utf-8 -*-
"""6. klase, 68. stunda: «Cik daudz papīra vajag dāvanai?»

Praktiska stunda, kurā parādās tā grūtība, ko formulas uzdevumos nav:
izmēri ir dažādās mērvienībās, un tos vispirms jāizlīdzina. Papīra patēriņš
turklāt nekad nav tieši virsmas laukums - vajag rezervi locījumiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Cik daudz papīra vajag dāvanai?"

MERKIS = ("Lietosim virsmas laukuma aprēķinu praktiskā situācijā, vienādojot "
          "mērvienības.")

SATURS = [
    Sakums("Papīra vienmēr vajag mazliet vairāk",
           fakti=["Virsmas laukums pasaka minimumu, ne patēriņu.",
                  "Locījumiem un pārlaidumam pieskaita apmēram desmito daļu.",
                  "Ja izmēri doti dažādās mērvienībās, tos vispirms "
                  "izlīdzina."]),

    Doma("Vispirms mērvienības, tad laukums, tad rezerve",
         "Praktiskā uzdevumā vispirms visus izmērus pārveido vienā "
         "mērvienībā, tad rēķina virsmas laukumu un tikai beigās pieskaita "
         "rezervi.",
         soli=[
             "Pieraksti visus izmērus un to mērvienības.",
             "Pārveido tos vienā mērvienībā.",
             "Aprēķini virsmas laukumu.",
             "Pieskaiti rezervi locījumiem, ja uzdevums to prasa.",
             "Pieraksti atbildi ar mērvienību.",
         ],
         pieze="30 cm un 0,2 m nav salīdzināmi, kamēr abus nepieraksta "
               "vienādi: 30 cm un 20 cm. Šis solis ir biežākā kļūdas vieta "
               "visā tematā."),

    Paraugs("Iesaiņo dāvanu",
            uzd="Kaste ir 30 cm gara, 0,2 m plata un 100 mm augsta. Cik cm² "
                "papīra vajag bez rezerves?",
            soli=[
                ("0,2 m = 20 cm; 100 mm = 10 cm",
                 "Visus izmērus centimetros."),
                ("Augša un apakša: 30 · 20 = 600 cm²",
                 "Garums reiz platums."),
                ("Priekša un aizmugure: 30 · 10 = 300 cm²",
                 "Garums reiz augstums."),
                ("Sāni: 20 · 10 = 200 cm²",
                 "Platums reiz augstums."),
                ("2 · (600 + 300 + 200) = 2200 cm²",
                 "Virsmas laukums."),
            ],
            atbilde="2200 cm²"),

    Ievadi("Izlīdzini un izrēķini", [
        {"jaut": "Cik cm ir 0,2 m?",
         "atb": ["20"], "padoms": "0,2 · 100."},
        {"jaut": "Cik cm ir 100 mm?",
         "atb": ["10"], "padoms": "100 : 10."},
        {"jaut": "Kaste 30 x 20 x 10 cm. Cik cm² ir virsmas laukums?",
         "atb": ["2200"], "padoms": "2 · (600 + 300 + 200)."},
        {"jaut": "Cik cm² papīra vajag ar 10 % rezervi? Noapaļo līdz "
                 "veselam.",
         "atb": ["2420"], "padoms": "2200 + 220."},
        {"jaut": "Kaste 0,5 m x 40 cm x 200 mm. Cik cm ir garums?",
         "atb": ["50"], "padoms": "0,5 · 100."},
        {"jaut": "Tā pati kaste. Cik cm² ir virsmas laukums?",
         "atb": ["7600"], "padoms": "2 · (2000 + 1000 + 800)."},
    ], pamats=4),

    Pasaule("Cik papīra sanāks no ruļļa?",
            Kustiba("", [
                {"jaut": "Kaste 30 x 20 x 10 cm. Cik cm² ir virsmas "
                         "laukums?",
                 "atb": 2200, "beigas": 10000, "iedala": 2000,
                 "mers": "kvadrātcentimetri", "merkis": "vajag",
                 "objekts": "Papīrs",
                 "padoms": "2 · (600 + 300 + 200)."},
                {"jaut": "Kaste 40 x 30 x 20 cm. Cik cm² ir virsmas "
                         "laukums?",
                 "atb": 5200, "beigas": 10000, "iedala": 2000,
                 "mers": "kvadrātcentimetri", "merkis": "vajag",
                 "objekts": "Papīrs",
                 "padoms": "2 · (1200 + 800 + 600)."},
                {"jaut": "Kubs ar šķautni 25 cm. Cik cm² ir virsmas "
                         "laukums?",
                 "atb": 3750, "beigas": 10000, "iedala": 2000,
                 "mers": "kvadrātcentimetri", "merkis": "vajag",
                 "objekts": "Papīrs",
                 "padoms": "6 · 625."},
                {"jaut": "Kaste 0,5 m x 0,4 m x 0,2 m. Cik cm² ir virsmas "
                         "laukums?",
                 "atb": 7600, "beigas": 10000, "iedala": 2000,
                 "mers": "kvadrātcentimetri", "merkis": "vajag",
                 "objekts": "Papīrs",
                 "padoms": "Vispirms centimetros: 50, 40 un 20."},
            ]),
            pavediens="veikals",
            konteksts="Rullī ir noteikts papīra daudzums - jāzina, vai tas "
                      "nosegs visu kasti.",
            kapec="Mērvienību izlīdzināšana ir pirmais solis, ne pēdējais."),

    Varianti("Kur slēpjas kļūda?", [
        {"jaut": "Skolēns rēķina ar 30 cm, 0,2 m un 100 mm, tos "
                 "nepārveidojot. Kas notiks?",
         "opcijas": ["Atbilde būs pilnīgi greiza",
                     "Atbilde būs tikai mazliet greiza",
                     "Nekas nenotiks", "Atbilde būs pareiza"],
         "pareizi": 0,
         "padoms": "Skaitļi ir dažādās vienībās."},
        {"jaut": "Cik cm² ir 1 m²?",
         "opcijas": ["10 000", "100", "1000", "10"],
         "pareizi": 0,
         "padoms": "100 · 100."},
        {"jaut": "Kāpēc papīra vajag vairāk nekā virsmas laukums?",
         "opcijas": ["Locījumiem un pārlaidumam",
                     "Jo papīrs ir plāns",
                     "Jo kaste ir liela", "Nevajag vairāk"],
         "pareizi": 0,
         "padoms": "Malas jāpārloka."},
        {"jaut": "Kaste 20 x 20 x 20 cm. Cik cm² ir virsma?",
         "opcijas": ["2400", "8000", "400", "1200"],
         "pareizi": 0,
         "padoms": "6 · 400."},
    ], pamats=4),

    Kopsavilkums([
        "Pārveidoju visus izmērus vienā mērvienībā pirms rēķina.",
        "Aprēķinu virsmas laukumu praktiskā situācijā.",
        "Pieskaitu rezervi, ja uzdevums to prasa.",
        "Pierakstu atbildi ar pareizo mērvienību.",
    ]),

    Majas([
        "Izmēri kādu mājas kasti trijos izmēros un aprēķini papīra "
        "patēriņu.",
        "Pieskaiti 10 % rezervi un pieraksti gala skaitli.",
        "Pieraksti, kurā mērvienībā strādāji un kāpēc.",
    ]),
]
