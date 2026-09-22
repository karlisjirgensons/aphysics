# -*- coding: utf-8 -*-
"""5. klase, 86. stunda: «Kad daļa ir vesels skaitlis?»

Trešā stunda par daļu un dalījumu, un tā noslēdz apli: daļa var būt arī
vesels skaitlis, un vesels skaitlis vienmēr ir pierakstāms kā daļa. Otrais
virziens skolēnam šķiet lieks, bet tieši tas vēlāk ļauj saskaitīt veselo ar
daļu - un tas jau notika 68. stundā, rakstot 1 = {5|5}.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kad daļa ir vesels skaitlis?"

MERKIS = ("Iemācīsimies noteikt, kad daļas vērtība ir vesels skaitlis, un "
          "pierakstīt veselu skaitli kā daļu.")

SATURS = [
    Sakums("Kad daļa pārvēršas par skaitli",
           zimejums=restis([["8/4", "12/3", "20/5"],
                            ["2", "4", "4"]],
                           virsraksts="Augšā daļa, apakšā tās vērtība"),
           paraksts="Ja skaitītājs dalās ar saucēju, daļa ir vesels skaitlis.",
           fakti=["{8|4} nav jāatstāj kā daļa - tas ir 2.",
                  "Pietiek, ka skaitītājs dalās ar saucēju.",
                  "Arī otrādi: 3 var uzrakstīt kā {3|1} vai {6|2}."]),

    Doma("Vesels skaitlis ir daļa bez atlikuma",
         "Daļas vērtība ir vesels skaitlis tad, ja skaitītājs dalās ar "
         "saucēju bez atlikuma; jebkuru veselu skaitli var uzrakstīt kā "
         "daļu ar saucēju 1.",
         soli=[
             "Pārbaudi, vai skaitītājs dalās ar saucēju.",
             "Ja dalās - izdali un pieraksti veselo skaitli.",
             "Ja nedalās - atstāj daļu un saīsini to.",
             "Veselu skaitli raksti kā daļu ar saucēju 1.",
             "Vajadzīgo saucēju iegūsti, paplašinot šo daļu.",
         ],
         pieze="5 = {5|1} = {10|2} = {15|3} - veselam skaitlim arī ir "
               "bezgalīgi daudz daļas pierakstu. Tieši to izmanto, kad "
               "veselo vajag saskaitīt ar daļu."),

    Paraugs("Kuras daļas ir veseli skaitļi?",
            uzd="Nosaki {8|4}, {9|4} un {20|5} vērtības.",
            soli=[
                ("8 : 4 = 2",
                 "Dalās bez atlikuma."),
                ("{8|4} = 2",
                 "Vesels skaitlis."),
                ("9 : 4 nedalās",
                 "{9|4} paliek daļa."),
                ("20 : 5 = 4",
                 "{20|5} = 4."),
            ],
            atbilde="{8|4} = 2 un {20|5} = 4; {9|4} paliek daļa"),

    Ievadi("Vesels skaitlis vai daļa?", [
        {"jaut": "Cik ir {8|4}?",
         "atb": ["2"], "padoms": "8 : 4."},
        {"jaut": "Cik ir {12|3}?",
         "atb": ["4"], "padoms": "12 : 3."},
        {"jaut": "Cik ir {20|5}?",
         "atb": ["4"], "padoms": "20 : 5."},
        {"jaut": "Cik ir {36|6}?",
         "atb": ["6"], "padoms": "36 : 6."},
        {"jaut": "Uzraksti 3 kā daļu ar saucēju 1. Ieraksti skaitītāju.",
         "atb": ["3"], "padoms": "{3|1}."},
        {"jaut": "Uzraksti 3 kā daļu ar saucēju 4. Ieraksti skaitītāju.",
         "atb": ["12"], "padoms": "3 · 4."},
        {"jaut": "Uzraksti 5 kā daļu ar saucēju 6. Ieraksti skaitītāju.",
         "atb": ["30"], "padoms": "5 · 6."},
        {"jaut": "Uzraksti 1 kā daļu ar saucēju 9. Ieraksti skaitītāju.",
         "atb": ["9"], "padoms": "{9|9} = 1."},
    ], pamats=4,
        ievads="Vispirms pārbaudi, vai skaitītājs dalās ar saucēju."),

    Zimejums("No daļas uz skaitli un atpakaļ",
             restis([["8/4", "2"],
                     ["3", "12/4"]],
                    virsraksts="Abos virzienos"),
             paskaidro="Augšējā rindā daļa kļūst par skaitli, apakšējā - "
                       "skaitlis par daļu. Abas reizes vērtība nemainās.",
             ievads="Pārveidot var uz abām pusēm."),

    Varianti("Kad iznāk vesels skaitlis?", [
        {"jaut": "Kad daļas vērtība ir vesels skaitlis?",
         "opcijas": ["Kad skaitītājs dalās ar saucēju",
                     "Kad saucējs dalās ar skaitītāju",
                     "Kad abi ir pāra skaitļi",
                     "Nekad"],
         "pareizi": 0,
         "padoms": "Dalījums bez atlikuma."},
        {"jaut": "Kura daļa ir vesels skaitlis?",
         "opcijas": ["{15|3}", "{15|4}", "{15|2}", "{15|6}"],
         "pareizi": 0,
         "padoms": "15 : 3 = 5."},
        {"jaut": "Kā uzrakstīt 7 kā daļu?",
         "opcijas": ["{7|1}", "{1|7}", "{7|7}", "{0|7}"],
         "pareizi": 0,
         "padoms": "Saucējs 1."},
        {"jaut": "Cik ir {24|8}?",
         "opcijas": ["3", "4", "2", "{3|1} nesaīsināts"],
         "pareizi": 0,
         "padoms": "24 : 8."},
        {"jaut": "Uzraksti 4 ar saucēju 5. Kāds ir skaitītājs?",
         "opcijas": ["20", "4", "5", "9"],
         "pareizi": 0,
         "padoms": "4 · 5."},
        {"jaut": "Kāpēc veselu skaitli reizēm raksta kā daļu?",
         "opcijas": ["Lai to varētu saskaitīt ar citu daļu",
                     "Lai skaitlis būtu lielāks",
                     "Lai to saīsinātu",
                     "Tas nekad nav vajadzīgs"],
         "pareizi": 0,
         "padoms": "Vajadzīgs kopsaucējs."},
    ], pamats=4),

    Pasaule("Cik pilnu komplektu sanāk?",
            Ievadi("", [
                {"jaut": "24 zīmuļi jāsadala 6 komplektos. Cik zīmuļu ir "
                         "katrā?",
                 "atb": ["4"], "padoms": "{24|6}."},
                {"jaut": "30 burtnīcas 5 klasēm. Cik burtnīcu katrai?",
                 "atb": ["6"], "padoms": "{30|5}."},
                {"jaut": "25 grāmatas 4 plauktiem. Vai sanāk vesels skaits? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "25 : 4 nedalās."},
                {"jaut": "Uzraksti 6 komplektus kā daļu ar saucēju 2. "
                         "Ieraksti skaitītāju.",
                 "atb": ["12"], "padoms": "6 · 2."},
            ]),
            pavediens="skola",
            konteksts="Skolas materiālus dala komplektos, un reizēm skaitlis "
                      "dalās, reizēm ne.",
            kapec="Pārbaudīt to ir viena dalīšana, nevis visa rēķina "
                  "izpilde."),

    Kopsavilkums([
        "Nosaku, vai daļas vērtība ir vesels skaitlis.",
        "Aprēķinu daļas vērtību, kas izsakāma ar veselu skaitli.",
        "Pierakstu veselu skaitli kā daļu ar saucēju 1.",
        "Pierakstu veselu skaitli kā daļu ar jebkuru vajadzīgo saucēju.",
    ]),

    Majas([
        "Atrodi trīs daļas, kuru vērtība ir vesels skaitlis.",
        "Uzraksti 8 kā daļu ar saucējiem 1, 3 un 5.",
        "Paskaidro, kāpēc {9|9} un {12|12} ir viens un tas pats skaitlis.",
    ]),
]
