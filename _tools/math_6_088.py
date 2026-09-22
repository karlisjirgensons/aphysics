# -*- coding: utf-8 -*-
"""6. klase, 88. stunda: «Ko stāsta produkta sastāvs?»

Procenti kļūst par rīku, ar ko lasīt etiķeti. Uzdevumi te nāk no īstiem
iepakojumiem, un atbilde nav tikai skaitlis - tā ir arī izvēle starp diviem
produktiem, kas jāpamato.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Ko stāsta produkta sastāvs?"

MERKIS = ("Ar procentiem raksturosim pārtikas sastāvu un salīdzināsim to ar "
          "ieteikumiem.")

SATURS = [
    Sakums("Uz etiķetes viss ir procentos",
           zimejums=kolonnas([("sula A", 50), ("sula B", 25),
                              ("sula C", 100)], " %"),
           paraksts="Trīs dzērieni: pirmajā puse augļu, otrajā ceturtdaļa, "
                    "trešajā tikai augļi.",
           fakti=["Sastāvdaļas raksta dilstošā secībā pēc daudzuma.",
                  "Procenti pasaka, cik no kopējās masas ir katra viela.",
                  "Visu sastāvdaļu procenti kopā ir 100 %."]),

    Doma("Procenti no masas, ne no tilpuma",
         "Produkta sastāvā procenti rāda, cik lielu daļu no kopējās masas "
         "veido katra viela; visu sastāvdaļu summa ir 100 %.",
         soli=[
             "Pieraksti produkta kopējo masu.",
             "Atrodi, cik procentu ir meklētā viela.",
             "Aprēķini 1 % no masas.",
             "Reizini ar procentu skaitu.",
             "Pārbaudi: vai atbilde ir mazāka par kopējo masu?",
         ],
         pieze="Ja etiķetē ir «100 g produkta satur 12 g cukura», tad cukurs "
               "ir 12 % - te procentus pat nav jārēķina, jo kopums jau ir "
               "simts."),

    Paraugs("Cik cukura ir pudelē?",
            uzd="Dzēriena pudelē ir 500 g, cukurs ir 8 % no masas. Cik gramu "
                "cukura tajā ir?",
            soli=[
                ("1 % no 500 ir 5 g",
                 "500 : 100."),
                ("8 · 5 = 40 g",
                 "Astoņas simtdaļas."),
                ("Dienas ieteicamais daudzums ir ap 50 g",
                 "Salīdzinājumam."),
                ("40 g ir 80 % no ieteicamā",
                 "Gandrīz visa dienas norma vienā pudelē."),
            ],
            atbilde="40 g cukura"),

    Ievadi("Izlasi etiķeti", [
        {"jaut": "Pudelē 500 g, cukurs 8 %. Cik gramu cukura?",
         "atb": ["40"], "padoms": "8 · 5."},
        {"jaut": "Jogurtā 200 g, tauki 2,5 %. Cik gramu tauku?",
         "atb": ["5"], "padoms": "2,5 · 2."},
        {"jaut": "Maizē 400 g, rudzu milti 60 %. Cik gramu miltu?",
         "atb": ["240"], "padoms": "60 · 4."},
        {"jaut": "Sulā 1000 g, augļi 25 %. Cik gramu augļu?",
         "atb": ["250"], "padoms": "25 · 10."},
        {"jaut": "Produktā 250 g, sāls 1,2 %. Cik gramu sāls?",
         "atb": ["3"], "padoms": "1 % ir 2,5 g."},
        {"jaut": "100 g produkta satur 12 g cukura. Cik procenti tas ir?",
         "atb": ["12"], "padoms": "Kopums jau ir simts."},
    ], pamats=4),

    Petijums("Salīdzini divus produktus",
             vajag="divi pārtikas iepakojumi ar sastāvu",
             soli=[
                 "Pieraksti abu produktu masu un cukura procentus.",
                 "Aprēķini cukura daudzumu gramos katrā.",
                 "Salīdzini ar ieteicamo dienas daudzumu.",
                 "Pieraksti, kurš produkts ir izdevīgāks un kāpēc.",
             ],
             secinajums="Lielāks procents ne vienmēr nozīmē vairāk gramu - "
                        "izšķir arī iepakojuma masa."),

    Varianti("Ko pasaka procenti?", [
        {"jaut": "Visu sastāvdaļu procenti kopā ir...",
         "opcijas": ["100 %", "50 %", "atkarīgs no produkta", "1000 %"],
         "pareizi": 0,
         "padoms": "Kopums vienmēr ir viss produkts."},
        {"jaut": "Produktā A 10 % cukura pie 100 g, produktā B 5 % pie "
                 "400 g. Kurā ir vairāk cukura?",
         "opcijas": ["B: 20 g pret 10 g", "A: 10 % ir vairāk",
                     "Vienādi", "Nevar salīdzināt"],
         "pareizi": 0,
         "padoms": "Izšķir arī masa."},
        {"jaut": "Kāda secībā raksta sastāvdaļas?",
         "opcijas": ["Dilstoši pēc daudzuma", "Alfabēta secībā",
                     "Augoši pēc daudzuma", "Nejauši"],
         "pareizi": 0,
         "padoms": "Pirmā ir tā, kuras ir visvairāk."},
        {"jaut": "Ja etiķetē ir «100 g satur 12 g cukura», cukurs ir...",
         "opcijas": ["12 %", "1,2 %", "120 %", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Kopums ir 100 g."},
    ], pamats=4),

    Pasaule("Kurš dzēriens ir labāks?",
            Ievadi("", [
                {"jaut": "Dzēriens A: 330 ml, cukurs 10 %. Cik gramu cukura?",
                 "atb": ["33"], "padoms": "1 % ir 3,3."},
                {"jaut": "Dzēriens B: 500 ml, cukurs 6 %. Cik gramu cukura?",
                 "atb": ["30"], "padoms": "1 % ir 5."},
                {"jaut": "Cik gramu cukura ir abos kopā?",
                 "atb": ["63"], "padoms": "33 + 30."},
                {"jaut": "Ieteicamais dienas daudzums ir 50 g. Par cik "
                         "gramiem tas ir pārsniegts?",
                 "atb": ["13"], "padoms": "63 − 50."},
            ]),
            pavediens="virtuve",
            konteksts="Divi dzērieni var izskatīties vienādi, bet cukura "
                      "daudzums tajos atšķiras.",
            kapec="Procenti kopā ar masu pasaka, cik tiešām apēd."),

    Kopsavilkums([
        "Lasu produkta sastāvu un saprotu, ko nozīmē procenti.",
        "Aprēķinu vielas daudzumu gramos no procentiem un masas.",
        "Salīdzinu divus produktus, ņemot vērā arī masu.",
        "Salīdzinu rezultātu ar ieteicamo daudzumu.",
    ]),

    Majas([
        "Izlasi trīs mājās esošu produktu sastāvu un pieraksti cukura "
        "procentus.",
        "Aprēķini, cik gramu cukura ir katrā iepakojumā.",
        "Pieraksti, kurš produkts tev būtu jāizvēlas un kāpēc.",
    ]),
]
