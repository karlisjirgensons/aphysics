# -*- coding: utf-8 -*-
"""6. klase, 40. stunda: «Kā reizināt galvā?»

Stunda par paņēmieniem, ne par algoritmu. Vesela skaitļa un decimāldaļas
reizinājumu gandrīz vienmēr var izrēķināt galvā - ja skaitli sadala vai
pārraksta ērtāk. Skolēni paši nosauc, kuru paņēmienu lietoja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā reizināt galvā?"

MERKIS = ("Iemācīsimies galvā aprēķināt vesela skaitļa un decimāldaļas "
          "reizinājumu un paskaidrot savu paņēmienu.")

SATURS = [
    Sakums("Veikalā kalkulatoru neviens neizņem",
           fakti=["4 · 2,5 € ir 10 € - to var pateikt ātrāk nekā ierakstīt.",
                  "Paņēmiens: 2,5 ir puse no 5, tāpēc 4 · 2,5 = 2 · 5.",
                  "Galvā rēķina nevis ātrāk, bet gudrāk."]),

    Doma("Pārraksti skaitli ērtāk",
         "Decimāldaļu reizinot galvā, to pārraksta ērtākā veidā: kā veselu "
         "skaitli ar dalīšanu vai kā summu.",
         soli=[
             "Paskaties, vai decimāldaļa ir tuvu veselam skaitlim.",
             "Ja jā - reizini ar veselo un tad atņem lieko.",
             "Ja daļa ir 0,5; 0,25 vai 0,2 - lieto dalīšanu: puse, "
             "ceturtdaļa, piektdaļa.",
             "Citos gadījumos reizini bez komata un komatu ieliec beigās.",
             "Pārbaudi ar novērtējumu.",
         ],
         pieze="6 · 1,9 ir ērtāk kā 6 · 2 − 6 · 0,1 = 12 − 0,6 = 11,4. "
               "Tas ir divas darbības, bet abas - galvā."),

    Paraugs("Trīs paņēmieni vienam uzdevumam",
            uzd="Cik ir 8 · 2,5? Parādi trīs ceļus.",
            soli=[
                ("Puse: 2,5 ir puse no 5, tātad 8 · 2,5 = 4 · 5 = 20",
                 "Viens reizinātājs uz pusi mazāks, otrs divreiz lielāks."),
                ("Summa: 8 · 2 + 8 · 0,5 = 16 + 4 = 20",
                 "Sadala decimāldaļu summā."),
                ("Bez komata: 8 · 25 = 200, komats vienā vietā: 20,0",
                 "Reizinātājā viens cipars aiz komata."),
                ("Visi trīs dod 20",
                 "Izvēlas to, kurš konkrētajam skaitlim ir ērtākais."),
            ],
            atbilde="20"),

    Ievadi("Rēķini galvā", [
        {"jaut": "Cik ir 4 · 2,5?",
         "atb": ["10"], "padoms": "2,5 ir puse no 5."},
        {"jaut": "Cik ir 6 · 1,5?",
         "atb": ["9"], "padoms": "6 · 1 + 6 · 0,5."},
        {"jaut": "Cik ir 5 · 0,4?",
         "atb": ["2"], "padoms": "5 · 4 = 20; komats vienā vietā."},
        {"jaut": "Cik ir 7 · 0,2?",
         "atb": ["1,4", "1.4"], "padoms": "7 · 2 = 14."},
        {"jaut": "Cik ir 3 · 1,9?",
         "atb": ["5,7", "5.7"], "padoms": "3 · 2 − 3 · 0,1."},
        {"jaut": "Cik ir 12 · 0,25?",
         "atb": ["3"], "padoms": "0,25 ir ceturtdaļa; 12 : 4."},
    ], pamats=4,
        ievads="Pie katras atbildes padomā, kuru paņēmienu lietoji."),

    Pasaule("Cik maksās pirkums?",
            Kustiba("", [
                {"jaut": "6 pudeles pa 1,5 €. Cik eiro kopā?",
                 "atb": 9, "beigas": 30, "iedala": 5, "mers": "eiro",
                 "merkis": "summa", "objekts": "Čeks",
                 "padoms": "6 · 1 + 6 · 0,5."},
                {"jaut": "4 paciņas pa 2,5 €. Cik eiro kopā?",
                 "atb": 10, "beigas": 30, "iedala": 5, "mers": "eiro",
                 "merkis": "summa", "objekts": "Čeks",
                 "padoms": "2,5 ir puse no 5."},
                {"jaut": "8 maizes pa 0,75 €. Cik eiro kopā?",
                 "atb": 6, "beigas": 30, "iedala": 5, "mers": "eiro",
                 "merkis": "summa", "objekts": "Čeks",
                 "padoms": "8 · 0,75 = 8 · 3 : 4."},
                {"jaut": "5 kastes pa 3,8 €. Cik eiro kopā?",
                 "atb": 19, "beigas": 30, "iedala": 5, "mers": "eiro",
                 "merkis": "summa", "objekts": "Čeks",
                 "padoms": "5 · 4 − 5 · 0,2."},
            ]),
            pavediens="veikals",
            konteksts="Kase rāda summu tikai pašās beigās - līdz tam rēķina "
                      "pats pircējs.",
            kapec="Galvā rēķinot, summu zina jau pirms kases."),

    Varianti("Kurš paņēmiens te ir ērtākais?", [
        {"jaut": "20 · 0,25. Kā rēķināt ātrāk?",
         "opcijas": ["20 : 4", "20 · 25", "20 + 0,25", "20 · 4"],
         "pareizi": 0,
         "padoms": "0,25 ir ceturtdaļa."},
        {"jaut": "9 · 1,1. Kā rēķināt ātrāk?",
         "opcijas": ["9 + 0,9", "9 · 11", "9 : 1,1", "9 − 0,9"],
         "pareizi": 0,
         "padoms": "1,1 ir 1 + 0,1."},
        {"jaut": "40 · 0,5 ir...",
         "opcijas": ["20", "2", "200", "0,2"],
         "pareizi": 0,
         "padoms": "Puse no 40."},
        {"jaut": "Kāpēc 5 · 0,4 nav 2,0 kļūda, bet 20 - ir?",
         "opcijas": ["Jo 0,4 ir mazāks par 1, tāpēc rezultāts ir mazāks "
                     "par 5",
                     "Jo 5 · 4 = 20",
                     "Jo komats nekur nav vajadzīgs",
                     "Abas atbildes der"],
         "pareizi": 0,
         "padoms": "Novērtējums pasaka, kur komats."},
    ], pamats=4),

    Kopsavilkums([
        "Reizinu veselu skaitli ar decimāldaļu galvā.",
        "Izvēlos paņēmienu pēc skaitļa: puse, ceturtdaļa vai summa.",
        "Paskaidroju, kuru paņēmienu un kāpēc lietoju.",
        "Pārbaudu rezultātu ar novērtējumu.",
    ]),

    Majas([
        "Izrēķini galvā 6 · 2,5; 8 · 1,25 un 7 · 0,2.",
        "Atrodi veikalā trīs cenas un izrēķini galvā trīs vienādu preču "
        "summu.",
        "Pieraksti paņēmienu, kuru lietoji visbiežāk.",
    ]),
]
