# -*- coding: utf-8 -*-
"""2. klase, 153. stunda: «Cik bērniem pietiks?»

Otra dalīšanas nozīme: dala pa 3, 4 vai 5 un skaita, cik daļu sanāk.
«30 zīmuļi pa 5 katram - cik bērniem?» 30 : 5 = 6. Atšķirībā no
iepriekšējās stundas nezināms ir daļu skaits.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Cik bērniem pietiks?"

MERKIS = ("Šodien dalīsim daļās pa 3, 4 vai 5 un noteiksim daļu skaitu.")

_DIVAS = ["cik katram", "cik daļu"]

SATURS = [
    Sakums("30 zīmuļi - katram bērnam pa 5. Cik bērniem pietiks?",
           zimejums=bildes([[("zimulis", 5)]] * 6),
           paraksts="6 kaudzītes pa 5 - 30 : 5 = 6.",
           fakti=["Liek pa 5 kaudzītēs, līdz beidzas.",
                  "Saskaita kaudzītes.",
                  "Pietiks 6 bērniem."]),

    Doma("Pa ... katram",
         "Ja zināms, cik katram, dalījums pasaka, cik daļu.",
         soli=[
             "Atskaiti pa 5 un noliec kaudzītē.",
             "Atkārto, līdz nekas nepaliek.",
             "Saskaiti kaudzītes.",
             "Pieraksti: 30 : 5 = 6.",
         ]),

    Ievadi("Cik daļu?", [
        {"jaut": "20 āboli pa 4 maisiņā. Cik maisiņu?", "atb": ["5"],
         "padoms": "4 · 5 = 20."},
        {"jaut": "27 bērni pa 3 laivā. Cik laivu?", "atb": ["9"],
         "padoms": "3 · 9 = 27."},
        {"jaut": "40 kūciņas pa 5 kastītē. Cik kastīšu?", "atb": ["8"],
         "padoms": "5 · 8 = 40."},
        {"jaut": "36 krēsli pa 4 pie galda. Cik galdu?", "atb": ["9"],
         "padoms": "4 · 9 = 36."},
        {"jaut": "18 riteņi - trīsriteņi. Cik trīsriteņu?", "atb": ["6"],
         "padoms": "3 · 6 = 18."},
        {"jaut": "45 pirksti - rokas pa 5. Cik roku?", "atb": ["9"],
         "padoms": "5 · 9 = 45."},
    ], pamats=4),

    Varianti("Ko jautā?", [
        {"jaut": "«24 ogas 4 bērniem vienādi.»", "opcijas": _DIVAS,
         "jaukt": False, "pareizi": 0, "padoms": "Bērnu skaits zināms."},
        {"jaut": "«24 ogas pa 4 katram.»", "opcijas": _DIVAS,
         "jaukt": False, "pareizi": 1, "padoms": "Bērnu skaits nezināms."},
        {"jaut": "Abās situācijās 24 : 4 = ?", "opcijas": ["6", "20", "28"],
         "pareizi": 0, "padoms": "4 · 6 = 24."},
    ]),

    Pasaule("Laivu noma",
            Ievadi("", [
                {"jaut": "Laivā sēž 4 cilvēki. Ekskursijā 32 cilvēki. Cik "
                         "laivu vajag?", "atb": ["8"], "padoms": "32 : 4."},
                {"jaut": "Viena laiva maksā 5 €. Cik maksā visas?",
                 "atb": ["40"], "mers": "€", "padoms": "8 · 5."},
            ]),
            pavediens="celojums",
            konteksts="Pa Gauju brauc ar laivām.",
            kapec="Dalīšana pasaka, cik laivu nomāt."),

    Kopsavilkums([
        "Dalu pa 3, 4 vai 5.",
        "Nosaku, cik daļu sanāk.",
        "Atšķiru abas dalīšanas nozīmes.",
    ]),

    Majas([
        "Sadali 20 karotes pa 4 kaudzītēs. Cik kaudzīšu?",
        "Sadali tās pašas pa 5.",
        "Pieraksti abus dalījumus.",
    ]),
]
