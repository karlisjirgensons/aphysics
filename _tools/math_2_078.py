# -*- coding: utf-8 -*-
"""2. klase, 78. stunda: «Ko rēķina vispirms?»

Darbību secības noteikums 2. klasei: vispirms iekavās, pēc tam no kreisās
uz labo. Tas ir svarīgi arī tad, ja ir tikai «+» un «−»: 20 − 5 + 3 ir 18,
nevis 12.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti)

TEMA = "Ko rēķina vispirms?"

MERKIS = ("Šodien noteiksim darbību secību un aprēķināsim divu darbību "
          "izteiksmes vērtību.")

SATURS = [
    Sakums("20 − 5 + 3 = 12 vai 18?",
           fakti=["No kreisās: 20 − 5 = 15, 15 + 3 = 18.",
                  "12 iznāk, ja vispirms saskaita 5 + 3 - tas ir nepareizi.",
                  "Bez iekavām - vienmēr no kreisās uz labo."]),

    Doma("Darbību secība",
         "Vispirms iekavās, tad no kreisās uz labo.",
         soli=[
             "Vai ir iekavas? Ja jā - izrēķini tās.",
             "Tad izpildi darbības no kreisās uz labo.",
             "Neizvēlies, kuru darbību gribi pirmo.",
             "Pārbaudi ar apmēru.",
         ]),

    Slidnis("Divas izteiksmes, tie paši skaitļi", [
        {"v": "40 − 10 + 5", "teksts": "No kreisās: 30 + 5 = 35."},
        {"v": "40 − (10 + 5)", "teksts": "Iekavās: 15. Tad 40 − 15 = 25."},
        {"v": "35 un 25", "teksts": "Iekavas mainīja secību un rezultātu."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "30 − 10 + 5 = ?", "atb": ["25"], "padoms": "20 + 5."},
        {"jaut": "30 − (10 + 5) = ?", "atb": ["15"], "padoms": "30 − 15."},
        {"jaut": "50 − 20 − 10 = ?", "atb": ["20"], "padoms": "30 − 10."},
        {"jaut": "50 − (20 − 10) = ?", "atb": ["40"], "padoms": "50 − 10."},
        {"jaut": "64 + 16 − 30 = ?", "atb": ["50"], "padoms": "80 − 30."},
        {"jaut": "83 − (40 + 3) = ?", "atb": ["40"], "padoms": "83 − 43."},
    ], pamats=4),

    Varianti("Kurš rēķinājis pareizi?", [
        {"jaut": "45 − 15 + 10. Anna: 40. Toms: 20.",
         "opcijas": ["Anna", "Toms"], "jaukt": False, "pareizi": 0,
         "padoms": "30 + 10."},
        {"jaut": "60 − (25 + 5). Anna: 40. Toms: 30.",
         "opcijas": ["Anna", "Toms"], "jaukt": False, "pareizi": 1,
         "padoms": "60 − 30."},
        {"jaut": "70 − 30 − 20. Anna: 60. Toms: 20.",
         "opcijas": ["Anna", "Toms"], "jaukt": False, "pareizi": 1,
         "padoms": "40 − 20."},
        {"jaut": "36 + (14 − 10). Anna: 40. Toms: 12.",
         "opcijas": ["Anna", "Toms"], "jaukt": False, "pareizi": 0,
         "padoms": "36 + 4."},
    ]),

    Pasaule("Kāpēc noteikums vajadzīgs?",
            Varianti("", [
                {"jaut": "Bija 20 €, iztērēja 5 €, tad dabūja 3 €. Kas "
                         "patiesībā palika?",
                 "opcijas": ["18 €", "12 €"], "jaukt": False, "pareizi": 0,
                 "padoms": "Notikumu secība: − 5, tad + 3."},
            ]),
            pavediens="veikals",
            konteksts="Izteiksme 20 − 5 + 3 apraksta notikumus pēc kārtas.",
            kapec="Ja katrs rēķinātu citā secībā, rezultāti atšķirtos."),

    Kopsavilkums([
        "Vispirms rēķinu iekavās.",
        "Pēc tam no kreisās uz labo.",
        "Zinu, ka secība maina rezultātu.",
    ]),

    Majas([
        "Aprēķini 50 − 10 + 20 un 50 − (10 + 20).",
        "Paskaidro mājiniekam, kāpēc rezultāti atšķiras.",
        "Izdomā vēl vienu šādu pāri.",
    ]),
]
