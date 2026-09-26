# -*- coding: utf-8 -*-
"""4. klase, 44. stunda: «Cik apmēram būs dalījums?»

Dalījuma aptuvenā vērtība: dalāmo aizstāj ar tuvāko skaitli, kas ērti
dalās (738 : 3 ≈ 750 : 3 vai 720 : 3). Pārbauda arī ar kalkulatoru - un
aptuvenā vērtība atklāj, ja kalkulatorā nospiests kas lieks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, kolonnas)

TEMA = "Cik apmēram būs dalījums?"

MERKIS = ("Noteiksim dalījuma aptuveno vērtību un pārbaudīsim to, arī ar "
          "digitāliem rīkiem.")

SATURS = [
    Sakums("Vai kalkulatoram var ticēt?",
           zimejums=kolonnas([("aptuveni", 250), ("ekrānā", 2460)]),
           paraksts="738 : 3 ≈ 750 : 3 = 250. Bet ekrānā 2460?",
           fakti=["Kāds nospieda 7380 : 3 - lieka nulle.",
                  "Aptuvenā vērtība atmasko kļūdu vienā mirklī."]),

    Doma("Aizstāj dalāmo ar ērti dalāmu kaimiņu",
         "Atrodi tuvu skaitli, kas dalās ar dalītāju galvā; tas dod aptuveno "
         "dalījumu.",
         soli=[
             "Paskaties uz dalītāju: 7.",
             "Atrodi dalāmajam tuvu skaitli no reizināšanas tabulas: "
             "518 ≈ 490 vai 560.",
             "Izdali galvā: 490 : 7 = 70, 560 : 7 = 80.",
             "Precīzā atbilde būs starp tiem: 518 : 7 = 74.",
         ],
         pieze="Tā var uzreiz pateikt arī ciparu skaitu: dalījums ir starp 70 "
               "un 80 - divi cipari."),

    Paraugs("Novērtē 628 : 4",
            uzd="Novērtē un izrēķini 628 : 4.",
            soli=[
                ("628 ≈ 600 vai 640", "Tuvi skaitļi, kas dalās ar 4."),
                ("600 : 4 = 150, 640 : 4 = 160", "Dalījums starp 150 un 160."),
                ("628 : 4 = 157", "Precīzi - un tas ir starp."),
            ],
            atbilde="157"),

    Ievadi("Aptuveni", [
        {"jaut": "Novērtē 738 : 3 ≈ 750 : 3 = ?", "atb": ["250"],
         "padoms": "75 : 3 = 25."},
        {"jaut": "Novērtē 395 : 8 ≈ 400 : 8 = ?", "atb": ["50"],
         "padoms": "40 : 8 = 5."},
        {"jaut": "Novērtē 812 : 9 ≈ 810 : 9 = ?", "atb": ["90"],
         "padoms": "81 : 9 = 9."},
        {"jaut": "Novērtē 355 : 6 ≈ 360 : 6 = ?", "atb": ["60"],
         "padoms": "36 : 6 = 6."},
    ]),

    Varianti("Kurš rezultāts ticams?", [
        {"jaut": "Kalkulatorā 824 : 4 = 26. Ticams?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "800 : 4 = 200 - vajag trīs ciparus."},
        {"jaut": "Kalkulatorā 567 : 7 = 81. Ticams?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "560 : 7 = 80."},
        {"jaut": "Starp kuriem skaitļiem ir 450 : 7?",
         "opcijas": ["60 un 70", "6 un 7", "600 un 700", "70 un 80"],
         "pareizi": 0, "padoms": "420 : 7 = 60, 490 : 7 = 70."},
        {"jaut": "Kurš dalījums ir tuvāk 100?",
         "opcijas": ["498 : 5", "498 : 4", "498 : 6", "498 : 3"],
         "pareizi": 0, "padoms": "500 : 5 = 100."},
    ], pamats=4),

    Pasaule("Cik maksā vienā dienā?",
            Ievadi("", [
                {"jaut": "Nometnes cena 7 dienām ir 518 €. Novērtē cenu "
                         "dienā ar 490 : 7.",
                 "atb": ["70"], "padoms": "49 : 7 = 7."},
                {"jaut": "Precīzi: 518 : 7 = ?", "atb": ["74"],
                 "padoms": "490 : 7 + 28 : 7."},
                {"jaut": "Velosipēda noma 5 dienām 185 €. Cik dienā?",
                 "atb": ["37"], "padoms": "150 : 5 + 35 : 5."},
                {"jaut": "Mēneša abonements 9 treniņiem 144 €. Cik viens "
                         "treniņš?",
                 "atb": ["16"], "padoms": "144 : 9."},
            ]),
            pavediens="veikals",
            konteksts="Cenu salīdzināšanai to pārrēķina uz vienu dienu vai "
                      "vienu reizi.",
            kapec="Novērtējums galvā pasaka, vai kalkulators neiet greizi."),

    Kopsavilkums([
        "Novērtēju dalījumu ar ērti dalāmu kaimiņu.",
        "Pasaku, starp kuriem skaitļiem ir dalījums.",
        "Pārbaudu kalkulatora rezultātu ar novērtējumu.",
    ]),

    Majas([
        "Ar kalkulatoru izdali 3 skaitļus un pārbaudi ar novērtējumu.",
        "Novērtē, cik maksā viena diena tavā pulciņā mēnesī.",
        "Izdomā «aplamu kalkulatora» atbildi un atmasko to.",
    ]),
]
