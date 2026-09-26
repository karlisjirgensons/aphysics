# -*- coding: utf-8 -*-
"""7. klase, 27. stunda: «Kā uzzīmēt vienādu figūru?»

Rūtiņu lapā vienādu figūru var uzzīmēt precīzi: katru virsotni pārnes ar
to pašu «soli» - tik rūtiņu pa labi un tik uz augšu. Pagriešana par 90°
maina soļus vietām. Stundā zīmē un pārbauda ar koordinātu soļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, figura, plakne)

TEMA = "Kā uzzīmēt vienādu figūru?"

MERKIS = ("Zīmēsim rūtiņu lapā figūru, kas vienāda ar doto, pēc dotiem "
          "nosacījumiem.")

SATURS = [
    Sakums("Pikseļu māksla: tas pats zīmējums citā vietā",
           zimejums=plakne(lauzta=[(1, 1), (4, 1), (4, 3), (1, 1)],
                           punkti=[(1, 1, "A"), (4, 1, "B"), (4, 3, "C")],
                           no_x=0, lidz_x=8, no_y=0, lidz_y=5),
           paraksts="Katru virsotni pārvieto par tik pašām rūtiņām.",
           fakti=["Spēlēs tēls pārvietojas, katru pikseli nobīdot vienādi.",
                  "Ja visas virsotnes bīda vienādi - figūra paliek vienāda."]),

    Doma("Katru virsotni pārvieto vienādi",
         "Lai uzzīmētu vienādu figūru, katru virsotni pārnes ar to pašu "
         "pārvietojumu. Pārbīdot visu figūru par a rūtiņām pa labi un b "
         "rūtiņām uz augšu, iegūst vienādu figūru.",
         soli=[
             "Nolasi katras virsotnes koordinātas (x; y).",
             "Pieskaiti visām vienu un to pašu nobīdi.",
             "Atzīmē jaunās virsotnes un savieno tās tajā pašā secībā.",
             "Pārbaudi: malu soļi (cik pa labi, cik uz augšu) ir tādi paši.",
         ],
         pieze="Pagriežot par 90°, mala «3 pa labi, 2 uz augšu» kļūst par "
               "«2 pa kreisi, 3 uz augšu» - garums nemainās."),

    Paraugs("Pārbīdi trijstūri",
            uzd="Trijstūris A(1; 1), B(4; 1), C(4; 3). Uzzīmē vienādu "
                "trijstūri, pārbīdot to par 3 rūtiņām pa labi un 1 uz augšu.",
            soli=[
                ("A′(1 + 3; 1 + 1) = A′(4; 2)", "Pieskaita nobīdi."),
                ("B′(7; 2), C′(7; 4)", "Tāpat pārējās."),
                ("A′B′ = 3 rūtiņas, B′C′ = 2 rūtiņas",
                 "Tādas pašas kā AB un BC."),
            ],
            atbilde="A′(4; 2), B′(7; 2), C′(7; 4)"),

    Zimejums("Oriģināls un kopija",
             plakne(grafiki=[([(1, 1), (4, 1), (4, 3), (1, 1)], ""),
                             ([(4, 2), (7, 2), (7, 4), (4, 2)], "")],
                    punkti=[(1, 1, "A"), (4, 1, "B"), (4, 3, "C"),
                            (4, 2, "A′"), (7, 2, "B′"), (7, 4, "C′")],
                    no_x=0, lidz_x=8, no_y=0, lidz_y=5),
             paskaidro="△A′B′C′ = △ABC - tikai citā vietā."),

    Ievadi("Aprēķini jaunās koordinātas", [
        {"jaut": "Punktu (2; 5) pārbīda par 4 pa labi. Kāda ir jaunā x "
                 "koordināta?",
         "atb": ["6"], "padoms": "2 + 4."},
        {"jaut": "Punktu (2; 5) pārbīda par 3 uz leju. Kāda ir jaunā y "
                 "koordināta?",
         "atb": ["2"], "padoms": "5 − 3."},
        {"jaut": "Nogrieznis no (0; 0) līdz (3; 4) ir 5 rūtiņas garš. "
                 "Pārbīdīts par (2; 2), cik garš tas ir?",
         "atb": ["5"], "padoms": "Pārbīde garumu nemaina."},
        {"jaut": "Kvadrātu ar virsotni (1; 1) un malu 3 pārbīda. Kāds ir "
                 "jaunā kvadrāta laukums?",
         "atb": ["9"], "padoms": "3 · 3."},
    ]),

    Varianti("Vai figūra būs vienāda?", [
        {"jaut": "Visām virsotnēm pieskaita 2 pie x un 5 pie y.",
         "opcijas": ["Vienāda", "Nav vienāda", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Vienāda nobīde."},
        {"jaut": "Visām virsotnēm x reizina ar 2.",
         "opcijas": ["Vienāda", "Nav vienāda", "Nevar zināt"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Figūra izstiepjas."},
        {"jaut": "Visām virsotnēm maina x zīmi: (x; y) → (−x; y).",
         "opcijas": ["Vienāda", "Nav vienāda", "Nevar zināt"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Spoguļattēls pret y asi."},
    ]),

    Pasaule("Grīdas raksts",
            Ievadi("", [
                {"jaut": "Flīzes raksts ir 4 rūtiņas plats. Cik vienādu "
                         "rakstu ietilps rindā 36 rūtiņu platumā?",
                 "atb": ["9"], "padoms": "36 : 4."},
                {"jaut": "Pirmā raksta kreisā mala ir pie x = 0. Pie kāda x "
                         "sākas piektais raksts?",
                 "atb": ["16"], "padoms": "4 raksti pirms tā · 4."},
                {"jaut": "Katrā rakstā ir 6 zilas rūtiņas. Cik zilu "
                         "rūtiņu visā rindā?",
                 "atb": ["54"], "padoms": "9 · 6."},
            ]),
            pavediens="maja",
            konteksts="Flīžu un tapešu raksti ir viena figūra, pārbīdīta "
                      "atkal un atkal.",
            kapec="Pārbīde rada vienādas figūras bez mērīšanas."),

    Zimejums("Raksts no vienādām figūrām",
             figura([(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (0, 2)],
                    platums=3, augstums=3),
             paskaidro="Vienu šādu «L» var pārbīdīt atkal un atkal."),

    Kopsavilkums([
        "Zīmēju vienādu figūru, pārbīdot visas virsotnes vienādi.",
        "Aprēķinu jaunās koordinātas.",
        "Zinu, ka pārbīde, pagrieziens un spoguļattēls saglabā vienādību.",
        "Zinu, ka stiepšana to nesaglabā.",
    ]),

    Majas([
        "Uzzīmē četrstūri rūtiņu lapā un vēl divus vienādus citās vietās.",
        "Pagriez savu četrstūri par 90° un pārbaudi malu garumus.",
        "Izdomā savu flīzes rakstu no vienādām figūrām.",
    ]),
]
