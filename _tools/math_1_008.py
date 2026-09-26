# -*- coding: utf-8 -*-
"""1. klase, 8. stunda: «Kurš pēc kārtas?»

Pamata skaitlis atbild uz «cik?», kārtas skaitlis - uz «kurš pēc kārtas?».
Rindā vieta atkarīga no tā, no kuras puses skaita, tāpēc vispirms vienojas
par sākumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kurš pēc kārtas?"

MERKIS = ("Šodien teiksim, kurš pēc kārtas: pirmais, otrais, trešais.")

_RINDA = ["masina", "zivs", "putns", "sirds", "zvaigzne"]
_VARDI = {"masina": "mašīna", "zivs": "zivs", "putns": "putns",
          "sirds": "sirds", "zvaigzne": "zvaigzne"}

SATURS = [
    Sakums("Kurš ir trešais rindā?",
           zimejums=bildes([_RINDA]),
           paraksts="Skaitām no kreisās: mašīna ir pirmā, zivs - otrā.",
           fakti=["«Cik?» - pieci.",
                  "«Kurš pēc kārtas?» - pirmais, otrais, trešais.",
                  "Vispirms vienojies, no kuras puses skaiti."]),

    Doma("Cik? un Kurš?",
         "Skaitot pēc kārtas, pēdējais vārds pasaka vietu: trešais.",
         soli=[
             "Sāc no kreisās puses.",
             "Pirmais, otrais, trešais, ceturtais, piektais.",
             "Ja sāc no labās, vietas mainās.",
         ]),

    Varianti("Kurš pēc kārtas? (no kreisās)", [
        {"jaut": "Kas ir trešais?", "zim": bildes([_RINDA]),
         "opcijas": ["putns", "zivs", "sirds", "mašīna"], "pareizi": 0,
         "padoms": "Mašīna, zivs, putns."},
        {"jaut": "Kas ir piektais?", "zim": bildes([_RINDA]),
         "opcijas": ["zvaigzne", "sirds", "mašīna", "putns"], "pareizi": 0,
         "padoms": "Pēdējais rindā."},
        {"jaut": "Kas ir pirmais no labās?", "zim": bildes([_RINDA]),
         "opcijas": ["zvaigzne", "mašīna", "putns", "zivs"], "pareizi": 0,
         "padoms": "Sāc no labās malas."},
    ]),

    Ievadi("Kurā vietā? (no kreisās)", [
        {"jaut": "Kurā vietā ir sirds?", "zim": bildes([_RINDA]),
         "atb": ["4"], "padoms": "Skaiti: 1, 2, 3, 4."},
        {"jaut": "Kurā vietā ir zivs?", "zim": bildes([_RINDA]),
         "atb": ["2"], "padoms": "Tūlīt aiz mašīnas."},
        {"jaut": "Cik lietu ir rindā?", "zim": bildes([_RINDA]),
         "atb": ["5"], "padoms": "Tas ir «cik?», nevis «kurš?»."},
        {"jaut": "Kurā vietā ir sirds, ja skaita no labās?",
         "zim": bildes([_RINDA]), "atb": ["2"],
         "padoms": "Zvaigzne pirmā, sirds otrā."},
    ]),

    Pasaule("Rinda uz ēdnīcu",
            Ievadi("", [
                {"jaut": "Rindā stāv 7 bērni. Ance ir trešā. Cik bērnu ir "
                         "priekšā Ancei?", "atb": ["2"],
                 "padoms": "Pirmais un otrais."},
                {"jaut": "Cik bērnu ir aiz Ances?", "atb": ["4"],
                 "padoms": "Ceturtais līdz septītais."},
            ]),
            pavediens="skola",
            konteksts="Pusdienās klase stāv rindā pie ēdnīcas durvīm.",
            kapec="Vieta rindā pasaka, cik vēl jāgaida."),

    Kopsavilkums([
        "Atšķiru «cik?» un «kurš pēc kārtas?».",
        "Lietoju vārdus pirmais, otrais, trešais.",
        "Zinu, ka vieta atkarīga no tā, no kuras puses skaita.",
    ]),

    Majas([
        "Noliec 5 rotaļlietas rindā un pastāsti, kura ir trešā.",
        "Kurā vietā tu esi, ja ģimene nostājas pēc auguma?",
        "Kura diena pēc kārtas nedēļā ir piektdiena?",
    ]),
]
