# -*- coding: utf-8 -*-
"""3. klase, 79. stunda: «Cik liels bija veselais?»

Apgrieztais uzdevums: redzama tikai daļa, meklē veselo. Tas ir grūtāks nekā
tiešais, jo prasa saprast, ka daļa ir *mērs* - ja 5 rūtiņas ir trešdaļa, tad
veselajā tādu trešdaļu ir trīs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         dala)

TEMA = "Cik liels bija veselais?"

MERKIS = ("Papildināsim figūru līdz veselajam, ja redzama tikai tā daļa.")

SATURS = [
    Sakums("Cik liela bija visa šokolāde, ja palicis tikai gabals?",
           zimejums=dala(3, 1, "1/3", "redzama tikai viena trešdaļa"),
           paraksts="Ja šis gabals ir trešdaļa, tad veselajā tādu ir trīs.",
           fakti=["Daļa ir mērs: veselais ir tik daļu, cik pasaka saucējs.",
                  "Ja zini vienu daļu, veselo iegūst ar reizināšanu."]),

    Doma("Veselais ir tik daļu, cik pasaka apakšējais skaitlis",
         "Ja 5 rūtiņas ir {1|3}, tad veselajā ir 3 · 5 = 15 rūtiņas.",
         soli=[
             "Noskaidro, kāda daļa ir redzama.",
             "Paskaties, cik daļu ir veselajā - to pasaka apakšējais "
             "skaitlis.",
             "Reizini redzamās daļas lielumu ar šo skaitli.",
             "Pārbaudi: vai veselais tiešām dalās šajās daļās?",
         ],
         pieze="Ja redzamas vairākas daļas, vispirms izrēķina vienu: ja "
               "8 rūtiņas ir {2|5}, tad viena piektdaļa ir 4, bet veselais - "
               "20."),

    Paraugs("Cik liels ir veselais?",
            uzd="Figūrā redzamas 5 rūtiņas, un tā ir {1|3} no veselā. Cik "
                "rūtiņu ir veselajā?",
            soli=[
                ("Viena trešdaļa ir 5 rūtiņas",
                 "Tas ir dots."),
                ("Veselajā ir 3 trešdaļas",
                 "Apakšējais skaitlis pasaka daļu skaitu."),
                ("3 · 5 = 15",
                 "Veselajā ir 15 rūtiņas."),
            ],
            atbilde="15 rūtiņas"),

    Ievadi("Atrodi veselo", [
        {"jaut": "{1|3} ir 5 rūtiņas. Cik rūtiņu ir veselajā?",
         "atb": ["15"], "padoms": "3 · 5."},
        {"jaut": "{1|4} ir 6 rūtiņas. Cik rūtiņu ir veselajā?",
         "atb": ["24"], "padoms": "4 · 6."},
        {"jaut": "{1|5} ir 7 rūtiņas. Cik rūtiņu ir veselajā?",
         "atb": ["35"], "padoms": "5 · 7."},
        {"jaut": "{2|5} ir 8 rūtiņas. Cik rūtiņu ir vienā piektdaļā?",
         "atb": ["4"], "padoms": "8 : 2."},
        {"jaut": "Cik rūtiņu ir veselajā?", "atb": ["20"],
         "padoms": "5 · 4."},
        {"jaut": "{1|2} ir 9 rūtiņas. Cik rūtiņu ir veselajā?",
         "atb": ["18"], "padoms": "2 · 9."},
    ], pamats=4),

    Petijums("Papildini figūru līdz veselajam",
             vajag="rūtiņu lapa un zīmulis",
             soli=[
                 "Uzzīmē joslu no 4 rūtiņām.",
                 "Pieņem, ka tā ir {1|3} no veselā, un uzzīmē visu veselo.",
                 "Pieņem, ka tā ir {1|4}, un uzzīmē veselo vēlreiz.",
                 "Salīdzini abus veselos.",
             ],
             secinajums="Viena un tā pati daļa dod dažādus veselos - viss "
                        "atkarīgs no tā, kāda daļa tā ir."),

    Zimejums("No divām piektdaļām līdz veselajam",
             dala(5, 2, "2/5 = 8 rūtiņas", "veselais ir 20 rūtiņas"),
             paskaidro="Vispirms izrēķina vienu piektdaļu (4 rūtiņas), tikai "
                       "tad veselo.",
             ievads="Redzamas divas daļas no piecām."),

    Varianti("Cik liels ir veselais?", [
        {"jaut": "{1|4} ir 3 rūtiņas. Cik rūtiņu ir veselajā?",
         "opcijas": ["12", "7", "9", "4"],
         "pareizi": 0, "padoms": "4 · 3."},
        {"jaut": "{1|2} ir 10 rūtiņas. Cik rūtiņu ir veselajā?",
         "opcijas": ["20", "12", "5", "10"],
         "pareizi": 0, "padoms": "2 · 10."},
        {"jaut": "{3|4} ir 12 rūtiņas. Cik rūtiņu ir vienā ceturtdaļā?",
         "opcijas": ["4", "3", "6", "12"],
         "pareizi": 0, "padoms": "12 : 3."},
        {"jaut": "Cik rūtiņu ir veselajā, ja {3|4} ir 12?",
         "opcijas": ["16", "15", "24", "36"],
         "pareizi": 0, "padoms": "4 · 4."},
    ], pamats=4),

    Pasaule("Cik bija visa kūka?",
            Ievadi("", [
                {"jaut": "Palikusi {1|4} kūkas - tie ir 3 gabali. Cik gabalu "
                         "bija kūkā?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Apēsta {1|3} pankūku - tās ir 4 pankūkas. Cik "
                         "pankūku bija?",
                 "atb": ["12"], "padoms": "3 · 4."},
                {"jaut": "Palikušas {2|5} no cepumiem - tie ir 6 cepumi. Cik "
                         "cepumu ir vienā piektdaļā?",
                 "atb": ["3"], "padoms": "6 : 2."},
                {"jaut": "Cik cepumu bija sākumā?",
                 "atb": ["15"], "padoms": "5 · 3."},
            ]),
            pavediens="virtuve",
            konteksts="Pēc svētkiem uz galda paliek tikai daļa - bet pēc tās "
                      "var pateikt, cik bija sākumā.",
            kapec="Daļa vienmēr atceras, cik liels bija veselais."),

    Kopsavilkums([
        "Atrodu veselo, ja zināma viena daļa.",
        "Vispirms izrēķinu vienu daļu, ja redzamas vairākas.",
        "Zinu, ka veselajā ir tik daļu, cik pasaka apakšējais skaitlis.",
        "Papildinu figūru līdz veselajam.",
    ]),

    Majas([
        "Uzzīmē 5 rūtiņas un papildini tās līdz veselajam, ja tā ir {1|4}.",
        "Izdomā uzdevumu, kurā redzama tikai puse.",
        "Atrodi mājās kaut ko, no kā palikusi tikai daļa, un pasaki, cik "
        "bija sākumā.",
    ]),
]
