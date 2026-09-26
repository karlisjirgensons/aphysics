# -*- coding: utf-8 -*-
"""4. klase, 94. stunda: «Kur uz skaitļu taisnes ir daļa?»

Daļa ir skaitlis, un tam ir sava vieta uz skaitļu taisnes. Nogriezni no 0
līdz 1 sadala saucēja skaitā vienādu daļu un no nulles atskaita
skaitītāja skaitu. Tā daļa pārstāj būt «picas gabals» un kļūst par punktu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, taisne)

TEMA = "Kur uz skaitļu taisnes ir daļa?"

MERKIS = ("Atliksim daļu uz dotas skaitļu taisnes un pamatosim tās vietu.")

SATURS = [
    Sakums("Kur uz lineāla ir {3|4} metra?",
           zimejums=taisne(0, 1, 1, [(0.75, "3/4")], sikas=4),
           paraksts="No 0 līdz 1 - četras vienādas daļas, trīs no tām.",
           fakti=["Daļa ir skaitlis starp veseliem skaitļiem.",
                  "{3|4} ir starp 0 un 1, tuvāk 1."]),

    Doma("Sadali vienu vienību saucēja daļās",
         "Lai atliktu {a|b}, nogriezni no 0 līdz 1 sadala b vienādās daļās "
         "un no 0 atskaita a daļas.",
         soli=[
             "Atrodi nogriezni no 0 līdz 1.",
             "Sadali to saucēja skaitā vienādu daļu.",
             "No 0 pa labi atskaiti skaitītāja skaitu iedaļu.",
             "Atzīmē punktu un uzraksti daļu.",
         ],
         pieze="{4|4} nonāk tieši pie 1 - četras ceturtdaļas ir viss."),

    Paraugs("Kur ir {2|5}?",
            uzd="Atliec {2|5} uz skaitļu taisnes.",
            soli=[
                ("0 līdz 1 → 5 daļas", "Saucējs 5."),
                ("2 iedaļas no 0", "Skaitītājs 2."),
            ],
            atbilde="otrajā iedaļā no piecām"),

    Kustiba("Aizved līdz daļai", [
        {"jaut": "Taisne no 0 līdz 1, sadalīta 10 daļās. Aizved līdz {7|10}. "
                 "Cik desmitdaļu jānobrauc?",
         "atb": 7, "beigas": 10, "iedala": 1, "mers": "desmitdaļas",
         "merkis": "7/10", "objekts": "Gliemezis",
         "padoms": "Skaitītājs 7.",
         "stasts": "Skala skaita desmitdaļas no 0 līdz 1."},
        {"jaut": "Tagad līdz {3|10}. Cik desmitdaļu?",
         "atb": 3, "beigas": 10, "iedala": 1, "mers": "desmitdaļas",
         "merkis": "3/10", "objekts": "Gliemezis", "padoms": "3."},
        {"jaut": "Līdz pusei - {5|10}. Cik desmitdaļu?",
         "atb": 5, "beigas": 10, "iedala": 1, "mers": "desmitdaļas",
         "merkis": "1/2", "objekts": "Gliemezis", "padoms": "Puse no 10."},
        {"jaut": "Līdz 1 - cik desmitdaļu?",
         "atb": 10, "beigas": 10, "iedala": 1, "mers": "desmitdaļas",
         "merkis": "1", "objekts": "Gliemezis", "padoms": "Visas."},
    ], pamats=2),

    Varianti("Kur ir daļa?", [
        {"jaut": "Taisne 0-1 sadalīta 4 daļās. Kurā iedaļā {1|4}?",
         "opcijas": ["pirmajā", "ceturtajā", "otrajā", "pie 1"],
         "pareizi": 0, "padoms": "Viena iedaļa no 0."},
        {"jaut": "Kura daļa ir tuvāk 1: {1|5} vai {4|5}?",
         "opcijas": ["{4|5}", "{1|5}", "vienādi"], "pareizi": 0,
         "padoms": "4 iedaļas no 5."},
        {"jaut": "Kurš punkts ir pusē starp 0 un 1?",
         "opcijas": ["{1|2}", "{1|3}", "{2|3}", "{1|4}"], "pareizi": 0,
         "padoms": "Puse."},
        {"jaut": "Cik iedaļās jāsadala 0-1, lai atliktu {5|6}?",
         "opcijas": ["6", "5", "11", "1"], "pareizi": 0,
         "padoms": "Saucējs."},
    ], pamats=4),

    Ievadi("Nolasi daļu", [
        {"jaut": "0-1 sadalīts 8 daļās, punkts 5. iedaļā. Kāda daļa?",
         "atb": ["5/8"], "vieta": "piem., 1/2", "padoms": "5 no 8."},
        {"jaut": "0-1 sadalīts 3 daļās, punkts 2. iedaļā.",
         "atb": ["2/3"], "vieta": "piem., 1/2", "padoms": "2 no 3."},
        {"jaut": "0-1 sadalīts 6 daļās, punkts 1. iedaļā.",
         "atb": ["1/6"], "vieta": "piem., 1/2", "padoms": "1 no 6."},
        {"jaut": "0-1 sadalīts 10 daļās, punkts 9. iedaļā.",
         "atb": ["9/10"], "vieta": "piem., 1/2", "padoms": "9 no 10."},
    ]),

    Pasaule("Maratona progress",
            Ievadi("", [
                {"jaut": "Trase sadalīta 10 vienādos posmos. Skrējējs "
                         "pabeidzis 4. Kāda daļa trases noskrieta?",
                 "atb": ["4/10"], "vieta": "piem., 1/2",
                 "padoms": "4 no 10."},
                {"jaut": "Cik posmu vēl atlicis?", "atb": ["6"],
                 "padoms": "10 − 4."},
                {"jaut": "Kāda daļa trases vēl atlikusi?", "atb": ["6/10"],
                 "vieta": "piem., 1/2", "padoms": "6 no 10."},
                {"jaut": "Pēc cik posmiem skrējējs būs pusē?", "atb": ["5"],
                 "padoms": "{5|10} = puse."},
            ]),
            pavediens="sports",
            konteksts="Sporta pulksteņi rāda progresa joslu - tā ir skaitļu "
                      "taisne no 0 līdz 1.",
            kapec="Daļa uz taisnes parāda, cik tālu esi no mērķa."),

    Kopsavilkums([
        "Atlieku daļu uz skaitļu taisnes.",
        "Sadalu nogriezni no 0 līdz 1 saucēja skaitā daļu.",
        "Nolasu daļu no taisnes.",
    ]),

    Majas([
        "Uzzīmē taisni 0-1 ar 12 rūtiņām un atliec {1|4}, {1|3}, {5|6}.",
        "Pavēro progresa joslu telefonā vai datorā: kāda daļa pabeigta?",
        "Paskaidro, kāpēc {4|4} ir tieši pie 1.",
    ]),
]
