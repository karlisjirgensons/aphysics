# -*- coding: utf-8 -*-
"""8. klase, 40. stunda: «Cik ciparu atstāt?»

Noapaļošana ar norādīto precizitāti - tieši eksāmena 2. uzdevums (36,74
līdz desmitdaļām). Stundā arī jautājums «kāpēc tieši tik»: kalkulatora 12
cipari no mērījuma ar 2 cipariem ir izdomāta precizitāte.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, taisne)

TEMA = "Cik ciparu atstāt?"

MERKIS = ("Noapaļosim skaitli ar norādīto precizitāti un pamatosim "
          "izvēli.")

SATURS = [
    Sakums("36,74 līdz desmitdaļām",
           zimejums=taisne(36.6, 36.9, 0.1, [(36.74, "36,74")], sikas=10),
           paraksts="36,74 ir tuvāk 36,7 nekā 36,8.",
           fakti=["Skaties uz ciparu aiz noapaļojamās vietas: 4.",
                  "0-4 - atmet, 5-9 - pieskaita vienu.",
                  "36,74 ≈ 36,7."]),

    Doma("Noapaļošanas likums",
         "Noapaļojot līdz noteiktai vietai, skatās uz nākamo ciparu pa labi.",
         soli=[
             "Atrodi ciparu, līdz kuram noapaļo.",
             "Nākamais cipars 0-4: noapaļojamais cipars nemainās.",
             "Nākamais cipars 5-9: noapaļojamo palielina par 1.",
             "Pārējos ciparus aiz komata atmet, pirms komata - aizstāj ar 0.",
             "Raksti ≈, nevis =.",
         ],
         pieze="Rezultātā nedrīkst būt vairāk ciparu nekā mērījumos - "
               "kalkulatora 12 cipari no 2 ciparu mērījuma ir izdomāti."),

    Paraugs("Dažādas precizitātes",
            uzd="Noapaļo 2,9651 līdz desmitdaļām, simtdaļām un veseliem.",
            soli=[
                ("2,9651 ≈ 3,0", "Aiz 9 ir 6 - 9 kļūst 10, pārnes."),
                ("2,9651 ≈ 2,97", "Aiz 6 ir 5."),
                ("2,9651 ≈ 3", "Aiz 2 ir 9."),
            ],
            atbilde="3,0; 2,97; 3"),

    Ievadi("Noapaļo", [
        {"jaut": "36,74 līdz desmitdaļām", "atb": ["36,7", "36.7"],
         "padoms": "Aiz 7 ir 4."},
        {"jaut": "0,5862 līdz simtdaļām", "atb": ["0,59", "0.59"],
         "padoms": "Aiz 8 ir 6."},
        {"jaut": "14 572 līdz tūkstošiem", "atb": ["15000", "15 000"],
         "padoms": "Aiz 4 ir 5."},
        {"jaut": "7,996 līdz simtdaļām", "atb": ["8,00", "8.00"],
         "padoms": "9 + 1 = 10 - pārnes divreiz."},
        {"jaut": "{2|3} līdz tūkstošdaļām", "atb": ["0,667", "0.667"],
         "padoms": "0,6666..."},
        {"jaut": "π = 3,14159... līdz desmittūkstošdaļām",
         "atb": ["3,1416", "3.1416"], "padoms": "Aiz 5 ir 9."},
    ], pamats=4),

    Varianti("Cik ciparu atstāt?", [
        {"jaut": "Istabas garums 4,2 m un platums 3,1 m. Kalkulators rāda "
                 "laukumu 13,02 m². Ko rakstīt?",
         "opcijas": ["≈ 13 m²", "13,02 m²", "13,0200 m²", "10 m²"],
         "pareizi": 0, "padoms": "Mērījumos 2 cipari."},
        {"jaut": "Ko nozīmē 8,0 cm, nevis 8 cm?",
         "opcijas": ["Mērīts ar precizitāti līdz 0,1 cm",
                     "Tas pats - nulli var nerakstīt",
                     "Tā ir kļūda", "8,0 ir lielāks"],
         "pareizi": 0, "padoms": "Nulle aiz komata ir informācija."},
    ]),

    Zimejums("Kas noapaļojas līdz 2,5?",
             taisne(2.4, 2.6, 0.05, [(2.45, "2,45"), (2.5, "2,5"),
                                     (2.55, "2,55")],
                    intervali=[(2.45, 2.55, True, False)]),
             paskaidro="Līdz desmitdaļām uz 2,5 noapaļojas visi skaitļi no "
                       "2,45 (ieskaitot) līdz 2,55 (neieskaitot)."),

    Pasaule("Rēķins veikalā",
            Ievadi("", [
                {"jaut": "1,35 kg āboli pa 1,79 €/kg. Kalkulators: 2,4165. "
                         "Cik eiro maksā (līdz centiem)?",
                 "atb": ["2,42", "2.42"], "padoms": "Aiz 1 ir 6."},
                {"jaut": "Degviela: 38,6 l pa 1,639 €/l. Cik eiro (līdz "
                         "centiem)?",
                 "atb": ["63,27", "63.27"], "padoms": "63,2654."},
                {"jaut": "Somijā skaidrā naudā kopsummu noapaļo līdz 5 "
                         "centiem. Cik maksā 63,27 €?",
                 "atb": ["63,25", "63.25"], "padoms": "Tuvākais 5 centu solis."},
            ]),
            pavediens="veikals",
            konteksts="Kase noapaļo līdz centiem, bet vairākās eirozonas "
                      "valstīs skaidrā naudā maksā ar 5 centu soli.",
            kapec="Noapaļošanas likums ir tas pats - mainās tikai solis."),

    Kopsavilkums([
        "Noapaļoju līdz norādītajai vietai.",
        "Pareizi pārnesu, ja noapaļo 9.",
        "Atstāju tik ciparu, cik pamato mērījumi.",
    ]),

    Majas([
        "Noapaļo 5,4449 līdz desmitdaļām un simtdaļām.",
        "Atrodi čekā vienu cenu, kas noapaļota, un pārbaudi to.",
        "Paskaidro, kāpēc 5,4449 līdz desmitdaļām nav 5,5.",
    ]),
]
