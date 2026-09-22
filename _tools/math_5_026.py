# -*- coding: utf-8 -*-
"""5. klase, 26. stunda: «Kā izteiksmi padarīt vienkāršāku?»

Sadalāmības īpašība b · a + c · a = (b + c) · a. Skolēns to jau lieto, pat
nezinot: 7 · 6 + 3 · 6 viņš rēķina kā «desmit sešnieki». Stundas darbs ir šo
domu pierakstīt un pamanīt kopīgo reizinātāju arī tur, kur tas neduras acīs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā izteiksmi padarīt vienkāršāku?"

MERKIS = ("Iemācīsimies aprēķināt izteiksmes vērtību, lietojot sadalāmības "
          "īpašību b · a + c · a = (b + c) · a.")

SATURS = [
    Sakums("Septiņi seši un vēl trīs seši",
           fakti=["7 · 6 + 3 · 6 - divi reizinājumi, viens rēķins.",
                  "Septiņi seši un trīs seši kopā ir desmit seši.",
                  "10 · 6 = 60. Abus reizinājumus rēķināt nevajadzēja."]),

    Doma("Kopīgo reizinātāju var iznest pirms iekavām",
         "Ja abos reizinājumos ir viens un tas pats reizinātājs, saskaitīt "
         "var tikai pārējos: b · a + c · a = (b + c) · a.",
         soli=[
             "Paskaties, vai abos reizinājumos ir kopīgs reizinātājs.",
             "Uzraksti to aiz iekavām.",
             "Iekavās saskaiti abus atlikušos skaitļus.",
             "Izrēķini vienu reizinājumu, nevis divus.",
         ],
         pieze="Tas pats strādā arī atpakaļ: (20 + 3) · 7 var izrēķināt kā "
               "20 · 7 + 3 · 7 = 140 + 21 = 161. Tieši tā reizina stabiņā."),

    Paraugs("Kopīgais reizinātājs aiz iekavām",
            uzd="Aprēķini 17 · 6 + 3 · 6 racionāli.",
            soli=[
                ("Abos reizinājumos ir 6",
                 "6 ir kopīgais reizinātājs."),
                ("(17 + 3) · 6",
                 "Kopīgo iznesam aiz iekavām."),
                ("20 · 6 = 120",
                 "Iekavās sanāca apaļš skaitlis."),
            ],
            atbilde="17 · 6 + 3 · 6 = 120"),

    Ievadi("Iznes kopīgo reizinātāju", [
        {"jaut": "7 · 6 + 3 · 6 = ?", "atb": ["60"],
         "padoms": "(7 + 3) · 6."},
        {"jaut": "12 · 5 + 8 · 5 = ?", "atb": ["100"],
         "padoms": "(12 + 8) · 5."},
        {"jaut": "24 · 7 + 6 · 7 = ?", "atb": ["210"],
         "padoms": "(24 + 6) · 7."},
        {"jaut": "48 · 9 + 52 · 9 = ?", "atb": ["900"],
         "padoms": "(48 + 52) · 9."},
        {"jaut": "15 · 4 + 15 · 6 = ?", "atb": ["150"],
         "padoms": "Kopīgais ir 15: 15 · (4 + 6)."},
        {"jaut": "8 · 25 + 12 · 25 = ?", "atb": ["500"],
         "padoms": "(8 + 12) · 25."},
        {"jaut": "37 · 8 − 27 · 8 = ?", "atb": ["80"],
         "padoms": "Atņemšanā tas pats: (37 − 27) · 8."},
        {"jaut": "(20 + 3) · 7 = ?", "atb": ["161"],
         "padoms": "20 · 7 + 3 · 7."},
    ], pamats=4,
        ievads="Vispirms meklē kopīgo reizinātāju."),

    Varianti("Kur slēpjas kopīgais reizinātājs?", [
        {"jaut": "Kurš ir kopīgais reizinātājs izteiksmē 24 · 7 + 6 · 7?",
         "opcijas": ["7", "24", "6", "30"],
         "pareizi": 0,
         "padoms": "Tas, kas atkārtojas abos reizinājumos."},
        {"jaut": "Kā pareizi pārraksta 12 · 5 + 8 · 5?",
         "opcijas": ["(12 + 8) · 5", "12 + 8 · 5", "(12 · 8) + 5",
                     "12 · 5 · 8"],
         "pareizi": 0,
         "padoms": "Kopīgais paliek aiz iekavām, pārējie saskaitās."},
        {"jaut": "Vai īpašība der arī atņemšanai?",
         "opcijas": ["Der: (b − c) · a", "Neder nekad",
                     "Der tikai pāra skaitļiem", "Der tikai ar iekavām"],
         "pareizi": 0,
         "padoms": "Pārbaudi ar 37 · 8 − 27 · 8."},
        {"jaut": "Kāpēc šī īpašība palīdz rēķināt galvā?",
         "opcijas": ["Iekavās bieži sanāk apaļš skaitlis",
                     "Jo skaitļi kļūst mazāki",
                     "Jo reizinājumu vairs nav",
                     "Jo iekavas rēķina pēdējās"],
         "pareizi": 0,
         "padoms": "17 + 3 = 20."},
    ], pamats=4),

    Pasaule("Cik maksā divas kastes?",
            Ievadi("", [
                {"jaut": "Vienā kastē 17 burkas, otrā 3, katra burka "
                         "6 eiro. Cik eiro kopā?",
                 "atb": ["120"], "padoms": "(17 + 3) · 6."},
                {"jaut": "Pirmdien pārdeva 48 biļetes, otrdien 52, katra "
                         "9 eiro. Cik eiro kopā?",
                 "atb": ["900"], "padoms": "(48 + 52) · 9."},
                {"jaut": "Bija 37 paciņas pa 8 centiem, pārdeva 27 paciņas. "
                         "Par cik centiem palicis vairāk nekā pārdots?",
                 "atb": ["80"], "padoms": "(37 − 27) · 8."},
                {"jaut": "Grozā 15 āboli pa 4 centiem un 15 bumbieri pa "
                         "6 centiem. Cik centu kopā?",
                 "atb": ["150"], "padoms": "15 · (4 + 6)."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā viena un tā pati cena atkārtojas daudzās "
                      "rindās - tieši tur kopīgais reizinātājs arī rodas.",
            kapec="Vienu reizinājumu izrēķināt ir ātrāk nekā divus."),

    Kopsavilkums([
        "Pamanu kopīgo reizinātāju divos reizinājumos.",
        "Iznesu to aiz iekavām un saskaitu atlikušos skaitļus.",
        "Lietoju to pašu atņemšanai: (b − c) · a.",
        "Lietoju īpašību arī otrā virzienā: (20 + 3) · 7.",
    ]),

    Majas([
        "Uzraksti izteiksmi, kurā kopīgais reizinātājs ļauj rēķināt galvā.",
        "Pārbaudi ar kalkulatoru, vai abi ceļi dod vienu atbildi.",
        "Atrodi čekā divas rindas ar vienu un to pašu cenu.",
    ]),
]
