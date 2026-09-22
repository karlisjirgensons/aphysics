# -*- coding: utf-8 -*-
"""5. klase, 147. stunda: «Kā aprēķināt procentus no skaitļa?»

Pirmais īstais procentu rēķins, un tas nav jauns: procenti ir daļa, tāpēc
der 74. stundas paņēmiens - dali ar saucēju, reizini ar skaitītāju. Vienīgā
atšķirība ir tā, ka saucējs vienmēr ir 100. Shēma te ir obligāta: tā pasaka,
kas ir veselais.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kā aprēķināt procentus no skaitļa?"

MERKIS = ("Iemācīsimies aprēķināt procentus no veselā, veidojot shematisku "
          "zīmējumu.")

SATURS = [
    Sakums("Divdesmit procenti no 80 eiro",
           zimejums=dala(10, 2, "20 % no cenas"),
           paraksts="Visa josla ir 80 €, divas desmitdaļas no tās - 16 €.",
           fakti=["Visa josla vienmēr ir 100 %.",
                  "20 % ir viena piektdaļa joslas.",
                  "Vispirms atrod 1 %, tad reizina."]),

    Doma("Vispirms viens procents",
         "Procentus no skaitļa aprēķina, veselo dalot ar 100 un reizinot ar "
         "procentu skaitu; biežāk lietotos procentus ērtāk rēķināt kā daļu.",
         soli=[
             "Uzzīmē joslu - tā ir 100 %.",
             "Atzīmē, kura daļa jāatrod.",
             "Dali veselo ar 100 - iegūsi vienu procentu.",
             "Reizini ar procentu skaitu.",
             "Vai arī pārtulko procentus daļā un dali uzreiz.",
         ],
         pieze="20 % no 80 var rēķināt divējādi: 80 : 100 · 20 = 16 vai "
               "{1|5} no 80 = 16. Otrais ceļš ir īsāks, bet der tikai "
               "biežāk lietotajiem procentiem."),

    Paraugs("Cik ir 20 % no 80 €?",
            uzd="Aprēķini atlaidi.",
            soli=[
                ("Visa summa 80 € ir 100 %",
                 "Veselais."),
                ("80 : 100 = 0,8 (€)",
                 "Viens procents."),
                ("0,8 · 20 = 16 (€)",
                 "Divdesmit procenti."),
                ("Vai arī: 20 % = {1|5}, 80 : 5 = 16",
                 "Īsākais ceļš."),
            ],
            atbilde="20 % no 80 € ir 16 €"),

    Ievadi("Aprēķini procentus", [
        {"jaut": "Cik ir 20 % no 80? Ieraksti skaitli.",
         "atb": ["16"], "padoms": "80 : 5."},
        {"jaut": "Cik ir 25 % no 80?",
         "atb": ["20"], "padoms": "80 : 4."},
        {"jaut": "Cik ir 50 % no 80?",
         "atb": ["40"], "padoms": "80 : 2."},
        {"jaut": "Cik ir 10 % no 250?",
         "atb": ["25"], "padoms": "250 : 10."},
        {"jaut": "Cik ir 1 % no 400?",
         "atb": ["4"], "padoms": "400 : 100."},
        {"jaut": "Cik ir 3 % no 400?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "Cik ir 75 % no 200?",
         "atb": ["150"], "padoms": "200 : 4 · 3."},
        {"jaut": "Cik ir 40 % no 60?",
         "atb": ["24"], "padoms": "60 : 100 · 40."},
    ], pamats=4,
        ievads="Vai nu caur vienu procentu, vai caur biežāk lietoto daļu."),

    Zimejums("Shēma pirms rēķina",
             dala(10, 2, "20 % iekrāsoti"),
             paskaidro="Josla ir 80 €, sadalīta desmit daļās pa 8 €. Divas "
                       "daļas ir 16 € - tieši 20 %.",
             ievads="Shēma pasaka, kas ir veselais un kas - daļa."),

    Varianti("Kā rēķina procentus?", [
        {"jaut": "Kā atrod vienu procentu no skaitļa?",
         "opcijas": ["Dala ar 100", "Dala ar 10", "Reizina ar 100",
                     "Atņem 1"],
         "pareizi": 0,
         "padoms": "Procents ir simtdaļa."},
        {"jaut": "Cik ir 25 % no 80?",
         "opcijas": ["20", "25", "40", "2"],
         "pareizi": 0,
         "padoms": "80 : 4."},
        {"jaut": "Cik ir 10 % no 250?",
         "opcijas": ["25", "10", "2,5", "250"],
         "pareizi": 0,
         "padoms": "250 : 10."},
        {"jaut": "Kas shēmā ir visa josla?",
         "opcijas": ["100 %", "1 %", "Meklētā daļa", "Atlikums"],
         "pareizi": 0,
         "padoms": "Veselais."},
        {"jaut": "Kurš ceļš ir īsāks 50 % aprēķinam?",
         "opcijas": ["Dalīt ar 2", "Dalīt ar 100 un reizināt ar 50",
                     "Reizināt ar 50", "Atņemt 50"],
         "pareizi": 0,
         "padoms": "50 % = {1|2}."},
        {"jaut": "Cik ir 100 % no 45?",
         "opcijas": ["45", "100", "4,5", "450"],
         "pareizi": 0,
         "padoms": "Viss veselais."},
    ], pamats=4),

    Pasaule("Cik liela ir atlaide?",
            Ievadi("", [
                {"jaut": "Prece maksā 80 €, atlaide 20 %. Cik eiro ir "
                         "atlaide?",
                 "atb": ["16"], "padoms": "80 : 5."},
                {"jaut": "Cik eiro būs jāmaksā?",
                 "atb": ["64"], "padoms": "80 - 16."},
                {"jaut": "Prece maksā 200 €, atlaide 25 %. Cik eiro ir "
                         "atlaide?",
                 "atb": ["50"], "padoms": "200 : 4."},
                {"jaut": "Prece maksā 60 €, atlaide 10 %. Cik eiro būs "
                         "jāmaksā?",
                 "atb": ["54"], "padoms": "60 - 6."},
            ]),
            pavediens="veikals",
            konteksts="Cenu zīmē raksta procentus, bet maksāt nākas eiro.",
            kapec="Procentu vērtību atrod tieši tāpat kā jebkuras citas "
                  "daļas vērtību."),

    Kopsavilkums([
        "Uzzīmēju shēmu, kurā visa josla ir 100 %.",
        "Atrodu vienu procentu, dalot veselo ar 100.",
        "Aprēķinu procentus no skaitļa.",
        "Biežāk lietotos procentus rēķinu kā daļu.",
    ]),

    Majas([
        "Aprēķini 20 % no 150, 25 % no 60 un 5 % no 200.",
        "Uzzīmē shēmu vienam no šiem uzdevumiem.",
        "Atrodi veikalā preci ar atlaidi un aprēķini tās vērtību eiro.",
    ]),
]
