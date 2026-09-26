# -*- coding: utf-8 -*-
"""3. klase, 95. stunda: «Cik daļu vajag līdz veselam?»

Papildinājums līdz veselajam - tas pats, kas 84. stundā, bet tagad kā
patstāvīgs uzdevums ar dzīves situācijām. No šīs prasmes vēlāk aug gan
atņemšana no veselā, gan procentu papildinājums līdz simtam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Cik daļu vajag līdz veselam?"

MERKIS = ("Noteiksim, cik daļu pietrūkst līdz veselajam.")

SATURS = [
    Sakums("Cik vēl pietrūkst?",
           zimejums=dala(6, 4, "4/6, pietrūkst 2/6", "sešas vienādas daļas"),
           paraksts="Līdz veselajam pietrūkst tieši divu sestdaļu.",
           fakti=["Līdz veselajam vienmēr pietrūkst tik, cik saucējs mīnus "
                  "skaitītājs.",
                  "Abas daļas kopā dod {n|n} = 1."]),

    Doma("Atņem skaitītāju no saucēja",
         "Ja ir {4|6}, tad līdz veselajam pietrūkst {2|6}, jo 6 − 4 = 2.",
         soli=[
             "Paskaties uz saucēju - tik daļu ir veselajā.",
             "Atņem no tā skaitītāju.",
             "Rezultāts ir trūkstošo daļu skaits.",
             "Pieraksti to ar to pašu saucēju.",
         ],
         pieze="Pārbaudi ar saskaitīšanu: dotā daļa plus trūkstošā daļa "
               "vienmēr dod {n|n}, tas ir, vienu veselu."),

    Paraugs("Cik pietrūkst līdz veselajam?",
            uzd="Kūkas palikušas {4|6}. Cik daļu ir apēsts?",
            soli=[
                ("Saucējs ir 6",
                 "Kūka bija sadalīta sešās daļās."),
                ("6 − 4 = 2",
                 "Tik daļu vairs nav."),
                ("{4|6} + {2|6} = {6|6} = 1",
                 "Pārbaude: abas daļas kopā dod visu kūku."),
            ],
            atbilde="{2|6}"),

    Ievadi("Cik pietrūkst?", [
        {"jaut": "Ir {4|6}. Cik sestdaļu pietrūkst līdz veselajam?",
         "atb": ["2"], "padoms": "6 − 4."},
        {"jaut": "Ir {3|8}. Cik astotdaļu pietrūkst?", "atb": ["5"],
         "padoms": "8 − 3."},
        {"jaut": "Ir {7|10}. Cik desmitdaļu pietrūkst?", "atb": ["3"],
         "padoms": "10 − 7."},
        {"jaut": "Ir {1|5}. Cik piektdaļu pietrūkst?", "atb": ["4"],
         "padoms": "5 − 1."},
        {"jaut": "Ir {9|12}. Cik divpadsmitdaļu pietrūkst?", "atb": ["3"],
         "padoms": "12 − 9."},
        {"jaut": "Ir {2|3}. Cik trešdaļu pietrūkst?", "atb": ["1"],
         "padoms": "3 − 2."},
    ], pamats=4),

    Zimejums("Trūkstošā daļa",
             dala(10, 7, "7/10, pietrūkst 3/10", "desmit vienādas daļas"),
             paskaidro="Baltā daļa vienmēr ir tā, kas pietrūkst līdz "
                       "veselajam.",
             ievads="Iekrāsotas septiņas desmitdaļas."),

    Varianti("Cik pietrūkst?", [
        {"jaut": "Ir {5|9}. Cik pietrūkst līdz veselajam?",
         "opcijas": ["{4|9}", "{5|9}", "{9|5}", "{1|9}"],
         "pareizi": 0, "padoms": "9 − 5."},
        {"jaut": "Ir {1|2}. Cik pietrūkst līdz veselajam?",
         "opcijas": ["{1|2}", "{2|2}", "{1|4}", "Nekas"],
         "pareizi": 0, "padoms": "2 − 1."},
        {"jaut": "Ir {8|8}. Cik pietrūkst līdz veselajam?",
         "opcijas": ["Nekas", "{1|8}", "{8|8}", "{0|1}"],
         "pareizi": 0, "padoms": "Tas jau ir viens vesels."},
        {"jaut": "Ar ko pārbaudīt atbildi?",
         "opcijas": ["Saskaitot abas daļas", "Atņemot vēlreiz",
                     "Reizinot saucējus", "Nekā"],
         "pareizi": 0, "padoms": "Summai jābūt {n|n}."},
    ], pamats=4),

    Pasaule("Cik ligzdas vēl jāuzbūvē?",
            Ievadi("", [
                {"jaut": "Putns sagādājis {5|8} no ligzdas materiāla. Cik "
                         "astotdaļu vēl vajag?",
                 "atb": ["3"], "padoms": "8 − 5."},
                {"jaut": "Ligzdai vajag 40 zariņus. Cik zariņu ir viena "
                         "astotdaļa?",
                 "atb": ["5"], "padoms": "40 : 8."},
                {"jaut": "Cik zariņu putns jau sagādājis?", "atb": ["25"],
                 "padoms": "5 · 5."},
                {"jaut": "Cik zariņu vēl trūkst?", "atb": ["15"],
                 "padoms": "40 − 25."},
            ]),
            pavediens="daba",
            konteksts="Ligzdas būvē pakāpeniski, un putns vienmēr «zina», cik "
                      "daļas vēl trūkst.",
            kapec="Trūkstošā daļa pasaka, cik darba vēl priekšā."),

    Kopsavilkums([
        "Nosaku, cik daļu pietrūkst līdz veselajam.",
        "Atņemu skaitītāju no saucēja.",
        "Pārbaudu atbildi, saskaitot abas daļas.",
        "Pārrēķinu daļas arī skaitļos.",
    ]),

    Majas([
        "Izrēķini, cik pietrūkst līdz veselajam daļām {3|7}, {5|12} un "
        "{1|9}.",
        "Uzzīmē modeli vienai no tām.",
        "Atrodi mājās kaut ko, kas vēl nav pabeigts, un nosauc trūkstošo "
        "daļu.",
    ]),
]
