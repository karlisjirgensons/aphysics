# -*- coding: utf-8 -*-
"""9. klase, 68. stunda: «Kā formulas paātrina rēķinus?»

Galvas rēķināšanas triki no formulām: 99^2, 51^2, 38 · 42, 1002^2 − 998^2.
Skolēns sacenšas ar kalkulatoru un pamato, kāpēc triks strādā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā formulas paātrina rēķinus?"

MERKIS = ("Lietosim formulas skaitliskos aprēķinos un pamatosim to "
          "izdevīgumu.")

SATURS = [
    Sakums("99² - ātrāk nekā kalkulators?",
           zimejums=restis([["99²", "(100 − 1)²"],
                            ["", "10 000 − 200 + 1"], ["", "9801"]]),
           paraksts="Trīs vienkārši soļi galvā.",
           fakti=["Skaitli tuvu apaļam raksta kā 100 − 1 vai 50 + 1.",
                  "Divu skaitļu reizinājums ap vidu - kvadrātu starpība.",
                  "Lielu kvadrātu starpību - sadala reizinātājos."]),

    Doma("Trīs triki",
         "(a ± b)^2 skaitļa kvadrātam, (a − b)(a + b) reizinājumam, "
         "a^2 − b^2 starpībai.",
         soli=[
             "51^2 = (50 + 1)^2 = 2500 + 100 + 1 = 2601.",
             "38 · 42 = (40 − 2)(40 + 2) = 1600 − 4 = 1596.",
             "73^2 − 27^2 = (73 − 27)(73 + 27) = 46 · 100 = 4600.",
         ]),

    Paraugs("Liels skaitlis",
            uzd="Aprēķini 1002^2 − 998^2 bez kalkulatora.",
            soli=[
                ("(1002 − 998)(1002 + 998)", "Kvadrātu starpība."),
                ("= 4 · 2000 = 8000", "Viegli."),
            ],
            atbilde="8000"),

    Ievadi("Rēķini galvā", [
        {"jaut": "41^2 = ?", "atb": ["1681"], "padoms": "1600 + 80 + 1."},
        {"jaut": "59^2 = ?", "atb": ["3481"], "padoms": "3600 − 120 + 1."},
        {"jaut": "23 · 17 = ?", "atb": ["391"], "padoms": "400 − 9."},
        {"jaut": "65^2 − 35^2 = ?", "atb": ["3000", "3 000"],
         "padoms": "30 · 100."},
        {"jaut": "0,99^2 = ?", "atb": ["0,9801"], "padoms": "(1 − 0,01)^2."},
        {"jaut": "205^2 = ?", "atb": ["42025", "42 025"],
         "padoms": "40 000 + 2000 + 25."},
    ], pamats=4),

    Varianti("Kurš triks?", [
        {"jaut": "47 · 53",
         "opcijas": ["(50 − 3)(50 + 3)", "(47 + 53)^2", "47^2 + 53^2",
                     "(50 + 3)^2"],
         "pareizi": 0, "padoms": "Simetriski ap 50."},
        {"jaut": "88^2",
         "opcijas": ["(90 − 2)^2", "(90 − 2)(90 + 2)", "90^2 − 2^2",
                     "80^2 + 8^2"],
         "pareizi": 0, "padoms": "Starpības kvadrāts."},
    ]),

    Pasaule("Sacīkstes ar kalkulatoru",
            Kustiba("", [
                {"jaut": "Aprēķini 21 · 19 galvā. Cik tas ir?",
                 "atb": 399, "sakums": 350, "beigas": 450, "iedala": 25,
                 "mers": "", "merkis": "399?", "objekts": "Tu",
                 "padoms": "400 − 1."},
                {"jaut": "Aprēķini 32 · 28 galvā.",
                 "atb": 896, "sakums": 850, "beigas": 950, "iedala": 25,
                 "mers": "", "merkis": "896?", "objekts": "Tu",
                 "padoms": "900 − 4."},
            ]),
            pavediens="speles",
            konteksts="Viens raksta kalkulatorā, otrs rēķina ar formulu - "
                      "kurš ātrāks?",
            kapec="Formulas ir ātrākas nekā pogas."),

    Kopsavilkums([
        "Rēķinu kvadrātus ar (a ± b)^2.",
        "Reizinu simetriskus skaitļus ar kvadrātu starpību.",
        "Pamatoju, kāpēc triks ir precīzs.",
    ]),

    Majas([
        "Aprēķini galvā: 71^2, 29^2, 64 · 56.",
        "Izdomā savu triku un paskaidro to ar formulu.",
        "Sacenties mājās ar kādu, kam ir kalkulators.",
    ]),
]
