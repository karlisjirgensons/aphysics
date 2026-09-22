# -*- coding: utf-8 -*-
"""5. klase, 115. stunda: «Kā izmērīt riņķa līnijas garumu?»

Praktiskā stunda: riņķa līnijas garumu ar lineālu tieši nenomērīsi, tāpēc
to mēra ar diegu vai ripinot. Mērījumi tiek pierakstīti tabulā, jo nākamajā
stundā tieši no šīs tabulas parādīsies sakarība starp diametru un garumu.
Tāpēc te svarīgāk ir precīzi pierakstīt nekā precīzi izmērīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis, rinkis)

TEMA = "Kā izmērīt riņķa līnijas garumu?"

MERKIS = ("Mācīsimies praktiski noteikt riņķa līnijas garumu un pierakstīt "
          "mērījumus tabulā.")

SATURS = [
    Sakums("Lineāls te nepalīdz",
           zimejums=rinkis(diametrs="d", virsraksts="Cik gara ir pati "
                                                    "līnija?"),
           paraksts="Riņķa līnija ir izliekta, tāpēc to mēra ar diegu.",
           fakti=["Taisnu nogriezni mēra ar lineālu.",
                  "Izliektu līniju - ar diegu vai ripinot.",
                  "Mērījumus pieraksta tabulā, lai varētu salīdzināt."]),

    Doma("Izliektu līniju iztaisno",
         "Riņķa līnijas garumu mēra, ap to aplokot diegu un pēc tam izstiepjot "
         "diegu gar lineālu, vai arī ripinot apaļu priekšmetu pa lineālu.",
         soli=[
             "Apliec diegu tieši vienu reizi apkārt riņķa līnijai.",
             "Atzīmē vietu, kur diegs satiekas.",
             "Iztaisno diegu un izmēri to ar lineālu.",
             "Izmēri arī diametru.",
             "Ieraksti abus skaitļus tabulā.",
         ],
         pieze="Mērījums vienmēr ir nedaudz neprecīzs: diegs izstiepjas, "
               "lineāls ir ar milimetru iedaļu. Tāpēc tabulā pieraksta to, "
               "kas izmērīts, nevis to, kas «vajadzētu būt»."),

    Petijums("Izmēri trīs apaļas lietas",
             soli=["Izvēlies trīs apaļas lietas: glāzi, bundžu, monētu.",
                   "Katrai izmēri diametru ar lineālu.",
                   "Katrai izmēri līnijas garumu ar diegu.",
                   "Ieraksti abus skaitļus tabulā ar divām ailēm.",
                   "Salīdzini, cik reižu garums ir lielāks par diametru."],
             vajag="diegs, lineāls, trīs apaļas lietas",
             secinajums="Visām lietām garums iznāk apmēram trīs reizes "
                        "lielāks par diametru."),

    Paraugs("Mērījumu tabula",
            uzd="Glāzes diametrs ir 8 cm, līnijas garums 25 cm. Ko var "
                "pierakstīt tabulā?",
            soli=[
                ("Diametrs d = 8 cm",
                 "Pirmā aile."),
                ("Garums C = 25 cm",
                 "Otrā aile."),
                ("25 : 8 ir mazliet vairāk par 3",
                 "Trešā aile - attiecība."),
                ("Tabulā pieraksta visus trīs skaitļus",
                 "Tā mērījumu var salīdzināt ar citiem."),
            ],
            atbilde="d = 8 cm, C = 25 cm, C : d ir apmēram 3"),

    Ievadi("Pieraksti mērījumu", [
        {"jaut": "Diametrs 8 cm, garums 25 cm. Cik apmēram ir garums, dalīts "
                 "ar diametru? Ieraksti veselu skaitli.",
         "atb": ["3"], "padoms": "25 : 8."},
        {"jaut": "Diametrs 10 cm, garums 31 cm. Cik apmēram ir attiecība? "
                 "Ieraksti veselu skaitli.",
         "atb": ["3"], "padoms": "31 : 10."},
        {"jaut": "Diametrs 5 cm, garums 16 cm. Cik apmēram ir attiecība? "
                 "Ieraksti veselu skaitli.",
         "atb": ["3"], "padoms": "16 : 5."},
        {"jaut": "Rādiuss ir 4 cm. Cik centimetru ir diametrs?",
         "atb": ["8"], "padoms": "2 · 4."},
        {"jaut": "Diametrs ir 12 cm. Cik apmēram ir līnijas garums? Ieraksti "
                 "veselu skaitli.",
         "atb": ["36"], "padoms": "Apmēram 3 · 12."},
        {"jaut": "Diametrs ir 20 cm. Cik apmēram ir līnijas garums?",
         "atb": ["60"], "padoms": "Apmēram 3 · 20."},
        {"jaut": "Garums ir apmēram 30 cm. Cik apmēram ir diametrs?",
         "atb": ["10"], "padoms": "30 : 3."},
        {"jaut": "Garums ir apmēram 45 cm. Cik apmēram ir diametrs?",
         "atb": ["15"], "padoms": "45 : 3."},
    ], pamats=4,
        ievads="Mērījumi ir aptuveni, tāpēc arī atbildes te ir aptuvenas."),

    Zimejums("Trīs mērījumi tabulā",
             restis([["d", "8", "10", "5"],
                     ["C", "25", "31", "16"]],
                    virsraksts="Diametrs un garums centimetros"),
             paskaidro="Katrai lietai savs skaitļu pāris. Tieši no šīs "
                       "tabulas nākamajā stundā parādīsies sakarība.",
             ievads="Tabulā mērījumus var salīdzināt blakus."),

    Varianti("Kā mēra izliektu līniju?", [
        {"jaut": "Ar ko mēra riņķa līnijas garumu?",
         "opcijas": ["Ar diegu vai ripinot", "Tikai ar lineālu",
                     "Ar cirkuli", "Ar transportieri"],
         "pareizi": 0,
         "padoms": "Līnija ir izliekta."},
        {"jaut": "Cik reizes diegu apliek apkārt?",
         "opcijas": ["Tieši vienu", "Divas", "Cik sanāk", "Trīs"],
         "pareizi": 0,
         "padoms": "Mēra vienas līnijas garumu."},
        {"jaut": "Kāpēc mērījumi ir neprecīzi?",
         "opcijas": ["Diegs izstiepjas un lineālam ir iedaļas",
                     "Riņķa līnijai nav garuma",
                     "Lineāls ir par īsu",
                     "Tie nav neprecīzi"],
         "pareizi": 0,
         "padoms": "Katram mērījumam ir robeža."},
        {"jaut": "Diametrs ir 10 cm. Cik apmēram ir garums?",
         "opcijas": ["Ap 30 cm", "Ap 20 cm", "Ap 10 cm", "Ap 100 cm"],
         "pareizi": 0,
         "padoms": "Apmēram trīs diametri."},
        {"jaut": "Ko pieraksta tabulā?",
         "opcijas": ["To, kas izmērīts", "To, kas vajadzētu būt",
                     "Vidējo skaitli", "Neko"],
         "pareizi": 0,
         "padoms": "Mērījums ir dati."},
        {"jaut": "Kā vēl var izmērīt garumu?",
         "opcijas": ["Ripinot priekšmetu pa lineālu", "Skaitot rādiusus",
                     "Ar cirkuli", "Ar svariem"],
         "pareizi": 0,
         "padoms": "Viens pilns apgrieziens."},
    ], pamats=4),

    Pasaule("Cik gara ir lente ap spaini?",
            Ievadi("", [
                {"jaut": "Spaiņa diametrs ir 30 cm. Cik apmēram centimetru "
                         "lentes vajag apkārt?",
                 "atb": ["90"], "padoms": "Apmēram 3 · 30."},
                {"jaut": "Caurules diametrs ir 10 cm. Cik apmēram centimetru "
                         "lentes vajag?",
                 "atb": ["30"], "padoms": "Apmēram 3 · 10."},
                {"jaut": "Lente ir 60 cm gara. Ap kādu apmēram diametru tā "
                         "aplieksies?",
                 "atb": ["20"], "padoms": "60 : 3."},
                {"jaut": "Koka stumbra apkārtmērs ir 90 cm. Cik apmēram "
                         "centimetru ir diametrs?",
                 "atb": ["30"], "padoms": "90 : 3."},
            ]),
            pavediens="maja",
            konteksts="Lenti pērk metros, bet apaļas lietas mēra pa "
                      "diametru.",
            kapec="Aptuvenais rēķins «reiz trīs» der jau veikalā."),

    Kopsavilkums([
        "Izmēru riņķa līnijas garumu ar diegu vai ripinot.",
        "Izmēru tās pašas figūras diametru.",
        "Pierakstu mērījumus tabulā.",
        "Zinu, ka mērījums vienmēr ir aptuvens.",
    ]),

    Majas([
        "Izmēri trīs apaļas lietas mājās un pieraksti tabulā.",
        "Katrai aprēķini, cik reižu garums ir lielāks par diametru.",
        "Padomā, kāpēc visiem iznāk apmēram viens un tas pats skaitlis.",
    ]),
]
