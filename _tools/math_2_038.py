# -*- coding: utf-8 -*-
"""2. klase, 38. stunda: «Kurš paņēmiens tev ērtākais?»

Viena summa - vairāki ceļi: pa daļām, stabiņā, uz taisnes, ar apaļošanu
(49 + 26 = 50 + 25). Stundā skolēns izvēlas piemērotāko katram piemēram un
pamato - tā pati prasme, ko eksāmenā prasa kā «izvēlies racionālu ceļu».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, taisne)

TEMA = "Kurš paņēmiens tev ērtākais?"

MERKIS = ("Šodien izvēlēsimies piemērotāko saskaitīšanas paņēmienu "
          "konkrētam piemēram un pamatosim izvēli.")

SATURS = [
    Sakums("Kā izrēķināt 49 + 26 galvā dažās sekundēs?",
           zimejums=taisne(45, 80, 5, bultas=[(49, 50, "+1"),
                                               (50, 75, "+25")]),
           paraksts="49 + 1 = 50, 50 + 25 = 75.",
           fakti=["49 ir gandrīz 50.",
                  "Paņem 1 no 26 un atdod 49.",
                  "50 + 25 ir viegli!"]),

    Doma("Paņēmieni",
         "Nav viena pareizā ceļa - izvēlas vienkāršāko šim piemēram.",
         soli=[
             "Pa daļām: desmiti ar desmitiem, vieni ar vieniem.",
             "Apaļošana: ja skaitlis beidzas ar 8 vai 9, papildini līdz "
             "desmitam.",
             "Stabiņā: ja skaitļi neērti.",
             "Uz taisnes: ja gribi redzēt lēcienus.",
         ]),

    Paraugs("Cik ir 38 + 27?",
            uzd="Izmanto apaļošanu.",
            soli=[("38 + 2 = 40", "Paņem 2 no 27."),
                  ("40 + 25 = 65", "Pieskaita atlikušo.")],
            atbilde="65"),

    Varianti("Kurš ceļš ērtāks?", [
        {"jaut": "59 + 23",
         "opcijas": ["60 + 22", "stabiņā", "skaitīt pa vienam"],
         "pareizi": 0, "padoms": "59 ir gandrīz 60."},
        {"jaut": "40 + 35",
         "opcijas": ["desmiti ar desmitiem: 70 + 5", "stabiņā ar "
                     "pārnešanu", "skaitīt pa vienam"],
         "pareizi": 0, "padoms": "40 jau ir apaļš."},
        {"jaut": "25 + 25", "opcijas": ["dubulti: 50", "stabiņā",
                                        "uz taisnes pa 1"],
         "pareizi": 0, "padoms": "Divi vienādi."},
        {"jaut": "28 + 48",
         "opcijas": ["30 + 46 vai stabiņā", "skaitīt pa vienam",
                     "dubulti"], "pareizi": 0,
         "padoms": "28 ir gandrīz 30."},
    ]),

    Ievadi("Rēķini ērtāk", [
        {"jaut": "29 + 35 = ?", "atb": ["64"], "padoms": "30 + 34."},
        {"jaut": "48 + 17 = ?", "atb": ["65"], "padoms": "50 + 15."},
        {"jaut": "35 + 35 = ?", "atb": ["70"], "padoms": "Dubulti."},
        {"jaut": "19 + 58 = ?", "atb": ["77"], "padoms": "20 + 57."},
        {"jaut": "39 + 39 = ?", "atb": ["78"], "padoms": "40 + 40 − 2."},
        {"jaut": "67 + 18 = ?", "atb": ["85"], "padoms": "67 + 20 − 2."},
    ], pamats=4),

    Pasaule("Kuģītis uz ezera",
            Ievadi("", [
                {"jaut": "No rīta kuģītī brauca 49 pasažieri, pēcpusdienā - "
                         "38. Cik kopā?", "atb": ["87"],
                 "padoms": "50 + 37."},
                {"jaut": "Vakarā vēl 9. Cik visas dienas laikā?",
                 "atb": ["96"], "padoms": "87 + 10 − 1."},
            ]),
            pavediens="celojums",
            konteksts="Pa Alūksnes ezeru vasarā kursē kuģītis.",
            kapec="Kapteinis skaita pasažierus galvā - ērtākajā veidā."),

    Kopsavilkums([
        "Zinu vairākus saskaitīšanas paņēmienus.",
        "Izvēlos ērtāko konkrētajam piemēram.",
        "Pamatoju savu izvēli.",
    ]),

    Majas([
        "Izrēķini 49 + 27 trīs veidos.",
        "Kurš bija ātrākais?",
        "Iemāci savu paņēmienu mājiniekam.",
    ]),
]
