# -*- coding: utf-8 -*-
"""8. klase, 22. stunda: «Kā lietot īpašības kopā?»

Bloka noslēgums: garas izteiksmes, kurās vajadzīgas visas četras īpašības.
Katram solim - viena īpašība un tās nosaukums, lai skolēns redz, ka garš
uzdevums ir tikai vairāki īsi pēc kārtas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kā lietot īpašības kopā?"

MERKIS = ("Vienkāršosim izteiksmes, lietojot vairākas pakāpju īpašības pēc "
          "kārtas.")

SATURS = [
    Sakums("Četras īpašības vienā lapā",
           zimejums=restis([["2³ · 2²", "2⁵"],
                            ["2⁵ : 2²", "2³"],
                            ["(2³)²", "2⁶"],
                            ["(2 · 3)²", "2² · 3²"]]),
           paraksts="Reizina - saskaita, dala - atņem, kāpina - reizina, "
                    "reizinājumu kāpina pa vienam.",
           fakti=["Vispirms iekavas ar kāpinātāju.",
                  "Tad reizināšana un dalīšana no kreisās.",
                  "Beigās - skaitliskais koeficients."]),

    Doma("Secība garā izteiksmē",
         "Izteiksmi vienkāršo pa soļiem, katrā lietojot vienu īpašību. "
         "Skaitļus un burtus apstrādā atsevišķi.",
         soli=[
             "Kāpini iekavas: (ab)^n un (a^m)^n.",
             "Sareizini skaitļus savā starpā.",
             "Katram burtam saskaiti vai atņem kāpinātājus.",
             "Pieraksti: skaitlis, tad burti alfabēta secībā.",
         ]),

    Slidnis("Vienkāršo pa soļiem", [
        {"v": "{(2a^3)^2 · a^4|4a^5}", "teksts": "Sākums"},
        {"v": "{4a^6 · a^4|4a^5}", "teksts": "(ab)^n un (a^m)^n"},
        {"v": "{4a^10|4a^5}", "teksts": "Reizināšana: 6 + 4"},
        {"v": "a^5", "teksts": "4 : 4 = 1; 10 − 5 = 5"},
    ]),

    Ievadi("Vienkāršo", [
        {"jaut": "x^3 · (x^2)^4", "atb": ["x^11", "x^{11}"],
         "padoms": "x^3 · x^8.", "tastatura": "text"},
        {"jaut": "{(a^2)^5|a^3 · a^4}", "atb": ["a^3"],
         "padoms": "{a^{10}|a^7}.", "tastatura": "text"},
        {"jaut": "(3x^2)^2 · 2x", "atb": ["18x^5"],
         "padoms": "9x^4 · 2x.", "tastatura": "text"},
        {"jaut": "{2^5 · 2^3|(2^2)^3} - aprēķini", "atb": ["4"],
         "padoms": "{2^8|2^6}."},
        {"jaut": "{6x^7y^3|2x^4y}", "atb": ["3x^3y^2"],
         "padoms": "6 : 2; 7 − 4; 3 − 1.", "tastatura": "text"},
        {"jaut": "{3^10|9^4} - aprēķini", "atb": ["9"],
         "padoms": "9^4 = 3^8."},
    ], pamats=4),

    Varianti("Kurš solis ir kļūdains?", [
        {"jaut": "(2x^3)^2 = 2x^6",
         "opcijas": ["Nekāpināja 2", "Nepareizi kāpinātāji",
                     "Pareizi", "Jābūt 4x^5"],
         "pareizi": 0, "padoms": "(2)^2 = 4."},
        {"jaut": "{a^6|a^2} = a^3",
         "opcijas": ["Kāpinātājus dalīja, nevis atņēma", "Pareizi",
                     "Jābūt a^8", "Jābūt a^{12}"],
         "pareizi": 0, "padoms": "6 − 2 = 4."},
    ]),

    Pasaule("Mikroshēmu likums",
            Ievadi("", [
                {"jaut": "Tranzistoru skaits mikroshēmā divkāršojas ik 2 "
                         "gadus. Cik reižu tas pieaug 10 gados? (2^5)",
                 "atb": ["32"], "padoms": "5 divkāršošanās."},
                {"jaut": "Un 20 gados? Pieraksti kā (2^5)^2 un aprēķini.",
                 "atb": ["1024"], "padoms": "2^{10}."},
                {"jaut": "Mikroshēmā 2^{30} tranzistoru, nākamajā - 2^{33}. "
                         "Cik reižu vairāk?",
                 "atb": ["8"], "padoms": "2^3."},
            ]),
            pavediens="tehnika",
            konteksts="Mūra likums apraksta, kā datoru jauda 50 gadus pieauga "
                      "pakāpēs - tāpēc telefons ir jaudīgāks par 1990. gadu "
                      "superdatoru.",
            kapec="Pakāpju īpašības ļauj salīdzināt bez milzīgiem skaitļiem."),

    Kopsavilkums([
        "Vienkāršoju izteiksmi, lietojot īpašības pa vienai.",
        "Skaitļus un burtus apstrādāju atsevišķi.",
        "Atrodu kļūdaino soli citā risinājumā.",
    ]),

    Majas([
        "Vienkāršo: (a^2b)^3 · ab^2, {(x^3)^3|x^5}, {8^2|2^4}.",
        "Katram solim pieraksti, kuru īpašību lietoji.",
        "Izveido savu izteiksmi, kuras rezultāts ir x^{10}.",
    ]),
]
