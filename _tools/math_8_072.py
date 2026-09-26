# -*- coding: utf-8 -*-
"""8. klase, 72. stunda: «Kā atrast rādiusu?»

Apgrieztais uzdevums: no C = 2πr iegūst r = {C|2π}, no S = πr^2 - r^2 un
tad kvadrātsakni (55. stunda). Negatīvo sakni atmet, jo rādiuss ir garums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, rinkis)

TEMA = "Kā atrast rādiusu?"

MERKIS = ("Aprēķināsim rādiusu vai diametru, ja zināms laukums vai riņķa "
          "līnijas garums.")

SATURS = [
    Sakums("Laukums 49π cm² - cik liels ir rādiuss?",
           zimejums=rinkis(radiuss="r = ?"),
           paraksts="S = 49π, tātad r^2 = 49 un r = 7 cm.",
           fakti=["No C = 2πr izriet r = {C|2π}.",
                  "No S = πr^2 izriet r^2 = {S|π}; tad velk sakni.",
                  "Rādiuss ir garums - negatīvo sakni atmet."]),

    Doma("Atpakaļ no rezultāta",
         "Formulu lasa otrādi: zināms rezultāts, jāatrod rādiuss.",
         soli=[
             "Pieraksti formulu un ievieto zināmo lielumu.",
             "Izsaki r vai r^2.",
             "Ja iegūts r^2, velc kvadrātsakni.",
             "Diametrs ir d = 2r.",
         ]),

    Paraugs("No laukuma",
            uzd="Riņķa laukums ir 78,5 cm² (π ≈ 3,14). Atrodi rādiusu un "
                "riņķa līnijas garumu.",
            soli=[
                ("3,14 · r^2 = 78,5", "Ievieto."),
                ("r^2 = 25", "78,5 : 3,14."),
                ("r = 5 cm", "Pozitīvā sakne."),
                ("C = 2 · 3,14 · 5 = 31,4 cm", "Riņķa līnija."),
            ],
            atbilde="5 cm; 31,4 cm"),

    Ievadi("Atrodi", [
        {"jaut": "S = 64π. r = ?", "atb": ["8"], "padoms": "r^2 = 64."},
        {"jaut": "C = 18π. r = ?", "atb": ["9"], "padoms": "{18|2}."},
        {"jaut": "C = 31,4 cm (π ≈ 3,14). d (cm)?", "atb": ["10"],
         "padoms": "d = {C|π}."},
        {"jaut": "S = 12,56 cm² (π ≈ 3,14). r (cm)?", "atb": ["2"],
         "padoms": "r^2 = 4."},
        {"jaut": "S = 100π. d = ?", "atb": ["20"], "padoms": "r = 10."},
        {"jaut": "C = 44 cm (π ≈ {22|7}). r (cm)?", "atb": ["7"],
         "padoms": "2 · {22|7} · r = 44."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "S = 36π. r = ?",
         "opcijas": ["6", "18", "36", "12"],
         "pareizi": 0, "padoms": "√36."},
        {"jaut": "Riņķa līnija kļūst 2 reizes garāka. Laukums kļūst...",
         "opcijas": ["4 reizes lielāks", "2 reizes lielāks", "tāds pats",
                     "8 reizes lielāks"],
         "pareizi": 0, "padoms": "Rādiuss divkāršojas."},
        {"jaut": "S = 9π. Tad C = ?",
         "opcijas": ["6π", "9π", "3π", "18π"],
         "pareizi": 0, "padoms": "r = 3; C = 2π · 3."},
    ]),

    Pasaule("Mežsarga mērlente",
            Ievadi("", [
                {"jaut": "Koka apkārtmērs ir 157 cm (π ≈ 3,14). Diametrs "
                         "(cm)?",
                 "atb": ["50"], "padoms": "157 : 3,14."},
                {"jaut": "Stumbra šķērsgriezuma laukums (cm²)?",
                 "atb": ["1962,5"], "padoms": "25^2 · 3,14."},
                {"jaut": "Cik m² tas ir (līdz simtdaļām)?",
                 "atb": ["0,2", "0,20"], "padoms": "1 m² = 10 000 cm²."},
            ]),
            pavediens="daba",
            konteksts="Mežsargs apņem koku ar mērlenti un no apkārtmēra "
                      "aprēķina diametru un koksnes daudzumu.",
            kapec="Apkārtmēru izmērīt var, diametru - ne: koks ir priekšā."),

    Kopsavilkums([
        "Atrodu rādiusu no riņķa līnijas garuma.",
        "Atrodu rādiusu no laukuma, izvelkot kvadrātsakni.",
        "Pāreju no rādiusa uz diametru un otrādi.",
    ]),

    Majas([
        "Ar diegu izmēri koka vai burkas apkārtmēru un aprēķini diametru.",
        "Riņķa laukums ir 1 m². Aprēķini rādiusu līdz cm.",
        "Paskaidro, kāpēc rādiusam atmet negatīvo sakni.",
    ]),
]
