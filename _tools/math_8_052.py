# -*- coding: utf-8 -*-
"""8. klase, 52. stunda: «Kāda ir aptuvenā vērtība?»

Ja sakne nav izvelkama precīzi, to «ieķer» starp diviem kvadrātiem un
precizē pa soļiem. Kalkulators dod to pašu uzreiz, bet novērtējums
pasargā no nospiesta nepareiza cipara.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, taisne)

TEMA = "Kāda ir aptuvenā vērtība?"

MERKIS = ("Noteiksim kvadrātsaknes aptuveno vērtību, izmantojot kvadrātu "
          "tabulu vai kalkulatoru.")

SATURS = [
    Sakums("√20 - starp 4 un 5",
           zimejums=taisne(4, 5, 0.1, [(4.47, "√20")],
                           intervali=[(4.4, 4.5, True, True)]),
           paraksts="16 < 20 < 25, tātad 4 < √20 < 5.",
           fakti=["4,4² = 19,36 - par maz.",
                  "4,5² = 20,25 - par daudz.",
                  "√20 ≈ 4,47."]),

    Doma("Ieķer sakni",
         "Aptuveno vērtību atrod, meklējot divus tuvus skaitļus, kuru kvadrāti "
         "ir abās pusēs zemsaknes skaitlim.",
         soli=[
             "Atrodi tuvākos pilnos kvadrātus: 16 < 20 < 25.",
             "Tātad sakne ir starp to saknēm: 4 < √20 < 5.",
             "Pārbaudi desmitdaļas: 4,4^2 un 4,5^2.",
             "Vajadzības gadījumā - simtdaļas.",
             "Ar kalkulatoru: poga √, bet novērtējums vispirms.",
         ]),

    Slidnis("Precizē √7", [
        {"v": "2 < √7 < 3", "teksts": "4 < 7 < 9"},
        {"v": "2,6 < √7 < 2,7", "teksts": "2,6^2 = 6,76; 2,7^2 = 7,29"},
        {"v": "2,64 < √7 < 2,65", "teksts": "2,64^2 = 6,9696; "
                                            "2,65^2 = 7,0225"},
        {"v": "√7 ≈ 2,65", "teksts": "7 tuvāk 7,0225 nekā 6,9696"},
    ]),

    Paraugs("Kalkulators un novērtējums",
            uzd="Atrodi √150 līdz simtdaļām.",
            soli=[
                ("144 < 150 < 169, tātad 12 < √150 < 13", "Novērtējums."),
                ("Kalkulators: 12,247...", "Iekrīt novērtējumā."),
                ("√150 ≈ 12,25", "Līdz simtdaļām."),
            ],
            atbilde="√150 ≈ 12,25"),

    Ievadi("Novērtē un aprēķini", [
        {"jaut": "Starp kuriem veseliem ir √50? Ieraksti mazāko.",
         "atb": ["7"], "padoms": "49 < 50 < 64."},
        {"jaut": "Starp kuriem veseliem ir √90? Ieraksti lielāko.",
         "atb": ["10"], "padoms": "81 < 90 < 100."},
        {"jaut": "√3 līdz desmitdaļām", "atb": ["1,7", "1.7"],
         "padoms": "1,7^2 = 2,89; 1,8^2 = 3,24."},
        {"jaut": "√10 līdz simtdaļām", "atb": ["3,16", "3.16"],
         "padoms": "3,16^2 = 9,9856."},
        {"jaut": "√200 līdz desmitdaļām", "atb": ["14,1", "14.1"],
         "padoms": "14,1^2 = 198,81."},
        {"jaut": "√(0,5) līdz simtdaļām", "atb": ["0,71", "0.71"],
         "padoms": "0,7^2 = 0,49."},
    ], pamats=4),

    Varianti("Kurš novērtējums pareizs?", [
        {"jaut": "√40 ≈",
         "opcijas": ["6,3", "20", "4,0", "7,1"],
         "pareizi": 0, "padoms": "36 < 40 < 49."},
        {"jaut": "Kalkulators rāda √85 = 92,2. Kas noticis?",
         "opcijas": ["Nospiests nepareizi - jābūt ap 9,2", "Viss pareizi",
                     "Kalkulators bojāts", "Jāņem −92,2"],
         "pareizi": 0, "padoms": "81 < 85 < 100."},
    ]),

    Pasaule("Televizora ekrāns",
            Ievadi("", [
                {"jaut": "Kvadrātveida mākslas darba laukums 2 m². Mala līdz "
                         "centimetriem (m)?",
                 "atb": ["1,41", "1.41"], "padoms": "√2 ≈ 1,414."},
                {"jaut": "Rāmim vajag 4 malas. Cik metru līstes (līdz "
                         "desmitdaļām, uz augšu)?",
                 "atb": ["5,7", "5.7"], "padoms": "4 · 1,414 = 5,656."},
                {"jaut": "Kvadrātveida paklājs 10 m². Mala līdz desmitdaļām?",
                 "atb": ["3,2", "3.2"], "padoms": "√10 ≈ 3,16."},
            ]),
            pavediens="maja",
            konteksts="Kvadrāta mala no laukuma, kas nav pilns kvadrāts, ir "
                      "iracionāla - veikalā vajag tuvinājumu.",
            kapec="Novērtējums pasaka, vai mērlentes rezultāts ir ticams."),

    Kopsavilkums([
        "Novērtēju sakni starp diviem veseliem skaitļiem.",
        "Precizēju līdz desmitdaļām un simtdaļām.",
        "Pārbaudu kalkulatora rezultātu ar novērtējumu.",
    ]),

    Majas([
        "Novērtē un tad aprēķini ar kalkulatoru: √30, √120, √(0,3).",
        "Bez kalkulatora atrodi √5 līdz desmitdaļām.",
        "Uzraksti, kāpēc √(0,4) > 0,4.",
    ]),
]
