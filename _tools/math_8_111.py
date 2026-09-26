# -*- coding: utf-8 -*-
"""8. klase, 111. stunda: «Kā kāpina monomu?»

(ab)^n = a^n b^n un (a^m)^n = a^{mn}: kāpina katru reizinātāju, arī
koeficientu un zīmi. Pāra kāpinātājs mīnusu «noēd», nepāra - saglabā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, kermenis)

TEMA = "Kā kāpina monomu?"

MERKIS = "Kāpināsim monomu un pierakstīsim rezultātu normālformā."

_T = "text"

SATURS = [
    Sakums("Kuba šķautne 3x. Cik liels ir tilpums?",
           zimejums=kermenis("kubs"),
           paraksts="(3x)^3 = 3^3 · x^3 = 27x^3",
           fakti=["Kāpina katru reizinātāju: (ab)^n = a^n b^n.",
                  "Pakāpi kāpinot, kāpinātājus reizina: (a^m)^n = a^{mn}.",
                  "Kāpina arī koeficientu un zīmi."]),

    Doma("Monoma kāpināšana",
         "Katrs reizinātājs iekavās tiek kāpināts.",
         soli=[
             "Kāpini koeficientu: (−2)^3 = −8.",
             "Katra burta kāpinātāju reizini ar n: (x^3)^2 = x^6.",
             "Pāra kāpinātājs dod plusu: (−a)^4 = a^4.",
             "Pieraksti normālformā.",
         ],
         pieze="Bieža kļūda: (2x)^2 = 2x^2 - nē, pareizi 4x^2."),

    Paraugs("Kāpini",
            uzd="Aprēķini (−2ab^2)^3 un (5x^2y)^2.",
            soli=[
                ("(−2)^3 = −8; a^3; (b^2)^3 = b^6", "Pa daļām."),
                ("−8a^3b^6", "Pirmais."),
                ("5^2 = 25; (x^2)^2 = x^4; y^2", "Otrais."),
                ("25x^4y^2", "Normālforma."),
            ],
            atbilde="−8a^3b^6 un 25x^4y^2"),

    Ievadi("Kāpini (normālformā)", [
        {"jaut": "(3a)^2", "atb": ["9a^2"], "tastatura": _T,
         "padoms": "3^2 · a^2."},
        {"jaut": "(x^2)^3", "atb": ["x^6"], "tastatura": _T,
         "padoms": "2 · 3."},
        {"jaut": "(−a)^4", "atb": ["a^4"], "tastatura": _T,
         "padoms": "Pāra kāpinātājs."},
        {"jaut": "(−2x^3)^3", "atb": ["−8x^9", "-8x^9"], "tastatura": _T,
         "padoms": "(−2)^3 = −8; 3 · 3 = 9."},
        {"jaut": "(2x^3y)^2: pakāpe?", "atb": ["8"],
         "padoms": "4x^6y^2."},
        {"jaut": "(5a^2)^2: koeficients?", "atb": ["25"], "padoms": "5^2."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "(−3x)^2 = ?",
         "opcijas": ["9x^2", "−9x^2", "6x^2", "−6x^2"],
         "pareizi": 0, "padoms": "(−3)^2 = 9."},
        {"jaut": "(a^3)^2 = ?",
         "opcijas": ["a^6", "a^5", "a^9", "2a^3"],
         "pareizi": 0, "padoms": "Reizina: 3 · 2."},
        {"jaut": "(2a)^3 = ?",
         "opcijas": ["8a^3", "6a^3", "2a^3", "8a"],
         "pareizi": 0, "padoms": "2^3 = 8."},
    ]),

    Pasaule("Kuba izmēri",
            Ievadi("", [
                {"jaut": "Kuba šķautne 3x cm. Tilpums = ?x^3 cm³",
                 "atb": ["27"], "padoms": "(3x)^3."},
                {"jaut": "Vienas skaldnes laukums = ?x^2 cm²", "atb": ["9"],
                 "padoms": "(3x)^2."},
                {"jaut": "Visa virsma = ?x^2 cm²", "atb": ["54"],
                 "padoms": "6 · 9x^2."},
            ]),
            pavediens="maja",
            konteksts="Kastes un kubus ražo dažādos izmēros; formula ar x der "
                      "visiem.",
            kapec="Divkāršojot šķautni, tilpums pieaug (2x)^3 = 8x^3 - "
                  "astoņas reizes."),

    Kopsavilkums([
        "Kāpinu monomu, kāpinot katru reizinātāju.",
        "Lietoju (a^m)^n = a^{mn}.",
        "Ievēroju zīmi pāra un nepāra kāpinātājam.",
    ]),

    Majas([
        "Kāpini: (4x^2)^2; (−a^2b)^3; (0,1y)^2.",
        "Paskaidro, kāpēc (2x)^2 nav 2x^2.",
        "Aprēķini, cik reizes palielinās kuba tilpums, ja šķautni "
        "trīskāršo.",
    ]),
]
