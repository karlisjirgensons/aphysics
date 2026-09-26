# -*- coding: utf-8 -*-
"""8. klase, 31. stunda: «Kā vienkāršot garu izteiksmi?»

Garas izteiksmes ar skaitļiem, vairākiem burtiem un negatīviem
kāpinātājiem. Jauns ir tikai viens solis - pārbaude, ievietojot skaitli:
ja sākumā un beigās sanāk tas pats, pārveidojums visticamāk ir pareizs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kā vienkāršot garu izteiksmi?"

MERKIS = ("Vienkāršosim izteiksmes ar vairākām pakāpēm un pārbaudīsim "
          "rezultātu.")

SATURS = [
    Sakums("Pārbaudi ar x = 2",
           zimejums=restis([["x⁵ · x⁻² : x", "x²"],
                            ["32 · 1/4 : 2 = 4", "4"]]),
           paraksts="Sākumā un beigās - tas pats skaitlis.",
           fakti=["Pārbaudei der jebkurš ērts skaitlis, izņemot 0 un 1.",
                  "Ja skaitļi atšķiras - kaut kur ir kļūda.",
                  "Pārbaude aizņem pusminūti."]),

    Doma("Plāns garai izteiksmei",
         "Izteiksmi vienkāršo pa slāņiem: iekavas, tad skaitļi, tad katrs burts "
         "atsevišķi. Beigās - pārbaude.",
         soli=[
             "Kāpini visas iekavas.",
             "Sareizini un izdali skaitliskos koeficientus.",
             "Katram burtam saskaiti un atņem kāpinātājus.",
             "Pieraksti bez negatīviem kāpinātājiem.",
             "Pārbaudi, ievietojot skaitli.",
         ]),

    Slidnis("Pa slāņiem", [
        {"v": "{(2a^−1b^2)^3 · a^5|4ab^4}", "teksts": "Sākums"},
        {"v": "{8a^−3b^6 · a^5|4ab^4}", "teksts": "Iekavas: 2^3, (−1)·3, 2·3"},
        {"v": "{8a^2b^6|4ab^4}", "teksts": "a: −3 + 5 = 2"},
        {"v": "2ab^2", "teksts": "8 : 4; a: 2 − 1; b: 6 − 4"},
        {"v": "a = 2, b = 1: 4 = 4",
         "teksts": "Pārbaude: sākumā (2 · 0,5 · 1)^3 · 32 : 8 = 4, beigās "
                   "2 · 2 · 1 = 4"},
    ]),

    Ievadi("Vienkāršo", [
        {"jaut": "x^5 · x^−2 : x", "atb": ["x^2"], "padoms": "5 − 2 − 1.",
         "tastatura": "text"},
        {"jaut": "(3a^2)^2 · a^−3", "atb": ["9a"], "padoms": "9a^4 · a^−3.",
         "tastatura": "text"},
        {"jaut": "{12x^3y^−2|3xy}", "atb": ["{4x^2|y^3}", "4x^2/y^3",
                                            "4x^2y^-3"],
         "padoms": "y: −2 − 1 = −3.", "tastatura": "text"},
        {"jaut": "{(2^3)^2 · 2^−4|2^−1} - aprēķini", "atb": ["8"],
         "padoms": "2^{6 − 4 + 1}."},
        {"jaut": "(a^−2b)^−2", "atb": ["{a^4|b^2}", "a^4/b^2", "a^4b^-2"],
         "padoms": "a^4b^−2.", "tastatura": "text"},
        {"jaut": "{5^−3 · 25^2|5^0} - aprēķini", "atb": ["5"],
         "padoms": "5^{−3 + 4}."},
    ], pamats=4),

    Varianti("Pārbaudes rezultāts", [
        {"jaut": "Skolēns ieguva (a^2)^3 · a = a^6. Pārbaude ar a = 2: "
                 "sākumā 128, beigās 64. Ko tas nozīmē?",
         "opcijas": ["Ir kļūda - jābūt a^7", "Viss pareizi",
                     "Pārbaude neder", "Jāņem a = 1"],
         "pareizi": 0, "padoms": "2^7 = 128."},
        {"jaut": "Kāpēc pārbaudē neņem a = 1?",
         "opcijas": ["1 jebkurā pakāpē ir 1 - kļūdu neredz",
                     "Tā ir aizliegts", "Tas ir par lielu",
                     "Var ņemt"],
         "pareizi": 0, "padoms": "1^6 = 1^7."},
    ]),

    Pasaule("Ekrāna pikseļi",
            Ievadi("", [
                {"jaut": "Ekrāns 2^{11} × 2^{10} pikseļu. Cik pikseļu? "
                         "Pieraksti kā 2^?",
                 "atb": ["2^21", "2^{21}"], "padoms": "11 + 10.",
                 "tastatura": "text"},
                {"jaut": "Katram pikselim 2^2 baiti. Cik baitu vienam kadram? "
                         "2^?",
                 "atb": ["2^23", "2^{23}"], "padoms": "21 + 2.",
                 "tastatura": "text"},
                {"jaut": "1 MB = 2^{20} baitu. Cik MB ir kadrs?",
                 "atb": ["8"], "padoms": "2^{23 − 20}."},
            ]),
            pavediens="dati",
            konteksts="Datora atmiņu rēķina divnieka pakāpēs, tāpēc garu "
                      "reizinājumu var vienkāršot vienā rindā.",
            kapec="60 kadri sekundē - 480 MB katru sekundi."),

    Kopsavilkums([
        "Vienkāršoju garu izteiksmi pa slāņiem.",
        "Apstrādāju katru burtu atsevišķi.",
        "Pārbaudu rezultātu, ievietojot skaitli.",
    ]),

    Majas([
        "Vienkāršo un pārbaudi: {(x^2y)^3|x^4y^5}, (2a^−1)^−2 · a^3.",
        "Uzraksti vienu nepareizu pārveidojumu un atmasko to ar pārbaudi.",
        "Aprēķini, cik MB aizņem 10 sekunžu video ar 60 kadriem sekundē.",
    ]),
]
