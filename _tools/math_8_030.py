# -*- coding: utf-8 -*-
"""8. klase, 30. stunda: «Kāda zīme ir pakāpei?»

Zīmi nosaka pirms aprēķina: negatīva bāze pāra kāpinātājā dod plusu,
nepāra - mīnusu. Tas der arī negatīviem kāpinātājiem, jo {1|x} zīme ir tā
pati, kas x. Stunda trenē noteikt zīmi uzreiz, pat neaprēķinot vērtību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kāda zīme ir pakāpei?"

MERKIS = ("Noteiksim pakāpes zīmi, ja bāze ir negatīvs skaitlis.")

SATURS = [
    Sakums("Mīnusu pāri",
           zimejums=restis([["(−1)¹", "(−1)²", "(−1)³", "(−1)⁴", "(−1)⁵"],
                            ["−1", "1", "−1", "1", "−1"]]),
           paraksts="Katrs mīnusu pāris dod plusu.",
           fakti=["Pāra skaits mīnusu - pluss.",
                  "Nepāra skaits - viens mīnuss paliek pāri.",
                  "Zīmi var noteikt, neaprēķinot vērtību."]),

    Doma("Pakāpes zīmes likums",
         "Ja a > 0, tad a^n > 0 jebkuram veselam n. Ja a < 0, zīmi nosaka "
         "kāpinātāja paritāte.",
         soli=[
             "Negatīva bāze, pāra kāpinātājs - pozitīva vērtība.",
             "Negatīva bāze, nepāra kāpinātājs - negatīva vērtība.",
             "Negatīvs kāpinātājs zīmi nemaina: (−2)^−3 = −{1|8}.",
             "Bez iekavām −a^n: vispirms a^n, tad mīnuss.",
         ]),

    Slidnis("Iekavas maina visu", [
        {"v": "(−2)^4 = 16", "teksts": "Kāpina −2: četri mīnusi"},
        {"v": "−2^4 = −16", "teksts": "Kāpina 2, mīnuss paliek priekšā"},
        {"v": "(−2)^3 = −8", "teksts": "Trīs mīnusi"},
        {"v": "−(−2)^3 = 8", "teksts": "Pretējais skaitlim −8"},
    ]),

    Varianti("Pozitīva vai negatīva?", [
        {"jaut": "(−7)^{10}",
         "opcijas": ["Pozitīva", "Negatīva", "Nulle", "Nevar noteikt"],
         "pareizi": 0, "padoms": "Pāra kāpinātājs.", "jaukt": False},
        {"jaut": "(−0,3)^5",
         "opcijas": ["Pozitīva", "Negatīva", "Nulle", "Nevar noteikt"],
         "pareizi": 1, "padoms": "Nepāra.", "jaukt": False},
        {"jaut": "−5^2",
         "opcijas": ["Pozitīva", "Negatīva", "Nulle", "Nevar noteikt"],
         "pareizi": 1, "padoms": "Kāpina tikai 5.", "jaukt": False},
        {"jaut": "(−3)^−2",
         "opcijas": ["Pozitīva", "Negatīva", "Nulle", "Nevar noteikt"],
         "pareizi": 0, "padoms": "{1|9}.", "jaukt": False},
        {"jaut": "(−1)^{2027}",
         "opcijas": ["Pozitīva", "Negatīva", "Nulle", "Nevar noteikt"],
         "pareizi": 1, "padoms": "2027 - nepāra.", "jaukt": False},
        {"jaut": "(−4)^3 · (−2)^2",
         "opcijas": ["Pozitīva", "Negatīva", "Nulle", "Nevar noteikt"],
         "pareizi": 1, "padoms": "Mīnuss reiz pluss.", "jaukt": False},
    ], pamats=4),

    Ievadi("Aprēķini", [
        {"jaut": "(−1)^{100} + (−1)^{101}", "atb": ["0"],
         "padoms": "1 + (−1)."},
        {"jaut": "(−3)^3", "atb": ["−27", "-27"], "padoms": "Nepāra."},
        {"jaut": "−(−2)^2", "atb": ["−4", "-4"], "padoms": "−(4)."},
        {"jaut": "(−{1|2})^−3", "atb": ["−8", "-8"], "padoms": "(−2)^3."},
    ]),

    Pasaule("Pārvietojums pa ielu",
            Ievadi("", [
                {"jaut": "Robots katrā solī iet 1 m un maina virzienu: "
                         "(−1)^1 + (−1)^2 + ... Kur tas ir pēc 2 soļiem?",
                 "atb": ["0"], "padoms": "−1 + 1."},
                {"jaut": "Pēc 7 soļiem? (nepāra skaits)",
                 "atb": ["−1", "-1"], "padoms": "Viens −1 paliek pāri."},
                {"jaut": "Pēc 2026 soļiem?",
                 "atb": ["0"], "padoms": "1013 pāri."},
            ]),
            pavediens="tehnika",
            konteksts="Svārsts, maiņstrāva, pulsējošs signāls - viss, kas "
                      "mainās «uz priekšu - atpakaļ», ir (−1)^n.",
            kapec="Pāra-nepāra likums pasaka rezultātu bez skaitīšanas."),

    Kopsavilkums([
        "Nosaku pakāpes zīmi pēc bāzes un kāpinātāja paritātes.",
        "Atšķiru (−a)^n no −a^n.",
        "Zinu, ka negatīvs kāpinātājs zīmi nemaina.",
    ]),

    Majas([
        "Nosaki zīmi: (−5)^7, (−0,1)^8, −3^4, (−2)^−5.",
        "Aprēķini (−1)^1 + (−1)^2 + ... + (−1)^{15}.",
        "Paskaidro, kāpēc (−a)^2 = a^2 jebkuram a.",
    ]),
]
