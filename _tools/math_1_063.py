# -*- coding: utf-8 -*-
"""1. klase, 63. stunda: «Ko nozīmē zīmes «<» un «>»?»

Zīmes «<» un «>» - atvērtā puse vienmēr pret lielāko skaitli. 35 < 53
lasa «35 ir mazāks nekā 53», no otras puses - «53 ir lielāks nekā 35».
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Ko nozīmē zīmes «<» un «>»?"

MERKIS = ("Šodien lietosim zīmes «<» un «>» un lasīsim pierakstu no abām "
          "pusēm.")


def _zime(a, b):
    pareiza = "<" if a < b else ">" if a > b else "="
    return {"jaut": "%d ? %d" % (a, b), "opcijas": ["<", ">", "="],
            "jaukt": False, "pareizi": ["<", ">", "="].index(pareiza),
            "padoms": "Atvērtā puse pret lielāko."}


SATURS = [
    Sakums("Kurā pusē «mute» ir atvērta?",
           zimejums=restis([[35, "<", 53]]),
           paraksts="35 < 53 - atvērtā puse pret lielāko.",
           fakti=["«<» lasa «ir mazāks nekā».",
                  "«>» lasa «ir lielāks nekā».",
                  "Atvērtā puse vienmēr pret lielāko."]),

    Doma("Zīme starp skaitļiem",
         "Smailais gals rāda uz mazāko, atvērtā puse - uz lielāko.",
         soli=[
             "Salīdzini skaitļus.",
             "Pagriez zīmi ar atvērto pusi pret lielāko.",
             "Vienādi? Liec «=».",
             "Izlasi no kreisās un no labās puses.",
         ]),

    Varianti("Liec zīmi", [
        _zime(35, 53), _zime(71, 68), _zime(40, 40), _zime(19, 91),
        _zime(88, 80), _zime(26, 62),
    ], pamats=4),

    Varianti("Izlasi", [
        {"jaut": "Kā izlasīt 72 > 27?",
         "opcijas": ["72 ir lielāks nekā 27", "72 ir mazāks nekā 27",
                     "72 ir vienāds ar 27"], "pareizi": 0,
         "padoms": "«>» - lielāks."},
        {"jaut": "Tas pats no labās: 27 ... 72",
         "opcijas": ["27 ir mazāks nekā 72", "27 ir lielāks nekā 72"],
         "jaukt": False, "pareizi": 0, "padoms": "No otras puses - «<»."},
    ]),

    Pasaule("Cenu salīdzināšana",
            Varianti("", [
                {"jaut": "Ābolu sula 89 c, apelsīnu sula 98 c. 89 ? 98",
                 "opcijas": ["<", ">", "="], "jaukt": False, "pareizi": 0,
                 "padoms": "8 desmiti < 9 desmiti."},
                {"jaut": "Kura sula lētāka?",
                 "opcijas": ["ābolu", "apelsīnu"], "jaukt": False,
                 "pareizi": 0, "padoms": "Mazākā cena."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā cenas salīdzina, lai izvēlētos.",
            kapec="Zīme īsi pasaka, kurš ir mazāks."),

    Kopsavilkums([
        "Lietoju zīmes «<», «>» un «=».",
        "Pagriežu atvērto pusi pret lielāko.",
        "Lasu pierakstu no abām pusēm.",
    ]),

    Majas([
        "Uzraksti 3 pierakstus ar «<» un 3 ar «>».",
        "Salīdzini savu un mājinieka vecumu ar zīmi.",
        "Izlasi katru pierakstu no abām pusēm.",
    ]),
]
