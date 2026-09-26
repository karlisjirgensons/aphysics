# -*- coding: utf-8 -*-
"""1. klase, 61. stunda: «Kā izskatās simta kvadrāts?»

Simta kvadrātā skaitļi 1-100 stāv pa 10 rindā. Katra rinda ir viens
desmits; lejup kolonnā skaitlis aug par 10, pa labi - par 1. Tā atrod
jebkura skaitļa vietu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, simta_kvadrats)

TEMA = "Kā izskatās simta kvadrāts?"

MERKIS = ("Šodien aizpildīsim simta kvadrātu un atradīsim skaitļu vietas "
          "tajā.")

SATURS = [
    Sakums("Kur simta kvadrātā ir 47?",
           zimejums=simta_kvadrats(izcelt=[47]),
           paraksts="5. rindā (41-50), 7. kolonnā.",
           fakti=["Katrā rindā 10 skaitļu.",
                  "Pa labi - par 1 vairāk.",
                  "Uz leju - par 10 vairāk."]),

    Doma("Kā atrast vietu",
         "Rinda pasaka desmitus, kolonna - vienus.",
         soli=[
             "Atrodi rindu: 47 ir starp 41 un 50.",
             "Ej pa rindu līdz vieniem: 7.",
             "Zem skaitļa - par 10 lielāks, virs - par 10 mazāks.",
         ]),

    Ievadi("Kurš skaitlis paslēpts?", [
        {"jaut": "Kurš skaitlis paslēpts?",
         "zim": simta_kvadrats(21, 40, slept=[34]), "atb": ["34"],
         "padoms": "Starp 33 un 35."},
        {"jaut": "Kurš skaitlis paslēpts?",
         "zim": simta_kvadrats(51, 70, slept=[58]), "atb": ["58"],
         "padoms": "Starp 57 un 59."},
        {"jaut": "Kurš skaitlis ir tieši zem 36?", "atb": ["46"],
         "padoms": "Par 10 vairāk."},
        {"jaut": "Kurš skaitlis ir tieši virs 72?", "atb": ["62"],
         "padoms": "Par 10 mazāk."},
        {"jaut": "Kurš skaitlis ir pa labi no 39?", "atb": ["40"],
         "padoms": "Par 1 vairāk."},
        {"jaut": "Kurš skaitlis paslēpts?",
         "zim": simta_kvadrats(81, 100, slept=[90]), "atb": ["90"],
         "padoms": "Rindas beigas."},
    ], pamats=4),

    Varianti("Ko tu redzi?", [
        {"jaut": "Ar ko beidzas visi skaitļi labajā kolonnā?",
         "zim": simta_kvadrats(izcelt=[10, 20, 30, 40, 50, 60, 70, 80, 90,
                                       100]),
         "opcijas": ["ar 0", "ar 1", "ar 9"], "pareizi": 0,
         "padoms": "10, 20, 30..."},
        {"jaut": "Kas kopīgs skaitļiem vienā kolonnā?",
         "opcijas": ["vienādi vieni", "vienādi desmiti", "nekas"],
         "pareizi": 0, "padoms": "3, 13, 23, 33..."},
    ]),

    Pasaule("Kinoteātra sēdvietas",
            Ievadi("", [
                {"jaut": "Zālē sēdvietas numurētas kā simta kvadrātā - pa 10 "
                         "rindā. Kurā rindā ir 45. vieta?", "atb": ["5"],
                 "padoms": "41-50 ir 5. rinda."},
                {"jaut": "Kura vieta ir tieši aiz 45 (nākamajā rindā)?",
                 "atb": ["55"], "padoms": "Par 10 vairāk."},
            ]),
            pavediens="celojums",
            konteksts="Kinoteātrī katrā rindā ir 10 sēdvietu.",
            kapec="Simta kvadrāts palīdz atrast vietu ātri."),

    Kopsavilkums([
        "Zinu, kā izkārtots simta kvadrāts.",
        "Atrodu skaitļa vietu.",
        "Zinu: uz leju +10, pa labi +1.",
    ]),

    Majas([
        "Uzzīmē simta kvadrāta vienu rindu no 31 līdz 40.",
        "Atrodi kalendārā līdzīgu kārtību.",
        "Kuri skaitļi ir ap 55 (augšā, apakšā, pa kreisi, pa labi)?",
    ]),
]
