# -*- coding: utf-8 -*-
"""2. klase, 58. stunda: «Cik var paveikt vienā minūtē?»

Minūte ir īsa, bet tajā var izdarīt daudz: uzrakstīt, pārlēkt, saskaitīt.
Skolēni mēra, cik reižu kaut ko izdara minūtē, ieraksta tabulā un salīdzina
- un tā iegūst sajūtu par minūtes garumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas, restis)

TEMA = "Cik var paveikt vienā minūtē?"

MERKIS = ("Šodien mērīsim, cik daudz var paveikt vienā minūtē, ierakstīsim "
          "rezultātus tabulā un salīdzināsim.")

_MINUTE = restis([["darbība", "reizes minūtē"], ["lēcieni ar auklu", 48],
                  ["pietupieni", 25], ["uzrakstīti vārdi", 12],
                  ["sirds sitieni", 90]])

SATURS = [
    Sakums("Cik reizes tava sirds pukst vienā minūtē?",
           zimejums=kolonnas([("mierā", 80), ("pēc skriešanas", 120)]),
           paraksts="Bērna sirds pukst apmēram 80-100 reizes minūtē.",
           fakti=["Kolibri sirds minūtē pukst vairāk nekā 1000 reižu!",
                  "Minūte - 60 sekundes.",
                  "Ko tu paspēj vienā minūtē?"]),

    Doma("Minūtes eksperiments",
         "Mēra, cik reižu darbību izdara tieši vienā minūtē.",
         soli=[
             "Viens mēra laiku: «Starts!» un pēc 60 s «Stop!».",
             "Otrs dara un skaita.",
             "Rezultātu ieraksta tabulā.",
             "Salīdzina rezultātus.",
         ]),

    Ievadi("Nolasi tabulu", [
        {"jaut": "Cik lēcienu ar auklu minūtē?", "zim": _MINUTE,
         "atb": ["48"], "padoms": "Pirmā rinda."},
        {"jaut": "Par cik vairāk lēcienu nekā pietupienu?", "zim": _MINUTE,
         "atb": ["23"], "padoms": "48 − 25."},
        {"jaut": "Cik vārdu uzrakstītu 2 minūtēs, rakstot tikpat ātri?",
         "zim": _MINUTE, "atb": ["24"], "padoms": "12 + 12."},
        {"jaut": "Cik pietupienu pusminūtē, ja tempu nemaina? (apmēram)",
         "zim": _MINUTE, "atb": ["12", "13"],
         "padoms": "Apmēram puse no 25."},
    ]),

    Varianti("Minūte vai stunda?", [
        {"jaut": "Cik ilgi tīra zobus?", "opcijas": ["2 minūtes",
                                                    "2 stundas", "2 s"],
         "pareizi": 0, "padoms": "Ne pārāk ilgi."},
        {"jaut": "Cik ilgi ilgst mācību stunda?",
         "opcijas": ["40 minūtes", "40 sekundes", "40 stundas"],
         "pareizi": 0, "padoms": "Mazāk par stundu."},
        {"jaut": "Cik ilgi aizsien kurpes?",
         "opcijas": ["dažas sekundes", "dažas stundas", "diena"],
         "pareizi": 0, "padoms": "Ļoti ātri."},
        {"jaut": "Cik ilgi guļ naktī?",
         "opcijas": ["apmēram 10 stundas", "10 minūtes", "10 sekundes"],
         "pareizi": 0, "padoms": "Visu nakti."},
    ]),

    Petijums("Mūsu minūtes tabula", [
        "Pārī izvēlieties 3 darbības: lēcieni, aplaudēšana, burtu rakstīšana.",
        "Katru dariet tieši 1 minūti.",
        "Ierakstiet rezultātus tabulā.",
        "Kurā darbībā bija visvairāk reižu?",
    ], vajag="hronometrs, lapa tabulai"),

    Pasaule("Cik ātri pārlēksi auklu?",
            Ievadi("", [
                {"jaut": "Ance pirmdien pārlēca 36 reizes minūtē, piektdien "
                         "- 51. Par cik vairāk?", "atb": ["15"],
                 "padoms": "51 − 36."},
                {"jaut": "Viņas mērķis - 60. Cik vēl pietrūkst?",
                 "atb": ["9"], "padoms": "60 − 51."},
            ]),
            pavediens="sports",
            konteksts="Ance trenējas lēkšanā ar auklu.",
            kapec="Minūtes rezultāts rāda, vai treniņš palīdz."),

    Kopsavilkums([
        "Mēru, cik reižu darbību izdara minūtē.",
        "Ierakstu rezultātus tabulā.",
        "Salīdzinu un izdaru secinājumu.",
    ]),

    Majas([
        "Saskaiti savus sirdspukstus minūtē mierā.",
        "Tad palec 1 minūti un saskaiti vēlreiz.",
        "Par cik vairāk?",
    ]),
]
