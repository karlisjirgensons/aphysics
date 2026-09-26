# -*- coding: utf-8 -*-
"""1. klase, 169. stunda: «Kur gada laikā noderēja matemātika?»

Gada apkopojums: skaitīšana, saskaitīšana un atņemšana, mērīšana, laiks,
nauda, figūras. Skolēns katrai jomai atrod piemēru no savas dzīves.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, bildes)

TEMA = "Kur gada laikā noderēja matemātika?"

MERKIS = ("Šodien apkoposim gadā apgūto un atradīsim piemērus no savas "
          "dzīves.")

SATURS = [
    Sakums("Ko tu iemācījies šogad?",
           zimejums=bildes([["abols", "zimulis", "masina", "zvaigzne",
                             "kvadrats"]]),
           paraksts="Skaitļi, mērīšana, laiks, nauda, figūras.",
           fakti=["Skaitām līdz 100.",
                  "Saskaitām un atņemam 20 apjomā.",
                  "Mērām, zinām laiku un naudu."]),

    Doma("Gada ceļš",
         "Katra joma noder dzīvē.",
         soli=[
             "Skaitīšana - cik ir.",
             "Saskaitīšana un atņemšana - cik kopā, cik palika.",
             "Mērīšana - cik garš, smags.",
             "Laiks un nauda - kad un cik maksā.",
             "Figūras - formas ap mums.",
         ]),

    Ievadi("Atkārtojums", [
        {"jaut": "8 + 7 = ?", "atb": ["15"], "padoms": "8 + 2 + 5."},
        {"jaut": "Cik cm ir 1 dm?", "atb": ["10"], "padoms": "Desmits."},
        {"jaut": "Cik centu ir 1 eiro?", "atb": ["100"], "padoms": "Simts."},
        {"jaut": "Cik stūru ir piecstūrim?", "atb": ["5"],
         "padoms": "Vārdā."},
        {"jaut": "Cik minūšu ir stundā?", "atb": ["60"], "padoms": "Aplis."},
        {"jaut": "Kurš skaitlis ir pēc 99?", "atb": ["100"],
         "padoms": "Simts."},
    ], pamats=4),

    Varianti("Kur tas noderēja?", [
        {"jaut": "Veikalā noderēja...",
         "opcijas": ["nauda un saskaitīšana", "simetrija", "kubi"],
         "pareizi": 0, "padoms": "Cenas."},
        {"jaut": "Lai nenokavētu, noderēja...",
         "opcijas": ["pulkstenis", "lineāls", "kauliņi"], "pareizi": 0,
         "padoms": "Laiks."},
        {"jaut": "Zīmējot kartīti, noderēja...",
         "opcijas": ["simetrija", "nauda", "kilogrami"], "pareizi": 0,
         "padoms": "Vienādas puses."},
    ]),

    Petijums("Mana matemātikas grāmatiņa", [
        "Uzzīmē 5 lapiņas - katrai jomai viena.",
        "Katrā uzzīmē, kur tā tev noderēja.",
        "Saspraud grāmatiņā.",
        "Parādi klasei vienu lapiņu.",
    ], vajag="papīrs, krāsas, skavotājs"),

    Pasaule("Gada svētki",
            Ievadi("", [
                {"jaut": "Klases svētkiem 20 bērni, katram 1 kūkas gabals. "
                         "Nogrieza 16. Cik vēl jānogriež?", "atb": ["4"],
                 "padoms": "20 − 16."},
            ]),
            pavediens="skola",
            konteksts="Gada beigās klase svin svētkus.",
            kapec="Matemātika noder arī svētkos."),

    Kopsavilkums([
        "Zinu, ko šogad iemācījos.",
        "Atrodu piemērus no dzīves.",
        "Stāstu par savu gadu.",
    ]),

    Majas([
        "Pastāsti mājiniekiem, kas tev patika matemātikā.",
        "Atrodi mājās 3 vietas, kur noder matemātika.",
        "Uzzīmē savu mīļāko uzdevumu.",
    ]),
]
