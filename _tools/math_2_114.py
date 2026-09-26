# -*- coding: utf-8 -*-
"""2. klase, 114. stunda: «Vai diviem taisnstūriem var būt viens perimetrs?»

Pētījums: taisnstūri ar perimetru 12 rūtiņas var būt 1 un 5, 2 un 4, 3 un
3 - perimetrs viens, bet laukums 5, 8 un 9. Un otrādi - viens laukums,
dažāds perimetrs. Tā skolēns redz, ka perimetrs un laukums ir dažādas
lietas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, rutinas,
                         restis)

TEMA = "Vai diviem taisnstūriem var būt viens perimetrs?"

MERKIS = ("Šodien zīmēsim taisnstūrus ar dotu perimetru vai laukumu un "
          "salīdzināsim tos.")

_TABULA = restis([["garums", "platums", "perimetrs", "laukums"],
                  [5, 1, 12, 5], [4, 2, 12, 8], [3, 3, 12, 9]])

SATURS = [
    Sakums("Kurš dārzs lielāks, ja abiem ir vienāds žogs?",
           zimejums=_TABULA,
           paraksts="Perimetrs visiem 12, laukums - dažāds!",
           fakti=["Vienāds perimetrs nenozīmē vienādu laukumu.",
                  "Kvadrāts ar to pašu perimetru ir vislielākais.",
                  "Šauram un garam taisnstūrim laukums mazs."]),

    Doma("Perimetrs un laukums - dažādi",
         "Mainot formu, perimetrs var palikt, bet laukums mainās.",
         soli=[
             "Izvēlies perimetru, piemēram, 12 rūtiņas.",
             "Garums + platums = 6 (puse perimetra).",
             "Izmēģini: 5 un 1, 4 un 2, 3 un 3.",
             "Katram saskaiti rūtiņas iekšā.",
         ]),

    Slidnis("Perimetrs 12 rūtiņas", [
        {"v": "5 un 1", "teksts": "Laukums 5.", "zim": rutinas(5, 5, 5, 1)},
        {"v": "4 un 2", "teksts": "Laukums 8.", "zim": rutinas(5, 5, 4, 2)},
        {"v": "3 un 3", "teksts": "Laukums 9 - kvadrāts.",
         "zim": rutinas(5, 5, 3, 3)},
    ]),

    Ievadi("Pētī", [
        {"jaut": "Taisnstūris 6 un 2 rūtiņas. Perimetrs?", "atb": ["16"],
         "padoms": "8 + 8."},
        {"jaut": "Taisnstūris 6 un 2. Laukums?", "atb": ["12"],
         "padoms": "6 + 6."},
        {"jaut": "Taisnstūris 4 un 3. Laukums?", "atb": ["12"],
         "padoms": "4 + 4 + 4."},
        {"jaut": "Taisnstūris 4 un 3. Perimetrs?", "atb": ["14"],
         "padoms": "7 + 7."},
    ]),

    Varianti("Secini", [
        {"jaut": "Taisnstūriem 6 un 2, 4 un 3 laukums 12. Vai perimetri "
                 "vienādi?", "opcijas": ["Nē: 16 un 14", "Jā"],
         "jaukt": False, "pareizi": 0, "padoms": "Aprēķināji iepriekš."},
        {"jaut": "Kuram taisnstūrim ar perimetru 16 ir lielākais laukums?",
         "opcijas": ["4 un 4", "7 un 1", "6 un 2"], "pareizi": 0,
         "padoms": "Kvadrāts."},
    ]),

    Petijums("Taisnstūri ar perimetru 16", [
        "Rūtiņu lapā uzzīmē visus taisnstūrus ar perimetru 16 rūtiņas.",
        "Katram saskaiti laukumu.",
        "Ieraksti tabulā.",
        "Kuram laukums lielākais?",
    ], vajag="rūtiņu lapa", secinajums="7 un 1, 6 un 2, 5 un 3, 4 un 4 - "
                                        "kvadrātam laukums lielākais: 16."),

    Pasaule("Kuru dobi izvēlēties?",
            Varianti("", [
                {"jaut": "Ir 20 m apmales. Kura dobe dos vairāk vietas "
                         "puķēm?", "opcijas": ["5 m un 5 m", "9 m un 1 m",
                                               "8 m un 2 m"],
                 "pareizi": 0, "padoms": "Kvadrāts - vislielākais laukums."},
            ]),
            pavediens="daba",
            konteksts="Apmales daudzums ir noteikts, bet formu var izvēlēties.",
            kapec="Gudra forma dod vairāk vietas par to pašu naudu."),

    Kopsavilkums([
        "Zīmēju taisnstūrus ar dotu perimetru.",
        "Salīdzinu to laukumus.",
        "Zinu, ka perimetrs un laukums ir dažādi lielumi.",
    ]),

    Majas([
        "Ar 12 sērkociņiem saliec dažādus taisnstūrus.",
        "Kuram laukums lielākais?",
        "Uzzīmē tos rūtiņu lapā.",
    ]),
]
