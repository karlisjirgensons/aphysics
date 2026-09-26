# -*- coding: utf-8 -*-
"""7. klase, 128. stunda: «Vai apgalvojums par izteiksmēm ir patiess?»

Apgalvojumu par visiem skaitļiem pierāda ar pārveidojumu, bet atspēko ar
vienu pretpiemēru. Klasisks piemērs: «trīs pēc kārtas esošu skaitļu summa
dalās ar 3» - to pierāda ar n + (n + 1) + (n + 2) = 3(n + 1).
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Vai apgalvojums par izteiksmēm ir patiess?"

MERKIS = ("Pamatosim, ka izteiksmes ir identiski vienādas, vai atspēkosim "
          "to ar pretpiemēru.")

SATURS = [
    Sakums("Trīs pēc kārtas - dalās ar 3?",
           zimejums=restis([["skaitļi", "summa", ": 3"],
                            ["4, 5, 6", "15", "5"],
                            ["10, 11, 12", "33", "11"],
                            ["n, n + 1, n + 2", "3n + 3", "n + 1"]]),
           paraksts="Pēdējā rinda pierāda visiem n.",
           fakti=["Piemēri ir pārliecinoši, bet nepierāda.",
                  "Ar n pierādījums der visiem skaitļiem.",
                  "3n + 3 = 3(n + 1) - dalās ar 3."]),

    Doma("Pierādi ar burtiem, atspēko ar skaitli",
         "Apgalvojumu par visiem skaitļiem pierāda, pierakstot to ar "
         "mainīgajiem un pārveidojot. Aplamu apgalvojumu atspēko ar vienu "
         "konkrētu pretpiemēru.",
         soli=[
             "Pieraksti apgalvojumu ar mainīgo (n, 2n, 2n + 1).",
             "Pārveido izteiksmi (atver iekavas, iznes kopīgo).",
             "Parādi vajadzīgo īpašību (piemēram, reizinātāju 3).",
             "Ja neizdodas - meklē pretpiemēru.",
         ],
         pieze="Pāra skaitli pieraksta kā 2n, nepāra - kā 2n + 1."),

    Paraugs("Divu nepāra skaitļu summa",
            uzd="Pierādi, ka divu nepāra skaitļu summa ir pāra skaitlis.",
            soli=[
                ("Nepāra skaitļi: 2m + 1 un 2n + 1", "Pieraksta."),
                ("(2m + 1) + (2n + 1) = 2m + 2n + 2", "Saskaita."),
                ("= 2(m + n + 1)", "Iznes 2."),
                ("Dalās ar 2 - pāra skaitlis", "Secinājums."),
            ],
            atbilde="Pierādīts."),

    Varianti("Patiess vai aplams?", [
        {"jaut": "Divu pāra skaitļu summa ir pāra.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "2m + 2n = 2(m + n)."},
        {"jaut": "Četru pēc kārtas esošu skaitļu summa dalās ar 4.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 1, "jaukt": False,
         "padoms": "1 + 2 + 3 + 4 = 10."},
        {"jaut": "Pāra un nepāra skaitļa summa ir nepāra.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "2m + 2n + 1."},
        {"jaut": "Jebkuram n izteiksme n² + n ir pāra.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "n(n + 1) - viens no tiem pāra."},
        {"jaut": "Jebkuram n: 2n + 1 > n.",
         "opcijas": ["Patiess naturāliem n", "Aplams naturāliem n"],
         "pareizi": 0, "jaukt": False,
         "padoms": "n + 1 > 0."},
        {"jaut": "a + b = b + a jebkuriem a, b.",
         "opcijas": ["Patiess", "Aplams"], "pareizi": 0, "jaukt": False,
         "padoms": "Pārvietojamības likums."},
    ], pamats=4),

    Zimejums("Pāra un nepāra pieraksts",
             restis([["skaitlis", "pieraksts"],
                     ["pāra", "2n"],
                     ["nepāra", "2n + 1"],
                     ["dalās ar 3", "3n"],
                     ["trīs pēc kārtas", "n, n + 1, n + 2"]]),
             paskaidro="Ar šiem pierakstiem pierāda apgalvojumus par visiem "
                       "skaitļiem."),

    Pasaule("Kalendāra triks",
            Varianti("", [
                {"jaut": "Kalendārā izvēlies 3 datumus vienā kolonnā pēc "
                         "kārtas (n, n + 7, n + 14). Summa ir...",
                 "opcijas": ["3n + 21 = 3(n + 7) - trīsreiz vidējais",
                             "3n", "n + 21", "nav likumsakarības"],
                 "pareizi": 0, "padoms": "Saskaiti."},
                {"jaut": "Draugs saka summu 57. Kāds ir vidējais datums?",
                 "opcijas": ["19", "12", "26", "57"],
                 "pareizi": 0, "padoms": "57 : 3."},
                {"jaut": "Kāpēc triks strādā vienmēr?",
                 "opcijas": ["Pierādīts ar izteiksmi visiem n",
                             "Tā gadās", "Kalendāri ir vienādi",
                             "Tikai septembrī"],
                 "pareizi": 0, "padoms": "3(n + 7)."},
            ]),
            pavediens="skola",
            konteksts="Matemātiskie triki «uzminu tavu skaitli» strādā, jo "
                      "ir pierādīti ar izteiksmēm.",
            kapec="Pierādījums - garantija visiem gadījumiem."),

    Kopsavilkums([
        "Pierakstu apgalvojumu ar mainīgajiem.",
        "Pierādu ar pārveidojumu.",
        "Atspēkoju ar pretpiemēru.",
        "Lietoju pierakstus 2n, 2n + 1, n, n + 1.",
    ]),

    Majas([
        "Pierādi: piecu pēc kārtas esošu skaitļu summa dalās ar 5.",
        "Izdomā kalendāra triku draugam.",
        "Atspēko: «divu nepāra skaitļu reizinājums ir pāra».",
    ]),
]
