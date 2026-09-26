# -*- coding: utf-8 -*-
"""2. klase, 74. stunda: «Kura izteiksme der šim risinājumam?»

Saskaņošana: risinājums pa soļiem ↔ viena izteiksme. Katrs solis atbilst
vienai izteiksmes darbībai; ja pirmajā solī saskaita divus skaitļus, kas
pēc tam jāatņem, izteiksmē tie stāv iekavās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kura izteiksme der šim risinājumam?"

MERKIS = ("Šodien katrai izteiksmei atradīsim atbilstošu pierakstu pa "
          "soļiem un otrādi.")

SATURS = [
    Sakums("Pa soļiem vai vienā rindā - tas pats risinājums?",
           zimejums=restis([["pa soļiem", "izteiksme"],
                            ["1) 12 + 8 = 20", "50 − (12 + 8)"],
                            ["2) 50 − 20 = 30", "= 30"]]),
           fakti=["Katrs solis ir viena darbība izteiksmē.",
                  "Ja 1. solī summa, ko pēc tam atņem - tai vajag iekavas."]),

    Doma("Soļi ↔ izteiksme",
         "Izteiksme ir visi soļi kopā tajā secībā, kā tos izpilda.",
         soli=[
             "1. solis ir tā darbība, ko izteiksmē izpilda vispirms.",
             "Ja tā nav pirmā no kreisās - vajag iekavas.",
             "2. solis izmanto 1. soļa rezultātu.",
             "Pārbaudi: vai abi pieraksti dod vienu skaitli?",
         ]),

    Varianti("Atrodi izteiksmi soļiem", [
        {"jaut": "1) 35 + 15 = 50; 2) 50 − 20 = 30",
         "opcijas": ["35 + 15 − 20", "35 − (15 + 20)", "35 + (15 + 20)"],
         "pareizi": 0, "padoms": "Vispirms saskaita, tad atņem."},
        {"jaut": "1) 15 + 20 = 35; 2) 60 − 35 = 25",
         "opcijas": ["60 − (15 + 20)", "60 − 15 + 20", "15 + 20 − 60"],
         "pareizi": 0, "padoms": "No 60 atņem summu."},
        {"jaut": "1) 80 − 30 = 50; 2) 50 − 15 = 35",
         "opcijas": ["80 − 30 − 15", "80 − (30 − 15)", "80 + 30 − 15"],
         "pareizi": 0, "padoms": "Divreiz atņem pēc kārtas."},
        {"jaut": "1) 40 + 25 = 65; 2) 90 − 65 = 25",
         "opcijas": ["90 − (40 + 25)", "90 − 40 + 25", "40 + 25 + 90"],
         "pareizi": 0, "padoms": "No 90 atņem summu."},
    ]),

    Ievadi("Uzraksti soļus - atbildi uz jautājumu", [
        {"jaut": "Izteiksme 70 − (18 + 22). Kāds ir 1. soļa rezultāts?",
         "atb": ["40"], "padoms": "Iekavās: 18 + 22."},
        {"jaut": "Kāds ir 2. soļa rezultāts?", "atb": ["30"],
         "padoms": "70 − 40."},
        {"jaut": "Izteiksme 45 + 15 − 30. 1. soļa rezultāts?",
         "atb": ["60"], "padoms": "45 + 15."},
        {"jaut": "2. soļa rezultāts?", "atb": ["30"], "padoms": "60 − 30."},
    ]),

    Pasaule("Kas ir kasiera čekā?",
            Varianti("", [
                {"jaut": "Kasiere rēķināja: 1) 8 + 7 = 15 €; 2) 20 − 15 = 5 €. "
                         "Kāda izteiksme?",
                 "opcijas": ["20 − (8 + 7)", "20 − 8 + 7", "8 + 7 + 20"],
                 "pareizi": 0, "padoms": "No 20 atņem pirkumu summu."},
                {"jaut": "Ko nozīmē 5 €?",
                 "opcijas": ["atlikums", "pirkuma cena", "iedotā nauda"],
                 "pareizi": 0, "padoms": "Kas paliek pāri."},
            ]),
            pavediens="veikals",
            konteksts="Pircējs iedeva 20 € par diviem pirkumiem - 8 € un 7 €.",
            kapec="Viena izteiksme apraksta visu pirkumu."),

    Kopsavilkums([
        "Katram solim atrodu vietu izteiksmē.",
        "Zinu, kad vajag iekavas.",
        "Pārvēršu izteiksmi soļos un otrādi.",
    ]),

    Majas([
        "Uzraksti divus soļus kādam mājas uzdevumam.",
        "Pārraksti tos vienā izteiksmē.",
        "Pārbaudi, vai vērtība sakrīt.",
    ]),
]
