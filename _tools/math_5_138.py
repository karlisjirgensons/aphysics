# -*- coding: utf-8 -*-
"""5. klase, 138. stunda: «Kā saskaitīt rakstos?»

Galvā rēķināt vairs nepietiek, kad skaitļi kļūst gari. Kolonna decimāldaļām
ir tā pati, kas veseliem skaitļiem, ar vienu papildu noteikumu: komats zem
komata. Ja tas ir ievērots, tad vienas šķiras cipari paši sastājas vienā
kolonnā, un tālāk viss notiek kā 4. klasē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā saskaitīt rakstos?"

MERKIS = ("Iemācīsimies saskaitīt decimāldaļas, rakstot vienas šķiras ciparus "
          "vienu zem otra.")

SATURS = [
    Sakums("Komats zem komata",
           zimejums=restis([["3", ",", "4", "5"],
                            ["1", ",", "2", "0"]],
                           virsraksts="Viens skaitlis zem otra"),
           paraksts="3,45 + 1,2 = 4,65 - ja komats stāv zem komata.",
           fakti=["Kolonnā raksta vienas šķiras ciparus vienu zem otra.",
                  "Komats stāv zem komata.",
                  "Trūkstošās vietas aizpilda ar nullēm."]),

    Doma("Vienas šķiras cipari vienā kolonnā",
         "Decimāldaļas saskaita kolonnā: komatu raksta zem komata, un tad "
         "vienas šķiras cipari paši nostājas viens zem otra.",
         soli=[
             "Uzraksti pirmo skaitli.",
             "Otro raksti zem tā tā, lai komats būtu zem komata.",
             "Tukšās vietas aizpildi ar nullēm.",
             "Saskaiti pa kolonnām no labās uz kreiso.",
             "Atbildē komatu liec zem komata.",
         ],
         pieze="Nulles aiz komata te nav rotājums: 1,2 = 1,20, un tikai tad "
               "simtdaļu kolonnā ir kas saskaitāms. Bez tām viegli sajaukt "
               "šķiras."),

    Paraugs("3,45 + 1,2",
            uzd="Saskaiti kolonnā.",
            soli=[
                ("1,2 = 1,20",
                 "Izlīdzina ciparu skaitu."),
                ("Komats zem komata",
                 "Šķiras sastājas vienā kolonnā."),
                ("5 + 0 = 5 simtdaļas",
                 "Labā kolonna."),
                ("4 + 2 = 6 desmitdaļas",
                 "Nākamā kolonna."),
                ("3 + 1 = 4 veselie; atbilde 4,65",
                 "Komats paliek savā vietā."),
            ],
            atbilde="3,45 + 1,2 = 4,65"),

    Ievadi("Saskaiti rakstos", [
        {"jaut": "3,45 + 1,2 = ? Ieraksti skaitli.",
         "atb": ["4,65"], "padoms": "1,2 = 1,20."},
        {"jaut": "2,7 + 1,45 = ?",
         "atb": ["4,15"], "padoms": "2,70 + 1,45."},
        {"jaut": "5,06 + 2,4 = ?",
         "atb": ["7,46"], "padoms": "2,4 = 2,40."},
        {"jaut": "12,5 + 3,75 = ?",
         "atb": ["16,25"], "padoms": "12,50 + 3,75."},
        {"jaut": "0,8 + 0,35 = ?",
         "atb": ["1,15"], "padoms": "0,80 + 0,35."},
        {"jaut": "4,9 + 5,1 = ?",
         "atb": ["10"], "padoms": "10 desmitdaļas ir vesels."},
        {"jaut": "7,25 + 0,75 = ?",
         "atb": ["8"], "padoms": "100 simtdaļas ir vesels."},
        {"jaut": "1,05 + 2,95 = ?",
         "atb": ["4"], "padoms": "Simtdaļas dod veselu."},
    ], pamats=4,
        ievads="Vispirms izlīdzini ciparu skaitu, tad raksti kolonnā."),

    Zimejums("Kolonna ar izlīdzinātiem cipariem",
             restis([["3", ",", "4", "5"],
                     ["1", ",", "2", "0"],
                     ["4", ",", "6", "5"]],
                    virsraksts="Summa apakšējā rindā"),
             paskaidro="Katra kolonna ir viena šķira: simtdaļas, desmitdaļas, "
                       "veselie. Komats visās rindās ir vienā vietā.",
             ievads="Tā izskatās pareizi uzrakstīta kolonna."),

    Varianti("Kur rodas kļūda?", [
        {"jaut": "Kā raksta skaitļus kolonnā?",
         "opcijas": ["Komats zem komata", "Pa labi izlīdzinot",
                     "Pa kreisi izlīdzinot", "Kā sanāk"],
         "pareizi": 0,
         "padoms": "Tad šķiras sakrīt."},
        {"jaut": "Skolēns raksta 3,45 + 1,2 un izlīdzina pa labi. Kas notiks?",
         "opcijas": ["Saskaitīs dažādas šķiras", "Nekas",
                     "Atbilde būs lielāka", "Komats pazudīs"],
         "pareizi": 0,
         "padoms": "2 nonāks zem 5."},
        {"jaut": "Kā aizpilda tukšās vietas aiz komata?",
         "opcijas": ["Ar nullēm", "Ar atstarpēm", "Ar punktiem",
                     "Neaizpilda"],
         "pareizi": 0,
         "padoms": "1,2 = 1,20."},
        {"jaut": "2,7 + 1,45 ir...",
         "opcijas": ["4,15", "3,52", "4,52", "1,72"],
         "pareizi": 0,
         "padoms": "2,70 + 1,45."},
        {"jaut": "Kur atbildē liek komatu?",
         "opcijas": ["Zem pārējiem komatiem", "Beigās",
                     "Pēc pirmā cipara", "Kur sanāk"],
         "pareizi": 0,
         "padoms": "Kolonna to nosaka."},
        {"jaut": "4,9 + 5,1 ir...",
         "opcijas": ["10", "9,10", "9,1", "10,10"],
         "pareizi": 0,
         "padoms": "10 desmitdaļas ir vesels."},
    ], pamats=4),

    Pasaule("Cik maksā viss pirkums?",
            Ievadi("", [
                {"jaut": "Maize 1,45 € un piens 1,2 €. Cik eiro kopā?",
                 "atb": ["2,65"], "padoms": "1,45 + 1,20."},
                {"jaut": "Siers 3,75 € un sula 1,25 €. Cik eiro kopā?",
                 "atb": ["5"], "padoms": "Simtdaļas dod veselu."},
                {"jaut": "Trīs preces: 2,5 €, 0,8 € un 1,45 €. Cik eiro "
                         "kopā?",
                 "atb": ["4,75"], "padoms": "2,50 + 0,80 + 1,45."},
                {"jaut": "Čeks 12,5 € un vēl 3,75 €. Cik eiro kopā?",
                 "atb": ["16,25"], "padoms": "12,50 + 3,75."},
            ]),
            pavediens="maja",
            konteksts="Čekā visas summas ir ar diviem cipariem aiz komata, "
                      "bet cenu zīmēs - ne vienmēr.",
            kapec="Kolonna ar komatu zem komata nekad nesajauc centus ar "
                  "eiro."),

    Kopsavilkums([
        "Rakstu decimāldaļas kolonnā ar komatu zem komata.",
        "Aizpildu tukšās vietas aiz komata ar nullēm.",
        "Saskaitu pa kolonnām no labās uz kreiso.",
        "Atbildē komatu lieku zem pārējiem komatiem.",
    ]),

    Majas([
        "Saskaiti kolonnā 6,35 + 2,8 un 14,7 + 3,45.",
        "Atrodi čeku un pārbaudi kopsummu ar kolonnu.",
        "Paskaidro, kāpēc komatam jābūt zem komata.",
    ]),
]
