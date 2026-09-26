# -*- coding: utf-8 -*-
"""3. klase, 41. stunda: «Kā aprēķināt izteiksmi ar iekavām?»

Tagad izteiksmē ir 2-4 darbības un iekavas. Galvenais paņēmiens ir pieraksts:
katrā solī pārraksta visu izteiksmi no jauna, aizstājot izpildīto darbību ar
tās rezultātu. Tā kļūda paliek redzama, nevis pazūd galvā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kā aprēķināt izteiksmi ar iekavām?"

MERKIS = ("Aprēķināsim izteiksmes vērtību, kurā ir 2-4 darbības un iekavas.")

SATURS = [
    Sakums("Kā netikt apmaldīties garā izteiksmē?",
           zimejums=restis([["(30 − 12) : 3 + 4 · 2"],
                            ["18 : 3 + 4 · 2"],
                            ["6 + 8"],
                            ["14"]],
                           "četri soļi"),
           paraksts="Katrā solī pārraksta visu izteiksmi no jauna.",
           fakti=["Garā izteiksmē kļūda rodas tad, kad soļus tur galvā.",
                  "Pārrakstot izteiksmi, katrs solis paliek redzams."]),

    Doma("Katrā solī izpildi vienu darbību un pārraksti visu",
         "Izteiksme ar katru soli kļūst īsāka, līdz paliek viens skaitlis.",
         soli=[
             "Atrodi darbību, kura pēc secības ir pirmā.",
             "Izrēķini to.",
             "Pārraksti visu izteiksmi, ieliekot rezultātu tās vietā.",
             "Atkārto, līdz paliek viens skaitlis.",
         ],
         pieze="Ja iekavas ir vairākas, sāc ar to, kas ir iekšpusē: "
               "((8 + 4) : 2) · 5 - vispirms 8 + 4."),

    Slidnis("Kā sarūk izteiksme",
            soli=[
                {"v": "(30 − 12) : 3 + 4 · 2",
                 "teksts": "Sākuma izteiksme.", "josla": 25},
                {"v": "18 : 3 + 4 · 2",
                 "teksts": "Izpildīja iekavas.", "josla": 50},
                {"v": "6 + 8",
                 "teksts": "Izpildīja dalīšanu un reizināšanu.",
                 "josla": 75},
                {"v": "14", "teksts": "Palika viens skaitlis.", "josla": 100},
            ],
            ievads="Spied soļus - izteiksme katrā solī kļūst īsāka."),

    Paraugs("Cik ir 5 · (12 − 4) : 8?",
            uzd="Aprēķini izteiksmes 5 · (12 − 4) : 8 vērtību.",
            soli=[
                ("12 − 4 = 8",
                 "Vispirms iekavas."),
                ("5 · 8 : 8",
                 "Pārraksta izteiksmi ar iegūto skaitli."),
                ("40 : 8 = 5",
                 "Reizināšanu un dalīšanu izpilda no kreisās puses."),
            ],
            atbilde="5"),

    Ievadi("Aprēķini pa soļiem", [
        {"jaut": "(15 + 5) : 4 = ?", "atb": ["5"],
         "padoms": "Vispirms iekavas."},
        {"jaut": "3 · (10 − 4) = ?", "atb": ["18"],
         "padoms": "Vispirms 10 − 4."},
        {"jaut": "(24 : 6) · 5 = ?", "atb": ["20"],
         "padoms": "Vispirms 24 : 6."},
        {"jaut": "(30 − 12) : 3 + 4 = ?", "atb": ["10"],
         "padoms": "18 : 3 = 6; 6 + 4."},
        {"jaut": "2 · (7 + 3) − 5 = ?", "atb": ["15"],
         "padoms": "2 · 10 = 20; 20 − 5."},
        {"jaut": "(8 + 4) : 2 · 5 = ?", "atb": ["30"],
         "padoms": "12 : 2 = 6; 6 · 5."},
    ], pamats=4),

    Zimejums("Iekava iekavā",
             restis([["((8 + 4) : 2) · 5"],
                     ["(12 : 2) · 5"],
                     ["6 · 5 = 30"]],
                    "sāk ar iekšējo iekavu"),
             paskaidro="Ja iekavas ir viena otrā, vispirms izpilda to, kas "
                       "ir iekšpusē.",
             ievads="Trīs soļi, un izteiksme ir izrēķināta."),

    Varianti("Kura darbība tagad?", [
        {"jaut": "Kura darbība ir pirmā izteiksmē 4 · (6 + 2) − 10?",
         "opcijas": ["6 + 2", "4 · 6", "2 − 10", "4 − 10"],
         "pareizi": 0, "padoms": "Vispirms iekavas."},
        {"jaut": "Cik ir (20 − 8) : 4?",
         "opcijas": ["3", "18", "12", "5"],
         "pareizi": 0, "padoms": "12 : 4."},
        {"jaut": "Cik ir 36 : (2 + 4)?",
         "opcijas": ["6", "22", "18", "9"],
         "pareizi": 0, "padoms": "36 : 6."},
        {"jaut": "Cik ir 2 · 3 + 4 · 5?",
         "opcijas": ["26", "50", "70", "45"],
         "pareizi": 0, "padoms": "6 + 20."},
    ], pamats=4),

    Pasaule("Cik vietas aizņem dublikāti?",
            Ievadi("", [
                {"jaut": "Mapē 5 attēli pa 4 MB un 3 video pa 12 MB. Cik MB "
                         "kopā? (5 · 4 + 3 · 12)",
                 "atb": ["56"], "padoms": "20 + 36."},
                {"jaut": "Visu sadalīja 8 vienādās daļās. (56 : 8)",
                 "atb": ["7"], "padoms": "56 : 8."},
                {"jaut": "No 100 MB izdzēsa 4 failus pa 9 MB. "
                         "(100 − 4 · 9)",
                 "atb": ["64"], "padoms": "100 − 36."},
                {"jaut": "6 mapes pa (10 − 3) MB. (6 · (10 − 3))",
                 "atb": ["42"], "padoms": "6 · 7."},
            ]),
            pavediens="dati",
            konteksts="Datora mapes izmēru rēķina tieši tā: katru veidu "
                      "atsevišķi un tad saskaita.",
            kapec="Garš rēķins pa soļiem ir drošāks nekā viens ilgs "
                  "domāšanas brīdis."),

    Kopsavilkums([
        "Aprēķinu izteiksmes ar 2-4 darbībām un iekavām.",
        "Katrā solī izpildu vienu darbību un pārrakstu visu izteiksmi.",
        "Sāku ar iekšējo iekavu, ja to ir vairākas.",
        "Pārbaudu, vai beigās palicis viens skaitlis.",
    ]),

    Majas([
        "Aprēķini (40 − 16) : 4 + 3 · 2 un pieraksti visus soļus.",
        "Pārbaudi atbildi ar kalkulatoru.",
        "Izdomā izteiksmi ar divām iekavām un iedod to draugam.",
    ]),
]
