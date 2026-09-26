# -*- coding: utf-8 -*-
"""7. klase, 132. stunda: «Kad vienādojumi ir ekvivalenti?»

Vienādojumi ir ekvivalenti, ja tiem ir vienas un tās pašas saknes.
Risinot vienādojumu, to aizstāj ar vienkāršāku ekvivalentu vienādojumu -
tāpēc katram solim jāsaglabā saknes.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kad vienādojumi ir ekvivalenti?"

MERKIS = ("Noteiksim, vai divi vienādojumi ir ekvivalenti, un pamatosim "
          "atbildi.")

SATURS = [
    Sakums("Trīs vienādojumi - viena sakne",
           zimejums=restis([["vienādojums", "sakne"],
                            ["2x + 3 = 11", "4"],
                            ["2x = 8", "4"],
                            ["x = 4", "4"]]),
           paraksts="Visi trīs ir ekvivalenti.",
           fakti=["Pēdējais ir visvienkāršākais - no tā uzreiz redz sakni.",
                  "Risināšana ir ceļš pa ekvivalentiem vienādojumiem."]),

    Doma("Vienādas saknes - ekvivalenti",
         "Divus vienādojumus sauc par ekvivalentiem, ja tiem ir vienas un tās "
         "pašas saknes (arī, ja abiem sakņu nav).",
         soli=[
             "Atrisini abus vienādojumus.",
             "Salīdzini sakņu kopas.",
             "Vienādas - ekvivalenti; atšķiras - nav.",
             "Ja kaut viena sakne atšķiras - nav ekvivalenti.",
         ],
         pieze="x = 3 un x² = 9 nav ekvivalenti: otrajam ir arī sakne −3."),

    Paraugs("Pārbaudi ekvivalenci",
            uzd="Vai 3x − 6 = 0 un x − 2 = 0 ir ekvivalenti?",
            soli=[
                ("3x − 6 = 0 ⇒ x = 2", "Pirmā sakne."),
                ("x − 2 = 0 ⇒ x = 2", "Otrā sakne."),
                ("Sakņu kopas vienādas", "{2} un {2}."),
            ],
            atbilde="Ekvivalenti."),

    Varianti("Ekvivalenti?", [
        {"jaut": "x + 5 = 8 un 2x = 6",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Abiem x = 3."},
        {"jaut": "x = 4 un x² = 16",
         "opcijas": ["Jā", "Nē"], "pareizi": 1, "jaukt": False,
         "padoms": "x² = 16 ir arī −4."},
        {"jaut": "5x = 10 un x = 5",
         "opcijas": ["Jā", "Nē"], "pareizi": 1, "jaukt": False,
         "padoms": "Pirmajam x = 2."},
        {"jaut": "x² = −1 un x + 1 = x",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Abiem sakņu nav."},
        {"jaut": "{x|2} = 3 un x = 6",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Abiem 6."},
        {"jaut": "2(x − 1) = 4 un 2x − 1 = 4",
         "opcijas": ["Jā", "Nē"], "pareizi": 1, "jaukt": False,
         "padoms": "3 un 2,5."},
    ], pamats=4),

    Pasaule("Receptes pārrēķins",
            Varianti("", [
                {"jaut": "«2 porcijas prasa 300 g miltu» un «1 porcija prasa "
                         "150 g». Vai apgalvojumi ekvivalenti?",
                 "opcijas": ["Jā - abi apraksta vienu attiecību",
                             "Nē", "Tikai kūkām", "Nevar zināt"],
                 "pareizi": 0, "padoms": "2x = 300 un x = 150."},
                {"jaut": "Kas notiek ar vienādojumu, ja abas puses dala ar 2?",
                 "opcijas": ["Iegūst ekvivalentu", "Sakne mainās",
                             "Sakne pazūd", "Rodas otra sakne"],
                 "pareizi": 0, "padoms": "Dalīšana ar skaitli ≠ 0."},
            ]),
            pavediens="virtuve",
            konteksts="Pārrēķinot recepti, iegūst ekvivalentu «vienādojumu» - "
                      "attiecība nemainās.",
            kapec="Ekvivalenti pārveidojumi saglabā atbildi."),

    Zimejums("Ceļš pa ekvivalentiem",
             restis([["4(x − 1) = 12"], ["x − 1 = 3"], ["x = 4"]]),
             paskaidro="Katrs solis - ekvivalents vienādojums."),

    Kopsavilkums([
        "Zinu, kas ir ekvivalenti vienādojumi.",
        "Pārbaudu ekvivalenci, salīdzinot saknes.",
        "Zinu, ka risināšana ir ekvivalentu vienādojumu virkne.",
        "Atrodu pretpiemēru ar papildu sakni.",
    ]),

    Majas([
        "Uzraksti 3 vienādojumus, ekvivalentus x = −2.",
        "Pārbaudi: vai x + 3 = 3 un 5x = 0 ekvivalenti?",
        "Izdomā divus vienādojumus bez saknēm.",
    ]),
]
