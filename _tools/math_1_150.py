# -*- coding: utf-8 -*-
"""1. klase, 150. stunda: «Kā izteiksmē ielikt savu iepirkumu?»

Reālu iepirkumu pieraksta kā izteiksmi ar nosauktiem skaitļiem:
20 € + 30 € + 5 € = 55 €. Pirms aprēķina novērtē, pēc tam pārbauda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā izteiksmē ielikt savu iepirkumu?"

MERKIS = ("Šodien veidosim savu izteiksmi par reālu iepirkumu un "
          "aprēķināsim rezultātu.")

_CENAS = restis([["prece", "cena"], ["zābaki", "40 €"], ["cepure", "10 €"],
                 ["cimdi", "5 €"]])

SATURS = [
    Sakums("Ziemas iepirkums - kā to pierakstīt?",
           zimejums=_CENAS,
           paraksts="40 € + 10 € + 5 € = 55 €.",
           fakti=["Katra prece - skaitlis ar €.",
                  "Visas cenas savieno ar «+».",
                  "Atlikums - ar «−»."]),

    Doma("Mans iepirkums izteiksmē",
         "Izteiksmē ir visas cenas un darbības, kas notiek.",
         soli=[
             "Uzraksti katras preces cenu.",
             "Savieno ar «+» - kopējā summa.",
             "No naudas atņem summu - atlikums.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "40 € + 10 € + 5 € = ? €", "zim": _CENAS, "atb": ["55"],
         "padoms": "40 + 10 = 50, un 5."},
        {"jaut": "Tev 60 €. Cik paliek pēc pirkuma (€)?", "zim": _CENAS,
         "atb": ["5"], "padoms": "60 − 55."},
        {"jaut": "Bez cepures: 40 € + 5 € = ? €", "atb": ["45"],
         "padoms": "40 + 5."},
    ]),

    Varianti("Kura izteiksme der?", [
        {"jaut": "Nopirku grāmatu par 12 € un zīmuli par 3 €. Man bija 20 €.",
         "opcijas": ["20 − 12 − 3", "20 + 12 + 3", "12 + 3 + 20"],
         "pareizi": 0, "padoms": "No naudas atņem."},
    ]),

    Petijums("Mans iepirkums", [
        "Izvēlies 3 preces no reklāmas.",
        "Uzraksti izteiksmi ar cenām.",
        "Novērtē summu, tad izrēķini.",
        "Cik paliek no 100 €?",
    ], vajag="veikala reklāma, zīmulis"),

    Pasaule("Skolas somas pirkums",
            Ievadi("", [
                {"jaut": "Soma 30 €, penālis 8 €, pudele 2 €. Cik kopā (€)?",
                 "atb": ["40"], "padoms": "30 + 8 + 2."},
            ]),
            pavediens="skola",
            konteksts="Augustā gatavojas jaunajam mācību gadam.",
            kapec="Izteiksme parāda visu iepirkumu vienā rindā."),

    Kopsavilkums([
        "Veidoju izteiksmi par iepirkumu.",
        "Aprēķinu summu un atlikumu.",
        "Pārbaudu ar aplēsi.",
    ]),

    Majas([
        "Pieraksti ģimenes iepirkumu kā izteiksmi.",
        "Aprēķini summu.",
        "Salīdzini ar čeku.",
    ]),
]
