# -*- coding: utf-8 -*-
"""9. klase, 118. stunda: «Kā uzdevumu pārtulkot sistēmā?»

Uzdevums ar diviem nezināmajiem un diviem faktiem: katrs fakts - viens
vienādojums. Tabula «kas | skaits | cena | kopā» palīdz nepazaudēt datus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā uzdevumu pārtulkot sistēmā?"

MERKIS = ("Veidosim vienādojumu sistēmu situācijas uzdevumam un skaidrosim "
          "nezināmos.")


SATURS = [
    Sakums("35 galvas un 94 kājas - cik vistu un trušu?",
           zimejums=restis([["", "skaits", "kājas"], ["vistas", "x", "2x"],
                            ["truši", "y", "4y"], ["kopā", "35", "94"]]),
           paraksts="Senā ķīniešu mīkla: x + y = 35, 2x + 4y = 94.",
           fakti=["Divi nezināmie - divi fakti.",
                  "Galvas dod vienu vienādojumu, kājas - otru.",
                  "Atbilde: 23 vistas un 12 truši."]),

    Doma("Tulkošana sistēmā",
         "Apzīmē nezināmos, sastādi tabulu un no katras «kopā» rindas "
         "pieraksti vienādojumu.",
         soli=[
             "x - ..., y - ... (vārdiem, ar mērvienību).",
             "Tabula: katram lielumam rinda, katram raksturlielumam kolonna.",
             "Kopsummas dod vienādojumus.",
             "Atrisini un atbildi uz jautājumu ar vārdiem.",
         ]),

    Paraugs("Mīklas risinājums",
            uzd="Atrisini x + y = 35, 2x + 4y = 94.",
            soli=[
                ("2x + 2y = 70", "Pirmo · 2."),
                ("2y = 24 ⇒ y = 12", "Atņem."),
                ("x = 35 − 12 = 23", "Vistas."),
            ],
            atbilde="23 vistas, 12 truši"),

    Varianti("Kura sistēma atbilst?", [
        {"jaut": "Divu skaitļu summa 50, starpība 12.",
         "opcijas": ["x + y = 50, x − y = 12", "x + y = 12, x − y = 50",
                     "xy = 50, x − y = 12", "x + y = 50, xy = 12"],
         "pareizi": 0, "padoms": "Summa un starpība."},
        {"jaut": "3 kg ābolu un 2 kg banānu maksā 7 €; 1 kg ābolu dārgāks par "
                 "1 kg banānu par 0,50 €.",
         "opcijas": ["3a + 2b = 7, a − b = 0,5", "3a + 2b = 7, b − a = 0,5",
                     "a + b = 7, 3a − 2b = 0,5", "3a = 2b + 7, a = b"],
         "pareizi": 0, "padoms": "a - āboli."},
        {"jaut": "Tēvs 3 reizes vecāks par dēlu; pēc 10 gadiem - 2 reizes.",
         "opcijas": ["x = 3y, x + 10 = 2(y + 10)",
                     "x = 3y, x + 10 = 2y + 10", "3x = y, x + 10 = 2y",
                     "x = 3y, x = 2y + 10"],
         "pareizi": 0, "padoms": "Abiem pieskaita 10."},
    ]),

    Ievadi("Sastādi un atrisini", [
        {"jaut": "Divu skaitļu summa 50, starpība 12. Lielākais?",
         "atb": ["31"], "padoms": "2x = 62."},
        {"jaut": "Tēvs 3 reizes vecāks par dēlu, pēc 10 gadiem - 2 reizes. "
                 "Dēla vecums?", "atb": ["10"],
         "padoms": "3y + 10 = 2y + 20."},
        {"jaut": "Klasē 26 skolēni; meiteņu par 4 vairāk nekā zēnu. Zēnu?",
         "atb": ["11"], "padoms": "2x + 4 = 26."},
    ]),

    Pasaule("Koncerta biļetes",
            Ievadi("", [
                {"jaut": "Pārdotas 400 biļetes par 12 € un 20 €, ieņēmumi "
                         "6000 €. Sistēma: x + y = 400, 12x + 20y = 6000. "
                         "Lētāko biļešu skaits?", "atb": ["250"],
                 "padoms": "12x + 20(400 − x) = 6000."},
                {"jaut": "Dārgāko biļešu skaits?", "atb": ["150"],
                 "padoms": "400 − 250."},
            ]),
            pavediens="veikals",
            konteksts="Organizatori zina tikai kopējo skaitu un kopējo naudu.",
            kapec="Divi fakti - divi vienādojumi - viena atbilde.",
            zimejums=restis([["biļete", "skaits", "cena", "kopā"],
                             ["parastā", "x", "12 €", "12x"],
                             ["VIP", "y", "20 €", "20y"],
                             ["kopā", "400", "", "6000 €"]])),

    Kopsavilkums([
        "Apzīmēju nezināmos un sastādu tabulu.",
        "Pierakstu sistēmu no diviem faktiem.",
        "Atbildu uz jautājumu ar vārdiem.",
    ]),

    Majas([
        "Sastādi sistēmu: 12 monētas pa 2 € un 1 €, kopā 19 €.",
        "Atrisini to.",
        "Izdomā savu «galvas un kājas» mīklu.",
    ]),
]
