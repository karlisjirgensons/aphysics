# -*- coding: utf-8 -*-
"""1. klase, 107. stunda: «Par cik viena sloksnīte garāka nekā otra?»

Divas sloksnītes noliek vienu zem otras no viena sākuma: garākās «lieko»
galu saskaita - tas ir, par cik tā garāka. Aprēķinā - atņemšana: 9 − 5 = 4.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals, sloksnes)

TEMA = "Par cik viena sloksnīte garāka nekā otra?"

MERKIS = ("Šodien ar sloksnītēm un lineālu noteiksim, par cik viens skaitlis "
          "ir lielāks nekā otrs.")

SATURS = [
    Sakums("Sarkanā 9 rūtiņas, zilā 5. Par cik sarkanā garāka?",
           zimejums=sloksnes([("sarkanā", 9), ("zilā", 5)]),
           paraksts="Oranžās rūtiņas - «liekais» gals: 4.",
           fakti=["Noliec sloksnītes no viena sākuma.",
                  "Saskaiti garākās lieko galu.",
                  "Aprēķinā: 9 − 5 = 4."]),

    Doma("Par cik garāka",
         "«Par cik vairāk» atrod ar atņemšanu: lielākais − mazākais.",
         soli=[
             "Noliec abas no viena gala.",
             "Atrodi, kur īsākā beidzas.",
             "Saskaiti garākās atlikušās rūtiņas.",
             "Pieraksti: 9 − 5 = 4.",
         ]),

    Ievadi("Par cik garāka?", [
        {"jaut": "Par cik augšējā garāka?",
         "zim": sloksnes([("A", 7), ("B", 4)]), "atb": ["3"],
         "padoms": "7 − 4."},
        {"jaut": "Par cik augšējā garāka?",
         "zim": sloksnes([("A", 12), ("B", 8)]), "atb": ["4"],
         "padoms": "12 − 8."},
        {"jaut": "Par cik apakšējā garāka?",
         "zim": sloksnes([("A", 6), ("B", 11)]), "atb": ["5"],
         "padoms": "11 − 6."},
        {"jaut": "Lente 15 cm, otra 9 cm. Par cik cm pirmā garāka?",
         "zim": lineals(20, [(0, 15, "15 cm"), (0, 9, "9 cm")]),
         "atb": ["6"], "padoms": "15 − 9."},
    ]),

    Varianti("Kā atrast?", [
        {"jaut": "Par cik 14 ir lielāks nekā 10?",
         "opcijas": ["14 − 10", "14 + 10", "10 − 14"], "pareizi": 0,
         "padoms": "Lielākais − mazākais."},
    ]),

    Petijums("Sloksnītes klasē", [
        "Izgriez divas papīra sloksnītes: 12 cm un 7 cm.",
        "Noliec tās no viena gala.",
        "Izmēri lieko galu ar lineālu.",
        "Pārbaudi: 12 − 7 = ?",
    ], vajag="papīrs, šķēres, lineāls"),

    Pasaule("Kurš izaudzis vairāk?",
            Ievadi("", [
                {"jaut": "Gurķis izaudzis 16 cm, cukīni 9 cm. Par cik cm "
                         "gurķis garāks?", "atb": ["7"], "padoms": "16 − 9."},
            ]),
            pavediens="daba",
            konteksts="Skolas dārzā mēra dārzeņus.",
            kapec="Starpība parāda, par cik viens pārspēj otru."),

    Kopsavilkums([
        "Salīdzinu sloksnītes no viena sākuma.",
        "Nosaku, par cik viena garāka.",
        "Pierakstu to ar atņemšanu.",
    ]),

    Majas([
        "Izmēri divus zīmuļus un atrodi, par cik viens garāks.",
        "Salīdzini savu un mājinieka plaukstu.",
        "Pieraksti ar atņemšanu.",
    ]),
]
