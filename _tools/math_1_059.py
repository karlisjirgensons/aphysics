# -*- coding: utf-8 -*-
"""1. klase, 59. stunda: «Cik dažādus skaitļus var izveidot?»

No cipariem 3, 5 un 7 veido divciparu skaitļus. Lai neaizmirstu nevienu,
kārto pēc desmitiem: 35, 37, 53, 57, 73, 75 - seši (ja ciparus neatkārto).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Cik dažādus skaitļus var izveidot?"

MERKIS = ("Šodien no dotiem cipariem izveidosim visus iespējamos divciparu "
          "skaitļus.")

SATURS = [
    Sakums("No kartītēm 3, 5 un 7 - cik divciparu skaitļu?",
           zimejums=restis([[3, 5, 7]]),
           paraksts="Katru kartīti var likt desmitu vai vienu vietā.",
           fakti=["Pirmā kartīte - desmiti, otrā - vieni.",
                  "Kārto pēc desmitiem, lai neko neaizmirstu.",
                  "Ar 3 kartītēm sanāk 6 skaitļi."]),

    Doma("Kārtīgs saraksts",
         "Izvēlies desmitu ciparu un pieliec visus pārējos vieniem - tad nākamo.",
         soli=[
             "Desmiti 3: 35, 37.",
             "Desmiti 5: 53, 57.",
             "Desmiti 7: 73, 75.",
             "Saskaiti: 6 skaitļi.",
         ]),

    Ievadi("Cik skaitļu?", [
        {"jaut": "Kartītes 2 un 8. Cik divciparu skaitļu?", "atb": ["2"],
         "padoms": "28 un 82."},
        {"jaut": "No 3, 5, 7: lielākais skaitlis?", "atb": ["75"],
         "padoms": "Lielākais cipars desmitos."},
        {"jaut": "No 3, 5, 7: mazākais skaitlis?", "atb": ["35"],
         "padoms": "Mazākais cipars desmitos."},
        {"jaut": "Kurš trūkst: 14, 16, 41, ?, 61, 64", "atb": ["46"],
         "padoms": "Desmiti 4: 41 un ..."},
    ]),

    Varianti("Vai saraksts pilns?", [
        {"jaut": "No 1, 2, 3 Toms uzrakstīja: 12, 13, 21, 31, 32. Kas "
                 "trūkst?", "opcijas": ["23", "33", "11"], "pareizi": 0,
         "padoms": "Desmiti 2: 21 un ..."},
        {"jaut": "Ja kartīti drīkst likt divreiz (33), cik skaitļu no 3 un "
                 "5?", "opcijas": ["4", "2", "6"], "pareizi": 0,
         "padoms": "33, 35, 53, 55."},
    ]),

    Petijums("Kartīšu spēle", [
        "Izgriez 3 kartītes ar cipariem.",
        "Liec pa divām - desmiti un vieni.",
        "Pieraksti katru skaitli tabulā pēc desmitiem.",
        "Pārbaudi: vai ir 6 skaitļi?",
    ], vajag="3 kartītes, zīmulis"),

    Pasaule("Skapīša kods",
            Ievadi("", [
                {"jaut": "Skapīša kods - divi dažādi cipari no 4 un 9. Cik "
                         "kodu jāizmēģina?", "atb": ["2"],
                 "padoms": "49 un 94."},
                {"jaut": "Ja cipari var atkārtoties (44, 99)?",
                 "atb": ["4"], "padoms": "44, 49, 94, 99."},
            ]),
            pavediens="kodi",
            konteksts="Sporta zālē skapītim ir divciparu kods.",
            kapec="Kārtīgs saraksts palīdz izmēģināt visu."),

    Kopsavilkums([
        "Veidoju divciparu skaitļus no dotiem cipariem.",
        "Kārtoju pēc desmitiem, lai neko neaizmirstu.",
        "Atrodu lielāko un mazāko skaitli.",
    ]),

    Majas([
        "No cipariem 1, 4, 6 uzraksti visus divciparu skaitļus.",
        "Kurš ir lielākais? Kurš mazākais?",
        "Izdomā savu divciparu kodu.",
    ]),
]
