# -*- coding: utf-8 -*-
"""1. klase, 97. stunda: «Kā pārbaudīt starpību?»

Starpību pārbauda ar saskaitīšanu: ja 15 − 7 = 8, tad 8 + 7 jābūt 15.
Ja nesanāk - kļūda ir atņemšanā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, majina)

TEMA = "Kā pārbaudīt starpību?"

MERKIS = ("Šodien pārbaudīsim atņemšanas rezultātu ar saskaitīšanu.")

SATURS = [
    Sakums("15 − 7 = 8. Vai tiešām?",
           zimejums=majina(15, [(8, 7)]),
           paraksts="8 + 7 = 15 - pareizi!",
           fakti=["Starpība + atņemamais = sākuma skaitlis.",
                  "Ja sakrīt - pareizi.",
                  "Ja nē - meklē kļūdu."]),

    Doma("Pārbaude ar saskaitīšanu",
         "Tas, kas palika, un tas, ko atņēma, kopā ir tas, kas bija.",
         soli=[
             "Izrēķini starpību.",
             "Pieskaiti atņemamo.",
             "Salīdzini ar sākuma skaitli.",
         ]),

    Ievadi("Pārbaudi", [
        {"jaut": "16 − 9 = 7. Pārbaude: 7 + 9 = ?", "atb": ["16"],
         "padoms": "Jāsanāk 16."},
        {"jaut": "13 − 5 = 8. Pārbaude: 8 + 5 = ?", "atb": ["13"],
         "padoms": "Jāsanāk 13."},
        {"jaut": "11 − 3 = 8. Pārbaude: 8 + 3 = ?", "atb": ["11"],
         "padoms": "Jāsanāk 11."},
    ]),

    Varianti("Vai pareizi?", [
        {"jaut": "14 − 6 = 9. Pārbaude 9 + 6 = 15.",
         "opcijas": ["kļūda - jābūt 8", "pareizi"], "jaukt": False,
         "pareizi": 0, "padoms": "15 nav 14."},
        {"jaut": "17 − 8 = 9. Pārbaude 9 + 8 = 17.",
         "opcijas": ["pareizi", "kļūda"], "jaukt": False, "pareizi": 0,
         "padoms": "Sakrīt."},
        {"jaut": "12 − 4 = 7. Pārbaude 7 + 4 = 11.",
         "opcijas": ["kļūda - jābūt 8", "pareizi"], "jaukt": False,
         "pareizi": 0, "padoms": "11 nav 12."},
    ]),

    Pasaule("Atlikums veikalā",
            Ievadi("", [
                {"jaut": "Tev bija 15 €, nopirki par 8 €. Palika 7 €. "
                         "Pārbaude: 7 + 8 = ?", "atb": ["15"],
                 "padoms": "Jāsanāk 15."},
            ]),
            pavediens="veikals",
            konteksts="Pārdevēja izdod atlikumu.",
            kapec="Pārbaudi atlikumu - vai tev iedeva pareizi."),

    Kopsavilkums([
        "Pārbaudu starpību ar saskaitīšanu.",
        "Atrodu kļūdu, ja nesakrīt.",
        "Izlaboju rezultātu.",
    ]),

    Majas([
        "Izrēķini 3 starpības un pārbaudi.",
        "Pārbaudi mājinieka atņemšanu.",
        "Paskaidro, kāpēc pārbaude strādā.",
    ]),
]
