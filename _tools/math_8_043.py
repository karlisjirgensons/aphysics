# -*- coding: utf-8 -*-
"""8. klase, 43. stunda: «Kā pārbaudīt starprezultātus?»

Novērtējums «ar apaļiem skaitļiem» pirms aprēķina pasaka, kādai atbildei
jābūt. Ja kalkulators rāda 10 reizes vairāk - kļūda nospiesta pogā. Bloka
noslēgums: skolēns seko svešai aprēķinu gaitai un atrod kļūdaino soli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis)

TEMA = "Kā pārbaudīt starprezultātus?"

MERKIS = ("Sekosim aprēķinu gaitai un pārbaudīsim starprezultātus ar "
          "novērtējumu.")

SATURS = [
    Sakums("Vai 48,7 · 21,3 = 10 373,1?",
           zimejums=restis([["novērtē", "50 · 20 = 1000"],
                            ["kalkulators", "10 373,1"],
                            ["secinājums", "10 reizes par daudz!"]]),
           paraksts="Pareizi ir 1037,31 - nospiests komats nepareizā vietā.",
           fakti=["Novērtējums aizņem 5 sekundes.",
                  "Tas neatrod mazas kļūdas, bet atrod lielas.",
                  "Lielākās kļūdas ir komatā un nullēs."]),

    Doma("Novērtējums",
         "Pirms rēķini precīzi, noapaļo katru skaitli līdz vienam vai diviem "
         "cipariem un aprēķini ar galvu.",
         soli=[
             "Noapaļo skaitļus līdz ērtiem: 48,7 ≈ 50; 21,3 ≈ 20.",
             "Aprēķini novērtējumu: 50 · 20 = 1000.",
             "Aprēķini precīzi.",
             "Salīdzini: vai kārta (ciparu skaits) sakrīt?",
             "Katram starprezultātam - tāda pati pārbaude.",
         ]),

    Slidnis("Atrodi kļūdaino soli", [
        {"v": "Uzdevums", "teksts": "3 kastes pa 12,5 kg un 4 maisi pa 4,8 kg. "
                                    "Kopējā masa?"},
        {"v": "3 · 12,5 = 37,5", "teksts": "Novērtējums 3 · 12 = 36 - labi"},
        {"v": "4 · 4,8 = 1,92", "teksts": "Novērtējums 4 · 5 = 20 - kļūda!"},
        {"v": "4 · 4,8 = 19,2", "teksts": "Izlabots"},
        {"v": "37,5 + 19,2 = 56,7", "teksts": "Novērtējums 36 + 20 = 56 - labi"},
    ]),

    Ievadi("Novērtē", [
        {"jaut": "Novērtē 297 · 41 (noapaļo līdz 300 un 40).",
         "atb": ["12000", "12 000"], "padoms": "300 · 40."},
        {"jaut": "Novērtē 7,89 : 1,98 (līdz veseliem).",
         "atb": ["4"], "padoms": "8 : 2."},
        {"jaut": "Novērtē 0,52 · 61 (0,5 un 60).",
         "atb": ["30"], "padoms": "Puse no 60."},
        {"jaut": "Kalkulators rāda 596 : 0,49 = 121,6. Kāds ir pareizais "
                 "rezultāts (līdz desmitdaļām)?",
         "atb": ["1216,3", "1216.3"], "padoms": "600 : 0,5 = 1200."},
    ]),

    Varianti("Kurš rezultāts ticams?", [
        {"jaut": "19,8 · 5,1 =",
         "opcijas": ["100,98", "10,098", "1009,8", "1,0098"],
         "pareizi": 0, "padoms": "20 · 5 = 100."},
        {"jaut": "Skolēna augums metros ir...",
         "opcijas": ["1,62", "16,2", "162", "0,162"],
         "pareizi": 0, "padoms": "Salīdzini ar durvīm (2 m)."},
        {"jaut": "Cik kg sver 1 litrs ūdens?",
         "opcijas": ["1", "10", "0,1", "100"],
         "pareizi": 0, "padoms": "Ūdens blīvums 1 kg/l."},
    ]),

    Pasaule("Ceļojuma budžets",
            Ievadi("", [
                {"jaut": "Viesnīca 3 naktis pa 68 €. Novērtē (70 · 3).",
                 "atb": ["210"], "padoms": "70 · 3."},
                {"jaut": "Precīzi?",
                 "atb": ["204"], "padoms": "68 · 3."},
                {"jaut": "Ēdiens 4 cilvēkiem 3 dienas pa 19,50 € dienā "
                         "cilvēkam. Precīzi?",
                 "atb": ["234"], "padoms": "12 · 19,5."},
                {"jaut": "Kopā viesnīca un ēdiens?",
                 "atb": ["438"], "padoms": "204 + 234."},
            ]),
            pavediens="celojums",
            konteksts="Plānojot ceļojumu, vispirms novērtē - vai vispār "
                      "pietiek naudas -, un tikai tad rēķina precīzi.",
            kapec="Novērtējums pasargā no pārsteiguma kasē."),

    Kopsavilkums([
        "Novērtēju rezultātu ar noapaļotiem skaitļiem.",
        "Pārbaudu katru starprezultātu.",
        "Atrodu kļūdu komatā vai nullēs.",
        "Izvērtēju, vai rezultāts ir ticams dzīvē.",
    ]),

    Majas([
        "Novērtē un tad aprēķini: 38,2 · 11,9; 812 : 3,9.",
        "Atrodi čekā kopsummu un novērtē to, noapaļojot cenas.",
        "Uzraksti vienu aprēķinu ar tīšu kļūdu - lai klasesbiedrs to atrod.",
    ]),
]
