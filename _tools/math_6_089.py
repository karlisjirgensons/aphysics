# -*- coding: utf-8 -*-
"""6. klase, 89. stunda: «Kā izplānot telpas iekārtošanu?»

Stunda, kurā satiekas divi temati: attiecība no gada sākuma un procenti no
šī temata. Laukumu sadala procentos, bet materiālu - attiecībā, un abi
rezultāti jāsaskaņo vienā plānā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā izplānot telpas iekārtošanu?"

MERKIS = ("Plānosim dārza vai sporta laukuma iekārtošanu, lietojot attiecību "
          "un procentus.")

SATURS = [
    Sakums("Plānā vispirms procenti, tad metri",
           zimejums=restis([["dobes", "celiņi", "zāliens"],
                            ["50 %", "20 %", "30 %"]]),
           paraksts="Kopā vienmēr 100 %. Tikai pēc tam procentus pārvērš "
                    "kvadrātmetros.",
           fakti=["Plānojot vispirms sadala procentos - tā vieglāk mainīt.",
                  "Procentu summa ir 100 %, arī tad, ja daļu ir daudz.",
                  "Metros pārvērš pašās beigās."]),

    Doma("Sadali procentos, tad pārvērt metros",
         "Telpu plāno divos soļos: vispirms sadala laukumu procentos, tad "
         "katru procentu daļu pārvērš kvadrātmetros.",
         soli=[
             "Aprēķini visu laukumu.",
             "Sadali to procentos pa zonām; summai jābūt 100 %.",
             "Atrodi 1 % no laukuma.",
             "Aprēķini katras zonas laukumu kvadrātmetros.",
             "Pārbaudi: zonu summa ir viss laukums.",
         ],
         pieze="Ja plānā parādās attiecība - piemēram, dobes pret celiņiem "
               "5 : 2 -, to vispirms pārvērš procentos: 5 no 7 daļām ir "
               "apmēram 71 %, bet 2 no 7 - apmēram 29 %."),

    Paraugs("Sadali dārzu",
            uzd="Dārzs ir 20 m x 15 m. Dobēm atvēl 50 %, celiņiem 20 %, "
                "zālienam pārējo. Cik kvadrātmetru ir katrai zonai?",
            soli=[
                ("Laukums: 20 · 15 = 300 m²",
                 "Viss dārzs."),
                ("1 % ir 3 m²",
                 "300 : 100."),
                ("Dobes: 50 · 3 = 150 m²",
                 "Puse."),
                ("Celiņi: 20 · 3 = 60 m²",
                 "Piektdaļa."),
                ("Zāliens: 30 · 3 = 90 m²",
                 "100 − 50 − 20 = 30 %."),
            ],
            atbilde="150 m², 60 m² un 90 m²"),

    Ievadi("Sadali laukumu", [
        {"jaut": "Dārzs 20 m x 15 m. Cik m² ir laukums?",
         "atb": ["300"], "padoms": "20 · 15."},
        {"jaut": "Cik m² ir 1 %?",
         "atb": ["3"], "padoms": "300 : 100."},
        {"jaut": "Dobēm atvēl 50 %. Cik m² tas ir?",
         "atb": ["150"], "padoms": "50 · 3."},
        {"jaut": "Celiņiem atvēl 20 %. Cik m² tas ir?",
         "atb": ["60"], "padoms": "20 · 3."},
        {"jaut": "Cik procentu paliek zālienam?",
         "atb": ["30"], "padoms": "100 − 50 − 20."},
        {"jaut": "Cik m² ir zālienam?",
         "atb": ["90"], "padoms": "30 · 3."},
    ], pamats=4),

    Varianti("Vai plāns saiet kopā?", [
        {"jaut": "Zonu procentu summai jābūt...",
         "opcijas": ["100 %", "50 %", "200 %", "jebkādai"],
         "pareizi": 0,
         "padoms": "Viss laukums ir kopums."},
        {"jaut": "Attiecība 3 : 1 procentos ir...",
         "opcijas": ["75 % un 25 %", "30 % un 10 %",
                     "3 % un 1 %", "60 % un 40 %"],
         "pareizi": 0,
         "padoms": "4 daļas; viena daļa ir 25 %."},
        {"jaut": "Laukums 400 m², vienai zonai 35 %. Cik m² tas ir?",
         "opcijas": ["140", "35", "400", "114"],
         "pareizi": 0,
         "padoms": "1 % ir 4 m²."},
        {"jaut": "Kāpēc plāno vispirms procentos?",
         "opcijas": ["Jo tad plānu var pielietot jebkuram laukumam",
                     "Jo procenti ir vieglāki",
                     "Jo metros nevar plānot", "Nav iemesla"],
         "pareizi": 0,
         "padoms": "Procenti nav piesaistīti izmēram."},
    ], pamats=4),

    Petijums("Izplāno klases sporta laukumu",
             vajag="rūtiņu lapa, lineālis, mērlente",
             soli=[
                 "Izmēriet laukuma garumu un platumu un aprēķiniet laukumu.",
                 "Sadaliet to procentos: spēļu zona, skrejceļš, soliņi.",
                 "Pārbaudiet, vai procentu summa ir 100 %.",
                 "Pārrēķiniet katru zonu kvadrātmetros.",
                 "Uzzīmējiet plānu mērogā 1 : 200.",
             ],
             secinajums="Plāns ir pareizs tad, ja zonu laukumu summa sakrīt "
                        "ar visu laukumu - tā ir vienīgā pārbaude."),

    Pasaule("Cik materiāla vajag zonām?",
            Ievadi("", [
                {"jaut": "Celiņiem 60 m², vienam kvadrātmetram vajag 25 kg "
                         "grants. Cik kg?",
                 "atb": ["1500", "1 500"], "padoms": "60 · 25."},
                {"jaut": "Zālienam 90 m², sēklas 30 g uz kvadrātmetru. Cik "
                         "gramu sēklu?",
                 "atb": ["2700", "2 700"], "padoms": "90 · 30."},
                {"jaut": "Cik kilogramu sēklu tas ir?",
                 "atb": ["2,7", "2.7"], "padoms": "2700 : 1000."},
                {"jaut": "Dobēm 150 m², kūdra 20 l uz kvadrātmetru. Cik "
                         "litru kūdras?",
                 "atb": ["3000", "3 000"], "padoms": "150 · 20."},
            ]),
            pavediens="skola",
            konteksts="Skolas dārza plāns beidzas ar iepirkumu sarakstu - "
                      "un tas nāk tieši no zonu laukumiem.",
            kapec="Procenti sadala laukumu, laukums nosaka materiālu."),

    Zimejums("Plāns procentos",
             restis([["dobes 50 %", "celiņi 20 %", "zāliens 30 %"],
                     ["150 m²", "60 m²", "90 m²"]]),
             paskaidro="Augšējā rinda ir plāns, apakšējā - tā pati "
                       "informācija kvadrātmetros.",
             ievads="Viens plāns, divi pieraksti."),

    Kopsavilkums([
        "Sadalu laukumu procentos un pārbaudu, vai summa ir 100 %.",
        "Pārvēršu procentus kvadrātmetros.",
        "Pārvēršu attiecību procentos, ja plāns to prasa.",
        "Aprēķinu materiāla daudzumu no zonas laukuma.",
    ]),

    Majas([
        "Sadali savas istabas grīdu procentos pa zonām.",
        "Pārrēķini katru zonu kvadrātmetros.",
        "Pieraksti, kura zona aizņem visvairāk vietas.",
    ]),
]
