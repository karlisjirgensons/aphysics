# -*- coding: utf-8 -*-
"""8. klase, 39. stunda: «Kā pierakstīt mērījuma rezultātu?»

Mērījuma rezultāts ir intervāls, nevis viens skaitlis: x = (17,4 ± 0,1) cm
nozīmē «no 17,3 līdz 17,5 cm». Kļūdu ņem vienādu ar iedaļas vērtību, kā
dabaszinībās. Uz skaitļu taisnes tas izskatās kā nogrieznis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā pierakstīt mērījuma rezultātu?"

MERKIS = ("Pierakstīsim mērījuma rezultātu, ievērojot mērījuma kļūdu.")

SATURS = [
    Sakums("Zīmulis: (17,4 ± 0,1) cm",
           zimejums=taisne(17, 18, 0.1, [(17.4, "17,4")],
                           intervali=[(17.3, 17.5, True, True)]),
           paraksts="Patiesais garums ir kaut kur iesvītrotajā nogrieznī.",
           fakti=["17,4 - nolasītā vērtība.",
                  "0,1 - kļūda (iedaļas vērtība).",
                  "Patiesais garums - no 17,3 līdz 17,5 cm."]),

    Doma("Rezultāta pieraksts",
         "Mērījuma rezultātu pieraksta formā x = (x₀ ± Δx) mērvienība, kur x₀ ir "
         "nolasītā vērtība un Δx - absolūtā kļūda.",
         soli=[
             "Nolasi vērtību x₀.",
             "Nosaki kļūdu: Δx = c (iedaļas vērtība).",
             "Pieraksti: x = (x₀ ± Δx) un mērvienību aiz iekavām.",
             "Robežas: no x₀ − Δx līdz x₀ + Δx.",
             "x₀ un Δx raksta ar tikpat cipariem aiz komata.",
         ],
         pieze="Relatīvā kļūda R = {Δx|x₀} · 100 % parāda, cik precīzs "
               "mērījums ir salīdzinājumā ar pašu lielumu."),

    Paraugs("Pieraksti un atrod robežas",
            uzd="Termometrs (c = 2 °C) rāda 36 °C. Pieraksti rezultātu.",
            soli=[
                ("Δt = 2 °C", "Kļūda - iedaļas vērtība."),
                ("t = (36 ± 2) °C", "Pieraksts."),
                ("34 °C ≤ t ≤ 38 °C", "Robežas."),
                ("R = {2|36} · 100 % ≈ 6 %", "Relatīvā kļūda."),
            ],
            atbilde="t = (36 ± 2) °C"),

    Ievadi("Robežas un kļūda", [
        {"jaut": "m = (250 ± 5) g. Mazākā iespējamā masa (g)?",
         "atb": ["245"], "padoms": "250 − 5."},
        {"jaut": "l = (12,4 ± 0,1) cm. Lielākais iespējamais garums (cm)?",
         "atb": ["12,5", "12.5"], "padoms": "12,4 + 0,1."},
        {"jaut": "Garums ir no 3,2 m līdz 3,6 m. Kāda ir kļūda Δx (m)?",
         "atb": ["0,2", "0.2"], "padoms": "Puse no 0,4."},
        {"jaut": "Tam pašam: nolasītā vērtība x₀ (m)?",
         "atb": ["3,4", "3.4"], "padoms": "Vidus."},
        {"jaut": "V = (80 ± 4) ml. Relatīvā kļūda procentos?",
         "atb": ["5", "5 %", "5%"], "padoms": "4 : 80."},
        {"jaut": "Ar kuru kļūdu (mm) mēra lineāls ar c = 1 mm?",
         "atb": ["1"], "padoms": "Δx = c."},
    ], pamats=4),

    Varianti("Pareizs pieraksts?", [
        {"jaut": "Kurš pieraksts ir pareizs?",
         "opcijas": ["(4,50 ± 0,05) m", "(4,5 ± 0,05) m",
                     "4,50 m ± 0,05", "(4,5 ± 0,05 m)"],
         "pareizi": 0, "padoms": "Vienāds ciparu skaits, mērvienība aiz "
                                 "iekavām."},
        {"jaut": "Kurš mērījums ir relatīvi precīzāks: (100 ± 1) m vai "
                 "(10 ± 1) m?",
         "opcijas": ["(100 ± 1) m - 1 %", "(10 ± 1) m - 10 %", "Vienādi",
                     "Nevar noteikt"],
         "pareizi": 0, "padoms": "Salīdzina R."},
    ]),

    Zimejums("Divi mērījumi uz taisnes",
             taisne(10, 14, 0.5, [(11.5, "A"), (12.5, "B")],
                    intervali=[(11, 12, True, True), (12, 13, True, True)]),
             paskaidro="A = (11,5 ± 0,5) cm, B = (12,5 ± 0,5) cm. Intervāli "
                       "saskaras - nevar droši teikt, ka B ir garāks."),

    Pasaule("Ķermeņa temperatūra",
            Ievadi("", [
                {"jaut": "Digitālais termometrs rāda 37,4 °C, c = 0,1 °C. "
                         "Augšējā robeža (°C)?",
                 "atb": ["37,5", "37.5"], "padoms": "37,4 + 0,1."},
                {"jaut": "Paaugstināta temperatūra sākas no 37,5 °C. Cik "
                         "grādu līdz robežai no nolasītās vērtības?",
                 "atb": ["0,1", "0.1"], "padoms": "37,5 − 37,4."},
                {"jaut": "Vecais termometrs ar c = 0,2 °C rāda 37,2 °C. "
                         "Augšējā robeža?",
                 "atb": ["37,4", "37.4"], "padoms": "37,2 + 0,2."},
            ]),
            pavediens="daba",
            konteksts="Ārsts uz robežas vērtību skatās ar kļūdu: 37,4 °C ar "
                      "kļūdu 0,1 °C vēl var būt 37,5 °C.",
            kapec="Kļūda pasaka, cik drošs ir secinājums."),

    Kopsavilkums([
        "Pierakstu mērījumu formā (x₀ ± Δx) mērvienība.",
        "Nosaku robežas, kurās ir patiesā vērtība.",
        "Aprēķinu relatīvo kļūdu.",
    ]),

    Majas([
        "Nomēri grāmatas garumu un platumu, pieraksti ar kļūdu.",
        "Aprēķini abu mērījumu relatīvo kļūdu.",
        "Paskaidro, kurš mērījums ir precīzāks un kāpēc.",
    ]),
]
