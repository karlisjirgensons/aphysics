# -*- coding: utf-8 -*-
"""6. klase, 137. stunda: «Kā saskaitīt ļoti daudz saskaitāmo?»

Stunda par ideju, ne par rēķinu. Simts saskaitāmo nav jāsaskaita pa vienam -
tos var sagrupēt pāros. Šī ir viena no tām idejām, kas paliek atmiņā ilgāk
nekā jebkurš algoritms.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā saskaitīt ļoti daudz saskaitāmo?"

MERKIS = ("Aprēķināsim summu, kas veidota pēc likumsakarības, sadalot "
          "problēmu daļās.")

SATURS = [
    Sakums("Simts saskaitāmo vienā minūtē",
           zimejums=restis([["−5", "+5", "−4", "+4", "−3", "+3"],
                            ["0", "", "0", "", "0", ""]]),
           paraksts="Katrs pāris dod nulli. Tāpēc visa rinda ir nulle, "
                    "neatkarīgi no tā, cik gara tā ir.",
           fakti=["Garā summā meklē likumsakarību, nevis rēķini pa vienam.",
                  "Pretēju skaitļu pāri dod nulli.",
                  "Ja pāru nav, meklē vienādas summas."]),

    Doma("Sadali summu pāros",
         "Summu, kas veidota pēc likuma, aprēķina, sadalot to pāros vai "
         "grupās ar vienādu summu, un tad saskaita grupas.",
         soli=[
             "Pieraksti dažus pirmos un pēdējos saskaitāmos.",
             "Paskaties, vai tie veido pretēju skaitļu pārus.",
             "Ja veido, saskaiti pārus - katrs dod nulli.",
             "Ja neveido, pārbaudi, vai pāru summas ir vienādas.",
             "Reizini vienas grupas summu ar grupu skaitu.",
         ],
         pieze="Summai no −5 līdz 5 visi skaitļi veido pārus, tāpēc atbilde "
               "ir nulle. Summai no 1 līdz 10 pāri ir 1 + 10, 2 + 9 un tā "
               "tālāk - katrs dod 11, un pāru ir pieci."),

    Paraugs("Divas dažādas summas",
            uzd="Cik ir −5 + (−4) + ... + 4 + 5 un cik ir 1 + 2 + ... + 10?",
            soli=[
                ("Pirmajā summā katram skaitlim ir pretējais",
                 "−5 un 5, −4 un 4 un tā tālāk."),
                ("Visi pāri dod nulli; nulle pati ir vidū",
                 "Atbilde: 0."),
                ("Otrajā: 1 + 10 = 11; 2 + 9 = 11 un tā tālāk",
                 "Katrs pāris dod 11."),
                ("Pāru ir 5, tātad 5 · 11 = 55",
                 "Atbilde: 55."),
            ],
            atbilde="0 un 55"),

    Ievadi("Saskaiti pēc likuma", [
        {"jaut": "Cik ir −5 + (−4) + (−3) + ... + 4 + 5?",
         "atb": ["0"], "padoms": "Visi pāri izsvītrojas."},
        {"jaut": "Cik ir 1 + 2 + 3 + ... + 10?",
         "atb": ["55"], "padoms": "5 pāri pa 11."},
        {"jaut": "Cik ir −10 + (−9) + ... + 9 + 10?",
         "atb": ["0"], "padoms": "Simetriska summa."},
        {"jaut": "Cik ir 1 + 2 + ... + 20?",
         "atb": ["210"], "padoms": "10 pāri pa 21."},
        {"jaut": "Cik ir −3 + (−2) + (−1) + 0 + 1 + 2 + 3 + 4?",
         "atb": ["4"], "padoms": "Viss līdz 3 izsvītrojas."},
        {"jaut": "Cik pāru ir summā no 1 līdz 100?",
         "atb": ["50"], "padoms": "100 : 2."},
    ], pamats=4),

    Petijums("Saskaiti simts skaitļus",
             vajag="burtnīca",
             soli=[
                 "Pieraksti summu 1 + 2 + 3 + ... + 100.",
                 "Savieno pirmo ar pēdējo, otro ar priekšpēdējo.",
                 "Aprēķini vienu pāra summu.",
                 "Saskaiti, cik pāru ir kopā.",
                 "Sareizini abus skaitļus.",
             ],
             secinajums="Katrs pāris dod 101, un pāru ir 50 - tātad summa ir "
                        "5050. Pa vienam skaitot, tas prasītu stundu."),

    Varianti("Kā sagrupēt?", [
        {"jaut": "Summā no −7 līdz 7 atbilde ir...",
         "opcijas": ["0", "7", "−7", "49"],
         "pareizi": 0,
         "padoms": "Visi skaitļi veido pārus."},
        {"jaut": "Summā no 1 līdz 10 katrs pāris dod...",
         "opcijas": ["11", "10", "5", "55"],
         "pareizi": 0,
         "padoms": "1 + 10."},
        {"jaut": "Cik pāru ir summā no 1 līdz 10?",
         "opcijas": ["5", "10", "11", "2"],
         "pareizi": 0,
         "padoms": "10 : 2."},
        {"jaut": "Kāpēc summa no −n līdz n ir nulle?",
         "opcijas": ["Jo katram skaitlim ir pretējais",
                     "Jo skaitļu ir daudz",
                     "Jo tur ir nulle", "Tā nav nulle"],
         "pareizi": 0,
         "padoms": "Pretēju skaitļu summa."},
    ], pamats=4),

    Pasaule("Cik soļu kopā?",
            Ievadi("", [
                {"jaut": "Robots iet 1 + 2 + 3 + ... + 10 soļus. Cik soļu "
                         "kopā?",
                 "atb": ["55"], "padoms": "5 pāri pa 11."},
                {"jaut": "Cits robots iet −5; −4; ...; 4; 5 soļus. Kur tas "
                         "nonāk?",
                 "atb": ["0"], "padoms": "Visi pāri izsvītrojas."},
                {"jaut": "Trešais iet 1 + 2 + ... + 20 soļus. Cik soļu?",
                 "atb": ["210"], "padoms": "10 pāri pa 21."},
                {"jaut": "Par cik soļiem trešais pārspēj pirmo?",
                 "atb": ["155"], "padoms": "210 − 55."},
            ]),
            pavediens="tehnika",
            konteksts="Robota programmā soļu skaits aug pēc likuma - un "
                      "kopējo ceļu var izrēķināt, to nemaz nepalaižot.",
            kapec="Likumsakarība ļauj aizstāt simts darbības ar divām."),

    Zimejums("Pāri summā no 1 līdz 10",
             restis([["1", "2", "3", "4", "5"],
                     ["10", "9", "8", "7", "6"],
                     ["11", "11", "11", "11", "11"]]),
             paskaidro="Piecas kolonnas, katra dod 11. Kopā 5 · 11 = 55.",
             ievads="Tā izskatās summa, sadalīta pāros."),

    Kopsavilkums([
        "Aprēķinu summu, kas veidota pēc likumsakarības.",
        "Sadalu summu pāros ar vienādu summu.",
        "Atpazīstu pretēju skaitļu pārus, kas dod nulli.",
        "Reizinu vienas grupas summu ar grupu skaitu.",
    ]),

    Majas([
        "Aprēķini summu no 1 līdz 30.",
        "Aprēķini summu no −20 līdz 20.",
        "Pieraksti, cik pāru bija katrā gadījumā.",
    ]),
]
