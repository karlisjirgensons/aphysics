# -*- coding: utf-8 -*-
"""2. klase, 27. stunda: «Kā skaitli pierakstīt kā summu?»

Skaitli var sadalīt divos, trīs un vairāk saskaitāmajos, arī vienādos:
12 = 6 + 6 = 4 + 4 + 4. Skaitļa mājiņa parāda visus pārus, un vienādu
saskaitāmo summas sagatavo reizināšanu, kas nāks 2.7. tematā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes, majina)

TEMA = "Kā skaitli pierakstīt kā summu?"

MERKIS = ("Šodien pierakstīsim skaitli līdz 20 kā divu un vairāku skaitļu "
          "summu, arī kā vienādu skaitļu summu.")

SATURS = [
    Sakums("Kā 12 konfektes salikt vienādās kaudzītēs?",
           zimejums=bildes([[("ripina", 6)], [("ripina", 6)]]),
           paraksts="12 = 6 + 6.",
           fakti=["12 = 4 + 4 + 4 - trīs kaudzītes.",
                  "12 = 3 + 3 + 3 + 3 - četras kaudzītes.",
                  "Vienu skaitli var sadalīt daudzos veidos."]),

    Doma("Skaitlis kā summa",
         "Skaitli var sadalīt divos vai vairākos saskaitāmajos.",
         soli=[
             "Divi saskaitāmie: 12 = 7 + 5 = 8 + 4 = 9 + 3.",
             "Trīs saskaitāmie: 12 = 5 + 4 + 3.",
             "Vienādi saskaitāmie: 12 = 6 + 6 = 4 + 4 + 4.",
             "Pārbaudi - saskaiti atpakaļ.",
         ]),

    Ievadi("Aizpildi mājiņu", [
        {"jaut": "Mājiņā 14. Kāds skaitlis trūkst: 9 + ?",
         "zim": majina(14, [(9, None)]), "atb": ["5"], "padoms": "14 − 9."},
        {"jaut": "Mājiņā 16. 8 + ?", "zim": majina(16, [(8, None)]),
         "atb": ["8"], "padoms": "Divi vienādi."},
        {"jaut": "Mājiņā 18. ? + 11", "zim": majina(18, [(None, 11)]),
         "atb": ["7"], "padoms": "18 − 11."},
        {"jaut": "Mājiņā 20. 13 + ?", "zim": majina(20, [(13, None)]),
         "atb": ["7"], "padoms": "20 − 13."},
    ]),

    Ievadi("Vienādi saskaitāmie", [
        {"jaut": "10 = 5 + ?", "atb": ["5"], "padoms": "Divi vienādi."},
        {"jaut": "15 = 5 + 5 + ?", "atb": ["5"], "padoms": "15 − 10."},
        {"jaut": "18 = 9 + ?", "atb": ["9"], "padoms": "Divi vienādi."},
        {"jaut": "Cik reizes jāsaskaita 2, lai sanāktu 8?", "atb": ["4"],
         "padoms": "2 + 2 + 2 + 2."},
        {"jaut": "20 = 10 + ?", "atb": ["10"], "padoms": "Divi desmiti."},
        {"jaut": "Cik reizes jāsaskaita 3, lai sanāktu 9?", "atb": ["3"],
         "padoms": "3 + 3 + 3."},
    ], pamats=4),

    Varianti("Vai summa pareiza?", [
        {"jaut": "Kura summa nav 12?",
         "opcijas": ["5 + 5 + 3", "4 + 4 + 4", "6 + 6", "3 + 3 + 3 + 3"],
         "pareizi": 0, "padoms": "5 + 5 + 3 = 13."},
        {"jaut": "Kurš skaitlis nav vienādu divu skaitļu summa?",
         "opcijas": ["13", "14", "16", "10"], "pareizi": 0,
         "padoms": "6 + 6 = 12, 7 + 7 = 14."},
    ]),

    Pasaule("Kā sadalīt spēlētājus?",
            Varianti("", [
                {"jaut": "16 bērni sadalās vienādās komandās. Kurš "
                         "sadalījums der?",
                 "opcijas": ["8 + 8", "7 + 9", "5 + 5 + 5"], "pareizi": 0,
                 "padoms": "Komandām jābūt vienādām un kopā 16."},
                {"jaut": "Kā sadalīt 16 bērnus 4 vienādās komandās?",
                 "opcijas": ["4 + 4 + 4 + 4", "5 + 5 + 3 + 3",
                             "8 + 8"], "pareizi": 0,
                 "padoms": "Četras komandas pa ... ."},
            ]),
            pavediens="sports",
            konteksts="Sporta stundā 16 bērni spēlēs stafeti.",
            kapec="Vienāda summa - godīga spēle."),

    Kopsavilkums([
        "Pierakstu skaitli kā divu un vairāku skaitļu summu.",
        "Atrodu vienādu skaitļu summas.",
        "Pārbaudu summu, saskaitot atpakaļ.",
    ]),

    Majas([
        "Sadali 20 ķiršus vienādās kaudzītēs visos iespējamos veidos.",
        "Pieraksti katru ar summu.",
        "Kuru skaitli nevar sadalīt divās vienādās daļās: 11 vai 12?",
    ]),
]
