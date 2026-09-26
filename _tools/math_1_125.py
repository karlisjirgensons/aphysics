# -*- coding: utf-8 -*-
"""1. klase, 125. stunda: «Kā savākt datus par klasi?»

Klase savāc savus datus (mājdzīvnieki, brokastis): uzdod jautājumu,
atzīmē katru atbildi ar svītriņu, saskaita un ieraksta tabulā. Pēc tam
var uzzīmēt diagrammu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas, restis)

TEMA = "Kā savākt datus par klasi?"

MERKIS = ("Šodien savāksim klases datus un pierakstīsim tos tabulā.")

_BROKASTIS = restis([["putra", "maize", "jogurts", "pārslas"],
                     [8, 5, 4, 3]])

SATURS = [
    Sakums("Ko klase ēd brokastīs?",
           zimejums=_BROKASTIS,
           paraksts="Katrs atbild vienreiz; svītriņas saskaita.",
           fakti=["Uzdod vienu skaidru jautājumu.",
                  "Katru atbildi atzīmē ar svītriņu.",
                  "Saskaiti un ieraksti tabulā."]),

    Doma("Datu vākšana",
         "Katram bērnam - viena atbilde; kopā jābūt tik, cik bērnu.",
         soli=[
             "Izdomā jautājumu un atbilžu variantus.",
             "Aptaujā visus, atzīmē svītriņas.",
             "Saskaiti svītriņas.",
             "Pārbaudi: kopā tik, cik bērnu?",
         ]),

    Ievadi("Pārbaudi datus", [
        {"jaut": "Cik bērnu atbildēja kopā?", "zim": _BROKASTIS,
         "atb": ["20"], "padoms": "8 + 5 + 4 + 3."},
        {"jaut": "Par cik putras ēdāju vairāk nekā jogurta?",
         "zim": _BROKASTIS, "atb": ["4"], "padoms": "8 − 4."},
        {"jaut": "Klasē 21 bērns, bet atbildes 20. Cik neatbildēja?",
         "atb": ["1"], "padoms": "21 − 20."},
    ]),

    Varianti("Labs jautājums?", [
        {"jaut": "Kurš jautājums labāks aptaujai?",
         "opcijas": ["Kāds ir tavs mājdzīvnieks?",
                     "Vai tev patīk dzīvnieki un saldējums?"],
         "jaukt": False, "pareizi": 0, "padoms": "Viens jautājums."},
    ]),

    Petijums("Mūsu klases aptauja", [
        "Izvēlieties jautājumu: mājdzīvnieks, krāsa vai auglis.",
        "Uzrakstiet 3-4 atbilžu variantus.",
        "Aptaujājiet katru klasē, atzīmējiet svītriņas.",
        "Saskaitiet un ierakstiet tabulā.",
        "Uzzīmējiet stabiņu diagrammu.",
    ], vajag="lapa, zīmulis, krāsu zīmuļi"),

    Pasaule("Pēc aptaujas",
            Ievadi("", [
                {"jaut": "Kurš ēdiens populārākais? Cik bērnu?",
                 "zim": kolonnas([("putra", 8), ("maize", 5),
                                  ("jogurts", 4), ("pārslas", 3)]),
                 "atb": ["8"], "padoms": "Augstākais stabiņš."},
            ]),
            pavediens="virtuve",
            konteksts="Datus parāda skolas pavāram.",
            kapec="Pavārs zina, ko gatavot vairāk."),

    Kopsavilkums([
        "Savācu datus ar svītriņām.",
        "Ierakstu tos tabulā.",
        "Pārbaudu, vai atbildes sakrīt ar bērnu skaitu.",
    ]),

    Majas([
        "Aptaujā ģimeni: mīļākais ēdiens.",
        "Ieraksti tabulā.",
        "Uzzīmē diagrammu.",
    ]),
]
