# -*- coding: utf-8 -*-
"""4. klase, 45. stunda: «Cik maksā deviņi bloki?»

Proporcionāli lielumi pirmo reizi: ja 4 bloki maksā 36 €, tad viens - 9 €,
bet deviņi - 81 €. Vispirms atrod vienu, tad cik vajag («caur vienu»).
Shematisks zīmējums ar vienādiem nodalījumiem padara to redzamu. Šī pati
doma 4.8. temata sākumā kļūs par cenu, skaitu un samaksu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Cik maksā deviņi bloki?"

MERKIS = ("Risināsim uzdevumus par proporcionāliem lielumiem, veidojot "
          "shematisku zīmējumu.")

SATURS = [
    Sakums("4 konstruktora bloki maksā 36 €. Cik maksā 9?",
           zimejums=restis([["4 bloki", "36 €"],
                            ["1 bloks", "36 : 4 = 9 €"],
                            ["9 bloki", "9 · 9 = 81 €"]],
                           "caur vienu"),
           paraksts="Vispirms viens, tad cik vajag.",
           fakti=["Ja visi bloki vienādi, katrs maksā tikpat.",
                  "Tāpēc der ceļš «caur vienu»."]),

    Doma("Atrodi vienu, tad reizini",
         "Ja lielumi ir proporcionāli, vienas vienības vērtību atrod ar "
         "dalīšanu, bet vajadzīgo - ar reizināšanu.",
         soli=[
             "Nosaki, kas ir zināms: 4 bloki - 36 €.",
             "Atrodi vienu: 36 : 4 = 9 €.",
             "Reizini ar vajadzīgo skaitu: 9 · 9 = 81 €.",
             "Pārbaudi: vairāk bloku - vairāk naudas.",
         ],
         pieze="Zīmējumā 4 vienādas rūtiņas ir 36; viena rūtiņa 9; 9 rūtiņas "
               "81."),

    Paraugs("5 burtnīcas maksā 4 € 50 ct",
            uzd="5 burtnīcas maksā 450 ct. Cik maksā 7 burtnīcas?",
            soli=[
                ("450 : 5 = 90", "Viena burtnīca - 90 ct."),
                ("90 · 7 = 630", "Septiņas."),
            ],
            atbilde="630 ct = 6 € 30 ct"),

    Slidnis("Caur vienu",
            soli=[
                {"v": "4 bloki - 36 €", "teksts": "Zināmais.", "josla": 44},
                {"v": "1 bloks - 9 €", "teksts": "Dala ar 4.", "josla": 11},
                {"v": "9 bloki - 81 €", "teksts": "Reizina ar 9.",
                 "josla": 100},
            ],
            ievads="Josla parāda cenu: vispirms saraujas līdz vienam, tad "
                   "izaug."),

    Ievadi("Caur vienu", [
        {"jaut": "3 kg ābolu maksā 6 €. Cik maksā 5 kg?", "atb": ["10"],
         "padoms": "6 : 3 = 2 €; 2 · 5."},
        {"jaut": "6 biļetes maksā 48 €. Cik maksā 4 biļetes?", "atb": ["32"],
         "padoms": "48 : 6 = 8; 8 · 4."},
        {"jaut": "Auto 3 stundās nobrauc 240 km. Cik km 5 stundās?",
         "atb": ["400"], "padoms": "240 : 3 = 80; 80 · 5."},
        {"jaut": "8 pildspalvas maksā 96 ct. Cik maksā 3?", "atb": ["36"],
         "padoms": "96 : 8 = 12."},
        {"jaut": "Printeris 4 minūtēs izdrukā 100 lapas. Cik 7 minūtēs?",
         "atb": ["175"], "padoms": "100 : 4 = 25."},
        {"jaut": "7 dienās izlasīja 91 lpp. Cik 3 dienās?", "atb": ["39"],
         "padoms": "91 : 7 = 13."},
    ], pamats=4),

    Varianti("Vai der «caur vienu»?", [
        {"jaut": "3 maizes 4 € 50 ct. Cik maksā 6 maizes?",
         "opcijas": ["9 €", "6 €", "4 € 50 ct", "13 € 50 ct"],
         "pareizi": 0, "padoms": "Divreiz vairāk - divreiz dārgāk."},
        {"jaut": "Kurā situācijā *nevar* rēķināt «caur vienu»?",
         "opcijas": ["Viens bērns 10 gadi - cik gadu 3 bērniem?",
                     "1 kg maksā 3 € - cik 4 kg?",
                     "1 stundā 60 km - cik 2 stundās?"], "pareizi": 0,
         "padoms": "Vecums nesaskaitās tā."},
        {"jaut": "5 bloki 45 €. Cik maksā viens?",
         "opcijas": ["9 €", "40 €", "50 €", "5 €"], "pareizi": 0,
         "padoms": "45 : 5."},
    ]),

    Pasaule("Robotikas pulciņa iepirkums",
            Ievadi("", [
                {"jaut": "4 motori maksā 36 €. Cik maksā 9 motori?",
                 "atb": ["81"], "padoms": "36 : 4 · 9."},
                {"jaut": "6 sensori maksā 54 €. Cik maksā 8 sensori?",
                 "atb": ["72"], "padoms": "54 : 6 = 9."},
                {"jaut": "3 baterijas maksā 12 €. Cik maksā 10?",
                 "atb": ["40"], "padoms": "12 : 3 = 4."},
                {"jaut": "Cik maksā viss pirkums: 9 motori, 8 sensori un 10 "
                         "baterijas?",
                 "atb": ["193"], "padoms": "81 + 72 + 40."},
            ]),
            pavediens="tehnika",
            konteksts="Pulciņš būvē robotus - detaļas pērk dažādā skaitā, "
                      "bet cenas ir par iepakojumu.",
            kapec="Kas zina cenu vienai detaļai, tas izrēķina jebkuru "
                  "pasūtījumu."),

    Kopsavilkums([
        "Atrodu vienas vienības vērtību ar dalīšanu.",
        "Atrodu vajadzīgo vērtību ar reizināšanu.",
        "Zīmēju shēmu ar vienādām daļām.",
        "Pamanu, kad «caur vienu» neder.",
    ]),

    Majas([
        "Veikalā atrodi preci, kas pārdod iepakojumā, un izrēķini vienas "
        "cenu.",
        "Izrēķini, cik maksās 9 saldējumi, ja 3 maksā 4 € 50 ct.",
        "Izdomā «caur vienu» uzdevumu par savu hobiju.",
    ]),
]
