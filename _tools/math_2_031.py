# -*- coding: utf-8 -*-
"""2. klase, 31. stunda: «Kā atcerēties summas?»

Summas 20 apjomā iegaumē nevis pa vienai, bet ar atbalsta punktiem:
dubulti (7 + 7), gandrīz dubulti (7 + 8 = 7 + 7 + 1), desmita draugi
(3 + 7) un «+ 9 ir + 10 − 1». Katrs izvēlas savu paņēmienu un to trenē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kā atcerēties summas?"

MERKIS = ("Šodien iepazīsim paņēmienus summu atcerēšanai un trenēsim "
          "summas un starpības 20 apjomā.")

SATURS = [
    Sakums("Kā čempioni rēķina galvā ātrāk nekā ar kalkulatoru?",
           zimejums=restis([["1 + 9", "2 + 8", "3 + 7", "4 + 6", "5 + 5"]],
                           "desmita draugi"),
           fakti=["Viņi atceras dažas summas un pārējās izveido no tām.",
                  "Desmita draugi kopā dod 10.",
                  "Dubulti: 6 + 6, 7 + 7, 8 + 8."]),

    Doma("Četri triki",
         "Nezināmu summu var atrast no tās, ko jau zini.",
         soli=[
             "Dubulti: 7 + 7 = 14.",
             "Gandrīz dubulti: 7 + 8 = 7 + 7 + 1 = 15.",
             "Desmita draugi: 3 + 7 = 10, tātad 13 + 7 = 20.",
             "Pieskaiti 9: + 10 un − 1. 6 + 9 = 16 − 1 = 15.",
         ]),

    Varianti("Kurš triks der?", [
        {"jaut": "8 + 9", "opcijas": ["gandrīz dubulti: 8 + 8 + 1",
                                      "desmita draugi", "nekas neder"],
         "pareizi": 0, "padoms": "8 un 9 ir blakus."},
        {"jaut": "5 + 9", "opcijas": ["+ 10 − 1", "dubulti",
                                      "gandrīz dubulti"],
         "pareizi": 0, "padoms": "Pieskaiti 10 un atņem 1."},
        {"jaut": "14 + 6", "opcijas": ["desmita draugi: 4 + 6",
                                       "dubulti", "+ 10 − 1"],
         "pareizi": 0, "padoms": "4 + 6 = 10."},
        {"jaut": "6 + 7", "opcijas": ["gandrīz dubulti: 6 + 6 + 1",
                                      "+ 10 − 1", "desmita draugi"],
         "pareizi": 0, "padoms": "6 un 7 ir blakus."},
    ]),

    Ievadi("Trenējies", [
        {"jaut": "7 + 7 = ?", "atb": ["14"], "padoms": "Dubulti."},
        {"jaut": "7 + 8 = ?", "atb": ["15"], "padoms": "7 + 7 + 1."},
        {"jaut": "9 + 7 = ?", "atb": ["16"], "padoms": "7 + 10 − 1."},
        {"jaut": "12 + 8 = ?", "atb": ["20"], "padoms": "2 + 8 = 10."},
        {"jaut": "16 − 8 = ?", "atb": ["8"], "padoms": "8 + 8 = 16."},
        {"jaut": "15 − 7 = ?", "atb": ["8"], "padoms": "7 + 8 = 15."},
        {"jaut": "9 + 6 = ?", "atb": ["15"], "padoms": "6 + 10 − 1."},
        {"jaut": "18 − 9 = ?", "atb": ["9"], "padoms": "9 + 9 = 18."},
    ], pamats=6),

    Pasaule("Punkti galda spēlē",
            Ievadi("", [
                {"jaut": "Metienā uzkrita 6 un 6. Cik punktu?", "atb": ["12"],
                 "padoms": "Dubulti."},
                {"jaut": "Tad uzkrita 5 un 6. Cik punktu šajā metienā?",
                 "atb": ["11"], "padoms": "5 + 5 + 1."},
                {"jaut": "Cik punktu abos metienos kopā?", "atb": ["23"],
                 "padoms": "12 + 11."},
            ]),
            pavediens="speles",
            konteksts="Galda spēlē met divus kauliņus un saskaita punktus.",
            kapec="Kas zina summas no galvas, spēlē ātrāk."),

    Kopsavilkums([
        "Zinu dubultus un desmita draugus.",
        "Lietoju gandrīz dubultus un «+ 10 − 1».",
        "Izvēlos savu paņēmienu un trenējos.",
    ]),

    Majas([
        "Izveido kartītes ar 10 summām, kas tev grūtas.",
        "Otrā pusē uzraksti atbildes.",
        "Trenējies ar mājinieku 5 minūtes katru dienu.",
    ]),
]
