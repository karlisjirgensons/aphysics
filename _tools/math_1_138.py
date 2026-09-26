# -*- coding: utf-8 -*-
"""1. klase, 138. stunda: «Cik ilgi?»

Notikuma ilgums - no sākuma līdz beigām: 8:00 līdz 11:00 - 3 stundas;
3:15 līdz 3:45 - 30 minūtes. 1 stunda = 60 minūtes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, pulkstenis)

TEMA = "Cik ilgi?"

MERKIS = ("Šodien aprēķināsim, cik ilgi notikums ilgst - stundās un "
          "minūtēs.")

SATURS = [
    Sakums("Skola no 8 līdz 12 - cik stundas?",
           zimejums=pulkstenis(12),
           paraksts="No 8 līdz 12 - 4 stundas.",
           fakti=["Ilgums = beigas − sākums.",
                  "1 stunda = 60 minūtes.",
                  "Pusstunda = 30 minūtes."]),

    Doma("Ilgums",
         "Skaiti no sākuma līdz beigām - stundas vai minūtes.",
         soli=[
             "Nolasi sākumu un beigas.",
             "Pilnām stundām - atņem stundas.",
             "Minūtēm - skaiti pa 5.",
         ]),

    Ievadi("Cik ilgi?", [
        {"jaut": "No 8:00 līdz 11:00. Cik stundu?", "atb": ["3"],
         "padoms": "11 − 8."},
        {"jaut": "No 3:15 līdz 3:45. Cik minūšu?", "atb": ["30"],
         "padoms": "45 − 15."},
        {"jaut": "No 2:00 līdz 2:30. Cik minūšu?", "atb": ["30"],
         "padoms": "Pusstunda."},
        {"jaut": "Cik minūšu ir 1 stundā?", "atb": ["60"],
         "padoms": "Viss aplis."},
    ]),

    Varianti("Kas ilgāk?", [
        {"jaut": "Kas ilgst ilgāk: 1 stunda vai 45 minūtes?",
         "opcijas": ["1 stunda", "45 minūtes"], "jaukt": False,
         "pareizi": 0, "padoms": "60 > 45."},
        {"jaut": "Kas ilgst apmēram 1 stundu?",
         "opcijas": ["futbola treniņš", "roku mazgāšana", "nakts miegs"],
         "pareizi": 0, "padoms": "Ne pārāk īss, ne visa nakts."},
    ]),

    Pasaule("Futbola spēle",
            Ievadi("", [
                {"jaut": "Bērnu spēle ilgst 2 puslaikus pa 20 minūtēm. Cik "
                         "minūšu?", "atb": ["40"], "padoms": "20 + 20."},
                {"jaut": "Spēle sākās 5:00. Starpbrīdis 10 min. Kad beigsies? "
                         "(kā 5:50)", "atb": ["5:50", "5,50"],
                 "tastatura": "text", "padoms": "40 + 10 = 50 min."},
            ]),
            pavediens="sports",
            konteksts="Svētdien ir futbola spēle.",
            kapec="Zinot ilgumu, vecāki zina, kad atbraukt."),

    Kopsavilkums([
        "Aprēķinu ilgumu stundās.",
        "Aprēķinu ilgumu minūtēs.",
        "Zinu, ka 1 h = 60 min.",
    ]),

    Majas([
        "Cik ilgi tu guli? (no ... līdz ...)",
        "Cik ilgi ilgst tava mīļākā multfilma?",
        "Cik minūšu ej uz skolu?",
    ]),
]
