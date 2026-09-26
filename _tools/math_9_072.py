# -*- coding: utf-8 -*-
"""9. klase, 72. stunda: «Kā pierādīt apgalvojumu par skaitļiem?»

Algebra pierāda to, ko piemēri tikai rāda: n^2 − n vienmēr ir pāra
skaitlis, jo n(n − 1) ir divu blakus skaitļu reizinājums. Sadalīšana
reizinātājos atklāj dalītāju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, restis)

TEMA = "Kā pierādīt apgalvojumu par skaitļiem?"

MERKIS = ("Pamatosim skaitļu dalāmību vai citu īpašību, izmantojot "
          "sadalīšanu reizinātājos.")

SATURS = [
    Sakums("Vai (n + 1)² − (n − 1)² vienmēr dalās ar 4?",
           zimejums=restis([["n", "1", "2", "3", "10"],
                            ["vērtība", "4", "8", "12", "40"]]),
           paraksts="Piemēri rāda - bet pierāda algebra.",
           fakti=["(n + 1)^2 − (n − 1)^2 = 4n.",
                  "4n dalās ar 4 jebkuram veselam n.",
                  "Piemēri neko nepierāda - pat 1000 piemēru."]),

    Doma("Pierādījums ar reizinātājiem",
         "Ja izteiksmi var uzrakstīt kā k · (vesels skaitlis), tā dalās ar k.",
         soli=[
             "Pieraksti apgalvojumu ar burtu n (vesels skaitlis).",
             "Vienkāršo vai sadali reizinātājos.",
             "Atrodi reizinātāju, kas parāda dalāmību.",
             "Uzraksti secinājumu vārdiem.",
         ],
         pieze="Divu pēc kārtas sekojošu veselu skaitļu reizinājums n(n + 1) "
               "vienmēr ir pāra skaitlis."),

    Slidnis("Pierādījums soli pa solim", [
        {"v": "Apgalvojums", "teksts": "n^2 − n ir pāra skaitlis jebkuram "
                                       "veselam n"},
        {"v": "1", "teksts": "n^2 − n = n(n − 1)"},
        {"v": "2", "teksts": "n − 1 un n ir blakus skaitļi - viens no tiem "
                             "pāra"},
        {"v": "3", "teksts": "Reizinājums ar pāra skaitli ir pāra skaitlis ∎"},
    ]),

    Paraugs("Kvadrātu starpība",
            uzd="Pierādi: 37^2 − 13^2 dalās ar 50.",
            soli=[
                ("37^2 − 13^2 = (37 − 13)(37 + 13)", "Formula."),
                ("= 24 · 50", "Reizinātājs 50."),
                ("dalās ar 50 ∎", "Nav jārēķina 1369 − 169."),
            ],
            atbilde="1200 = 24 · 50"),

    Varianti("Kurš reizinātājs pierāda?", [
        {"jaut": "Pierādīt, ka 5n + 10 dalās ar 5.",
         "opcijas": ["5(n + 2)", "5n + 10", "n + 2", "10(n + 1)"],
         "pareizi": 0, "padoms": "Iznes 5."},
        {"jaut": "Pierādīt, ka 43^2 − 7^2 dalās ar 36.",
         "opcijas": ["(43 − 7)(43 + 7) = 36 · 50", "43 · 7",
                     "43^2 = 1849", "(43 + 7)^2"],
         "pareizi": 0, "padoms": "Kvadrātu starpība."},
        {"jaut": "n^3 − n = (n − 1)n(n + 1). Ar ko tas noteikti dalās?",
         "opcijas": ["ar 6", "ar 5", "ar 4", "ar 9"],
         "pareizi": 0, "padoms": "Trīs pēc kārtas: viens dalās ar 2, viens "
                                 "ar 3."},
    ]),

    Ievadi("Aprēķini izdevīgi", [
        {"jaut": "57^2 − 43^2 = ?", "atb": ["1400", "1 400"],
         "padoms": "14 · 100."},
        {"jaut": "(n + 3)^2 − (n − 3)^2 = ?n", "atb": ["12"],
         "padoms": "6n − (−6n)."},
        {"jaut": "Ar n = 5: n^2 − n = ?", "atb": ["20"],
         "padoms": "5 · 4 - pāra."},
    ]),

    Pasaule("Kalendāra triks",
            Ievadi("", [
                {"jaut": "Kalendārā izvēlas 2 × 2 kvadrātu: n, n + 1, n + 7, "
                         "n + 8. Diagonāļu reizinājumu starpība "
                         "(n + 1)(n + 7) − n(n + 8) = ?",
                 "atb": ["7"], "padoms": "n^2 + 8n + 7 − n^2 − 8n."},
                {"jaut": "Pārbaudi ar 10, 11, 17, 18: 11 · 17 − 10 · 18 = ?",
                 "atb": ["7"], "padoms": "187 − 180."},
            ]),
            pavediens="skola",
            konteksts="Jebkurā kalendāra 2 × 2 kvadrātā «krustiskā» starpība "
                      "vienmēr ir 7 - to pierāda algebra.",
            kapec="Viens pierādījums der visiem mēnešiem uzreiz."),

    Kopsavilkums([
        "Pierakstu apgalvojumu ar burtiem.",
        "Sadalu reizinātājos un atrodu dalītāju.",
        "Atšķiru piemēru no pierādījuma.",
    ]),

    Majas([
        "Pierādi: trīs pēc kārtas sekojošu skaitļu summa dalās ar 3.",
        "Pierādi: 51^2 − 49^2 dalās ar 100.",
        "Pārbaudi kalendāra triku ar 3 × 3 kvadrātu stūriem.",
    ]),
]
