# -*- coding: utf-8 -*-
"""9. klase, 31. stunda: «Kā aprēķināt laukumu?»

Formula abos virzienos: no pamatiem un augstuma - laukums, no laukuma -
augstums vai pamats. Tieši šāds bija 2025. gada eksāmena 21. uzdevums
(DE = 5, CF = 14, S = 57, jāatrod augstums).
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Kustiba,
                         Majas, Paraugs, Pasaule, Sakums, Varianti,
                         geometrija, trapece)

TEMA = "Kā aprēķināt laukumu?"

MERKIS = ("Aprēķināsim trapeces laukumu un nezināmos lielumus, ja laukums "
          "zināms.")

SATURS = [
    Sakums("Laukums 57 cm² - cik augsta trapece?",
           zimejums=geometrija(trapece(14, 5, 6, nobide=3, pedas=True)[:5],
                               nogriezni=TRAPECES_MALAS + ["DH"],
                               taisni=["DHB"],
                               malas=[("AB", "14"), ("DC", "5"),
                                      ("DH", "h")]),
           paraksts="Eksāmens 2025: {14 + 5|2} · h = 57.",
           fakti=["9,5 · h = 57.",
                  "h = 57 : 9,5 = 6 cm.",
                  "Formulu lieto arī «otrādi»."]),

    Doma("No laukuma atpakaļ",
         "S = {a + b|2} · h ⇒ h = {2S|a + b} un a + b = {2S|h}.",
         soli=[
             "Pieraksti formulu ar zināmajiem skaitļiem.",
             "Aprēķini, kas zināms (pamatu pussumma vai augstums).",
             "Atrisini vienādojumu.",
             "Pārbaudi, ievietojot atpakaļ.",
         ]),

    Paraugs("Pamats no laukuma",
            uzd="Trapeces laukums 60 cm², augstums 5 cm, viens pamats 15 cm. "
                "Atrodi otru pamatu.",
            soli=[
                ("{15 + b|2} · 5 = 60", "Formula."),
                ("15 + b = 24", "Abas puses · 2 : 5."),
                ("b = 9", "Pārbaude: 12 · 5 = 60."),
            ],
            atbilde="9 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "a = 12, b = 8, h = 7. S = ?", "atb": ["70"],
         "padoms": "10 · 7."},
        {"jaut": "S = 45, a = 11, b = 7. h = ?", "atb": ["5"],
         "padoms": "9 · h = 45."},
        {"jaut": "S = 36, h = 4, a = 12. b = ?", "atb": ["6"],
         "padoms": "a + b = 18."},
        {"jaut": "S = 50, m = 10. h = ?", "atb": ["5"],
         "padoms": "S = m · h."},
        {"jaut": "a = 2,4 m, b = 1,6 m, h = 0,5 m. S = ? m²", "atb": ["1"],
         "padoms": "2 · 0,5."},
        {"jaut": "S = 84, h = 7, a − b = 4. a = ?", "atb": ["14"],
         "padoms": "a + b = 24."},
    ], pamats=4),

    Varianti("Biežākā kļūda", [
        {"jaut": "Vienādsānu trapecē a = 10, b = 4, sānu mala 5. Skolēns: "
                 "S = 7 · 5 = 35. Kur kļūda?",
         "opcijas": ["Sānu mala nav augstums; h = 4, S = 28",
                     "Nav kļūdas", "Jādala ar 4", "Jāņem a · b"],
         "pareizi": 0, "padoms": "Augstums ⊥ pamatiem: √(25 − 9) = 4."},
        {"jaut": "S = {a + b|2} · h. Ja h dubulto, S...",
         "opcijas": ["dubultojas", "četrkāršojas", "nemainās",
                     "samazinās"],
         "pareizi": 0, "padoms": "Tieši proporcionāls h."},
    ]),

    Pasaule("Krāsojam garāžas sienu",
            Kustiba("", [
                {"jaut": "Garāžas sānu siena - trapece: apakšā 6 m, augšā 4 m, "
                         "augstums 2,5 m. Cik m² jākrāso?",
                 "atb": 12.5, "beigas": 20, "iedala": 2.5, "mers": "m²",
                 "merkis": "siena", "objekts": "Rullis",
                 "padoms": "5 · 2,5."},
                {"jaut": "1 litrs krāsas pietiek 5 m². Cik litru divām sienām?",
                 "atb": 5, "beigas": 10, "iedala": 1, "mers": "l",
                 "merkis": "krāsa", "objekts": "Kanna",
                 "padoms": "25 : 5."},
            ]),
            pavediens="maja",
            konteksts="Garāžai ar slīpu jumtu sānu sienas ir trapeces.",
            kapec="Krāsu pērk pēc laukuma - trapeces formula ietaupa naudu."),

    Kopsavilkums([
        "Aprēķinu trapeces laukumu.",
        "No laukuma aprēķinu augstumu vai pamatu.",
        "Nejaucu sānu malu ar augstumu.",
    ]),

    Majas([
        "Izmēri kādu trapeces formas virsmu mājās un aprēķini laukumu.",
        "S = 90 cm², pamati 13 un 17 cm. Atrodi augstumu.",
        "Izveido pats eksāmena stila uzdevumu ar laukumu.",
    ]),
]
