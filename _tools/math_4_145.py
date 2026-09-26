# -*- coding: utf-8 -*-
"""4. klase, 145. stunda: «Cik liels ir kvadrātmetrs?»

1 m² - kvadrāts, kurā var nostāties četri bērni. Skolēns novērtē telpas
virsmu laukumu m² (tāfele, grīda, logs) un pārbauda, izmērot garumu un
platumu. Novērtēšana ar aci ir prasme, ko lieto dzīvē daudz biežāk nekā
precīzo rēķinu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas)

TEMA = "Cik liels ir kvadrātmetrs?"

MERKIS = ("Novērtēsim telpas virsmu laukumu kvadrātmetros un pārbaudīsim "
          "novērtējumu.")

SATURS = [
    Sakums("Cik bērnu ietilpst kvadrātmetrā?",
           zimejums=kolonnas([("tāfele", 4), ("durvis", 2), ("grīda", 56),
                              ("logs", 3)], " m²"),
           paraksts="Klases virsmas kvadrātmetros (aptuveni).",
           fakti=["1 m² - kvadrāts 1 m × 1 m.",
                  "Tajā cieši var nostāties 4 bērni."]),

    Doma("Novērtē, tad izmēri",
         "Laukumu m² vispirms novērtē ar aci (cik kvadrātmetru «ietilpst»), "
         "tad izmēra garumu un platumu metros un sareizina.",
         soli=[
             "Iedomājies 1 m² kvadrātu uz virsmas.",
             "Novērtē, cik tādu ietilpst.",
             "Izmēri garumu un platumu metros.",
             "Sareizini un salīdzini ar novērtējumu.",
         ],
         pieze="Klase 8 m × 7 m = 56 m²; tajā 28 skolēniem katram 2 m²."),

    Petijums("Klases mērīšana",
             soli=[
                 "Izveido 1 m² kvadrātu no avīzēm vai auklas.",
                 "Novērtē tāfeles, grīdas un loga laukumu.",
                 "Izmēri ar mērlenti un aprēķini.",
                 "Salīdzini novērtējumus ar mērījumiem.",
             ],
             vajag="mērlente, avīzes vai aukla, līmlente",
             secinajums="Ar praksi novērtējums kļūst arvien precīzāks."),

    Ievadi("Aprēķini m²", [
        {"jaut": "Klase 8 m × 7 m. Laukums?", "atb": ["56"],
         "padoms": "8 · 7."},
        {"jaut": "Tāfele 4 m × 1 m. Laukums?", "atb": ["4"],
         "padoms": "4 · 1."},
        {"jaut": "Istaba 5 m × 4 m. Laukums?", "atb": ["20"],
         "padoms": "5 · 4."},
        {"jaut": "Sporta zāle 30 m × 18 m. Laukums?", "atb": ["540"],
         "padoms": "30 · 18."},
    ]),

    Varianti("Kas ir aptuveni?", [
        {"jaut": "Cik m² aptuveni ir durvis?",
         "opcijas": ["2", "20", "200", "0"], "pareizi": 0,
         "padoms": "2 m × 1 m."},
        {"jaut": "Cik m² aptuveni ir skolas galds?",
         "opcijas": ["1", "10", "100", "1000"], "pareizi": 0,
         "padoms": "Ap 1 m × 1 m."},
        {"jaut": "Kurā vienībā mēra klases grīdu?",
         "opcijas": ["m²", "cm²", "mm²", "km"], "pareizi": 0,
         "padoms": "Lielām virsmām - m²."},
    ]),

    Pasaule("Dzīvokļa plāns",
            Ievadi("", [
                {"jaut": "Guļamistaba 4 m × 3 m. Cik m²?", "atb": ["12"],
                 "padoms": "4 · 3."},
                {"jaut": "Viesistaba 6 m × 4 m. Cik m²?", "atb": ["24"],
                 "padoms": "6 · 4."},
                {"jaut": "Virtuve 3 m × 3 m. Cik m²?", "atb": ["9"],
                 "padoms": "3 · 3."},
                {"jaut": "Cik m² visās trijās telpās?", "atb": ["45"],
                 "padoms": "12 + 24 + 9."},
            ]),
            pavediens="maja",
            konteksts="Dzīvokļa sludinājumos lielumu raksta m² - tas "
                      "palīdz salīdzināt dzīvokļus.",
            kapec="Kvadrātmetri ir mājokļa valoda."),

    Kopsavilkums([
        "Zinu, cik liels ir 1 m².",
        "Novērtēju virsmas laukumu m².",
        "Pārbaudu novērtējumu ar mērīšanu.",
    ]),

    Majas([
        "Izmēri savu istabu un aprēķini laukumu.",
        "Atrodi sludinājumā dzīvokli un salīdzini tā m² ar savu māju.",
        "Novērtē un izmēri gultas laukumu.",
    ]),
]
