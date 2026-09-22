# -*- coding: utf-8 -*-
"""5. klase, 137. stunda: «Kā saskaitīt galvā?»

Pirmā darbība ar decimāldaļām, un tā notiek galvā. Iemesls ir vienkāršs:
0,7 + 0,5 ir tas pats, kas 7 + 5 desmitdaļas, tikai atbilde jāatliek atpakaļ
desmitdaļās. Tāpēc stunda nemāca kolonnu, bet domu gaitu - un prasa to
pateikt vārdiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā saskaitīt galvā?"

MERKIS = ("Iemācīsimies saskaitīt divas decimāldaļas ar vienu ciparu aiz "
          "komata galvā un skaidrot savu domu gaitu.")

SATURS = [
    Sakums("Septiņas plus piecas desmitdaļas",
           zimejums=taisne(0, 2, 0.5, [(0.7, "0,7"), (1.2, "1,2")],
                           virsraksts="No 0,7 vēl 0,5 uz priekšu"),
           paraksts="0,7 + 0,5 = 1,2 - divpadsmit desmitdaļas.",
           fakti=["0,7 ir 7 desmitdaļas, 0,5 ir 5 desmitdaļas.",
                  "Kopā tās ir 12 desmitdaļas.",
                  "Desmit desmitdaļas ir vesels, tāpēc iznāk 1,2."]),

    Doma("Skaiti desmitdaļas, ne komatus",
         "Decimāldaļas ar vienu ciparu aiz komata saskaita kā desmitdaļas; ja "
         "to summa pārsniedz 10, veidojas vesels skaitlis.",
         soli=[
             "Pasaki katru skaitli desmitdaļās.",
             "Saskaiti desmitdaļas kā parastus skaitļus.",
             "Ja iznāk vairāk par 10, atdali veselos.",
             "Pieraksti atbildi ar komatu.",
             "Pārbaudi: atbildei jābūt lielākai par katru saskaitāmo.",
         ],
         pieze="0,7 + 0,5 = 1,2, jo 12 desmitdaļas ir viens vesels un vēl "
               "divas. Tas ir tas pats, kas {7|10} + {5|10} = {12|10} = "
               "1{2|10}."),

    Paraugs("0,7 + 0,5",
            uzd="Izrēķini galvā un paskaidro, kā domāji.",
            soli=[
                ("0,7 ir 7 desmitdaļas",
                 "Pirmais saskaitāmais."),
                ("0,5 ir 5 desmitdaļas",
                 "Otrais saskaitāmais."),
                ("7 + 5 = 12 desmitdaļas",
                 "Saskaita kā veselus skaitļus."),
                ("12 desmitdaļas = 1 vesels un 2 desmitdaļas",
                 "Atdala veselo."),
                ("0,7 + 0,5 = 1,2",
                 "Atbilde ar komatu."),
            ],
            atbilde="0,7 + 0,5 = 1,2"),

    Ievadi("Saskaiti galvā", [
        {"jaut": "0,7 + 0,5 = ? Ieraksti skaitli.",
         "atb": ["1,2"], "padoms": "12 desmitdaļas."},
        {"jaut": "0,3 + 0,4 = ?",
         "atb": ["0,7"], "padoms": "7 desmitdaļas."},
        {"jaut": "0,6 + 0,6 = ?",
         "atb": ["1,2"], "padoms": "12 desmitdaļas."},
        {"jaut": "0,8 + 0,2 = ?",
         "atb": ["1"], "padoms": "10 desmitdaļas ir vesels."},
        {"jaut": "1,4 + 0,3 = ?",
         "atb": ["1,7"], "padoms": "Veselais paliek, desmitdaļas saskaitās."},
        {"jaut": "2,5 + 1,5 = ?",
         "atb": ["4"], "padoms": "10 desmitdaļas ir vesels."},
        {"jaut": "0,9 + 0,9 = ?",
         "atb": ["1,8"], "padoms": "18 desmitdaļas."},
        {"jaut": "3,2 + 0,9 = ?",
         "atb": ["4,1"], "padoms": "11 desmitdaļas."},
    ], pamats=4,
        ievads="Pasaki abus skaitļus desmitdaļās un saskaiti tās."),

    Zimejums("Lēciens pa skaitļu taisni",
             taisne(0, 2, 0.5, [(0.7, "0,7"), (1.2, "1,2")],
                    virsraksts="Pieci soļi pa desmitdaļai"),
             paskaidro="No 0,7 piecas desmitdaļas uz priekšu ir tieši 1,2. "
                       "Uz taisnes saskaitīšana ir lēciens pa labi.",
             ievads="To pašu var redzēt arī uz taisnes."),

    Varianti("Kā domā, saskaitot galvā?", [
        {"jaut": "0,7 + 0,5 ir...",
         "opcijas": ["1,2", "0,12", "1,12", "0,75"],
         "pareizi": 0,
         "padoms": "12 desmitdaļas."},
        {"jaut": "Cik desmitdaļu ir skaitlī 0,6?",
         "opcijas": ["6", "0,6", "60", "1"],
         "pareizi": 0,
         "padoms": "Pirmais cipars aiz komata."},
        {"jaut": "Cik ir 10 desmitdaļas?",
         "opcijas": ["1", "10", "0,1", "0,10"],
         "pareizi": 0,
         "padoms": "Viens vesels."},
        {"jaut": "0,8 + 0,2 ir...",
         "opcijas": ["1", "0,10", "0,16", "0,82"],
         "pareizi": 0,
         "padoms": "10 desmitdaļas."},
        {"jaut": "Kā pārbauda summu bez rēķināšanas?",
         "opcijas": ["Tai jābūt lielākai par katru saskaitāmo",
                     "Tai jābūt mazākai par 1",
                     "Tai jābūt veselai",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Pieliekot kļūst vairāk."},
        {"jaut": "2,5 + 1,5 ir...",
         "opcijas": ["4", "3,10", "3,55", "4,10"],
         "pareizi": 0,
         "padoms": "10 desmitdaļas ir vesels."},
    ], pamats=4),

    Pasaule("Cik metru dēļa kopā?",
            Ievadi("", [
                {"jaut": "Divi dēļi: 0,7 m un 0,5 m. Cik metru kopā?",
                 "atb": ["1,2"], "padoms": "12 desmitdaļas."},
                {"jaut": "Divi dēļi: 1,4 m un 0,3 m. Cik metru kopā?",
                 "atb": ["1,7"], "padoms": "Desmitdaļas saskaitās."},
                {"jaut": "Divas līstes: 2,5 m un 1,5 m. Cik metru kopā?",
                 "atb": ["4"], "padoms": "10 desmitdaļas ir vesels."},
                {"jaut": "Divas auklas: 0,9 m un 0,9 m. Cik metru kopā?",
                 "atb": ["1,8"], "padoms": "18 desmitdaļas."},
            ]),
            pavediens="maja",
            konteksts="Remontā garumus saskaita visu laiku, un parasti tas "
                      "notiek galvā, nevis uz papīra.",
            kapec="Ar vienu ciparu aiz komata rēķināt galvā ir ātrāk nekā "
                  "meklēt zīmuli."),

    Kopsavilkums([
        "Saskaitu divas decimāldaļas ar vienu ciparu aiz komata galvā.",
        "Pasaku skaitļus desmitdaļās un saskaitu tās.",
        "Atdalu veselo, ja desmitdaļu summa pārsniedz 10.",
        "Skaidroju savu domu gaitu vārdiem.",
    ]),

    Majas([
        "Izrēķini galvā 0,4 + 0,8; 1,6 + 0,7; 2,3 + 1,9.",
        "Uzraksti, kā tu domāji, rēķinot pirmo piemēru.",
        "Atrodi divus garumus mājās un saskaiti tos galvā.",
    ]),
]
