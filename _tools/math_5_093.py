# -*- coding: utf-8 -*-
"""5. klase, 93. stunda: «Kā jauktu skaitli pārvērst neīstā daļā?»

Pretējais virziens, un tas ir tikai viens rēķins: veselo reizina ar saucēju
un pieskaita skaitītāju. Bet tieši šis virziens vēlāk ir vajadzīgs biežāk -
bez tā nevar ne atņemt, ne reizināt jauktus skaitļus. Tāpēc stundas beigās
vienmēr ir pārbaude: no iegūtās daļas atgriežas atpakaļ.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā jauktu skaitli pārvērst neīstā daļā?"

MERKIS = ("Iemācīsimies pārveidot jauktu skaitli par neīstu daļu un "
          "pārbaudīt rezultātu.")

SATURS = [
    Sakums("Cik ceturtdaļu ir 2{3|4}?",
           zimejums=restis([["2 3/4", "11/4"]],
                           virsraksts="Viens skaitlis, divi pieraksti"),
           paraksts="Divos veselos ir 8 ceturtdaļas, un vēl 3 klāt - kopā 11.",
           fakti=["Katrā veselā ir tik ceturtdaļu, cik rāda saucējs.",
                  "Divos veselos to ir divreiz vairāk.",
                  "Pēc tam pieskaita jau esošo skaitītāju."]),

    Doma("Reizini veselo ar saucēju un pieskaiti skaitītāju",
         "Jauktu skaitli pārvērš neīstā daļā, veselo reizinot ar saucēju un "
         "pieskaitot skaitītāju; saucējs paliek tas pats.",
         soli=[
             "Reizini veselo daļu ar saucēju.",
             "Pieskaiti reizinājumam skaitītāju.",
             "Iegūto summu raksti skaitītājā.",
             "Saucēju atstāj neskartu.",
             "Pārbaudi: izdali skaitītāju ar saucēju un atgriezies atpakaļ.",
         ],
         pieze="2{3|4} = {2 · 4 + 3|4} = {11|4}. Viss rēķins ir vienā rindā, "
               "un tieši tāpēc šo pieraksta veidu ir vērts iemācīties "
               "no galvas."),

    Paraugs("Pārvērt 2{3|4} par neīstu daļu",
            uzd="Pieraksti jaukto skaitli 2{3|4} kā neīstu daļu.",
            soli=[
                ("2 · 4 = 8",
                 "Cik ceturtdaļu ir divos veselos."),
                ("8 + 3 = 11",
                 "Pieskaita esošo skaitītāju."),
                ("{11|4}",
                 "Saucējs paliek 4."),
                ("Pārbaude: 11 : 4 = 2, atl. 3",
                 "Atgriežamies pie 2{3|4}."),
            ],
            atbilde="2{3|4} = {11|4}"),

    Ievadi("Pārvērt neīstā daļā", [
        {"jaut": "2{3|4} kā neīsta daļa. Atbildi raksti kā a/b.",
         "atb": ["11/4"], "padoms": "2 · 4 + 3."},
        {"jaut": "3{1|2} kā neīsta daļa. Atbildi raksti kā a/b.",
         "atb": ["7/2"], "padoms": "3 · 2 + 1."},
        {"jaut": "1{4|5} kā neīsta daļa. Atbildi raksti kā a/b.",
         "atb": ["9/5"], "padoms": "1 · 5 + 4."},
        {"jaut": "5{2|3} kā neīsta daļa. Atbildi raksti kā a/b.",
         "atb": ["17/3"], "padoms": "5 · 3 + 2."},
        {"jaut": "2{1|6} kā neīsta daļa. Atbildi raksti kā a/b.",
         "atb": ["13/6"], "padoms": "2 · 6 + 1."},
        {"jaut": "4{3|8} kā neīsta daļa. Atbildi raksti kā a/b.",
         "atb": ["35/8"], "padoms": "4 · 8 + 3."},
        {"jaut": "3 kā daļa ar saucēju 4. Atbildi raksti kā a/b.",
         "atb": ["12/4"], "padoms": "3 · 4."},
        {"jaut": "1{1|2} kā neīsta daļa. Atbildi raksti kā a/b.",
         "atb": ["3/2"], "padoms": "1 · 2 + 1."},
    ], pamats=4,
        ievads="Reizini, pieskaiti, saucēju atstāj - trīs soļi vienā rindā."),

    Zimejums("Abi virzieni blakus",
             restis([["2 3/4", "11/4"],
                     ["3 1/2", "7/2"]],
                    virsraksts="Pa kreisi jaukts, pa labi neīsta daļa"),
             paskaidro="Uz labo pusi reizina un pieskaita, uz kreiso dala ar "
                       "atlikumu. Skaitlis abās pusēs ir viens un tas pats.",
             ievads="Iepriekšējā stunda gāja pa kreisi, šī iet pa labi."),

    Varianti("Kāds rēķins ir skaitītājā?", [
        {"jaut": "Kā iegūst neīstās daļas skaitītāju?",
         "opcijas": ["Veselo reizina ar saucēju un pieskaita skaitītāju",
                     "Veselo pieskaita skaitītājam",
                     "Veselo reizina ar skaitītāju",
                     "Saucēju reizina ar skaitītāju"],
         "pareizi": 0,
         "padoms": "Vispirms reizina, tad pieskaita."},
        {"jaut": "3{1|2} kā neīsta daļa ir...",
         "opcijas": ["{7|2}", "{4|2}", "{6|2}", "{3|2}"],
         "pareizi": 0,
         "padoms": "3 · 2 + 1."},
        {"jaut": "Kas notiek ar saucēju?",
         "opcijas": ["Paliek tas pats", "Reizinās ar veselo",
                     "Pieskaitās", "Pazūd"],
         "pareizi": 0,
         "padoms": "Gabalu lielums nemainās."},
        {"jaut": "Skolēns raksta 2{3|4} = {5|4}. Kur ir kļūda?",
         "opcijas": ["Veselais nav reizināts ar saucēju",
                     "Skaitītājs nav pieskaitīts",
                     "Saucējs ir nepareizs",
                     "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "2 + 3 nav 2 · 4 + 3."},
        {"jaut": "Kā pārbaudīt rezultātu?",
         "opcijas": ["Izdalīt skaitītāju ar saucēju",
                     "Saskaitīt abus locekļus",
                     "Saīsināt daļu",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Jāiegūst sākotnējais jauktais skaitlis."},
        {"jaut": "Kāpēc šis virziens ir vajadzīgs biežāk?",
         "opcijas": ["Ar neīstām daļām ir vieglāk rēķināt",
                     "Tas ir ātrāks",
                     "Tas ir vienīgais pareizais",
                     "Tas nav vajadzīgs biežāk"],
         "pareizi": 0,
         "padoms": "Atņemot un reizinot veselais traucē."},
    ], pamats=4),

    Pasaule("Cik ceturtdaļglāžu ir receptē?",
            Ievadi("", [
                {"jaut": "Receptē 2{3|4} glāzes. Cik tas ir ceturtdaļglāžu?",
                 "atb": ["11"], "padoms": "2 · 4 + 3."},
                {"jaut": "Receptē 3{1|2} glāzes. Cik tas ir pusglāžu?",
                 "atb": ["7"], "padoms": "3 · 2 + 1."},
                {"jaut": "Receptē 1{2|3} glāzes. Cik tas ir trešdaļglāžu?",
                 "atb": ["5"], "padoms": "1 · 3 + 2."},
                {"jaut": "Receptē 2{1|8} glāzes. Cik tas ir astotdaļglāžu?",
                 "atb": ["17"], "padoms": "2 · 8 + 1."},
            ]),
            pavediens="virtuve",
            konteksts="Ja mērglāzei ir tikai ceturtdaļu iedaļas, jāzina, cik "
                      "reižu to piepildīt.",
            kapec="Neīsta daļa pasaka tieši to - cik mazo mēru vajag."),

    Kopsavilkums([
        "Pārveidoju jauktu skaitli par neīstu daļu.",
        "Reizinu veselo ar saucēju un pieskaitu skaitītāju.",
        "Atstāju saucēju nemainīgu.",
        "Pārbaudu rezultātu, pārveidojot to atpakaļ.",
    ]),

    Majas([
        "Pārvērt neīstās daļās 3{2|5}, 4{1|3} un 2{5|6}.",
        "Pārbaudi katru atbildi, pārveidojot to atpakaļ.",
        "Uzraksti, kurš virziens tev šķiet vieglāks un kāpēc.",
    ]),
]
