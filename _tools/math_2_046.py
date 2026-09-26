# -*- coding: utf-8 -*-
"""2. klase, 46. stunda: «Kur radusies kļūda?»

Kļūdu meklēšana gatavā risinājumā. Biežākās kļūdas 100 apjomā ir trīs:
aizmirsts pārnestais desmits, nesamazināti desmiti pēc aizņemšanās un
atņemts mazākais no lielākā «otrādi» (8 − 3 vietā 3 − 8).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, stabins)

TEMA = "Kur radusies kļūda?"

MERKIS = ("Šodien atradīsim kļūdu dotajā risinājumā un izlabosim to.")

_VEIDI = ["aizmirsts pārnestais desmits", "nesamazināti desmiti",
          "atņemts otrādi"]

SATURS = [
    Sakums("Robots rēķina ātri, bet kļūdās. Atrodi, kur!",
           zimejums=stabins(46, 38),
           paraksts="Pareizi ir 84. Kāpēc robots uzrakstīja 74?",
           fakti=["Kļūdas nav nejaušas - tās atkārtojas.",
                  "Kas zina biežākās kļūdas, tās vairs nedara."]),

    Doma("Trīs biežākās kļūdas",
         "Kļūdu atrod, pārbaudot katru soli pēc kārtas.",
         soli=[
             "46 + 38 = 74 - aizmirsts pārnestais desmits.",
             "52 − 18 = 44 - aizņēmās, bet nesamazināja desmitus.",
             "63 − 28 = 45 - atņēma 3 no 8 otrādi.",
             "Pārbaude ar pretējo darbību parāda, ka kļūda ir.",
         ]),

    Varianti("Kāda kļūda?", [
        {"jaut": "57 + 26 = 73", "opcijas": _VEIDI, "jaukt": False,
         "pareizi": 0, "padoms": "7 + 6 = 13."},
        {"jaut": "71 − 35 = 44", "opcijas": _VEIDI, "jaukt": False,
         "pareizi": 2, "padoms": "5 − 1 = 4 - otrādi."},
        {"jaut": "80 − 23 = 67", "opcijas": _VEIDI, "jaukt": False,
         "pareizi": 1, "padoms": "10 − 3 = 7, bet desmiti 7 − 2."},
        {"jaut": "38 + 45 = 73", "opcijas": _VEIDI, "jaukt": False,
         "pareizi": 0, "padoms": "8 + 5 = 13."},
        {"jaut": "54 − 29 = 35", "opcijas": _VEIDI, "jaukt": False,
         "pareizi": 1, "padoms": "14 − 9 = 5, desmiti 4 − 2 = 2."},
        {"jaut": "92 − 47 = 55", "opcijas": _VEIDI, "jaukt": False,
         "pareizi": 2, "padoms": "7 − 2 = 5 - otrādi."},
    ], pamats=4),

    Ievadi("Izlabo", [
        {"jaut": "57 + 26 = 73. Pareizi ir?", "atb": ["83"],
         "padoms": "Pārnes desmitu."},
        {"jaut": "71 − 35 = 44. Pareizi ir?", "atb": ["36"],
         "padoms": "11 − 5, 6 − 3."},
        {"jaut": "80 − 23 = 67. Pareizi ir?", "atb": ["57"],
         "padoms": "10 − 3, 7 − 2."},
        {"jaut": "38 + 45 = 73. Pareizi ir?", "atb": ["83"],
         "padoms": "13 - pārnes 1."},
    ]),

    Pasaule("Kurš rēķins veikalā nav pareizs?",
            Varianti("", [
                {"jaut": "Kurā čekā ir kļūda?",
                 "opcijas": ["26 € + 17 € = 33 €", "15 € + 24 € = 39 €",
                             "40 € + 35 € = 75 €"], "pareizi": 0,
                 "padoms": "6 + 7 = 13."},
                {"jaut": "Cik jābūt pareizi?",
                 "opcijas": ["43 €", "33 €", "313 €"], "pareizi": 0,
                 "padoms": "26 + 17."},
            ]),
            pavediens="veikals",
            konteksts="Tirgū cenas saskaita uz papīra.",
            kapec="Ātra pārbaude pasargā no zaudējuma."),

    Kopsavilkums([
        "Zinu biežākās kļūdas saskaitīšanā un atņemšanā.",
        "Atrodu kļūdu dotā risinājumā.",
        "Izlaboju un pārbaudu.",
    ]),

    Majas([
        "Pārbaudi savas pēdējās nedēļas uzdevumus.",
        "Vai atradi kādu no trim biežākajām kļūdām?",
        "Izdomā «robota kļūdu» mājiniekam.",
    ]),
]
