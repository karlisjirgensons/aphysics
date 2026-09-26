# -*- coding: utf-8 -*-
"""1. klase, 24. stunda: «Vai esam atraduši visus gadījumus?»

Sadalījumus sakārto pēc kārtas: kreisā daļa 0, 1, 2 ... līdz skaitlim. Tad
redz, ja kāds trūkst, un zina, kad beigt: sadalījumu (ar 0) ir par vienu
vairāk nekā skaitlis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Vai esam atraduši visus gadījumus?"

MERKIS = ("Šodien sakārtosim sadalījumus pēc kārtas un pārliecināsimies, ka "
          "neviens nav aizmirsts.")

SATURS = [
    Sakums("Juris atrada 4 veidus, kā sadalīt 5. Vai tas ir viss?",
           zimejums=restis([[2, 3], [5, 0], [1, 4], [3, 2]]),
           paraksts="Pēc kārtas būtu vieglāk redzēt, kā trūkst.",
           fakti=["Sakārto pēc kreisās daļas: 0, 1, 2, 3...",
                  "Caurums rindā - tur trūkst gadījuma.",
                  "Skaitlim 5 ir 6 sadalījumi (ar 0)."]),

    Doma("Pēc kārtas - nekas nepazūd",
         "Ja kreisā daļa aug pa 1 no 0 līdz skaitlim, visi gadījumi ir "
         "atrasti.",
         soli=[
             "Sāc ar 0 kreisajā pusē.",
             "Katrā nākamajā rindā - par 1 vairāk.",
             "Beidz, kad kreisajā pusē ir pats skaitlis.",
         ]),

    Ievadi("Kā trūkst?", [
        {"jaut": "Sadalījumi skaitlim 4. Kurš skaitlis trūkst kreisajā "
                 "ailē?",
         "zim": restis([[0, 4], [1, 3], [None, 2], [3, 1], [4, 0]]),
         "atb": ["2"], "padoms": "0, 1, ?, 3, 4."},
        {"jaut": "Juris sadalīja 5: 2+3, 5+0, 1+4, 3+2. Cik gadījumu "
                 "trūkst?", "atb": ["2"], "padoms": "Trūkst 0+5 un 4+1."},
        {"jaut": "Cik sadalījumu (ar 0) ir skaitlim 6?", "atb": ["7"],
         "padoms": "No 0+6 līdz 6+0."},
        {"jaut": "Cik sadalījumu (ar 0) ir skaitlim 3?", "atb": ["4"],
         "padoms": "0+3, 1+2, 2+1, 3+0."},
    ]),

    Varianti("Kurš saraksts ir pilns?", [
        {"jaut": "Kurš saraksts skaitlim 3 ir pilns?",
         "opcijas": ["0+3, 1+2, 2+1, 3+0", "1+2, 2+1",
                     "0+3, 1+2, 3+0"],
         "pareizi": 0, "padoms": "Jābūt 4 gadījumiem."},
        {"jaut": "Kā zināt, ka visi gadījumi atrasti?",
         "opcijas": ["kreisā daļa iet 0, 1, 2 ... bez cauruma",
                     "kad apnīk", "kad ir 3 gadījumi"],
         "pareizi": 0, "padoms": "Sakārto pēc kārtas."},
    ]),

    Pasaule("Divas kastes rotaļlietām",
            Ievadi("", [
                {"jaut": "4 lācīši jāsaliek divās kastēs (kaste var būt "
                         "tukša). Cik veidos?", "atb": ["5"],
                 "padoms": "0+4, 1+3, 2+2, 3+1, 4+0."},
            ]),
            pavediens="maja",
            konteksts="Lācīšus var salikt kastēs dažādi.",
            kapec="Sakārtots saraksts parāda visus veidus."),

    Kopsavilkums([
        "Sakārtoju sadalījumus pēc kārtas.",
        "Pamanu, kurš gadījums trūkst.",
        "Zinu, kad visi gadījumi ir atrasti.",
    ]),

    Majas([
        "Uzraksti visus skaitļa 5 sadalījumus pēc kārtas.",
        "Parādi mājiniekam, kā zināt, ka neviens nav aizmirsts.",
        "Cik sadalījumu ir skaitlim 7?",
    ]),
]
