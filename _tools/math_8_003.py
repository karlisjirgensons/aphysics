# -*- coding: utf-8 -*-
"""8. klase, 3. stunda: «Kā datus apstrādāt ar digitāliem rīkiem?»

Izklājlapa ir rūtiņu tabula, kurā katra rūtiņa zina savu adresi (B3), un
formula rēķina no adresēm, nevis no skaitļiem. Tāpēc, nomainot vienu
datu vērtību, pārrēķinās viss - tieši to stundā izmēģina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kā datus apstrādāt ar digitāliem rīkiem?"

MERKIS = ("Mācīsimies izklājlapā sakārtot, saskaitīt un apkopot datus ar "
          "formulām.")

_LAPA = restis([["", "A", "B"],
                ["1", "diena", "min"],
                ["2", "P", "95"],
                ["3", "O", "120"],
                ["4", "T", "80"],
                ["5", "C", "150"],
                ["6", "Pk", "135"]])

SATURS = [
    Sakums("Ekrāna laiks nedēļā",
           zimejums=_LAPA,
           paraksts="Kolonnā B - minūtes telefonā katru darba dienu.",
           fakti=["Katrai rūtiņai ir adrese: kolonna un rinda, piemēram, B3.",
                  "Formula sākas ar «=» un rēķina no adresēm.",
                  "Maini skaitli - rezultāts pārrēķinās pats."]),

    Doma("Piecas formulas, kas der gandrīz visam",
         "Izklājlapā (Excel, Google Sheets, LibreOffice) skaitļus neraksta "
         "formulā - raksta adreses. Apgabals B2:B6 nozīmē «no B2 līdz B6».",
         soli=[
             "=SUM(B2:B6) - summa.",
             "=AVERAGE(B2:B6) - aritmētiskais vidējais.",
             "=MIN(B2:B6) un =MAX(B2:B6) - mazākā un lielākā vērtība.",
             "=COUNT(B2:B6) - cik ir skaitļu.",
             "Poga «Kārtot» sakārto rindas augošā vai dilstošā secībā.",
         ],
         pieze="Dažās valodu versijās funkcijas argumentus atdala ar "
               "semikolu, piemēram, =ROUND(B7;1), bet apgabals vienmēr ir "
               "ar kolu: B2:B6."),

    Paraugs("Ko izrēķina formulas?",
            uzd="Tabulā B2:B6 ir 95, 120, 80, 150, 135. Ko parāda "
                "=SUM(B2:B6), =MAX(B2:B6) un =AVERAGE(B2:B6)?",
            soli=[
                ("95 + 120 + 80 + 150 + 135 = 580", "SUM - 580 min."),
                ("Lielākā vērtība - 150", "MAX - ceturtdien."),
                ("580 : 5 = 116", "AVERAGE - vidēji dienā."),
            ],
            atbilde="580; 150; 116"),

    Ievadi("Esi izklājlapa", [
        {"jaut": "B2:B6 = 95, 120, 80, 150, 135. Cik ir =MIN(B2:B6)?",
         "atb": ["80"], "padoms": "Mazākā vērtība."},
        {"jaut": "Cik ir =B5 − B4?",
         "atb": ["70"], "padoms": "150 − 80."},
        {"jaut": "Cik ir =COUNT(B2:B6)?",
         "atb": ["5"], "padoms": "Pieci skaitļi."},
        {"jaut": "B3 nomaina uz 60. Cik tagad ir =SUM(B2:B6)?",
         "atb": ["520"], "padoms": "580 − 120 + 60."},
        {"jaut": "Cik tagad ir =AVERAGE(B2:B6)?",
         "atb": ["104"], "padoms": "520 : 5."},
        {"jaut": "Sākotnējie dati: cik stundu ir =SUM(B2:B6)/60? "
                 "Noapaļo līdz desmitdaļām.",
         "atb": ["9,7", "9.7"], "padoms": "580 : 60 ≈ 9,67."},
    ], pamats=4),

    Varianti("Kura formula?", [
        {"jaut": "Vajag kopējo summu rūtiņās C2 līdz C20.",
         "opcijas": ["=SUM(C2:C20)", "=SUM(C2+C20)", "=C2:C20",
                     "SUM C2 C20"],
         "pareizi": 0, "padoms": "Apgabals ar kolu."},
        {"jaut": "Kāpēc formulā raksta =B2+B3, nevis =95+120?",
         "opcijas": ["Mainot datus, rezultāts pārrēķinās",
                     "Tā ir īsāk", "Skaitļus nedrīkst rakstīt",
                     "Tā ir precīzāk"],
         "pareizi": 0, "padoms": "Adrese seko datiem."},
        {"jaut": "Ko nozīmē apgabals A1:A5?",
         "opcijas": ["Rūtiņas A1, A2, A3, A4, A5", "Tikai A1 un A5",
                     "A1 dalīts ar A5", "Piecas kolonnas"],
         "pareizi": 0, "padoms": "No ... līdz."},
    ]),

    Zimejums("Tā izskatās formula rūtiņā",
             restis([["", "A", "B"],
                     ["7", "kopā", "=SUM(B2:B6)"],
                     ["8", "vidēji", "=AVERAGE(B2:B6)"]]),
             paskaidro="Ekrānā rūtiņa rāda rezultātu (580 un 116), bet "
                       "formula paliek aiz tās."),

    Pasaule("Klases ekrāna laika pētījums",
            Ievadi("", [
                {"jaut": "4 skolēnu nedēļas ekrāna laiks stundās: 14, 21, "
                         "9, 18. Cik ir =SUM?",
                 "atb": ["62"], "padoms": "14 + 21 + 9 + 18."},
                {"jaut": "Cik ir =AVERAGE?",
                 "atb": ["15,5", "15.5"], "padoms": "62 : 4."},
                {"jaut": "Cik stundu vidēji dienā (7 dienas)? Noapaļo līdz "
                         "desmitdaļām.",
                 "atb": ["2,2", "2.2"], "padoms": "15,5 : 7 ≈ 2,21."},
            ]),
            pavediens="dati",
            konteksts="Telefoni paši skaita ekrāna laiku - tie ir īsti dati, "
                      "ko var ievadīt izklājlapā.",
            kapec="Viena formula aprēķina visai klasei uzreiz."),

    Kopsavilkums([
        "Lasu rūtiņas adresi un apgabalu.",
        "Lietoju SUM, AVERAGE, MIN, MAX un COUNT.",
        "Sakārtoju datus ar pogu «Kārtot».",
        "Saprotu, kāpēc formula rēķina no adresēm.",
    ]),

    Majas([
        "Ievadi izklājlapā savu nedēļas ekrāna laiku.",
        "Ar formulām atrodi summu, vidējo, mazāko un lielāko.",
        "Nomaini vienu vērtību un pavēro, kas pārrēķinās.",
    ]),
]
