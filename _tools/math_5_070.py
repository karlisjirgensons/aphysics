# -*- coding: utf-8 -*-
"""5. klase, 70. stunda: «Ko nozīmē dalīt daļu?»

Temata pēdējā stunda pirms pārbaudes darba, un vienīgā, kurā daļu dala.
Formulu te nemāca - 5. klasē pietiek ar modeli un ar diviem jautājumiem,
kas izskatās līdzīgi, bet nozīmē pretējo: «sadalīt daļu gabalos» un «cik
reižu daļa ietilpst veselajā».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Ko nozīmē dalīt daļu?"

MERKIS = ("Mācīsimies ar modeli izskaidrot pamatdaļas dalīšanu ar veselu "
          "skaitli un vesela skaitļa dalīšanu ar pamatdaļu.")

SATURS = [
    Sakums("Puse torte - un trīs cilvēki",
           zimejums=dala(6, 1, "1/6"),
           paraksts="{1|2} sadalīta trīs daļās - katram tiek {1|6}.",
           fakti=["Puse, sadalīta trīs daļās, nav trešdaļa.",
                  "Gabals kļūst mazāks, tātad saucējs - lielāks.",
                  "{1|2} : 3 = {1|6}."]),

    Doma("Dalot daļu, gabali kļūst sīkāki",
         "Dalot pamatdaļu ar veselu skaitli, saucēju reizina ar šo skaitli; "
         "dalot veselu skaitli ar pamatdaļu, skaita, cik reižu daļa tajā "
         "ietilpst.",
         soli=[
             "Izlasi, kurš no diviem jautājumiem uzdots.",
             "Ja daļu dala gabalos - saucēju reizina ar dalītāju.",
             "Ja meklē, cik reižu daļa ietilpst - reizina veselo ar saucēju.",
             "Pārbaudi atbildi ar zīmējumu.",
         ],
         pieze="{1|2} : 3 = {1|6}, jo katrs gabals kļūst trīsreiz mazāks. "
               "Bet 3 : {1|2} = 6, jo trijos veselos ietilpst sešas puses. "
               "Pirmajā gadījumā atbilde ir mazāka, otrajā - lielāka."),

    Paraugs("Divi jautājumi par pusi",
            uzd="Cik ir {1|2} : 3 un cik ir 3 : {1|2}?",
            soli=[
                ("{1|2} : 3 - pusi dala trijās daļās",
                 "Katrs gabals kļūst trīsreiz sīkāks."),
                ("{1|2} : 3 = {1|6}",
                 "Saucēju reizina ar 3."),
                ("3 : {1|2} - cik pušu ir trijos veselos",
                 "Skaita gabalus, nevis dala tos."),
                ("3 : {1|2} = 6",
                 "Katrā veselā ir divas puses; 3 · 2 = 6."),
            ],
            atbilde="{1|2} : 3 = {1|6}, bet 3 : {1|2} = 6"),

    Ievadi("Sadali vai saskaiti gabalus", [
        {"jaut": "Cik ir {1|2} : 2? Atbildi raksti kā a/b.",
         "atb": ["1/4"], "padoms": "Saucēju reizina ar 2."},
        {"jaut": "Cik ir {1|3} : 2? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "Saucēju reizina ar 2."},
        {"jaut": "Cik ir {1|4} : 3? Atbildi raksti kā a/b.",
         "atb": ["1/12"], "padoms": "Saucēju reizina ar 3."},
        {"jaut": "Cik ir {1|5} : 2? Atbildi raksti kā a/b.",
         "atb": ["1/10"], "padoms": "Saucēju reizina ar 2."},
        {"jaut": "Cik ceturtdaļu ir divos veselos? Jeb cik ir 2 : {1|4}?",
         "atb": ["8"], "padoms": "Katrā veselā četras ceturtdaļas."},
        {"jaut": "Cik trešdaļu ir četros veselos? Jeb cik ir 4 : {1|3}?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "Cik pušu ir piecos veselos? Jeb cik ir 5 : {1|2}?",
         "atb": ["10"], "padoms": "5 · 2."},
        {"jaut": "Cik astotdaļu ir trijos veselos? Jeb cik ir 3 : {1|8}?",
         "atb": ["24"], "padoms": "3 · 8."},
    ], pamats=4,
        ievads="Pirms rēķina izlem: gabalus sadala vai gabalus skaita."),

    Zimejums("Puse, sadalīta trijās daļās",
             dala(6, 3, "1/2 = 3/6"),
             paskaidro="Puse aizņem trīs sestdaļas. Ja to sadala trim "
                       "cilvēkiem, katram tiek viena sestdaļa.",
             ievads="Sadalītā puse ir redzama tajās pašās sestdaļās."),

    Varianti("Kurš rēķins te vajadzīgs?", [
        {"jaut": "Pusi tortes sadala 4 cilvēkiem. Cik tiek katram?",
         "opcijas": ["{1|8}", "{1|4}", "{1|2}", "2"],
         "pareizi": 0,
         "padoms": "{1|2} : 4."},
        {"jaut": "Cik reižu {1|4} ietilpst vienā veselā?",
         "opcijas": ["4", "1", "{1|4}", "8"],
         "pareizi": 0,
         "padoms": "Viens vesels ir četras ceturtdaļas."},
        {"jaut": "Dalot daļu ar veselu skaitli, atbilde ir...",
         "opcijas": ["Mazāka par doto daļu", "Lielāka par doto daļu",
                     "Vesels skaitlis", "Tā pati daļa"],
         "pareizi": 0,
         "padoms": "Gabals kļūst sīkāks."},
        {"jaut": "Dalot veselu skaitli ar pamatdaļu, atbilde ir...",
         "opcijas": ["Lielāka par doto skaitli", "Mazāka par doto skaitli",
                     "Daļa", "Nulle"],
         "pareizi": 0,
         "padoms": "Mazu gabalu ietilpst daudz."},
        {"jaut": "Cik ir {1|3} : 3?",
         "opcijas": ["{1|9}", "{1|6}", "1", "{3|3}"],
         "pareizi": 0,
         "padoms": "Saucēju reizina ar 3."},
        {"jaut": "Skolēns raksta {1|2} : 3 = {1|3}. Kur ir kļūda?",
         "opcijas": ["Saucējs nav reizināts ar 3",
                     "Skaitītājs nav reizināts",
                     "Jādala skaitītājs",
                     "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "{1|2} : 3 = {1|6}."},
    ], pamats=4),

    Pasaule("Cik skolēniem pietiks?",
            Ievadi("", [
                {"jaut": "Puse kūkas jāsadala 3 skolēniem. Cik tiek katram? "
                         "Atbildi raksti kā a/b.",
                 "atb": ["1/6"], "padoms": "{1|2} : 3."},
                {"jaut": "Ceturtdaļa picas jāsadala 2 skolēniem. Cik tiek "
                         "katram? Atbildi raksti kā a/b.",
                 "atb": ["1/8"], "padoms": "{1|4} : 2."},
                {"jaut": "Ir 4 veselas picas, katram dod {1|4} picas. Cik "
                         "skolēnu paēdinās?",
                 "atb": ["16"], "padoms": "4 · 4."},
                {"jaut": "Ir 6 veselas kūkas, katram dod {1|3} kūkas. Cik "
                         "skolēnu paēdinās?",
                 "atb": ["18"], "padoms": "6 · 3."},
            ]),
            pavediens="skola",
            konteksts="Klases svētkos abi jautājumi ir vienā elpas vilcienā: "
                      "cik tiek katram un cik cilvēkiem pietiks.",
            kapec="Tie ir divi dažādi dalījumi, tāpēc arī atbildes ir "
                  "pretējas."),

    Kopsavilkums([
        "Modelēju pamatdaļas dalīšanu ar veselu skaitli.",
        "Modelēju vesela skaitļa dalīšanu ar pamatdaļu.",
        "Atšķiru abus jautājumus pēc tā, kas ar ko tiek dalīts.",
        "Novērtēju, vai atbildei jābūt lielākai vai mazākai par doto.",
    ]),

    Majas([
        "Uzzīmē modeli, kas parāda {1|3} : 2.",
        "Izrēķini, cik sestdaļu ir piecos veselos.",
        "Izdomā vienu dzīves uzdevumu katram no abiem dalījuma veidiem.",
    ]),
]
