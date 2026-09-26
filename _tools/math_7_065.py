# -*- coding: utf-8 -*-
"""7. klase, 65. stunda: «Ko nozīmē koeficienti k un b?»

k ir slīpums (virziena koeficients), b - pārbīde pa y asi. Stunda pēta tos
atsevišķi, kā digitālajā rīkā: maina vienu, otru tur nemainīgu. Paralēlām
taisnēm ir vienāds k, bet dažādi b.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         plakne)

TEMA = "Ko nozīmē koeficienti k un b?"

MERKIS = ("Pētīsim, kā grafika novietojums ir atkarīgs no k un b "
          "vērtībām.")


def _b(b, uzr):
    return plakne(grafiki=[(1, 0, "y = x"), (1, b, uzr)], no_x=-4,
                  lidz_x=4, no_y=-4, lidz_y=5, solis=1)


SATURS = [
    Sakums("Paralēlas taisnes - vienāds k",
           zimejums=plakne(grafiki=[(0.5, 2, "y = 0,5x + 2"),
                                    (0.5, -1, "y = 0,5x − 1")],
                           no_x=-4, lidz_x=4, no_y=-4, lidz_y=5, solis=1),
           paraksts="Abām k = 0,5 - tās ir paralēlas.",
           fakti=["k nosaka slīpumu.",
                  "b nosaka, kur taisne krusto y asi.",
                  "Maini b - taisne pārbīdās, bet nepagriežas."]),

    Doma("k - slīpums, b - pārbīde",
         "Funkcijas y = kx + b grafikā k parāda, par cik vienībām taisne "
         "paceļas, x pieaugot par 1; b parāda krustpunktu ar y asi (0; b). "
         "Taisnes ar vienādu k ir paralēlas.",
         soli=[
             "No (0; b) ej 1 pa labi un k uz augšu (vai leju, ja k < 0).",
             "Tas ir otrs punkts - savieno.",
             "Vienāds k, dažādi b - paralēlas taisnes.",
             "Vienāds b, dažādi k - taisnes krustojas punktā (0; b).",
         ],
         pieze="Tā grafikus pēta ar digitālo rīku, piemēram, GeoGebra: "
               "slīdnis k groza taisni, slīdnis b to bīda."),

    Slidnis("Maini b (k = 1)", [
        {"v": "b = −2", "teksts": "Taisne pārbīdās uz leju",
         "zim": _b(-2, "y = x − 2")},
        {"v": "b = 0", "teksts": "Caur sākumpunktu", "zim": _b(0, "")},
        {"v": "b = 2", "teksts": "Uz augšu par 2",
         "zim": _b(2, "y = x + 2")},
        {"v": "b = 4", "teksts": "Uz augšu par 4",
         "zim": _b(4, "y = x + 4")},
    ], ievads="Violetā - y = x, dzintara - ar citu b."),

    Paraugs("Zīmē pēc k un b",
            uzd="Uzzīmē y = −{2|3}x + 3, lietojot k un b.",
            soli=[
                ("b = 3 - punkts (0; 3)", "Sākums uz y ass."),
                ("k = −{2|3}: 3 pa labi, 2 uz leju", "Lai būtu veseli soļi."),
                ("Otrs punkts (3; 1)", "No (0; 3)."),
                ("Novelk taisni", "Gatavs."),
            ],
            atbilde="Taisne caur (0; 3) un (3; 1)"),

    Varianti("Salīdzini taisnes", [
        {"jaut": "Kuras taisnes ir paralēlas?",
         "opcijas": ["y = 3x + 1 un y = 3x − 5",
                     "y = 3x + 1 un y = −3x + 1",
                     "y = x un y = 2x",
                     "y = 4 un y = 4x"],
         "pareizi": 0,
         "padoms": "Vienāds k."},
        {"jaut": "Kurām taisnēm kopīgs punkts (0; 2)?",
         "opcijas": ["y = 5x + 2 un y = −x + 2",
                     "y = 2x un y = 2x + 1",
                     "y = x + 2 un y = x − 2",
                     "y = 2 un y = −2"],
         "pareizi": 0,
         "padoms": "Vienāds b."},
        {"jaut": "Kura taisne ir visstāvākā?",
         "opcijas": ["y = −5x", "y = 3x", "y = 0,5x + 10", "y = x"],
         "pareizi": 0,
         "padoms": "Lielākais |k|."},
    ]),

    Petijums("Pēti ar GeoGebra",
             ["Atver geogebra.org un ieraksti y = k·x + b.",
              "Piekrīt izveidot slīdņus k un b.",
              "Maini tikai k: kas notiek ar taisni? Pieraksti.",
              "Maini tikai b: kas notiek? Pieraksti.",
              "Atrodi k un b, lai taisne ietu caur (2; 5) un (0; 1)."],
             vajag="dators vai telefons ar GeoGebra",
             secinajums="k groza taisni ap punktu (0; b), b bīda taisni uz "
                         "augšu un leju. Caur (0; 1) un (2; 5): k = 2, b = 1."),

    Ievadi("Nolasi k un b", [
        {"jaut": "Taisne iet caur (0; −1) un (1; 2). Cik ir k?",
         "atb": ["3"], "padoms": "No −1 līdz 2: +3."},
        {"jaut": "Tai pašai taisnei b = ?",
         "atb": ["−1", "-1"], "padoms": "Krustpunkts ar y asi."},
        {"jaut": "Taisne paralēla y = 4x un iet caur (0; 7). Cik ir b?",
         "atb": ["7"], "padoms": "y = 4x + 7."},
        {"jaut": "Taisne caur (0; 5) un (2; 1). Cik ir k?",
         "atb": ["−2", "-2"], "padoms": "2 pa labi, 4 uz leju."},
    ]),

    Pasaule("Divi krājkonti",
            Ievadi("", [
                {"jaut": "Anna sāk ar 50 € un krāj 10 € nedēļā; Toms sāk ar "
                         "20 € un krāj 10 € nedēļā. Kurš koeficients abiem "
                         "vienāds - «k» vai «b»?",
                 "atb": ["k"], "padoms": "Krāšanas ātrums.",
                 "tastatura": "text"},
                {"jaut": "Par cik € Annai būs vairāk pēc 10 nedēļām?",
                 "atb": ["30"], "padoms": "Paralēlas taisnes - starpība "
                                        "nemainās."},
                {"jaut": "Cik € būs Tomam pēc 10 nedēļām?",
                 "atb": ["120"], "padoms": "20 + 100."},
            ]),
            pavediens="veikals",
            konteksts="Divas paralēlas taisnes nekad nekrustojas - Toms "
                      "Annu nepanāks, ja krāj tikpat.",
            kapec="Vienāds k - starpība paliek."),

    Kopsavilkums([
        "Zinu, ka k ir slīpums, b - krustpunkts ar y asi.",
        "Zīmēju taisni no (0; b) ar soli k.",
        "Atpazīstu paralēlas taisnes pēc vienāda k.",
        "Pētu grafikus ar digitālu rīku.",
    ]),

    Majas([
        "Uzraksti 3 taisnes, paralēlas y = −2x + 1.",
        "Uzraksti 3 taisnes caur punktu (0; −3).",
        "GeoGebra atrodi taisni caur (1; 4) un (3; 8).",
    ]),
]
