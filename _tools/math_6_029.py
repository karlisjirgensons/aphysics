# -*- coding: utf-8 -*-
"""6. klase, 29. stunda: «Kas ir apgrieztais skaitlis?»

Viens jēdziens, viena stunda. Apgrieztais skaitlis pats par sevi neko
nerēķina, bet bez tā nākamajā stundā nav ko teikt par dalīšanu. Tāpēc te tas
tiek nevis definēts, bet atrasts: kas jāreizina, lai iznāktu tieši 1?
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kas ir apgrieztais skaitlis?"

MERKIS = ("Iemācīsimies atrast un pierakstīt skaitlim apgriezto skaitli un "
          "secināsim, ka to reizinājums ir 1.")

SATURS = [
    Sakums("Kas jāreizina, lai iznāktu tieši viens?",
           fakti=["{3|4} · {4|3} = {12|12} = 1.",
                  "Tādus divus skaitļus sauc par savstarpēji apgrieztiem.",
                  "Nullei apgrieztā skaitļa nav - ar nulli nevar iznākt 1."]),

    Doma("Apgriež daļu otrādi",
         "Apgriezto skaitli iegūst, samainot vietām skaitītāju un saucēju; "
         "skaitļa un tā apgrieztā skaitļa reizinājums vienmēr ir 1.",
         soli=[
             "Pieraksti skaitli kā daļu; veselam skaitlim saucējs ir 1.",
             "Samaini vietām skaitītāju un saucēju.",
             "Jaukto skaitli vispirms pārveido par neīstu daļu.",
             "Pārbaudi: sareizini abus - jāiznāk 1.",
         ],
         pieze="Skaitlim 5 = {5|1} apgrieztais ir {1|5}. Skaitlim 1 "
               "apgrieztais ir tas pats 1, un tas ir vienīgais tāds "
               "pozitīvais skaitlis."),

    Paraugs("Atrodi apgriezto skaitli",
            uzd="Kāds ir apgrieztais skaitlis jauktajam skaitlim 2{1|3}?",
            soli=[
                ("2{1|3} = {7|3}",
                 "Vispirms neīsta daļa: 2 · 3 + 1 = 7."),
                ("Apgriež: {3|7}",
                 "Skaitītājs un saucējs maina vietas."),
                ("Pārbaude: {7|3} · {3|7} = {21|21}",
                 "Sareizina abus."),
                ("{21|21} = 1",
                 "Tieši tā, kā jābūt."),
            ],
            atbilde="{3|7}"),

    Ievadi("Uzraksti apgriezto skaitli", [
        {"jaut": "Kāds ir apgrieztais skaitlis daļai {2|5}? Atbildi raksti "
                 "kā a/b.",
         "atb": ["5/2", "2 1/2"], "padoms": "Samaini vietām."},
        {"jaut": "Kāds ir apgrieztais skaitlis daļai {7|8}? Atbildi raksti "
                 "kā a/b.",
         "atb": ["8/7", "1 1/7"], "padoms": "Skaitītājs kļūst par saucēju."},
        {"jaut": "Kāds ir apgrieztais skaitlis skaitlim 6? Atbildi raksti "
                 "kā a/b.",
         "atb": ["1/6"], "padoms": "6 = {6|1}."},
        {"jaut": "Kāds ir apgrieztais skaitlis daļai {1|9}?",
         "atb": ["9"], "padoms": "{9|1} = 9."},
        {"jaut": "Kāds ir apgrieztais skaitlis jauktajam skaitlim 1{1|2}? "
                 "Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "1{1|2} = {3|2}."},
        {"jaut": "Cik ir {4|9} · {9|4}?",
         "atb": ["1"], "padoms": "{36|36}."},
    ], pamats=4,
        ievads="Pārbaude vienmēr ir viena un tā pati: reizinājumam jābūt 1."),

    Varianti("Vai šie skaitļi ir apgriezti?", [
        {"jaut": "{3|5} un {5|3} - vai tie ir savstarpēji apgriezti?",
         "opcijas": ["Jā, to reizinājums ir 1", "Nē, tie ir dažādi",
                     "Jā, jo abi ir daļas", "Nē, reizinājums ir {15|15}"],
         "pareizi": 0,
         "padoms": "{15|15} ir tieši 1."},
        {"jaut": "Kuram skaitlim nav apgrieztā skaitļa?",
         "opcijas": ["0", "1", "{1|2}", "100"],
         "pareizi": 0,
         "padoms": "Ar nulli nevar iegūt vieninieku."},
        {"jaut": "Kāds ir apgrieztais skaitlis skaitlim 1?",
         "opcijas": ["1", "0", "{1|2}", "Tāda nav"],
         "pareizi": 0,
         "padoms": "1 · 1 = 1."},
        {"jaut": "Ja skaitlis ir lielāks par 1, tad tā apgrieztais "
                 "skaitlis...",
         "opcijas": ["ir mazāks par 1", "ir lielāks par 1",
                     "ir tieši 1", "var būt jebkāds"],
         "pareizi": 0,
         "padoms": "{5|2} apgrieztais ir {2|5}."},
    ], pamats=4),

    Pasaule("Cik reižu jāpalielina?",
            Ievadi("", [
                {"jaut": "Attēlu samazināja līdz {2|3} no sākotnējā. Ar kādu "
                         "skaitli to reizināt, lai atgrieztu? Atbildi raksti "
                         "kā a/b.",
                 "atb": ["3/2", "1 1/2"], "padoms": "Apgrieztais skaitlis."},
                {"jaut": "Attēls bija 600 pikseļu plats un kļuva {2|3} no "
                         "tā. Cik pikseļu tas ir tagad?",
                 "atb": ["400"], "padoms": "600 : 3 · 2."},
                {"jaut": "Cik pikseļu būs, ja 400 reizinās ar {3|2}?",
                 "atb": ["600"], "padoms": "400 : 2 · 3."},
                {"jaut": "Attēlu samazināja līdz {1|4}. Ar kādu skaitli to "
                         "reizināt, lai atgrieztu sākotnējo izmēru?",
                 "atb": ["4"], "padoms": "{4|1}."},
            ]),
            pavediens="dati",
            konteksts="Attēla izmēru maina ar reizinātāju; lai atgrieztos, "
                      "vajag tieši apgriezto skaitli.",
            kapec="Apgrieztais skaitlis ir «atpakaļgaita» reizināšanai."),

    Kopsavilkums([
        "Nosaku un pierakstu skaitlim apgriezto skaitli.",
        "Pārveidoju jauktu skaitli par neīstu daļu pirms apgriešanas.",
        "Pārbaudu, vai reizinājums ir tieši 1.",
        "Zinu, ka nullei apgrieztā skaitļa nav.",
    ]),

    Majas([
        "Uzraksti apgrieztos skaitļus pieciem dažādiem skaitļiem.",
        "Atrodi skaitli, kurš ir vienāds ar savu apgriezto skaitli.",
        "Paskaidro, kāpēc nullei apgrieztā skaitļa nav.",
    ]),
]
