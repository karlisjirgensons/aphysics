# -*- coding: utf-8 -*-
"""6. klase, 144. stunda: «Par cik mainījās temperatūra?»

Stunda ar dabaszinātņu saturu. Visi skaitļi nāk no īstiem mērījumiem, un
uzdevums vienmēr ir viens: atrast starpību. Tā ir tā pati atņemšana, tikai
ar mērvienībām un ticamības pārbaudi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Par cik mainījās temperatūra?"

MERKIS = ("Lietosim saskaitīšanu un atņemšanu situācijās ar citu mācību "
          "jomu kontekstu.")

SATURS = [
    Sakums("Starpība ir atņemšana ar mērvienību",
           zimejums=plakne(lauzta=[(0, -12), (6, -4), (12, 3), (18, -2)],
                           no_x=0, lidz_x=18, no_y=-14, lidz_y=6, solis=3,
                           x_nos="h", y_nos="°C"),
           paraksts="Diennakts mērījumi. Starpība starp augstāko un zemāko "
                    "ir 3 − (−12) = 15 grādi.",
           fakti=["Izmaiņa ir jaunā vērtība mīnus vecā.",
                  "Ja izmaiņa ir negatīva, lielums samazinājās.",
                  "Atbildi vienmēr pieraksta ar mērvienību."]),

    Doma("Jaunā mīnus vecā",
         "Lieluma izmaiņu aprēķina, no jaunās vērtības atņemot veco; "
         "rezultāta zīme pasaka, vai lielums auga vai sarūka.",
         soli=[
             "Pieraksti abas vērtības ar zīmēm un mērvienībām.",
             "No jaunās atņem veco.",
             "Pārraksti atņemšanu par saskaitīšanu, ja vajag.",
             "Nosaki zīmi un aprēķini moduli.",
             "Pieraksti atbildi ar mērvienību un ar vārdiem.",
         ],
         pieze="Ja jautā «par cik grādiem aukstāks», atbildē ir modulis, "
               "nevis negatīvs skaitlis: «par 8 grādiem aukstāks», nevis "
               "«par −8 grādiem aukstāks»."),

    Paraugs("Aprēķini izmaiņu",
            uzd="Naktī bija −12 °C, dienā 3 °C. Par cik grādiem mainījās "
                "temperatūra?",
            soli=[
                ("Jaunā vērtība: 3; vecā: −12",
                 "Abas ar zīmēm."),
                ("3 − (−12)",
                 "Jaunā mīnus vecā."),
                ("= 3 + 12 = 15",
                 "Atņemt negatīvu nozīmē pieskaitīt."),
                ("Temperatūra paaugstinājās par 15 grādiem",
                 "Atbilde ar vārdiem."),
            ],
            atbilde="paaugstinājās par 15 °C"),

    Ievadi("Aprēķini izmaiņas", [
        {"jaut": "No −12 °C uz 3 °C. Par cik grādiem paaugstinājās?",
         "atb": ["15"], "padoms": "3 + 12."},
        {"jaut": "No 3 °C uz −2 °C. Par cik grādiem pazeminājās?",
         "atb": ["5"], "padoms": "3 + 2."},
        {"jaut": "No −4 °C uz −9 °C. Par cik grādiem pazeminājās?",
         "atb": ["5"], "padoms": "9 − 4."},
        {"jaut": "Kalnā −18 °C, ielejā −3 °C. Par cik grādiem ieleja "
                 "siltāka?",
         "atb": ["15"], "padoms": "−3 − (−18)."},
        {"jaut": "Dziļums no −150 m uz −40 m. Par cik metriem pacēlās?",
         "atb": ["110"], "padoms": "150 − 40."},
        {"jaut": "Augstums no 250 m uz −50 m. Par cik metriem nolaidās?",
         "atb": ["300"], "padoms": "250 + 50."},
    ], pamats=4),

    Petijums("Izmēri temperatūras izmaiņu",
             vajag="termometrs vai laika ziņu lietotne",
             soli=[
                 "Pieraksti temperatūru no rīta, pusdienlaikā un vakarā.",
                 "Aprēķini izmaiņu starp katriem diviem mērījumiem.",
                 "Pieraksti, kura izmaiņa bija vislielākā.",
                 "Aprēķini starpību starp dienas augstāko un zemāko.",
             ],
             secinajums="Dienas svārstība ir starpība starp augstāko un "
                        "zemāko mērījumu - un tā parasti ir lielāka, nekā "
                        "liekas."),

    Varianti("Auga vai sarūka?", [
        {"jaut": "Izmaiņa ir −6 grādi. Tas nozīmē...",
         "opcijas": ["kļuva par 6 grādiem aukstāks",
                     "kļuva par 6 grādiem siltāks",
                     "temperatūra ir −6", "nekas nemainījās"],
         "pareizi": 0,
         "padoms": "Negatīva izmaiņa - samazinājums."},
        {"jaut": "Izmaiņu aprēķina kā...",
         "opcijas": ["jaunā mīnus vecā", "vecā mīnus jaunā",
                     "abu summa", "lielākā mīnus mazākā"],
         "pareizi": 0,
         "padoms": "Tad zīme pasaka virzienu."},
        {"jaut": "No −5 °C uz −1 °C izmaiņa ir...",
         "opcijas": ["+4 grādi", "−4 grādi", "+6 grādi", "−6 grādi"],
         "pareizi": 0,
         "padoms": "−1 − (−5)."},
        {"jaut": "Ja jautā «par cik aukstāks», atbildē raksta...",
         "opcijas": ["moduli bez zīmes", "negatīvu skaitli",
                     "abas vērtības", "nulli"],
         "pareizi": 0,
         "padoms": "Vārds «aukstāks» jau satur virzienu."},
    ], pamats=4),

    Pasaule("Ko rāda diennakts mērījumi?",
            Ievadi("", [
                {"jaut": "Mērījumi: −12; −4; 3; −2 °C. Kāda ir augstākā "
                         "vērtība?",
                 "atb": ["3"], "padoms": "Lielākais skaitlis."},
                {"jaut": "Kāda ir zemākā vērtība?",
                 "atb": ["-12", "−12"], "padoms": "Mazākais skaitlis."},
                {"jaut": "Kāda ir diennakts svārstība grādos?",
                 "atb": ["15"], "padoms": "3 − (−12)."},
                {"jaut": "Par cik grādiem temperatūra pazeminājās pēdējā "
                         "posmā?",
                 "atb": ["5"], "padoms": "No 3 uz −2."},
            ]),
            pavediens="planeta",
            konteksts="Meteoroloģijā diennakts svārstība ir viens no "
                      "galvenajiem rādītājiem - un tā ir vienkārša starpība.",
            kapec="Viena atņemšana apraksta visu diennakti."),

    Kopsavilkums([
        "Aprēķinu lieluma izmaiņu kā jaunās un vecās vērtības starpību.",
        "Nosaku pēc zīmes, vai lielums auga vai sarūka.",
        "Pierakstu atbildi ar mērvienību un ar vārdiem.",
        "Aprēķinu svārstību starp augstāko un zemāko vērtību.",
    ]),

    Majas([
        "Pieraksti trīs šodienas temperatūras un aprēķini visas izmaiņas.",
        "Atrodi dienas svārstību.",
        "Pieraksti, kura izmaiņa bija visstraujākā.",
    ]),
]
