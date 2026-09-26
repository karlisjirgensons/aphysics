# -*- coding: utf-8 -*-
"""9. klase, 73. stunda: «Kur radusies kļūda?»

Kļūdu katalogs: (a + b)^2 = a^2 + b^2, zīmes aiz mīnusa, saīsināti
saskaitāmie, aizmirsts vidējais loceklis, nepabeigta sadalīšana. Skolēns
atrod kļūdu, nosauc cēloni un izlabo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kur radusies kļūda?"

MERKIS = ("Atradīsim kļūdu dotā pārveidojumā un izskaidrosim tās cēloni.")

_T = "text"

SATURS = [
    Sakums("«Pierādījums», ka 2 = 1",
           zimejums=restis([["a = b"], ["a² − b² = ab − b²"],
                            ["(a − b)(a + b) = b(a − b)"], ["a + b = b"],
                            ["2b = b  ⇒  2 = 1 ?!"]]),
           paraksts="Kurā rindā ir kļūda?",
           fakti=["Rindā 4 abas puses dalītas ar a − b.",
                  "Bet a = b, tātad a − b = 0.",
                  "Ar nulli dalīt nedrīkst!"]),

    Doma("Piecas biežākās kļūdas",
         "Lielākā daļa kļūdu ir viena no piecām - zinot tās, tās var ātri "
         "atrast.",
         soli=[
             "(a + b)^2 = a^2 + b^2 - aizmirsts 2ab.",
             "−(x − 3) = −x − 3 - zīme maināta tikai pirmajam.",
             "{x + 5|5} = x - saīsināts saskaitāmais.",
             "(3x)^2 = 3x^2 - koeficients nav kāpināts.",
             "Dalīts ar izteiksmi, kas var būt 0.",
         ]),

    Slidnis("Kļūdu katalogs", [
        {"v": "1", "teksts": "(x + 5)^2 = x^2 + 25 ✘ → x^2 + 10x + 25"},
        {"v": "2", "teksts": "4 − (x − 1) = 4 − x − 1 ✘ → 4 − x + 1 = 5 − x"},
        {"v": "3", "teksts": "{2x + 6|2} = x + 6 ✘ → x + 3"},
        {"v": "4", "teksts": "(2a)^2 = 2a^2 ✘ → 4a^2"},
        {"v": "5", "teksts": "x^2 = 3x ⇒ x = 3 ✘ → pazaudēta sakne x = 0"},
    ]),

    Varianti("Atrodi kļūdu", [
        {"jaut": "(a − 3)^2 = a^2 − 6a − 9",
         "opcijas": ["Pēdējais loceklis +9", "Vidējais −3a", "Pareizi",
                     "Jābūt a^2 − 9"],
         "pareizi": 0, "padoms": "(−3)^2 = 9."},
        {"jaut": "x^2 − 16 = (x − 4)^2",
         "opcijas": ["Jābūt (x − 4)(x + 4)", "Pareizi", "Jābūt (x − 8)^2",
                     "Jābūt (x + 4)^2"],
         "pareizi": 0, "padoms": "Kvadrātu starpība."},
        {"jaut": "2x^2 − 8 = 2(x^2 − 4) - sadalīts pilnīgi?",
         "opcijas": ["Nē: 2(x − 2)(x + 2)", "Jā", "Jābūt 2(x − 4)",
                     "Jābūt (2x − 8)"],
         "pareizi": 0, "padoms": "x^2 − 4 vēl sadalās."},
        {"jaut": "(x + 2)(x − 2) − (x^2 + 4) = −8. Vai pareizi?",
         "opcijas": ["Pareizi", "Jābūt 0", "Jābūt 2x^2", "Jābūt −4"],
         "pareizi": 0, "padoms": "x^2 − 4 − x^2 − 4."},
    ]),

    Ievadi("Izlabo", [
        {"jaut": "(3x)^2 = ?", "atb": ["9x^2"], "tastatura": _T,
         "padoms": "3^2 · x^2."},
        {"jaut": "5 − (2 − x) = ?", "atb": ["3 + x", "x + 3"],
         "tastatura": _T, "padoms": "5 − 2 + x."},
        {"jaut": "(y − 1)^2 = ?", "atb": ["y^2 − 2y + 1"], "tastatura": _T,
         "padoms": "Trīs locekļi."},
        {"jaut": "{3a + 9|3} = ?", "atb": ["a + 3", "3 + a"],
         "tastatura": _T, "padoms": "3(a + 3) : 3."},
    ]),

    Pasaule("Sociālo tīklu «ģēnijs»",
            Varianti("", [
                {"jaut": "Ierakstā: «(10 + 1)^2 = 10^2 + 1^2 = 101, viegli!». "
                         "Pareizi ir...",
                 "opcijas": ["121", "101", "111", "100"],
                 "pareizi": 0, "padoms": "100 + 20 + 1."},
                {"jaut": "Tas pats autors: «99 · 101 = 100^2 − 1 = 9999». "
                         "Vai tas ir pareizi?",
                 "opcijas": ["Jā - kvadrātu starpība", "Nē, 9899", "Nē, 10 001",
                             "Nē, 9900"],
                 "pareizi": 0, "padoms": "(100 − 1)(100 + 1)."},
            ]),
            pavediens="dati",
            konteksts="Internetā klīst «matemātikas triki» - daži pareizi, "
                      "daži ne.",
            kapec="Pārbaudīt prot tas, kurš zina formulas."),

    Kopsavilkums([
        "Pazīstu piecas biežākās kļūdas.",
        "Atrodu kļūdu pārveidojumā un nosaucu cēloni.",
        "Izlaboju pārveidojumu.",
    ]),

    Majas([
        "Pārbaudi savus pēdējos mājasdarbus: vai kāda no piecām kļūdām?",
        "Uzraksti «pierādījumu» ar apslēptu kļūdu klasesbiedram.",
        "Atrisini: x^2 = 5x, nepazaudējot sakni.",
    ]),
]
