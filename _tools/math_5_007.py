# -*- coding: utf-8 -*-
"""5. klase, 7. stunda: «Kā skaitli uzrakstīt ar diviem simboliem?»

Jauns mikrotemats. Binārais pieraksts te nav pašmērķis - tas parāda, ka
vietas nozīme (1. stunda) ir vispārīgs princips, nevis desmitnieku īpašība.
Skolēnam nav jāprot pārvērst lielus skaitļus; pietiek saprast domu un
uzrakstīt nākamos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, biti)

TEMA = "Kā skaitli uzrakstīt ar diviem simboliem?"

MERKIS = ("Iepazīsim bināro pierakstu un sapratīsim, kā ar diviem cipariem "
          "var uzrakstīt jebkuru skaitli.")

SATURS = [
    Sakums("Kā ar astoņiem slēdžiem uzrakstīt jebkuru burtu?",
           zimejums=biti("01001010"),
           paraksts="Astoņi slēdži - viens baits. Tieši tā dators glabā "
                    "burtu «J».",
           fakti=["Datorā nav desmit ciparu - ir tikai ieslēgts un izslēgts.",
                  "Ar 8 slēdžiem sanāk 256 dažādas kombinācijas."]),

    Doma("Katra nākamā vieta ir divreiz lielāka",
         "Decimālajā pierakstā vietas ir 1, 10, 100; binārajā - 1, 2, 4, 8, "
         "16.",
         soli=[
             "Uzraksti vietu vērtības no labās: 1, 2, 4, 8, 16.",
             "Zem katras vietas liec 1, ja to ņem, vai 0, ja neņem.",
             "Saskaiti tās vietas, kur ir 1 - sanāk parastais skaitlis.",
         ],
         pieze="Binārajā pierakstā nav cipara 2: divi vieni pārvēršas par "
               "vienu nākamajā vietā, tāpat kā desmit vieni pārvēršas par "
               "vienu desmitu."),

    Paraugs("Ko nozīmē 1011?",
            uzd="Pārvērs bināro skaitli 1011 parastajā pierakstā.",
            soli=[
                ("Vietas: 8, 4, 2, 1",
                 "Uzraksta vietu vērtības no labās uz kreiso."),
                ("1 · 8 + 0 · 4 + 1 · 2 + 1 · 1",
                 "Katru ciparu reizina ar savas vietas vērtību."),
                ("8 + 2 + 1 = 11",
                 "Saskaita tikai tās vietas, kur bija 1."),
            ],
            atbilde="1011 binārajā pierakstā ir 11"),

    Ievadi("Pārvērs parastajā pierakstā", [
        {"jaut": "Binārais 10 - kāds tas ir parastais skaitlis?",
         "atb": ["2"], "padoms": "Vietas ir 2 un 1."},
        {"jaut": "Binārais 100 - kāds skaitlis?", "atb": ["4"],
         "padoms": "Vietas ir 4, 2, 1."},
        {"jaut": "Binārais 111 - kāds skaitlis?", "atb": ["7"],
         "padoms": "4 + 2 + 1."},
        {"jaut": "Binārais 1000 - kāds skaitlis?", "atb": ["8"],
         "padoms": "Nākamā vieta aiz 4 ir 8."},
        {"jaut": "Binārais 1010 - kāds skaitlis?", "atb": ["10"],
         "padoms": "8 + 2."},
        {"jaut": "Binārais 1111 - kāds skaitlis?", "atb": ["15"],
         "padoms": "8 + 4 + 2 + 1."},
    ], pamats=4,
        ievads="Vietu vērtības no labās: 1, 2, 4, 8, 16."),

    Ievadi("Uzraksti binārajā pierakstā", [
        {"jaut": "Kā binārajā pierakstā uzraksta 3?", "atb": ["11"],
         "padoms": "2 + 1.", "tastatura": "numeric"},
        {"jaut": "Kā binārajā pierakstā uzraksta 5?", "atb": ["101"],
         "padoms": "4 + 1 - divnieka vietu neņem."},
        {"jaut": "Kā binārajā pierakstā uzraksta 6?", "atb": ["110"],
         "padoms": "4 + 2."},
        {"jaut": "Kā binārajā pierakstā uzraksta 9?", "atb": ["1001"],
         "padoms": "8 + 1."},
    ], ievads="Ieraksti atbildi ar nullēm un vieniniekiem."),

    Varianti("Kas notiek tālāk?", [
        {"jaut": "Binārajā skaitīšanā pēc 1 nāk...",
         "opcijas": ["10", "2", "11", "01"],
         "pareizi": 0,
         "padoms": "Cipara 2 binārajā pierakstā nav."},
        {"jaut": "Cik dažādus skaitļus var uzrakstīt ar 3 binārajām vietām?",
         "opcijas": ["8", "3", "6", "9"],
         "pareizi": 0,
         "padoms": "No 000 līdz 111."},
        {"jaut": "Kurš binārais skaitlis ir lielākais?",
         "opcijas": ["1100", "1011", "111", "1001"],
         "pareizi": 0,
         "padoms": "Pārvērs visus parastajā pierakstā."},
        {"jaut": "Kāpēc binārajā pierakstā skaitļi ir gari?",
         "opcijas": ["Katra vieta dod tikai divreiz vairāk",
                     "Tāpēc, ka dators ir lēns",
                     "Tāpēc, ka trūkst cipara 0",
                     "Tāpēc, ka vietas skaita no kreisās"],
         "pareizi": 0,
         "padoms": "Desmitniekos katra vieta dod desmitreiz vairāk."},
    ], pamats=4),

    Zimejums("Viens un tas pats skaitlis, divi pieraksti",
             biti("1101"),
             paskaidro="Ieslēgtie slēdži ir 8, 4 un 1. Kopā sanāk 13.",
             ievads="Slēdžu rinda pati izstāsta, kāpēc iznāk tieši šis "
                    "skaitlis."),

    Pasaule("Cik attēlu ietilpst atmiņā?",
            Ievadi("", [
                {"jaut": "Cik bitu ir vienā baitā?", "atb": ["8"],
                 "padoms": "Astoņi slēdži."},
                {"jaut": "Cik dažādu vērtību var uzrakstīt ar 4 bitiem?",
                 "atb": ["16"], "padoms": "No 0000 līdz 1111."},
                {"jaut": "Attēls aizņem 2 MB. Cik tādu ietilpst 100 MB?",
                 "atb": ["50"], "padoms": "100 : 2."},
                {"jaut": "Cik dažādu vērtību var uzrakstīt ar 8 bitiem?",
                 "atb": ["256"], "padoms": "Katrs bits dubulto: 2, 4, 8, 16 "
                                           "un tā tālāk."},
            ]),
            pavediens="dati",
            konteksts="Viens burts aizņem vienu baitu; viena fotogrāfija - "
                      "vairākus miljonus baitu.",
            kapec="Tāpēc telefona atmiņu mēra megabaitos un gigabaitos, "
                  "nevis burtos."),

    Kopsavilkums([
        "Zinu, ka binārajā pierakstā ir tikai cipari 0 un 1.",
        "Pārvēršu īsu bināro skaitli parastajā pierakstā.",
        "Saprotu, ka vietas nozīme darbojas jebkurā pieraksta sistēmā.",
    ]),

    Majas([
        "Uzraksti binārajā pierakstā skaitļus no 1 līdz 8 un paskaties, kā "
        "tie aug.",
        "Uzzini, cik bitu ir vienā baitā, un padomā, cik dažādu skaitļu tas "
        "ļauj uzrakstīt.",
        "Pamēģini ar pirkstiem parādīt skaitli 10 binārajā pierakstā: pirksts "
        "uz augšu ir 1.",
    ]),
]
