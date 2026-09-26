# -*- coding: utf-8 -*-
"""7. klase, 8. stunda: «Kas ir pilnā pārlase?»

Pilnā pārlase nozīmē uzskaitīt visus gadījumus pēc kārtības, kas garantē,
ka neviens nav izlaists un neviens nav divreiz. Stundā to dara ar tabulu
un iespēju koku, un skaitu pārbauda ar reizināšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, koks, restis)

TEMA = "Kas ir pilnā pārlase?"

MERKIS = ("Iemācīsimies uzskaitīt visus iespējamos gadījumus un "
          "pārliecināties, ka neviens nav izlaists.")

SATURS = [
    Sakums("Cik tērpu var salikt no 3 kreklu un 2 bikšu?",
           zimejums=koks([["balts", "zils", "melns"], ["džinsi", "šorti"]],
                         atdalitajs=" + "),
           paraksts="Katram kreklam - divi zari: 3 · 2 = 6 tērpi.",
           fakti=["Nejauši minot, kāds tērps vienmēr pazūd.",
                  "Koks vai tabula ir kārtība, kurā nekas nepazūd."]),

    Doma("Kārtība garantē, ka nekas nav izlaists",
         "Pilnā pārlase ir visu gadījumu uzskaitīšana tādā kārtībā, lai "
         "katrs gadījums parādītos tieši vienu reizi.",
         soli=[
             "Nosaki, kādas izvēles jāizdara un kādā secībā.",
             "Nofiksē pirmo izvēli un pārlasi visas otrās.",
             "Tad nomaini pirmo izvēli un atkārto.",
             "Pārbaudi skaitu: izvēļu skaitu reizinājums.",
         ],
         pieze="Tabula der divām izvēlēm (rindas un kolonnas), koks - "
               "arī trim un vairāk."),

    Paraugs("Divciparu skaitļi no cipariem",
            uzd="Cik divciparu skaitļu var izveidot no cipariem 1, 2, 3, "
                "ja cipari drīkst atkārtoties?",
            soli=[
                ("Desmiti 1: 11, 12, 13", "Nofiksē pirmo ciparu."),
                ("Desmiti 2: 21, 22, 23", "Nomaina pirmo."),
                ("Desmiti 3: 31, 32, 33", "Un vēlreiz."),
                ("3 · 3 = 9", "Pārbaude ar reizināšanu."),
            ],
            atbilde="9 skaitļi"),

    Zimejums("Tie paši skaitļi tabulā",
             restis([["", "1", "2", "3"],
                     ["1", "11", "12", "13"],
                     ["2", "21", "22", "23"],
                     ["3", "31", "32", "33"]]),
             paskaidro="Rinda - desmiti, kolonna - vieni. Katra rūtiņa ir "
                       "viens gadījums."),

    Ievadi("Cik gadījumu?", [
        {"jaut": "Cik divciparu skaitļu var izveidot no cipariem 1, 2, 3, "
                 "ja cipari neatkārtojas?",
         "atb": ["6"], "padoms": "12, 13, 21, 23, 31, 32."},
        {"jaut": "Met divus kauliņus. Cik ir iespējamo iznākumu pāru?",
         "atb": ["36"], "padoms": "6 · 6."},
        {"jaut": "Met divus kauliņus. Cik pāros summa ir 7?",
         "atb": ["6"], "padoms": "1+6, 2+5, 3+4, 4+3, 5+2, 6+1."},
        {"jaut": "Met monētu trīs reizes. Cik iznākumu?",
         "atb": ["8"], "padoms": "2 · 2 · 2."},
        {"jaut": "Ēdnīcā 3 zupas, 4 otrie ēdieni, 2 deserti. Cik "
                 "dažādu pusdienu (pa vienam no katra)?",
         "atb": ["24"], "padoms": "3 · 4 · 2."},
        {"jaut": "Met divus kauliņus. Cik pāros abi skaitļi ir vienādi?",
         "atb": ["6"], "padoms": "1-1, 2-2, ..., 6-6."},
    ], pamats=4),

    Varianti("Kur kļūda pārlasē?", [
        {"jaut": "Marks uzskaitīja monētas divus metienus: ĢĢ, ĢC, CC. "
                 "Kas trūkst?",
         "opcijas": ["CĢ", "ĢĢĢ", "Nekas", "CC otrreiz"],
         "pareizi": 0,
         "padoms": "ĢC un CĢ ir dažādi: pirmā monēta ir cita."},
        {"jaut": "Kāpēc pārlasē nofiksē pirmo izvēli?",
         "opcijas": ["Lai visas otrās izvēles pārlasītu līdz galam",
                     "Lai būtu mazāk gadījumu",
                     "Lai izvēlētos labāko",
                     "Tā ir tikai tradīcija"],
         "pareizi": 0,
         "padoms": "Kārtība nozīmē - neko neizlaist."},
        {"jaut": "No 4 krekliem un 5 biksēm var salikt...",
         "opcijas": ["20 tērpus", "9 tērpus", "45 tērpus", "10 tērpus"],
         "pareizi": 0,
         "padoms": "4 · 5."},
    ]),

    Pasaule("Viedā slēdzene",
            Ievadi("", [
                {"jaut": "Velosipēda slēdzenei ir 3 ripiņas ar cipariem "
                         "0-9. Cik ir dažādu kodu?",
                 "atb": ["1000"], "padoms": "10 · 10 · 10."},
                {"jaut": "Zaglis pārbauda 1 kodu 2 sekundēs. Cik sekundēs "
                         "viņš noteikti atvērs slēdzeni?",
                 "atb": ["2000"], "padoms": "1000 · 2 s - nedaudz vairāk "
                                           "par pusstundu."},
                {"jaut": "Cik kodu būtu slēdzenei ar 4 ripiņām?",
                 "atb": ["10000"], "padoms": "Vēl viens reizinātājs 10."},
            ]),
            pavediens="kodi",
            konteksts="Pilnā pārlase ir arī tas, ko dara zaglis vai "
                      "dators, minot paroli.",
            kapec="Katra jauna ripiņa padara pārlasi 10 reižu garāku."),

    Kopsavilkums([
        "Uzskaitu visus gadījumus noteiktā kārtībā.",
        "Lietoju tabulu divām izvēlēm un koku - vairākām.",
        "Pārbaudu gadījumu skaitu ar reizināšanu.",
        "Atšķiru ĢC no CĢ, ja secība ir svarīga.",
    ]),

    Majas([
        "Uzskaiti visus tērpus no taviem 3 krekliem un 2 biksēm.",
        "Cik trīsciparu skaitļu var izveidot no 1, 2, 3 bez atkārtošanās?",
        "Uzzīmē koku trim monētas metieniem.",
    ]),
]
