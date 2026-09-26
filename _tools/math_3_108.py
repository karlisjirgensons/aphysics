# -*- coding: utf-8 -*-
"""3. klase, 108. stunda: «Kas ir leņķis?»

Leņķa jēdziens. Tas nav «stūris», bet *pagrieziens* starp diviem stariem no
viena punkta - tieši tāpēc leņķa lielums nav atkarīgs no staru garuma. Šo
atšķirību bērni jauc visbiežāk, tāpēc tā te ir galvenā doma.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, lenkis)

TEMA = "Kas ir leņķis?"

MERKIS = ("Parādīsim leņķus daudzstūros un apkārtnē un lietosim jēdzienu "
          "leņķis.")

SATURS = [
    Sakums("Cik liels pagrieziens ir starp pulksteņa rādītājiem?",
           zimejums=lenkis([(0, "stars"), (60, "stars")],
                           [(0, 60, "leņķis")],
                           "leņķis starp diviem stariem"),
           paraksts="Leņķis ir pagrieziens starp diviem stariem no viena "
                    "punkta.",
           fakti=["Leņķim ir virsotne un divi stari.",
                  "Leņķa lielums nav atkarīgs no staru garuma."]),

    Doma("Leņķis ir pagrieziens, ne garums",
         "Divi stari no viena punkta veido leņķi; jo lielāks pagrieziens, jo "
         "lielāks leņķis.",
         soli=[
             "Atrodi virsotni - punktu, kur stari satiekas.",
             "Paskaties, cik tālu viens stars ir pagriezts no otra.",
             "Jo lielāks pagrieziens, jo lielāks leņķis.",
             "Staru garums leņķa lielumu nemaina.",
         ],
         pieze="Tāpēc, pagarinot pulksteņa rādītāju, laiks nemainās - leņķis "
               "starp rādītājiem paliek tas pats."),

    Paraugs("Cik leņķu ir taisnstūrim?",
            uzd="Saskaiti, cik leņķu ir taisnstūrim, un nosauc to veidu.",
            soli=[
                ("Četras virsotnes",
                 "Katrā virsotnē satiekas divas malas."),
                ("Katrā virsotnē viens leņķis",
                 "Tātad leņķu ir četri."),
                ("Visi ir taisni leņķi",
                 "Tā ir taisnstūra pazīme."),
            ],
            atbilde="4 taisni leņķi"),

    Ievadi("Saskaiti leņķus", [
        {"jaut": "Cik leņķu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Tik, cik virsotņu."},
        {"jaut": "Cik leņķu ir trīsstūrim?", "atb": ["3"],
         "padoms": "Trīs virsotnes."},
        {"jaut": "Cik leņķu ir piecstūrim?", "atb": ["5"],
         "padoms": "Piecas virsotnes."},
        {"jaut": "Cik staru veido vienu leņķi?", "atb": ["2"],
         "padoms": "Divi stari no viena punkta."},
        {"jaut": "Cik virsotņu ir vienam leņķim?", "atb": ["1"],
         "padoms": "Punkts, kur stari satiekas."},
        {"jaut": "Cik leņķu ir sešstūrim?", "atb": ["6"],
         "padoms": "Sešas virsotnes."},
    ], pamats=4),

    Zimejums("Divi dažādi leņķi",
             lenkis([(0, ""), (30, ""), (120, "")],
                    [(0, 30, "mazs"), (30, 120, "liels")],
                    "viens punkts, divi leņķi"),
             paskaidro="Abiem leņķiem virsotne ir viena, bet pagriezieni "
                       "dažādi.",
             ievads="Jo lielāks pagrieziens, jo lielāks leņķis."),

    Varianti("Kas nosaka leņķa lielumu?", [
        {"jaut": "No kā *nav* atkarīgs leņķa lielums?",
         "opcijas": ["No staru garuma", "No pagrieziena",
                     "No staru virziena", "No virsotnes vietas"],
         "pareizi": 0, "padoms": "Garākus starus zīmējot, leņķis nemainās."},
        {"jaut": "Cik staru veido leņķi?",
         "opcijas": ["Divi", "Viens", "Trīs", "Četri"],
         "pareizi": 0, "padoms": "Abi iziet no vienas virsotnes."},
        {"jaut": "Kur atrodas leņķa virsotne?",
         "opcijas": ["Kur stari satiekas", "Stara galā",
                     "Stara vidū", "Ārpus leņķa"],
         "pareizi": 0, "padoms": "Tas ir kopīgais punkts."},
        {"jaut": "Cik leņķu ir astoņstūrim?",
         "opcijas": ["8", "4", "6", "16"],
         "pareizi": 0, "padoms": "Tik, cik virsotņu."},
    ], pamats=4),

    Pasaule("Kā pagriežas robota roka?",
            Ievadi("", [
                {"jaut": "Robota roka pagriežas 4 reizes pa vienam taisnam "
                         "leņķim. Cik taisnu leņķu tas ir?",
                 "atb": ["4"], "padoms": "Viens pilns aplis."},
                {"jaut": "Cik taisnu leņķu ir vienā pilnā apgriezienā?",
                 "atb": ["4"], "padoms": "Četri pagriezieni pa taisnam "
                                         "leņķim."},
                {"jaut": "Robots pagriežas 2 taisnus leņķus. Kurp tas "
                         "skatās - uz priekšu vai atpakaļ? Raksti «atpakaļ» "
                         "vai «uz priekšu».",
                 "atb": ["atpakaļ"], "padoms": "Divi taisni leņķi ir puse "
                                               "apgrieziena.",
                 "tastatura": "text"},
                {"jaut": "Cik taisnu leņķu ir trijos pilnos apgriezienos?",
                 "atb": ["12"], "padoms": "3 · 4."},
            ]),
            pavediens="tehnika",
            konteksts="Robota locītavu pagriezienus programmē leņķos - tieši "
                      "tāpēc leņķis ir pagrieziens, ne stūris.",
            kapec="Ja leņķis nav pareizs, roka aiziet garām mērķim."),

    Kopsavilkums([
        "Zinu, ka leņķis ir pagrieziens starp diviem stariem.",
        "Atrodu leņķa virsotni un starus.",
        "Zinu, ka leņķa lielums nav atkarīgs no staru garuma.",
        "Saskaitu leņķus daudzstūrī.",
    ]),

    Majas([
        "Atrodi mājās piecus leņķus un parādi katram virsotni.",
        "Pagriez pulksteņa rādītāju un vēro, kā mainās leņķis.",
        "Uzzīmē divus leņķus ar vienu virsotni.",
    ]),
]
