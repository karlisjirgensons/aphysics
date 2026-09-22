# -*- coding: utf-8 -*-
"""6. klase, 135. stunda: «Cik dažādus rezultātus var iegūt?»

Mikrotemata noslēgums ar atvērtu uzdevumu. Skaitļi ir doti, zīmes - nav.
Meklējot lielāko un mazāko rezultātu, skolēns lieto visu, ko šis mikrotemats
mācīja, un turklāt spriež, nevis tikai rēķina.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Cik dažādus rezultātus var iegūt?"

MERKIS = ("Starp dotiem skaitļiem ievietosim zīmes, lai iegūtu dažādus "
          "rezultātus.")

SATURS = [
    Sakums("Trīs skaitļi, četri rezultāti",
           fakti=["Starp 5; 3 un 8 var likt plusus un mīnusus.",
                  "5 + 3 + 8 = 16, bet 5 − 3 − 8 = −6.",
                  "Starpība starp lielāko un mazāko ir 22."]),

    Doma("Lielākais - visi plusi, mazākais - visi mīnusi",
         "Lielāko rezultātu iegūst, visus skaitļus pēc pirmā pieskaitot; "
         "mazāko - visus atņemot.",
         soli=[
             "Pieraksti dotos skaitļus tādā secībā, kā tie doti.",
             "Lielākajam rezultātam liec visur plusus.",
             "Mazākajam - visur mīnusus aiz pirmā skaitļa.",
             "Izrēķini abus.",
             "Pārējos rezultātus iegūsti, mainot pa vienai zīmei.",
         ],
         pieze="Katra zīmes maiņa no plusa uz mīnusu samazina rezultātu par "
               "divkāršu skaitli: 5 + 3 ir 8, bet 5 − 3 ir 2 - starpība ir "
               "2 · 3 = 6."),

    Paraugs("Lielākais un mazākais",
            uzd="Starp skaitļiem 5; 3 un 8 ieliec zīmes. Kāds ir lielākais "
                "un kāds mazākais rezultāts?",
            soli=[
                ("Lielākais: 5 + 3 + 8 = 16",
                 "Visi plusi."),
                ("Mazākais: 5 − 3 − 8 = −6",
                 "Visi mīnusi."),
                ("Vēl divi: 5 + 3 − 8 = 0",
                 "Viena zīme mainīta."),
                ("5 − 3 + 8 = 10",
                 "Otra zīme mainīta."),
            ],
            atbilde="lielākais 16, mazākais −6"),

    Ievadi("Izrēķini variantus", [
        {"jaut": "Cik ir 5 + 3 + 8?",
         "atb": ["16"], "padoms": "Visi plusi."},
        {"jaut": "Cik ir 5 − 3 − 8?",
         "atb": ["-6", "−6"], "padoms": "Visi mīnusi."},
        {"jaut": "Cik ir 5 + 3 − 8?",
         "atb": ["0"], "padoms": "8 − 8."},
        {"jaut": "Cik ir 5 − 3 + 8?",
         "atb": ["10"], "padoms": "2 + 8."},
        {"jaut": "Kāda ir starpība starp lielāko un mazāko rezultātu?",
         "atb": ["22"], "padoms": "16 − (−6)."},
        {"jaut": "Cik dažādu rezultātu var iegūt ar trim skaitļiem un divām "
                 "zīmēm?",
         "atb": ["4"], "padoms": "Divas zīmes, katrai divas iespējas."},
    ], pamats=4),

    Petijums("Atrodi visus rezultātus",
             vajag="burtnīca",
             soli=[
                 "Paņem skaitļus 9; 4 un 6.",
                 "Pieraksti visas četras zīmju kombinācijas.",
                 "Izrēķini katru un sakārto rezultātus augošā secībā.",
                 "Atrodi starpību starp lielāko un mazāko.",
                 "Pārbaudi: vai tā ir divkārša otrā un trešā skaitļa summa?",
             ],
             secinajums="Starpība starp lielāko un mazāko rezultātu ir "
                        "2 · (4 + 6) = 20 - tā nav sakritība."),

    Varianti("Kā iegūt lielāko?", [
        {"jaut": "Lai rezultāts būtu vislielākais, visas zīmes ir...",
         "opcijas": ["plusi", "mīnusi", "sajaukti", "vienalga"],
         "pareizi": 0,
         "padoms": "Visu pieskaita."},
        {"jaut": "Lai rezultāts būtu vismazākais, zīmes aiz pirmā skaitļa "
                 "ir...",
         "opcijas": ["mīnusi", "plusi", "sajaukti", "vienalga"],
         "pareizi": 0,
         "padoms": "Visu atņem."},
        {"jaut": "Mainot vienu zīmi no plusa uz mīnusu pie skaitļa 4, "
                 "rezultāts samazinās par...",
         "opcijas": ["8", "4", "2", "16"],
         "pareizi": 0,
         "padoms": "Divkāršs skaitlis."},
        {"jaut": "Ar četriem skaitļiem un trim zīmēm rezultātu ir...",
         "opcijas": ["8", "4", "3", "16"],
         "pareizi": 0,
         "padoms": "2 · 2 · 2."},
    ], pamats=4),

    Pasaule("Kā mainās krājumi?",
            Ievadi("", [
                {"jaut": "Noliktavā 20 kastes. Trīs notikumi: 8; 5; 6. Ja "
                         "visi ir piegādes, cik kastu ir?",
                 "atb": ["39"], "padoms": "20 + 8 + 5 + 6."},
                {"jaut": "Ja visi trīs ir izsūtījumi, cik kastu paliek?",
                 "atb": ["1"], "padoms": "20 − 19."},
                {"jaut": "Ja 8 ir piegāde, bet 5 un 6 - izsūtījumi, cik "
                         "kastu ir?",
                 "atb": ["17"], "padoms": "20 + 8 − 11."},
                {"jaut": "Kāda ir starpība starp lielāko un mazāko iespējamo "
                         "rezultātu?",
                 "atb": ["38"], "padoms": "39 − 1."},
            ]),
            pavediens="tehnika",
            konteksts="Noliktavas atlikums ir viena izteiksme, kurā katrs "
                      "notikums var būt gan pluss, gan mīnuss.",
            kapec="Zīmju izvietojums maina rezultātu vairāk nekā paši "
                  "skaitļi."),

    Kopsavilkums([
        "Ievietoju zīmes, lai iegūtu dažādus rezultātus.",
        "Atrodu lielāko un mazāko iespējamo rezultātu.",
        "Zinu, par cik mainās rezultāts, mainot vienu zīmi.",
        "Saskaitu, cik dažādu rezultātu vispār iespējams iegūt.",
    ]),

    Majas([
        "Ar skaitļiem 12; 5 un 7 atrodi lielāko un mazāko rezultātu.",
        "Pieraksti visas četras kombinācijas.",
        "Pārbaudi, vai starpība ir 2 · (5 + 7).",
    ]),
]
