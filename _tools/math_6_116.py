# -*- coding: utf-8 -*-
"""6. klase, 116. stunda: «Kā raksturot grafiku ar vārdiem?»

Mikrotemata noslēgums. Grafiku izlasīt ir viena prasme, izstāstīt to - cita.
Te tiek nostiprināti precīzi vārdu savienojumi: «paaugstinās par», «zem
nulles», «par tik lielāks» - tie paši, ko prasa eksāmens.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kā raksturot grafiku ar vārdiem?"

MERKIS = ("Raksturosim grafisko attēlu, lietojot «paaugstinās par», «zem "
          "nulles», «par tik lielāks».")

SATURS = [
    Sakums("Pareizs vārds ir tikpat svarīgs kā pareizs skaitlis",
           zimejums=plakne(lauzta=[(0, -4), (2, -1), (4, 3), (6, 1)],
                           no_x=0, lidz_x=6, no_y=-6, lidz_y=4, solis=2,
                           x_nos="h", y_nos="°C"),
           paraksts="«No 0 h līdz 4 h temperatūra paaugstinājās par 7 "
                    "grādiem» - tā ir pilnīga atbilde.",
           fakti=["«Paaugstinās par» lieto izmaiņai, «ir» - vērtībai.",
                  "«Zem nulles» nozīmē negatīvu vērtību.",
                  "«Par tik lielāks» ir starpība, nevis reizinājums."]),

    Doma("Vērtība, izmaiņa un salīdzinājums - trīs dažādi vārdi",
         "Grafiku raksturo trijos veidos: pasakot vērtību konkrētā brīdī, "
         "izmaiņu starp diviem brīžiem un salīdzinājumu ar citu vērtību.",
         soli=[
             "Vērtībai lieto «ir»: «pie 2 h temperatūra ir −1 °C».",
             "Izmaiņai lieto «paaugstinājās par» vai «pazeminājās par».",
             "Salīdzinājumam lieto «par tik lielāks nekā».",
             "Negatīvai vērtībai pievieno «zem nulles».",
             "Katram apgalvojumam pieliec skaitli un mērvienību.",
         ],
         pieze="«Temperatūra paaugstinājās par 7 grādiem» un «temperatūra ir "
               "7 grādi» ir divi pilnīgi dažādi apgalvojumi. Pirmais runā "
               "par izmaiņu, otrs - par vērtību."),

    Paraugs("Izstāsti grafiku",
            uzd="Grafiks: 0 h → −4 °C; 2 h → −1 °C; 4 h → 3 °C; 6 h → 1 °C. "
                "Uzraksti četrus apgalvojumus.",
            soli=[
                ("Pie 0 h temperatūra ir −4 °C, tas ir zem nulles",
                 "Vērtība."),
                ("No 0 h līdz 4 h temperatūra paaugstinājās par 7 grādiem",
                 "Izmaiņa."),
                ("No 4 h līdz 6 h tā pazeminājās par 2 grādiem",
                 "Pretējā izmaiņa."),
                ("Pie 4 h temperatūra ir par 4 grādiem lielāka nekā pie 2 h",
                 "Salīdzinājums."),
            ],
            atbilde="četri apgalvojumi ar skaitļiem"),

    Ievadi("Aizpildi apgalvojumu", [
        {"jaut": "Pie 0 h ir −4 °C, pie 4 h ir 3 °C. Par cik grādiem tā "
                 "paaugstinājās?",
         "atb": ["7"], "padoms": "4 + 3."},
        {"jaut": "Pie 4 h ir 3 °C, pie 6 h ir 1 °C. Par cik grādiem tā "
                 "pazeminājās?",
         "atb": ["2"], "padoms": "3 − 1."},
        {"jaut": "Pie 2 h ir −1 °C. Par cik grādiem tas ir zem nulles?",
         "atb": ["1"], "padoms": "Modulis."},
        {"jaut": "Pie 4 h ir 3 °C, pie 2 h ir −1 °C. Par cik grādiem pirmā "
                 "vērtība ir lielāka?",
         "atb": ["4"], "padoms": "3 − (−1)."},
        {"jaut": "Cik stundas temperatūra bija zem nulles, ja tā bija zem "
                 "nulles no 0 h līdz 3 h?",
         "atb": ["3"], "padoms": "Trīs stundas."},
        {"jaut": "Kāda ir starpība starp augstāko (3 °C) un zemāko (−4 °C) "
                 "vērtību?",
         "atb": ["7"], "padoms": "3 + 4."},
    ], pamats=4),

    Varianti("Kurš vārds te der?", [
        {"jaut": "«Temperatūra ... par 5 grādiem.» Kurš vārds der izmaiņai "
                 "uz augšu?",
         "opcijas": ["paaugstinājās", "ir", "sasniedza", "bija"],
         "pareizi": 0,
         "padoms": "Izmaiņai lieto «par»."},
        {"jaut": "«Pie 3 h temperatūra ... −2 °C.» Kurš vārds der?",
         "opcijas": ["ir", "paaugstinājās par", "pazeminājās par",
                     "mainījās par"],
         "pareizi": 0,
         "padoms": "Runa ir par vērtību."},
        {"jaut": "«−3 °C ir ... grādiem zem nulles.»",
         "opcijas": ["par 3", "par −3", "par 0", "par 6"],
         "pareizi": 0,
         "padoms": "Attālums līdz nullei."},
        {"jaut": "«2 °C ir par ... grādiem lielāks nekā −3 °C.»",
         "opcijas": ["5", "1", "−1", "6"],
         "pareizi": 0,
         "padoms": "2 − (−3)."},
    ], pamats=4),

    Petijums("Izstāsti grafiku soļabiedram",
             vajag="grafiks no iepriekšējās stundas vai no ziņām",
             soli=[
                 "Uzraksti četrus apgalvojumus par savu grafiku.",
                 "Katrā pieliec skaitli un mērvienību.",
                 "Iedod tikai apgalvojumus soļabiedram, bez grafika.",
                 "Palūdz viņam uzzīmēt grafiku pēc taviem vārdiem.",
                 "Salīdziniet abus grafikus.",
             ],
             secinajums="Ja grafiki sakrita, apgalvojumi bija pietiekami "
                        "precīzi; ja ne, trūka kāda skaitļa."),

    Pasaule("Kā ziņo laika prognozi?",
            Ievadi("", [
                {"jaut": "Naktī −7 °C, dienā 2 °C. Par cik grādiem "
                         "paaugstinājās?",
                 "atb": ["9"], "padoms": "7 + 2."},
                {"jaut": "Par cik grādiem nakts temperatūra ir zem nulles?",
                 "atb": ["7"], "padoms": "Modulis."},
                {"jaut": "Nākamajā naktī −3 °C. Par cik grādiem tā ir "
                         "siltāka nekā iepriekšējā?",
                 "atb": ["4"], "padoms": "−3 − (−7)."},
                {"jaut": "Kāda ir starpība starp siltāko dienu (2 °C) un "
                         "aukstāko nakti (−7 °C)?",
                 "atb": ["9"], "padoms": "2 + 7."},
            ]),
            pavediens="planeta",
            konteksts="Laika ziņās katrs vārds ir izvēlēts precīzi: "
                      "«paaugstināsies par» nav tas pats, kas «būs».",
            kapec="Precīzs vārds pasaka, vai runa ir par vērtību vai "
                  "izmaiņu."),

    Zimejums("Grafiks, ko izstāstīt",
             plakne(lauzta=[(0, 2), (2, -1), (4, -4), (6, -2)],
                    no_x=0, lidz_x=6, no_y=-6, lidz_y=4, solis=2,
                    x_nos="h", y_nos="°C"),
             paskaidro="Pamēģini pats: uzraksti četrus apgalvojumus par šo "
                       "grafiku, katrā pieliekot skaitli.",
             ievads="Otrs grafiks patstāvīgam darbam."),

    Kopsavilkums([
        "Raksturoju grafiku ar precīziem vārdiem.",
        "Atšķiru vērtību no izmaiņas.",
        "Lietoju «paaugstinās par», «zem nulles» un «par tik lielāks».",
        "Katram apgalvojumam pievienoju skaitli un mērvienību.",
    ]),

    Majas([
        "Uzraksti četrus apgalvojumus par šodienas laika grafiku.",
        "Vienā no tiem lieto vārdus «zem nulles».",
        "Pieraksti, kurš apgalvojums runā par izmaiņu, nevis par vērtību.",
    ]),
]
