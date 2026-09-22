# -*- coding: utf-8 -*-
"""5. klase, 37. stunda: «Kā izveidot skaitli, kas dalās?»

Uzdevums apgriezts otrādi: nevis pārbaudīt doto skaitli, bet uzbūvēt tādu,
kas dalās. Vienkāršākais paņēmiens - reizināt - noved pie domas, ka skaitļu,
kas dalās ar doto, ir bezgalīgi daudz. Tieši tā ir dalāmo virkne, ar kuru
strādā nākamā stunda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā izveidot skaitli, kas dalās?"

MERKIS = ("Mācīsimies veidot skaitļus, kas dalās ar doto skaitli, un "
          "skaidrot savu paņēmienu.")

SATURS = [
    Sakums("Izdomā skaitli, kas dalās ar 6",
           fakti=["Var meklēt: 61? nē. 62? nē. 63? nē.",
                  "Var arī uzbūvēt: 6 · 11 = 66. Gatavs.",
                  "Otrais paņēmiens strādā vienmēr un uzreiz."]),

    Doma("Reizini - un skaitlis dalīsies noteikti",
         "Jebkurš skaitļa reizinājums ar veselu skaitli dalās ar šo skaitli.",
         soli=[
             "Paņem skaitli, ar kuru jādalās.",
             "Reizini to ar jebkuru veselu skaitli.",
             "Rezultāts dalās ar doto skaitli - un ar reizinātāju arī.",
             "Ja vajag noteiktu lielumu, izvēlies piemērotu reizinātāju.",
             "Pārbaudi ar dalīšanu.",
         ],
         pieze="Skaitļus, kas dalās ar doto, sauc par tā dalāmajiem. To ir "
               "bezgalīgi daudz: 6, 12, 18, 24, 30... - katrs nākamais par 6 "
               "lielāks nekā iepriekšējais."),

    Paraugs("Mazākais trīsciparu skaitlis, kas dalās ar 6",
            uzd="Kurš ir mazākais trīsciparu skaitlis, kas dalās ar 6?",
            soli=[
                ("Mazākais trīsciparu skaitlis ir 100",
                 "No tā jāsāk."),
                ("100 : 6 = 16, atlikums 4",
                 "Pats 100 nedalās."),
                ("Nākamais reizinājums: 6 · 17 = 102",
                 "Reizinātāju palielina par 1."),
                ("Pārbaude: 102 : 6 = 17",
                 "Dalās bez atlikuma."),
            ],
            atbilde="102"),

    Ievadi("Uzbūvē vajadzīgo skaitli", [
        {"jaut": "Kurš ir mazākais trīsciparu skaitlis, kas dalās ar 6?",
         "atb": ["102"], "padoms": "6 · 17."},
        {"jaut": "Kurš ir lielākais divciparu skaitlis, kas dalās ar 7?",
         "atb": ["98"], "padoms": "7 · 14."},
        {"jaut": "Kurš ir mazākais skaitlis, lielāks par 50, kas dalās ar 8?",
         "atb": ["56"], "padoms": "8 · 7."},
        {"jaut": "Kurš skaitlis dalās gan ar 2, gan ar 3 un ir starp 20 un "
                 "25?",
         "atb": ["24"], "padoms": "Dalās ar 6."},
        {"jaut": "Kurš ir piektais skaitlis, kas dalās ar 9? (pirmais ir 9)",
         "atb": ["45"], "padoms": "9 · 5."},
        {"jaut": "Cik skaitļu no 1 līdz 30 dalās ar 5?", "atb": ["6"],
         "padoms": "30 : 5."},
        {"jaut": "Cik skaitļu no 1 līdz 100 dalās ar 25?", "atb": ["4"],
         "padoms": "100 : 25."},
        {"jaut": "Kurš ir mazākais skaitlis, kas dalās gan ar 4, gan ar 10?",
         "atb": ["20"], "padoms": "4 · 5 = 20 un 10 · 2 = 20."},
    ], pamats=4,
        ievads="Nemeklē pēc kārtas - reizini."),

    Varianti("Kāpēc paņēmiens strādā?", [
        {"jaut": "Kāpēc 6 · 11 noteikti dalās ar 6?",
         "opcijas": ["Jo tas ir salikts no sešiniekiem",
                     "Jo 11 ir pirmskaitlis",
                     "Jo abi skaitļi ir mazi",
                     "Tas nedalās"],
         "pareizi": 0,
         "padoms": "Reizinājums satur reizinātāju 6."},
        {"jaut": "Cik ir skaitļu, kas dalās ar 6?",
         "opcijas": ["Bezgalīgi daudz", "Seši", "Tikai divciparu",
                     "Tikai pāra"],
         "pareizi": 0,
         "padoms": "Katrs nākamais ir par 6 lielāks."},
        {"jaut": "Skaitlis dalās ar 4. Ar ko tas dalās noteikti?",
         "opcijas": ["Ar 2", "Ar 8", "Ar 3", "Ar 6"],
         "pareizi": 0,
         "padoms": "4 = 2 · 2."},
        {"jaut": "Kā uzbūvēt skaitli, kas dalās gan ar 3, gan ar 5?",
         "opcijas": ["Reizināt 15 ar jebko", "Saskaitīt 3 un 5",
                     "Reizināt 3 ar 5 un atņemt 1",
                     "Tādu skaitļu nav"],
         "pareizi": 0,
         "padoms": "3 · 5 = 15."},
    ], pamats=4),

    Pasaule("Cik degvielas pietiks?",
            Ievadi("", [
                {"jaut": "Auto ar vienu bāku nobrauc 600 km. Cik kilometru "
                         "nobrauks ar 3 bākām?",
                 "atb": ["1800"], "padoms": "600 · 3."},
                {"jaut": "Ceļš ir 1 750 km. Cik pilnas bākas vajadzēs?",
                 "atb": ["3"], "padoms": "1 750 : 600 = 2, atlikums 550."},
                {"jaut": "Atpūtas vietas ik pēc 80 km. Kurā kilometrā ir "
                         "ceturtā?",
                 "atb": ["320"], "padoms": "80 · 4."},
                {"jaut": "Kurš ir pirmais atpūtas vietas kilometrs pēc "
                         "500 km atzīmes?",
                 "atb": ["560"], "padoms": "80 · 7 = 560."},
            ]),
            pavediens="celojums",
            konteksts="Ceļā viss atkārtojas ik pēc noteikta attāluma - "
                      "degvielas uzpildes, atpūtas vietas, maiņas.",
            kapec="Reizinājums pasaka, kur nākamā atkārtošanās notiks."),

    Kopsavilkums([
        "Veidoju skaitļus, kas dalās ar doto, tos reizinot.",
        "Skaidroju, kāpēc paņēmiens strādā vienmēr.",
        "Atrodu mazāko vai lielāko skaitli ar doto īpašību.",
        "Zinu, ka skaitļu, kas dalās ar doto, ir bezgalīgi daudz.",
    ]),

    Majas([
        "Uzraksti piecus skaitļus, kas dalās ar 7.",
        "Atrodi mazāko četrciparu skaitli, kas dalās ar 12.",
        "Izdomā skaitli, kas dalās ar 2, 3 un 5 vienlaikus.",
    ]),
]
