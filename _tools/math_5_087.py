# -*- coding: utf-8 -*-
"""5. klase, 87. stunda: «Cik bieži uzkrīt ģerbonis?»

Pirmā stunda par gadījuma notikumiem, un tā ir eksperimenta stunda. Skolēns
met monētu, skaita rezultātus un pieraksta biežumu kā daļu - tieši to pašu
daļu, ko veidoja iepriekšējās stundās. Jaunais ir tas, ka atbilde katrai
grupai iznāk citāda, un tas nav kļūda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kolonnas)

TEMA = "Cik bieži uzkrīt ģerbonis?"

MERKIS = ("Mācīsimies modelēt vienādi iespējamus notikumus, apkopot datus un "
          "raksturot biežumu ar daļu.")

SATURS = [
    Sakums("Divdesmit metieni, divi iznākumi",
           zimejums=kolonnas([("Ģerbonis", 12), ("Cipars", 8)]),
           paraksts="No 20 metieniem ģerbonis uzkrita 12 reizes: {12|20} = "
                    "{3|5}.",
           fakti=["Monētai ir divas puses, un abas ir vienādi iespējamas.",
                  "Tomēr 20 metienos reti iznāk tieši 10 un 10.",
                  "Biežumu pieraksta kā daļu no visiem metieniem."]),

    Doma("Biežums ir daļa no mēģinājumiem",
         "Notikuma biežumu izsaka kā daļu: cik reižu notikums notika pār to, "
         "cik reižu mēģinājums tika izdarīts.",
         soli=[
             "Saskaiti, cik mēģinājumu bija pavisam - tas ir saucējs.",
             "Saskaiti, cik reižu notikums notika - tas ir skaitītājs.",
             "Uzraksti daļu un saīsini to.",
             "Salīdzini biežumu ar {1|2}, ja iznākumi ir vienādi iespējami.",
             "Pieraksti secinājumu vārdiem.",
         ],
         pieze="Vienādi iespējami nenozīmē vienādi bieži. Divdesmit metienos "
               "ģerbonis var uzkrist 12 reizes, bet simt metienos attiecība "
               "parasti pietuvojas pusei."),

    Petijums("Met monētu divdesmit reizes",
             soli=["Uzraksti tabulu ar divām ailēm: ģerbonis un cipars.",
                   "Met monētu 20 reizes un atzīmē katru rezultātu.",
                   "Saskaiti, cik reižu uzkrita ģerbonis.",
                   "Pieraksti biežumu kā daļu no 20 un saīsini to.",
                   "Salīdzini savu daļu ar kaimiņa daļu."],
             vajag="monēta, burtnīca, zīmulis",
             secinajums="Daļas atšķiras, bet visas ir tuvu {1|2} - jo vairāk "
                        "metienu, jo tuvāk."),

    Paraugs("No 20 metieniem 12 ģerboņi",
            uzd="Pieraksti ģerboņa biežumu kā daļu un salīdzini to ar pusi.",
            soli=[
                ("Mēģinājumu skaits ir 20",
                 "Saucējs."),
                ("Ģerbonis uzkrita 12 reizes",
                 "Skaitītājs."),
                ("{12|20} = {3|5}",
                 "Abus locekļus dala ar 4."),
                ("{3|5} = {6|10}, {1|2} = {5|10}",
                 "Ar kopsaucēju 10."),
                ("{3|5} > {1|2}",
                 "Ģerbonis uzkrita biežāk nekā puse reižu."),
            ],
            atbilde="Biežums ir {3|5}, tas ir vairāk nekā puse"),

    Ievadi("Pieraksti biežumu", [
        {"jaut": "No 20 metieniem 12 ģerboņi. Kāds biežums? Atbildi raksti "
                 "kā a/b.",
         "atb": ["3/5", "12/20"], "padoms": "Abus dala ar 4."},
        {"jaut": "No 20 metieniem 8 cipari. Kāds biežums? Atbildi raksti kā "
                 "a/b.",
         "atb": ["2/5", "8/20"], "padoms": "Abus dala ar 4."},
        {"jaut": "No 30 metieniem 15 ģerboņi. Kāds biežums? Atbildi raksti "
                 "kā a/b.",
         "atb": ["1/2", "15/30"], "padoms": "Tieši puse."},
        {"jaut": "No 24 metieniem 18 ģerboņi. Kāds biežums? Atbildi raksti "
                 "kā a/b.",
         "atb": ["3/4", "18/24"], "padoms": "Abus dala ar 6."},
        {"jaut": "No 50 metieniem 20 ģerboņi. Kāds biežums? Atbildi raksti "
                 "kā a/b.",
         "atb": ["2/5", "20/50"], "padoms": "Abus dala ar 10."},
        {"jaut": "No 40 metieniem 24 ģerboņi. Kāds biežums? Atbildi raksti "
                 "kā a/b.",
         "atb": ["3/5", "24/40"], "padoms": "Abus dala ar 8."},
        {"jaut": "No 20 metieniem 12 ģerboņi. Cik reižu uzkrita cipars?",
         "atb": ["8"], "padoms": "20 - 12."},
        {"jaut": "No 100 metieniem 48 ģerboņi. Cik reižu uzkrita cipars?",
         "atb": ["52"], "padoms": "100 - 48."},
    ], pamats=4,
        ievads="Skaitītājā - cik reižu notika, saucējā - cik reižu mēģināja."),

    Zimejums("Divas ailes pēc divdesmit metieniem",
             kolonnas([("Ģerbonis", 12), ("Cipars", 8)]),
             paskaidro="Stabiņi nav vienādi, kaut abas puses ir vienādi "
                       "iespējamas. Tā notiek katrā īsā mēģinājumu virknē.",
             ievads="Dati no viena eksperimenta izskatās tieši šādi."),

    Varianti("Ko pasaka biežums?", [
        {"jaut": "Kurš skaitlis ir saucējā?",
         "opcijas": ["Visu mēģinājumu skaits", "Notikumu skaits",
                     "Monētas pušu skaits", "Skolēnu skaits"],
         "pareizi": 0,
         "padoms": "Saucējs ir veselais."},
        {"jaut": "Vai 20 metienos ģerbonim jāuzkrīt tieši 10 reizes?",
         "opcijas": ["Nē, biežums var atšķirties", "Jā, vienmēr",
                     "Jā, ja monēta ir laba", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Vienādi iespējami nav vienādi bieži."},
        {"jaut": "Biežums iznāca {12|20}. Saīsinātā veidā tas ir...",
         "opcijas": ["{3|5}", "{6|10} nesaīsināts", "{1|2}", "{5|3}"],
         "pareizi": 0,
         "padoms": "Abus dala ar 4."},
        {"jaut": "Kas notiek ar biežumu, palielinot metienu skaitu?",
         "opcijas": ["Tas tuvojas pusei", "Tas kļūst lielāks",
                     "Tas kļūst mazāks", "Tas nemainās"],
         "pareizi": 0,
         "padoms": "Garā virknē puses izlīdzinās."},
        {"jaut": "No 20 metieniem 12 ģerboņi. Cik ir cipara biežums?",
         "opcijas": ["{2|5}", "{3|5}", "{1|2}", "{8|12}"],
         "pareizi": 0,
         "padoms": "{8|20}."},
        {"jaut": "Abu biežumu summa vienmēr ir...",
         "opcijas": ["1", "{1|2}", "0", "2"],
         "pareizi": 0,
         "padoms": "Visi mēģinājumi kopā."},
    ], pamats=4),

    Pasaule("Kurš sāk spēli?",
            Ievadi("", [
                {"jaut": "Klasē metiens izšķir, kurš sāk. No 16 spēlēm "
                         "8. klases komanda sāka 10 reizes. Kāds biežums? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["5/8", "10/16"], "padoms": "Abus dala ar 2."},
                {"jaut": "Cik reižu sāka otra komanda?",
                 "atb": ["6"], "padoms": "16 - 10."},
                {"jaut": "Kāds ir otras komandas biežums? Atbildi raksti kā "
                         "a/b.",
                 "atb": ["3/8", "6/16"], "padoms": "{6|16}."},
                {"jaut": "Nākamajās 20 spēlēs katra sāka 10 reizes. Kāds "
                         "biežums? Atbildi raksti kā a/b.",
                 "atb": ["1/2", "10/20"], "padoms": "Tieši puse."},
            ]),
            pavediens="skola",
            konteksts="Spēles sākumu izlozē ar monētu, un klasē uzreiz sāk "
                      "strīdēties, vai tas ir godīgi.",
            kapec="Biežums parāda, ka īsā virknē nelīdzsvars ir parasts."),

    Kopsavilkums([
        "Modelēju vienādi iespējamus notikumus ar monētu.",
        "Apkopoju eksperimenta datus tabulā.",
        "Pierakstu notikuma biežumu kā daļu un saīsinu to.",
        "Zinu, ka vienādi iespējami notikumi īsā virknē nav vienādi bieži.",
    ]),

    Majas([
        "Met monētu 50 reizes un pieraksti ģerboņa biežumu kā daļu.",
        "Salīdzini savu rezultātu ar {1|2}.",
        "Uzraksti, kas notiktu, ja metienu būtu 1000.",
    ]),
]
