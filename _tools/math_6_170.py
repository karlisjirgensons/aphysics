# -*- coding: utf-8 -*-
"""6. klase, 170. stunda: «Ko protu ar procentiem un attiecību?»

Otrā noslēguma stunda. Attiecība no gada sākuma un procenti no gada vidus
izrādās viens un tas pats rīks: abi apraksta daļu no kopuma. Te tie tiek
salikti blakus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Ko protu ar procentiem un attiecību?"

MERKIS = ("Atkārtosim attiecību, mērogu un procentus un saskatīsim to "
          "kopīgo.")

SATURS = [
    Sakums("Attiecība un procenti ir viens rīks",
           zimejums=dala(5, 2, "2 : 3 jeb 40 %"),
           paraksts="Attiecība 2 pret 3 nozīmē, ka pirmajam pienākas 40 % "
                    "no kopuma.",
           fakti=["Attiecība sadala kopumu daļās.",
                  "Procenti pasaka daļu no simta.",
                  "Abus var pārrakstīt vienu otrā."]),

    Doma("No attiecības uz procentiem",
         "Attiecību pārvērš procentos, katru skaitli izdalot ar daļu summu "
         "un pārrēķinot simtdaļās.",
         soli=[
             "Saskaiti attiecības skaitļus - tas ir daļu skaits.",
             "Katram pierakstīti daļu no kopuma.",
             "Pārvērt daļu procentos.",
             "Pārbaudi: procentu summai jābūt 100 %.",
             "Vajadzības gadījumā pārrēķini eiro vai kilogramos.",
         ],
         pieze="Mērogs ir tā pati attiecība: 1 : 500 nozīmē, ka kartes "
               "attālums ir {1|500} no dabas attāluma. Tāpēc visi trīs "
               "jēdzieni ir viens rīks trijos pierakstos."),

    Paraugs("Attiecība, procenti, mērogs",
            uzd="Kopums 60 sadalīts attiecībā 2 : 3. Cik ir katram un cik "
                "procentu?",
            soli=[
                ("2 + 3 = 5 daļas; 60 : 5 = 12",
                 "Viena daļa."),
                ("Pirmais: 2 · 12 = 24; otrais: 3 · 12 = 36",
                 "Abas daļas."),
                ("24 no 60 ir 40 %",
                 "{24|60} = {2|5}."),
                ("36 no 60 ir 60 %; kopā 100 %",
                 "Pārbaude."),
            ],
            atbilde="24 un 36; 40 % un 60 %"),

    Ievadi("Atkārto attiecību un procentus", [
        {"jaut": "Kopums 60, attiecība 2 : 3. Cik ir pirmajam?",
         "atb": ["24"], "padoms": "5 daļas pa 12."},
        {"jaut": "Cik procenti tas ir no kopuma?",
         "atb": ["40"], "padoms": "{24|60}."},
        {"jaut": "Cik procenti ir otrajam?",
         "atb": ["60"], "padoms": "100 − 40."},
        {"jaut": "Mērogs 1 : 500, kartē 6 cm. Cik metru dabā?",
         "atb": ["30"], "padoms": "3000 cm."},
        {"jaut": "Cena 80 €, atlaide 15 %. Cik eiro ir atlaide?",
         "atb": ["12"], "padoms": "1 % ir 0,8 €."},
        {"jaut": "Ja 30 % ir 21, cik ir kopums?",
         "atb": ["70"], "padoms": "1 % ir 0,7."},
    ], pamats=4),

    Varianti("Kurš rīks te der?", [
        {"jaut": "«Sadalīt 60 attiecībā 2 : 3» nozīmē...",
         "opcijas": ["sadalīt 5 vienādās daļās un tad grupēt",
                     "dalīt ar 2 un ar 3",
                     "reizināt ar 2 un ar 3", "atņemt"],
         "pareizi": 0,
         "padoms": "Vispirms daļu skaits."},
        {"jaut": "Attiecība 1 : 4 procentos ir...",
         "opcijas": ["20 % un 80 %", "1 % un 4 %",
                     "25 % un 75 %", "10 % un 40 %"],
         "pareizi": 0,
         "padoms": "5 daļas; viena daļa ir 20 %."},
        {"jaut": "Mērogs 1 : 1000 nozīmē, ka 1 cm kartē ir...",
         "opcijas": ["10 m dabā", "1000 m dabā",
                     "100 m dabā", "1 m dabā"],
         "pareizi": 0,
         "padoms": "1000 cm = 10 m."},
        {"jaut": "Kas ir kopīgs attiecībai un procentiem?",
         "opcijas": ["Abi apraksta daļu no kopuma",
                     "Abi ir mērvienības",
                     "Abi ir veseli skaitļi", "Nekas"],
         "pareizi": 0,
         "padoms": "Viens rīks, divi pieraksti."},
    ], pamats=4),

    Pasaule("Kā sadalīt pasākuma budžetu?",
            Ievadi("", [
                {"jaut": "Budžets 300 €, sadala attiecībā 3 : 2. Cik eiro ir "
                         "viena daļa?",
                 "atb": ["60"], "padoms": "5 daļas."},
                {"jaut": "Cik eiro ir lielākajai daļai?",
                 "atb": ["180"], "padoms": "3 · 60."},
                {"jaut": "Cik procenti tas ir no budžeta?",
                 "atb": ["60"], "padoms": "{180|300}."},
                {"jaut": "Ja budžetu samazinātu par 20 %, cik eiro tas būtu?",
                 "atb": ["240"], "padoms": "300 · 0,8."},
            ]),
            pavediens="skola",
            konteksts="Pasākuma budžetu sadala attiecībā, bet pārskatā raksta "
                      "procentos - tas ir viens un tas pats sadalījums.",
            kapec="Viens rīks trijos pierakstos: attiecība, daļa, procenti."),

    Kopsavilkums([
        "Sadalu kopumu dotā attiecībā.",
        "Pārvēršu attiecību procentos un otrādi.",
        "Lietoju mērogu abos virzienos.",
        "Aprēķinu procentus no skaitļa un kopumu no procentiem.",
    ]),

    Majas([
        "Sadali 120 attiecībā 1 : 3 un pieraksti abas daļas procentos.",
        "Aprēķini, cik metru dabā ir 4 cm kartē mērogā 1 : 2000.",
        "Atrodi, cik ir kopums, ja 40 % ir 32.",
    ]),
]
