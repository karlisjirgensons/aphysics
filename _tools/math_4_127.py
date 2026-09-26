# -*- coding: utf-8 -*-
"""4. klase, 127. stunda: «Kā zīmējums palīdz?»

Shematisks zīmējums daļas uzdevumam: josla ir veselais, sadalīta saucēja
skaitā gabalu, uz vienu gabalu raksta pamatdaļu. Tas pats zīmējums der
gan «daļa no skaita», gan otrādi - «skaitlis, ja zināma daļa» (131. st.).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā zīmējums palīdz?"

MERKIS = ("Veidosim shematisku zīmējumu daļas noteikšanai un pastāstīsim, "
          "kā tas palīdz.")

SATURS = [
    Sakums("Kā ieraudzīt uzdevumu?",
           zimejums=restis([["?", "?", "?", "?", "?"],
                            ["", "viss: 60", "", "", ""]],
                           "josla sadalīta 5 daļās"),
           paraksts="Katrs «?» ir 60 : 5 = 12.",
           fakti=["Zīmējumā redz, cik gabalu un cik liels ir viss.",
                  "Tad skaitli gabalā atrast ir viegli."]),

    Doma("Josla - veselais, gabali - saucējs",
         "Uzzīmē joslu kā veselo, sadali to saucēja skaitā vienādu gabalu, "
         "atzīmē prasīto daļu un uzraksti zināmos skaitļus.",
         soli=[
             "Uzzīmē joslu un pie tās uzraksti veselo.",
             "Sadali to saucēja skaitā vienādu gabalu.",
             "Iekrāso tik gabalu, cik saka skaitītājs.",
             "Aprēķini vienu gabalu, tad iekrāsotos.",
         ],
         pieze="Zīmējums nav jāzīmē precīzi - svarīgi, lai gabali būtu "
               "vienādi."),

    Zimejums("{2|5} no 60",
             dala(5, 2, "katrs gabals 12, iekrāsoti 2 → 24"),
             paskaidro="Josla ir 60; piecas daļas pa 12; divas daļas - 24.",
             ievads="Tā izskatās shēma."),

    Paraugs("Ar zīmējumu",
            uzd="Veikalā 72 bumbas, {5|9} - futbola bumbas. Cik futbola "
                "bumbu?",
            soli=[
                ("josla 9 gabalos = 72", "Shēma."),
                ("72 : 9 = 8", "Viens gabals."),
                ("5 · 8 = 40", "Pieci gabali."),
            ],
            atbilde="40 futbola bumbas"),

    Ievadi("Zīmē un rēķini", [
        {"jaut": "{2|5} no 60 = ?", "atb": ["24"], "padoms": "12 · 2."},
        {"jaut": "{5|9} no 72 = ?", "atb": ["40"], "padoms": "8 · 5."},
        {"jaut": "{3|10} no 90 = ?", "atb": ["27"], "padoms": "9 · 3."},
        {"jaut": "{7|12} no 36 = ?", "atb": ["21"], "padoms": "3 · 7."},
    ]),

    Varianti("Kura shēma der?", [
        {"jaut": "«{3|4} no 20»",
         "opcijas": ["josla 4 gabalos, iekrāsoti 3",
                     "josla 3 gabalos, iekrāsoti 4",
                     "josla 20 gabalos, iekrāsoti 3"], "pareizi": 0,
         "padoms": "Saucējs - gabalu skaits."},
        {"jaut": "Josla 6 gabalos = 48. Cik viens gabals?",
         "opcijas": ["8", "6", "42", "288"], "pareizi": 0,
         "padoms": "48 : 6."},
        {"jaut": "Tajā pašā joslā iekrāsoti 5 gabali. Cik tas ir?",
         "opcijas": ["40", "30", "5", "43"], "pareizi": 0,
         "padoms": "5 · 8."},
    ]),

    Pasaule("Konstruktora komplekts",
            Ievadi("", [
                {"jaut": "Komplektā 120 detaļas, {1|4} ir riteņi. Cik "
                         "riteņu?",
                 "atb": ["30"], "padoms": "120 : 4."},
                {"jaut": "{2|5} ir klucīši. Cik klucīšu?", "atb": ["48"],
                 "padoms": "120 : 5 · 2."},
                {"jaut": "{1|10} ir motori un vadi. Cik?", "atb": ["12"],
                 "padoms": "120 : 10."},
                {"jaut": "Cik detaļu ir pārējās?", "atb": ["30"],
                 "padoms": "120 − 30 − 48 − 12."},
            ]),
            pavediens="tehnika",
            konteksts="Robotu komplektā detaļas sagrupētas - un instrukcija "
                      "min daļas, nevis skaitļus.",
            kapec="Shēma palīdz neapjukt daudzu daļu uzdevumā."),

    Kopsavilkums([
        "Zīmēju shēmu daļas uzdevumam.",
        "Nosaku viena gabala vērtību no shēmas.",
        "Pastāstu, kā zīmējums palīdz.",
    ]),

    Majas([
        "Uzzīmē shēmu: {3|8} no 40 un atrisini.",
        "Izdomā uzdevumu, kuram der josla 6 gabalos.",
        "Paskaidro kādam, kāpēc gabaliem jābūt vienādiem.",
    ]),
]
