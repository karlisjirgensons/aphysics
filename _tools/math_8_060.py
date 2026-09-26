# -*- coding: utf-8 -*-
"""8. klase, 60. stunda: «Kā saskaitīt līdzīgas saknes?»

Līdzīgas saknes saskaita kā līdzīgus saskaitāmos: 2√3 + 5√3 = 7√3, tāpat
kā 2 āboli + 5 āboli. Nelīdzīgas saknes kļūst līdzīgas pēc iznešanas
(√8 = 2√2), bet √2 + √3 paliek summa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā saskaitīt līdzīgas saknes?"

MERKIS = "Saskaitīsim un atņemsim līdzīgas kvadrātsaknes un pamatosim darbību."

SATURS = [
    Sakums("2√3 + 5√3 = ?",
           zimejums=restis([["2√3", "+", "5√3", "=", "7√3"],
                            ["2 āboli", "+", "5 āboli", "=", "7 āboli"]]),
           paraksts="√3 ir kā mērvienība - saskaita, cik to ir.",
           fakti=["Līdzīgām saknēm ir vienāds zemsaknes skaitlis.",
                  "√2 + √3 nav √5 - tās nav līdzīgas.",
                  "Pēc iznešanas saknes var kļūt līdzīgas: √8 = 2√2."]),

    Doma("Līdzīgas saknes",
         "a√c + b√c = (a + b)√c - saskaita skaitļus pirms saknes.",
         soli=[
             "Vienkāršo katru sakni: iznes reizinātājus.",
             "Sagrupē līdzīgās saknes.",
             "Saskaita koeficientus, sakni pārraksta.",
         ],
         pieze="Nelīdzīgas saknes paliek kā summa: 3√2 + 4√5 vairs "
               "nevienkāršo."),

    Paraugs("Vispirms iznes",
            uzd="Vienkāršo √12 + √27 − √48.",
            soli=[
                ("√12 = 2√3; √27 = 3√3; √48 = 4√3", "Iznes reizinātājus."),
                ("2√3 + 3√3 − 4√3", "Tagad saknes ir līdzīgas."),
                ("= (2 + 3 − 4)√3 = √3", "Saskaita koeficientus."),
            ],
            atbilde="√3"),

    Ievadi("Ieraksti koeficientu", [
        {"jaut": "4√5 + 3√5 = ?√5", "atb": ["7"], "padoms": "4 + 3."},
        {"jaut": "9√2 − 11√2 = ?√2", "atb": ["−2", "-2"],
         "padoms": "9 − 11."},
        {"jaut": "√50 + √8 = ?√2", "atb": ["7"], "padoms": "5√2 + 2√2."},
        {"jaut": "√75 − √12 = ?√3", "atb": ["3"], "padoms": "5√3 − 2√3."},
        {"jaut": "2√18 + √32 = ?√2", "atb": ["10"], "padoms": "6√2 + 4√2."},
        {"jaut": "3√20 − √45 = ?√5", "atb": ["3"], "padoms": "6√5 − 3√5."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "√2 + √2 = ?",
         "opcijas": ["2√2", "√4", "2", "4"],
         "pareizi": 0, "padoms": "Divas vienādas saknes."},
        {"jaut": "√3 + √12 = ?",
         "opcijas": ["3√3", "√15", "2√3", "4√3"],
         "pareizi": 0, "padoms": "√12 = 2√3."},
        {"jaut": "Kuras saknes ir līdzīgas?",
         "opcijas": ["√8 un √18", "√8 un √12", "√2 un √3", "√5 un √10"],
         "pareizi": 0, "padoms": "2√2 un 3√2."},
    ]),

    Pasaule("Divas dobes",
            Ievadi("", [
                {"jaut": "Kvadrātveida dobes laukums ir 8 m². Mala = ?√2 m",
                 "atb": ["2"], "padoms": "8 = 4 · 2."},
                {"jaut": "Otras kvadrātveida dobes laukums ir 18 m². "
                         "Mala = ?√2 m",
                 "atb": ["3"], "padoms": "18 = 9 · 2."},
                {"jaut": "Dobes ir blakus, malas vienā rindā. Kopējais "
                         "garums = ?√2 m",
                 "atb": ["5"], "padoms": "2√2 + 3√2."},
                {"jaut": "Cik m tas ir aptuveni (līdz desmitdaļām)?",
                 "atb": ["7,1"], "padoms": "5 · 1,414 = 7,07."},
            ]),
            pavediens="maja",
            konteksts="Kvadrātveida dobes mala ir laukuma sakne. Līdzīgas "
                      "saknes saskaita kā parastus garumus.",
            kapec="Precīzi saskaita, un noapaļo tikai beigās."),

    Kopsavilkums([
        "Atpazīstu līdzīgas saknes.",
        "Saskaitu un atņemu līdzīgas saknes.",
        "Pirms saskaitīšanas iznesu reizinātājus.",
    ]),

    Majas([
        "Vienkāršo: √8 + √50 − √18; √27 + √300.",
        "Paskaidro, kāpēc √2 + √3 nav √5 (pārbaudi ar kalkulatoru).",
        "Izdomā piemēru, kur trīs dažādas saknes kļūst līdzīgas.",
    ]),
]
