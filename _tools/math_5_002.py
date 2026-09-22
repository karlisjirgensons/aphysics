# -*- coding: utf-8 -*-
"""5. klase, 2. stunda: «Kā skaitli uzrakstīt kā šķiru summu?»

Turpina 1. stundu: ja cipara vērtību nosaka tā vieta, tad skaitli var
izjaukt pa vietām un salikt atpakaļ. Šķiru summa vēlāk noder noapaļošanā un
rakstiskajos aprēķinos, tāpēc te to pieraksta uzmanīgi - arī tad, kad vidū
ir nulle.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Kā skaitli uzrakstīt kā šķiru summu?"

MERKIS = ("Iemācīsimies skaitli izjaukt pa šķirām un atkal salikt kopā, kā "
          "arī nosaukt skaitļa kaimiņus.")

SATURS = [
    Sakums("Kā samaksāt 4 320 eiro ar banknotēm?",
           zimejums=kolonnas([("pa 1000", 4), ("pa 100", 3), ("pa 10", 2),
                              ("pa 1", 0)]),
           paraksts="4 320 = 4 000 + 300 + 20. Vienu banknošu nevajag.",
           fakti=["Katra šķira ir viena banknošu kaudzīte."]),

    Doma("Katra šķira dod savu gabalu",
         "Skaitlis ir savu šķiru summa - un neviens gabals nedrīkst pazust.",
         soli=[
             "Paskaties, kurā vietā stāv katrs cipars.",
             "Uzraksti katra cipara vērtību atsevišķi: 4 000, 300, 20.",
             "Saliec tās ar plusiem - sanāk pats skaitlis.",
             "Ja ciparā ir nulle, tā šķira summā neparādās.",
         ],
         pieze="Kaimiņi ir skaitļi, kas stāv blakus: pirms 4 320 ir 4 319, "
               "aiz tā - 4 321."),

    Paraugs("Kā izjaukt 60 704?",
            uzd="Uzraksti 60 704 kā šķiru summu un nosauc tā kaimiņus.",
            soli=[
                ("60 704 → 6 desmiti tūkstošu, 0 tūkstoši, 7 simti, "
                 "0 desmiti, 4 vieni",
                 "Vispirms nosauc katra cipara vietu."),
                ("60 704 = 60 000 + 700 + 4",
                 "Nulles šķiras summā neraksta - tur nav ko pielikt."),
                ("60 703 un 60 705",
                 "Kaimiņi ir par vienu mazāk un par vienu vairāk."),
            ],
            atbilde="60 704 = 60 000 + 700 + 4; kaimiņi 60 703 un 60 705"),

    Ievadi("Uzraksti šķiru summu", [
        {"jaut": "2 500 = ?", "atb": ["2000+500", "2 000 + 500"],
         "padoms": "Divas šķiras: tūkstoši un simti.",
         "vieta": "2000+500"},
        {"jaut": "7 043 = ?", "atb": ["7000+40+3", "7 000 + 40 + 3"],
         "padoms": "Simtu šķirā ir nulle - to summā neraksta.",
         "vieta": "7000+40+3"},
        {"jaut": "310 000 = ?", "atb": ["300000+10000", "300 000 + 10 000"],
         "padoms": "Tikai divas šķiras nav tukšas."},
        {"jaut": "9 090 = ?", "atb": ["9000+90", "9 000 + 90"],
         "padoms": "Simti un vieni ir nulles."},
        {"jaut": "45 608 = ?", "atb": ["40000+5000+600+8",
                                       "40 000 + 5 000 + 600 + 8"],
         "padoms": "Desmitu šķirā ir nulle."},
        {"jaut": "800 001 = ?", "atb": ["800000+1", "800 000 + 1"],
         "padoms": "Starp tām ir tikai nulles."},
    ], pamats=4,
        ievads="Ieraksti summu ar plusiem, piemēram: 4000+300+20."),

    Ievadi("Nosauc kaimiņu", [
        {"jaut": "Kurš skaitlis ir tieši pirms 5 000?", "atb": ["4999",
                                                                "4 999"],
         "padoms": "Par vienu mazāk - visas šķiras mainās uzreiz."},
        {"jaut": "Kurš skaitlis ir tieši aiz 19 999?", "atb": ["20000",
                                                               "20 000"],
         "padoms": "Deviņnieki pārvēršas nullēs."},
        {"jaut": "Kurš skaitlis ir tieši pirms 100 000?", "atb": ["99999",
                                                                  "99 999"],
         "padoms": "Vienu mazāk par simt tūkstošiem."},
        {"jaut": "Kurš skaitlis ir tieši aiz 809?", "atb": ["810"],
         "padoms": "Vienu šķiru uz augšu."},
    ], ievads="Kaimiņi ir par vienu mazāk un par vienu vairāk."),

    Varianti("Kur ir kļūda?", [
        {"jaut": "Kurš pieraksts ir pareizs skaitlim 3 070?",
         "opcijas": ["3 000 + 70", "3 000 + 700", "300 + 70", "3 000 + 7"],
         "pareizi": 0,
         "padoms": "Cipars 7 stāv desmitu vietā."},
        {"jaut": "Kurš skaitlis sanāk no 50 000 + 600 + 9?",
         "opcijas": ["50 609", "56 009", "50 069", "5 069"],
         "pareizi": 0,
         "padoms": "Katrai tukšai šķirai vietā jāieliek nulle."},
        {"jaut": "Kuram skaitlim kaimiņi ir 6 999 un 7 001?",
         "opcijas": ["7 000", "6 990", "7 010", "6 998"],
         "pareizi": 0,
         "padoms": "Meklē skaitli starp abiem."},
        {"jaut": "Cik šķiru nav tukšas skaitlī 400 020?",
         "opcijas": ["2", "3", "4", "6"],
         "pareizi": 0,
         "padoms": "Saskaiti tikai tos ciparus, kas nav nulles."},
    ], pamats=4),

    Pasaule("Cik degvielas paņem raķete?",
            Ievadi("", [
                {"jaut": "Uzraksti 2 030 kā šķiru summu.",
                 "atb": ["2000+30", "2 000 + 30"],
                 "padoms": "Simtu šķirā ir nulle.", "vieta": "2000+30"},
                {"jaut": "Kāds skaitlis ir 500 000 + 40 000 + 7?",
                 "atb": ["540007", "540 007"],
                 "padoms": "Tukšās vietas aizpilda ar nullēm."},
                {"jaut": "Cik tonnu ir 3 000 + 800 + 50?",
                 "atb": ["3850", "3 850"], "padoms": "Saskaiti gabalus."},
                {"jaut": "Kurš skaitlis ir tieši pirms 100 000?",
                 "atb": ["99999", "99 999"], "padoms": "Par vienu mazāk."},
            ]),
            pavediens="kosmoss",
            konteksts="Lielas raķetes starta masa ir ap 3 000 tonnu, un "
                      "gandrīz visa tā ir degviela.",
            kapec="Inženieri masu skaita pa šķirām: tonnas, simti, desmiti - "
                  "katra atsevišķi."),

    Kopsavilkums([
        "Uzrakstu skaitli kā šķiru summu.",
        "Zinu, ka nulles šķiru summā neraksta, bet vietā tā paliek.",
        "Nosaucu skaitļa kaimiņus, arī tad, ja mainās visas šķiras.",
    ]),

    Majas([
        "Uzraksti kā šķiru summu: sava mājas numura un pasta indeksa "
        "skaitļus.",
        "Padomā, kāpēc 1 000 kaimiņš 999 izskatās pavisam citāds.",
        "Atrodi veikala čekā skaitli un izjauc to pa šķirām.",
    ]),
]
