# -*- coding: utf-8 -*-
"""1. klase, 126. stunda: «Vai pieraksts ir patiess bez rēķināšanas?»

Salīdzina summu vai starpību ar skaitli, neskaitot precīzi: 9 + 5 > 10, jo
9 + 1 jau ir 10; 15 − 8 < 10, jo atņemot vairāk nekā 5, paliek mazāk nekā
10. Spriest ar «<», «>», «=».
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Vai pieraksts ir patiess bez rēķināšanas?"

MERKIS = ("Šodien salīdzināsim summu vai starpību ar skaitli, neveicot "
          "precīzu aprēķinu.")


def _z(izteiksme, vertiba, skaitlis, padoms):
    zime = "<" if vertiba < skaitlis else ">" if vertiba > skaitlis else "="
    return {"jaut": "%s ? %d" % (izteiksme, skaitlis),
            "opcijas": ["<", ">", "="], "jaukt": False,
            "pareizi": ["<", ">", "="].index(zime), "padoms": padoms}


SATURS = [
    Sakums("9 + 5 ? 10 - vai jāskaita?",
           fakti=["9 + 1 jau ir 10.",
                  "5 ir vairāk nekā 1 - tātad vairāk nekā 10.",
                  "9 + 5 > 10 - bez precīza rēķina."]),

    Doma("Spried, neskaitot",
         "Salīdzini ar tuvu skaitli, ko zini.",
         soli=[
             "Atrodi viegli skaitāmu salīdzinājumu (10, 20).",
             "Vai pieskaitāmais lielāks vai mazāks?",
             "Izlem: <, > vai =.",
         ]),

    Varianti("Liec zīmi, neskaitot", [
        _z("9 + 5", 14, 10, "9 + 1 = 10, bet 5 > 1."),
        _z("15 − 8", 7, 10, "15 − 5 = 10, atņem vairāk."),
        _z("6 + 4", 10, 10, "Desmita draugi."),
        _z("18 − 2", 16, 20, "Jau 18 < 20."),
        _z("7 + 7", 14, 15, "7 + 8 būtu 15."),
        _z("12 + 5", 17, 16, "12 + 4 = 16, bet 5 > 4."),
    ], pamats=4),

    Varianti("Patiess?", [
        {"jaut": "8 + 3 > 10", "opcijas": ["Patiess", "Aplams"],
         "jaukt": False, "pareizi": 0, "padoms": "8 + 2 = 10."},
        {"jaut": "20 − 9 < 10", "opcijas": ["Patiess", "Aplams"],
         "jaukt": False, "pareizi": 1, "padoms": "20 − 10 = 10, 9 < 10."},
    ]),

    Pasaule("Vai pietiks 10 €?",
            Varianti("", [
                {"jaut": "Grāmata 7 €, krāsas 4 €. Vai kopā vairāk nekā "
                         "10 €?", "opcijas": ["Jā", "Nē"], "jaukt": False,
                 "pareizi": 0, "padoms": "7 + 3 = 10, 4 > 3."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā jāspriež ātri, bez papīra.",
            kapec="Salīdzināt var ātrāk, nekā izrēķināt."),

    Kopsavilkums([
        "Salīdzinu izteiksmi ar skaitli bez precīza rēķina.",
        "Izmantoju 10 un 20 kā orientierus.",
        "Lietoju <, >, =.",
    ]),

    Majas([
        "Izdomā 3 pierakstus, kuru patiesumu var noteikt bez rēķina.",
        "Pārbaudi ar precīzu rēķinu.",
        "Izskaidro mājiniekam.",
    ]),
]
