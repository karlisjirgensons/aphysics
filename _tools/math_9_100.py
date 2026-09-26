# -*- coding: utf-8 -*-
"""9. klase, 100. stunda: «Kā uzdevumu pierakstīt ar vienādojumu?»

Situācijas uzdevums → nezināmais → vienādojums → saknes → «kura der?».
Trīs tipiski sižeti: laukums, skaitļi, kustība. Katrā vienu sakni izmet
situācijas dēļ.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā uzdevumu pierakstīt ar vienādojumu?"

MERKIS = ("Veidosim kvadrātvienādojumu situācijas uzdevumam un izvērtēsim "
          "atrisinājuma jēgu.")

SATURS = [
    Sakums("Foto ar rāmi: 600 cm²",
           zimejums=geometrija([("_1", 0, 0), ("_2", 24, 0), ("_3", 24, 25),
                                ("_4", 0, 25), ("_5", 2, 2), ("_6", 22, 2),
                                ("_7", 22, 23), ("_8", 2, 23)],
                               nogriezni=[("_1", "_2"), ("_2", "_3"),
                                          ("_3", "_4"), ("_4", "_1"),
                                          ("_5", "_6"), ("_6", "_7"),
                                          ("_7", "_8"), ("_8", "_5")],
                               iekrasot=[(("_1", "_2", "_3", "_4"), 1),
                                         (("_5", "_6", "_7", "_8"), 0)],
                               uzraksti=[(12, 12.5, "20 × 21"),
                                         (12, 24, "x")]),
           paraksts="Foto 20 × 21 cm, rāmis x cm platumā, kopā 600 cm².",
           fakti=["(20 + 2x)(21 + 2x) = 600.",
                  "4x^2 + 82x − 180 = 0 ⇒ x = 2 vai x = −22,5.",
                  "Rāmja platums nevar būt negatīvs: x = 2 cm."]),

    Doma("No teksta uz vienādojumu",
         "Apzīmē nezināmo, izsaki pārējo ar to, pieraksti vienādību no "
         "teksta, atrisini un izvērtē.",
         soli=[
             "Ko apzīmē ar x? Pieraksti vārdiem (ar mērvienību).",
             "Izsaki pārējos lielumus ar x.",
             "Atrodi teikumu, kas dod vienādību.",
             "Atrisini; katru sakni pārbaudi pret situāciju.",
             "Atbildi uz jautājumu - ne tikai «x = ...».",
         ]),

    Slidnis("Trīs sižeti", [
        {"v": "Laukums", "teksts": "Taisnstūris: mala x, otra x + 3, S = 40 "
                                   "⇒ x^2 + 3x − 40 = 0 ⇒ x = 5"},
        {"v": "Skaitļi", "teksts": "Divi pēc kārtas skaitļi, reizinājums 132: "
                                   "x(x + 1) = 132 ⇒ 11 un 12 (vai −12 un −11)"},
        {"v": "Kustība", "teksts": "h = −5t^2 + 25t = 30 ⇒ t = 2 vai t = 3 - "
                                   "abas der (augšup un lejup)"},
    ]),

    Paraugs("Skaitļu uzdevums",
            uzd="Skaitļa kvadrāts ir par 30 lielāks nekā pats skaitlis. Kāds "
                "ir skaitlis?",
            soli=[
                ("x^2 = x + 30 ⇒ x^2 − x − 30 = 0", "Vienādojums."),
                ("D = 121; x = {1 ± 11|2}", "Saknes."),
                ("x = 6 vai x = −5", "Abas der - skaitlis var būt negatīvs."),
            ],
            atbilde="6 vai −5"),

    Ievadi("Sastādi un atrisini", [
        {"jaut": "Taisnstūra garums par 4 cm lielāks par platumu, laukums "
                 "60 cm². Platums (cm)?", "atb": ["6"],
         "padoms": "x(x + 4) = 60."},
        {"jaut": "Divu pēc kārtas naturālu skaitļu reizinājums 156. Mazākais?",
         "atb": ["12"], "padoms": "x(x + 1) = 156."},
        {"jaut": "Kvadrāta laukums pieauga par 45 cm², kad malu palielināja "
                 "par 3 cm. Sākotnējā mala (cm)?", "atb": ["6"],
         "padoms": "(x + 3)^2 − x^2 = 45."},
    ]),

    Varianti("Kura sakne der?", [
        {"jaut": "Laukuma uzdevumā saknes 8 un −11.",
         "opcijas": ["8", "−11", "abas", "neviena"],
         "pareizi": 0, "padoms": "Garums > 0."},
        {"jaut": "Skolēnu skaita uzdevumā saknes 24 un 2,5.",
         "opcijas": ["24", "2,5", "abas", "neviena"],
         "pareizi": 0, "padoms": "Skolēnu skaits - vesels."},
    ]),

    Pasaule("Klases ekskursija",
            Ievadi("", [
                {"jaut": "Autobuss maksā 360 €, dala visiem vienādi. Ja brauktu "
                         "par 6 skolēniem vairāk, katram būtu jāmaksā par 2 € "
                         "mazāk. {360|x} − {360|x + 6} = 2 ⇒ x^2 + 6x − 1080 = 0. "
                         "Cik skolēnu brauc?", "atb": ["30"],
                 "padoms": "D = 36 + 4320 = 4356 = 66^2."},
                {"jaut": "Cik € maksā katrs?", "atb": ["12"],
                 "padoms": "360 : 30."},
            ]),
            pavediens="skola",
            konteksts="Klase plāno ekskursiju; cena uz vienu atkarīga no "
                      "braucēju skaita.",
            kapec="Negatīvā sakne −36 skolēnu skaitam neder."),

    Kopsavilkums([
        "Apzīmēju nezināmo un sastādu vienādojumu.",
        "Atrisinu un izvērtēju katru sakni.",
        "Atbildu uz uzdevuma jautājumu.",
    ]),

    Majas([
        "Sastādi un atrisini: taisnstūra perimetrs 34 cm, laukums 60 cm².",
        "Izdomā uzdevumu, kurā abas saknes der.",
        "Izdomā uzdevumu, kurā der tikai viena.",
    ]),
]
