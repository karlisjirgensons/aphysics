# -*- coding: utf-8 -*-
"""5. klase, 53. stunda: «Kā daļas atlikt uz vienas taisnes?»

Divas taisnes ir ērti, bet uz papīra vietas ir maz, un salīdzināt vieglāk uz
vienas. Tad rodas jautājums: cik sīki sadalīt vienību, lai uz tās ietilptu gan
puses, gan trešdaļas. Atbilde ir 39. stundas kopīgais dalāmais - te tas
parādās nevis kā vingrinājums, bet kā vajadzība.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā daļas atlikt uz vienas taisnes?"

MERKIS = ("Mācīsimies izvēlēties vienu iedaļu, kurā uz vienas skaitļu "
          "taisnes ietilpst daļas ar dažādiem saucējiem.")

SATURS = [
    Sakums("Trīs daļas, viena taisne",
           zimejums=taisne(0, 1, 1, [(1 / 2.0, "1/2"), (3 / 4.0, "3/4")],
                           virsraksts="Puses un ceturtdaļas kopā"),
           paraksts="Ceturtdaļu iedaļās ietilpst arī puse: {1|2} = {2|4}.",
           fakti=["Uz vienas taisnes salīdzināt ir vieglāk nekā uz divām.",
                  "Bet iedaļa var būt tikai viena.",
                  "Tātad tai jāder visām daļām uzreiz."]),

    Doma("Iedaļu izvēlas pēc saucējiem",
         "Vienību sadala tik daļās, lai šis skaitlis dalītos ar visiem "
         "dotajiem saucējiem.",
         soli=[
             "Izraksti visus saucējus.",
             "Atrodi skaitli, kas dalās ar tiem visiem.",
             "Sadali vienību tik daļās - tā ir taisnes iedaļa.",
             "Pārraksti katru daļu ar šo saucēju.",
             "Atzīmē visus punktus un salīdzini.",
         ],
         pieze="Der jebkurš kopīgais dalāmais, bet mazākais ir ērtākais: "
               "saucējiem 2 un 3 der gan 12, gan 18, tomēr ar 6 iedaļām "
               "zīmējums ir skaidrāks."),

    Paraugs("{1|2}, {2|3} un {5|6} uz vienas taisnes",
            uzd="Kādā iedaļā sadalīt vienību un kur nokļūst katra daļa?",
            soli=[
                ("Saucēji: 2, 3 un 6",
                 "Vispirms izraksta, kas jāsaskaņo."),
                ("6 dalās ar 2, 3 un 6",
                 "Mazākais kopīgais dalāmais ir 6."),
                ("{1|2} = {3|6}",
                 "Abus locekļus reizina ar 3."),
                ("{2|3} = {4|6}",
                 "Abus locekļus reizina ar 2."),
                ("{5|6} paliek {5|6}",
                 "Tās saucējs jau ir 6."),
            ],
            atbilde="Vienību sadala 6 daļās; punkti ir {3|6}, {4|6} un {5|6}"),

    Zimejums("Visi trīs punkti vienā taisnē",
             taisne(0, 1, 1, [(3 / 6.0, "3/6"), (4 / 6.0, "4/6"),
                              (5 / 6.0, "5/6")],
                    virsraksts="Vienība sadalīta 6 daļās"),
             paskaidro="Tie paši trīs skaitļi, ko sauc par {1|2}, {2|3} un "
                       "{5|6}. Tagad uzreiz redz, kurš ir lielāks.",
             ievads="Kad saucējs visiem viens, secība ir acīmredzama."),

    Ievadi("Cik daļās sadalīt vienību?", [
        {"jaut": "Uz taisnes jāatliek {1|2} un {1|3}. Cik daļās sadalīt "
                 "vienību?",
         "atb": ["6"], "padoms": "Mazākais skaitlis, kas dalās ar 2 un 3."},
        {"jaut": "Jāatliek {1|2} un {1|4}. Cik daļās sadalīt vienību?",
         "atb": ["4"], "padoms": "4 jau dalās ar 2."},
        {"jaut": "Jāatliek {2|3} un {1|4}. Cik daļās sadalīt vienību?",
         "atb": ["12"], "padoms": "Mazākais skaitlis, kas dalās ar 3 un 4."},
        {"jaut": "Jāatliek {1|5} un {1|2}. Cik daļās sadalīt vienību?",
         "atb": ["10"], "padoms": "5 · 2."},
        {"jaut": "Vienība sadalīta 6 daļās. Kurā iedaļā nokļūst {2|3}?",
         "atb": ["4"], "padoms": "{2|3} = {4|6}."},
        {"jaut": "Vienība sadalīta 12 daļās. Kurā iedaļā nokļūst {3|4}?",
         "atb": ["9"], "padoms": "{3|4} = {9|12}."},
        {"jaut": "Vienība sadalīta 10 daļās. Kurā iedaļā nokļūst {1|2}?",
         "atb": ["5"], "padoms": "{1|2} = {5|10}."},
        {"jaut": "Jāatliek {1|4}, {1|6} un {1|2}. Cik daļās sadalīt vienību?",
         "atb": ["12"], "padoms": "12 dalās ar 4, 6 un 2."},
    ], pamats=4,
        ievads="Vispirms iedaļa, tikai tad punkti - citādi kaut kas "
               "neietilps."),

    Varianti("Kā izvēlēties iedaļu?", [
        {"jaut": "Kādam jābūt daļu skaitam, kurā sadala vienību?",
         "opcijas": ["Tādam, kas dalās ar visiem saucējiem",
                     "Tādam, kas dalās ar visiem skaitītājiem",
                     "Lielākajam no saucējiem",
                     "Visu saucēju summai"],
         "pareizi": 0,
         "padoms": "Iedaļai jāder katrai daļai."},
        {"jaut": "Jāatliek {1|3} un {1|6}. Vai der 6 iedaļas?",
         "opcijas": ["Der, jo 6 dalās gan ar 3, gan ar 6",
                     "Neder, vajag 18",
                     "Neder, vajag 9",
                     "Der tikai {1|6}"],
         "pareizi": 0,
         "padoms": "Lielākais saucējs reizēm jau ir kopīgais dalāmais."},
        {"jaut": "Jāatliek {1|2} un {1|5}. Vai der 20 iedaļas?",
         "opcijas": ["Der, bet 10 ir ērtāk", "Neder nekādā gadījumā",
                     "Der, un mazāk nevar", "Neder, vajag 7"],
         "pareizi": 0,
         "padoms": "Jebkurš kopīgais dalāmais der; mazākais ir skaidrāks."},
        {"jaut": "Vienību sadala 8 daļās. Kuru daļu uz tās *nevar* precīzi "
                 "atzīmēt?",
         "opcijas": ["{1|3}", "{1|2}", "{3|4}", "{5|8}"],
         "pareizi": 0,
         "padoms": "8 nedalās ar 3."},
        {"jaut": "Kāpēc uz vienas taisnes salīdzināt ir ērtāk?",
         "opcijas": ["Visi punkti ir vienā rindā un secība redzama uzreiz",
                     "Taisne ir garāka",
                     "Nevajag pārrakstīt daļas",
                     "Iedaļas kļūst lielākas"],
         "pareizi": 0,
         "padoms": "Divas taisnes vēl jāsalīdzina savā starpā."},
        {"jaut": "Jāatliek {2|3}, {3|4} un {1|2}. Cik iedaļu ir ērtākais "
                 "sadalījums?",
         "opcijas": ["12", "24", "9", "7"],
         "pareizi": 0,
         "padoms": "Mazākais skaitlis, kas dalās ar 3, 4 un 2."},
    ], pamats=4),

    Pasaule("Viens mērtrauks visai receptei",
            Ievadi("", [
                {"jaut": "Receptē ir {1|2} glāzes piena un {1|3} glāzes "
                         "eļļas. Cik iedaļu mērtraukam vajag vismaz?",
                 "atb": ["6"], "padoms": "6 dalās ar 2 un 3."},
                {"jaut": "Tāds trauks ir. Cik iedaļu ir {1|2} glāzes?",
                 "atb": ["3"], "padoms": "{1|2} = {3|6}."},
                {"jaut": "Tas pats trauks. Cik iedaļu ir {1|3} glāzes?",
                 "atb": ["2"], "padoms": "{1|3} = {2|6}."},
                {"jaut": "Receptē ir {3|4} un {2|3} glāzes. Cik iedaļu "
                         "mērtraukam vajag vismaz?",
                 "atb": ["12"], "padoms": "12 dalās ar 4 un 3."},
            ]),
            pavediens="virtuve",
            konteksts="Virtuvē neviens negrib trīs mērtraukus - grib vienu, "
                      "kas der visai receptei.",
            kapec="Iedaļu skaitu izvēlas tāpat kā iedaļu uz skaitļu taisnes."),

    Kopsavilkums([
        "Izvēlos iedaļu, kas dalās ar visiem dotajiem saucējiem.",
        "Pārrakstu katru daļu ar izvēlēto saucēju.",
        "Atlieku visas daļas uz vienas skaitļu taisnes.",
        "Skaidroju, kāpēc mazākais kopīgais dalāmais ir ērtākais.",
    ]),

    Majas([
        "Uzzīmē taisni no 0 līdz 1 ar 12 iedaļām un atzīmē uz tās {1|2}, "
        "{2|3} un {3|4}.",
        "Atrodi divas daļas, kurām der 10 iedaļas, bet neder 6.",
        "Padomā, vai ir daļas, kurām nederētu nekāds iedaļu skaits.",
    ]),
]
