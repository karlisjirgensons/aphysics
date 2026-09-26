# -*- coding: utf-8 -*-
"""8. klase, 45. stunda: «Kas ir periodiska decimāldaļa?»

Periodiskā decimāldaļā ciparu grupa atkārtojas bezgalīgi; to pieraksta ar
iekavām: 0,(3), 0,1(6). Stundas «triks» - ceļš atpakaļ uz parasto daļu
ar reizināšanu ar 10 vai 100 un atņemšanu, kā vienādojumā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kas ir periodiska decimāldaļa?"

MERKIS = ("Lasīsim un pierakstīsim periodiskas decimāldaļas un saistīsim "
          "tās ar parastām daļām.")

SATURS = [
    Sakums("0,999... = 1?",
           zimejums=restis([["1/3", "=", "0,(3)"],
                            ["· 3", "", "· 3"],
                            ["1", "=", "0,(9)"]]),
           paraksts="Ja {1|3} = 0,333..., tad 3 · {1|3} = 0,999...",
           fakti=["Tātad 0,(9) = 1 - tas ir viens un tas pats skaitlis.",
                  "Iekavās raksta periodu - atkārtojošos ciparus.",
                  "Katru periodisku decimāldaļu var pārvērst par daļu."]),

    Doma("Periods un pieraksts",
         "Periodiskā decimāldaļā kāda ciparu grupa - periods - atkārtojas "
         "bezgalīgi. Periodu raksta iekavās.",
         soli=[
             "0,333... = 0,(3) - periods 3.",
             "0,121212... = 0,(12) - periods 12.",
             "0,1666... = 0,1(6) - pirms perioda cipars 1.",
             "Nolasa: «nulle komats trīs periodā».",
         ],
         pieze="Dažās grāmatās periodu raksta ar svītru virs cipariem; "
               "Latvijas skolā parasti lieto iekavas."),

    Slidnis("No 0,(12) uz daļu", [
        {"v": "x = 0,121212...", "teksts": "Nosauc skaitli par x"},
        {"v": "100x = 12,121212...", "teksts": "Periods 2 cipari - · 100"},
        {"v": "100x − x = 12", "teksts": "Atņem - bezgalīgās astes saīsinās"},
        {"v": "99x = 12", "teksts": "Vienādojums"},
        {"v": "x = {12|99} = {4|33}", "teksts": "Saīsina ar 3"},
    ]),

    Paraugs("Ar ciparu pirms perioda",
            uzd="Pārveido 0,1(6) parastā daļā.",
            soli=[
                ("x = 0,1666...", "Nosauc."),
                ("10x = 1,666...; 100x = 16,666...", "Divi reizinājumi."),
                ("100x − 10x = 15", "Astes vienādas."),
                ("x = {15|90} = {1|6}", "Saīsina ar 15."),
            ],
            atbilde="0,1(6) = {1|6}"),

    Ievadi("Pārveido", [
        {"jaut": "0,(5) = {5|?}", "atb": ["9"], "padoms": "10x − x = 5."},
        {"jaut": "0,(27) - atbildi raksti kā a/b (saīsinātu)",
         "atb": ["{3|11}", "3/11"], "padoms": "{27|99}."},
        {"jaut": "{2|9} kā periodiska daļa: 0,(?)", "atb": ["2"],
         "padoms": "{2|9} = 0,222..."},
        {"jaut": "{5|6} = 0,8(?)", "atb": ["3"], "padoms": "0,8333..."},
        {"jaut": "0,(9) = ?", "atb": ["1"], "padoms": "3 · 0,(3)."},
        {"jaut": "1,(3) - atbildi raksti kā a/b",
         "atb": ["{4|3}", "4/3"], "padoms": "1 + {1|3}."},
    ], pamats=4),

    Varianti("Salīdzini", [
        {"jaut": "Kurš lielāks: 0,(3) vai 0,33?",
         "opcijas": ["0,(3)", "0,33", "Vienādi", "Nevar salīdzināt"],
         "pareizi": 0, "padoms": "0,333... > 0,330."},
        {"jaut": "Kurš lielāks: 0,(18) vai 0,1(8)?",
         "opcijas": ["0,1(8) = 0,1888...", "0,(18) = 0,1818...", "Vienādi",
                     "Nevar salīdzināt"],
         "pareizi": 0, "padoms": "Trešais cipars."},
        {"jaut": "Kāds ir {1|7} periods?",
         "opcijas": ["142857", "14", "1428", "7"],
         "pareizi": 0, "padoms": "Seši cipari."},
    ]),

    Pasaule("Mūzikas ritms",
            Ievadi("", [
                {"jaut": "Dziesmā 3 sitieni sekundē. Cik sekunžu ilgst viens "
                         "sitiens? Atbildi raksti kā a/b.",
                 "atb": ["{1|3}", "1/3"], "padoms": "Precīzi, nevis 0,33."},
                {"jaut": "Cik sekundes ilgst 60 sitieni?",
                 "atb": ["20"], "padoms": "60 · {1|3}."},
                {"jaut": "Ja viens sitiens būtu 0,33 s, cik sekunžu 60 "
                         "sitieni?",
                 "atb": ["19,8", "19.8"], "padoms": "Kļūda uzkrājas."},
            ]),
            pavediens="tehnika",
            konteksts="Mūzikas programmas glabā ritmu kā daļu - ar 0,33 s "
                      "dziesma pēc minūtes aizbēgtu no ritma.",
            kapec="Periodiska decimāldaļa ir precīza tikai kā parasta daļa."),

    Kopsavilkums([
        "Lasu un pierakstu periodisku decimāldaļu ar iekavām.",
        "Pārveidoju periodisku decimāldaļu parastā daļā.",
        "Salīdzinu periodiskas decimāldaļas.",
    ]),

    Majas([
        "Pārveido daļās: 0,(7), 0,(36), 0,2(3).",
        "Pārbaudi, izdalot iegūtās daļas.",
        "Paskaidro draugam, kāpēc 0,(9) = 1.",
    ]),
]
