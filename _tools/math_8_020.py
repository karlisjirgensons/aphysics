# -*- coding: utf-8 -*-
"""8. klase, 20. stunda: «Kā kāpina pakāpi?»

(a^2)^3 ir trīs reizes pēc kārtas a^2 - kāpinātāji saskaitās trīs reizes,
tātad reizinās. Galvenā kļūda ir sajaukt to ar reizināšanu (saskaitīt),
tāpēc abas īpašības stundā stāv blakus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā kāpina pakāpi?"

MERKIS = ("Formulēsim un lietosim pakāpes kāpināšanas īpašību.")

SATURS = [
    Sakums("Kubs no kvadrātiem",
           zimejums=restis([["(2²)³", "=", "2² · 2² · 2²", "=", "2⁶"]]),
           paraksts="Trīs reizes pa divi - seši reizinātāji.",
           fakti=["(2²)³ = 4³ = 64 = 2⁶.",
                  "Kāpinot pakāpi, kāpinātājus reizina.",
                  "Reizinot pakāpes, kāpinātājus saskaita."]),

    Slidnis("No kāpināšanas uz reizināšanu", [
        {"v": "(a^2)^3", "teksts": "a^2 trīs reizes"},
        {"v": "a^2 · a^2 · a^2", "teksts": "Reizināšanas īpašība"},
        {"v": "a^{2 + 2 + 2}", "teksts": "Trīs vienādi saskaitāmie"},
        {"v": "a^6", "teksts": "2 · 3 = 6"},
        {"v": "(a^m)^n = a^{mn}", "teksts": "Kāpinātājus reizina"},
    ]),

    Doma("Kāpināšanas īpašība",
         "Kāpinot pakāpi, bāzi atstāj, bet kāpinātājus sareizina: "
         "(a^m)^n = a^{mn}.",
         soli=[
             "(a^m)^n - iekavas ar kāpinātāju ārpusē: reizina.",
             "a^m · a^n - divas pakāpes blakus: saskaita.",
             "Pārbaude ar mazu skaitli: (2^2)^3 = 4^3 = 64 = 2^6.",
         ],
         pieze="Kad šaubies, izraksti reizinātājus vai pārbaudi ar a = 2 - "
               "tas aizņem pusminūti un pasargā no kļūdas."),

    Paraugs("Divas īpašības kopā",
            uzd="Vienkāršo (x^3)^4 · x^2.",
            soli=[
                ("(x^3)^4 = x^{12}", "3 · 4."),
                ("x^{12} · x^2 = x^{14}", "12 + 2."),
            ],
            atbilde="x^{14}"),

    Ievadi("Vienkāršo", [
        {"jaut": "(a^4)^2", "atb": ["a^8"], "padoms": "4 · 2.",
         "tastatura": "text"},
        {"jaut": "(y^5)^3", "atb": ["y^15", "y^{15}"], "padoms": "5 · 3.",
         "tastatura": "text"},
        {"jaut": "(3^2)^2 - aprēķini", "atb": ["81"], "padoms": "3^4."},
        {"jaut": "(x^2)^5 : x^4", "atb": ["x^6"], "padoms": "x^{10} : x^4.",
         "tastatura": "text"},
        {"jaut": "(10^3)^2 - cik nuļļu?", "atb": ["6"],
         "padoms": "10^6."},
        {"jaut": "4^3 pieraksti kā pakāpi ar bāzi 2",
         "atb": ["2^6"], "padoms": "(2^2)^3.", "tastatura": "text"},
    ], pamats=4),

    Varianti("Reizināt vai saskaitīt?", [
        {"jaut": "(a^3)^5 =",
         "opcijas": ["a^{15}", "a^8", "a^{35}", "5a^3"],
         "pareizi": 0, "padoms": "Iekavas - reizina."},
        {"jaut": "a^3 · a^5 =",
         "opcijas": ["a^8", "a^{15}", "a^2", "2a^8"],
         "pareizi": 0, "padoms": "Blakus - saskaita."},
        {"jaut": "(a^2)^3 · a =",
         "opcijas": ["a^7", "a^6", "a^9", "a^{12}"],
         "pareizi": 0, "padoms": "a^6 · a^1."},
    ]),

    Pasaule("Papīra locīšana",
            Ievadi("", [
                {"jaut": "Katrā pārlocījumā kārtu skaits divkāršojas. Cik "
                         "kārtu pēc 5 pārlocījumiem?",
                 "atb": ["32"], "padoms": "2^5."},
                {"jaut": "Katru reizi locot 3 reizes pēc kārtas (2^3 kārtas), "
                         "to atkārto 2 reizes: (2^3)^2. Cik kārtu?",
                 "atb": ["64"], "padoms": "2^6."},
                {"jaut": "Papīrs 0,1 mm biezs. Cik mm biezs ir 64 kārtu "
                         "sainis?",
                 "atb": ["6,4", "6.4"], "padoms": "64 · 0,1."},
            ]),
            pavediens="tehnika",
            konteksts="Pierādīts, ka parastu lapu ar rokām nevar pārlocīt vairāk "
                      "par 7-8 reizēm - biezums aug pakāpēs.",
            kapec="Pakāpe aug ātrāk, nekā intuīcija gaida."),

    Kopsavilkums([
        "Pamatoju (a^m)^n = a^{mn}.",
        "Atšķiru kāpināšanu (reizina) no reizināšanas (saskaita).",
        "Pārbaudu ar mazu skaitli.",
    ]),

    Majas([
        "Vienkāršo: (b^3)^3, (x^2)^4 · x, (5^2)^3 : 5^4.",
        "Pieraksti 8^2 un 16^3 kā pakāpes ar bāzi 2.",
        "Izmēģini pārlocīt lapu 8 reizes un pieraksti kārtu skaitu.",
    ]),
]
