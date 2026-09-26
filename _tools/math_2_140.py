# -*- coding: utf-8 -*-
"""2. klase, 140. stunda: «Vai 3 · 4 un 4 · 3 ir vienādi?»

Reizinātāju vietas maiņa: taisnstūris 3 rindās pa 4, pagriezts, ir 4 rindas
pa 3 - rūtiņu skaits nemainās. Tāpēc katru reizinājumu pietiek iemācīties
vienu reizi - 3 · 7 ir tas pats, kas 7 · 3.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, rutinas)

TEMA = "Vai 3 · 4 un 4 · 3 ir vienādi?"

MERKIS = ("Šodien ar taisnstūra modeli paskaidrosim, kāpēc reizinātāju "
          "secība nemaina rezultātu.")

SATURS = [
    Sakums("Pagriez šokolādi - vai gabaliņu kļūst vairāk?",
           zimejums=rutinas(4, 3),
           paraksts="3 rindas pa 4 = 12. Pagriežot - 4 rindas pa 3 = 12.",
           fakti=["Pagriežot rūtiņas nepazūd.",
                  "3 · 4 = 4 · 3 = 12.",
                  "Reizinātājus var samainīt vietām."]),

    Doma("Vietas maiņa",
         "Reizinātāju vietas maiņa reizinājumu nemaina.",
         soli=[
             "Uzzīmē 3 rindas pa 4.",
             "Pagriez - 4 rindas pa 3.",
             "Rūtiņu skaits tas pats: 12.",
             "Tāpat saskaitīšanā: 3 + 4 = 4 + 3.",
         ],
         pieze="Tas atvieglo darbu: ja zini 2 · 9, tu zini arī 9 · 2."),

    Slidnis("Pagriežam", [
        {"v": "3 · 4 = 12", "teksts": "3 rindas pa 4.",
         "zim": rutinas(4, 3)},
        {"v": "4 · 3 = 12", "teksts": "4 rindas pa 3 - tas pats!",
         "zim": rutinas(3, 4)},
    ]),

    Ievadi("Izmanto vietas maiņu", [
        {"jaut": "Ja 3 · 7 = 21, tad 7 · 3 = ?", "atb": ["21"],
         "padoms": "Samainīti."},
        {"jaut": "9 · 3 = ?", "atb": ["27"], "padoms": "3 · 9."},
        {"jaut": "8 · 3 = ?", "atb": ["24"], "padoms": "3 · 8."},
        {"jaut": "10 · 3 = ?", "atb": ["30"], "padoms": "3 · 10."},
        {"jaut": "6 · 3 = ?", "atb": ["18"], "padoms": "3 · 6."},
        {"jaut": "5 · 2 = 2 · ?", "atb": ["5"], "padoms": "Samaini."},
    ], pamats=4),

    Varianti("Vienāds vai nē?", [
        {"jaut": "3 · 5 ☐ 5 · 3", "opcijas": ["=", "<", ">"],
         "jaukt": False, "pareizi": 0, "padoms": "Vietas maiņa."},
        {"jaut": "2 · 8 ☐ 8 · 3", "opcijas": ["=", "<", ">"],
         "jaukt": False, "pareizi": 1, "padoms": "16 un 24."},
        {"jaut": "Vai 10 − 3 = 3 − 10?", "opcijas": ["Nē", "Jā"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Atņemšanā vietas mainīt nedrīkst."},
        {"jaut": "Vai 4 · 3 = 3 · 4?", "opcijas": ["Jā", "Nē"],
         "jaukt": False, "pareizi": 0, "padoms": "Reizināšanā drīkst."},
    ]),

    Pasaule("Kinozāle",
            Ievadi("", [
                {"jaut": "Kinozālē 3 rindas pa 9 krēsliem. Cik krēslu?",
                 "atb": ["27"], "padoms": "3 · 9."},
                {"jaut": "Otrā zālē 9 rindas pa 3 krēsliem. Cik krēslu?",
                 "atb": ["27"], "padoms": "9 · 3 = 3 · 9."},
            ]),
            pavediens="skola",
            konteksts="Skolas zālēs krēsli izkārtoti rindās.",
            kapec="Dažāds izkārtojums - tikpat vietu."),

    Kopsavilkums([
        "Zinu, ka reizinātājus var samainīt vietām.",
        "Paskaidroju to ar taisnstūri.",
        "Izmantoju to, lai rēķinātu vieglāk.",
    ]),

    Majas([
        "Noliec 12 monētas 3 rindās pa 4.",
        "Pārkārto 4 rindās pa 3.",
        "Pastāsti mājiniekam, ko tas pierāda.",
    ]),
]
