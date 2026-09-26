# -*- coding: utf-8 -*-
"""9. klase, 30. stunda: «Kā rodas trapeces laukuma formula?»

Trīs ceļi uz vienu formulu: divi trijstūri (diagonāle), divas trapeces
kopā - paralelograms, un taisnstūris ar viduslīnijas platumu. Visi dod
S = {a + b|2} · h. Eksāmena formulu lapā tās nav - to jāzina pašam.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija,
                         trapece)

TEMA = "Kā rodas trapeces laukuma formula?"

MERKIS = ("Iegūsim trapeces laukuma formulu, izmantojot jau zināmo par "
          "laukumu.")

_T = trapece(10, 4, 4, nobide=2)

# Divas vienādas trapeces: otrā apgriezta un pielikta pie BC - paralelograms.
_PARALELOGRAMS = geometrija(
    _T + [("E", 14, 0), ("F", 16, 4)],
    nogriezni=["AE", "EF", "FD", "DA", "BC"],
    iekrasot=[("ABCD", 0), ("BEFC", 1)],
    malas=[("AB", "a"), ("BE", "b"), ("DC", "b"), ("CF", "a")])

SATURS = [
    Sakums("Divas trapeces - viens paralelograms",
           zimejums=_PARALELOGRAMS,
           paraksts="Paralelograma pamats a + b, augstums h.",
           fakti=["Paralelograma laukums: (a + b) · h.",
                  "Viena trapece ir puse no tā.",
                  "S = {a + b|2} · h."]),

    Slidnis("Trīs ceļi uz formulu", [
        {"v": "Diagonāle", "teksts": "S = {a · h|2} + {b · h|2} = "
                                     "{a + b|2} · h",
         "zim": geometrija(_T, nogriezni=TRAPECES_MALAS + ["AC"],
                           iekrasot=[("ABC", 0), ("ACD", 1)])},
        {"v": "Divas trapeces", "teksts": "Paralelograms (a + b) · h, puse "
                                          "no tā",
         "zim": _PARALELOGRAMS},
        {"v": "Viduslīnija", "teksts": "S = m · h - kā taisnstūrim ar malu m",
         "zim": geometrija(trapece(10, 4, 4, nobide=2, viduspunkti=True),
                           nogriezni=TRAPECES_MALAS, izcelti=["MN"])},
    ]),

    Doma("Trapeces laukums",
         "S = {a + b|2} · h = m · h, kur a un b - pamati, h - augstums, "
         "m - viduslīnija.",
         soli=[
             "Pamatu summu dala ar 2 (vai ņem viduslīniju).",
             "Reizina ar augstumu - NEVIS ar sānu malu.",
             "Mērvienības: cm · cm = cm².",
         ]),

    Varianti("Kurš ceļš ir pareizs?", [
        {"jaut": "Ar diagonāli trapece sadalās...",
         "opcijas": ["divos trijstūros ar vienu augstumu h",
                     "divos taisnstūros", "četros trijstūros",
                     "paralelogramā"],
         "pareizi": 0, "padoms": "Abiem trijstūriem augstums ir h."},
        {"jaut": "Ja trapecei b = 0, formula dod...",
         "opcijas": ["trijstūra laukumu {a · h|2}", "0", "taisnstūri",
                     "neko"],
         "pareizi": 0, "padoms": "Augšējais pamats sarūk punktā."},
        {"jaut": "Ja b = a, formula dod...",
         "opcijas": ["paralelograma laukumu a · h", "2a · h",
                     "trijstūri", "0"],
         "pareizi": 0, "padoms": "{a + a|2} = a."},
    ]),

    Ievadi("Pirmie aprēķini", [
        {"jaut": "a = 10, b = 4, h = 4. S = ?", "atb": ["28"],
         "padoms": "7 · 4."},
        {"jaut": "a = 9, b = 5, h = 3. S = ?", "atb": ["21"],
         "padoms": "7 · 3."},
        {"jaut": "m = 6, h = 5. S = ?", "atb": ["30"], "padoms": "m · h."},
        {"jaut": "a = 7,5, b = 2,5, h = 2. S = ?", "atb": ["10"],
         "padoms": "5 · 2."},
    ]),

    Pasaule("Dambja šķērsgriezums",
            Ievadi("", [
                {"jaut": "Dambis apakšā 40 m, augšā 8 m, augstums 12 m. "
                         "Šķērsgriezuma laukums (m²)?", "atb": ["288"],
                 "padoms": "24 · 12."},
                {"jaut": "Dambis 200 m garš. Cik m³ zemes tajā?",
                 "atb": ["57600", "57 600"], "padoms": "288 · 200."},
            ]),
            pavediens="planeta",
            konteksts="Dambja apjomu inženieri rēķina: šķērsgriezuma laukums "
                      "reiz garums.",
            kapec="Trapeces laukums ir pirmais solis tilpumam."),

    Kopsavilkums([
        "Iegūstu trapeces laukuma formulu trīs veidos.",
        "Zinu S = {a + b|2} · h = m · h.",
        "Pārbaudu formulu robežgadījumos.",
    ]),

    Majas([
        "Izgriez divas vienādas trapeces un saliec paralelogramu.",
        "Uzzīmē trapeci rūtiņās, saskaiti rūtiņas un salīdzini ar formulu.",
        "Aprēķini: a = 13 cm, b = 7 cm, h = 6 cm.",
    ]),
]
