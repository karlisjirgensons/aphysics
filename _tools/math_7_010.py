# -*- coding: utf-8 -*-
"""7. klase, 10. stunda: «Vai secībai ir nozīme?»

Iepriekšējā stundā iemācījāmies atšķirt izlasi no apakškopas. Tagad to
pašu lieto, lai pamatotu spriedumu: kāpēc tieši šajā situācijā secība ir
svarīga. Stunda beidzas ar rokasspiedienu un sūtītām vēstulēm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Vai secībai ir nozīme?"

MERKIS = ("Iemācīsimies pamatot, vai konkrētajā situācijā izvēles secībai "
          "ir nozīme, un saskaitīt gadījumus.")

SATURS = [
    Sakums("Rokasspiedieni un apsveikumi",
           fakti=["5 draugi sasveicinās ar rokasspiedienu - cik to ir?",
                  "5 draugi viens otram nosūta apsveikumu - cik to ir?",
                  "Skaitļi atšķiras divreiz. Kāpēc?"]),

    Doma("Pamato ar vienu jautājumu",
         "Secībai ir nozīme, ja samainot divus izvēlētos rodas cits "
         "gadījums. Rokasspiediens Anna-Bens ir tas pats, kas Bens-Anna; "
         "vēstule no Annas Benam nav tā pati, kas no Bena Annai.",
         soli=[
             "Uzraksti vienu gadījumu, piemēram, (A; B).",
             "Samaini: (B; A). Vai tas ir cits gadījums?",
             "Ja jā - skaiti sakārtotus pārus: n · (n − 1).",
             "Ja nē - dali ar 2: n · (n − 1) : 2.",
         ],
         pieze="Pamatojumā uzraksti tieši šo samainīšanas pārbaudi - tā ir "
               "argumentācija, ko prasa eksāmenā."),

    Paraugs("Rokasspiedieni",
            uzd="Sapulcē ir 6 cilvēki. Katrs ar katru sarokojas vienu "
                "reizi. Cik rokasspiedienu?",
            soli=[
                ("Katrs sarokojas ar 5 citiem: 6 · 5 = 30",
                 "Katru rokasspiedienu tā saskaita divreiz."),
                ("A-B un B-A ir viens rokasspiediens",
                 "Secībai nav nozīmes."),
                ("30 : 2 = 15", "Dala ar 2."),
            ],
            atbilde="15 rokasspiedienu"),

    Varianti("Pamato", [
        {"jaut": "Futbola turnīrā 8 komandas, katra ar katru spēlē vienu "
                 "reizi. Vai secībai ir nozīme?",
         "opcijas": ["Nē - spēle A pret B ir tā pati, kas B pret A",
                     "Jā - viena komanda ir mājās",
                     "Jā - viena uzvar",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Viena spēle - viens pāris."},
        {"jaut": "Tas pats turnīrs, bet katrs pāris spēlē divreiz - mājās "
                 "un izbraukumā. Vai secībai ir nozīme?",
         "opcijas": ["Jā - A mājās pret B ir cita spēle nekā B mājās pret A",
                     "Nē - komandas ir tās pašas",
                     "Tikai finālā",
                     "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Mājas laukums ir «pirmā vieta»."},
        {"jaut": "Cik spēļu ir 8 komandu turnīrā vienā aplī?",
         "opcijas": ["28", "56", "64", "16"],
         "pareizi": 0,
         "padoms": "8 · 7 : 2."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "7 draugi sarokojas katrs ar katru. Cik rokasspiedienu?",
         "atb": ["21"], "padoms": "7 · 6 : 2."},
        {"jaut": "7 draugi nosūta katrs katram īsziņu. Cik īsziņu?",
         "atb": ["42"], "padoms": "7 · 6."},
        {"jaut": "Turnīrā 10 šahisti, katrs ar katru spēlē vienu partiju. "
                 "Cik partiju?",
         "atb": ["45"], "padoms": "10 · 9 : 2."},
        {"jaut": "Grupā ir 5 cilvēki. Cik dažādos veidos var izvēlēties "
                 "priekšsēdētāju un sekretāru?",
         "atb": ["20"], "padoms": "5 · 4."},
        {"jaut": "Bija 36 rokasspiedieni, katrs ar katru. Cik cilvēku?",
         "atb": ["9"], "padoms": "n · (n − 1) = 72."},
        {"jaut": "Hokeja līgā 6 komandas, katrs pāris spēlē 2 reizes "
                 "(mājās un izbraukumā). Cik spēļu?",
         "atb": ["30"], "padoms": "6 · 5."},
    ], pamats=4),

    Pasaule("Līgas kalendārs",
            Ievadi("", [
                {"jaut": "Virslīgā ir 10 komandas; katrs pāris spēlē 4 "
                         "reizes. Cik spēļu sezonā?",
                 "atb": ["180"], "padoms": "Pāru ir 45; 45 · 4."},
                {"jaut": "Katra kārta ir 5 spēles (visas komandas spēlē). "
                         "Cik kārtu sezonā?",
                 "atb": ["36"], "padoms": "180 : 5."},
                {"jaut": "Cik spēļu sezonā aizvada viena komanda?",
                 "atb": ["36"], "padoms": "9 pretinieki · 4."},
            ]),
            pavediens="sports",
            konteksts="Līgas vadība kalendāru plāno tieši ar šo rēķinu, "
                      "vēl pirms sezonas sākuma.",
            kapec="Vispirms pāri, tad atkārtojumi - divi soļi."),

    Kopsavilkums([
        "Pamatoju, vai secībai ir nozīme, ar samainīšanas pārbaudi.",
        "Sakārtoti pāri: n · (n − 1).",
        "Nesakārtoti pāri: n · (n − 1) : 2.",
        "Pierakstu pamatojumu vārdiem.",
    ]),

    Majas([
        "Cik rokasspiedienu būtu tavā klasē?",
        "Izdomā situāciju, kur tas pats skaits cilvēku dod divreiz vairāk "
        "gadījumu.",
        "Pārbaudi ar 4 cilvēkiem, uzzīmējot visus rokasspiedienus.",
    ]),
]
