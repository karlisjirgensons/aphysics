# -*- coding: utf-8 -*-
"""5. klase, 136. stunda: «Kurš skaitlis ir lielāks?»

Mikrotemata noslēgums. Salīdzināšana pati par sevi ir vienkārša, bet te
sanāk visas iepriekšējās stundas kopā: šķiras, paplašināšana un taisne.
Biežākā kļūda ir salīdzināt aiz komata kā veselus skaitļus - tad 0,45 iznāk
lielāks par 0,5. Tieši to stunda arī novērš.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis, taisne)

TEMA = "Kurš skaitlis ir lielāks?"

MERKIS = ("Iemācīsimies salīdzināt decimāldaļas līdz tūkstošdaļām un "
          "skaidrot, kā sprieda.")

SATURS = [
    Sakums("0,45 vai 0,5?",
           zimejums=taisne(0.4, 0.6, 0.05, [(0.45, "0,45"), (0.5, "0,5")],
                           virsraksts="Kurš punkts ir pa labi"),
           paraksts="0,5 = 0,50, tāpēc tas ir lielāks par 0,45.",
           fakti=["45 ir lielāks par 5, bet 0,45 nav lielāks par 0,5.",
                  "Aiz komata salīdzina pa šķirām, ne kā veselus skaitļus.",
                  "Drošākais ceļš - izlīdzināt ciparu skaitu."]),

    Doma("Salīdzina pa šķirām",
         "Decimāldaļas salīdzina, vispirms salīdzinot veselās daļas, tad "
         "desmitdaļas, tad simtdaļas un tūkstošdaļas.",
         soli=[
             "Salīdzini veselās daļas - ja tās atšķiras, atbilde ir gatava.",
             "Ja vienādas, salīdzini desmitdaļas.",
             "Tad simtdaļas, tad tūkstošdaļas.",
             "Vai arī izlīdzini ciparu skaitu ar nullēm un salīdzini uzreiz.",
             "Pieraksti atbildi ar zīmi < vai >.",
         ],
         pieze="Abi ceļi ir droši. Salīdzināšana pa šķirām ir ātrāka, "
               "nullēm izlīdzinātais pieraksts - drošāks. Bīstams ir tikai "
               "trešais ceļš: salīdzināt ciparus aiz komata kā veselu "
               "skaitli."),

    Paraugs("Salīdzini 0,45 un 0,5",
            uzd="Kurš skaitlis ir lielāks?",
            soli=[
                ("Veselās daļas abiem ir 0",
                 "Ar tām neizšķiras."),
                ("Desmitdaļas: 4 un 5",
                 "Pirmais cipars aiz komata."),
                ("4 < 5",
                 "Tālāk salīdzināt nevajag."),
                ("0,45 < 0,5",
                 "Vai arī: 0,45 < 0,50."),
            ],
            atbilde="Lielāks ir 0,5"),

    Ievadi("Kurš skaitlis lielāks?", [
        {"jaut": "0,45 vai 0,5? Ieraksti lielāko.",
         "atb": ["0,5", "0,50"], "padoms": "Desmitdaļas 4 un 5."},
        {"jaut": "0,8 vai 0,79? Ieraksti lielāko.",
         "atb": ["0,8", "0,80"], "padoms": "0,80 pret 0,79."},
        {"jaut": "1,2 vai 1,19? Ieraksti lielāko.",
         "atb": ["1,2", "1,20"], "padoms": "1,20 pret 1,19."},
        {"jaut": "0,305 vai 0,31? Ieraksti lielāko.",
         "atb": ["0,31", "0,310"], "padoms": "0,310 pret 0,305."},
        {"jaut": "2,5 vai 2,49? Ieraksti lielāko.",
         "atb": ["2,5", "2,50"], "padoms": "2,50 pret 2,49."},
        {"jaut": "0,07 vai 0,7? Ieraksti lielāko.",
         "atb": ["0,7", "0,70"], "padoms": "Desmitdaļas pret simtdaļām."},
        {"jaut": "3,14 vai 3,2? Ieraksti lielāko.",
         "atb": ["3,2", "3,20"], "padoms": "Desmitdaļas 1 un 2."},
        {"jaut": "0,999 vai 1? Ieraksti lielāko.",
         "atb": ["1"], "padoms": "Veselās daļas 0 un 1."},
    ], pamats=4,
        ievads="Sāc ar veselajām daļām un ej pa šķirām uz labo pusi."),

    Zimejums("Šķira pēc šķiras",
             restis([["0,45", "0,50"],
                     ["0,79", "0,80"]],
                    virsraksts="Pa labi - lielākais"),
             paskaidro="Abās rindās skaitļi ir izlīdzināti ar nullēm, tāpēc "
                       "tos var salīdzināt kā parastus ciparu virknes.",
             ievads="Izlīdzināts pieraksts padara salīdzināšanu vienkāršu."),

    Varianti("Kā salīdzina decimāldaļas?", [
        {"jaut": "Ko salīdzina vispirms?",
         "opcijas": ["Veselās daļas", "Ciparus aiz komata",
                     "Ciparu skaitu", "Komatu"],
         "pareizi": 0,
         "padoms": "Lielākā šķira izšķir."},
        {"jaut": "0,45 un 0,5 - kurš lielāks?",
         "opcijas": ["0,5", "0,45", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Desmitdaļas 4 un 5."},
        {"jaut": "Kāpēc 0,45 nav lielāks par 0,5?",
         "opcijas": ["Aiz komata salīdzina pa šķirām",
                     "45 ir mazāks par 5",
                     "Tur ir vairāk ciparu",
                     "Tas ir lielāks"],
         "pareizi": 0,
         "padoms": "4 desmitdaļas pret 5."},
        {"jaut": "0,305 un 0,31 - kurš lielāks?",
         "opcijas": ["0,31", "0,305", "Vienādi", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "0,310 pret 0,305."},
        {"jaut": "Kurš no tiem ir vislielākais?",
         "opcijas": ["0,9", "0,89", "0,891", "0,099"],
         "pareizi": 0,
         "padoms": "Desmitdaļas."},
        {"jaut": "Kāds ir drošākais paņēmiens?",
         "opcijas": ["Izlīdzināt ciparu skaitu ar nullēm",
                     "Salīdzināt ciparus aiz komata kā skaitli",
                     "Skaitīt ciparus",
                     "Noņemt komatu"],
         "pareizi": 0,
         "padoms": "Tad šķiras sakrīt."},
    ], pamats=4),

    Pasaule("Kura prece ir lētāka?",
            Ievadi("", [
                {"jaut": "0,45 € vai 0,5 €? Ieraksti lētāko.",
                 "atb": ["0,45"], "padoms": "0,45 pret 0,50."},
                {"jaut": "1,2 € vai 1,19 €? Ieraksti lētāko.",
                 "atb": ["1,19"], "padoms": "1,20 pret 1,19."},
                {"jaut": "2,05 € vai 2,5 €? Ieraksti lētāko.",
                 "atb": ["2,05"], "padoms": "Desmitdaļas 0 un 5."},
                {"jaut": "0,99 € vai 1 €? Ieraksti lētāko.",
                 "atb": ["0,99"], "padoms": "Veselās daļas 0 un 1."},
            ]),
            pavediens="veikals",
            konteksts="Plauktā cenas atšķiras par centiem, un tieši tur "
                      "visvieglāk kļūdīties.",
            kapec="Salīdzināt pa šķirām nozīmē salīdzināt centus ar centiem."),

    Kopsavilkums([
        "Salīdzinu decimāldaļas pa šķirām.",
        "Izlīdzinu ciparu skaitu ar nullēm, ja tā ir drošāk.",
        "Skaidroju, kā sprieda, nevis tikai nosaucu atbildi.",
        "Zinu, ka ciparus aiz komata nedrīkst lasīt kā veselu skaitli.",
    ]),

    Majas([
        "Sakārto augošā secībā 0,7; 0,07; 0,77 un 0,707.",
        "Salīdzini 4,5 un 4,49; 0,301 un 0,3.",
        "Atrodi veikalā divas cenas, kuras atšķiras par vienu centu.",
    ]),
]
