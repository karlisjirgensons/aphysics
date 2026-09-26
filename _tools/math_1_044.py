# -*- coding: utf-8 -*-
"""1. klase, 44. stunda: «Cik centimetru?»

Mēra īstus priekšmetus veselos centimetros un pieraksta ar mērvienību:
8 cm. Skaitlis bez «cm» nepasaka, ko mērīja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals)

TEMA = "Cik centimetru?"

MERKIS = ("Šodien izmērīsim priekšmetus centimetros un pierakstīsim "
          "rezultātu ar «cm».")

SATURS = [
    Sakums("Zīmulis ir 8 ... ko?",
           zimejums=lineals(10, [(0, 8, "zīmulis")]),
           paraksts="8 cm - skaitlis un mērvienība.",
           fakti=["Rezultātu raksta ar mērvienību: 8 cm.",
                  "«cm» nozīmē centimetrs.",
                  "Bez mērvienības skaitlis neko nepasaka."]),

    Doma("Mērījuma pieraksts",
         "Skaitlis stāsta, cik; mērvienība - ar ko mērīja.",
         soli=[
             "Pieliec lineālu no 0.",
             "Nolasi skaitli pie gala.",
             "Uzraksti skaitli un «cm»: 8 cm.",
         ]),

    Ievadi("Cik cm?", [
        {"jaut": "Cik cm gara ir dzēšgumija?",
         "zim": lineals(10, [(0, 3, "dzēšgumija")]), "atb": ["3"],
         "padoms": "Skaitlis pie gala."},
        {"jaut": "Cik cm gara ir karote?",
         "zim": lineals(20, [(0, 15, "karote")]), "atb": ["15"],
         "padoms": "Skaitlis pie gala."},
        {"jaut": "Cik cm garš ir krītiņš?",
         "zim": lineals(10, [(0, 6, "krītiņš")]), "atb": ["6"],
         "padoms": "Skaitlis pie gala."},
        {"jaut": "Cik cm gara ir sprādze?",
         "zim": lineals(10, [(0, 2, "sprādze")]), "atb": ["2"],
         "padoms": "Skaitlis pie gala."},
    ]),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "Grāmata ir 20 centimetru gara.",
         "opcijas": ["20 cm", "20", "cm 20"], "pareizi": 0,
         "padoms": "Skaitlis, tad mērvienība."},
        {"jaut": "Kurš ir garāks: 9 cm vai 6 cm?",
         "opcijas": ["9 cm", "6 cm", "vienādi"], "pareizi": 0,
         "padoms": "9 ir vairāk nekā 6."},
    ]),

    Petijums("Izmēri penāli", [
        "Izmēri zīmuli, dzēšgumiju un asināmo centimetros.",
        "Pieraksti katru ar «cm».",
        "Kurš ir garākais? Kurš īsākais?",
    ], vajag="lineāls, penālis"),

    Pasaule("Vai zīmulis ietilps penālī?",
            Ievadi("", [
                {"jaut": "Penālis iekšpusē 18 cm, zīmulis 16 cm. Par cik cm "
                         "penālis garāks?", "atb": ["2"], "padoms": "18 − 16."},
            ]),
            pavediens="skola",
            konteksts="Jauns zīmulis - vai tas ietilps vecajā penālī?",
            kapec="Centimetri ļauj salīdzināt, pat neliekot kopā."),

    Kopsavilkums([
        "Mēru veselos centimetros.",
        "Pierakstu ar mērvienību: 8 cm.",
        "Salīdzinu garumus.",
    ]),

    Majas([
        "Izmēri 3 lietas virtuvē un pieraksti centimetros.",
        "Kura bija garākā?",
        "Uzmini vienas lietas garumu, tad izmēri.",
    ]),
]
