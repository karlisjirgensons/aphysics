# -*- coding: utf-8 -*-
"""3. klase, 123. stunda: «Kā nolasīt mērtrauku?»

Mērtrauks ir skaitļu taisne, kas stāv stāvus. Grūtākais tajā ir iedaļas
vērtība: starp 0 un 500 ml var būt piecas iedaļas vai desmit, un no tā
atkarīgs viss nolasījums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         taisne)

TEMA = "Kā nolasīt mērtrauku?"

MERKIS = ("Nolasīsim mērtrauka skalu litros un mililitros.")

SATURS = [
    Sakums("Cik daudz ūdens ir traukā?",
           zimejums=taisne(0, 1000, 200, [(600, "600")]),
           paraksts="Mērtrauka skala ir skaitļu taisne, kas stāv stāvus.",
           fakti=["1 litrs ir 1000 mililitru.",
                  "Vispirms noskaidro, cik liela ir viena iedaļa."]),

    Doma("Vispirms noskaidro iedaļas vērtību",
         "Izdali attālumu starp diviem uzrakstītiem skaitļiem ar iedaļu "
         "skaitu starp tiem.",
         soli=[
             "Atrodi divus blakus uzrakstītus skaitļus uz skalas.",
             "Saskaiti iedaļas starp tiem.",
             "Izdali skaitļu starpību ar iedaļu skaitu.",
             "Saskaiti iedaļas no tuvākā skaitļa līdz ūdens līmenim.",
         ],
         pieze="Nolasot mērtrauku, acij jābūt ūdens līmeņa augstumā - citādi "
               "skaitlis iznāks lielāks vai mazāks, nekā ir."),

    Paraugs("Cik mililitru ir traukā?",
            uzd="Starp 0 un 200 ml ir 4 iedaļas. Ūdens līmenis ir 3 iedaļas "
                "virs 400 ml. Cik mililitru ir traukā?",
            soli=[
                ("200 : 4 = 50",
                 "Viena iedaļa ir 50 ml."),
                ("3 · 50 = 150",
                 "Trīs iedaļas virs 400."),
                ("400 + 150 = 550",
                 "Traukā ir 550 ml."),
            ],
            atbilde="550 ml"),

    Ievadi("Nolasi skalu", [
        {"jaut": "Starp 0 un 200 ml ir 4 iedaļas. Cik mililitru ir viena?",
         "atb": ["50"], "padoms": "200 : 4."},
        {"jaut": "Starp 0 un 500 ml ir 5 iedaļas. Cik mililitru ir viena?",
         "atb": ["100"], "padoms": "500 : 5."},
        {"jaut": "Cik mililitru ir 1 litrā?", "atb": ["1000"],
         "padoms": "Tūkstotis."},
        {"jaut": "Cik mililitru ir {1|2} litra?", "atb": ["500"],
         "padoms": "1000 : 2."},
        {"jaut": "Cik mililitru ir {1|4} litra?", "atb": ["250"],
         "padoms": "1000 : 4."},
        {"jaut": "Traukā 750 ml. Cik mililitru pietrūkst līdz litram?",
         "atb": ["250"], "padoms": "1000 − 750."},
    ], pamats=4),

    Petijums("Izmēri ar mērtrauku",
             vajag="mērtrauks, ūdens un trīs dažādi trauki",
             soli=[
                 "Noskaidro, cik liela ir viena iedaļa mērtraukā.",
                 "Piepildi pirmo trauku un ielej ūdeni mērtraukā.",
                 "Nolasi tilpumu, turot aci līmeņa augstumā.",
                 "Atkārto ar pārējiem traukiem un pieraksti visus mērījumus.",
             ],
             secinajums="Mērtrauks dod skaitli, ko var pierakstīt un "
                        "salīdzināt - ne tikai «vairāk» vai «mazāk»."),

    Zimejums("Skala ar iedaļām",
             taisne(0, 500, 100, [(250, "250"), (350, "350")]),
             paskaidro="Starp uzrakstītajiem skaitļiem ir vairākas iedaļas - "
                       "katra no tām ir 100 ml : iedaļu skaits.",
             ievads="Tā izskatās mērtrauka skala."),

    Varianti("Cik ir traukā?", [
        {"jaut": "Starp 0 un 1000 ml ir 10 iedaļas. Cik mililitru ir viena?",
         "opcijas": ["100", "10", "1000", "50"],
         "pareizi": 0, "padoms": "1000 : 10."},
        {"jaut": "Cik mililitru ir 2 litri?",
         "opcijas": ["2000", "200", "20", "2"],
         "pareizi": 0, "padoms": "2 · 1000."},
        {"jaut": "Kā pareizi nolasīt mērtrauku?",
         "opcijas": ["Aci turot līmeņa augstumā", "Skatoties no augšas",
                     "Skatoties no apakšas", "Vienalga kā"],
         "pareizi": 0, "padoms": "Citādi skaitlis iznāk nepareizs."},
        {"jaut": "Traukā 350 ml. Cik mililitru pietrūkst līdz 500?",
         "opcijas": ["150", "250", "50", "850"],
         "pareizi": 0, "padoms": "500 − 350."},
    ], pamats=4),

    Pasaule("Cik ūdens patērē diena?",
            Ievadi("", [
                {"jaut": "Glāze ir 250 ml. Cik mililitru ir 4 glāzes?",
                 "atb": ["1000"], "padoms": "4 · 250."},
                {"jaut": "Cik litru tas ir?", "atb": ["1"],
                 "padoms": "1000 ml."},
                {"jaut": "Dienā jāizdzer 2 litri. Cik glāžu pa 250 ml tas "
                         "ir?",
                 "atb": ["8"], "padoms": "2000 : 250."},
                {"jaut": "Cik litru izdzer nedēļā, ja dienā 2 litri?",
                 "atb": ["14"], "padoms": "7 · 2."},
            ]),
            pavediens="planeta",
            konteksts="Ūdens patēriņu skaita litros - gan cilvēkam, gan visai "
                      "pilsētai.",
            kapec="Tikai izmērot var pateikt, cik ūdens tiešām patērē."),

    Kopsavilkums([
        "Nolasu mērtrauka skalu litros un mililitros.",
        "Nosaku iedaļas vērtību.",
        "Zinu, ka 1 l = 1000 ml.",
        "Nolasu mērījumu, turot aci līmeņa augstumā.",
    ]),

    Majas([
        "Atrodi mājās mērtrauku un noskaidro tā iedaļas vērtību.",
        "Izmēri, cik mililitru ietilpst tavā glāzē.",
        "Izrēķini, cik glāžu ir divos litros.",
    ]),
]
