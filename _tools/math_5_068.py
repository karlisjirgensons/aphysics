# -*- coding: utf-8 -*-
"""5. klase, 68. stunda: «Kā papildināt līdz vienam?»

Atsevišķa stunda vienam gadījumam, jo tieši tur skolēns apstājas: no vesela
skaitļa atņemt daļu nav kur - skaitītāja nav. Risinājums ir viens un tas
pats abos virzienos: veselo pārraksta kā daļu ar to pašu saucēju. Zīmējums
te nav ilustrācija, bet paņēmiens - tukšais gabals ir atbilde.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums, dala)

TEMA = "Kā papildināt līdz vienam?"

MERKIS = ("Iemācīsimies atņemt daļu no vieninieka un papildināt daļu līdz "
          "vieniniekam, skaidrojot to ar zīmējumu.")

SATURS = [
    Sakums("Viens vesels - un cik tukšs?",
           zimejums=dala(5, 3, "3/5"),
           paraksts="Iekrāsotas {3|5}; tukšas palikušas {2|5}.",
           fakti=["Visa josla kopā ir viens vesels.",
                  "Iekrāsotā un tukšā daļa kopā dod vienu.",
                  "Tāpēc tukšo var izrēķināt, nevis izmērīt."]),

    Doma("Veselo pārraksta ar to pašu saucēju",
         "Lai no vieninieka atņemtu daļu, vieninieku pieraksta kā daļu, "
         "kuras skaitītājs un saucējs ir vienādi.",
         soli=[
             "Paskaties, kāds saucējs ir otrai daļai.",
             "Uzraksti vieninieku ar to pašu saucēju.",
             "Atņem skaitītājus.",
             "Saīsini, ja rezultāts ir saīsināms.",
             "Pārbaudi: abas daļas kopā dod vienu.",
         ],
         pieze="1 = {5|5} = {8|8} = {12|12} - vieninieku var uzrakstīt ar "
               "jebkuru saucēju, un izvēlas to, kāds vajadzīgs uzdevumā."),

    Paraugs("1 - {3|5}",
            uzd="Cik trūkst daļai {3|5} līdz vieniniekam?",
            soli=[
                ("1 = {5|5}",
                 "Vieninieku raksta ar saucēju 5."),
                ("{5|5} - {3|5}",
                 "Tagad abiem ir viens saucējs."),
                ("5 - 3 = 2",
                 "Atņem skaitītājus."),
                ("{2|5}",
                 "Tik trūkst līdz vieniniekam."),
                ("Pārbaude: {3|5} + {2|5} = {5|5} = 1",
                 "Abas daļas kopā dod veselo."),
            ],
            atbilde="1 - {3|5} = {2|5}"),

    Slidnis("Iekrāsotais un tukšais kopā ir viens",
            [{"v": "{1|5}", "teksts": "tukšas {4|5}", "josla": 20,
              "zim": dala(5, 1)},
             {"v": "{2|5}", "teksts": "tukšas {3|5}", "josla": 40,
              "zim": dala(5, 2)},
             {"v": "{3|5}", "teksts": "tukšas {2|5}", "josla": 60,
              "zim": dala(5, 3)},
             {"v": "{4|5}", "teksts": "tukša {1|5}", "josla": 80,
              "zim": dala(5, 4)},
             {"v": "{5|5}", "teksts": "tukša nav nekā", "josla": 100,
              "zim": dala(5, 5)}],
            ievads="Spied soli pa solim: cik pieaug viens, tik sarūk otrs."),

    Ievadi("Papildini līdz vieniniekam", [
        {"jaut": "Cik ir 1 - {1|4}? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "1 = {4|4}."},
        {"jaut": "Cik ir 1 - {2|7}? Atbildi raksti kā a/b.",
         "atb": ["5/7"], "padoms": "1 = {7|7}."},
        {"jaut": "Cik ir 1 - {5|8}? Atbildi raksti kā a/b.",
         "atb": ["3/8"], "padoms": "1 = {8|8}."},
        {"jaut": "Cik ir 1 - {7|10}? Atbildi raksti kā a/b.",
         "atb": ["3/10"], "padoms": "1 = {10|10}."},
        {"jaut": "Cik jāpieliek daļai {2|9}, lai iznāktu 1? Atbildi raksti "
                 "kā a/b.",
         "atb": ["7/9"], "padoms": "9 - 2 = 7."},
        {"jaut": "Cik jāpieliek daļai {5|6}, lai iznāktu 1? Atbildi raksti "
                 "kā a/b.",
         "atb": ["1/6"], "padoms": "6 - 5 = 1."},
        {"jaut": "Cik ir 1 - {4|6}? Atbildi raksti kā a/b.",
         "atb": ["1/3", "2/6"], "padoms": "{2|6} saīsināts."},
        {"jaut": "Cik ir 1 - {6|8}? Atbildi raksti kā a/b.",
         "atb": ["1/4", "2/8"], "padoms": "{2|8} saīsināts."},
    ], pamats=4,
        ievads="Vieninieku raksta ar to pašu saucēju - un tālāk viss ir "
               "parasta atņemšana."),

    Zimejums("Divas piektdaļas tukšuma",
             dala(5, 3, "3/5 iekrāsotas"),
             paskaidro="Tukšie gabali arī ir daļa: {2|5}. Kopā ar "
                       "iekrāsotajiem tie dod {5|5}, tas ir, vienu veselu.",
             ievads="Tukšo gabalu daļu var nolasīt no tā paša zīmējuma."),

    Varianti("Kā raksta vieninieku?", [
        {"jaut": "Kā uzrakstīt 1 ar saucēju 7?",
         "opcijas": ["{7|7}", "{1|7}", "{7|1}", "{0|7}"],
         "pareizi": 0,
         "padoms": "Visi gabali kopā."},
        {"jaut": "Kāpēc vieninieku pārraksta kā daļu?",
         "opcijas": ["Lai abiem būtu viens saucējs",
                     "Lai skaitlis kļūtu lielāks",
                     "Lai varētu saīsināt",
                     "Tā nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Atņemt var tikai vienādus gabalus."},
        {"jaut": "Cik ir 1 - {9|10}?",
         "opcijas": ["{1|10}", "{9|10}", "{10|9}", "{1|9}"],
         "pareizi": 0,
         "padoms": "10 - 9 = 1."},
        {"jaut": "Daļa un tās papildinājums kopā vienmēr dod...",
         "opcijas": ["Vienu veselu", "Nulli", "Divus", "Saucēju"],
         "pareizi": 0,
         "padoms": "Visa josla."},
        {"jaut": "Skolēns rēķina 1 - {2|5} = {1|3}. Kur ir kļūda?",
         "opcijas": ["Vieninieks nav pārrakstīts kā {5|5}",
                     "Skaitītājs par lielu",
                     "Jāsaīsina",
                     "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Atņemti dažādi gabali."},
        {"jaut": "Ja daļa ir {3|8}, kāds ir tās papildinājums līdz vienam?",
         "opcijas": ["{5|8}", "{3|8}", "{8|3}", "{11|8}"],
         "pareizi": 0,
         "padoms": "8 - 3 = 5."},
    ], pamats=4),

    Pasaule("Cik skolēnu vēl nav atbildējuši?",
            Ievadi("", [
                {"jaut": "Anketu aizpildījuši {3|5} klases. Cik daļa vēl "
                         "nav? Atbildi raksti kā a/b.",
                 "atb": ["2/5"], "padoms": "1 = {5|5}."},
                {"jaut": "Projektu pabeiguši {7|12} skolēnu. Cik daļa vēl "
                         "nav? Atbildi raksti kā a/b.",
                 "atb": ["5/12"], "padoms": "12 - 7 = 5."},
                {"jaut": "Ekskursijai pieteikušies {3|4} klases. Cik daļa "
                         "nav pieteikusies? Atbildi raksti kā a/b.",
                 "atb": ["1/4"], "padoms": "1 = {4|4}."},
                {"jaut": "Grāmatu nodevuši {5|6} skolēnu. Cik daļa vēl nav? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/6"], "padoms": "6 - 5 = 1."},
            ]),
            pavediens="skola",
            konteksts="Skolā vienmēr skaita abus skaitļus: cik jau ir un cik "
                      "vēl trūkst.",
            kapec="Otro var izrēķināt no pirmā, neko neskaitot no jauna."),

    Kopsavilkums([
        "Pierakstu vieninieku kā daļu ar vajadzīgo saucēju.",
        "Atņemu daļu no vieninieka.",
        "Papildinu doto daļu līdz vieniniekam.",
        "Skaidroju rezultātu ar joslas zīmējumu.",
    ]),

    Majas([
        "Izrēķini 1 - {5|9} un uzzīmē to ar joslu.",
        "Uzraksti trīs daļu pārus, kas kopā dod vienu veselu.",
        "Atrodi klasē skaitli, kuram var uzrakstīt papildinājumu līdz "
        "vienam.",
    ]),
]
