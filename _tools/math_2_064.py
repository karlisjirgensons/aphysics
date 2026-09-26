# -*- coding: utf-8 -*-
"""2. klase, 64. stunda: «Cik ilgi es esmu ceļā?»

Klase savāc datus par to, cik minūšu katrs pavada ceļā uz skolu, un sagrupē
tos intervālos tabulā. Tā parādās jautājumi, uz kuriem var atbildēt tikai ar
datiem: cik daudziem ceļš ir īsāks par 10 minūtēm?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Cik ilgi es esmu ceļā?"

MERKIS = ("Šodien savāksim klases datus par ceļā pavadīto laiku un "
          "apkoposim tos tabulā.")

_CELS = restis([["ceļā", "bērnu skaits"], ["līdz 10 min", 9],
                ["10-20 min", 11], ["20-30 min", 5], ["vairāk", 2]])

SATURS = [
    Sakums("Kurš klasē dzīvo vistālāk no skolas?",
           zimejums=_CELS,
           paraksts="27 bērnu dati vienā tabulā.",
           fakti=["Katrs pastāsta, cik minūšu ir ceļā.",
                  "Datus sagrupē pa 10 minūtēm.",
                  "Tabula parāda visu klasi uzreiz."]),

    Doma("No saraksta uz tabulu",
         "Katru skaitli ieliek savā grupā un saskaita, cik ir katrā.",
         soli=[
             "Pieraksti katra bērna laiku.",
             "Izvēlies grupas: līdz 10, 10-20, 20-30 min, vairāk.",
             "Katram laikam ievelc svītriņu savā grupā.",
             "Saskaiti svītriņas un ieraksti skaitu.",
         ]),

    Petijums("Mūsu klases ceļš", [
        "Katrs uzraksta uz lapiņas, cik minūšu ir ceļā uz skolu.",
        "Salieciet lapiņas pa grupām uz tāfeles.",
        "Saskaitiet katru grupu un aizpildiet tabulu.",
        "Kurā grupā ir visvairāk bērnu?",
    ], vajag="lapiņas, tāfele"),

    Ievadi("Nolasi tabulu", [
        {"jaut": "Cik bērnu ir ceļā līdz 10 min?", "zim": _CELS,
         "atb": ["9"], "padoms": "Pirmā rinda."},
        {"jaut": "Cik bērnu ir ceļā vairāk nekā 20 min?", "zim": _CELS,
         "atb": ["7"], "padoms": "5 + 2."},
        {"jaut": "Cik bērnu ir klasē?", "zim": _CELS, "atb": ["27"],
         "padoms": "9 + 11 + 5 + 2."},
        {"jaut": "Par cik vairāk bērnu grupā 10-20 min nekā līdz 10?",
         "zim": _CELS, "atb": ["2"], "padoms": "11 − 9."},
    ]),

    Varianti("Kurā grupā?", [
        {"jaut": "Ievas ceļš ir 15 minūtes. Kurā grupā viņa ir?",
         "zim": _CELS, "opcijas": ["10-20 min", "līdz 10 min",
                                   "20-30 min"], "pareizi": 0,
         "padoms": "15 ir starp 10 un 20."},
        {"jaut": "Kura grupa ir vislielākā?", "zim": _CELS,
         "opcijas": ["10-20 min", "līdz 10 min", "vairāk"],
         "pareizi": 0, "padoms": "Lielākais skaitlis."},
    ]),

    Pasaule("Cik agri jāiziet?",
            Ievadi("", [
                {"jaut": "Markuss ir ceļā 25 min, skola sākas 8:30. Cik "
                         "minūtes pēc 8:00 viņam jāiziet?", "atb": ["5"],
                 "padoms": "8:30 − 25 min = 8:05."},
                {"jaut": "Elīnai ceļš ir 8 min. Par cik minūtēm vēlāk nekā "
                         "Markuss viņa var iziet?", "atb": ["17"],
                 "padoms": "25 − 8."},
            ]),
            pavediens="skola",
            konteksts="Katram bērnam ceļš uz skolu ir citāds.",
            kapec="Dati palīdz saprast, kurš ceļā pavada visvairāk laika."),

    Kopsavilkums([
        "Savācu klases datus.",
        "Sagrupēju tos tabulā.",
        "Nolasu tabulu un rēķinu ar tās skaitļiem.",
    ]),

    Majas([
        "Nedēļu pieraksti, cik minūšu esi ceļā uz skolu.",
        "Kurā dienā ceļš bija visilgākais?",
        "Kāpēc tā varēja būt?",
    ]),
]
