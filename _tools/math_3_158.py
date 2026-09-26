# -*- coding: utf-8 -*-
"""3. klase, 158. stunda: «Cik skaldņu, šķautņu un virsotņu?»

Trīs jēdzieni, kurus skolēns tagad lieto pats: skaldne ir plakne, šķautne ir
līnija, virsotne ir punkts. Skaitīšana prasa sistēmu - citādi slēptās
šķautnes paliek nesaskaitītas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         kermenis, restis)

TEMA = "Cik skaldņu, šķautņu un virsotņu?"

MERKIS = ("Raksturosim telpisku figūru, lietojot jēdzienus skaldne, šķautne "
          "un virsotne.")

SATURS = [
    Sakums("Kā saskaitīt to, kas nav redzams?",
           zimejums=kermenis("kvadrs", virsraksts="taisnstūru skaldnis"),
           paraksts="Punktētās līnijas ir šķautnes, kas paliek aiz muguras.",
           fakti=["Skaldne ir plakne, šķautne - līnija, virsotne - punkts.",
                  "Kvadram ir 6 skaldnes, 12 šķautnes un 8 virsotnes."]),

    Doma("Skaiti pa grupām, ne pa vienam",
         "Šķautnes iet trīs virzienos, un katrā virzienā to ir četras - tāpēc "
         "kopā 12.",
         soli=[
             "Saskaiti skaldnes: augša, apakša un četri sāni.",
             "Saskaiti šķautnes pa virzieniem: 4 + 4 + 4.",
             "Saskaiti virsotnes: četras augšā, četras apakšā.",
             "Pārbaudi ar modeli vai kastīti.",
         ],
         pieze="Slēptās šķautnes zīmējumā velk punktētas - bet tās ir tikpat "
               "īstas kā redzamās, un tās arī jāskaita."),

    Petijums("Saskaiti uz īstas kastes",
             vajag="kartona kastīte un zīmulis",
             soli=[
                 "Paņem kastīti un saskaiti tās skaldnes.",
                 "Ar pirkstu izseko katru šķautni un saskaiti tās.",
                 "Saskaiti stūrus - tās ir virsotnes.",
                 "Salīdzini savus skaitļus ar 6, 12 un 8.",
             ],
             secinajums="Uz īstas kastes neviena šķautne nepazūd - tāpēc "
                        "skaitīt ar rokām ir vieglāk nekā zīmējumā."),

    Paraugs("Cik šķautņu ir kvadram?",
            uzd="Saskaiti taisnstūru skaldņa šķautnes.",
            soli=[
                ("Augšējā skaldnē 4 šķautnes",
                 "Augšas mala."),
                ("Apakšējā skaldnē arī 4",
                 "Apakšas mala."),
                ("Vēl 4 stāvus",
                 "Tās savieno augšu ar apakšu; kopā 12."),
            ],
            atbilde="12 šķautnes"),

    Ievadi("Saskaiti daļas", [
        {"jaut": "Cik skaldņu ir kvadram?", "atb": ["6"],
         "padoms": "Augša, apakša, četri sāni."},
        {"jaut": "Cik šķautņu ir kvadram?", "atb": ["12"],
         "padoms": "4 + 4 + 4."},
        {"jaut": "Cik virsotņu ir kvadram?", "atb": ["8"],
         "padoms": "4 + 4."},
        {"jaut": "Cik skaldņu ir četrstūra piramīdai?", "atb": ["5"],
         "padoms": "Pamats un četri trīsstūri."},
        {"jaut": "Cik virsotņu ir četrstūra piramīdai?", "atb": ["5"],
         "padoms": "Četras pamatā un viena augšā."},
        {"jaut": "Cik šķautņu ir četrstūra piramīdai?", "atb": ["8"],
         "padoms": "4 pamatā un 4 uz virsotni."},
    ], pamats=4),

    Zimejums("Kvadra daļas skaitļos",
             restis([["skaldnes", "šķautnes", "virsotnes"],
                     [6, 12, 8]],
                    "taisnstūru skaldnis"),
             paskaidro="Šie trīs skaitļi ir vienādi visiem kvadriem un "
                       "kubiem - lai kāds būtu to izmērs.",
             ievads="Trīs skaitļi, kas jāzina no galvas."),

    Varianti("Cik tur ir?", [
        {"jaut": "Cik šķautņu ir kubam?",
         "opcijas": ["12", "6", "8", "4"],
         "pareizi": 0, "padoms": "Trīs virzieni pa četrām."},
        {"jaut": "Kas ir skaldne?",
         "opcijas": ["Plakne, ar ko ķermenis norobežots", "Līnija",
                     "Punkts", "Tilpums"],
         "pareizi": 0, "padoms": "To var aptaustīt ar plaukstu."},
        {"jaut": "Kas ir virsotne?",
         "opcijas": ["Punkts, kur satiekas šķautnes", "Līnija",
                     "Plakne", "Mala"],
         "pareizi": 0, "padoms": "Tas ir stūris."},
        {"jaut": "Cik skaldņu ir trijiem kubiem?",
         "opcijas": ["18", "6", "12", "24"],
         "pareizi": 0, "padoms": "3 · 6."},
    ], pamats=4),

    Pasaule("Cik detaļu vajag karkasam?",
            Ievadi("", [
                {"jaut": "Kvadra karkasam vajag pa vienam stienim katrai "
                         "šķautnei. Cik stieņu vajag?",
                 "atb": ["12"], "padoms": "12 šķautnes."},
                {"jaut": "Cik savienojumu vajag virsotnēs?", "atb": ["8"],
                 "padoms": "8 virsotnes."},
                {"jaut": "Cik stieņu vajag 5 tādiem karkasiem?",
                 "atb": ["60"], "padoms": "5 · 12."},
                {"jaut": "Cik savienojumu vajag 5 karkasiem?",
                 "atb": ["40"], "padoms": "5 · 8."},
            ]),
            pavediens="tehnika",
            konteksts="Karkasa būvē katrai šķautnei ir savs stienis un katrai "
                      "virsotnei savs savienojums.",
            kapec="Bez pareiza skaita materiāls vai nepietiek, vai paliek "
                  "pāri."),

    Kopsavilkums([
        "Lietoju jēdzienus skaldne, šķautne un virsotne.",
        "Saskaitu tās pa grupām, ne pa vienam.",
        "Zinu, ka kvadram ir 6, 12 un 8.",
        "Pārbaudu skaitļus uz īsta modeļa.",
    ]),

    Majas([
        "Paņem mājās kastīti un saskaiti visas trīs daļas.",
        "Izdari to pašu ar piramīdas formas priekšmetu.",
        "Uzraksti abu ķermeņu skaitļus blakus un salīdzini.",
    ]),
]
