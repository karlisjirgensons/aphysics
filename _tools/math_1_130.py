# -*- coding: utf-8 -*-
"""1. klase, 130. stunda: «Cik jāizdod atpakaļ?»

Atlikums = samaksāts − cena. Pārdevēji bieži skaita uz priekšu: cena 7 €,
iedod 10 € - «8, 9, 10» - atlikums 3 €.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, monetas)

TEMA = "Cik jāizdod atpakaļ?"

MERKIS = ("Šodien izspēlēsim iepirkšanos un noteiksim, cik jāizdod "
          "atpakaļ.")

SATURS = [
    Sakums("Cena 7 €, tu iedod 10 €. Cik atpakaļ?",
           zimejums=monetas(["10 €"]),
           paraksts="10 − 7 = 3: atlikums 3 €.",
           fakti=["Atlikums = iedots − cena.",
                  "Var skaitīt uz priekšu no cenas.",
                  "Pārbaude: cena + atlikums = iedots."]),

    Paraugs("Atlikums",
            uzd="Sula maksā 2 €. Tu iedod 5 €. Cik atlikums?",
            soli=[
                ("5 € − 2 €", "Iedots mīnus cena."),
                ("= 3 €", "Aprēķins."),
                ("2 € + 3 € = 5 €", "Pārbaude."),
            ],
            atbilde="atlikums ir 3 €."),

    Doma("Kā pārdevējs",
         "Skaiti no cenas līdz iedotajai summai.",
         soli=[
             "Cena 7 €.",
             "Skaiti: 8, 9, 10 - trīs eiro.",
             "Izdod 3 €.",
         ]),

    Ievadi("Cik atlikums?", [
        {"jaut": "Cena 6 €, iedod 10 €.", "atb": ["4"], "padoms": "10 − 6."},
        {"jaut": "Cena 13 €, iedod 20 €.", "atb": ["7"], "padoms": "20 − 13."},
        {"jaut": "Cena 80 c, iedod 1 € (100 c). Cik centu?", "atb": ["20"],
         "padoms": "100 − 80."},
        {"jaut": "Cena 45 c, iedod 50 c. Cik centu?", "atb": ["5"],
         "padoms": "50 − 45."},
        {"jaut": "Cena 9 €, iedod 20 €.", "atb": ["11"], "padoms": "20 − 9."},
        {"jaut": "Cena 15 €, iedod 20 €.", "atb": ["5"], "padoms": "20 − 15."},
    ], pamats=4),

    Petijums("Veikals klasē", [
        "Viens ir pārdevējs, otrs - pircējs.",
        "Pircējs izvēlas preci un iedod lielāku naudu.",
        "Pārdevējs izdod atlikumu, skaitot uz priekšu.",
        "Pārbaudiet kopā.",
    ], vajag="rotaļu nauda, preces ar cenām"),

    Pasaule("Saldējums",
            Ievadi("", [
                {"jaut": "Saldējums 1 € 20 c. Iedod 2 €. Cik centu atpakaļ?",
                 "atb": ["80"], "padoms": "No 1 € 20 c līdz 2 € - 80 c."},
            ]),
            pavediens="veikals",
            konteksts="Kioskā pērc saldējumu.",
            kapec="Pārbaudi atlikumu - tā ir tava nauda."),

    Kopsavilkums([
        "Aprēķinu atlikumu.",
        "Skaitu uz priekšu no cenas.",
        "Pārbaudu: cena + atlikums = iedots.",
    ]),

    Majas([
        "Nākamreiz veikalā aprēķini atlikumu pirms pārdevēja.",
        "Izspēlē veikalu ar mājiniekiem.",
        "Pieraksti 3 pirkumus un atlikumus.",
    ]),
]
