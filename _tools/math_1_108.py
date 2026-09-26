# -*- coding: utf-8 -*-
"""1. klase, 108. stunda: «Kā vienu un to pašu pateikt divējādi?»

«Annai ir par 3 vairāk nekā Jānim» un «Jānim ir par 3 mazāk nekā Annai»
apraksta vienu un to pašu. Sloksnēs - tā pati starpība, skatīta no abām
pusēm.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, sloksnes)

TEMA = "Kā vienu un to pašu pateikt divējādi?"

MERKIS = ("Šodien teiksim to pašu divējādi: «par tik vairāk» un «par tik "
          "mazāk».")

_AJ = sloksnes([("Anna", 8), ("Jānis", 5)])

SATURS = [
    Sakums("Annai 8, Jānim 5 - kā to pateikt divējādi?",
           zimejums=_AJ,
           paraksts="Annai par 3 vairāk = Jānim par 3 mazāk.",
           fakti=["Starpība ir viena - 3.",
                  "No Annas puses - «vairāk».",
                  "No Jāņa puses - «mazāk»."]),

    Doma("Divas puses",
         "Ja A ir par 3 lielāks nekā B, tad B ir par 3 mazāks nekā A.",
         soli=[
             "Atrodi starpību.",
             "Lielākajam - «par tik vairāk».",
             "Mazākajam - «par tik mazāk».",
         ]),

    Varianti("Pasaki otrādi", [
        {"jaut": "Toms ir par 2 gadiem vecāks nekā Ilze. Tātad Ilze...",
         "opcijas": ["par 2 gadiem jaunāka", "par 2 gadiem vecāka",
                     "tikpat veca"], "pareizi": 0,
         "padoms": "Otra puse - pretējais vārds."},
        {"jaut": "Zilā sloksne par 4 īsāka nekā sarkanā. Tātad sarkanā...",
         "opcijas": ["par 4 garāka", "par 4 īsāka", "tikpat gara"],
         "pareizi": 0, "padoms": "Pretējais vārds."},
        {"jaut": "Annai 8, Jānim 5. Kurš teikums pareizs?", "zim": _AJ,
         "opcijas": ["Jānim par 3 mazāk", "Jānim par 3 vairāk",
                     "Annai par 5 vairāk"], "pareizi": 0,
         "padoms": "8 − 5 = 3."},
        {"jaut": "Maizē 12 šķēles, kēksā 9. Kēksā...",
         "opcijas": ["par 3 mazāk šķēļu", "par 3 vairāk šķēļu",
                     "tikpat"], "pareizi": 0, "padoms": "12 − 9 = 3."},
    ]),

    Pasaule("Augums",
            Varianti("", [
                {"jaut": "Tētis ir par 60 cm garāks nekā dēls. Kā to pateikt "
                         "no dēla puses?",
                 "opcijas": ["dēls par 60 cm īsāks", "dēls par 60 cm garāks"],
                 "jaukt": False, "pareizi": 0, "padoms": "Pretējais vārds."},
            ]),
            pavediens="maja",
            konteksts="Ģimene mērās pie durvju stenderes.",
            kapec="Viena atšķirība - divi veidi, kā to pateikt."),

    Kopsavilkums([
        "Saku to pašu divējādi.",
        "Zinu: «par tik vairāk» ↔ «par tik mazāk».",
        "Starpība abās pusēs ir tā pati.",
    ]),

    Majas([
        "Salīdzini savu un mājinieka vecumu divējādi.",
        "Pasaki divējādi par diviem priekšmetiem.",
        "Izdomā teikumu pārim «vieglāks - smagāks».",
    ]),
]
