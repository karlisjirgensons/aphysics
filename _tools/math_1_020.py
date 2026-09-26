# -*- coding: utf-8 -*-
"""1. klase, 20. stunda: «Cik stāvu ir skaitļa mājiņai?»

Skaitļa mājiņā jumtā ir skaitlis, katrā stāvā - divas daļas. Ja nelieto
0, skaitlim 5 ir 4 stāvi (1+4, 2+3, 3+2, 4+1); stāvu ir par vienu mazāk
nekā skaitlis. Nulli pievienos nākamajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, majina)

TEMA = "Cik stāvu ir skaitļa mājiņai?"

MERKIS = ("Šodien uzbūvēsim skaitļa mājiņu ar visiem sadalījumiem un "
          "saskaitīsim tās stāvus.")


def _pilna(n):
    return majina(n, [(i, n - i) for i in range(1, n)])


SATURS = [
    Sakums("Kāpēc skaitlim 5 ir 4 stāvi?",
           zimejums=_pilna(5),
           paraksts="1 un 4, 2 un 3, 3 un 2, 4 un 1.",
           fakti=["Jumtā - skaitlis.",
                  "Katrā stāvā - divas daļas, kas kopā dod jumta skaitli.",
                  "Stāvus sakārto: kreisā daļa aug pa 1."]),

    Slidnis("Mājiņas aug", [
        {"v": "3", "teksts": "2 stāvi", "zim": _pilna(3)},
        {"v": "4", "teksts": "3 stāvi", "zim": _pilna(4)},
        {"v": "5", "teksts": "4 stāvi", "zim": _pilna(5)},
        {"v": "6", "teksts": "5 stāvi", "zim": _pilna(6)},
    ]),

    Doma("Kā būvēt mājiņu",
         "Sāc ar 1 kreisajā pusē un palielini pa vienam - tā neviens stāvs "
         "nepazudīs.",
         soli=[
             "Pirmajā stāvā kreisajā pusē 1.",
             "Labajā pusē - cik vēl līdz jumta skaitlim.",
             "Katrā nākamajā stāvā kreisā daļa par 1 lielāka.",
             "Beidz, kad labajā pusē paliek 1.",
         ]),

    Ievadi("Aizpildi mājiņu", [
        {"jaut": "Kurš skaitlis trūkst?",
         "zim": majina(6, [(1, 5), (2, 4), (3, None), (4, 2), (5, 1)]),
         "atb": ["3"], "padoms": "3 un vēl cik ir 6?"},
        {"jaut": "Kurš skaitlis trūkst?",
         "zim": majina(7, [(1, 6), (2, 5), (None, 4), (4, 3)]),
         "atb": ["3"], "padoms": "Cik un vēl 4 ir 7?"},
        {"jaut": "Cik stāvu ir skaitļa 8 mājiņai (bez 0)?", "atb": ["7"],
         "padoms": "No 1 un 7 līdz 7 un 1."},
        {"jaut": "Cik stāvu ir skaitļa 10 mājiņai (bez 0)?", "atb": ["9"],
         "padoms": "Par vienu mazāk nekā 10."},
    ]),

    Pasaule("Zivis divos akvārijos",
            Ievadi("", [
                {"jaut": "6 zivis jāsadala divos akvārijos, katrā vismaz "
                         "viena. Cik veidos?", "atb": ["5"],
                 "padoms": "Tik stāvu, cik mājiņai 6."},
            ]),
            pavediens="daba",
            konteksts="Veikalā 6 zivtiņas jāsadala divos akvārijos.",
            kapec="Skaitļa mājiņa parāda visus veidus uzreiz."),

    Kopsavilkums([
        "Būvēju skaitļa mājiņu ar visiem sadalījumiem.",
        "Sakārtoju stāvus, lai neviens nepazūd.",
        "Zinu: bez 0 stāvu ir par vienu mazāk nekā skaitlis.",
    ]),

    Majas([
        "Uzzīmē skaitļa 7 mājiņu.",
        "Cik stāvu būs skaitlim 9? Pārbaudi, uzzīmējot.",
        "Sadali 6 rotaļlietas divos plauktos visos veidos.",
    ]),
]
