# -*- coding: utf-8 -*-
"""9. klase, 41. stunda: «Ko nozīmē malu attiecība?»

Katetes nosauc attiecībā pret leņķi: pretkatete stāv pretī α, piekatete
pieskaras α. Trīs attiecības - pretkatete : hipotenūza, piekatete :
hipotenūza, pretkatete : piekatete - nākamajās stundās iegūs vārdus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, restis,
                         taisnlenka)

TEMA = "Ko nozīmē malu attiecība?"

MERKIS = ("Skaidrosim, ka līdzīgos trijstūros atbilstošo malu attiecība "
          "nemainās.")

SATURS = [
    Sakums("Pretkatete un piekatete",
           zimejums=taisnlenka(4, 3, ("pretkatete", "piekatete",
                                      "hipotenūza")),
           paraksts="Nosaukumi atkarīgi no tā, pie kura leņķa stāvi.",
           fakti=["Hipotenūza - pretī taisnajam leņķim.",
                  "Pretkatete - pretī leņķim α.",
                  "Piekatete - pieskaras leņķim α."]),

    Slidnis("Maini skatpunktu", [
        {"v": "Leņķis A", "teksts": "Pie α: pretkatete BC, piekatete AC",
         "zim": taisnlenka(4, 3, ("pretkatete", "piekatete", "c"))},
        {"v": "Leņķis B", "teksts": "Pie β: pretkatete AC, piekatete BC",
         "zim": taisnlenka(4, 3, ("piekatete", "pretkatete", "c"),
                           lenkis=None, otrs="β")},
    ], ievads="Tās pašas katetes - citi nosaukumi."),

    Doma("Trīs attiecības",
         "Katram šaurajam leņķim ir trīs malu attiecības, un tās nemainās, "
         "ja trijstūri palielina.",
         soli=[
             "{pretkatete|hipotenūza}",
             "{piekatete|hipotenūza}",
             "{pretkatete|piekatete}",
         ],
         pieze="Tās ir skaitļi bez mērvienībām, un katram leņķim - savi."),

    Petijums("Mēram un rēķinām", [
        "Uzzīmē leņķi 40° un uz vienas malas trīs punktus 4, 8 un 12 cm "
        "no virsotnes.",
        "No katra punkta novelc perpendikulu līdz otrai malai.",
        "Izmēri katetes un hipotenūzas, aizpildi tabulu.",
        "Aprēķini visas trīs attiecības līdz simtdaļām.",
    ], vajag="transportieris, lineāls, trijstūris, kalkulators",
       secinajums="Visās rindās attiecības sakrīt: 0,64; 0,77; 0,84."),

    Varianti("Nosauc malu", [
        {"jaut": "△ABC, ∠C = 90°. Leņķa A pretkatete ir...",
         "opcijas": ["BC", "AC", "AB", "AC un BC"],
         "pareizi": 0, "padoms": "Pretī virsotnei A."},
        {"jaut": "Leņķa A piekatete ir...",
         "opcijas": ["AC", "BC", "AB", "CB"],
         "pareizi": 0, "padoms": "Iet no A, bet nav hipotenūza."},
        {"jaut": "Leņķa B pretkatete ir...",
         "opcijas": ["AC", "BC", "AB", "Nav"],
         "pareizi": 0, "padoms": "Pretī B."},
        {"jaut": "Kura attiecība vienmēr < 1?",
         "opcijas": ["pretkatete : hipotenūza", "pretkatete : piekatete",
                     "hipotenūza : katete", "neviena"],
         "pareizi": 0, "padoms": "Hipotenūza ir garākā."},
    ]),

    Ievadi("Aprēķini attiecību (katetes 5 un 12, hipotenūza 13)", [
        {"jaut": "Leņķim pretī 5: pretkatete : hipotenūza = ? (daļa)",
         "atb": ["{5|13}", "5/13"], "tastatura": "text",
         "padoms": "5 un 13."},
        {"jaut": "Tam pašam leņķim: pretkatete : piekatete = ?",
         "atb": ["{5|12}", "5/12"], "tastatura": "text",
         "padoms": "5 un 12."},
        {"jaut": "Otram leņķim: piekatete : hipotenūza = ?",
         "atb": ["{5|13}", "5/13"], "tastatura": "text",
         "padoms": "Otram leņķim piekatete ir 5."},
    ]),

    Pasaule("Kāpnes pie sienas",
            Ievadi("", [
                {"jaut": "Drošām kāpnēm augstuma un garuma attiecība ~0,97. "
                         "Kāpnes 4 m garas. Cik augstu tās sniedzas (m)? "
                         "Noapaļo līdz desmitdaļām.",
                 "atb": ["3,9"], "padoms": "0,97 · 4 = 3,88."},
                {"jaut": "Kāpnes 6 m garas - cik augstu (līdz desmitdaļām)?",
                 "atb": ["5,8"], "padoms": "0,97 · 6 = 5,82."},
            ]),
            pavediens="maja",
            konteksts="Kāpnes pie sienas stāv drošā leņķī ap 75° - tad "
                      "augstums : garums ir apmēram 0,97.",
            kapec="Viena attiecība der jebkura garuma kāpnēm.",
            zimejums=restis([["garums, m", "4", "6"],
                             ["augstums, m", None, None]])),

    Kopsavilkums([
        "Nosaucu pretkateti, piekateti un hipotenūzu.",
        "Aprēķinu trīs malu attiecības.",
        "Zinu, ka attiecības atkarīgas tikai no leņķa.",
    ]),

    Majas([
        "Pabeidz tabulu ar mērījumiem leņķim 40°.",
        "Atkārto mērījumus leņķim 60°.",
        "Trijstūrī 8, 15, 17 aprēķini visas attiecības abiem šaurajiem "
        "leņķiem.",
    ]),
]
