# -*- coding: utf-8 -*-
"""4. klase, 2. stunda: «Kā salīdzināt, nerēķinot precīzi?»

Spriest ir ātrāk nekā rēķināt: ja vienā summā abi saskaitāmie ir lielāki,
arī summa ir lielāka. Šī stunda māca skatīties uz izteiksmes uzbūvi, nevis
steigties pēc atbildes - to pašu vēlāk prasa aptuvenā vērtība un pārbaude.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, kolonnas)

TEMA = "Kā salīdzināt, nerēķinot precīzi?"

MERKIS = ("Salīdzināsim summas un starpības, spriežot par saskaitāmajiem, "
          "mazināmo un atņēmēju, nevis rēķinot precīzi.")

SATURS = [
    Sakums("Kurš grozs ir smagāks?",
           zimejums=kolonnas([("1. grozs", 347), ("2. grozs", 352)], " g"),
           paraksts="347 + 128 vai 352 + 128? Rēķināt nevajag.",
           fakti=["Abos grozos ir vienāds maizes klaips - 128 g.",
                  "Atšķiras tikai siers: 347 g un 352 g.",
                  "Smagāks ir tas grozs, kurā siers ir smagāks."]),

    Doma("Salīdzini tās daļas, kas atšķiras",
         "Ja vienādas daļas abās pusēs ir vienādas, lielāka ir tā puse, "
         "kurā atšķirīgā daļa ir lielāka.",
         soli=[
             "Atrodi, kas abās izteiksmēs ir vienāds.",
             "Salīdzini to, kas atšķiras.",
             "Summā: lielāks saskaitāmais - lielāka summa.",
             "Starpībā: lielāks atņēmējs - mazāka starpība.",
         ],
         pieze="Ar starpību ir otrādi: jo vairāk atņem, jo mazāk paliek. "
               "Tāpēc 500 − 199 ir lielāks nekā 500 − 201."),

    Paraugs("Kura starpība lielāka?",
            uzd="Salīdzini 800 − 356 un 800 − 365, nerēķinot.",
            soli=[
                ("800 = 800",
                 "Mazināmais abās starpībās ir vienāds."),
                ("356 < 365",
                 "Pirmajā starpībā atņem mazāk."),
                ("800 − 356 > 800 − 365",
                 "Kur atņem mazāk, tur paliek vairāk."),
            ],
            atbilde="800 − 356 > 800 − 365"),

    Slidnis("Kas notiek ar starpību, kad atņēmējs aug?",
            soli=[
                {"v": "500 − 100 = 400", "teksts": "Atņem simtu.",
                 "josla": 80},
                {"v": "500 − 200 = 300", "teksts": "Atņēmējs lielāks - "
                 "starpība mazāka.", "josla": 60},
                {"v": "500 − 300 = 200", "teksts": "Vēl mazāka.",
                 "josla": 40},
                {"v": "500 − 400 = 100", "teksts": "Paliek pavisam maz.",
                 "josla": 20},
            ],
            ievads="Mazināmais visur ir 500. Skaties, kā josla saraujas."),

    Varianti("Kura puse lielāka?", [
        {"jaut": "425 + 138 ☐ 425 + 183",
         "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "138 ir mazāks par 183."},
        {"jaut": "700 − 250 ☐ 700 − 205",
         "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "Pirmajā atņem vairāk, tāpēc paliek mazāk."},
        {"jaut": "316 + 99 ☐ 99 + 316",
         "opcijas": ["=", "<", ">"], "pareizi": 0,
         "padoms": "Saskaitāmos drīkst mainīt vietām."},
        {"jaut": "640 − 120 ☐ 650 − 120",
         "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "Lielāks mazināmais - lielāka starpība."},
        {"jaut": "208 + 415 ☐ 280 + 415",
         "opcijas": ["<", ">", "="], "pareizi": 0,
         "padoms": "Salīdzini 208 un 280."},
        {"jaut": "900 − 99 ☐ 900 − 100",
         "opcijas": [">", "<", "="], "pareizi": 0,
         "padoms": "Atņem par vienu mazāk - paliek par vienu vairāk."},
    ], pamats=4,
        ievads="Nerēķini! Paskaties, kas atšķiras, un izvēlies zīmi."),

    Ievadi("Cik liela ir atšķirība?", [
        {"jaut": "Par cik 350 + 47 ir lielāks nekā 350 + 40?",
         "atb": ["7"], "padoms": "Atšķiras tikai 47 un 40."},
        {"jaut": "Par cik 600 − 200 ir lielāks nekā 600 − 250?",
         "atb": ["50"], "padoms": "Otrajā atņem par 50 vairāk."},
        {"jaut": "Par cik 512 + 300 ir lielāks nekā 502 + 300?",
         "atb": ["10"], "padoms": "Salīdzini 512 un 502."},
        {"jaut": "Par cik 900 − 390 ir mazāks nekā 900 − 380?",
         "atb": ["10"], "padoms": "Pirmajā atņem par 10 vairāk."},
    ]),

    Pasaule("Kurā veikalā lētāk?",
            Varianti("", [
                {"jaut": "Velosipēds: 285 € + ķivere 39 € vai velosipēds "
                         "295 € + ķivere 39 €. Kurš komplekts lētāks?",
                 "opcijas": ["pirmais", "otrais", "vienādi"],
                 "pareizi": 0, "padoms": "Ķiveres vienādas - salīdzini "
                 "velosipēdus."},
                {"jaut": "Sākumā 500 €. Anna iztērē 198 €, Jānis - 189 €. "
                         "Kuram paliek vairāk?",
                 "opcijas": ["Jānim", "Annai", "vienādi"],
                 "pareizi": 0, "padoms": "Kas iztērē mazāk, tam paliek "
                 "vairāk."},
                {"jaut": "Brauciens: 120 € + viesnīca 240 € vai brauciens "
                         "240 € + viesnīca 120 €. Kas lētāk?",
                 "opcijas": ["vienādi", "pirmais", "otrais"],
                 "pareizi": 0, "padoms": "Tie paši skaitļi, tikai "
                 "samainīti vietām."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā reti ir laiks rēķināt precīzi - bet salīdzināt "
                      "var vienā mirklī.",
            kapec="Kas spriež, tas izvēlas ātrāk un kļūdās retāk."),

    Kopsavilkums([
        "Salīdzinu summas, skatoties uz atšķirīgajiem saskaitāmajiem.",
        "Zinu, ka lielāks atņēmējs dod mazāku starpību.",
        "Zinu, ka saskaitāmos drīkst mainīt vietām.",
        "Pasaku, par cik viena izteiksme lielāka, nerēķinot to visu.",
    ]),

    Majas([
        "Veikalā salīdzini divu līdzīgu pirkumu cenas, nerēķinot kopsummu.",
        "Izdomā divas starpības, kurām mazināmais ir vienāds, un pajautā "
        "mājiniekiem, kura lielāka.",
        "Uzraksti trīs pārus ar zīmēm <, > un =.",
    ]),
]
