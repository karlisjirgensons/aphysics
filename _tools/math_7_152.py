# -*- coding: utf-8 -*-
"""7. klase, 152. stunda: «Kad nevienādība ir patiesa?»

Nevienādība ar mainīgo var būt patiesa visiem skaitļiem (x² + 1 > 0), nevienam
(x² < −1) vai tikai dažiem (x + 2 > 5). Stunda iemāca pārbaudīt skaitļus un
atšķirt šos gadījumus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kad nevienādība ir patiesa?"

MERKIS = ("Noteiksim, vai nevienādība ir patiesa visām vai tikai dažām "
          "nezināmā vērtībām.")

SATURS = [
    Sakums("Ātruma ierobežojums: v ≤ 50",
           zimejums=taisne(0, 80, 10, intervali=[(0, 50, True, True)]),
           paraksts="Atļauti visi ātrumi no 0 līdz 50 km/h ieskaitot.",
           fakti=["49 km/h - patiess, 50 - patiess, 51 - aplams.",
                  "Nevienādība atdala «atļauts» no «aizliegts».",
                  "Zīmes: <, >, ≤ (mazāks vai vienāds), ≥."]),

    Doma("Patiesa - kādiem skaitļiem?",
         "Nevienādība ar mainīgo kļūst par patiesu vai aplamu skaitlisku "
         "nevienādību, ievietojot skaitli. Skaitli, ar kuru tā ir patiesa, "
         "sauc par nevienādības atrisinājumu.",
         soli=[
             "Ievieto skaitli un aprēķini abas puses.",
             "Salīdzini: vai patiess?",
             "Pārbaudi vairākus skaitļus - arī negatīvus un 0.",
             "Secini: visiem, nevienam vai dažiem.",
         ],
         pieze="≤ nozīmē «mazāks vai vienāds»: 5 ≤ 5 ir patiess, 5 < 5 - "
               "aplams."),

    Paraugs("Pārbaudi skaitļus",
            uzd="Kuri no skaitļiem −1; 2; 3; 4 ir nevienādības 2x − 1 ≥ 5 "
                "atrisinājumi?",
            soli=[
                ("x = −1: −3 ≥ 5 - aplams", ""),
                ("x = 2: 3 ≥ 5 - aplams", ""),
                ("x = 3: 5 ≥ 5 - patiess", "Ieskaitot."),
                ("x = 4: 7 ≥ 5 - patiess", ""),
            ],
            atbilde="3 un 4"),

    Varianti("Visiem, nevienam vai dažiem?", [
        {"jaut": "x² ≥ 0",
         "opcijas": ["Visiem", "Nevienam", "Dažiem"],
         "pareizi": 0, "jaukt": False, "padoms": "Kvadrāts nav negatīvs."},
        {"jaut": "x + 1 < x",
         "opcijas": ["Visiem", "Nevienam", "Dažiem"],
         "pareizi": 1, "jaukt": False, "padoms": "1 < 0 - aplams."},
        {"jaut": "3x > 12",
         "opcijas": ["Visiem", "Nevienam", "Dažiem"],
         "pareizi": 2, "jaukt": False, "padoms": "x > 4."},
        {"jaut": "|x| ≥ 0",
         "opcijas": ["Visiem", "Nevienam", "Dažiem"],
         "pareizi": 0, "jaukt": False, "padoms": "Modulis."},
    ], pamats=4),

    Ievadi("Pārbaudi", [
        {"jaut": "Vai x = 5 der nevienādībai 3x − 4 > 10? Raksti «jā» vai "
                 "«nē».",
         "atb": ["jā", "ja"], "padoms": "11 > 10."},
        {"jaut": "Vai x = −2 der nevienādībai 5 − x ≤ 6?",
         "atb": ["nē", "ne"], "padoms": "7 ≤ 6 - aplams."},
        {"jaut": "Mazākais vesels x, kam x + 7 > 10?",
         "atb": ["4"], "padoms": "x > 3."},
    ]),

    Pasaule("Lifta kravnesība",
            Ievadi("", [
                {"jaut": "Lifts ≤ 400 kg. 4 cilvēki pa 80 kg un kaste x kg. "
                         "Lielākā kastes masa (kg)?",
                 "atb": ["80"], "padoms": "320 + x ≤ 400."},
                {"jaut": "Vai kaste 85 kg ir atļauta? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "405 > 400."},
                {"jaut": "Ja iekāpj 5 cilvēki pa 80 kg - cik kg vēl drīkst?",
                 "atb": ["0"], "padoms": "400 − 400."},
            ]),
            pavediens="tehnika",
            konteksts="Drošības ierobežojumi ir nevienādības: ātrums, "
                      "kravnesība, vecums.",
            kapec="«Ne vairāk» nozīmē ≤."),

    Kopsavilkums([
        "Pārbaudu, vai skaitlis ir nevienādības atrisinājums.",
        "Atšķiru <, >, ≤, ≥.",
        "Nosaku: patiesa visiem, nevienam vai dažiem.",
        "Lasu ierobežojumus kā nevienādības.",
    ]),

    Majas([
        "Atrodi 3 ierobežojumus dzīvē un pieraksti tos ar nevienādībām.",
        "Pārbaudi skaitļus −2 … 3 nevienādībai 2x + 1 ≤ 5.",
        "Uzraksti nevienādību, kas patiesa visiem x.",
    ]),
]
