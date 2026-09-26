# -*- coding: utf-8 -*-
"""2. klase, 152. stunda: «Kā sadalīt konfektes taisnīgi?»

Dalīšana vienādās daļās ar 3, 4 un 5: izdala pa vienai pārmaiņus, līdz
beidzas, tad skaita vienu daļu. 15 : 3 = 5. Dalīšanu pieraksta ar «:».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, bildes)

TEMA = "Kā sadalīt konfektes taisnīgi?"

MERKIS = ("Šodien praktiski dalīsim daudzumu 3, 4 vai 5 vienādās daļās un "
          "pierakstīsim dalījumu.")


def _dalas(n, katra, ikona="ripina"):
    return bildes([[(ikona, katra)]] * n)


SATURS = [
    Sakums("Kā 15 konfektes sadalīt 3 draugiem, lai nevienam nav mazāk?",
           zimejums=_dalas(3, 5),
           paraksts="15 : 3 = 5 - katram 5.",
           fakti=["Izdala pa vienai pēc kārtas.",
                  "Kad beidzas - katram vienādi.",
                  "Pieraksta: 15 : 3 = 5."]),

    Doma("Vienādās daļās",
         "Dalīt vienādās daļās: katram tikpat, un nekas nepaliek pāri.",
         soli=[
             "Izliec tik šķīvju, cik daļu: 3.",
             "Liec pa vienai uz katra pēc kārtas.",
             "Kad beidzas - saskaiti vienu šķīvi.",
             "Pieraksti: 15 : 3 = 5.",
         ]),

    Slidnis("20 dala 4 daļās", [
        {"v": "1. kārta", "teksts": "Katram pa 1 - izdalīti 4.",
         "zim": _dalas(4, 1)},
        {"v": "3. kārta", "teksts": "Katram pa 3 - izdalīti 12.",
         "zim": _dalas(4, 3)},
        {"v": "20 : 4 = 5", "teksts": "Katram pa 5 - visi 20.",
         "zim": _dalas(4, 5)},
    ]),

    Ievadi("Sadali", [
        {"jaut": "12 : 3 = ?", "zim": _dalas(3, 4), "atb": ["4"],
         "padoms": "Katrā rindā 4."},
        {"jaut": "20 : 5 = ?", "zim": _dalas(5, 4), "atb": ["4"],
         "padoms": "5 rindas pa 4."},
        {"jaut": "16 : 4 = ?", "atb": ["4"], "padoms": "4 · 4 = 16."},
        {"jaut": "21 : 3 = ?", "atb": ["7"], "padoms": "3 · 7 = 21."},
        {"jaut": "25 : 5 = ?", "atb": ["5"], "padoms": "5 · 5 = 25."},
        {"jaut": "24 : 4 = ?", "atb": ["6"], "padoms": "4 · 6 = 24."},
    ], pamats=4),

    Varianti("Taisnīgi?", [
        {"jaut": "18 konfektes 3 bērniem: 7, 6, 5. Taisnīgi?",
         "opcijas": ["Nē - katram jābūt 6", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "18 : 3 = 6."},
        {"jaut": "20 zīmuļi 5 bērniem: katram 4. Taisnīgi?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "5 · 4 = 20."},
    ]),

    Pasaule("Dzimšanas dienas konfektes",
            Ievadi("", [
                {"jaut": "Klasē 24 konfektes un 4 galdi. Cik uz katra galda?",
                 "atb": ["6"], "padoms": "24 : 4."},
                {"jaut": "Pie katra galda 3 bērni. Cik konfekšu katram?",
                 "atb": ["2"], "padoms": "6 : 3."},
            ]),
            pavediens="skola",
            konteksts="Dzimšanas dienā jubilārs cienā klasi.",
            kapec="Taisnīga dalīšana - visi apmierināti."),

    Kopsavilkums([
        "Dalu daudzumu 3, 4 vai 5 vienādās daļās.",
        "Pierakstu dalījumu ar «:».",
        "Pārbaudu, vai visiem vienādi.",
    ]),

    Majas([
        "Sadali 20 riekstus 4 mājiniekiem vienādi.",
        "Pieraksti dalījumu.",
        "Pamēģini sadalīt 5 cilvēkiem.",
    ]),
]
