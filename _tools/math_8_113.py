# -*- coding: utf-8 -*-
"""8. klase, 113. stunda: «Kas ir polinoms?»

Polinoms - monomu summa; katrs monoms ir loceklis, zīme pieder loceklim.
Binoms - divi locekļi, trinoms - trīs; loceklis bez burta ir brīvais
loceklis. Monoms ir viena locekļa polinoms.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kas ir polinoms?"

MERKIS = "Nosauksim polinoma locekļus un nošķirsim binomu un trinomu."

SATURS = [
    Sakums("No kā sastāv 3x² − 5x + 7?",
           zimejums=restis([["3x²", "−5x", "+7"],
                            ["loceklis", "loceklis", "brīvais"]]),
           paraksts="Trīs locekļi - tas ir trinoms.",
           fakti=["Polinoms - monomu summa; katrs monoms ir loceklis.",
                  "Binomā ir divi locekļi, trinomā - trīs.",
                  "Loceklis bez burta ir brīvais loceklis."]),

    Doma("Polinoma locekļi",
         "Zīme pirms locekļa pieder loceklim.",
         soli=[
             "Atdali locekļus pie + un − zīmēm: 3x^2, −5x, +7.",
             "Saskaiti locekļus: 2 - binoms, 3 - trinoms.",
             "Monoms arī ir polinoms - ar vienu locekli.",
             "Koeficients pie x ir skaitlis, kas stāv pirms x (ar zīmi).",
         ]),

    Ievadi("Nosauc", [
        {"jaut": "3x^2 − 5x + 7: cik locekļu?", "atb": ["3"],
         "padoms": "Trinoms."},
        {"jaut": "3x^2 − 5x + 7: brīvais loceklis?", "atb": ["7"],
         "padoms": "Bez burta."},
        {"jaut": "3x^2 − 5x + 7: koeficients pie x?", "atb": ["−5", "-5"],
         "padoms": "Zīme pieder loceklim."},
        {"jaut": "a^2 − 4: cik locekļu?", "atb": ["2"], "padoms": "Binoms."},
        {"jaut": "x^3 − x^2 + x − 1: koeficients pie x^2?",
         "atb": ["−1", "-1"], "padoms": "−x^2 = −1 · x^2."},
        {"jaut": "x^3 − x^2 + x − 1: brīvais loceklis?", "atb": ["−1", "-1"],
         "padoms": "Pēdējais."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "Kura izteiksme ir trinoms?",
         "opcijas": ["a^2 + 2a + 1", "a + 1", "3a^2", "a^2bc"],
         "pareizi": 0, "padoms": "Trīs locekļi."},
        {"jaut": "Vai 5x ir polinoms?",
         "opcijas": ["Jā - viena locekļa polinoms", "Nē",
                     "Tikai ja x > 0", "Tas ir binoms"],
         "pareizi": 0, "padoms": "Monoms ir polinoms."},
        {"jaut": "Kura izteiksme ir binoms?",
         "opcijas": ["x − 7", "x", "x^2 + x + 1", "7"],
         "pareizi": 0, "padoms": "Divi locekļi."},
    ]),

    Pasaule("Veikala čeks",
            Ievadi("", [
                {"jaut": "Čeks: 3 maizes pa a €, 2 piena pakas pa b € un maiss "
                         "0,10 €: 3a + 2b + 0,1. Cik locekļu?",
                 "atb": ["3"], "padoms": "Trinoms."},
                {"jaut": "a = 1,2 un b = 0,9. Summa (€)?", "atb": ["5,5"],
                 "padoms": "3,6 + 1,8 + 0,1."},
                {"jaut": "Kurš loceklis ir brīvais (€)?", "atb": ["0,1"],
                 "padoms": "Maiss maksā vienmēr tikpat."},
            ]),
            pavediens="veikals",
            konteksts="Katrs čeka rindiņas loceklis ir monoms: cena reiz "
                      "daudzums.",
            kapec="Polinoms ir summa - kā čeks."),

    Kopsavilkums([
        "Nosaucu polinoma locekļus ar zīmēm.",
        "Nošķiru binomu un trinomu.",
        "Atrodu koeficientus un brīvo locekli.",
    ]),

    Majas([
        "Uzraksti savu iepirkumu kā polinomu.",
        "Uzraksti trinomu, kura brīvais loceklis ir −3.",
        "Nosauc visu locekļu koeficientus polinomā 2x^3 − x + 4.",
    ]),
]
