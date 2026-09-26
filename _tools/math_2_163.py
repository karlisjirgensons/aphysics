# -*- coding: utf-8 -*-
"""2. klase, 163. stunda: «Cik kopā abiem?»

Uzdevumi, kuros viens lielums ir vairākas reizes lielāks par otru un
jāatrod abu kopsumma: vispirms otrs lielums (reizināšana), tad summa. Divu
soļu uzdevums ar sloksņu zīmējumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, sloksnes)

TEMA = "Cik kopā abiem?"

MERKIS = ("Šodien risināsim uzdevumus, kuros viens lielums ir vairākas "
          "reizes lielāks, un atradīsim kopsummu.")

SATURS = [
    Sakums("Māsai 4 uzlīmes, brālim 3 reizes vairāk. Cik abiem?",
           zimejums=sloksnes([("māsa", 4, "4"), ("brālis", 12, "?")],
                             starpiba=False),
           paraksts="Brālim: 3 · 4 = 12. Kopā: 4 + 12 = 16.",
           fakti=["1. solis: otrs lielums.",
                  "2. solis: kopā.",
                  "Zīmējumā kopā ir 4 vienādi gabali."]),

    Doma("Divi soļi",
         "Vispirms atrod lielāko, tad saskaita abus.",
         soli=[
             "Uzzīmē mazāko sloksni.",
             "Lielākā - tik reižu garāka.",
             "1) Aprēķini lielāko: 3 · 4 = 12.",
             "2) Saskaiti: 4 + 12 = 16.",
         ]),

    Paraugs("Suns un kaķis",
            uzd="Kaķis sver 4 kg, suns 5 reizes vairāk. Cik abi kopā?",
            soli=[("1) 5 · 4 = 20 kg", "Suns."),
                  ("2) 4 + 20 = 24 kg", "Kopā.")],
            atbilde="24 kg"),

    Ievadi("Cik kopā?", [
        {"jaut": "Tomam 5 €, Annai 3 reizes vairāk. Cik abiem?",
         "atb": ["20"], "mers": "€", "padoms": "15 + 5."},
        {"jaut": "Mazā kaste 6 kg, lielā 4 reizes smagāka. Cik abas?",
         "atb": ["30"], "mers": "kg", "padoms": "24 + 6."},
        {"jaut": "Zēnam 7 gadi, tētim 5 reizes vairāk. Cik abiem kopā?",
         "atb": ["42"], "padoms": "35 + 7."},
        {"jaut": "Pirmajā dienā 8 lapas, otrajā 2 reizes vairāk. Cik "
                 "kopā?", "atb": ["24"], "padoms": "16 + 8."},
        {"jaut": "Baltas rozes 9, sarkanas 3 reizes vairāk. Cik kopā?",
         "atb": ["36"], "padoms": "27 + 9."},
        {"jaut": "Mazais trauks 10 l, lielais 4 reizes vairāk. Cik kopā?",
         "atb": ["50"], "mers": "l", "padoms": "40 + 10."},
    ], pamats=4),

    Varianti("Kas jāaprēķina vispirms?", [
        {"jaut": "Mārtiņam 6 konfektes, Līvai 2 reizes vairāk. Cik abiem?",
         "opcijas": ["2 · 6 - cik Līvai", "6 + 2", "6 − 2"], "pareizi": 0,
         "padoms": "Vispirms Līva."},
        {"jaut": "Kura atbilde nav iespējama «abiem kopā», ja vienam 5 un "
                 "otram 4 reizes vairāk?",
         "opcijas": ["20", "25"], "jaukt": False, "pareizi": 0,
         "padoms": "20 ir tikai otram, kopā 25."},
    ]),

    Pasaule("Ogu lasīšana",
            Ievadi("", [
                {"jaut": "Bērns salasīja 3 l melleņu, mamma 4 reizes vairāk. "
                         "Cik abi?", "atb": ["15"], "mers": "l",
                 "padoms": "12 + 3."},
            ]),
            pavediens="daba",
            konteksts="Augustā mežā lasa mellenes.",
            kapec="Divi soļi - un atbilde gatava."),

    Kopsavilkums([
        "Atrodu lielāko lielumu ar reizināšanu.",
        "Atrodu abu kopsummu.",
        "Zīmēju sloksnes, lai redzētu soļus.",
    ]),

    Majas([
        "Izdomā uzdevumu par sevi un pieaugušo: «... reizes vairāk».",
        "Atrisini to divos soļos.",
        "Uzzīmē sloksnes.",
    ]),
]
