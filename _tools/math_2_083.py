# -*- coding: utf-8 -*-
"""2. klase, 83. stunda: «Kā pārbaudīt otra darbu?»

Mikrotemata noslēgums pārī: katrs izveido izteiksmes, apmainās, aprēķina un
izskaidro, kādā secībā rēķināja. Pārbaudot citu, skolēns vēlreiz izsaka
noteikumu vārdos - tas nostiprina vairāk nekā vēl viens piemērs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti)

TEMA = "Kā pārbaudīt otra darbu?"

MERKIS = ("Šodien pārī apmainīsimies ar izteiksmēm, aprēķināsim tās un "
          "izskaidrosim savu darbību secību.")

SATURS = [
    Sakums("Kā labs pārbaudītājs atrod kļūdu?",
           fakti=["Viņš pārrēķina pats un salīdzina.",
                  "Pārbauda darbību secību.",
                  "Pasaka, kur kļūda, nevis tikai «nepareizi»."]),

    Doma("Pārbaudītāja soļi",
         "Pārbaudi secību, katru starprezultātu un vērtību.",
         soli=[
             "Vai ir iekavas? Vai tās izrēķinātas pirmās?",
             "Vai pārējās darbības no kreisās uz labo?",
             "Vai katrs starprezultāts ir pareizs?",
             "Ja atrodi kļūdu - pasaki, kurā solī.",
         ]),

    Varianti("Kurā solī kļūda?", [
        {"jaut": "70 − (15 + 25) = 70 − 30 = 40",
         "opcijas": ["1. solī: 15 + 25 = 40", "2. solī", "kļūdas nav"],
         "pareizi": 0, "padoms": "15 + 25 nav 30."},
        {"jaut": "48 + 12 − 20 = 60 − 20 = 30",
         "opcijas": ["2. solī: 60 − 20 = 40", "1. solī", "kļūdas nav"],
         "pareizi": 0, "padoms": "60 − 20 nav 30."},
        {"jaut": "55 − 15 + 10 = 55 − 25 = 30",
         "opcijas": ["Nepareiza secība", "1. solī", "kļūdas nav"],
         "pareizi": 0, "padoms": "No kreisās: 40 + 10 = 50."},
        {"jaut": "90 − (40 + 20) = 90 − 60 = 30",
         "opcijas": ["kļūdas nav", "1. solī", "2. solī"], "pareizi": 0,
         "padoms": "Viss pareizi."},
    ]),

    Petijums("Apmaiņa pārī", [
        "Katrs uzraksta 3 izteiksmes: vienu ar iekavām.",
        "Apmainieties ar burtnīcām.",
        "Aprēķiniet ar starprezultātiem.",
        "Salīdziniet un izstāstiet savu secību.",
    ], vajag="burtnīca"),

    Ievadi("Aprēķini pats", [
        {"jaut": "70 − (15 + 25) = ?", "atb": ["30"], "padoms": "70 − 40."},
        {"jaut": "55 − 15 + 10 = ?", "atb": ["50"], "padoms": "40 + 10."},
        {"jaut": "48 + 12 − 20 = ?", "atb": ["40"], "padoms": "60 − 20."},
        {"jaut": "100 − (55 − 5) = ?", "atb": ["50"], "padoms": "100 − 50."},
    ]),

    Pasaule("Robots-skolotājs",
            Varianti("", [
                {"jaut": "Robots pārbauda: «36 + 24 − 10 = 50». Ko tas "
                         "atbildēs?", "opcijas": ["Pareizi", "Nepareizi"],
                 "jaukt": False, "pareizi": 0, "padoms": "60 − 10."},
                {"jaut": "Robots pārbauda: «80 − (30 + 10) = 60». Ko "
                         "atbildēs?", "opcijas": ["Pareizi", "Nepareizi"],
                 "jaukt": False, "pareizi": 1, "padoms": "80 − 40 = 40."},
            ]),
            pavediens="tehnika",
            konteksts="Mācību programmas pārbauda atbildes automātiski.",
            kapec="Arī robotam jāzina darbību secība."),

    Kopsavilkums([
        "Pārbaudu klasesbiedra aprēķinu.",
        "Atrodu, kurā solī ir kļūda.",
        "Izskaidroju savu darbību secību.",
    ]),

    Majas([
        "Uzraksti mājiniekam 3 izteiksmes.",
        "Pārbaudi viņa atbildes.",
        "Ja ir kļūda, parādi, kurā solī.",
    ]),
]
