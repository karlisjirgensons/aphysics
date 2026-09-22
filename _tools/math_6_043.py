# -*- coding: utf-8 -*-
"""6. klase, 43. stunda: «Kura izteiksme ir lielāka?»

Mikrotemata noslēgums. Salīdzināt izteiksmes, tās neizrēķinot, ir gan ātrāk,
gan drošāk - un tieši tas eksāmenā ir viens no biežākajiem uzdevumu veidiem.
Rīks ir viens: novērtējums un vieninieka robeža.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kura izteiksme ir lielāka?"

MERKIS = ("Mācīsimies salīdzināt izteiksmes ar decimāldaļu reizinājumiem, "
          "novērtējot to aptuvenās vērtības.")

SATURS = [
    Sakums("Salīdzināt var, neizrēķinot",
           fakti=["48 · 0,9 ir mazāks par 48, jo 0,9 ir mazāks par 1.",
                  "48 · 1,1 ir lielāks par 48 - tā paša iemesla dēļ.",
                  "Tātad pirmā izteiksme ir mazāka, un rēķināt nevajag."]),

    Doma("Skaties uz reizinātāju, ne uz reizinājumu",
         "Salīdzinot izteiksmes ar vienu un to pašu skaitli, izšķir "
         "reizinātājs: vai tas ir lielāks vai mazāks par 1.",
         soli=[
             "Pārbaudi, vai abās izteiksmēs ir viens un tas pats skaitlis.",
             "Salīdzini reizinātājus ar vieninieku.",
             "Lielāks reizinātājs dod lielāku reizinājumu.",
             "Ja skaitļi ir dažādi, noapaļo abus un salīdzini novērtējumus.",
             "Ja novērtējumi ir tuvu, izrēķini precīzi.",
         ],
         pieze="Dalīšanai likums ir apgriezts: 48 : 0,9 ir *lielāks* par 48. "
               "Tāpēc vienmēr vispirms nosaki darbību, tikai tad salīdzini."),

    Slidnis("Viens skaitlis, dažādi reizinātāji",
            [{"v": "40 · 0,5", "teksts": "= 20", "josla": 25},
             {"v": "40 · 0,9", "teksts": "= 36", "josla": 45},
             {"v": "40 · 1", "teksts": "= 40 - robeža", "josla": 50},
             {"v": "40 · 1,2", "teksts": "= 48", "josla": 60},
             {"v": "40 · 2", "teksts": "= 80", "josla": 100}],
            ievads="Spied soli pa solim: skaitlis 40 nemainās. Robeža, kur "
                   "rezultāts pāriet pāri 40, ir tieši pie vieninieka."),

    Paraugs("Salīdzini, neizrēķinot",
            uzd="Kura izteiksme ir lielāka: 7,2 · 0,98 vai 7,2 · 1,02?",
            soli=[
                ("Abās ir viens un tas pats skaitlis 7,2",
                 "Tātad izšķir reizinātājs."),
                ("0,98 ir mazāks par 1",
                 "Pirmais reizinājums būs mazāks par 7,2."),
                ("1,02 ir lielāks par 1",
                 "Otrais būs lielāks par 7,2."),
                ("Tātad otrā izteiksme ir lielāka",
                 "Precīzs rēķins nav vajadzīgs."),
            ],
            atbilde="7,2 · 1,02"),

    Ievadi("Salīdzini bez rēķināšanas", [
        {"jaut": "25 · 0,8 ir lielāks vai mazāks par 25? Raksti «lielāks» "
                 "vai «mazāks».",
         "atb": ["mazāks"], "padoms": "0,8 ir mazāks par 1."},
        {"jaut": "25 · 1,4 ir lielāks vai mazāks par 25?",
         "atb": ["lielāks"], "padoms": "1,4 ir lielāks par 1."},
        {"jaut": "25 : 0,5 ir lielāks vai mazāks par 25?",
         "atb": ["lielāks"], "padoms": "Dalot ar mazāku par 1."},
        {"jaut": "Cik apmēram ir 9,8 · 3,1? Raksti veselu skaitli.",
         "atb": ["30"], "padoms": "10 · 3."},
        {"jaut": "Cik apmēram ir 19,7 · 0,52? Raksti veselu skaitli.",
         "atb": ["10"], "padoms": "20 · 0,5."},
        {"jaut": "Cik apmēram ir 4,1 · 5,9? Raksti veselu skaitli.",
         "atb": ["24"], "padoms": "4 · 6."},
    ], pamats=4,
        ievads="Vispirms novērtē, tikai tad - ja vajag - rēķini."),

    Varianti("Kura ir lielāka?", [
        {"jaut": "6,4 · 0,99 vai 6,4?",
         "opcijas": ["6,4", "6,4 · 0,99", "Vienādas", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "0,99 ir mazāks par 1."},
        {"jaut": "12 · 0,5 vai 12 : 0,5?",
         "opcijas": ["12 : 0,5", "12 · 0,5", "Vienādas", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Viena dod 6, otra 24."},
        {"jaut": "8,9 · 4,1 vai 9 · 4?",
         "opcijas": ["8,9 · 4,1", "9 · 4", "Vienādas", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "36,49 pret 36 - novērtējums šeit nepietiek, jārēķina."},
        {"jaut": "Kad novērtējums nepietiek?",
         "opcijas": ["Kad abi novērtējumi ir vienādi",
                     "Kad skaitļi ir lieli",
                     "Kad ir komats", "Novērtējums pietiek vienmēr"],
         "pareizi": 0,
         "padoms": "Tad jārēķina precīzi."},
    ], pamats=4),

    Pasaule("Kurš piedāvājums ir izdevīgāks?",
            Ievadi("", [
                {"jaut": "Prece maksā 40 €. Pirmais veikals dod 0,9 no "
                         "cenas, otrs - 0,85. Cik eiro maksā pirmajā?",
                 "atb": ["36"], "padoms": "40 · 0,9."},
                {"jaut": "Cik eiro maksā otrajā?",
                 "atb": ["34"], "padoms": "40 · 0,85."},
                {"jaut": "Cik eiro ietaupa, izvēloties izdevīgāko?",
                 "atb": ["2"], "padoms": "36 − 34."},
                {"jaut": "Trešais veikals prasa 1,05 no cenas. Cik eiro?",
                 "atb": ["42"], "padoms": "40 · 1,05."},
            ]),
            pavediens="veikals",
            konteksts="Reklāmā cenas mēdz rakstīt kā reizinātājus - tad "
                      "salīdzināt var, neizrēķinot nevienu summu.",
            kapec="Mazāks reizinātājs nozīmē lētāku preci, ja pamatcena ir "
                  "viena."),

    Kopsavilkums([
        "Salīdzinu izteiksmes, neizrēķinot tās līdz galam.",
        "Lietoju vieninieka robežu reizināšanai un dalīšanai.",
        "Novērtēju izteiksmes, noapaļojot abus skaitļus.",
        "Zinu, kad novērtējums nepietiek un jārēķina precīzi.",
    ]),

    Majas([
        "Salīdzini 15 · 0,97 un 15 : 0,97, neizrēķinot.",
        "Atrodi divas izteiksmes, kuras novērtējums nespēj atšķirt.",
        "Novērtē, cik maksās 2,9 kg preces par 4,1 € kilogramā.",
    ]),
]
