# -*- coding: utf-8 -*-
"""4. klase, 138. stunda: «Kuras figūras ir vienlielas?»

4.7. temata sākums. Vienlielas figūras - ar vienādu laukumu, bet var būt
dažādas formas. Rūtiņu lapā laukumu nosaka, skaitot rūtiņas. Tas atdala
«laukums» no «forma» un «perimetrs» - trīs dažādas lietas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura)

TEMA = "Kuras figūras ir vienlielas?"

MERKIS = ("Atradīsim rūtiņu lapā figūras ar vienādu laukumu un pamatosim "
          "atbildi.")

SATURS = [
    Sakums("Kas kopīgs taisnstūrim un burtam «L»?",
           zimejums=figura([(0, 0), (4, 0), (4, 2), (0, 2)], platums=5,
                           augstums=5),
           paraksts="Taisnstūrī 4 · 2 = 8 rūtiņas. Burtā «L» - arī 8.",
           fakti=["Laukums ir rūtiņu skaits figūrā.",
                  "Vienlielām figūrām rūtiņu skaits vienāds, forma - "
                  "dažāda."]),

    Doma("Vienlielas - vienāds laukums",
         "Figūras ir vienlielas, ja tām ir vienāds laukums - vienāds "
         "rūtiņu skaits, lai kāda būtu forma.",
         soli=[
             "Saskaiti rūtiņas katrā figūrā.",
             "Pusrūtiņas saliec pa divām.",
             "Salīdzini skaitus.",
             "Vienāds skaits - vienlielas figūras.",
         ],
         pieze="Vienlielām figūrām perimetrs var būt dažāds!"),

    Zimejums("Burts «L»",
             figura([(0, 0), (3, 0), (3, 2), (1, 2), (1, 4), (0, 4)],
                    platums=5, augstums=5),
             paskaidro="6 rūtiņas apakšā un 2 augšā - kopā 8.",
             ievads="Tā pati platība, cita forma."),

    Paraugs("Salīdzini",
            uzd="Kvadrāts 3 × 3 un taisnstūris 2 × 5. Vai vienlieli?",
            soli=[
                ("3 · 3 = 9", "Kvadrāts."),
                ("2 · 5 = 10", "Taisnstūris."),
                ("9 ≠ 10", "Nav vienlieli."),
            ],
            atbilde="nav vienlieli"),

    Ievadi("Saskaiti rūtiņas", [
        {"jaut": "Taisnstūris 6 × 2. Cik rūtiņu?", "atb": ["12"],
         "padoms": "6 · 2."},
        {"jaut": "Kvadrāts 4 × 4. Cik rūtiņu?", "atb": ["16"],
         "padoms": "4 · 4."},
        {"jaut": "Kādam taisnstūrim ar malu 3 ir laukums 12? Otrā mala?",
         "atb": ["4"], "padoms": "12 : 3."},
        {"jaut": "Cik dažādu taisnstūru (malas veseli skaitļi) ar laukumu "
                 "16? (4 × 4 un 2 × 8 un 1 × 16)", "atb": ["3"],
         "padoms": "Skaiti uzskaitītos."},
    ]),

    Varianti("Vienlieli vai nē?", [
        {"jaut": "Taisnstūri 2 × 6 un 3 × 4",
         "opcijas": ["vienlieli", "nav"], "pareizi": 0,
         "padoms": "12 un 12."},
        {"jaut": "Kvadrāts 5 × 5 un taisnstūris 4 × 6",
         "opcijas": ["nav", "vienlieli"], "pareizi": 0,
         "padoms": "25 un 24."},
        {"jaut": "Vai vienlielām figūrām jābūt vienādām formām?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "Svarīgs rūtiņu skaits."},
        {"jaut": "Vai vienlielām figūrām perimetrs vienmēr vienāds?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "1 × 16 un 4 × 4: perimetri 34 un 16."},
    ], pamats=4),

    Pasaule("Istabas grīda",
            Ievadi("", [
                {"jaut": "Istaba 4 m × 3 m. Cik m² grīdas?", "atb": ["12"],
                 "padoms": "4 · 3."},
                {"jaut": "Otra istaba 6 m × 2 m. Cik m²?", "atb": ["12"],
                 "padoms": "6 · 2."},
                {"jaut": "Vai abām istabām vajag vienādu daudzumu grīdas "
                         "seguma? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "tastatura": "text",
                 "padoms": "Vienlielas."},
                {"jaut": "Cik metru grīdlīstes vajag otrajai istabai "
                         "(perimetrs)?", "atb": ["16"],
                 "padoms": "6 + 2 + 6 + 2."},
            ]),
            pavediens="maja",
            konteksts="Remontā laukums nosaka grīdas segumu, bet perimetrs - "
                      "grīdlīstes.",
            kapec="Vienlielas istabas var prasīt dažādu grīdlīstu garumu."),

    Kopsavilkums([
        "Zinu, ka vienlielām figūrām ir vienāds laukums.",
        "Nosaku laukumu, skaitot rūtiņas.",
        "Zinu, ka forma un perimetrs var atšķirties.",
    ]),

    Majas([
        "Uzzīmē 3 dažādas figūras ar laukumu 10 rūtiņas.",
        "Izmēri divu galdu virsmas un salīdzini laukumus.",
        "Paskaidro, kāpēc vienlielām figūrām perimetrs var atšķirties.",
    ]),
]
