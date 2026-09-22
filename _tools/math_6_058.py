# -*- coding: utf-8 -*-
"""6. klase, 58. stunda: «Kur radusies kļūda?»

Temata pēdējā mācību stunda. Vērtēt cita risinājumu ir grūtāk nekā risināt
pašam: jāsaprot ne tikai, ka atbilde ir greiza, bet arī kurā solī un kāpēc.
Tieši šī prasme vēlāk ļauj pārbaudīt pašam savu darbu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kur radusies kļūda?"

MERKIS = ("Mācīsimies izvērtēt cita risinājuma pareizību un raksturot "
          "iespējamos kļūdas cēloņus.")

SATURS = [
    Sakums("Kļūdas atkārtojas vienās un tajās pašās vietās",
           fakti=["Komats reizinājumā - visbiežākā kļūda šajā tematā.",
                  "Aizmirsts apgriezt dalītāju - otra biežākā.",
                  "Nepareizs virziens, pārceļot komatu, - trešā."]),

    Doma("Meklē kļūdu pa soļiem, ne atbildē",
         "Lai atrastu kļūdu, katru risinājuma soli pārbauda atsevišķi: "
         "vispirms novērtē atbildi, tad seko soļiem no augšas uz leju.",
         soli=[
             "Novērtē, kāda atbilde būtu gaidāma.",
             "Salīdzini to ar doto - ja atšķirība ir desmitkārtīga, meklē "
             "komatu.",
             "Pārbaudi katru soli atsevišķi, sākot no pirmā.",
             "Atrodi pirmo soli, kurā rezultāts vairs nesakrīt.",
             "Pieraksti, kāda tieši kļūda tur notikusi.",
         ],
         pieze="Kļūdas cēloni raksta ar vārdiem, ne ar «te ir nepareizi»: "
               "«komats ielikts par vienu vietu pa labi» ir noderīgs "
               "aprakstījums, «nepareizi» - nav."),

    Paraugs("Atrodi kļūdu cita darbā",
            uzd="Skolēns rēķina: 0,6 · 0,4 = 2,4. Kur ir kļūda?",
            soli=[
                ("Novērtējums: abi reizinātāji mazāki par 1",
                 "Rezultātam jābūt mazākam par 0,6."),
                ("2,4 ir lielāks par abiem",
                 "Tātad atbilde nav ticama."),
                ("6 · 4 = 24 - cipari pareizi",
                 "Kļūda nav reizināšanā."),
                ("Aiz komata jābūt diviem cipariem: 0,24",
                 "Komats ielikts par vienu vietu pa labi."),
            ],
            atbilde="pareizi ir 0,24; kļūda ir komata vietā"),

    Ievadi("Izlabo kļūdaino atbildi", [
        {"jaut": "Skolēns: 0,6 · 0,4 = 2,4. Kāda ir pareizā atbilde?",
         "atb": ["0,24", "0.24"], "padoms": "Divi cipari aiz komata."},
        {"jaut": "Skolēns: 4,5 : 0,5 = 0,9. Kāda ir pareizā atbilde?",
         "atb": ["9"], "padoms": "45 : 5."},
        {"jaut": "Skolēns: {1|2} : {1|4} = {1|8}. Kāda ir pareizā atbilde?",
         "atb": ["2"], "padoms": "{1|2} · 4."},
        {"jaut": "Skolēns: 3,2 · 10 = 3,20. Kāda ir pareizā atbilde?",
         "atb": ["32"], "padoms": "Komats pa labi."},
        {"jaut": "Skolēns: 7 : 100 = 700. Kāda ir pareizā atbilde?",
         "atb": ["0,07", "0.07"], "padoms": "Komats pa kreisi."},
        {"jaut": "Skolēns: {2|3} · {3|4} = {5|7}. Kāda ir pareizā atbilde?",
         "atb": ["1/2", "6/12"], "padoms": "Reizinot nemeklē kopsaucēju."},
    ], pamats=4,
        ievads="Vispirms pasaki, kāda atbilde būtu gaidāma."),

    Varianti("Kāds ir kļūdas cēlonis?", [
        {"jaut": "0,6 · 0,4 = 2,4. Kāda kļūda?",
         "opcijas": ["Komats ielikts nepareizā vietā",
                     "Nepareizi sareizināti cipari",
                     "Saskaitīts, nevis reizināts", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "24 ir pareizi, komats - nē."},
        {"jaut": "{1|2} : {1|4} = {1|8}. Kāda kļūda?",
         "opcijas": ["Dalītājs nav apgriezts",
                     "Saucēji saskaitīti",
                     "Nepareizi saīsināts", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Dalot reizina ar apgriezto."},
        {"jaut": "3,2 · 10 = 3,20. Kāda kļūda?",
         "opcijas": ["Komats pārcelts nepareizā virzienā vai nemaz",
                     "Nepareizi sareizināts",
                     "Pierakstītas liekas nulles", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Reizinot ar 10, skaitlim jāaug."},
        {"jaut": "Ar ko sāk kļūdas meklēšanu?",
         "opcijas": ["Ar novērtējumu", "Ar pēdējo soli",
                     "Ar atbildes pārrakstīšanu", "Ar jaunu risinājumu"],
         "pareizi": 0,
         "padoms": "Novērtējums pasaka, cik tālu atbilde ir no patiesības."},
    ], pamats=4),

    Petijums("Pārbaudi sava soļabiedra darbu",
             vajag="divu skolēnu risinājumi",
             soli=[
                 "Samainieties burtnīcām ar soļabiedru.",
                 "Katram uzdevumam vispirms pieraksti savu novērtējumu.",
                 "Atrodi pirmo soli, kurā rezultāts nesakrīt.",
                 "Pieraksti kļūdas cēloni vārdiem, ne tikai «nepareizi».",
                 "Atdodiet burtnīcas un salīdziniet piezīmes.",
             ],
             secinajums="Cita kļūdu pamanīt ir vieglāk nekā savu - tieši "
                        "tāpēc pārbaude pa pāriem strādā."),

    Pasaule("Vai rēķins veikalā ir pareizs?",
            Ievadi("", [
                {"jaut": "Čekā: 2,5 kg pa 1,2 € = 30 €. Kāda ir pareizā "
                         "summa eiro?",
                 "atb": ["3"], "padoms": "25 · 12 = 300; divi cipari."},
                {"jaut": "Čekā: 0,4 kg pa 6 € = 24 €. Kāda ir pareizā summa?",
                 "atb": ["2,4", "2.4"], "padoms": "Viens cipars aiz komata."},
                {"jaut": "Čekā: 3 gab. pa 0,75 € = 2,25 €. Vai pareizi? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "3 · 75 = 225."},
                {"jaut": "Čekā kopsumma 3 + 2,4 + 2,25. Cik eiro?",
                 "atb": ["7,65", "7.65"], "padoms": "Saskaita pa vietām."},
            ]),
            pavediens="veikals",
            konteksts="Kases čeku pārbaudīt var tikai tas, kurš prot novērtēt "
                      "katru rindu atsevišķi.",
            kapec="Novērtējums atrod kļūdu ātrāk nekā pārrēķināšana."),

    Kopsavilkums([
        "Izvērtēju cita risinājuma pareizību pa soļiem.",
        "Sāku ar novērtējumu, nevis ar pārrēķināšanu.",
        "Atrodu pirmo kļūdaino soli.",
        "Raksturoju kļūdas cēloni ar vārdiem.",
    ]),

    Majas([
        "Atrodi savā vecā darbā kļūdu un pieraksti tās cēloni.",
        "Uzraksti kādam uzdevumu ar apzinātu kļūdu un palūdz to atrast.",
        "Pieraksti trīs kļūdas, kuras šajā tematā pieļāvi visbiežāk.",
    ]),
]
