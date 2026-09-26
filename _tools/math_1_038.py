# -*- coding: utf-8 -*-
"""1. klase, 38. stunda: «Kā aplamu vienādību salabot?»

Aplamu vienādību var salabot vairākos veidos: nomaina rezultātu, vienu
saskaitāmo vai zīmi. 5 + 2 = 8 labojas par 5 + 2 = 7, 5 + 3 = 8 vai
6 + 2 = 8. Salīdzina idejas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kā aplamu vienādību salabot?"

MERKIS = ("Šodien izdomāsim vairākus veidus, kā aplamu vienādību padarīt "
          "patiesu.")

SATURS = [
    Sakums("5 + 2 = 8 ir aplams. Kā to salabot?",
           zimejums=restis([[5, "+", 2, "=", 8]]),
           paraksts="Var mainīt jebkuru skaitli - vai zīmi.",
           fakti=["5 + 2 = 7 - maina rezultātu.",
                  "5 + 3 = 8 - maina otro skaitli.",
                  "6 + 2 = 8 - maina pirmo skaitli."]),

    Doma("Vairāki labojumi",
         "Aplamu vienādību var salabot, mainot tikai vienu skaitli - un "
         "katru var izvēlēties.",
         soli=[
             "Izrēķini kreiso pusi.",
             "Salabo rezultātu - vai",
             "maini vienu saskaitāmo, lai sanāktu labā puse.",
         ]),

    Ievadi("Salabo: 5 + 2 = 8", [
        {"jaut": "5 + 2 = ?", "atb": ["7"], "padoms": "Maini rezultātu."},
        {"jaut": "5 + ? = 8", "atb": ["3"], "padoms": "Maini otro skaitli."},
        {"jaut": "? + 2 = 8", "atb": ["6"], "padoms": "Maini pirmo skaitli."},
    ]),

    Ievadi("Salabo pats", [
        {"jaut": "9 − 3 = 5. Kāds jābūt rezultātam?", "atb": ["6"],
         "padoms": "3 + 6 = 9."},
        {"jaut": "4 + 4 = 9. Kāds jābūt otrajam skaitlim?", "atb": ["5"],
         "padoms": "4 + ? = 9."},
        {"jaut": "7 − ? = 4 (bija 7 − 2 = 4)", "atb": ["3"],
         "padoms": "4 + ? = 7."},
        {"jaut": "? + 1 = 10 (bija 8 + 1 = 10)", "atb": ["9"],
         "padoms": "Pirms 10."},
    ]),

    Varianti("Mainām zīmi", [
        {"jaut": "6 ? 2 = 4. Kāda zīme jāliek?",
         "opcijas": ["−", "+"], "jaukt": False, "pareizi": 0,
         "padoms": "Kļuva mazāk."},
        {"jaut": "3 ? 5 = 8. Kāda zīme jāliek?",
         "opcijas": ["+", "−"], "jaukt": False, "pareizi": 0,
         "padoms": "Kļuva vairāk."},
    ]),

    Pasaule("Kļūda cenu zīmē",
            Ievadi("", [
                {"jaut": "Uz zīmes: «2 bulciņas pa 3 € = 5 €». Pareizi "
                         "3 + 3 = ?", "atb": ["6"], "padoms": "Divreiz 3."},
            ]),
            pavediens="veikals",
            konteksts="Veikala zīmē kāds saskaitīja nepareizi.",
            kapec="Salabot var, izrēķinot vēlreiz."),

    Kopsavilkums([
        "Atrodu aplamu vienādību.",
        "Salaboju to vairākos veidos.",
        "Salīdzinu savus labojumus ar drauga.",
    ]),

    Majas([
        "Salabo 3 veidos: 4 + 3 = 9.",
        "Izdomā aplamu vienādību mājiniekam.",
        "Kurš labojums tev patīk vislabāk? Kāpēc?",
    ]),
]
