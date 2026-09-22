# -*- coding: utf-8 -*-
"""5. klase, 141. stunda: «Kā pārbaudīt atņemšanu?»

Pārbaude ar saskaitīšanu skolēnam ir zināma jau no 4. klases, bet decimāldaļām
tā kļūst daudz vajadzīgāka: te ir vairāk vietu, kur kļūdīties - nobīdīts
komats, aizmirsta nulle, neizdarīta aizņemšanās. Tāpēc stunda ne tikai
pārbauda, bet arī nosauc katru kļūdu vārdā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pārbaudīt atņemšanu?"

MERKIS = ("Iemācīsimies pārbaudīt starpību ar saskaitīšanu un nosaukt "
          "iespējamās kļūdas.")

SATURS = [
    Sakums("Pārbaude ir viena saskaitīšana",
           zimejums=restis([["2,03", "+", "1,57", "3,6"]],
                           virsraksts="Starpība plus atņēmējs"),
           paraksts="Ja summa sakrīt ar mazināmo, atņemšana ir pareiza.",
           fakti=["Atņemšanu pārbauda ar saskaitīšanu.",
                  "Starpībai plus atņēmējam jādod mazināmais.",
                  "Ja nesakrīt, kļūda ir vienā no trim vietām."]),

    Doma("Starpība plus atņēmējs ir mazināmais",
         "Atņemšanu pārbauda, starpībai pieskaitot atņēmēju: ja iznāk "
         "mazināmais, rēķins ir pareizs.",
         soli=[
             "Pieraksti iegūto starpību.",
             "Pieskaiti tai atņēmēju.",
             "Salīdzini summu ar mazināmo.",
             "Ja sakrīt - rēķins pareizs.",
             "Ja nesakrīt, meklē komatu, nulles un aizņemšanos.",
         ],
         pieze="Trīs biežākās kļūdas: komats nav zem komata, nav pierakstīta "
               "nulle beigās, nav izdarīta aizņemšanās. Katra no tām atstāj "
               "savu pēdu, un pārbaude tās visas pamana."),

    Paraugs("Pārbaudi 3,6 - 1,57 = 2,03",
            uzd="Vai starpība ir aprēķināta pareizi?",
            soli=[
                ("Starpība ir 2,03",
                 "Iegūtais rezultāts."),
                ("2,03 + 1,57",
                 "Pieskaita atņēmēju."),
                ("3 + 7 = 10 simtdaļas, pāriet 1",
                 "Saskaita kolonnā."),
                ("0 + 5 + 1 = 6 desmitdaļas",
                 "Nākamā kolonna."),
                ("2 + 1 = 3; summa 3,60 = 3,6",
                 "Sakrīt ar mazināmo - pareizi."),
            ],
            atbilde="Rēķins ir pareizs"),

    Ievadi("Pārbaudi ar saskaitīšanu", [
        {"jaut": "2,03 + 1,57 = ? Ieraksti skaitli.",
         "atb": ["3,6", "3,60"], "padoms": "Saskaiti kolonnā."},
        {"jaut": "Vai 3,6 - 1,57 = 2,03 ir pareizi? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Pārbaude sakrita."},
        {"jaut": "3,15 + 2,25 = ? Ieraksti skaitli.",
         "atb": ["5,4", "5,40"], "padoms": "Saskaiti kolonnā."},
        {"jaut": "Vai 5,4 - 2,25 = 3,15 ir pareizi?",
         "atb": ["jā", "ja"], "padoms": "Pārbaude sakrita."},
        {"jaut": "Skolēns raksta 4,5 - 1,8 = 3,3. Cik ir 3,3 + 1,8?",
         "atb": ["5,1"], "padoms": "Saskaiti."},
        {"jaut": "Vai 4,5 - 1,8 = 3,3 ir pareizi?",
         "atb": ["nē", "ne"], "padoms": "Iznāca 5,1, nevis 4,5."},
        {"jaut": "Kāda ir pareizā atbilde uzdevumam 4,5 - 1,8?",
         "atb": ["2,7"], "padoms": "45 - 18 desmitdaļas."},
        {"jaut": "Cik ir 2,7 + 1,8?",
         "atb": ["4,5", "4,50"], "padoms": "Pārbaude sakrīt."},
    ], pamats=4,
        ievads="Vienmēr pieskaiti starpībai atņēmēju un salīdzini."),

    Zimejums("Pārbaude kolonnā",
             restis([["2", ",", "0", "3"],
                     ["1", ",", "5", "7"],
                     ["3", ",", "6", "0"]],
                    virsraksts="Summa ir mazināmais"),
             paskaidro="Apakšējā rinda ir tieši tas skaitlis, no kura "
                       "sākumā atņēma. Tas arī nozīmē, ka rēķins ir pareizs.",
             ievads="Pārbaude izskatās kā parasta saskaitīšana."),

    Varianti("Kur bija kļūda?", [
        {"jaut": "Kā pārbauda atņemšanu?",
         "opcijas": ["Starpībai pieskaita atņēmēju",
                     "Starpību atņem no mazināmā",
                     "Saskaita visus trīs skaitļus",
                     "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Saskaitīšana ir pretējā darbība."},
        {"jaut": "Pārbaudē iznāca lielāks skaitlis nekā mazināmais. Ko tas "
                 "nozīmē?",
         "opcijas": ["Starpība ir par lielu", "Viss kārtībā",
                     "Atņēmējs ir nepareizs", "Nekas"],
         "pareizi": 0,
         "padoms": "Atņemts par maz."},
        {"jaut": "Kura ir biežākā kļūda ar decimāldaļām?",
         "opcijas": ["Komats nav zem komata", "Pārāk gari skaitļi",
                     "Nepareiza reizināšana", "Tādu nav"],
         "pareizi": 0,
         "padoms": "Šķiras sajūk."},
        {"jaut": "4,5 - 1,8: kāda ir pareizā atbilde?",
         "opcijas": ["2,7", "3,3", "3,7", "2,3"],
         "pareizi": 0,
         "padoms": "45 - 18 desmitdaļas."},
        {"jaut": "Ko pārbaude pamana vispirms?",
         "opcijas": ["Nobīdītu komatu", "Skaistu pierakstu",
                     "Garu rēķinu", "Neko"],
         "pareizi": 0,
         "padoms": "Summa atšķiras desmitkārt."},
        {"jaut": "Kad pārbaudi var izlaist?",
         "opcijas": ["Nekad nav vērts to izlaist", "Ja rēķins bija īss",
                     "Ja atbilde ir apaļa", "Vienmēr"],
         "pareizi": 0,
         "padoms": "Pārbaude maksā dažas sekundes."},
    ], pamats=4),

    Pasaule("Vai čeks ir pareizs?",
            Ievadi("", [
                {"jaut": "Bija 10 €, iztērēti 3,45 €. Kasē teica, ka palika "
                         "6,55 €. Cik ir 6,55 + 3,45?",
                 "atb": ["10"], "padoms": "Saskaiti kolonnā."},
                {"jaut": "Vai atlikums bija pareizs? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "Summa sakrita."},
                {"jaut": "Bija 20 €, iztērēti 12,8 €. Teica, ka palika "
                         "8,2 €. Cik ir 8,2 + 12,8?",
                 "atb": ["21"], "padoms": "Saskaiti."},
                {"jaut": "Vai atlikums bija pareizs?",
                 "atb": ["nē", "ne"], "padoms": "Iznāca 21, nevis 20."},
            ]),
            pavediens="maja",
            konteksts="Atlikumu kasē pārbauda tieši tāpat - pieskaita "
                      "pirkuma summu un salīdzina ar iedoto naudu.",
            kapec="Viena saskaitīšana pasaka, vai skaitīts pareizi."),

    Kopsavilkums([
        "Pārbaudu starpību, pieskaitot tai atņēmēju.",
        "Salīdzinu iegūto summu ar mazināmo.",
        "Nosaucu trīs biežākās kļūdas ar decimāldaļām.",
        "Atrodu kļūdas vietu, ja pārbaude nesakrīt.",
    ]),

    Majas([
        "Izrēķini 7,2 - 3,85 un pārbaudi ar saskaitīšanu.",
        "Uzraksti kļūdainu atņemšanu un iedod to draugam pārbaudīt.",
        "Pieraksti trīs kļūdas, kuras pārbaude pamana.",
    ]),
]
