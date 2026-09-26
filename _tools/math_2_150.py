# -*- coding: utf-8 -*-
"""2. klase, 150. stunda: «Cik gara ir visu šķautņu summa?»

Perimetra ideja telpiskai figūrai: kubam ir 12 vienādas šķautnes, tāpēc
visu šķautņu garums ir 12 reizes viena šķautne; kvadrātam - 4 vienādas
malas: P = 4 · a. Reizināšana saīsina perimetru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kermenis)

TEMA = "Cik gara ir visu šķautņu summa?"

MERKIS = ("Šodien ar saskaitīšanu un reizināšanu noteiksim figūras malu vai "
          "šķautņu garumu summu.")

SATURS = [
    Sakums("Cik stieples vajag kuba karkasam?",
           zimejums=kermenis("kubs"),
           paraksts="Kubam 12 vienādas šķautnes.",
           fakti=["Ja šķautne 5 cm - stieples 12 · 5 = 60 cm.",
                  "4 augšā, 4 apakšā, 4 sānos.",
                  "Vienādas malas - reizina."]),

    Doma("Vienādas malas - reizini",
         "Ja visas malas vai šķautnes vienādas, summu aprēķina ar "
         "reizināšanu.",
         soli=[
             "Saskaiti vienādās malas.",
             "Izmēri vienu.",
             "Reizini: skaits · garums.",
             "Kubam: 12 šķautnes = 4 + 4 + 4.",
         ]),

    Paraugs("Kvadrāta perimetrs",
            uzd="Kvadrāta mala 5 cm.",
            soli=[("P = 5 + 5 + 5 + 5", "Summa."),
                  ("P = 4 · 5 = 20 cm", "Reizinājums.")],
            atbilde="20 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Kvadrāts ar malu 7 cm. P = ?", "atb": ["28"], "mers": "cm",
         "padoms": "4 · 7."},
        {"jaut": "Trijstūris, visas malas 9 cm. P = ?", "atb": ["27"],
         "mers": "cm", "padoms": "3 · 9."},
        {"jaut": "Piecstūris, visas malas 6 cm. P = ?", "atb": ["30"],
         "mers": "cm", "padoms": "5 · 6."},
        {"jaut": "Kubs, šķautne 2 cm. Visu 12 šķautņu summa?",
         "zim": kermenis("kubs"), "atb": ["24"], "mers": "cm",
         "padoms": "4 · 2 = 8, trīs reizes."},
        {"jaut": "Kubs, šķautne 3 cm. Visu šķautņu summa?", "atb": ["36"],
         "mers": "cm", "padoms": "4 · 3 = 12, 12 + 12 + 12."},
        {"jaut": "Kvadrāta P = 36 cm. Mala?", "atb": ["9"], "mers": "cm",
         "padoms": "4 · ? = 36."},
    ], pamats=4),

    Varianti("Cik vienādu malu?", [
        {"jaut": "Kvadrātam", "opcijas": ["4", "3", "12"], "pareizi": 0,
         "padoms": "4 malas."},
        {"jaut": "Kuba šķautnes", "zim": kermenis("kubs"),
         "opcijas": ["12", "8", "6"], "pareizi": 0,
         "padoms": "4 + 4 + 4."},
    ]),

    Pasaule("Spēļu kubs no salmiņiem",
            Ievadi("", [
                {"jaut": "Kuba karkasam katrs salmiņš 5 cm. Cik salmiņu "
                         "vajag?", "atb": ["12"], "padoms": "Tik, cik šķautņu."},
                {"jaut": "Cik cm salmiņu kopā?", "atb": ["60"], "mers": "cm",
                 "padoms": "12 · 5 = 4 · 5 trīs reizes: 20 + 20 + 20."},
            ]),
            pavediens="tehnika",
            konteksts="No salmiņiem un plastilīna būvē figūru karkasus.",
            kapec="Reizinājums pasaka, cik materiāla vajag."),

    Kopsavilkums([
        "Aprēķinu malu summu ar reizināšanu, ja malas vienādas.",
        "Zinu, ka kubam 12 šķautnes.",
        "Atrodu malu, ja zināms perimetrs.",
    ]),

    Majas([
        "No salmiņiem vai zīmuļiem saliec kvadrātu un trijstūri.",
        "Izmēri un aprēķini perimetru ar reizināšanu.",
        "Cik zīmuļu vajadzētu kubam?",
    ]),
]
