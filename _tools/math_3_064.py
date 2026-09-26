# -*- coding: utf-8 -*-
"""3. klase, 64. stunda: «Kas notiek, reizinot ar 10 un 100?»

11. stundā likumsakarība bija par 10; tagad tai pievienojas 100, un abas
kopā kļūst par rīku, bez kura mērogu aprēķināt nevar. Kalkulators te ir
pārbaudes rīks: skolēns vispirms prognozē, tad pārbauda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kas notiek, reizinot ar 10 un 100?"

MERKIS = ("Reizināsim un dalīsim ar 10 un 100, pārbaudīsim ar kalkulatoru un "
          "formulēsim likumsakarību.")

SATURS = [
    Sakums("Cik nulles pieliek reizinājums ar 100?",
           zimejums=restis([[7, "· 10 =", 70],
                            [7, "· 100 =", 700],
                            [70, ": 10 =", 7],
                            [700, ": 100 =", 7]],
                           "nulles nāk un iet"),
           paraksts="Reizinot pieliek, dalot noņem - tik nulles, cik "
                    "reizinātājā.",
           fakti=["Reizinot ar 10, pieliek vienu nulli.",
                  "Reizinot ar 100, pieliek divas nulles.",
                  "Dalot ar 100, divas nulles noņem."]),

    Doma("Cik nulles reizinātājā, tik cipari pārceļas",
         "Reizinot ar 10, katrs cipars pārceļas vienu vietu pa kreisi; "
         "reizinot ar 100 - divas vietas.",
         soli=[
             "Saskaiti nulles reizinātājā: 10 ir viena, 100 ir divas.",
             "Tik pašu nulļu pieliec skaitlim galā.",
             "Dalot dari otrādi - noņem tikpat nulļu.",
             "Pārbaudi ar kalkulatoru.",
         ],
         pieze="Dalot noņemt var tikai tad, ja nulles skaitlim galā tiešām "
               "ir: 340 : 10 = 34, bet 345 : 10 nav vesels skaitlis."),

    Paraugs("Cik ir 24 · 100?",
            uzd="Izrēķini 24 · 100 un paskaidro, kas notika ar cipariem.",
            soli=[
                ("100 - divas nulles",
                 "Tātad cipari pārcelsies divas vietas pa kreisi."),
                ("24 → 2400",
                 "Divnieks no desmitiem kļuva par tūkstošiem, četrinieks - "
                 "par simtiem."),
                ("24 · 100 = 2400",
                 "Pārbaude ar kalkulatoru: sakrīt."),
            ],
            atbilde="2400"),

    Petijums("Pārbaudi ar kalkulatoru",
             vajag="kalkulators un lapa",
             soli=[
                 "Uzraksti piecus skaitļus no 1 līdz 99.",
                 "Prognozē, kas sanāks, reizinot katru ar 100.",
                 "Pārbaudi ar kalkulatoru.",
                 "Uzraksti vienā teikumā, ko pamanīji.",
             ],
             secinajums="Reizinot ar 100, pie skaitļa vienmēr nāk klāt tieši "
                        "divas nulles - tas strādā visiem skaitļiem."),

    Ievadi("Reizini un dali", [
        {"jaut": "35 · 10 = ?", "atb": ["350"], "padoms": "Viena nulle."},
        {"jaut": "35 · 100 = ?", "atb": ["3500"], "padoms": "Divas nulles."},
        {"jaut": "600 : 10 = ?", "atb": ["60"], "padoms": "Noņem nulli."},
        {"jaut": "600 : 100 = ?", "atb": ["6"], "padoms": "Noņem divas "
                                                          "nulles."},
        {"jaut": "8 · 100 = ?", "atb": ["800"], "padoms": "Divas nulles."},
        {"jaut": "4500 : 100 = ?", "atb": ["45"], "padoms": "Noņem divas "
                                                            "nulles."},
    ], pamats=4),

    Zimejums("Vietas pārceļas",
             restis([["T", "S", "D", "V"],
                     ["", "", 2, 4],
                     [2, 4, 0, 0]],
                    "24 un 24 · 100"),
             paskaidro="Cipari ir tie paši - tikai pārcēlušies divas vietas "
                       "pa kreisi.",
             ievads="Skaties, kur atrodas 2 un 4."),

    Varianti("Cik nulles nāks klāt?", [
        {"jaut": "Cik ir 12 · 100?",
         "opcijas": ["1200", "120", "112", "12000"],
         "pareizi": 0, "padoms": "Divas nulles."},
        {"jaut": "Cik ir 9000 : 100?",
         "opcijas": ["90", "900", "9", "9000"],
         "pareizi": 0, "padoms": "Noņem divas nulles."},
        {"jaut": "Kurš rēķins dod 700?",
         "opcijas": ["7 · 100", "7 · 10", "70 · 100", "700 · 10"],
         "pareizi": 0, "padoms": "Septiņi simti."},
        {"jaut": "Kuru skaitli nevar izdalīt ar 100 bez atlikuma?",
         "opcijas": ["345", "300", "1200", "900"],
         "pareizi": 0, "padoms": "Tam galā nav divu nulļu."},
    ], pamats=4),

    Pasaule("Cik metru ir ceļojumā?",
            Ievadi("", [
                {"jaut": "1 km ir 1000 m. Cik metru ir 3 km?",
                 "atb": ["3000"], "padoms": "3 · 1000."},
                {"jaut": "Cik kilometru ir 7000 m?",
                 "atb": ["7"], "padoms": "7000 : 1000."},
                {"jaut": "Autobuss brauc 60 km stundā. Cik kilometru tas "
                         "nobrauc 10 stundās?",
                 "atb": ["600"], "padoms": "60 · 10."},
                {"jaut": "Cik metru tas ir?",
                 "atb": ["600000", "600 000"], "padoms": "600 · 1000."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojumā attālumu raksta kilometros, bet karte rēķina "
                      "metros - tāpēc pārrēķins vajadzīgs visu laiku.",
            kapec="Reizināšana ar 1000 ir tā pati likumsakarība - tikai trīs "
                  "nulles."),

    Kopsavilkums([
        "Reizinu un dalu ar 10 un 100 bez pieraksta.",
        "Zinu, cik nulles nāk klāt vai tiek noņemtas.",
        "Prognozēju rezultātu un pārbaudu to ar kalkulatoru.",
        "Zinu, kad dalīt ar 100 nevar.",
    ]),

    Majas([
        "Izrēķini 17 · 10, 17 · 100 un 1700 : 100.",
        "Pārbaudi visus trīs ar kalkulatoru.",
        "Atrodi mājās iepakojumu, uz kura ir skaitlis ar divām nullēm galā.",
    ]),
]
