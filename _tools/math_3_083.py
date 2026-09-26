# -*- coding: utf-8 -*-
"""3. klase, 83. stunda: «Kā atcerēties, kurš ir kurš?»

Skaitītāju un saucēju jauc bieži, tāpēc te skolēns izveido *savu*
atcerēšanās stratēģiju un pārbauda to uz piemēriem. Pārbaude ir svarīgākā
daļa: stratēģija, kas nostrādā tikai reizēm, ir sliktāka par nekādu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā atcerēties, kurš ir kurš?"

MERKIS = ("Izstāstīsim savu atcerēšanās stratēģiju un pārbaudīsim to "
          "piemēros.")

SATURS = [
    Sakums("Kā nesajaukt skaitītāju ar saucēju?",
           zimejums=restis([["skaitītājs", "skaita, cik ņem"],
                            ["saucējs", "sauc daļu vārdā"]],
                           "divi vārdi, divas nozīmes"),
           paraksts="Abi vārdi paši pasaka, ko tie dara.",
           fakti=["Saucējs *sauc*: ceturtdaļa, astotdaļa, desmitdaļa.",
                  "Skaitītājs *skaita*, cik tādu daļu ņem."]),

    Doma("Vārds pats pasaka, ko tas dara",
         "Saucējs sauc daļu vārdā, skaitītājs skaita, cik to ir.",
         soli=[
             "Paskaties uz apakšējo skaitli - tas sauc daļu.",
             "Ja tur ir 4, daļu sauc par ceturtdaļu.",
             "Paskaties uz augšējo - tas saskaita ceturtdaļas.",
             "Pārbaudi stratēģiju uz trim dažādām daļām.",
         ],
         pieze="Der arī cits atbalsts: apakšējais skaitlis ir *zem* svītras, "
               "tāpat kā pamats zem mājas - tas notur visu daļu."),

    Petijums("Izveido savu atcerēšanās stratēģiju",
             vajag="lapa un zīmulis",
             soli=[
                 "Izdomā savu veidu, kā atcerēties abus vārdus.",
                 "Uzraksti to vienā teikumā.",
                 "Pārbaudi to uz daļām {2|5}, {7|10} un {1|3}.",
                 "Pastāsti stratēģiju klasesbiedram.",
             ],
             secinajums="Stratēģija der tad, ja tā nostrādā visās trijās "
                        "reizēs - ne tikai pirmajā."),

    Paraugs("Kā pārbaudīt savu stratēģiju?",
            uzd="Pārbaudi stratēģiju «saucējs sauc» uz daļas {7|10}.",
            soli=[
                ("Apakšējais skaitlis ir 10",
                 "Tas sauc daļu: desmitdaļa."),
                ("Augšējais skaitlis ir 7",
                 "Tas saskaita: septiņas desmitdaļas."),
                ("{7|10} - septiņas desmitdaļas",
                 "Stratēģija nostrādāja."),
            ],
            atbilde="septiņas desmitdaļas"),

    Ievadi("Nosauc daļu", [
        {"jaut": "Daļā {3|5} - kāds ir saucējs?", "atb": ["5"],
         "padoms": "Skaitlis zem svītras."},
        {"jaut": "Daļā {3|5} - kāds ir skaitītājs?", "atb": ["3"],
         "padoms": "Skaitlis virs svītras."},
        {"jaut": "Daļā {9|10} - kāds ir saucējs?", "atb": ["10"],
         "padoms": "Desmitdaļa."},
        {"jaut": "Kādu daļu sauc par ceturtdaļu - kāds ir tās saucējs?",
         "atb": ["4"], "padoms": "Četras vienādas daļas."},
        {"jaut": "Kāds saucējs ir sestdaļai?", "atb": ["6"],
         "padoms": "Sešas vienādas daļas."},
        {"jaut": "Daļā {1|7} - cik daļu ņemts?", "atb": ["1"],
         "padoms": "Skaitītājs."},
    ], pamats=4),

    Zimejums("Kurš skaitlis kur stāv",
             restis([["3", "← skaitītājs"],
                     ["—", ""],
                     ["8", "← saucējs"]],
                    "daļas pieraksts"),
             paskaidro="Skaitītājs vienmēr ir virs svītras, saucējs - zem "
                       "tās.",
             ievads="Tā daļu raksta latviešu standartā."),

    Varianti("Vai stratēģija strādā?", [
        {"jaut": "Kurš skaitlis sauc daļu vārdā?",
         "opcijas": ["Saucējs", "Skaitītājs", "Abi", "Neviens"],
         "pareizi": 0, "padoms": "Vārds pats to pasaka."},
        {"jaut": "Daļā {5|6} - kā to lasa?",
         "opcijas": ["piecas sestdaļas", "sešas piektdaļas",
                     "pieci seši", "piecdesmit seši"],
         "pareizi": 0, "padoms": "Vispirms skaitītājs."},
        {"jaut": "Kurš pieraksts nozīmē «trīs desmitdaļas»?",
         "opcijas": ["{3|10}", "{10|3}", "{1|30}", "{3|1}"],
         "pareizi": 0, "padoms": "Saucējs ir 10."},
        {"jaut": "Cik reizes stratēģija jāpārbauda?",
         "opcijas": ["Vismaz trīs", "Vienu", "Nav jāpārbauda", "Desmit"],
         "pareizi": 0, "padoms": "Viena reize var būt nejaušība."},
    ], pamats=4),

    Pasaule("Cik metienu trāpīja?",
            Ievadi("", [
                {"jaut": "Spēlētājs meta 10 reizes, trāpīja 6. Kāds ir "
                         "saucējs daļā?",
                 "atb": ["10"], "padoms": "Visi metieni."},
                {"jaut": "Kāds ir skaitītājs?", "atb": ["6"],
                 "padoms": "Trāpītie metieni."},
                {"jaut": "Cik metienu netrāpīja?", "atb": ["4"],
                 "padoms": "10 − 6."},
                {"jaut": "Otrs spēlētājs meta 8 reizes un trāpīja 6. Cik "
                         "metienu netrāpīja?",
                 "atb": ["2"], "padoms": "8 − 6."},
            ]),
            pavediens="sports",
            konteksts="Trāpījumu statistiku raksta kā daļu - un saucējs tur "
                      "ir visu metienu skaits.",
            kapec="6 no 10 un 6 no 8 ir dažādi rezultāti, kaut skaitītājs "
                  "viens."),

    Kopsavilkums([
        "Zinu, kurš skaitlis ir skaitītājs un kurš saucējs.",
        "Izmantoju savu atcerēšanās stratēģiju.",
        "Pārbaudu stratēģiju vairākos piemēros.",
        "Lasu daļu pareizi.",
    ]),

    Majas([
        "Uzraksti savu stratēģiju un pārbaudi to uz piecām daļām.",
        "Pastāsti to kādam mājiniekam.",
        "Uzraksti piecas daļas un nosauc katrai saucēju un skaitītāju.",
    ]),
]
