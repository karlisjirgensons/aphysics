# -*- coding: utf-8 -*-
"""6. klase, 86. stunda: «Cik liela ir atlaide?»

Jauns mikrotemats - procenti dzīvē. Atlaide ir visbiežākais procentu
lietojums, un tajā ir divi soļi, kurus mēdz sajaukt: cik liela ir atlaide un
cik liela ir jaunā cena. Stunda māca rēķināt abus - un otro arī īsceļā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Cik liela ir atlaide?"

MERKIS = ("Iemācīsimies aprēķināt procentus no skaitļa un jauno cenu pēc "
          "atlaides.")

SATURS = [
    Sakums("«−30 %» nav jaunā cena",
           fakti=["Uzraksts «−30 %» pasaka, cik atņem, ne cik maksā.",
                  "Jaunā cena ir 70 % no vecās.",
                  "Tāpēc to var rēķināt vienā solī, nevis divos."]),

    Doma("Atlaide vai jaunā cena - izlem uzreiz",
         "Atlaides lielumu iegūst, procentus rēķinot no sākotnējās cenas; "
         "jauno cenu - atņemot atlaidi vai uzreiz rēķinot atlikušos "
         "procentus.",
         soli=[
             "Izlasi, ko prasa: atlaidi vai jauno cenu.",
             "Atrodi 1 % no sākotnējās cenas.",
             "Reizini ar atlaides procentiem - tā ir atlaide.",
             "Jauno cenu iegūsti, atņemot atlaidi no sākotnējās cenas.",
             "Vai arī uzreiz rēķini atlikušos procentus.",
         ],
         pieze="Īsceļš ir drošāks: 30 % atlaide nozīmē, ka jāmaksā 70 %. "
               "Viena darbība divu vietā - un viena kļūdas iespēja mazāk."),

    Slidnis("Jo lielāka atlaide, jo mazāka cena",
            [{"v": "atlaide 10 %", "teksts": "maksā 90 % jeb 54 €",
              "josla": 90},
             {"v": "atlaide 25 %", "teksts": "maksā 75 % jeb 45 €",
              "josla": 75},
             {"v": "atlaide 50 %", "teksts": "maksā 50 % jeb 30 €",
              "josla": 50},
             {"v": "atlaide 70 %", "teksts": "maksā 30 % jeb 18 €",
              "josla": 30}],
            ievads="Sākotnējā cena ir 60 €. Spied soli pa solim: atlaide aug, "
                   "maksājamie procenti sarūk."),

    Paraugs("Divi ceļi uz jauno cenu",
            uzd="Prece maksā 60 €, atlaide ir 30 %. Cik tā maksā tagad?",
            soli=[
                ("1 % no 60 ir 0,6 €",
                 "60 : 100."),
                ("Atlaide: 30 · 0,6 = 18 €",
                 "Trīsdesmit simtdaļas."),
                ("Jaunā cena: 60 − 18 = 42 €",
                 "Pirmais ceļš."),
                ("Īsceļš: 70 · 0,6 = 42 €",
                 "Jāmaksā 70 % - viena darbība."),
            ],
            atbilde="42 €"),

    Ievadi("Aprēķini atlaidi un jauno cenu", [
        {"jaut": "Cena 60 €, atlaide 30 %. Cik eiro ir atlaide?",
         "atb": ["18"], "padoms": "30 · 0,6."},
        {"jaut": "Cik eiro maksā prece pēc atlaides?",
         "atb": ["42"], "padoms": "60 − 18 vai 70 %."},
        {"jaut": "Cena 80 €, atlaide 25 %. Cik eiro maksā tagad?",
         "atb": ["60"], "padoms": "75 % no 80."},
        {"jaut": "Cena 45 €, atlaide 20 %. Cik eiro maksā tagad?",
         "atb": ["36"], "padoms": "80 % no 45."},
        {"jaut": "Cena 120 €, atlaide 15 %. Cik eiro ir atlaide?",
         "atb": ["18"], "padoms": "1 % ir 1,2."},
        {"jaut": "Cena 200 €, atlaide 40 %. Cik eiro maksā tagad?",
         "atb": ["120"], "padoms": "60 % no 200."},
    ], pamats=4,
        ievads="Vispirms izlem, ko prasa - atlaidi vai jauno cenu."),

    Pasaule("Cik samaksāsi kasē?",
            Kustiba("", [
                {"jaut": "Cena 50 €, atlaide 20 %. Cik eiro samaksāsi?",
                 "atb": 40, "beigas": 100, "iedala": 20, "mers": "eiro",
                 "merkis": "jaunā cena", "objekts": "Čeks",
                 "padoms": "80 % no 50."},
                {"jaut": "Cena 90 €, atlaide 10 %. Cik eiro samaksāsi?",
                 "atb": 81, "beigas": 100, "iedala": 20, "mers": "eiro",
                 "merkis": "jaunā cena", "objekts": "Čeks",
                 "padoms": "90 % no 90."},
                {"jaut": "Cena 100 €, atlaide 35 %. Cik eiro samaksāsi?",
                 "atb": 65, "beigas": 100, "iedala": 20, "mers": "eiro",
                 "merkis": "jaunā cena", "objekts": "Čeks",
                 "padoms": "65 % no 100."},
                {"jaut": "Cena 80 €, atlaide 75 %. Cik eiro samaksāsi?",
                 "atb": 20, "beigas": 100, "iedala": 20, "mers": "eiro",
                 "merkis": "jaunā cena", "objekts": "Čeks",
                 "padoms": "25 % no 80."},
            ]),
            pavediens="veikals",
            konteksts="Kase parāda galīgo summu, bet to var zināt jau pie "
                      "plaukta.",
            kapec="Jaunā cena ir atlikušie procenti - viena darbība."),

    Varianti("Ko tieši prasa?", [
        {"jaut": "«Atlaide 40 %.» Cik procentu jāmaksā?",
         "opcijas": ["60", "40", "100", "140"],
         "pareizi": 0,
         "padoms": "100 − 40."},
        {"jaut": "Cena 200 €, atlaide 50 %. Jaunā cena ir...",
         "opcijas": ["100 €", "150 €", "50 €", "250 €"],
         "pareizi": 0,
         "padoms": "Puse."},
        {"jaut": "Skolēns rēķina 30 % no 60 = 18 un atbild «prece maksā "
                 "18 €». Kas nav labi?",
         "opcijas": ["18 € ir atlaide, nevis cena",
                     "Nepareizi izrēķināti procenti",
                     "Jārēķina 130 %", "Viss ir pareizi"],
         "pareizi": 0,
         "padoms": "Cena ir 60 − 18."},
        {"jaut": "Kurš īsceļš der 25 % atlaidei?",
         "opcijas": ["Rēķināt 75 % no cenas", "Dalīt ar 25",
                     "Reizināt ar 25", "Atņemt 25 €"],
         "pareizi": 0,
         "padoms": "Atlikušie procenti."},
    ], pamats=4),

    Kopsavilkums([
        "Aprēķinu atlaidi kā procentus no sākotnējās cenas.",
        "Aprēķinu jauno cenu abos ceļos.",
        "Lietoju īsceļu: jaunā cena ir atlikušie procenti.",
        "Atšķiru, ko uzdevums prasa - atlaidi vai cenu.",
    ]),

    Majas([
        "Atrodi veikalā trīs preces ar atlaidi un izrēķini jaunās cenas.",
        "Pieraksti, cik eiro kopā ietaupītu, tās nopērkot.",
        "Paskaidro kādam mājās, kāpēc «−25 %» nozīmē «maksā 75 %».",
    ]),
]
