# -*- coding: utf-8 -*-
"""2. klase, 60. stunda: «Cik ilgi notikums turpinājās?»

Ilgums = beigu laiks − sākuma laiks. Ērtāk to rēķina lēcienos pa laika
asi: līdz pilnai stundai, tad pa stundām, tad atlikušās minūtes - tāpat kā
«cik pietrūkst līdz 100».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, pulkstenis, taisne)

TEMA = "Cik ilgi notikums turpinājās?"

MERKIS = ("Šodien aprēķināsim notikuma ilgumu, ja zināms sākuma un beigu "
          "laiks.")

SATURS = [
    Sakums("Futbola spēle sākās 17:00 un beidzās 18:45. Cik ilgi tā "
           "turpinājās?",
           zimejums=taisne(17, 19, 1, bultas=[(17, 18, "1 h"),
                                              (18, 18.75, "45 min")]),
           paraksts="1 stunda un 45 minūtes.",
           fakti=["Ilgums ir laiks no sākuma līdz beigām.",
                  "Vispirms veselas stundas, tad minūtes.",
                  "1 h ir 1 stunda, 1 min - 1 minūte."]),

    Doma("Ilgums lēcienos",
         "No sākuma līdz beigām lec: līdz pilnai stundai, pa stundām, "
         "minūtes.",
         soli=[
             "Sākums 9:40, beigas 11:15.",
             "No 9:40 līdz 10:00 - 20 min.",
             "No 10:00 līdz 11:00 - 1 h.",
             "No 11:00 līdz 11:15 - 15 min. Kopā 1 h 35 min.",
         ]),

    Paraugs("Cik ilgi ilga mācību stunda?",
            uzd="Stunda sākās 8:30 un beidzās 9:10.",
            soli=[("8:30 → 9:00 = 30 min", "Līdz pilnai stundai."),
                  ("9:00 → 9:10 = 10 min", "Atlikums."),
                  ("30 min + 10 min = 40 min", "Kopā.")],
            atbilde="40 minūtes"),

    Ievadi("Cik ilgi?", [
        {"jaut": "No 14:00 līdz 16:00. Cik stundu?", "atb": ["2"],
         "mers": "h", "padoms": "16 − 14."},
        {"jaut": "No 10:15 līdz 10:50. Cik minūšu?", "atb": ["35"],
         "mers": "min", "padoms": "50 − 15."},
        {"jaut": "No 8:45 līdz 9:15. Cik minūšu?", "atb": ["30"],
         "mers": "min", "padoms": "15 + 15."},
        {"jaut": "No 12:30 līdz 13:00. Cik minūšu?", "atb": ["30"],
         "mers": "min", "padoms": "Līdz pilnai stundai."},
        {"jaut": "No 7:50 līdz 8:20. Cik minūšu?", "atb": ["30"],
         "mers": "min", "padoms": "10 + 20."},
        {"jaut": "No 15:20 līdz 15:58. Cik minūšu?", "atb": ["38"],
         "mers": "min", "padoms": "58 − 20."},
    ], pamats=4),

    Varianti("Nolasi pulksteņus", [
        {"jaut": "Sāka, kad pulkstenis rādīja 3:00, beidza - šo laiku. Cik "
                 "ilgi?", "zim": pulkstenis(3, 25),
         "opcijas": ["25 min", "3 h 25 min", "35 min"], "pareizi": 0,
         "padoms": "No 3:00 līdz 3:25."},
        {"jaut": "Filma sākās 18:10 un ilga 1 h 20 min. Vai tā beidzās "
                 "19:30?", "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "18:10 + 1 h = 19:10, + 20 min."},
    ]),

    Pasaule("Cik ilgi brauca vilciens?",
            Ievadi("", [
                {"jaut": "Vilciens no Rīgas atiet 9:15 un pienāk Siguldā "
                         "10:20. Cik minūšu virs stundas?", "atb": ["5"],
                 "mers": "min", "padoms": "1 h un vēl 5 min."},
                {"jaut": "Cik tas ir minūtēs kopā?", "atb": ["65"],
                 "mers": "min", "padoms": "60 + 5."},
            ]),
            pavediens="celojums",
            konteksts="Vilcienu sarakstā ir tikai atiešanas un pienākšanas "
                      "laiki.",
            kapec="Ceļa ilgumu jāizrēķina pašam."),

    Kopsavilkums([
        "Aprēķinu ilgumu no sākuma līdz beigām.",
        "Lecu līdz pilnai stundai, pa stundām, tad minūtes.",
        "Pierakstu ilgumu stundās un minūtēs.",
    ]),

    Majas([
        "Pieraksti, cikos sāc un cikos beidz mājasdarbus.",
        "Aprēķini, cik ilgi tie aizņēma.",
        "Dari tā trīs dienas un salīdzini.",
    ]),
]
