# -*- coding: utf-8 -*-
"""7. klase, 162. stunda: «Kā pārbaudīt atrisinājumu?»

Nevienādības atrisinājumu pārbauda ar trim skaitļiem: vienu no intervāla
(jābūt patiesam), vienu ārpus tā (jābūt aplamam) un pašu robežu
(patiess tikai, ja ≤ vai ≥). Tā atklāj gan aprēķina, gan zīmes kļūdas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pārbaudīt atrisinājumu?"

MERKIS = ("Pārbaudīsim atrisinājumu, izvēloties skaitli no iegūtā "
          "intervāla.")

SATURS = [
    Sakums("Trīs skaitļi - pilna pārbaude",
           fakti=["Skaitlis iekšā - nevienādībai jābūt patiesai.",
                  "Skaitlis ārā - jābūt aplamai.",
                  "Robeža - patiesa tikai ar ≤ vai ≥."]),

    Doma("Pārbaudi iekšā, ārā un robežā",
         "Lai pārbaudītu nevienādības atrisinājumu, sākotnējā nevienādībā "
         "ievieto skaitli no atrisinājuma (jābūt patiesam), skaitli ārpus tā "
         "(jābūt aplamam) un robežu.",
         soli=[
             "Izvēlies ērtu skaitli intervālā.",
             "Izvēlies skaitli ārpus intervāla.",
             "Pārbaudi robežu - vai tā ietilpst?",
             "Ja kāda pārbaude neder - meklē kļūdu (bieži - zīmes maiņā).",
         ]),

    Paraugs("Atklāj kļūdu",
            uzd="Līga atrisināja −2x + 4 > 10 un ieguva x > −3. Pārbaudi.",
            soli=[
                ("x = 0 (Līgas intervālā): 4 > 10 - aplams!", "Kļūda."),
                ("x = −4 (ārpus): 12 > 10 - patiess!", "Apgriezti."),
                ("−2x > 6 ⇒ x < −3", "Aizmirsta zīmes maiņa."),
            ],
            atbilde="Pareizi: x < −3."),

    Ievadi("Pārbaudi", [
        {"jaut": "3x − 2 ≤ 7, atbilde x ≤ 3. Vai x = 3 der? Raksti «jā» vai "
                 "«nē».",
         "atb": ["jā", "ja"], "padoms": "7 ≤ 7."},
        {"jaut": "5 − x < 1, atbilde x > 4. Vai x = 4 der?",
         "atb": ["nē", "ne"], "padoms": "1 < 1 - aplams."},
        {"jaut": "4x + 1 > 9, Toms: x > 2. Vai x = 3 der?",
         "atb": ["jā", "ja"], "padoms": "13 > 9."},
        {"jaut": "−3x ≥ 12, Anna: x ≥ −4. Vai x = 0 der sākotnējā?",
         "atb": ["nē", "ne"], "padoms": "0 ≥ 12 - aplams, Anna kļūdījās."},
    ]),

    Varianti("Kura pārbaude atklāj kļūdu?", [
        {"jaut": "Atbilde x > 5, bet pareizā x ≥ 5. Kurš skaitlis atklās?",
         "opcijas": ["5 - robeža", "6", "0", "100"],
         "pareizi": 0, "padoms": "Tikai robežā atšķiras."},
        {"jaut": "Atbilde x > 2, bet pareizā x < 2. Kurš skaitlis atklās?",
         "opcijas": ["Jebkurš, piemēram, 3", "Tikai 2", "Neviens",
                     "Tikai −100"],
         "pareizi": 0, "padoms": "Viss intervāls apgriezts."},
    ]),

    Pasaule("Pasūtījums ar bezmaksas piegādi",
            Ievadi("", [
                {"jaut": "Bezmaksas piegāde, ja pirkums ≥ 35 €. Grozā 22 € un "
                         "grāmatas pa 4 €. Cik grāmatu vismaz jāpievieno? "
                         "(22 + 4n ≥ 35)",
                 "atb": ["4"], "padoms": "4n ≥ 13, n ≥ 3,25."},
                {"jaut": "Pārbaude: ar 3 grāmatām cik €?",
                 "atb": ["34"], "padoms": "22 + 12 - nepietiek."},
                {"jaut": "Ar 4 grāmatām cik €?",
                 "atb": ["38"], "padoms": "22 + 16 ≥ 35 ✓."},
            ]),
            pavediens="veikals",
            konteksts="Internetveikali motivē pirkt vairāk ar «bezmaksas "
                      "piegādi no ...» - tā ir nevienādība.",
            kapec="Pārbaude ar robežām apstiprina atbildi."),

    Kopsavilkums([
        "Pārbaudu skaitli intervālā, ārpus tā un robežu.",
        "Atklāju zīmes maiņas kļūdu.",
        "Pārbaudu robežas iekļaušanu.",
        "Pārbaudu sākotnējā nevienādībā.",
    ]),

    Majas([
        "Atrisini un pārbaudi trīs skaitļos: 7 − 2x ≥ 1.",
        "Atrodi kļūdu: −x < 4 ⇒ x < −4.",
        "Aprēķini minimālo pirkumu bezmaksas piegādei.",
    ]),
]
