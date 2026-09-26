# -*- coding: utf-8 -*-
"""1. klase, 67. stunda: «Ko var nopirkt par vienu eiro?»

1 eiro = 100 centu. Cenas centos salīdzina ar 100: ja cena mazāka nekā
100 c, par eiro var nopirkt. Kas ir tieši 100 c - arī var.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, monetas)

TEMA = "Ko var nopirkt par vienu eiro?"

MERKIS = ("Šodien salīdzināsim cenas centos un noteiksim, ko var nopirkt "
          "par vienu eiro.")

SATURS = [
    Sakums("Tev ir 1 eiro. Vai pietiek bulciņai par 65 centiem?",
           zimejums=monetas(["1 €"]),
           paraksts="1 € = 100 c. 65 < 100 - pietiek.",
           fakti=["1 eiro ir 100 centu.",
                  "Ja cena mazāka nekā 100 c - pietiek.",
                  "Ja lielāka - nepietiek."]),

    Doma("Salīdzini ar 100",
         "Par eiro var nopirkt visu, kas maksā ne vairāk kā 100 centu.",
         soli=[
             "Nolasi cenu centos.",
             "Salīdzini ar 100.",
             "Mazāka vai vienāda - pietiek.",
         ]),

    Varianti("Vai pietiek ar 1 €?", [
        {"jaut": "Zīmulis 45 c", "opcijas": ["pietiek", "nepietiek"],
         "jaukt": False, "pareizi": 0, "padoms": "45 < 100."},
        {"jaut": "Grāmata 350 c (3 € 50 c)",
         "opcijas": ["pietiek", "nepietiek"], "jaukt": False, "pareizi": 1,
         "padoms": "Vairāk nekā 100 c."},
        {"jaut": "Ābols 30 c", "opcijas": ["pietiek", "nepietiek"],
         "jaukt": False, "pareizi": 0, "padoms": "30 < 100."},
        {"jaut": "Sula 100 c", "opcijas": ["pietiek", "nepietiek"],
         "jaukt": False, "pareizi": 0, "padoms": "Tieši 1 €."},
    ]),

    Ievadi("Cik centu?", [
        {"jaut": "Cik centu kopā?", "zim": monetas(["50 c", "20 c", "10 c"]),
         "atb": ["80"], "padoms": "50 + 20 + 10."},
        {"jaut": "Cik centu kopā?", "zim": monetas(["50 c", "50 c"]),
         "atb": ["100"], "padoms": "Tas ir 1 €."},
        {"jaut": "Cena 70 c. Cik paliek no 1 €?", "atb": ["30"],
         "padoms": "No 70 līdz 100."},
    ]),

    Pasaule("Skolas kafejnīcā",
            Varianti("", [
                {"jaut": "Tev 1 €. Bulciņa 60 c, sula 50 c. Vai var nopirkt "
                         "abus?", "opcijas": ["Nē - kopā 110 c", "Jā"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "60 + 50 = 110 > 100."},
                {"jaut": "Bulciņa 60 c un ābols 30 c?",
                 "opcijas": ["Jā - 90 c", "Nē"], "jaukt": False,
                 "pareizi": 0, "padoms": "60 + 30 = 90."},
            ]),
            pavediens="veikals",
            konteksts="Starpbrīdī var nopirkt uzkodu par savu eiro.",
            kapec="Salīdzinot ar 100 c, zini, vai pietiks."),

    Kopsavilkums([
        "Zinu, ka 1 € = 100 c.",
        "Salīdzinu cenas centos ar 100.",
        "Izlemju, ko var nopirkt par vienu eiro.",
    ]),

    Majas([
        "Atrodi veikalā vai reklāmā 3 lietas lētākas par 1 €.",
        "Saskaiti mājās centu monētas.",
        "Vai tev pietiktu eiro saldējumam?",
    ]),
]
