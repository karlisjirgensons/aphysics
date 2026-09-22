# -*- coding: utf-8 -*-
"""5. klase, 132. stunda: «Kāds ir decimāldaļas decimālais sastāvs?»

Tā pati 2. stundas doma, tikai tagad arī pa labi no komata: skaitlis ir
šķiru summa. Tieši šis pieraksts vēlāk izskaidro, kāpēc decimāldaļas saskaita
kolonnā pa šķirām un kāpēc 0,7 ir lielāks par 0,07 - katram ciparam ir sava
vieta un sava vērtība.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāds ir decimāldaļas decimālais sastāvs?"

MERKIS = ("Mācīsimies skaidrot decimāldaļas sastāvu un pierakstīt to kā "
          "summu.")

SATURS = [
    Sakums("Katram ciparam sava vieta",
           zimejums=restis([["3", ",", "1", "2"]],
                           virsraksts="Skaitlis 3,12 pa cipariem"),
           paraksts="3,12 = 3 + 0,1 + 0,02.",
           fakti=["Pirms komata ir veselie.",
                  "Pirmais cipars aiz komata - desmitdaļas.",
                  "Otrais - simtdaļas, trešais - tūkstošdaļas."]),

    Doma("Skaitlis ir šķiru summa",
         "Decimāldaļu var pierakstīt kā summu: veselie plus desmitdaļas plus "
         "simtdaļas plus tūkstošdaļas.",
         soli=[
             "Nosaki veselo daļu - to, kas ir pirms komata.",
             "Pirmais cipars aiz komata ir desmitdaļas.",
             "Otrais - simtdaļas, trešais - tūkstošdaļas.",
             "Uzraksti katru šķiru atsevišķi un saliec ar plusiem.",
             "Pārbaudi: summai jādod sākotnējais skaitlis.",
         ],
         pieze="Nulle aiz komata nav tukša vieta, bet šķira bez vienībām: "
               "3,05 ir 3 + 0 desmitdaļas + 5 simtdaļas. Tāpēc to nedrīkst "
               "izlaist."),

    Paraugs("Sadali 3,12 pa šķirām",
            uzd="Pieraksti skaitli 3,12 kā summu.",
            soli=[
                ("Veselā daļa ir 3",
                 "Pirms komata."),
                ("Desmitdaļas: 1",
                 "Pirmais cipars aiz komata - 0,1."),
                ("Simtdaļas: 2",
                 "Otrais cipars - 0,02."),
                ("3,12 = 3 + 0,1 + 0,02",
                 "Šķiru summa."),
            ],
            atbilde="3,12 = 3 + 0,1 + 0,02"),

    Ievadi("Nosaki šķiras", [
        {"jaut": "Skaitlī 3,12 - kāda ir veselā daļa?",
         "atb": ["3"], "padoms": "Pirms komata."},
        {"jaut": "Skaitlī 3,12 - cik ir desmitdaļu?",
         "atb": ["1"], "padoms": "Pirmais cipars aiz komata."},
        {"jaut": "Skaitlī 3,12 - cik ir simtdaļu?",
         "atb": ["2"], "padoms": "Otrais cipars aiz komata."},
        {"jaut": "Skaitlī 0,458 - cik ir tūkstošdaļu?",
         "atb": ["8"], "padoms": "Trešais cipars aiz komata."},
        {"jaut": "Skaitlī 7,05 - cik ir desmitdaļu?",
         "atb": ["0"], "padoms": "Pirmais cipars aiz komata ir nulle."},
        {"jaut": "Cik ir 2 + 0,3 + 0,04? Ieraksti skaitli.",
         "atb": ["2,34"], "padoms": "Saliec šķiras kopā."},
        {"jaut": "Cik ir 5 + 0,7? Ieraksti skaitli.",
         "atb": ["5,7"], "padoms": "Viena desmitdaļu šķira."},
        {"jaut": "Cik ir 0,2 + 0,06? Ieraksti skaitli.",
         "atb": ["0,26"], "padoms": "Desmitdaļas un simtdaļas."},
    ], pamats=4,
        ievads="Katram ciparam ir sava šķira - no tās arī vērtība."),

    Zimejums("Šķiras pa labi no komata",
             restis([["0,1", "0,01", "0,001"]],
                    virsraksts="Desmitdaļa, simtdaļa, tūkstošdaļa"),
             paskaidro="Katra nākamā šķira ir desmit reizes mazāka par "
                       "iepriekšējo - tieši tāpat kā pirms komata katra "
                       "nākamā ir desmit reizes lielāka.",
             ievads="Šķiru kārtība turpinās abos virzienos."),

    Varianti("Kura šķira tā ir?", [
        {"jaut": "Kurš cipars skaitlī 4,56 apzīmē simtdaļas?",
         "opcijas": ["6", "5", "4", "Neviens"],
         "pareizi": 0,
         "padoms": "Otrais aiz komata."},
        {"jaut": "Kurš cipars skaitlī 4,56 apzīmē desmitdaļas?",
         "opcijas": ["5", "6", "4", "Neviens"],
         "pareizi": 0,
         "padoms": "Pirmais aiz komata."},
        {"jaut": "Ko nozīmē nulle skaitlī 3,05?",
         "opcijas": ["Desmitdaļu nav", "Simtdaļu nav", "Veselo nav",
                     "Tā ir lieka"],
         "pareizi": 0,
         "padoms": "Nulle ir šķira bez vienībām."},
        {"jaut": "2 + 0,3 + 0,04 ir...",
         "opcijas": ["2,34", "0,234", "23,4", "2,304"],
         "pareizi": 0,
         "padoms": "Katra šķira savā vietā."},
        {"jaut": "Cik reižu simtdaļa ir mazāka par desmitdaļu?",
         "opcijas": ["10", "2", "100", "5"],
         "pareizi": 0,
         "padoms": "Katra nākamā šķira."},
        {"jaut": "Skaitlis 0,405 sastāv no...",
         "opcijas": ["0,4 un 0,005", "0,4 un 0,05", "4 un 5",
                     "0,04 un 0,5"],
         "pareizi": 0,
         "padoms": "Desmitdaļas un tūkstošdaļas."},
    ], pamats=4),

    Pasaule("Cenas un šķiras",
            Ievadi("", [
                {"jaut": "Prece maksā 3,45 €. Cik eiro ir veselā daļa?",
                 "atb": ["3"], "padoms": "Pirms komata."},
                {"jaut": "Cik centu ir šai cenai? Ieraksti skaitli.",
                 "atb": ["45"], "padoms": "Divi cipari aiz komata."},
                {"jaut": "Prece maksā 2,05 €. Cik centu tas ir?",
                 "atb": ["5"], "padoms": "Nulle desmitdaļās."},
                {"jaut": "Prece maksā 0,80 €. Cik centu tas ir?",
                 "atb": ["80"], "padoms": "Astoņas desmitdaļas eiro."},
            ]),
            pavediens="veikals",
            konteksts="Eiro un centi ir tieši veselie un simtdaļas - tāpēc "
                      "cena vienmēr ir ar diviem cipariem aiz komata.",
            kapec="Šķiru sastāvs pasaka, cik centu ir katrā cenā."),

    Kopsavilkums([
        "Nosaucu decimāldaļas šķiras: veselie, desmitdaļas, simtdaļas.",
        "Pierakstu decimāldaļu kā šķiru summu.",
        "Skaidroju, ko nozīmē nulle aiz komata.",
        "Salieku skaitli atpakaļ no šķiru summas.",
    ]),

    Majas([
        "Pieraksti kā summas 4,56, 0,708 un 12,03.",
        "Saliec kopā 7 + 0,2 + 0,005.",
        "Atrodi čekā cenu un pasaki, cik tajā ir desmitdaļu un simtdaļu.",
    ]),
]
