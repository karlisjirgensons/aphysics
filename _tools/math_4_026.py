# -*- coding: utf-8 -*-
"""4. klase, 26. stunda: «Kas mainās, ja rodas jauns desmits?»

Pāreja citā šķirā reizinot: 27 · 3 - vienos sanāk 21, un divi desmiti
pievienojas desmitiem. Metode paliek tā pati (pa daļām), tikai
starprezultātu saskaitīšanā parādās pārnesums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kas mainās, ja rodas jauns desmits?"

MERKIS = ("Reizināsim ar pāreju citā šķirā un pastāstīsim, kā rīkojāmies.")

SATURS = [
    Sakums("Cik olu 6 kastītēs pa 15?",
           zimejums=restis([["", "desmiti", "vieni"],
                            ["15 · 6", "10 · 6 = 60", "5 · 6 = 30"]],
                           "vienos sanāk vairāk par 9"),
           paraksts="5 · 6 = 30 - tie ir 3 jauni desmiti.",
           fakti=["Vienos sanāk 30 - tas vairs nav viens cipars.",
                  "Jaunie desmiti pievienojas pārējiem desmitiem."]),

    Doma("Metode tā pati - tikai starprezultāti lielāki",
         "Sadali, reizini katru daļu un saskaiti; ja vienos sanāk desmiti, "
         "tie pievienojas desmitiem.",
         soli=[
             "27 · 3: desmiti 20 · 3 = 60.",
             "Vieni 7 · 3 = 21 - tie ir 2 desmiti un 1 viens.",
             "Saskaiti: 60 + 21 = 81.",
             "Pārbaudi aptuveni: 27 ≈ 30, 30 · 3 = 90 - tuvu.",
         ],
         pieze="Jauns desmits nav kļūda - tas ir iemesls, kāpēc starprezultātu "
               "saskaitīšanai jābūt rūpīgai."),

    Paraugs("48 · 4",
            uzd="Izrēķini 48 · 4.",
            soli=[
                ("40 · 4 = 160", "Desmiti - sanāk pat simti."),
                ("8 · 4 = 32", "Vieni - 3 jauni desmiti."),
                ("160 + 32 = 192", None),
            ],
            atbilde="192"),

    Slidnis("Kā aug 17 · 6",
            soli=[
                {"v": "17 · 6", "teksts": "Sadalām 17 = 10 + 7."},
                {"v": "10 · 6 = 60", "teksts": "Desmiti.", "josla": 59},
                {"v": "7 · 6 = 42", "teksts": "Vieni - 4 jauni desmiti!",
                 "josla": 100},
                {"v": "60 + 42 = 102", "teksts": "Pavisam - pat pāri simtam."},
            ],
            ievads="Skaties, cik liela daļa nāk no vieniem."),

    Ievadi("Ar pāreju", [
        {"jaut": "27 · 3 = ?", "atb": ["81"], "padoms": "60 + 21."},
        {"jaut": "16 · 5 = ?", "atb": ["80"], "padoms": "50 + 30."},
        {"jaut": "35 · 4 = ?", "atb": ["140"], "padoms": "120 + 20."},
        {"jaut": "29 · 2 = ?", "atb": ["58"], "padoms": "40 + 18."},
        {"jaut": "18 · 7 = ?", "atb": ["126"], "padoms": "70 + 56."},
        {"jaut": "56 · 3 = ?", "atb": ["168"], "padoms": "150 + 18."},
        {"jaut": "74 · 6 = ?", "atb": ["444"], "padoms": "420 + 24."},
        {"jaut": "99 · 9 = ?", "atb": ["891"], "padoms": "810 + 81."},
    ], pamats=6),

    Varianti("Kur kļūda?", [
        {"jaut": "Mārtiņš: 26 · 3 = 68. Kas nav kārtībā?",
         "opcijas": ["18 no vieniem pierakstīja kā 8",
                     "sajauca reizināšanu ar saskaitīšanu",
                     "viss pareizi"], "pareizi": 0,
         "padoms": "60 + 18 = 78."},
        {"jaut": "Līga: 45 · 2 = 810. Kas nav kārtībā?",
         "opcijas": ["salika 80 un 10 blakus, nevis saskaitīja",
                     "sareizināja nepareizi", "viss pareizi"], "pareizi": 0,
         "padoms": "80 + 10 = 90."},
        {"jaut": "Cik ir 19 · 5?",
         "opcijas": ["95", "55", "59", "90"], "pareizi": 0,
         "padoms": "50 + 45."},
    ]),

    Pasaule("Virtuvē: cepumi skolas tirdziņam",
            Ievadi("", [
                {"jaut": "Vienai cepumu porcijai vajag 15 g sviesta. Cik "
                         "gramu 6 porcijām?",
                 "atb": ["90"], "padoms": "60 + 30."},
                {"jaut": "Uz vienas pannas 24 cepumi. Cik cepumu 4 pannās?",
                 "atb": ["96"], "padoms": "80 + 16."},
                {"jaut": "Vienam cepumam 7 šokolādes gabaliņi. Cik gabaliņu "
                         "vajag 36 cepumiem?",
                 "atb": ["252"], "padoms": "36 · 7 = 210 + 42."},
                {"jaut": "Maisiņā 8 cepumi. Cik cepumu 45 maisiņos?",
                 "atb": ["360"], "padoms": "45 · 8 = 320 + 40."},
            ]),
            pavediens="virtuve",
            konteksts="Recepti pavairojot, katra sastāvdaļa jāreizina - un "
                      "tur rodas jauni desmiti.",
            kapec="Kas nepārnes desmitu, tam pietrūks sviesta."),

    Kopsavilkums([
        "Reizinu ar pāreju citā šķirā.",
        "Saskaitu starprezultātus rūpīgi.",
        "Pārbaudu reizinājumu ar aptuveno vērtību.",
        "Pastāstu, kā rīkojos.",
    ]),

    Majas([
        "Atrodi recepti un izrēķini sastāvdaļas trīskāršai porcijai.",
        "Izrēķini 25 · 4 un 25 · 8 - ko pamani?",
        "Paskaidro mājiniekam, no kurienes rodas jauns desmits.",
    ]),
]
