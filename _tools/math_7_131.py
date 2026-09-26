# -*- coding: utf-8 -*-
"""7. klase, 131. stunda: «Ko nozīmē atrisināt vienādojumu?»

Atrisināt vienādojumu nozīmē atrast visas tā saknes un pamatot, ka citu
nav. Vienādojumam var būt viena sakne, vairākas, neviena vai bezgalīgi
daudz. Minēšana atrod sakni, bet nepamato, ka citu nav.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Ko nozīmē atrisināt vienādojumu?"

MERKIS = ("Paskaidrosim, ka jāatrod visas saknes un jāpamato, ka citu "
          "nav.")

SATURS = [
    Sakums("x² = 9. Atbilde «3» - pilnīga?",
           zimejums=restis([["x", "−3", "0", "3"],
                            ["x²", "9", "0", "9"]]),
           paraksts="Arī −3 ir sakne.",
           fakti=["Atrisināt - atrast VISAS saknes.",
                  "Aizmirsta sakne - nepilnīga atbilde.",
                  "Vajag pamatot, ka citu nav."]),

    Doma("Visas saknes un pamatojums",
         "Atrisināt vienādojumu nozīmē atrast visas tā saknes vai pierādīt, "
         "ka sakņu nav. Atbildi pieraksta kā sakņu kopu: x = 5, vai x₁ = 3, "
         "x₂ = −3, vai «sakņu nav».",
         soli=[
             "Pārveido vienādojumu līdz x = skaitlis.",
             "Katrs solis nedrīkst pazaudēt vai pievienot sakni.",
             "Ja ir vairākas iespējas (x² = 9) - apskati visas.",
             "Pārbaudi saknes, ievietojot sākotnējā vienādojumā.",
         ],
         pieze="Minēšana atrod sakni, bet nepasaka, vai tā ir vienīgā - "
               "tāpēc vajag metodi."),

    Paraugs("Visas saknes",
            uzd="Atrisini |x| = 7.",
            soli=[
                ("|x| = 7 nozīmē: attālums no 0 ir 7", "Moduļa nozīme."),
                ("x = 7 vai x = −7", "Divas vietas uz taisnes."),
                ("Citu nav: tikai divi punkti 7 attālumā", "Pamatojums."),
            ],
            atbilde="x₁ = 7, x₂ = −7"),

    Varianti("Cik sakņu?", [
        {"jaut": "x + 3 = 10",
         "opcijas": ["Viena", "Divas", "Neviena", "Bezgalīgi daudz"],
         "pareizi": 0, "padoms": "x = 7."},
        {"jaut": "x² = 16",
         "opcijas": ["Divas", "Viena", "Neviena", "Bezgalīgi daudz"],
         "pareizi": 0, "padoms": "4 un −4."},
        {"jaut": "x² = −4",
         "opcijas": ["Neviena", "Viena", "Divas", "Bezgalīgi daudz"],
         "pareizi": 0, "padoms": "Kvadrāts nav negatīvs."},
        {"jaut": "x + 1 = 1 + x",
         "opcijas": ["Bezgalīgi daudz", "Viena", "Neviena", "Divas"],
         "pareizi": 0, "padoms": "Patiess visiem x."},
    ], pamats=4),

    Ievadi("Atrisini", [
        {"jaut": "x − 8 = 3. x = ?",
         "atb": ["11"], "padoms": "3 + 8."},
        {"jaut": "x² = 25. Pozitīvā sakne?",
         "atb": ["5"], "padoms": "5 · 5."},
        {"jaut": "x² = 25. Negatīvā sakne?",
         "atb": ["−5", "-5"], "padoms": "(−5)²."},
        {"jaut": "|x| = 0. Cik sakņu?",
         "atb": ["1"], "padoms": "Tikai 0."},
    ]),

    Pasaule("Paroles atkopšana",
            Varianti("", [
                {"jaut": "Sistēma saka: «PIN cipari summā dod 2». Cik "
                         "divciparu PIN ir iespējami (00-99)?",
                 "opcijas": ["3 (02, 11, 20)", "1", "2", "Bezgalīgi"],
                 "pareizi": 0, "padoms": "Visas saknes: a + b = 2."},
                {"jaut": "Kāpēc hakeris pārbauda visus variantus?",
                 "opcijas": ["Viena sakne varbūt nav īstā - vajag visas",
                             "Tā ir vieglāk", "Nav nozīmes",
                             "Lai būtu ilgāk"],
                 "pareizi": 0, "padoms": "Visas saknes."},
            ]),
            pavediens="kodi",
            konteksts="Ja nosacījumam ir vairāki atrisinājumi, jāpārbauda "
                      "visi - tāpat kā vienādojumā.",
            kapec="Atrisināt nozīmē atrast visus."),

    Kopsavilkums([
        "Zinu, ka jāatrod visas saknes.",
        "Zinu, ka sakņu var būt viena, vairākas, neviena vai bezgalīgi.",
        "Pierakstu saknes x₁, x₂.",
        "Pārbaudu saknes sākotnējā vienādojumā.",
    ]),

    Majas([
        "Atrisini x² = 49 un |x| = 3.",
        "Izdomā vienādojumu bez saknēm.",
        "Izdomā vienādojumu ar bezgalīgi daudz saknēm.",
    ]),
]
