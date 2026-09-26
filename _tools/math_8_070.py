# -*- coding: utf-8 -*-
"""8. klase, 70. stunda: «Kā rodas riņķa laukuma formula?»

Riņķi sagriež sektoros un saliek joslā - puse ar loku uz leju, puse uz
augšu. Jo vairāk sektoru, jo josla vairāk līdzinās taisnstūrim πr × r.
Slīdnis rāda 4, 8, 16 un 32 sektorus (rinka_sektori).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, rinka_sektori)

TEMA = "Kā rodas riņķa laukuma formula?"

MERKIS = ("Paskaidrosim riņķa laukuma formulu, izmantojot riņķa sadalīšanu "
          "sektoros.")

SATURS = [
    Sakums("Kā riņķi pārvērst taisnstūrī?",
           zimejums=rinka_sektori(16),
           paraksts="16 sektori, salikti joslā, - gandrīz taisnstūris πr × r.",
           fakti=["Riņķa līnijas garums ir C = 2πr.",
                  "Joslas garums ≈ puse riņķa līnijas (πr), augstums - r.",
                  "Tātad S = πr · r = πr^2."]),

    Slidnis("Vairāk sektoru - taisnākas malas", [
        {"v": "4 sektori", "teksts": "Josla vēl ļoti izliekta",
         "zim": rinka_sektori(4)},
        {"v": "8 sektori", "teksts": "Malas kļūst taisnākas",
         "zim": rinka_sektori(8)},
        {"v": "16 sektori", "teksts": "Gandrīz paralelograms",
         "zim": rinka_sektori(16)},
        {"v": "32 sektori", "teksts": "Praktiski taisnstūris πr × r",
         "zim": rinka_sektori(32)},
    ]),

    Doma("Riņķa laukums",
         "S = πr^2 - rādiusa kvadrāts, reizināts ar π.",
         soli=[
             "Sadala riņķi daudzos vienādos sektoros.",
             "Pusi sektoru liek ar loku uz leju, pusi - ar loku uz augšu.",
             "Josla kļūst par taisnstūri: garums πr, augstums r.",
             "S = πr · r = πr^2.",
         ],
         pieze="Ja dots diametrs, vispirms atrod rādiusu: r = {d|2}."),

    Paraugs("Aprēķini laukumu",
            uzd="Riņķa rādiuss ir 5 cm. Aprēķini laukumu (π ≈ 3,14).",
            soli=[
                ("S = πr^2 = π · 5^2", "Formula."),
                ("S = 25π", "Precīzi."),
                ("S ≈ 25 · 3,14 = 78,5 cm²", "Aptuveni."),
            ],
            atbilde="25π ≈ 78,5 cm²"),

    Ievadi("Aprēķini (π ≈ 3,14)", [
        {"jaut": "r = 10 cm. S (cm²)?", "atb": ["314"],
         "padoms": "100 · 3,14."},
        {"jaut": "r = 2 m. S (m²)?", "atb": ["12,56"], "padoms": "4 · 3,14."},
        {"jaut": "d = 6 dm. S (dm²)?", "atb": ["28,26"],
         "padoms": "r = 3; 9 · 3,14."},
        {"jaut": "r = 7. S = ?π", "atb": ["49"], "padoms": "7^2."},
        {"jaut": "d = 20. S = ?π", "atb": ["100"], "padoms": "r = 10."},
        {"jaut": "r = 0,1 m. S (m²)?", "atb": ["0,0314"],
         "padoms": "0,01 · 3,14."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Kā mainās laukums, ja rādiusu divkāršo?",
         "opcijas": ["Četrkāršojas", "Divkāršojas", "Nemainās",
                     "Palielinās par 2"],
         "pareizi": 0, "padoms": "(2r)^2 = 4r^2."},
        {"jaut": "Kas iznāk no joslas, ja sektoru ir ļoti daudz?",
         "opcijas": ["Taisnstūris πr × r", "Kvadrāts r × r", "Trijstūris",
                     "Riņķis"],
         "pareizi": 0, "padoms": "Skaties slīdni."},
        {"jaut": "Riņķa ar d = 10 laukums:",
         "opcijas": ["25π", "100π", "10π", "5π"],
         "pareizi": 0, "padoms": "r = 5."},
    ]),

    Pasaule("Kura pica izdevīgāka?",
            Ievadi("", [
                {"jaut": "Picas diametrs 30 cm. Laukums (cm², π ≈ 3,14)?",
                 "atb": ["706,5"], "padoms": "15^2 · 3,14."},
                {"jaut": "Picas diametrs 40 cm. Laukums (cm²)?",
                 "atb": ["1256"], "padoms": "20^2 · 3,14."},
                {"jaut": "Cik reizes lielā pica lielāka par mazo (līdz "
                         "simtdaļām)?",
                 "atb": ["1,78"], "padoms": "1256 : 706,5."},
            ]),
            pavediens="virtuve",
            konteksts="Picas izmēru raksta ar diametru, bet ēdiena daudzumu "
                      "nosaka laukums.",
            kapec="Diametrs lielāks par trešdaļu, bet picas - gandrīz divreiz "
                  "vairāk."),

    Kopsavilkums([
        "Paskaidroju, kā no sektoriem rodas S = πr^2.",
        "Aprēķinu riņķa laukumu pēc rādiusa vai diametra.",
        "Zinu, ka divkāršs rādiuss dod četrkāršu laukumu.",
    ]),

    Majas([
        "Izgriez papīra riņķi, sagriez 16 sektoros un saliec joslu.",
        "Izmēri šķīvja diametru un aprēķini tā laukumu.",
        "Salīdzini divu picu izmērus un cenas picērijas ēdienkartē.",
    ]),
]
