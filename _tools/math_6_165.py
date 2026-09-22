# -*- coding: utf-8 -*-
"""6. klase, 165. stunda: «Kā apvienot procentus un daļas?»

Uzdevumi, kuros vienā tekstā satiekas abi pieraksti. Grūtākais nav rēķins,
bet jautājums, no kā katra daļa ir ņemta - no visa kopuma vai no atlikuma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā apvienot procentus un daļas?"

MERKIS = ("Risināsim uzdevumus, kuros vienlaikus lietoti procenti un daļas.")

SATURS = [
    Sakums("No kā ņemta otrā daļa?",
           zimejums=dala(10, 6, "vispirms 60 %"),
           paraksts="Ja no atlikušajiem 40 % ņem pusi, tas ir 20 % no visa - "
                    "nevis 50 %.",
           fakti=["Otrais procents parasti ir no atlikuma.",
                  "Daļu no daļas rēķina ar reizināšanu.",
                  "Vienmēr pieraksta, no kā katra daļa ņemta."]),

    Doma("Katrai daļai pieraksti, no kā tā ir",
         "Uzdevumos ar diviem soļiem katrai daļai jānosaka kopums: visa "
         "summa vai atlikums pēc pirmā soļa.",
         soli=[
             "Izlasi tekstu un atrodi pirmo daļu.",
             "Aprēķini to un pieraksti atlikumu.",
             "Noskaidro, no kā ņemta otrā daļa.",
             "Aprēķini to no pareizā kopuma.",
             "Pārbaudi: visu daļu summa ir sākotnējais kopums.",
         ],
         pieze="Vārdi «no tiem», «no atlikuma», «no pārējiem» vienmēr norāda "
               "uz iepriekšējo grupu, nevis uz visu kopumu. Tas ir viens "
               "vārds, kas maina visu atbildi."),

    Paraugs("Divi soļi pēc kārtas",
            uzd="Klasē 30 skolēni. 60 % apmeklē pulciņus, no atlikušajiem "
                "puse spēlē sportu. Cik skolēnu spēlē sportu?",
            soli=[
                ("60 % no 30 = 18",
                 "Apmeklē pulciņus."),
                ("30 − 18 = 12",
                 "Atlikums."),
                ("Puse no 12 = 6",
                 "No atlikuma, ne no 30."),
                ("6 no 30 ir 20 %",
                 "Tikai piektā daļa no visas klases."),
            ],
            atbilde="6 skolēni"),

    Ievadi("Rēķini pa soļiem", [
        {"jaut": "Klasē 30 skolēni, 60 % apmeklē pulciņus. Cik tas ir?",
         "atb": ["18"], "padoms": "30 · 0,6."},
        {"jaut": "Cik skolēnu ir atlikumā?",
         "atb": ["12"], "padoms": "30 − 18."},
        {"jaut": "Puse no atlikuma spēlē sportu. Cik tas ir?",
         "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "Cik procenti no visas klases tas ir?",
         "atb": ["20"], "padoms": "{6|30}."},
        {"jaut": "Ir 80 €, iztērē 25 %, tad {1|3} no atlikuma. Cik eiro ir "
                 "atlikums pēc pirmā soļa?",
         "atb": ["60"], "padoms": "80 − 20."},
        {"jaut": "Cik eiro iztērē otrajā solī?",
         "atb": ["20"], "padoms": "60 : 3."},
    ], pamats=4,
        ievads="Katrai daļai pasaki, no kā tā ir ņemta."),

    Varianti("No kā ņemta daļa?", [
        {"jaut": "«No atlikušajiem puse» nozīmē pusi no...",
         "opcijas": ["atlikuma", "visa kopuma",
                     "pirmās daļas", "puses"],
         "pareizi": 0,
         "padoms": "Vārds «atlikušajiem»."},
        {"jaut": "60 % no 30 ir...",
         "opcijas": ["18", "12", "20", "6"],
         "pareizi": 0,
         "padoms": "30 · 0,6."},
        {"jaut": "Puse no 12 ir cik procentu no 30?",
         "opcijas": ["20", "50", "6", "40"],
         "pareizi": 0,
         "padoms": "{6|30}."},
        {"jaut": "Kurš vārds norāda, ka daļa ir no atlikuma?",
         "opcijas": ["«no tiem»", "«kopā»", "«visi»", "«pavisam»"],
         "pareizi": 0,
         "padoms": "Norāde uz iepriekšējo grupu."},
    ], pamats=4),

    Pasaule("Cik palika no summas?",
            Ievadi("", [
                {"jaut": "Bija 200 €. Iztērēja 30 %. Cik eiro palika?",
                 "atb": ["140"], "padoms": "200 − 60."},
                {"jaut": "No atlikuma iztērēja {1|4}. Cik eiro tas ir?",
                 "atb": ["35"], "padoms": "140 : 4."},
                {"jaut": "Cik eiro palika beigās?",
                 "atb": ["105"], "padoms": "140 − 35."},
                {"jaut": "Cik procenti no sākotnējiem 200 € tas ir? Noapaļo "
                         "līdz veselam.",
                 "atb": ["53", "52"], "padoms": "{105|200}."},
            ]),
            pavediens="veikals",
            konteksts="Divas atlaides pēc kārtas nav tas pats, kas viena "
                      "liela - otrā ir no jau samazinātas cenas.",
            kapec="Kopums mainās pēc katra soļa."),

    Kopsavilkums([
        "Risinu uzdevumus ar procentiem un daļām vienlaikus.",
        "Katrai daļai nosaku, no kā tā ir ņemta.",
        "Pārrēķinu atlikumu pēc katra soļa.",
        "Pārbaudu, vai visu daļu summa ir sākotnējais kopums.",
    ]),

    Majas([
        "Ir 120 €. Iztērē 25 %, tad {1|3} no atlikuma. Cik palika?",
        "Pieraksti, no kā katra daļa bija ņemta.",
        "Izrēķini, cik procenti no sākuma palika.",
    ]),
]
