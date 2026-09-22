# -*- coding: utf-8 -*-
"""5. klase, 135. stunda: «Kur uz skaitļu taisnes ir 0,7?»

Skaitļu taisne decimāldaļām strādā tieši tāpat kā daļām, tikai iedaļu
izvēlas pēc ciparu skaita aiz komata. Grūtākais te ir mērogs: lai atzīmētu
0,07, vienību jāsadala simt daļās, un tāpēc parasti zīmē nevis no 0 līdz 1,
bet no 0 līdz 0,1.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kur uz skaitļu taisnes ir 0,7?"

MERKIS = ("Mācīsimies attēlot decimāldaļas uz skaitļu taisnes, izvēloties "
          "soli un sākuma punktu.")

SATURS = [
    Sakums("Septiņas desmitdaļas no vienas",
           zimejums=taisne(0, 1, 0.1, [(0.7, "0,7")],
                           virsraksts="Vienība sadalīta 10 daļās"),
           paraksts="0,7 ir septītā iedaļa no nulles.",
           fakti=["Desmitdaļām vienību dala 10 daļās.",
                  "Simtdaļām ar to vairs nepietiek.",
                  "Tad izvēlas citu taisnes sākumu un galu."]),

    Doma("Iedaļu izvēlas pēc ciparu skaita",
         "Decimāldaļu atliek uz skaitļu taisnes, vienību sadalot 10 daļās "
         "desmitdaļām vai 100 daļām simtdaļām; ja skaitļi ir tuvu, izvēlas "
         "šaurāku taisnes posmu.",
         soli=[
             "Paskaties, cik ciparu ir aiz komata.",
             "Viens cipars - dali vienību 10 daļās.",
             "Divi cipari - izvēlies posmu starp divām desmitdaļām.",
             "Atzīmē punktu un pieraksti pie tā skaitli.",
             "Pārbaudi, vai punkts ir starp pareizajām iedaļām.",
         ],
         pieze="Taisnei nav obligāti jāsākas ar nulli. Ja jāatzīmē 0,72 un "
               "0,75, ērtāk ir zīmēt posmu no 0,7 līdz 0,8 - tad katra "
               "iedaļa ir viena simtdaļa."),

    Paraugs("Atliec 0,7 un 0,75",
            uzd="Kādu taisni izvēlēties abiem skaitļiem?",
            soli=[
                ("0,7 ir desmitdaļa",
                 "Viens cipars aiz komata."),
                ("0,75 ir simtdaļa",
                 "Divi cipari aiz komata."),
                ("Posms no 0,7 līdz 0,8",
                 "Tur ietilpst abi skaitļi."),
                ("Iedaļa ir 0,01",
                 "Simtdaļas."),
                ("0,75 ir piektā iedaļa no 0,7",
                 "Tieši posma vidū."),
            ],
            atbilde="Der posms no 0,7 līdz 0,8 ar simtdaļu iedaļu"),

    Ievadi("Kura iedaļa tā ir?", [
        {"jaut": "Vienība sadalīta 10 daļās. Kurā iedaļā ir 0,7? Ieraksti "
                 "skaitli.",
         "atb": ["7"], "padoms": "Septītā no nulles."},
        {"jaut": "Vienība sadalīta 10 daļās. Kurā iedaļā ir 0,3?",
         "atb": ["3"], "padoms": "Trešā no nulles."},
        {"jaut": "Vienība sadalīta 100 daļās. Kurā iedaļā ir 0,25?",
         "atb": ["25"], "padoms": "Divdesmit piektā."},
        {"jaut": "Starp kuriem desmitdaļu skaitļiem ir 0,75? Ieraksti "
                 "mazāko.",
         "atb": ["0,7"], "padoms": "0,7 un 0,8."},
        {"jaut": "Starp kuriem veseliem skaitļiem ir 2,4? Ieraksti mazāko.",
         "atb": ["2"], "padoms": "Veselā daļa."},
        {"jaut": "Cik daļās jāsadala vienība, lai atzīmētu 0,07?",
         "atb": ["100"], "padoms": "Divi cipari aiz komata."},
        {"jaut": "Cik daļās jāsadala vienība, lai atzīmētu 0,4?",
         "atb": ["10"], "padoms": "Viens cipars aiz komata."},
        {"jaut": "Kurš skaitlis ir tieši posma no 0,7 līdz 0,8 vidū?",
         "atb": ["0,75"], "padoms": "Piektā simtdaļa."},
    ], pamats=4,
        ievads="Vispirms izlem, cik daļās dalīt vienību."),

    Zimejums("Tuvinājums no 0,7 līdz 0,8",
             taisne(0.7, 0.8, 0.02, [(0.75, "0,75")],
                    virsraksts="Iedaļa ir divas simtdaļas"),
             paskaidro="Ja taisni zīmē tikai starp 0,7 un 0,8, simtdaļas "
                       "kļūst redzamas. Tāpēc taisnes sākumu izvēlas pēc "
                       "skaitļiem.",
             ievads="Šaurāks posms parāda sīkākas šķiras."),

    Varianti("Kādu taisni izvēlēties?", [
        {"jaut": "Cik daļās dala vienību desmitdaļām?",
         "opcijas": ["10", "100", "2", "5"],
         "pareizi": 0,
         "padoms": "Viens cipars aiz komata."},
        {"jaut": "Cik daļās dala vienību simtdaļām?",
         "opcijas": ["100", "10", "50", "1000"],
         "pareizi": 0,
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "Starp kuriem skaitļiem atrodas 0,75?",
         "opcijas": ["0,7 un 0,8", "0,5 un 0,6", "7 un 8", "0,07 un 0,08"],
         "pareizi": 0,
         "padoms": "Desmitdaļas ap to."},
        {"jaut": "Vai skaitļu taisnei obligāti jāsākas ar nulli?",
         "opcijas": ["Nē, sākumu izvēlas pats", "Jā, vienmēr",
                     "Tikai decimāldaļām", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Posmu izvēlas pēc skaitļiem."},
        {"jaut": "Kurš skaitlis ir tuvāk vieniniekam?",
         "opcijas": ["0,9", "0,7", "0,5", "0,09"],
         "pareizi": 0,
         "padoms": "Vairāk desmitdaļu."},
        {"jaut": "Kurš skaitlis ir tuvāk nullei?",
         "opcijas": ["0,05", "0,5", "0,15", "0,25"],
         "pareizi": 0,
         "padoms": "Mazāk simtdaļu."},
    ], pamats=4),

    Pasaule("Cik sver iepakojums?",
            Ievadi("", [
                {"jaut": "Uz svariem 0,7 kg. Starp kuriem veseliem "
                         "kilogramiem tas ir? Ieraksti mazāko.",
                 "atb": ["0"], "padoms": "Mazāk par vienu."},
                {"jaut": "Svari rāda 1,25 kg. Starp kuriem veseliem tas ir? "
                         "Ieraksti mazāko.",
                 "atb": ["1"], "padoms": "Veselā daļa."},
                {"jaut": "Svari rāda 2,5 kg. Cik desmitdaļu ir aiz komata?",
                 "atb": ["5"], "padoms": "Pirmais cipars aiz komata."},
                {"jaut": "Kurš iepakojums ir smagāks - 0,8 kg vai 0,75 kg? "
                         "Ieraksti skaitli.",
                 "atb": ["0,8", "0,80"], "padoms": "0,80 pret 0,75."},
            ]),
            pavediens="veikals",
            konteksts="Svaru skala ir skaitļu taisne: iedaļas tur ir "
                       "desmitdaļas vai simtdaļas kilograma.",
            kapec="Nolasīt svaru nozīmē atrast punktu starp divām iedaļām."),

    Kopsavilkums([
        "Atlieku decimāldaļu uz skaitļu taisnes.",
        "Izvēlos iedaļu pēc ciparu skaita aiz komata.",
        "Izvēlos taisnes sākumu un galu pēc dotajiem skaitļiem.",
        "Pārbaudu, starp kurām iedaļām punkts atrodas.",
    ]),

    Majas([
        "Uzzīmē taisni no 0 līdz 1 ar desmitdaļu iedaļu un atzīmē 0,3 un "
        "0,8.",
        "Uzzīmē taisni no 0,4 līdz 0,5 un atzīmē 0,45.",
        "Padomā, kādu taisni vajadzētu skaitlim 0,005.",
    ]),
]
