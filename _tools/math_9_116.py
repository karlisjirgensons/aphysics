# -*- coding: utf-8 -*-
"""9. klase, 116. stunda: «Kā pārbaudīt atrisinājumu?»

Pāri pārbauda ABOS sākotnējos vienādojumos - pārbaude tikai vienā (to, no
kura izteica) neko nepierāda, jo tas der vienmēr. Stundā skolēns ir
vērtētājs: meklē, kur citu risinājumā kļūda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, paris, restis)

TEMA = "Kā pārbaudīt atrisinājumu?"

MERKIS = ("Pārbaudīsim atrisinājumu, ievietojot skaitļu pāri abos "
          "vienādojumos.")

_T = "text"

SATURS = [
    Sakums("Pārbaude, kas neko nepārbauda",
           zimejums=restis([["sistēma", "2x + y = 8", "x − y = 1"],
                            ["pāris (2; 4)", "4 + 4 = 8 ✔", "2 − 4 = −2 ✘"]]),
           paraksts="Pirmajā der, otrajā - nē. Tas nav atrisinājums.",
           fakti=["Pārbauda abos vienādojumos.",
                  "Sākotnējos, nevis pārveidotos.",
                  "Pareizā atbilde: (3; 2)."]),

    Doma("Pilna pārbaude",
         "Ievieto x un y katrā sākotnējā vienādojumā un pārliecinies, ka abās "
         "pusēs ir vienādi skaitļi.",
         soli=[
             "Negatīvus skaitļus - iekavās.",
             "Kreisā puse un labā puse atsevišķi.",
             "Ja kaut viens nesakrīt - meklē kļūdu.",
             "Biežāk kļūda ir zīmēs vai reizinot vienādojumu.",
         ]),

    Paraugs("Kļūdas meklēšana",
            uzd="Skolēns atrisināja 3x + 2y = 7, x − 2y = 5 un ieguva "
                "(3; −1). Pārbaudi.",
            soli=[
                ("3 · 3 + 2 · (−1) = 7 ✔", "Pirmais."),
                ("3 − 2 · (−1) = 5 ✔", "Otrais."),
            ],
            atbilde="pāris ir pareizs"),

    Varianti("Atrisinājums vai nē?", [
        {"jaut": "(1; 2) sistēmai 3x + y = 5, x + 4y = 9",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "5 un 9."},
        {"jaut": "(2; 1) sistēmai x + y = 3, 2x − y = 4",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 1, "padoms": "2x − y = 3 ≠ 4."},
        {"jaut": "(−1; 3) sistēmai 2x + y = 1, y − x = 4",
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "1 un 4."},
    ]),

    Ievadi("Atrisini un pārbaudi", [
        {"jaut": "x + y = 9 un 2x − y = 3", "atb": paris(4, 5),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "3x = 12."},
        {"jaut": "3x − y = 10 un x + 2y = 1", "atb": paris(3, "−1"),
         "tastatura": _T, "vieta": "(x; y)", "padoms": "y = 3x − 10."},
        {"jaut": "Pārbaude: 3 · 3 − (−1) = ?", "atb": ["10"],
         "padoms": "9 + 1."},
    ]),

    Pasaule("Klasesbiedra kļūda",
            Varianti("", [
                {"jaut": "Draugs: x + y = 10 un x − y = 4 ⇒ (6; 4). Pārbaude: "
                         "6 + 4 = 10 ✔. Viņš saka: «pareizi». Ko tu atbildi?",
                 "opcijas": ["Nepārbaudīja otro: 6 − 4 = 2 ≠ 4; pareizi (7; 3)",
                             "Viss pareizi", "Jābūt (4; 6)",
                             "Sistēmai nav atrisinājuma"],
                 "pareizi": 0, "padoms": "Abos vienādojumos."},
            ]),
            pavediens="skola",
            konteksts="Pārbaude tikai vienā vienādojumā ir tipiska eksāmena "
                      "kļūda.",
            kapec="Pārbaude aizņem 30 sekundes un izglābj punktus."),

    Kopsavilkums([
        "Pārbaudu pāri abos sākotnējos vienādojumos.",
        "Negatīvus skaitļus ievietoju iekavās.",
        "Atrodu kļūdu, ja pārbaude neizdodas.",
    ]),

    Majas([
        "Atrisini un pārbaudi: 4x + y = 14, 2x − 3y = 0.",
        "Izdomā kļūdainu risinājumu un iedod draugam pārbaudīt.",
        "Pārbaudi 3 iepriekšējos mājasdarbus.",
    ]),
]
