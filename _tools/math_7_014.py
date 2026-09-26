# -*- coding: utf-8 -*-
"""7. klase, 14. stunda: «Kā varbūtību noteikt ar eksperimentu?»

Relatīvais biežums ir notikuma reižu skaits, dalīts ar mēģinājumu skaitu.
Ar maz metieniem tas lēkā, ar daudz metieniem - nostabilizējas. Lapa
izmet kauliņu simtiem reižu, un skolēns redz, kā biežums tuvojas {1|6}.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Simulacija, Varianti)

TEMA = "Kā varbūtību noteikt ar eksperimentu?"

MERKIS = ("Iemācīsimies aprēķināt relatīvo biežumu un salīdzināt to ar "
          "prognozi.")

SATURS = [
    Sakums("Vai kauliņš ir godīgs?",
           fakti=["Kazino kauliņus pārbauda tūkstošiem metienu.",
                  "Godīgam kauliņam sešinieks krīt apmēram katrā sestajā.",
                  "Ar 10 metieniem to vēl nevar pateikt, ar 1000 - var."]),

    Doma("Relatīvais biežums = notika : mēģinājumi",
         "Ja notikums eksperimentā notika m reizes no n mēģinājumiem, tad tā "
         "relatīvais biežums ir {m|n}. Jo vairāk mēģinājumu, jo tuvāk tas "
         "parasti ir varbūtībai.",
         soli=[
             "Izdari eksperimentu daudz reižu un pieraksti rezultātus.",
             "Saskaiti, cik reizes notikums notika (m).",
             "Izdali ar visu mēģinājumu skaitu (n).",
             "Salīdzini ar prognozi.",
         ],
         pieze="Ar maz mēģinājumiem biežums var būt tālu no varbūtības - tā "
               "nav kļūda, tā ir nejaušība."),

    Simulacija("Met kauliņu", ["1", "2", "3", "4", "5", "6"], [5],
               "uzkrīt sešinieks", teorija="{1|6} ≈ 0,17",
               ievads="Spied «10 reizes» dažas reizes, tad «100 reizes». "
                      "Vēro, kā mainās biežums."),

    Paraugs("Aprēķini biežumu",
            uzd="Monētu meta 50 reizes, ģerbonis uzkrita 27 reizes. Kāds ir "
                "ģerboņa relatīvais biežums?",
            soli=[
                ("{m|n} = {27|50}", "Notika : mēģinājumi."),
                ("{27|50} = {54|100} = 0,54", "Paplašina līdz 100."),
                ("0,54 = 54 %", "Procentos."),
                ("Prognoze 0,5 - biežums ir tuvu", "Monēta šķiet godīga."),
            ],
            atbilde="0,54 jeb 54 %"),

    Ievadi("Aprēķini relatīvo biežumu", [
        {"jaut": "No 40 metieniem sešinieks krita 8 reizes. Biežums "
                 "decimāldaļā?",
         "atb": ["0,2"], "padoms": "8 : 40."},
        {"jaut": "No 200 izgatavotām detaļām 6 bija brāķis. Brāķa biežums "
                 "procentos (tikai skaitli)?",
         "atb": ["3"], "padoms": "6 : 200 = 0,03."},
        {"jaut": "Basketbolists no 25 soda metieniem trāpīja 20. Biežums "
                 "decimāldaļā?",
         "atb": ["0,8"], "padoms": "20 : 25."},
        {"jaut": "Biežums ir 0,3, mēģinājumu bija 60. Cik reizes notika "
                 "notikums?",
         "atb": ["18"], "padoms": "0,3 · 60."},
        {"jaut": "Pogu meta 100 reizes, uz malas tā nostājās 12 reizes. "
                 "Biežums procentos (tikai skaitli)?",
         "atb": ["12"], "padoms": "12 no 100."},
        {"jaut": "Biežums 0,25, notikums notika 15 reizes. Cik bija "
                 "mēģinājumu?",
         "atb": ["60"], "padoms": "15 : 0,25."},
    ], pamats=4),

    Varianti("Ko rāda eksperiments?", [
        {"jaut": "10 metienos sešinieks krita 4 reizes. Ko var secināt?",
         "opcijas": ["Pārāk maz metienu, lai spriestu",
                     "Kauliņš noteikti ir negodīgs",
                     "Varbūtība ir 0,4",
                     "Sešinieks krīt biežāk par citiem"],
         "pareizi": 0,
         "padoms": "Ar 10 metieniem nejaušība ir liela."},
        {"jaut": "Kad biežums visticamāk ir tuvāk varbūtībai?",
         "opcijas": ["Pēc 1000 metieniem", "Pēc 10 metieniem",
                     "Pēc 1 metiena", "Vienmēr vienādi"],
         "pareizi": 0,
         "padoms": "Lielo skaitļu likums."},
        {"jaut": "Pogai, kas var nokrist uz vienas vai otras puses vai uz "
                 "malas, varbūtību var noteikt...",
         "opcijas": ["tikai ar eksperimentu", "ar formulu {1|3}",
                     "ar formulu {1|2}", "nevar noteikt"],
         "pareizi": 0,
         "padoms": "Iznākumi nav vienādi iespējami."},
    ]),

    Petijums("Pogas eksperiments",
             ["Paņem pogu vai pudeles korķi.",
              "Met to 30 reizes un pieraksti: ar virspusi uz augšu vai uz "
              "leju.",
              "Aprēķini relatīvo biežumu pēc 10, 20 un 30 metieniem.",
              "Apvieno klases rezultātus un aprēķini biežumu no visiem "
              "metieniem."],
             vajag="poga vai korķis, tabula pierakstam",
             secinajums="Klases kopējais biežums ir labākais varbūtības "
                        "novērtējums, jo mēģinājumu ir visvairāk."),

    Pasaule("Soda sitieni",
            Ievadi("", [
                {"jaut": "Vārtsargs sezonā atvairīja 9 soda sitienus no "
                         "36. Kāds ir atvairīšanas biežums procentos "
                         "(tikai skaitli)?",
                 "atb": ["25"], "padoms": "9 : 36 = 0,25."},
                {"jaut": "Cik no nākamajiem 12 soda sitieniem viņš, "
                         "visticamāk, atvairīs?",
                 "atb": ["3"], "padoms": "0,25 · 12."},
                {"jaut": "Cits vārtsargs atvairīja 6 no 20. Kura biežums "
                         "ir lielāks - «pirmā» vai «otrā»?",
                 "atb": ["otrā", "otra", "otrais"],
                 "padoms": "6 : 20 = 0,3 > 0,25."},
            ]),
            pavediens="sports",
            konteksts="Treneri pirms soda sitiena skatās statistiku - tā ir "
                      "eksperimentāli iegūta varbūtība.",
            kapec="Salīdzina biežumus, nevis reižu skaitu."),

    Kopsavilkums([
        "Aprēķinu relatīvo biežumu {m|n}.",
        "Zinu, ka ar vairāk mēģinājumiem biežums tuvojas varbūtībai.",
        "Salīdzinu eksperimenta rezultātu ar prognozi.",
        "Zinu, kad varbūtību var noteikt tikai ar eksperimentu.",
    ]),

    Majas([
        "Met monētu 50 reizes un aprēķini ģerboņa biežumu.",
        "Atrodi sava mīļākā sportista trāpījumu biežumu.",
        "Salīdzini savu rezultātu ar lapas simulāciju.",
    ]),
]
