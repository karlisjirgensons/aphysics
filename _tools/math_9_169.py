# -*- coding: utf-8 -*-
"""9. klase, 169. stunda: «Cik veikli risinu skaitļu un izteiksmju uzdevumus?»

Eksāmena 1. daļas algebras sākums (2025. gada 1.-4. uzdevuma formāts):
pakāpes, noapaļošana, darbības ar pakāpēm, iekavu atvēršana, saīsinātās
reizināšanas formulas, kvadrātsaknes un procenti - bez kalkulatora.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti)

TEMA = "Cik veikli risinu skaitļu un izteiksmju uzdevumus?"

MERKIS = ("Risināsim eksāmena formāta uzdevumus par skaitļiem, procentiem un "
          "izteiksmēm.")

SATURS = [
    Sakums("Eksāmena pirmie 10 punkti - bez kalkulatora",
           fakti=["a^{−n} = {1|a^n}, a^m · a^n = a^{m + n}.",
                  "(a + b)^2 = a^2 + 2ab + b^2.",
                  "p % no skaitļa = {p|100} · skaitlis."]),

    Doma("Ātri un bez kļūdām",
         "Šie ir 1 punkta uzdevumi - tos risina ātri, bet pārbauda katru "
         "zīmi.",
         soli=[
             "Pakāpei ar negatīvu kāpinātāju - apgrieztais skaitlis.",
             "Decimāldaļas kvadrātā: ciparu skaits aiz komata divkāršojas.",
             "Iekavas atverot, reizini katru saskaitāmo - arī zīmi.",
             "Noapaļojot skaties tikai uz nākamo ciparu.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "5^3", "atb": ["125"], "padoms": "5 · 5 · 5."},
        {"jaut": "9^{−2} (daļskaitlis a/b)", "atb": ["1/81"],
         "tastatura": "text", "padoms": "{1|9^2}."},
        {"jaut": "(0,3)^2", "atb": ["0,09"], "padoms": "Divi cipari aiz "
                                                      "komata."},
        {"jaut": "√64 : √4", "atb": ["4"], "padoms": "8 : 2."},
        {"jaut": "(√7)^2 + √9", "atb": ["10"], "padoms": "7 + 3."},
    ]),

    Varianti("Izvēlies", [
        {"jaut": "Noapaļojot 36,74 līdz desmitdaļām, iegūst...",
         "opcijas": ["36,7", "36,8", "37", "36"],
         "pareizi": 0, "padoms": "Nākamais cipars 4 < 5."},
        {"jaut": "x^8 · x^2 = ...",
         "opcijas": ["x^{10}", "x^{16}", "x^6", "2x^{10}"],
         "pareizi": 0, "padoms": "Kāpinātājus saskaita."},
        {"jaut": "3(a − 6) = ...",
         "opcijas": ["3a − 18", "3a − 6", "3a + 18", "a − 18"],
         "pareizi": 0, "padoms": "Reizini abus saskaitāmos."},
        {"jaut": "(4 + b)^2 = ...",
         "opcijas": ["16 + 8b + b^2", "16 + b^2", "16 + 4b + b^2",
                     "8 + 8b + b^2"],
         "pareizi": 0, "padoms": "Neaizmirsti 2ab."},
    ]),

    Paraugs("2 punktu uzdevums",
            uzd="Izpildi darbības: (2c − 3)(5 + c) − 3c.",
            soli=[
                ("(2c − 3)(5 + c) = 10c + 2c^2 − 15 − 3c",
                 "Katrs ar katru."),
                ("= 2c^2 + 7c − 15", "Līdzīgie locekļi."),
                ("2c^2 + 7c − 15 − 3c = 2c^2 + 4c − 15", "Atņem 3c."),
            ],
            atbilde="2c^2 + 4c − 15"),

    Ievadi("Izteiksmes vērtība", [
        {"jaut": "(2c − 3)(5 + c) − 3c, ja c = 2", "atb": ["1"],
         "padoms": "1 · 7 − 6; vienkāršotā: 8 + 8 − 15 - tas pats."},
        {"jaut": "(a − 5)^2 − a^2, ja a = 3", "atb": ["−5"],
         "padoms": "4 − 9 vai −10a + 25."},
        {"jaut": "Cik ir 15 % no 240?", "atb": ["36"],
         "padoms": "240 : 100 · 15."},
    ]),

    Pasaule("Cena kāpj un krīt",
            Ievadi("", [
                {"jaut": "Telefons maksāja 450 €. Cenu palielināja par 10 %. "
                         "Jaunā cena (€)?", "atb": ["495"],
                 "padoms": "450 · 1,1."},
                {"jaut": "Tad jauno cenu samazināja par 10 %. Cena (€)?",
                 "atb": ["445,5", "445,50"], "padoms": "495 · 0,9."},
                {"jaut": "Par cik € tā ir mazāka nekā sākumā?",
                 "atb": ["4,5", "4,50"], "padoms": "450 − 445,5."},
            ]),
            pavediens="veikals",
            konteksts="Veikals vispirms paceļ cenu, pēc tam izsludina «−10 %» "
                      "atlaidi.",
            kapec="+10 % un −10 % nav tas pats skaitlis - procenti rēķinās "
                  "no dažādām cenām."),

    Kopsavilkums([
        "Rēķinu pakāpes, saknes un procentus bez kalkulatora.",
        "Atveru iekavas un lietoju saīsinātās reizināšanas formulas.",
        "Pārbaudu izteiksmi, ievietojot skaitli.",
    ]),

    Majas([
        "Atrisini 10 izteiksmju uzdevumus no iepriekšējo gadu eksāmeniem.",
        "Izveido sev «formulu kartīti» ar pakāpju un saīsinātās "
        "reizināšanas formulām.",
        "Pārbaudi katru izteiksmi, ievietojot x = 1.",
    ]),
]
