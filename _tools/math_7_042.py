# -*- coding: utf-8 -*-
"""7. klase, 42. stunda: «Kā sakarību pierakstīt ar formulu?»

Formula ir īsākais sakarības apraksts: tā vienā rindā pasaka to, ko tabula
rāda tikai dažiem skaitļiem. Stunda iemāca izvēlēties burtus lielumiem un
no vārdiem vai tabulas pāriet uz formulu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā sakarību pierakstīt ar formulu?"

MERKIS = ("Iemācīsimies pierakstīt sakarību starp lielumiem ar formulu, "
          "izvēloties burtus.")

SATURS = [
    Sakums("Straumēšanas abonements: 7 € mēnesī",
           zimejums=restis([["mēneši", "1", "2", "3", "n"],
                            ["€", "7", "14", "21", "?"]]),
           paraksts="Tabula beidzas, bet formula S = 7n der vienmēr.",
           fakti=["Tabulā redz tikai dažus mēnešus.",
                  "Formula strādā jebkuram mēnešu skaitam."]),

    Doma("Formula ir sakarība ar burtiem",
         "Formula ir vienādība, kas parāda, kā atkarīgo mainīgo aprēķina no "
         "neatkarīgā. Katram mainīgajam izvēlas burtu, kas atgādina tā "
         "nozīmi.",
         soli=[
             "Izvēlies burtus: n - skaits, t - laiks, S - summa, s - ceļš.",
             "Paskaties, ko dara ar neatkarīgo: reizina, pieskaita?",
             "Uzraksti: atkarīgais = izteiksme ar neatkarīgo.",
             "Pārbaudi ar vienu tabulas rindu.",
         ],
         pieze="Reizinājumu ar burtu raksta bez zīmes: 7 · n = 7n. Pirms "
               "burta vienmēr raksta skaitli."),

    Paraugs("No tabulas uz formulu",
            uzd="Kinoteātris: biļete 6 €, plus 1,50 € par rezervāciju "
                "visai grupai. Uzraksti formulu kopējai summai S grupai ar "
                "n cilvēkiem.",
            soli=[
                ("Par katru biļeti 6 €: 6n", "Reizina ar skaitu."),
                ("Viena rezervācija: + 1,5", "Pieskaita vienreiz."),
                ("S = 6n + 1,5", "Formula."),
                ("Pārbaude: n = 4, S = 24 + 1,5 = 25,5 (€)", "Ar vienu gadījumu."),
            ],
            atbilde="S = 6n + 1,5"),

    Varianti("Kura formula der?", [
        {"jaut": "Pildspalva maksā 0,8 €. Summa S par n pildspalvām.",
         "opcijas": ["S = 0,8n", "S = n + 0,8", "S = 0,8 : n", "n = 0,8S"],
         "pareizi": 0,
         "padoms": "Katra pildspalva - 0,8 €."},
        {"jaut": "Svece 20 cm, katru stundu sadeg 3 cm. Augstums h pēc t "
                 "stundām.",
         "opcijas": ["h = 20 − 3t", "h = 20 + 3t", "h = 3t", "h = 20t − 3"],
         "pareizi": 0,
         "padoms": "Augstums samazinās."},
        {"jaut": "Tabula: x = 1, 2, 3; y = 5, 8, 11.",
         "opcijas": ["y = 3x + 2", "y = 5x", "y = x + 4", "y = 2x + 3"],
         "pareizi": 0,
         "padoms": "Katru reizi +3; pārbaudi x = 1."},
        {"jaut": "Taisnstūrim ar malām a un 5 cm - perimetrs P.",
         "opcijas": ["P = 2a + 10", "P = 5a", "P = a + 5", "P = 2a + 5"],
         "pareizi": 0,
         "padoms": "P = 2(a + 5)."},
    ], pamats=4),

    Ievadi("Aprēķini pēc formulas", [
        {"jaut": "S = 6n + 1,5. Cik € maksā 10 biļetes?",
         "atb": ["61,5"], "padoms": "60 + 1,5."},
        {"jaut": "h = 20 − 3t. Cik cm pēc 4 h?",
         "atb": ["8"], "padoms": "20 − 12."},
        {"jaut": "y = 3x + 2. Cik ir y, ja x = 7?",
         "atb": ["23"], "padoms": "21 + 2."},
        {"jaut": "S = 7n. Cik mēnešus var abonēt par 84 €?",
         "atb": ["12"], "padoms": "84 : 7."},
    ]),

    Pasaule("Sporta klubs",
            Ievadi("", [
                {"jaut": "Klubs: iestāšanās 15 €, katrs treniņš 4 €. "
                         "Uzraksti summu S par n treniņiem - cik € par 10?",
                 "atb": ["55"], "padoms": "S = 4n + 15."},
                {"jaut": "Mēneša abonements 40 € par neierobežotu skaitu. "
                         "Cik treniņu ar pirmo tarifu maksā tikpat (bez "
                         "iestāšanās maksas)?",
                 "atb": ["10"], "padoms": "40 : 4."},
                {"jaut": "Ar 75 € (ieskaitot iestāšanās maksu) - cik "
                         "treniņu?",
                 "atb": ["15"], "padoms": "(75 − 15) : 4."},
            ]),
            pavediens="sports",
            konteksts="Sporta klubi piedāvā tarifus, ko var salīdzināt tikai "
                      "ar formulu.",
            kapec="Formula ļauj aprēķināt jebkuram treniņu skaitam."),

    Zimejums("Formula un tabula",
             restis([["n", "0", "5", "10", "20"],
                     ["S = 4n + 15", "15", "35", "55", "95"]]),
             paskaidro="Katra tabulas rinda ir formula ar konkrētu n."),

    Kopsavilkums([
        "Izvēlos burtus, kas atgādina lielumu nozīmi.",
        "Pierakstu sakarību ar formulu.",
        "Pārbaudu formulu ar tabulas rindu.",
        "Aprēķinu pēc formulas abos virzienos.",
    ]),

    Majas([
        "Uzraksti formulu savam telefona tarifam.",
        "Izveido tabulu un formulu: kabatas nauda, ja krāj 5 € nedēļā.",
        "Izdomā formulu ar samazinājumu (piemēram, sveci).",
    ]),
]
