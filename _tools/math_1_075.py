# -*- coding: utf-8 -*-
"""1. klase, 75. stunda: «Cik garš ir metrs?»

Metrs ir 100 cm - apmēram no pirkstu galiem līdz pretējam plecam
pieaugušajam. Pirmklasnieks ir mazliet garāks nekā metrs. Vispirms
novērtē, tad izmēra ar metramēru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kolonnas)

TEMA = "Cik garš ir metrs?"

MERKIS = ("Šodien salīdzināsim metru ar savu augumu un klases priekšmetiem "
          "un pārbaudīsim, izmērot.")

_AUGUMI = kolonnas([("metrs", 100), ("Anna", 121), ("galds", 76),
                    ("durvis", 200)], " cm")

SATURS = [
    Sakums("Vai tu esi garāks par metru?",
           zimejums=_AUGUMI,
           paraksts="Anna - 121 cm, mazliet vairāk nekā metrs.",
           fakti=["1 m = 100 cm.",
                  "Galds ir zemāks par metru.",
                  "Durvis - apmēram divi metri."]),

    Doma("Metrs ar acīm un ar metramēru",
         "Vispirms novērtē - vairāk vai mazāk nekā metrs -, tad izmēri.",
         soli=[
             "Iedomājies metru: līdz tavam vēderam/krūtīm.",
             "Novērtē: vairāk vai mazāk?",
             "Izmēri ar metramēru.",
         ]),

    Varianti("Vairāk vai mazāk nekā 1 m?", [
        {"jaut": "Krēsla augstums", "opcijas": ["mazāk", "vairāk"],
         "jaukt": False, "pareizi": 0, "padoms": "Krēsls ir zems."},
        {"jaut": "Tāfeles garums", "opcijas": ["vairāk", "mazāk"],
         "jaukt": False, "pareizi": 0, "padoms": "Tāfele ir gara."},
        {"jaut": "Zīmuļa garums", "opcijas": ["mazāk", "vairāk"],
         "jaukt": False, "pareizi": 0, "padoms": "Apmēram 15 cm."},
        {"jaut": "Skolotājas augums", "opcijas": ["vairāk", "mazāk"],
         "jaukt": False, "pareizi": 0, "padoms": "Pieaugušais."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Anna ir 121 cm. Par cik cm garāka par metru?",
         "atb": ["21"], "padoms": "121 − 100."},
        {"jaut": "Galds 76 cm. Cik cm līdz metram?", "zim": _AUGUMI,
         "atb": ["24"], "padoms": "No 76 līdz 100."},
        {"jaut": "Cik metru garas ir durvis (200 cm)?", "atb": ["2"],
         "padoms": "100 + 100."},
    ]),

    Petijums("Metrs klasē", [
        "Atrodi klasē 3 lietas, kas, tavuprāt, ir apmēram 1 m.",
        "Izmēri tās ar metramēru.",
        "Izmēri savu augumu pie sienas.",
        "Salīdzini ar metru.",
    ], vajag="metramērs vai mērlente"),

    Pasaule("Atrakcija atrakciju parkā",
            Varianti("", [
                {"jaut": "Karuselī drīkst braukt bērni, kas garāki par 1 m. "
                         "Jānis ir 98 cm. Vai drīkst?",
                 "opcijas": ["Vēl nē", "Jā"], "jaukt": False, "pareizi": 0,
                 "padoms": "98 < 100."},
                {"jaut": "Liene ir 1 m 10 cm. Vai drīkst?",
                 "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
                 "padoms": "110 > 100."},
            ]),
            pavediens="sports",
            konteksts="Atrakciju parkā pie ieejas ir atzīme 1 m.",
            kapec="Metrs noder drošībai."),

    Kopsavilkums([
        "Zinu, ka 1 m = 100 cm.",
        "Novērtēju, vai kas ir garāks vai īsāks par metru.",
        "Mēru ar metramēru.",
    ]),

    Majas([
        "Izmēri savu augumu mājās pie durvju stenderes.",
        "Atrodi mājās lietu, kas ir tieši apmēram 1 m.",
        "Noej 1 m ar soļiem - cik soļu?",
    ]),
]
