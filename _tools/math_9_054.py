# -*- coding: utf-8 -*-
"""9. klase, 54. stunda: «Cik stāvs ir nogāzes slīpums?»

Slīpumu dzīvē mēra trīs veidos: grādos, procentos (tg · 100) un attiecībā
(1 : 12). Stundā skolēns pārvērš vienu citā un risina uzdevumus par
ceļiem, rampām un kalniem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Pasaule,
                         Sakums, Slidnis, Varianti, taisnlenka)

TEMA = "Cik stāvs ir nogāzes slīpums?"

MERKIS = ("Risināsim praktisku uzdevumu par slīpumu, augstumu vai attālumu.")

SATURS = [
    Sakums("Kāpums 100 % - vai tas ir vertikāli?",
           zimejums=taisnlenka(5, 5, ("100 m", "100 m", None), "45°"),
           paraksts="100 % nozīmē: 100 m uz augšu uz 100 m uz priekšu.",
           fakti=["Slīpums % = tg α · 100.",
                  "100 % = 45°, nevis 90°.",
                  "Stāvākās ielas pasaulē ir ap 35 % kāpumā."]),

    Slidnis("Grādi, procenti, attiecība", [
        {"v": "5 %", "teksts": "tg α = 0,05 → α ≈ 2,9° (1 : 20)",
         "zim": taisnlenka(10, 1.5, ("5", "100", None), "α")},
        {"v": "20 %", "teksts": "tg α = 0,2 → α ≈ 11,3° (1 : 5)",
         "zim": taisnlenka(10, 2, ("20", "100", None), "α")},
        {"v": "58 %", "teksts": "tg α ≈ 0,58 → α ≈ 30°",
         "zim": taisnlenka(10, 5.8, ("58", "100", None), "α")},
    ], ievads="Viens un tas pats slīpums trīs pierakstos."),

    Doma("Slīpuma pieraksti",
         "Slīpums = {pacēlums|horizontālais attālums} = tg α; procentos - "
         "reizina ar 100.",
         soli=[
             "No procentiem: tg α = p : 100, tad SHIFT tan.",
             "No grādiem: p = tg α · 100.",
             "Attiecība 1 : n nozīmē tg α = {1|n}.",
             "Ceļa garums pa slīpumu - hipotenūza: c = {h|sin α}.",
         ]),

    Ievadi("Pārvērš", [
        {"jaut": "Kāpums 10 %. Leņķis līdz desmitdaļām?", "atb": ["5,7"],
         "padoms": "tg α = 0,1."},
        {"jaut": "Leņķis 20°. Kāpums % līdz veseliem?", "atb": ["36"],
         "padoms": "tg 20° ≈ 0,364."},
        {"jaut": "Slīpums 1 : 12. Kāpums % līdz desmitdaļām?",
         "atb": ["8,3"], "padoms": "1 : 12 = 0,0833."},
        {"jaut": "Kāpums 25 %. Cik m pacēlums uz 80 m horizontāli?",
         "atb": ["20"], "padoms": "80 · 0,25."},
    ]),

    Varianti("Kurš stāvāks?", [
        {"jaut": "15 % vai 10°?",
         "opcijas": ["10° (≈ 17,6 %)", "15 %", "vienādi", "nevar zināt"],
         "pareizi": 0, "padoms": "tg 10° ≈ 0,176."},
        {"jaut": "1 : 8 vai 12 %?",
         "opcijas": ["1 : 8 (12,5 %)", "12 %", "vienādi", "nevar zināt"],
         "pareizi": 0, "padoms": "1 : 8 = 0,125."},
    ]),

    Pasaule("Funikulārs",
            Kustiba("", [
                {"jaut": "Trase paceļas 120 m, slīpums 30°. Cik m garš ir "
                         "sliežu ceļš?",
                 "atb": 240, "beigas": 300, "iedala": 50, "mers": "m",
                 "merkis": "augšā", "objekts": "Vagons",
                 "padoms": "120 : sin 30°."},
                {"jaut": "Cik m horizontāli tas aizņem? (cos 30° ≈ 0,866, "
                         "līdz veseliem)",
                 "atb": 208, "beigas": 300, "iedala": 50, "mers": "m",
                 "merkis": "kalna pakāje", "objekts": "Vagons",
                 "padoms": "240 · 0,866 = 207,8."},
            ]),
            pavediens="celojums",
            konteksts="Kalnu pilsētās vagoniņi pa sliedēm brauc uz augšu pa "
                      "stāvu nogāzi.",
            kapec="Augstums un leņķis dod sliežu garumu."),

    Kopsavilkums([
        "Pārvēršu slīpumu grādos, procentos un attiecībā.",
        "Aprēķinu pacēlumu vai ceļa garumu.",
        "Salīdzinu slīpumus.",
    ]),

    Majas([
        "Atrodi tuvākās ielas vai rampas slīpumu (mēri augstumu un garumu).",
        "Pārvērš 7 % grādos un 15° procentos.",
        "Uzzīmē tabulu: 5 %, 10 %, 20 %, 50 %, 100 % - grādos.",
    ]),
]
