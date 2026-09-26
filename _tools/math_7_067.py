# -*- coding: utf-8 -*-
"""7. klase, 67. stunda: «Kurš tarifs ir izdevīgāks?»

Divi tarifi ir divas lineāras funkcijas. Krustpunktā tie maksā vienādi;
pa kreisi izdevīgāks viens, pa labi - otrs. Stunda salīdzina tarifus ar
grafiku un formulu un izvēlas atkarībā no lietošanas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, restis)

TEMA = "Kurš tarifs ir izdevīgāks?"

MERKIS = ("Salīdzināsim divus maksājumu tarifus, lietojot grafikus un "
          "formulas.")

_TARIFI = plakne(grafiki=[(0.3, 5, "A"), (0.55, 0, "B")],
                 punkti=[(20, 11, "(20; 11)")],
                 no_x=0, lidz_x=40, no_y=0, lidz_y=24, solis=5, solis_y=3,
                 x_nos="min", y_nos="€")

SATURS = [
    Sakums("Koplietošanas auto: divi tarifi",
           zimejums=_TARIFI,
           paraksts="A: 5 € + 0,30 €/min. B: 0,55 €/min.",
           fakti=["Īsam braucienam izdevīgāks B.",
                  "Garam - A.",
                  "Robeža - krustpunktā (20 min)."]),

    Doma("Krustpunkts - robeža",
         "Divus tarifus salīdzina, uzrakstot katram formulu un atrodot "
         "argumentu, kurā tie maksā vienādi. Pa vienu pusi izdevīgāks viens, "
         "pa otru - otrs.",
         soli=[
             "Uzraksti abu tarifu formulas.",
             "Pielīdzini tās un atrodi krustpunktu.",
             "Pārbaudi vienu argumentu katrā pusē.",
             "Secini: līdz ... izdevīgāks A, pēc ... - B.",
         ],
         pieze="Grafikā izdevīgāks ir tas tarifs, kura taisne tajā vietā "
               "ir zemāk."),

    Paraugs("Atrodi robežu",
            uzd="A: S = 0,3t + 5; B: S = 0,55t. Pie kāda t tie maksā "
                "vienādi?",
            soli=[
                ("0,3t + 5 = 0,55t", "Pielīdzina."),
                ("5 = 0,25t", "Atņem 0,3t."),
                ("t = 20 (min)", "Dala."),
                ("t = 10: A - 8 €, B - 5,5 €; izdevīgāks B", "Pārbaude."),
            ],
            atbilde="Līdz 20 min izdevīgāks B, pēc 20 min - A."),

    Zimejums("Tarifu tabula",
             restis([["min", "10", "20", "30", "40"],
                     ["A, €", "8", "11", "14", "17"],
                     ["B, €", "5,5", "11", "16,5", "22"]]),
             paskaidro="Pie 20 min - vienādi."),

    Ievadi("Salīdzini", [
        {"jaut": "Cik € maksā 30 min ar A?",
         "atb": ["14"], "padoms": "9 + 5."},
        {"jaut": "Cik € maksā 30 min ar B?",
         "atb": ["16,5"], "padoms": "0,55 · 30."},
        {"jaut": "Cik € ietaupa, 40 min braucot ar A, nevis B?",
         "atb": ["5"], "padoms": "22 − 17."},
        {"jaut": "Tarifi: C = 2x + 10, D = 4x. Pie kāda x vienādi?",
         "atb": ["5"], "padoms": "2x = 10."},
    ]),

    Varianti("Izvēlies tarifu", [
        {"jaut": "Brauciens 12 min. Kurš izdevīgāks?",
         "opcijas": ["B", "A", "Vienādi"],
         "pareizi": 0, "jaukt": False, "padoms": "Mazāk par 20 min."},
        {"jaut": "Brauciens 45 min. Kurš izdevīgāks?",
         "opcijas": ["B", "A", "Vienādi"],
         "pareizi": 1, "jaukt": False, "padoms": "Vairāk par 20 min."},
        {"jaut": "Grafikā: kurš tarifs izdevīgāks pa kreisi no krustpunkta?",
         "opcijas": ["Tas, kura taisne tur ir zemāk",
                     "Tas, kura taisne stāvāka",
                     "Tas, kura b lielāks", "Vienmēr A"],
         "pareizi": 0,
         "padoms": "Zemāk - lētāk."},
    ]),

    Pasaule("Sporta zāle",
            Ievadi("", [
                {"jaut": "Zāle 1: 30 € mēnesī neierobežoti. Zāle 2: 4 € par "
                         "apmeklējumu. Pie cik apmeklējumiem vienādi (var "
                         "būt daļskaitlis)?",
                 "atb": ["7,5"], "padoms": "4n = 30."},
                {"jaut": "Tu ej 2 reizes nedēļā (8 mēnesī). Cik € ar Zāli 2?",
                 "atb": ["32"], "padoms": "4 · 8."},
                {"jaut": "Kura zāle izdevīgāka 8 reizēm - «1» vai «2»?",
                 "atb": ["1"], "padoms": "30 < 32."},
            ]),
            pavediens="sports",
            konteksts="Abonements vai maksa par reizi - klasisks divu "
                      "tarifu salīdzinājums.",
            kapec="Krustpunkts saka, kad abonements atmaksājas."),

    Kopsavilkums([
        "Uzrakstu tarifu formulas.",
        "Atrodu krustpunktu, pielīdzinot formulas.",
        "Nosaku, kurš tarifs izdevīgāks katrā pusē.",
        "Lasu izdevīgumu no grafika.",
    ]),

    Majas([
        "Salīdzini divus mobilā sakaru tarifus no reāliem piedāvājumiem.",
        "Uzzīmē abu grafikus un atrodi krustpunktu.",
        "Izvēlies tarifu savam patēriņam un pamato.",
    ]),
]
