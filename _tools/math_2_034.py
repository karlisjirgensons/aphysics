# -*- coding: utf-8 -*-
"""2. klase, 34. stunda: «Kad rodas jauns desmits?»

Ja vienu summa ir 10 vai vairāk, desmit kubiņus sasien jaunā stienī: 38 +
25 = 50 + 13 = 63. Tā ir pāreja jaunā desmitā - vieni «pārlec» uz
desmitiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, desmiti)

TEMA = "Kad rodas jauns desmits?"

MERKIS = ("Šodien saskaitīsim divciparu skaitļus ar pāreju jaunā desmitā un "
          "izskaidrosim, kas notiek ar vieniem.")

SATURS = [
    Sakums("Ko darīt, ja kubiņu sanāk 13?",
           zimejums=desmiti(5, 13),
           paraksts="Desmit kubiņi - tas jau ir jauns stienis!",
           fakti=["8 + 5 = 13 vieni.",
                  "13 vieni = 1 desmits un 3 vieni.",
                  "Jaunais desmits pievienojas pārējiem."]),

    Doma("Jauns desmits",
         "Ja vienu ir 10 vai vairāk, desmit no tiem kļūst par desmitu.",
         soli=[
             "38 + 25: desmiti 30 + 20 = 50.",
             "Vieni 8 + 5 = 13.",
             "13 = 10 + 3 - jauns desmits.",
             "50 + 13 = 63.",
         ]),

    Slidnis("38 + 25 ar kubiņiem", [
        {"v": "38 + 25", "teksts": "5 stieņi un 13 kubiņi.",
         "zim": desmiti(5, 13)},
        {"v": "10 kubiņi = 1 stienis", "teksts": "Sasien desmit kubiņus.",
         "zim": desmiti(6, 3)},
        {"v": "63", "teksts": "6 desmiti un 3 vieni.",
         "zim": desmiti(6, 3)},
    ]),

    Paraugs("Cik ir 47 + 36?",
            uzd="Saskaiti ar pāreju jaunā desmitā.",
            soli=[("40 + 30 = 70", "Desmiti."),
                  ("7 + 6 = 13", "Vieni - vairāk par 10!"),
                  ("70 + 13 = 83", "Jaunais desmits pievienojas.")],
            atbilde="83"),

    Ievadi("Saskaiti", [
        {"jaut": "28 + 15 = ?", "atb": ["43"], "padoms": "30 + 13."},
        {"jaut": "36 + 27 = ?", "atb": ["63"], "padoms": "50 + 13."},
        {"jaut": "49 + 34 = ?", "atb": ["83"], "padoms": "70 + 13."},
        {"jaut": "57 + 26 = ?", "atb": ["83"], "padoms": "70 + 13."},
        {"jaut": "65 + 29 = ?", "atb": ["94"], "padoms": "80 + 14."},
        {"jaut": "18 + 18 = ?", "atb": ["36"], "padoms": "20 + 16."},
    ], pamats=4),

    Varianti("Vai rodas jauns desmits?", [
        {"jaut": "42 + 35", "opcijas": ["Nē", "Jā"], "jaukt": False,
         "pareizi": 0, "padoms": "2 + 5 = 7 - mazāk par 10."},
        {"jaut": "46 + 37", "opcijas": ["Nē", "Jā"], "jaukt": False,
         "pareizi": 1, "padoms": "6 + 7 = 13."},
        {"jaut": "55 + 25", "opcijas": ["Nē", "Jā"], "jaukt": False,
         "pareizi": 1, "padoms": "5 + 5 = 10 - tieši desmits!"},
        {"jaut": "Anna: 38 + 25 = 513. Kur kļūda?",
         "opcijas": ["Aizmirsa pārnest desmitu", "Nav kļūdas",
                     "Atņēma"], "pareizi": 0,
         "padoms": "13 vieni nav jāraksta blakus."},
    ]),

    Pasaule("Cik kilometru nobrauca?",
            Ievadi("", [
                {"jaut": "Pirmajā dienā velotūristi nobrauca 38 km, otrajā - "
                         "27 km. Cik kopā?", "atb": ["65"], "mers": "km",
                 "padoms": "50 + 15."},
                {"jaut": "Trešajā dienā vēl 26 km. Cik visās dienās?",
                 "atb": ["91"], "mers": "km", "padoms": "65 + 26."},
            ]),
            pavediens="celojums",
            konteksts="Ģimene brauc ar velosipēdiem ap Latgales ezeriem.",
            kapec="Kopējo ceļu plāno, lai zinātu, cik dienu vajag."),

    Kopsavilkums([
        "Saskaitu divciparu skaitļus ar pāreju jaunā desmitā.",
        "Zinu, ka 10 vieni ir 1 desmits.",
        "Pievienoju jauno desmitu pārējiem.",
    ]),

    Majas([
        "Ar sērkociņiem vai zīmuļiem parādi 27 + 15.",
        "Kad rodas jauns desmits, sasien to ar gumiju.",
        "Izrēķini: 39 + 24, 56 + 35.",
    ]),
]
