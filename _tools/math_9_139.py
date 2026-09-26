# -*- coding: utf-8 -*-
"""9. klase, 139. stunda: «Kā atrast locekļu skaitu?»

Pretējais jautājums: zināms pēdējais loceklis vai summa, jāatrod n. No
a_n formulas - lineārs vienādojums; no S_n formulas - kvadrātvienādojums
(saikne ar 9.5. tematu), kur negatīvā sakne neder.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā atrast locekļu skaitu?"

MERKIS = ("Aprēķināsim locekļu skaitu, ja zināma summa vai pēdējais "
          "loceklis.")

SATURS = [
    Sakums("Cik locekļu ir virknē 7, 11, 15, ..., 83?",
           zimejums=restis([["n", "1", "2", "3", "…", "?"],
                            ["aₙ", "7", "11", "15", "…", "83"]]),
           paraksts="7 + (n − 1) · 4 = 83 ⇒ n = 20.",
           fakti=["Pēdējais loceklis dod lineāru vienādojumu.",
                  "Summa dod kvadrātvienādojumu.",
                  "n jābūt naturālam."]),

    Doma("n no pēdējā locekļa vai summas",
         "No a_n: n = {a_n − a_1|d} + 1. No S_n: atrisina kvadrātvienādojumu "
         "un ņem naturālo sakni.",
         soli=[
             "Pieraksti formulu ar zināmajiem.",
             "No a_n - lineārs vienādojums.",
             "No S_n - ievieto a_n = a_1 + (n − 1)d, iegūst kvadrātvienādojumu.",
             "Atmet negatīvās un daļskaitļu saknes.",
         ]),

    Paraugs("No summas",
            uzd="Cik pirmo locekļu progresijā 3, 5, 7, ... jāsaskaita, lai "
                "summa būtu 120?",
            soli=[
                ("S_n = {(2 · 3 + (n − 1) · 2)n|2} = n^2 + 2n", "Formula."),
                ("n^2 + 2n − 120 = 0; D = 484", "Kvadrātvienādojums."),
                ("n = {−2 ± 22|2}: n = 10 (n = −12 neder)", "Naturāla sakne."),
            ],
            atbilde="10 locekļi"),

    Ievadi("Aprēķini n", [
        {"jaut": "5, 8, 11, ..., 62. n = ?", "atb": ["20"],
         "padoms": "57 : 3 + 1."},
        {"jaut": "100, 96, 92, ..., 4. n = ?", "atb": ["25"],
         "padoms": "96 : 4 + 1."},
        {"jaut": "1 + 2 + ... + n = 210. n = ?", "atb": ["20"],
         "padoms": "n^2 + n − 420 = 0."},
        {"jaut": "2 + 4 + 6 + ... (n locekļi) = 110. n = ?", "atb": ["10"],
         "padoms": "n(n + 1) = 110."},
    ]),

    Varianti("Kura sakne der?", [
        {"jaut": "Vienādojuma n^2 + n − 30 = 0 saknes 5 un −6. n = ?",
         "opcijas": ["5", "−6", "abas", "neviena"],
         "pareizi": 0, "padoms": "n ∈ ℕ."},
        {"jaut": "Aprēķins dod n = 12,5. Ko tas nozīmē?",
         "opcijas": ["Precīzi tāda summa nav iespējama", "n = 12",
                     "n = 13", "Kļūda nav iespējama"],
         "pareizi": 0, "padoms": "n jābūt veselam."},
    ]),

    Pasaule("Eksāmens 2025: sešstūru plāksnes",
            Ievadi("", [
                {"jaut": "Figūru virknē 1. figūrai 6 plāksnes, katrai nākamajai "
                         "par 4 vairāk (6, 10, 14, ...). Cik plākšņu 15. "
                         "figūrai?", "atb": ["62"], "padoms": "6 + 14 · 4."},
                {"jaut": "Cik plākšņu vajag visām 15 figūrām kopā?",
                 "atb": ["510"], "padoms": "{(6 + 62) · 15|2}."},
            ]),
            pavediens="maja",
            konteksts="Līdzīgs bija 2025. gada eksāmena 2. daļas 1. uzdevums "
                      "(3 punkti): figūru virkne no sešstūriem.",
            kapec="Figūrā saskata progresiju - tad formula dara pārējo."),

    Kopsavilkums([
        "Atrodu n no pēdējā locekļa.",
        "Atrodu n no summas ar kvadrātvienādojumu.",
        "Izvēlos naturālo sakni.",
    ]),

    Majas([
        "Cik locekļu ir virknē 12, 19, 26, ..., 187?",
        "Cik pirmo naturālo skaitļu summa ir 325?",
        "Uzzīmē figūru virkni no sešstūriem un saskaiti plāksnes.",
    ]),
]
