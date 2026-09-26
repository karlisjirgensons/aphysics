# -*- coding: utf-8 -*-
"""1. klase, 135. stunda: «Cik ir pusseptiņi?»

Pusstunda - garais rādītājs uz 6, īsais pusceļā starp cipariem.
«Pusseptiņi» = 6:30 (puse ceļa uz septiņiem). Latviski pusstundu sauc
pēc nākamās stundas - tas bieži jauc.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, pulkstenis)

TEMA = "Cik ir pusseptiņi?"

MERKIS = ("Šodien nolasīsim un parādīsim pilnas stundas un pusstundas "
          "pulkstenī.")

SATURS = [
    Sakums("Pusseptiņi - tas ir pirms vai pēc septiņiem?",
           zimejums=pulkstenis(6, 30),
           paraksts="Pusseptiņi = 6:30 - puse ceļa uz septiņiem.",
           fakti=["Pusstundā garais rādītājs uz 6.",
                  "Īsais - pusceļā starp cipariem.",
                  "«Pus-» nosauc nākamo stundu."]),

    Slidnis("No sešiem līdz septiņiem", [
        {"v": "6:00", "teksts": "Pulksten seši", "zim": pulkstenis(6)},
        {"v": "6:30", "teksts": "Pusseptiņi", "zim": pulkstenis(6, 30)},
        {"v": "7:00", "teksts": "Pulksten septiņi", "zim": pulkstenis(7)},
    ]),

    Doma("Pusstunda",
         "Garais uz 6 - pusstunda; stunda nosaukta pēc nākamās.",
         soli=[
             "Garais uz 6? - Tā ir pusstunda.",
             "Īsais starp 6 un 7? - Pusseptiņi.",
             "Ar cipariem: 6:30.",
         ]),

    Ievadi("Cik pulkstenis? (raksti kā 6:30)", [
        {"jaut": "Cik rāda?", "zim": pulkstenis(8, 30),
         "atb": ["8:30", "8,30"], "tastatura": "text",
         "padoms": "Pusdeviņi."},
        {"jaut": "Cik rāda?", "zim": pulkstenis(3, 30),
         "atb": ["3:30", "3,30"], "tastatura": "text",
         "padoms": "Pusčetri."},
        {"jaut": "Cik rāda?", "zim": pulkstenis(10), "atb": ["10:00", "10"],
         "tastatura": "text", "padoms": "Pilna stunda."},
        {"jaut": "Cik rāda?", "zim": pulkstenis(12, 30),
         "atb": ["12:30", "12,30"], "tastatura": "text",
         "padoms": "Pusviens."},
    ]),

    Varianti("Kā sauc?", [
        {"jaut": "7:30", "opcijas": ["pusastoņi", "pusseptiņi",
                                     "septiņi"], "pareizi": 0,
         "padoms": "Puse ceļa uz astoņiem."},
        {"jaut": "Pusdivi", "opcijas": ["1:30", "2:30", "2:00"],
         "pareizi": 0, "padoms": "Puse ceļa uz diviem."},
        {"jaut": "Kurš rāda pusdeviņi?", "zim": pulkstenis(8, 30),
         "opcijas": ["šis", "neviens"], "jaukt": False, "pareizi": 0,
         "padoms": "8:30."},
    ]),

    Pasaule("Multfilma",
            Varianti("", [
                {"jaut": "Multfilma sākas pusseptiņos. Pulkstenis rāda 6:00. "
                         "Vai jau sākusies?",
                 "opcijas": ["Nē - vēl pusstunda", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "Pusseptiņi = 6:30."},
            ]),
            pavediens="maja",
            konteksts="Vakarā visi gaida multfilmu.",
            kapec="«Pusseptiņi» nav 7:30!"),

    Kopsavilkums([
        "Nolasu pusstundas.",
        "Zinu: pusseptiņi = 6:30.",
        "Pierakstu laiku ar cipariem.",
    ]),

    Majas([
        "Pasaki mājiniekiem laiku pusstundās visu dienu.",
        "Parādi savā pulkstenī pusastoņi.",
        "Kad tev sākas stunda - pilnā stundā vai pusstundā?",
    ]),
]
