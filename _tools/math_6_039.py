# -*- coding: utf-8 -*-
"""6. klase, 39. stunda: «Kā reizinājumu parādīt simta kvadrātā?»

Jauns temats sākas ar to pašu modeli, kas parastajām daļām - kvadrātu ar
malu 1. Tikai tagad malas ir sadalītas desmitdaļās, tāpēc rūtiņu ir simts,
un komata vieta rezultātā nav jāiegaumē: to var saskaitīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         kvadrats)

TEMA = "Kā reizinājumu parādīt simta kvadrātā?"

MERKIS = ("Mācīsimies attēlot divu decimāldaļu reizinājumu simta kvadrātā "
          "un pierakstīt to.")

SATURS = [
    Sakums("Simts rūtiņu izstāsta visu",
           zimejums=kvadrats(10, 10, 4, 7, paraksts="28 no 100"),
           paraksts="Iekrāsotas 0,4 platumā un 0,7 augstumā. Kopā "
                    "28 rūtiņas no 100, tātad 0,28.",
           fakti=["Kvadrāta mala ir 1, tāpēc viena rūtiņa ir 0,01.",
                  "0,4 · 0,7 = 0,28 - mazāks par abiem reizinātājiem.",
                  "Rūtiņu skaits pats pasaka, kur liekams komats."]),

    Doma("Viena rūtiņa ir viena simtdaļa",
         "Simta kvadrātā decimāldaļu reizinājums ir iekrāsoto rūtiņu skaits, "
         "un katra rūtiņa ir 0,01.",
         soli=[
             "Sadali kvadrāta malas desmit vienādās daļās.",
             "Iekrāso tik kolonnu, cik pasaka pirmais reizinātājs.",
             "Iekrāso tik rindu, cik pasaka otrais.",
             "Saskaiti, cik rūtiņu ir abu krustojumā.",
             "Pieraksti rezultātu simtdaļās.",
         ],
         pieze="Tas ir tas pats modelis, kas parastajām daļām: "
               "{4|10} · {7|10} = {28|100}. Decimāldaļas ir daļas ar "
               "saucēju 10, 100 vai 1000 - tikai citā pierakstā."),

    Slidnis("Maini otro reizinātāju",
            [{"v": "0,5 · 0,2", "teksts": "= 0,10 - 10 rūtiņas",
              "josla": 10, "zim": kvadrats(10, 10, 5, 2)},
             {"v": "0,5 · 0,4", "teksts": "= 0,20 - 20 rūtiņas",
              "josla": 20, "zim": kvadrats(10, 10, 5, 4)},
             {"v": "0,5 · 0,6", "teksts": "= 0,30 - 30 rūtiņas",
              "josla": 30, "zim": kvadrats(10, 10, 5, 6)},
             {"v": "0,5 · 0,8", "teksts": "= 0,40 - 40 rūtiņas",
              "josla": 40, "zim": kvadrats(10, 10, 5, 8)}],
            ievads="Spied soli pa solim: pirmais reizinātājs paliek 0,5, "
                   "otrais aug. Iekrāsoto rūtiņu skaits aug tieši tikpat "
                   "reižu."),

    Paraugs("Uzzīmē 0,3 · 0,6",
            uzd="Attēlo reizinājumu 0,3 · 0,6 simta kvadrātā un pieraksti "
                "rezultātu.",
            soli=[
                ("Iekrāso 3 kolonnas",
                 "0,3 ir trīs desmitdaļas no platuma."),
                ("Iekrāso 6 rindas",
                 "0,6 ir sešas desmitdaļas no augstuma."),
                ("Krustojumā ir 3 · 6 = 18 rūtiņas",
                 "Tik rūtiņu ir abās reizēs iekrāsotas."),
                ("18 rūtiņas no 100 ir 0,18",
                 "Katra rūtiņa ir viena simtdaļa."),
            ],
            atbilde="0,18"),

    Ievadi("Saskaiti rūtiņas", [
        {"jaut": "Cik rūtiņu ir simta kvadrātā?",
         "atb": ["100"], "padoms": "10 · 10."},
        {"jaut": "Iekrāsotas 2 kolonnas un 5 rindas. Cik rūtiņu krustojumā?",
         "atb": ["10"], "padoms": "2 · 5.",
         "zim": kvadrats(10, 10, 2, 5)},
        {"jaut": "Kāds ir reizinājums 0,2 · 0,5?",
         "atb": ["0,1", "0.1", "0,10"], "padoms": "10 rūtiņas no 100."},
        {"jaut": "Kāds ir reizinājums 0,4 · 0,3?",
         "atb": ["0,12", "0.12"], "padoms": "4 · 3 = 12 rūtiņas."},
        {"jaut": "Kāds ir reizinājums 0,9 · 0,9?",
         "atb": ["0,81", "0.81"], "padoms": "9 · 9 = 81 rūtiņa."},
        {"jaut": "Cik rūtiņu jāiekrāso, lai iegūtu 0,25?",
         "atb": ["25"], "padoms": "25 simtdaļas."},
    ], pamats=4),

    Varianti("Ko rāda kvadrāts?", [
        {"jaut": "Cik liela ir viena rūtiņa simta kvadrātā?",
         "opcijas": ["0,01", "0,1", "1", "0,001"],
         "pareizi": 0,
         "padoms": "Simtā daļa no vesela."},
        {"jaut": "Kāpēc 0,4 · 0,7 ir mazāks par 0,4?",
         "opcijas": ["Jo 0,7 ir mazāks par 1", "Jo 0,4 ir maza",
                     "Jo rūtiņas ir mazas", "Tas nav mazāks"],
         "pareizi": 0,
         "padoms": "Reizinot ar skaitli, kas mazāks par 1, rezultāts sarūk."},
        {"jaut": "0,5 · 0,5 kvadrātā aizņem...",
         "opcijas": ["25 rūtiņas", "50 rūtiņas", "10 rūtiņas",
                     "100 rūtiņas"],
         "pareizi": 0,
         "padoms": "5 · 5."},
        {"jaut": "Kāds parasto daļu reizinājums atbilst 0,3 · 0,6?",
         "opcijas": ["{3|10} · {6|10}", "{3|6} · {6|3}",
                     "{30|10} · {60|10}", "{3|100} · {6|100}"],
         "pareizi": 0,
         "padoms": "Desmitdaļa ir {1|10}."},
    ], pamats=4),

    Zimejums("Puse no puses",
             kvadrats(10, 10, 5, 5, paraksts="25 no 100"),
             paskaidro="0,5 · 0,5 = 0,25. Tas ir tas pats, kas {1|2} · {1|2} "
                       "= {1|4}.",
             ievads="Tas pats piemērs abos pierakstos."),

    Pasaule("Cik liela ir ekrāna daļa?",
            Ievadi("", [
                {"jaut": "Logs aizņem 0,5 no ekrāna platuma un 0,4 no "
                         "augstuma. Cik liela daļa no ekrāna tas ir?",
                 "atb": ["0,2", "0.2", "0,20"],
                 "padoms": "5 · 4 = 20 rūtiņas."},
                {"jaut": "Otrs logs aizņem 0,3 un 0,3. Cik liela daļa?",
                 "atb": ["0,09", "0.09"], "padoms": "9 rūtiņas no 100."},
                {"jaut": "Ekrānā ir 1000 pikseļu rindu. Cik rindu aizņem "
                         "0,4 no augstuma?",
                 "atb": ["400"], "padoms": "1000 · 0,4."},
                {"jaut": "Cik procentu no ekrāna aizņem pirmais logs?",
                 "atb": ["20"], "padoms": "0,2 ir 20 simtdaļas."},
            ]),
            pavediens="dati",
            konteksts="Datorā logu izmērus bieži raksta kā daļu no ekrāna, "
                      "nevis pikseļos - tad tie der jebkuram ekrānam.",
            kapec="Divu daļu reizinājums pasaka, cik liels ir laukums."),

    Kopsavilkums([
        "Attēloju divu decimāldaļu reizinājumu simta kvadrātā.",
        "Zinu, ka viena rūtiņa ir 0,01.",
        "Nolasu rezultātu kā iekrāsoto rūtiņu skaitu simtdaļās.",
        "Saistu decimāldaļas ar parastajām daļām.",
    ]),

    Majas([
        "Uzzīmē 10 x 10 režģi un attēlo tajā 0,6 · 0,5.",
        "Atrodi divas decimāldaļas, kuru reizinājums ir 0,36.",
        "Paskaidro, kāpēc 0,1 · 0,1 ir 0,01, nevis 0,1.",
    ]),
]
