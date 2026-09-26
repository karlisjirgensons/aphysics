# -*- coding: utf-8 -*-
"""7. klase, 69. stunda: «Kāpēc grafiks nav ideāla taisne?»

Reālos mērījumos punkti nekad nav precīzi uz taisnes: mērinstrumentam ir
precizitāte, cilvēks nolasa neprecīzi, un process pats nav ideāli
vienmērīgs. Modelim ir arī robežas - svece nevar kļūt negatīva.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, plakne)

TEMA = "Kāpēc grafiks nav ideāla taisne?"

MERKIS = ("Izteiksim pieņēmumus par mērījumu novirzēm un procesa "
          "robežām.")

_DATI = [(0, 12.0), (10, 11.1), (20, 10.3), (30, 9.3), (40, 8.5),
         (50, 7.4)]

SATURS = [
    Sakums("Punkti ap taisni, nevis uz tās",
           zimejums=plakne(grafiki=[(-0.09, 12, "")], punkti=_DATI,
                           no_x=0, lidz_x=60, no_y=6, lidz_y=12, solis=10,
                           solis_y=1, x_nos="min", y_nos="cm"),
           paraksts="Pietuvināts: katrs punkts nedaudz virs vai zem.",
           fakti=["Lineāls mēra ar precizitāti 1 mm.",
                  "Svece deg nevienmērīgi - atkarībā no dakts un vēja.",
                  "Novirzes ir normālas - tās nav kļūda."]),

    Doma("Novirzes un robežas",
         "Mērījumu punkti novirzās no modeļa taisnes mērījumu "
         "neprecizitātes un procesa nevienmērīguma dēļ. Turklāt modelis der "
         "tikai noteiktās robežās.",
         soli=[
             "Novērtē mērinstrumenta precizitāti (piemēram, ±1 mm).",
             "Salīdzini novirzes ar šo precizitāti.",
             "Ja novirzes ir mazas un abos virzienos - modelis ir labs.",
             "Nosaki robežas: kad modelis vairs neder (h < 0, t < 0).",
         ],
         pieze="Ja visas novirzes ir vienā pusē vai tās aug, - process, "
               "iespējams, nav lineārs, un vajag citu modeli."),

    Paraugs("Aprēķini novirzi",
            uzd="Modelis h = −0,09t + 12. Mērījumā pie t = 30 min bija "
                "9,3 cm. Cik liela ir novirze?",
            soli=[
                ("Modelis: h = −0,09 · 30 + 12 = 9,3 (cm)", "Prognoze."),
                ("Mērījums: 9,3 cm", "Dati."),
                ("Novirze: 0 cm", "Šis punkts ir uz taisnes."),
                ("Pie t = 20: modelis 10,2, mērījums 10,3 - novirze 0,1 cm",
                 "Cits punkts."),
            ],
            atbilde="Novirzes ir līdz 0,1-0,2 cm - modelis ir labs."),

    Varianti("Novirzes cēlonis", [
        {"jaut": "Kāpēc mērījums var atšķirties par 1 mm?",
         "opcijas": ["Lineāla precizitāte", "Svece ir salūzusi",
                     "Formula ir nepareiza", "Laiks ir apgriezts"],
         "pareizi": 0,
         "padoms": "Instruments."},
        {"jaut": "Svece pie loga deg ātrāk. Ko tas nozīmē modelim?",
         "opcijas": ["Procesa apstākļi ietekmē k",
                     "Modelis ir bezjēdzīgs", "b kļūst negatīvs",
                     "Grafiks kļūst horizontāls"],
         "pareizi": 0,
         "padoms": "Ātrums mainās."},
        {"jaut": "Modelis prognozē h = −3 cm pēc 170 min. Kāpēc tas "
                 "nav iespējams?",
         "opcijas": ["Modelis der tikai, kamēr h ≥ 0",
                     "Svece aug atpakaļ", "Formula nepareiza",
                     "Laiks nevar būt 170"],
         "pareizi": 0,
         "padoms": "Robeža."},
        {"jaut": "Visi punkti ir virs taisnes sākumā un zem - beigās. Ko "
                 "tas var nozīmēt?",
         "opcijas": ["Process nav lineārs - ātrums mainās",
                     "Viss kārtībā", "Kļūda mērlentē",
                     "Punkti jāizmet"],
         "pareizi": 0,
         "padoms": "Novirzes nav nejaušas."},
    ], pamats=4),

    Zimejums("Nelineārs process: tējas atdzišana",
             plakne(grafiki=[([(0, 90), (5, 72), (10, 59), (15, 50),
                               (20, 43), (30, 35)], "")],
                    punkti=[(0, 90), (5, 72), (10, 59), (15, 50), (20, 43),
                            (30, 35)],
                    no_x=0, lidz_x=30, no_y=20, lidz_y=90, solis=5,
                    solis_y=10, x_nos="min", y_nos="°C"),
             paskaidro="Sākumā atdziest ātri, vēlāk lēnāk - taisne neder."),

    Pasaule("Viedtālruņa akumulatora prognoze",
            Varianti("", [
                {"jaut": "Telefons rāda «atlikušas 5 h», bet pēc stundas - "
                         "«3 h». Kāpēc?",
                 "opcijas": ["Lietojums mainījās - modeļa k mainījās",
                             "Telefons melo", "Laiks iet ātrāk",
                             "Akumulators aug"],
                 "pareizi": 0,
                 "padoms": "Spēles tērē vairāk."},
                {"jaut": "Kāpēc prognoze ir tikai aptuvena?",
                 "opcijas": ["Nākotnes lietojums nav zināms",
                             "Matemātika nestrādā",
                             "Akumulators ir lineārs vienmēr",
                             "Tā ir precīza"],
                 "pareizi": 0,
                 "padoms": "Modelis pieņem, ka turpināsi tāpat."},
                {"jaut": "Kāda ir modeļa robeža?",
                 "opcijas": ["0 % līdz 100 %", "Visi skaitļi",
                             "Tikai pozitīvs laiks", "Nav robežu"],
                 "pareizi": 0,
                 "padoms": "Procenti."},
            ]),
            pavediens="dati",
            konteksts="Telefons pastāvīgi pārrēķina lineāru modeli pēc tā, "
                      "kā to lieto.",
            kapec="Modelis ir labs tik ilgi, kamēr pieņēmumi der."),

    Kopsavilkums([
        "Skaidroju, kāpēc mērījumi novirzās no taisnes.",
        "Aprēķinu novirzi starp modeli un mērījumu.",
        "Nosaku modeļa robežas.",
        "Atpazīstu, kad process nav lineārs.",
    ]),

    Majas([
        "Mēri tējas temperatūru ik pēc 5 min un uzzīmē grafiku.",
        "Novērtē, vai process ir lineārs.",
        "Uzraksti 2 iemeslus, kāpēc tavi punkti nav uz taisnes.",
    ]),
]
