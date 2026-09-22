# -*- coding: utf-8 -*-
"""5. klase, 160. stunda: «Kā attēlot vienmērīgu kustību?»

Jauns mikrotemats. Kustības grafiks ir pirmais gadījums, kad no tabulas top
līnija, un tas ir arī pirmais grafiks, kurā līnija tiešām ir pamatota -
laiks un ceļš mainās nepārtraukti. Vienmērīgai kustībai tā vienmēr iznāk
taisna, un tieši tas ir stundas atklājums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne, restis)

TEMA = "Kā attēlot vienmērīgu kustību?"

MERKIS = ("Iemācīsimies grafiski attēlot tabulā doto sakarību starp laiku un "
          "veikto ceļu.")

SATURS = [
    Sakums("No tabulas uz līniju",
           zimejums=restis([["1", "2", "3", "4"],
                            ["60", "120", "180", "240"]],
                           virsraksts="Stundas un kilometri"),
           paraksts="Katrā stundā auto nobrauc 60 km - tāpēc grafiks ir "
                    "taisna līnija.",
           fakti=["Tabulā ir divas rindas: laiks un ceļš.",
                  "Katrs stabiņš ir viens punkts plaknē.",
                  "Vienmērīgai kustībai punkti sakārtojas uz taisnes."]),

    Doma("Katrs tabulas stabiņš ir punkts",
         "Kustības grafiku zīmē, katru tabulas skaitļu pāri attēlojot kā "
         "punktu koordinātu plaknē un savienojot punktus ar līniju.",
         soli=[
             "Uz x ass atliec laiku, uz y ass - ceļu.",
             "Izvēlies vienības pēc lielākajiem skaitļiem.",
             "Katru tabulas stabiņu atliec kā punktu.",
             "Savieno punktus ar līniju.",
             "Pārbaudi: vienmērīgai kustībai līnijai jābūt taisnai.",
         ],
         pieze="Grafiks sākas punktā (0; 0): sākumā laiks ir nulle un ceļš "
               "arī. Ja līnija nesākas turpat, kustība nav sākusies no "
               "vietas."),

    Paraugs("Auto brauc 60 km stundā",
            uzd="Uzzīmē grafiku pirmajām četrām stundām.",
            soli=[
                ("Pēc 1 stundas - 60 km",
                 "Punkts (1; 60)."),
                ("Pēc 2 stundām - 120 km",
                 "Punkts (2; 120)."),
                ("Pēc 3 stundām - 180 km",
                 "Punkts (3; 180)."),
                ("Visi punkti uz vienas taisnes",
                 "Kustība ir vienmērīga."),
            ],
            atbilde="Grafiks ir taisna līnija caur (0; 0)"),

    Ievadi("Aprēķini ceļu", [
        {"jaut": "Auto brauc 60 km stundā. Cik kilometru tas nobrauc "
                 "2 stundās?",
         "atb": ["120"], "padoms": "60 · 2."},
        {"jaut": "Cik kilometru 3 stundās?",
         "atb": ["180"], "padoms": "60 · 3."},
        {"jaut": "Cik kilometru 4 stundās?",
         "atb": ["240"], "padoms": "60 · 4."},
        {"jaut": "Cik stundās tas nobrauc 300 km?",
         "atb": ["5"], "padoms": "300 : 60."},
        {"jaut": "Velosipēdists brauc 15 km stundā. Cik kilometru "
                 "2 stundās?",
         "atb": ["30"], "padoms": "15 · 2."},
        {"jaut": "Cik kilometru 4 stundās?",
         "atb": ["60"], "padoms": "15 · 4."},
        {"jaut": "Kādā punktā sākas kustības grafiks? Ieraksti pirmo "
                 "koordinātu.",
         "atb": ["0"], "padoms": "Laiks ir nulle."},
        {"jaut": "Gājējs iet 5 km stundā. Cik kilometru 3 stundās?",
         "atb": ["15"], "padoms": "5 · 3."},
    ], pamats=4,
        ievads="Vienmērīgā kustībā ceļš ir ātrums reiz laiks."),

    Zimejums("Vienmērīga kustība ir taisne",
             plakne(lauzta=[(0, 0), (1, 60), (2, 120), (3, 180), (4, 240)],
                    no_x=0, lidz_x=5, no_y=0, lidz_y=300, solis=60,
                    virsraksts="Stundas un kilometri"),
             paskaidro="Katrā stundā ceļš pieaug par vienu un to pašu - "
                       "60 km. Tāpēc punkti sakārtojas uz taisnes.",
             ievads="Tā izskatās vienmērīgas kustības grafiks."),

    Varianti("Kāds ir grafika izskats?", [
        {"jaut": "Kāds ir vienmērīgas kustības grafiks?",
         "opcijas": ["Taisna līnija", "Lauzta līnija", "Riņķis",
                     "Atsevišķi punkti"],
         "pareizi": 0,
         "padoms": "Ceļš pieaug vienādi."},
        {"jaut": "Kas ir uz x ass?",
         "opcijas": ["Laiks", "Ceļš", "Ātrums", "Punkti"],
         "pareizi": 0,
         "padoms": "Pirmā koordināta."},
        {"jaut": "Kādā punktā sākas kustības grafiks?",
         "opcijas": ["(0; 0)", "(1; 60)", "(0; 60)", "(60; 0)"],
         "pareizi": 0,
         "padoms": "Sākumā nekas nav nobraukts."},
        {"jaut": "Auto brauc 60 km stundā. Kur būs punkts pēc 3 stundām?",
         "opcijas": ["(3; 180)", "(180; 3)", "(3; 60)", "(60; 3)"],
         "pareizi": 0,
         "padoms": "60 · 3."},
        {"jaut": "Ko nozīmē, ka punkti nav uz vienas taisnes?",
         "opcijas": ["Kustība nav vienmērīga", "Grafiks ir nepareizs",
                     "Vienība ir slikta", "Neko"],
         "pareizi": 0,
         "padoms": "Ceļš pieaug nevienādi."},
        {"jaut": "Cik kilometru gājējs noiet 3 stundās ar ātrumu 5 km "
                 "stundā?",
         "opcijas": ["15 km", "8 km", "5 km", "53 km"],
         "pareizi": 0,
         "padoms": "5 · 3."},
    ], pamats=4),

    Pasaule("Cik tālu tiksim?",
            Ievadi("", [
                {"jaut": "Auto brauc 80 km stundā. Cik kilometru "
                         "2 stundās?",
                 "atb": ["160"], "padoms": "80 · 2."},
                {"jaut": "Cik kilometru 5 stundās?",
                 "atb": ["400"], "padoms": "80 · 5."},
                {"jaut": "Cik stundās tas nobrauks 240 km?",
                 "atb": ["3"], "padoms": "240 : 80."},
                {"jaut": "Ceļš ir 400 km. Cik stundas jābrauc?",
                 "atb": ["5"], "padoms": "400 : 80."},
            ]),
            pavediens="celojums",
            konteksts="Pirms brauciena grafiks pasaka, cikos būsim galā, "
                      "neizrēķinot katru stundu atsevišķi.",
            kapec="Taisna līnija ļauj nolasīt jebkuru starpvērtību."),

    Kopsavilkums([
        "Attēloju tabulā doto laika un ceļa sakarību plaknē.",
        "Atlieku katru tabulas stabiņu kā punktu.",
        "Savienoju punktus ar līniju.",
        "Zinu, ka vienmērīgas kustības grafiks ir taisne caur (0; 0).",
    ]),

    Majas([
        "Uzzīmē grafiku velosipēdistam, kas brauc 15 km stundā.",
        "Nolasi no tā, cik kilometru viņš nobrauc 3 stundās.",
        "Pieraksti, kāpēc līnija ir taisna.",
    ]),
]
