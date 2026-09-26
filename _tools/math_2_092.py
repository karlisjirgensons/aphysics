# -*- coding: utf-8 -*-
"""2. klase, 92. stunda: «Kas notiek, ja nosacījums izpildās?»

Sazarots algoritms: solis atkarīgs no nosacījuma. Rombā ir jautājums
(«Vai skaitlis ir lielāks nekā 50?»), un atbilde «jā» vai «nē» izvēlas
zaru. Tā darbojas luksofors, termostats un spēles.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, algoritms)

TEMA = "Kas notiek, ja nosacījums izpildās?"

MERKIS = ("Šodien lasīsim un izpildīsim sazarotu algoritmu, kurā solis "
          "atkarīgs no nosacījuma.")

_A = algoritms(["Paņem skaitli",
                ("Vai tas ir lielāks nekā 50?", "Atņem 20", "Pieskaiti 20"),
                "Pieraksti rezultātu"])

SATURS = [
    Sakums("Kā luksofors zina, kad degt zaļajam?",
           zimejums=_A,
           paraksts="Rombā ir jautājums - atbilde izvēlas ceļu.",
           fakti=["Sazarotā algoritmā ir jautājums.",
                  "«Jā» - viens ceļš, «nē» - cits.",
                  "Tā darbojas arī luksofori un spēles."]),

    Doma("Nosacījums",
         "Pēc jautājuma algoritms iet pa vienu no diviem zariem.",
         soli=[
             "Nonāc pie romba un izlasi jautājumu.",
             "Atbildi par savu skaitli: jā vai nē.",
             "Ej pa atbilstošo zaru un izpildi tā soli.",
             "Abi zari satiekas un algoritms turpinās.",
         ]),

    Slidnis("Divi skaitļi - divi ceļi", [
        {"v": "70", "teksts": "Vai 70 > 50? Jā. 70 − 20 = 50."},
        {"v": "30", "teksts": "Vai 30 > 50? Nē. 30 + 20 = 50."},
        {"v": "50", "teksts": "Vai 50 > 50? Nē! 50 + 20 = 70."},
    ], ievads="Seko shēmai stundas sākumā."),

    Ievadi("Izpildi algoritmu", [
        {"jaut": "Skaitlis 80. Rezultāts?", "zim": _A, "atb": ["60"],
         "padoms": "Vai 80 > 50? Jā: − 20."},
        {"jaut": "Skaitlis 15. Rezultāts?", "zim": _A, "atb": ["35"],
         "padoms": "Vai 15 > 50? Nē: + 20."},
        {"jaut": "Skaitlis 51. Rezultāts?", "zim": _A, "atb": ["31"],
         "padoms": "Vai 51 > 50? Jā."},
        {"jaut": "Skaitlis 50. Rezultāts?", "zim": _A, "atb": ["70"],
         "padoms": "50 nav lielāks nekā 50."},
        {"jaut": "Skaitlis 49. Rezultāts?", "zim": _A, "atb": ["69"],
         "padoms": "Nē: + 20."},
        {"jaut": "Skaitlis 99. Rezultāts?", "zim": _A, "atb": ["79"],
         "padoms": "Jā: − 20."},
    ], pamats=4),

    Varianti("Kurš zars?", [
        {"jaut": "Skaitlis 62 - pa kuru zaru?", "zim": _A,
         "opcijas": ["jā", "nē"], "jaukt": False, "pareizi": 0,
         "padoms": "62 > 50."},
        {"jaut": "Skaitlis 50 - pa kuru zaru?", "zim": _A,
         "opcijas": ["jā", "nē"], "jaukt": False, "pareizi": 1,
         "padoms": "50 nav lielāks par sevi."},
    ]),

    Pasaule("Gudrā siltumnīca",
            Ievadi("", [
                {"jaut": "Ja siltumnīcā ir vairāk nekā 25 °C, atver logu, "
                         "citādi - aizver. Ir 28 °C. Raksti 1, ja logu "
                         "atver, 0 - ja aizver.", "atb": ["1"],
                 "padoms": "28 > 25."},
                {"jaut": "Ir 21 °C. Raksti 1 - atver, 0 - aizver.",
                 "atb": ["0"], "padoms": "21 nav vairāk nekā 25."},
            ]),
            zimejums=algoritms(["Nomēri temperatūru",
                                ("Vai vairāk nekā 25 °C?", "Atver logu",
                                 "Aizver logu")]),
            pavediens="tehnika",
            konteksts="Automātiska siltumnīca pati atver un aizver logu.",
            kapec="Datori lēmumus pieņem ar nosacījumiem."),

    Kopsavilkums([
        "Lasu sazarotu algoritmu.",
        "Atbildu uz nosacījumu jā vai nē.",
        "Izpildu atbilstošo zaru.",
    ]),

    Majas([
        "Uzraksti algoritmu: ja līst lietus - ņem lietussargu, citādi - "
        "cepuri.",
        "Uzzīmē to kā shēmu ar rombu.",
        "Izpildi to trīs dienas.",
    ]),
]
