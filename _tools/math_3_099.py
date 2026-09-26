# -*- coding: utf-8 -*-
"""3. klase, 99. stunda: «Kas ir simtdaļa?»

Simtdaļa jau parādījās naudā; te tā tiek nosaukta vārdā un piesieta modelim -
simta kvadrātam, kurā viena rūtiņa ir viena simtdaļa. No šī modeļa 6. klasē
izaugs procenti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kvadrats)

TEMA = "Kas ir simtdaļa?"

MERKIS = ("Lasīsim un pierakstīsim simtdaļas; saistīsim tās ar daļu, kuras "
          "saucējs ir 100.")

SATURS = [
    Sakums("Cik maza ir viena rūtiņa simta kvadrātā?",
           zimejums=kvadrats(10, 10, 3, 10,
                             paraksts="30 rūtiņas no 100"),
           fakti=["Simta kvadrātā ir 100 vienādu rūtiņu.",
                  "Viena rūtiņa ir {1|100} jeb 0,01.",
                  "Trīsdesmit rūtiņas ir {30|100} jeb 0,3."]),

    Doma("Simtdaļa ir viena no simts vienādām daļām",
         "{1|100} = 0,01, un desmit simtdaļas ir viena desmitdaļa: "
         "{10|100} = {1|10} = 0,1.",
         soli=[
             "Sadali veselo 100 vienādās daļās.",
             "Viena daļa ir simtdaļa.",
             "Pieraksti to ar komatu: 0,01.",
             "Desmit simtdaļas saliec vienā desmitdaļā.",
         ],
         pieze="Aiz komata pirmā vieta ir desmitdaļas, otrā - simtdaļas. "
               "Tāpēc 0,25 ir divas desmitdaļas un piecas simtdaļas."),

    Paraugs("Kā pierakstīt 25 simtdaļas?",
            uzd="Pieraksti {25|100} ar komatu un pasaki, cik tas ir "
                "desmitdaļās.",
            soli=[
                ("{25|100} = 0,25",
                 "Divi cipari aiz komata - simtdaļas."),
                ("20 simtdaļas = 2 desmitdaļas",
                 "Desmit simtdaļas ir viena desmitdaļa."),
                ("0,25 = 2 desmitdaļas un 5 simtdaļas",
                 "Tas ir arī {1|4} no veselā."),
            ],
            atbilde="0,25"),

    Ievadi("Simtdaļas", [
        {"jaut": "Pieraksti {1|100} ar komatu.", "atb": ["0,01", "0.01"],
         "padoms": "Divi cipari aiz komata."},
        {"jaut": "Pieraksti {25|100} ar komatu.", "atb": ["0,25", "0.25"],
         "padoms": "Divdesmit piecas simtdaļas."},
        {"jaut": "Cik simtdaļu ir vienā desmitdaļā?", "atb": ["10"],
         "padoms": "100 : 10."},
        {"jaut": "Cik simtdaļu ir vienā veselajā?", "atb": ["100"],
         "padoms": "Visas."},
        {"jaut": "Cik rūtiņu simta kvadrātā ir {1|4}?", "atb": ["25"],
         "padoms": "100 : 4."},
        {"jaut": "Cik rūtiņu simta kvadrātā ir {1|2}?", "atb": ["50"],
         "padoms": "100 : 2."},
    ], pamats=4),

    Zimejums("Ceturtdaļa simta kvadrātā",
             kvadrats(10, 10, 5, 5, paraksts="25 rūtiņas no 100"),
             paskaidro="25 rūtiņas no 100 ir {25|100} jeb 0,25 jeb {1|4}.",
             ievads="Tā izskatās ceturtdaļa."),

    Varianti("Cik tas ir?", [
        {"jaut": "Cik ir {50|100}?",
         "opcijas": ["0,5", "0,05", "5,0", "50"],
         "pareizi": 0, "padoms": "Piecdesmit simtdaļas ir puse."},
        {"jaut": "Kura daļa ir vienāda ar 0,25?",
         "opcijas": ["{1|4}", "{1|25}", "{1|2}", "{25|10}"],
         "pareizi": 0, "padoms": "25 no 100."},
        {"jaut": "Cik simtdaļu ir 0,07?",
         "opcijas": ["7", "70", "0,7", "700"],
         "pareizi": 0, "padoms": "Divi cipari aiz komata."},
        {"jaut": "Kura vieta aiz komata ir simtdaļas?",
         "opcijas": ["Otrā", "Pirmā", "Trešā", "Pēdējā"],
         "pareizi": 0, "padoms": "Pirmā ir desmitdaļas."},
    ], pamats=4),

    Pasaule("Cik liela ir atlaide?",
            Ievadi("", [
                {"jaut": "Prece maksāja 100 centus, atlaide 25 simtdaļas. "
                         "Cik centu ir atlaide?",
                 "atb": ["25"], "padoms": "{25|100} no 100."},
                {"jaut": "Cik centu jāmaksā pēc atlaides?",
                 "atb": ["75"], "padoms": "100 − 25."},
                {"jaut": "Prece maksāja 200 centus, atlaide ir {1|4}. Cik "
                         "centu ir atlaide?",
                 "atb": ["50"], "padoms": "200 : 4."},
                {"jaut": "Cik centu jāmaksā pēc atlaides?",
                 "atb": ["150"], "padoms": "200 − 50."},
            ]),
            pavediens="veikals",
            konteksts="Atlaides veikalā rēķina tieši simtdaļās - vēlāk tās "
                      "sauks par procentiem.",
            kapec="Simta kvadrāts parāda atlaidi tā, ka to var saskaitīt."),

    Kopsavilkums([
        "Zinu, ka simtdaļa ir viena no simts vienādām daļām.",
        "Pierakstu simtdaļas ar komatu: {1|100} = 0,01.",
        "Zinu, ka desmit simtdaļas ir viena desmitdaļa.",
        "Atrodu simtdaļas simta kvadrātā.",
    ]),

    Majas([
        "Uzzīmē simta kvadrātu un iekrāso tajā {1|4}.",
        "Pieraksti ar komatu {40|100} un {7|100}.",
        "Atrodi veikalā atlaidi un pasaki, cik simtdaļas tā ir.",
    ]),
]
