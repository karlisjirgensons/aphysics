# -*- coding: utf-8 -*-
"""2. klase, 28. stunda: «Kā rēķināt uz skaitļu taisnes?»

Saskaitīšana ir lēciens pa labi, atņemšana - pa kreisi. Uz taisnes redz
arī caur 10: vispirms lēciens līdz desmitam, tad atlikums. Tas pats lineāls
ir skaitļu taisne ar centimetriem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Pasaule, Sakums, Varianti, taisne)

TEMA = "Kā rēķināt uz skaitļu taisnes?"

MERKIS = ("Šodien saskaitīsim un atņemsim, lecot pa skaitļu taisni un "
          "lineālu.")

SATURS = [
    Sakums("Kā vardīte izrēķina 7 + 6?",
           zimejums=taisne(0, 20, 1, bultas=[(7, 10, "+3"), (10, 13, "+3")]),
           paraksts="Divi lēcieni: līdz 10 un vēl 3.",
           fakti=["Pieskaitot lec pa labi.",
                  "Atņemot lec pa kreisi.",
                  "Lineāls arī ir skaitļu taisne."]),

    Doma("Lēcieni pa taisni",
         "Sāc pie pirmā skaitļa un lec tik vienību, cik pieskaita vai atņem.",
         soli=[
             "Atrodi sākuma skaitli.",
             "«+» - lec pa labi, «−» - pa kreisi.",
             "Lielu lēcienu sadali: vispirms līdz 10.",
             "Kur apstājies - tā ir atbilde.",
         ]),

    Kustiba("Aizved vardi", [
        {"jaut": "Varde sēž pie 9. Tā lec +5. Kur tā nonāks?", "atb": 14,
         "beigas": 20, "iedala": 2, "objekts": "varde", "merkis": "9 + 5",
         "padoms": "9 + 1 + 4."},
        {"jaut": "Varde pie 16 lec −7. Kur tā nonāks?", "atb": 9,
         "beigas": 20, "iedala": 2, "objekts": "varde", "merkis": "16 − 7",
         "padoms": "16 − 6 − 1."},
        {"jaut": "Varde pie 8 lec +8. Kur tā nonāks?", "atb": 16,
         "beigas": 20, "iedala": 2, "objekts": "varde", "merkis": "8 + 8",
         "padoms": "8 + 2 + 6."},
        {"jaut": "Varde pie 13 lec −6. Kur tā nonāks?", "atb": 7,
         "beigas": 20, "iedala": 2, "objekts": "varde", "merkis": "13 − 6",
         "padoms": "13 − 3 − 3."},
    ], ievads="Ieraksti, kur varde apstāsies, un spied «Palaist»."),

    Varianti("Kāds lēciens?", [
        {"jaut": "Kāda darbība uzzīmēta?",
         "zim": taisne(0, 20, 1, bultas=[(12, 10, "−2"), (10, 7, "−3")]),
         "opcijas": ["12 − 5 = 7", "12 + 5 = 17", "7 + 5 = 12"],
         "pareizi": 0, "padoms": "Lēcieni iet pa kreisi."},
        {"jaut": "Kāda darbība uzzīmēta?",
         "zim": taisne(0, 20, 1, bultas=[(6, 10, "+4"), (10, 15, "+5")]),
         "opcijas": ["6 + 9 = 15", "15 − 9 = 6", "6 + 4 = 10"],
         "pareizi": 0, "padoms": "Saskaiti abus lēcienus."},
    ]),

    Ievadi("Rēķini ar lineālu", [
        {"jaut": "Uz lineāla no 4 cm pa labi par 9 cm. Kur esi?",
         "atb": ["13"], "mers": "cm", "padoms": "4 + 9."},
        {"jaut": "No 15 cm pa kreisi par 8 cm. Kur esi?", "atb": ["7"],
         "mers": "cm", "padoms": "15 − 8."},
    ]),

    Pasaule("Lifts daudzstāvu mājā",
            Ievadi("", [
                {"jaut": "Lifts no 3. stāva brauc 9 stāvus uz augšu. Kurā "
                         "stāvā tas apstāsies?", "atb": ["12"],
                 "padoms": "3 + 9."},
                {"jaut": "No 12. stāva tas brauc 7 stāvus uz leju. Kurā "
                         "stāvā?", "atb": ["5"], "padoms": "12 − 7."},
            ]),
            pavediens="maja",
            konteksts="Lifta pogas ir kā skaitļu taisne, kas stāv vertikāli.",
            kapec="Uz augšu - pieskaiti, uz leju - atņem."),

    Kopsavilkums([
        "Saskaitu, lecot pa skaitļu taisni pa labi.",
        "Atņemu, lecot pa kreisi.",
        "Sadalu lēcienu caur 10.",
    ]),

    Majas([
        "Uzzīmē skaitļu taisni no 0 līdz 20.",
        "Parādi lēcienos 8 + 7 un 15 − 8.",
        "Izdomā vienu lēcienu uzdevumu mājiniekam.",
    ]),
]
