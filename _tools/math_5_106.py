# -*- coding: utf-8 -*-
"""5. klase, 106. stunda: «Kā aizpildīt skaitļu trijstūri?»

Temata pēdējā stunda pirms pārbaudes darba, un tā ir 18. stundas maģiskā
kvadrāta pēctece: tas pats uzdevuma veids, tikai ar daļām. Skaitļu trijstūrī
katrs skaitlis ir abu zem tā stāvošo summa, tāpēc aizpildīt var gan no
apakšas uz augšu, gan otrādi - un tieši otrais virziens prasa atņemšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā aizpildīt skaitļu trijstūri?"

MERKIS = ("Mācīsimies papildināt skaitļu sakārtojumu ar daļām un jauktiem "
          "skaitļiem pēc dotiem nosacījumiem.")

SATURS = [
    Sakums("Katrs skaitlis ir abu apakšējo summa",
           zimejums=restis([["1/4", "1/4", "1/2"]],
                           virsraksts="Trijstūra apakšējā rinda"),
           paraksts="Virs pirmajiem diviem būs {1|2}, virs pēdējiem "
                    "diviem - {3|4}.",
           fakti=["Trijstūra apakšā ir trīs skaitļi.",
                  "Katrs skaitlis virs tiem ir divu apakšējo summa.",
                  "Virsotnē paliek viens skaitlis."]),

    Doma("No apakšas uz augšu - saskaitot",
         "Skaitļu trijstūrī katrs skaitlis ir abu zem tā stāvošo summa; "
         "trūkstošo apakšējo atrod, no augšējā atņemot otru apakšējo.",
         soli=[
             "Pārbaudi, kuri skaitļi jau ir doti.",
             "Ja doti abi apakšējie - saskaiti tos.",
             "Ja dots augšējais un viens apakšējais - atņem.",
             "Pārraksti daļas ar kopsaucēju, pirms rēķini.",
             "Pārbaudi visu trijstūri no apakšas uz augšu.",
         ],
         pieze="Aizpildīt ne vienmēr var pēc kārtas: reizēm vispirms jāatrod "
               "kāds skaitlis vidū, un tikai tad kļūst iespējams nākamais. "
               "Tāpēc vispirms der paskatīties, kur ir divi zināmie blakus."),

    Paraugs("Aizpildi trijstūri",
            uzd="Apakšējā rindā ir {1|4}, {1|4} un {1|2}. Aizpildi pārējo.",
            soli=[
                ("{1|4} + {1|4} = {2|4} = {1|2}",
                 "Otrās rindas pirmais skaitlis."),
                ("{1|4} + {1|2} = {1|4} + {2|4} = {3|4}",
                 "Otrās rindas otrais skaitlis."),
                ("{1|2} + {3|4} = {2|4} + {3|4} = {5|4}",
                 "Virsotne."),
                ("{5|4} = 1{1|4}",
                 "Atdala veselo."),
            ],
            atbilde="Otrajā rindā {1|2} un {3|4}, virsotnē 1{1|4}"),

    Ievadi("Aizpildi trūkstošo", [
        {"jaut": "{1|4} + {1|4} = ? Atbildi raksti kā a/b.",
         "atb": ["1/2", "2/4"], "padoms": "{2|4} = {1|2}."},
        {"jaut": "{1|4} + {1|2} = ? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "{1|4} + {2|4}."},
        {"jaut": "{1|2} + {3|4} = ? Atbildi raksti kā a b/c.",
         "atb": ["1 1/4"], "padoms": "{5|4} = 1{1|4}."},
        {"jaut": "Virs diviem skaitļiem ir {3|4}, viens no tiem ir {1|4}. "
                 "Kāds ir otrs? Atbildi raksti kā a/b.",
         "atb": ["1/2", "2/4"], "padoms": "{3|4} - {1|4}."},
        {"jaut": "Virs diviem skaitļiem ir 1{1|2}, viens no tiem ir {3|4}. "
                 "Kāds ir otrs? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "1{1|2} - {3|4}."},
        {"jaut": "Virs diviem skaitļiem ir 1, viens no tiem ir {1|3}. Kāds "
                 "ir otrs? Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "1 = {3|3}."},
        {"jaut": "{2|3} + {1|6} = ? Atbildi raksti kā a/b.",
         "atb": ["5/6"], "padoms": "{4|6} + {1|6}."},
        {"jaut": "Virs diviem skaitļiem ir {5|6}, viens no tiem ir {1|6}. "
                 "Kāds ir otrs? Atbildi raksti kā a/b.",
         "atb": ["2/3", "4/6"], "padoms": "{5|6} - {1|6} = {4|6}."},
    ], pamats=4,
        ievads="Divi apakšējie dod augšējo; augšējais un viens apakšējais "
               "dod otru."),

    Zimejums("Aizpildīts trijstūris",
             restis([["1 1/4", "", ""],
                     ["1/2", "3/4", ""],
                     ["1/4", "1/4", "1/2"]],
                    virsraksts="Virsotne augšā, pamats apakšā"),
             paskaidro="Apakšējā rindā ir dotie skaitļi, vidējā - to summas, "
                       "virsotnē - abu vidējo summa.",
             ievads="Tā izskatās gatavs skaitļu trijstūris."),

    Varianti("Kā aizpilda trijstūri?", [
        {"jaut": "Kas ir katrs trijstūra skaitlis?",
         "opcijas": ["Abu zem tā stāvošo summa", "Abu starpība",
                     "Abu reizinājums", "Nejaušs skaitlis"],
         "pareizi": 0,
         "padoms": "No apakšas uz augšu - saskaitot."},
        {"jaut": "Kā atrod trūkstošo apakšējo skaitli?",
         "opcijas": ["No augšējā atņem otru apakšējo",
                     "Saskaita abus augšējos",
                     "Augšējo dala ar diviem",
                     "To nevar atrast"],
         "pareizi": 0,
         "padoms": "Atņemšana ir pretējā darbība."},
        {"jaut": "Apakšā ir {1|4} un {1|4}. Kas ir virs tiem?",
         "opcijas": ["{1|2}", "{2|8}", "{1|4}", "{1|16}"],
         "pareizi": 0,
         "padoms": "{2|4} = {1|2}."},
        {"jaut": "Virs diviem skaitļiem ir 1, viens ir {1|3}. Kāds ir otrs?",
         "opcijas": ["{2|3}", "{1|3}", "1{1|3}", "{3|3}"],
         "pareizi": 0,
         "padoms": "1 = {3|3}."},
        {"jaut": "Ko dara, pirms saskaita daļas ar dažādiem saucējiem?",
         "opcijas": ["Pārraksta ar kopsaucēju", "Saīsina",
                     "Atdala veselo", "Neko"],
         "pareizi": 0,
         "padoms": "Vienādi gabali vispirms."},
        {"jaut": "Kā pārbaudīt aizpildīto trijstūri?",
         "opcijas": ["Pārrēķināt to no apakšas uz augšu",
                     "Saskaitīt visus skaitļus",
                     "Salīdzināt ar kaimiņa darbu",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Katrai summai jāsakrīt."},
    ], pamats=4),

    Pasaule("Treniņu piramīda",
            Ievadi("", [
                {"jaut": "Pirmajās divās dienās 1{1|4} km un 1{1|4} km. Cik "
                         "kopā? Atbildi raksti kā a b/c.",
                 "atb": ["2 1/2", "2 2/4"], "padoms": "{2|4} = {1|2}."},
                {"jaut": "Otrajā un trešajā dienā 1{1|4} km un 1{1|2} km. Cik "
                         "kopā? Atbildi raksti kā a b/c.",
                 "atb": ["2 3/4"], "padoms": "{1|4} + {2|4}."},
                {"jaut": "Cik kopā abas summas? Atbildi raksti kā a b/c.",
                 "atb": ["5 1/4"], "padoms": "2{1|2} + 2{3|4}."},
                {"jaut": "Divu dienu summa ir 2{1|2} km, pirmā diena "
                         "1{1|4} km. Cik otrā? Atbildi raksti kā a b/c.",
                 "atb": ["1 1/4"], "padoms": "2{1|2} - 1{1|4}."},
            ]),
            pavediens="sports",
            konteksts="Treniņu tabulā arī rēķina pa pāriem: divu dienu "
                      "summa, tad divu summu summa.",
            kapec="Trijstūris ir tā pati tabula, tikai sakārtota."),

    Kopsavilkums([
        "Aizpildu skaitļu trijstūri, saskaitot blakus stāvošos skaitļus.",
        "Atrodu trūkstošo apakšējo skaitli ar atņemšanu.",
        "Pārrakstu daļas ar kopsaucēju, pirms rēķinu.",
        "Pārbaudu visu sakārtojumu no apakšas uz augšu.",
    ]),

    Majas([
        "Aizpildi trijstūri, kura apakšā ir {1|3}, {1|6} un {1|2}.",
        "Izveido savu trijstūri ar jauktiem skaitļiem apakšā.",
        "Sagatavojies pārbaudes darbam: pārskati 91.-105. stundas "
        "kopsavilkumus.",
    ]),
]
