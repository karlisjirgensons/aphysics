# -*- coding: utf-8 -*-
"""5. klase, 131. stunda: «Kā parasto daļu pieraksta ar komatu?»

Jauna temata pirmā stunda. Decimāldaļa nav jauns skaitļu veids - tā ir tā
pati daļa ar saucēju 10, 100 vai 1000, tikai pierakstīta bez svītras. Tāpēc
stunda sākas nevis ar komata likumiem, bet ar pāreju turp un atpakaļ: no
{7|10} uz 0,7 un no 0,7 atkal uz {7|10}.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā parasto daļu pieraksta ar komatu?"

MERKIS = ("Iemācīsimies pierakstīt daļu ar saucēju 10, 100 vai 1000 kā "
          "decimāldaļu un otrādi.")

SATURS = [
    Sakums("Cenu zīmē nav svītras",
           zimejums=dala(10, 7, "7/10"),
           paraksts="{7|10} un 0,7 ir viens un tas pats skaitlis.",
           fakti=["Veikalā raksta 0,7 kg, nevis {7|10} kg.",
                  "Aiz komata stāv daļas skaitītājs.",
                  "Saucēju pasaka ciparu skaits aiz komata."]),

    Doma("Saucēju pasaka ciparu skaits",
         "Daļu ar saucēju 10, 100 vai 1000 raksta ar komatu: viens cipars aiz "
         "komata nozīmē desmitdaļas, divi - simtdaļas, trīs - tūkstošdaļas.",
         soli=[
             "Paskaties uz saucēju: 10, 100 vai 1000.",
             "Saskaiti nulles - tik ciparu būs aiz komata.",
             "Uzraksti veselo daļu, tad komatu.",
             "Aiz komata raksti skaitītāju, ja vajag - ar nullēm priekšā.",
             "Atpakaļ: cipari aiz komata ir skaitītājs, saucēju dod to "
             "skaits.",
         ],
         pieze="{7|100} ir 0,07, nevis 0,7 - simtdaļām aiz komata jābūt "
               "diviem cipariem. Tieši šī nulle ir biežākā kļūda, tāpēc "
               "vienmēr vispirms saskaita nulles saucējā."),

    Paraugs("Pieraksti {12|100} ar komatu",
            uzd="Uzraksti daļu {12|100} kā decimāldaļu.",
            soli=[
                ("Saucējs ir 100",
                 "Divas nulles."),
                ("Tātad aiz komata būs divi cipari",
                 "Simtdaļas."),
                ("Veselo nav, tāpēc raksta 0",
                 "Pirms komata."),
                ("0,12",
                 "Skaitītājs aiz komata."),
            ],
            atbilde="{12|100} = 0,12"),

    Ievadi("No daļas uz decimāldaļu", [
        {"jaut": "{7|10} kā decimāldaļa. Ieraksti skaitli.",
         "atb": ["0,7", "0.7"], "padoms": "Viens cipars aiz komata."},
        {"jaut": "{3|10} kā decimāldaļa.",
         "atb": ["0,3", "0.3"], "padoms": "Desmitdaļas."},
        {"jaut": "{12|100} kā decimāldaļa.",
         "atb": ["0,12", "0.12"], "padoms": "Divi cipari aiz komata."},
        {"jaut": "{7|100} kā decimāldaļa.",
         "atb": ["0,07", "0.07"], "padoms": "Vajag nulli priekšā."},
        {"jaut": "{125|1000} kā decimāldaļa.",
         "atb": ["0,125", "0.125"], "padoms": "Trīs cipari aiz komata."},
        {"jaut": "0,9 kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["9/10"], "padoms": "Viens cipars - desmitdaļas."},
        {"jaut": "0,45 kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["45/100", "9/20"], "padoms": "Divi cipari - simtdaļas."},
        {"jaut": "0,05 kā parastā daļa. Atbildi raksti kā a/b.",
         "atb": ["5/100", "1/20"], "padoms": "Simtdaļas."},
    ], pamats=4,
        ievads="Saskaiti nulles saucējā - tik ciparu būs aiz komata."),

    Zimejums("Desmitdaļas un simtdaļas",
             restis([["7/10", "0,7"],
                     ["7/100", "0,07"]],
                    virsraksts="Viena nulle maina visu"),
             paskaidro="Abās rindās skaitītājs ir 7, bet saucēji atšķiras "
                       "desmitkārt - un tieši tāpēc aiz komata ir dažāds "
                       "ciparu skaits.",
             ievads="Nulle aiz komata nav lieka."),

    Varianti("Cik ciparu aiz komata?", [
        {"jaut": "Saucējs ir 100. Cik ciparu būs aiz komata?",
         "opcijas": ["Divi", "Viens", "Trīs", "Neviens"],
         "pareizi": 0,
         "padoms": "Tik, cik nulļu saucējā."},
        {"jaut": "{7|100} kā decimāldaļa ir...",
         "opcijas": ["0,07", "0,7", "7,0", "0,007"],
         "pareizi": 0,
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "0,3 kā parastā daļa ir...",
         "opcijas": ["{3|10}", "{3|100}", "{1|3}", "{10|3}"],
         "pareizi": 0,
         "padoms": "Viens cipars - desmitdaļas."},
        {"jaut": "Ko nozīmē cipari aiz komata?",
         "opcijas": ["Daļas skaitītāju", "Daļas saucēju", "Veselo daļu",
                     "Neko"],
         "pareizi": 0,
         "padoms": "Saucēju dod ciparu skaits."},
        {"jaut": "{125|1000} kā decimāldaļa ir...",
         "opcijas": ["0,125", "0,0125", "1,25", "0,25"],
         "pareizi": 0,
         "padoms": "Trīs nulles - trīs cipari."},
        {"jaut": "Kas ir 2,5?",
         "opcijas": ["2 veseli un {5|10}", "{25|10} un nekas vairāk",
                     "2 veseli un {5|100}", "{2|5}"],
         "pareizi": 0,
         "padoms": "Pirms komata - veselie."},
    ], pamats=4),

    Pasaule("Ko rāda svari veikalā?",
            Ievadi("", [
                {"jaut": "Svari rāda {7|10} kg. Kā to raksta ar komatu?",
                 "atb": ["0,7", "0.7"], "padoms": "Desmitdaļas."},
                {"jaut": "Cenu zīmē ir 0,5 kg. Kā to raksta kā parasto daļu? "
                         "Atbildi kā a/b.",
                 "atb": ["5/10", "1/2"], "padoms": "Desmitdaļas."},
                {"jaut": "Iepakojumā ir {25|100} kg. Kā to raksta ar komatu?",
                 "atb": ["0,25", "0.25"], "padoms": "Simtdaļas."},
                {"jaut": "Svari rāda 0,05 kg. Kā to raksta kā parasto daļu? "
                         "Atbildi kā a/b.",
                 "atb": ["5/100", "1/20"], "padoms": "Divi cipari aiz "
                                                     "komata."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā visi skaitļi ir ar komatu, bet skolā tie paši "
                      "skaitļi ir daļas.",
            kapec="Pāriet no viena pieraksta uz otru var bez rēķina."),

    Kopsavilkums([
        "Pierakstu daļu ar saucēju 10, 100 vai 1000 kā decimāldaļu.",
        "Pierakstu decimāldaļu kā parasto daļu.",
        "Zinu, ka ciparu skaits aiz komata atbilst nullēm saucējā.",
        "Neaizmirstu nulli pierakstā 0,07.",
    ]),

    Majas([
        "Pieraksti ar komatu {9|10}, {3|100} un {45|1000}.",
        "Pieraksti kā parastās daļas 0,4, 0,08 un 0,125.",
        "Atrodi veikalā trīs skaitļus ar komatu un pieraksti tos kā daļas.",
    ]),
]
