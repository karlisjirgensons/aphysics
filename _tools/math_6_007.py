# -*- coding: utf-8 -*-
"""6. klase, 7. stunda: «Kā pagatavot maisījumu?»

Tas pats rēķins, kas iepriekšējā stundā, bet no otra gala: dots nevis
kopums, bet vienas sastāvdaļas daudzums. Tieši tā tas notiek virtuvē un
darbnīcā - miltu maisā ir, cik ir, un pārējais jāpielāgo.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kā pagatavot maisījumu?"

MERKIS = ("Mācīsimies izveidot maisījumu dotā attiecībā, ja zināms viena "
          "sastāvdaļa daudzums vai kopējais daudzums.")

SATURS = [
    Sakums("Kāpēc pankūkas dažreiz sanāk gumijas?",
           fakti=["Pankūku mīklā miltus un pienu ņem apmēram 1 : 2.",
                  "Ja piena par maz, mīkla kļūst bieza un cieta.",
                  "Recepte ir attiecība, nevis viens pareizais daudzums."]),

    Doma("Sāc no tā, kas jau ir",
         "Ja zināms viena sastāvdaļa daudzums, vispirms izrēķini vienu daļu.",
         soli=[
             "Atrodi tekstā sastāvdaļu, kuras daudzums ir dots.",
             "Izdali to ar tās sastāvdaļas daļu skaitu - tā ir viena daļa.",
             "Katrai pārējai reizini vienu daļu ar tās skaitli.",
             "Saskaiti visu kopā - tā ir maisījuma masa vai tilpums.",
         ],
         pieze="Tas ir tas pats divsoļu rēķins: vispirms viena daļa, tad "
               "reizināšana. Mainās tikai tas, no kura skaitļa sāk."),

    Paraugs("Trīs sastāvdaļas no vienas",
            uzd="Musli gatavo, auzu pārslas, riekstus un rozīnes ņemot "
                "attiecībā 6 : 2 : 1. Pārslu ir 300 g. Cik ir pārējo?",
            soli=[
                ("300 : 6 = 50 g",
                 "Pārslām pienākas 6 daļas, tātad viena daļa ir 50 g."),
                ("Rieksti 2 · 50 = 100 g",
                 "Reizina vienu daļu ar riekstu skaitli."),
                ("Rozīnes 1 · 50 = 50 g",
                 "Tā pati darbība pēdējai sastāvdaļai."),
                ("300 + 100 + 50 = 450 g",
                 "Tik sver viss maisījums."),
            ],
            atbilde="100 g riekstu, 50 g rozīņu; kopā 450 g"),

    Ievadi("Pagatavo maisījumu", [
        {"jaut": "Sula un ūdens 1 : 3. Sulas ir 200 ml. Cik ml ūdens?",
         "atb": ["600"], "padoms": "3 · 200."},
        {"jaut": "Tas pats dzēriens. Cik ml sanāks kopā?",
         "atb": ["800"], "padoms": "200 + 600."},
        {"jaut": "Java: cements un smiltis 1 : 4. Smilšu ir 20 kg. Cik kg "
                 "cementa?",
         "atb": ["5"], "padoms": "20 : 4."},
        {"jaut": "Musli 6 : 2 : 1. Rozīņu ir 30 g. Cik gramu pārslu?",
         "atb": ["180"], "padoms": "Viena daļa ir 30 g; 6 · 30."},
        {"jaut": "Krāsa un šķīdinātājs 5 : 2. Šķīdinātāja ir 400 ml. Cik ml "
                 "krāsas?",
         "atb": ["1000"], "padoms": "400 : 2 = 200; 5 · 200."},
        {"jaut": "Tēja: ūdens un koncentrāts 9 : 1. Kopā sanāk 2 l. Cik ml "
                 "koncentrāta?",
         "atb": ["200"], "padoms": "2 l = 2000 ml; 10 daļas; 2000 : 10."},
    ], pamats=4,
        ievads="Vispirms viena daļa - tad viss pārējais ir reizināšana."),

    Varianti("Vai maisījums iznāks?", [
        {"jaut": "Attiecība 1 : 3. Ir 5 karotes sulas. Cik karotes ūdens?",
         "opcijas": ["15", "8", "3", "12"],
         "pareizi": 0,
         "padoms": "Viena daļa ir 5 karotes; ūdenim pienākas 3 daļas."},
        {"jaut": "Recepte 2 : 3, bet ir tikai 7 g pirmās vielas. Kas notiek?",
         "opcijas": ["Viena daļa ir 3,5 g - maisījums sanāk",
                     "Maisījumu izveidot nevar",
                     "Jāņem 7 daļas", "Attiecība mainās uz 7 : 3"],
         "pareizi": 0,
         "padoms": "Daļa nav obligāti vesels skaitlis."},
        {"jaut": "Kurā gadījumā viena daļa ir vislielākā?",
         "opcijas": ["120 g sadalot attiecībā 1 : 1",
                     "120 g sadalot attiecībā 1 : 2",
                     "120 g sadalot attiecībā 1 : 3",
                     "120 g sadalot attiecībā 2 : 3"],
         "pareizi": 0,
         "padoms": "Jo mazāk daļu kopā, jo lielāka katra daļa."},
        {"jaut": "Maisījumā 3 : 1 pielēja vēl ūdeni. Kas notika?",
         "opcijas": ["Attiecība mainījās", "Nekas nemainījās",
                     "Viena daļa palika tā pati", "Kopums samazinājās"],
         "pareizi": 0,
         "padoms": "Viena sastāvdaļa auga, otra ne."},
    ], pamats=4),

    Pasaule("Cik pagatavot vienai klasei?",
            Ievadi("", [
                {"jaut": "Kakao: piens un pulveris 20 : 1. Pulvera ir 25 g. "
                         "Cik ml piena?",
                 "atb": ["500"], "padoms": "20 · 25."},
                {"jaut": "Klasē 25 skolēni, katram 200 ml dzēriena. Cik ml "
                         "kopā?",
                 "atb": ["5000"], "padoms": "25 · 200."},
                {"jaut": "Dzērienā sula un ūdens ir 1 : 4. Cik ml sulas "
                         "vajag 5000 ml dzēriena?",
                 "atb": ["1000"], "padoms": "5 daļas; 5000 : 5."},
                {"jaut": "Cik ml ūdens vajadzēs klāt?",
                 "atb": ["4000"], "padoms": "4 · 1000."},
            ]),
            pavediens="virtuve",
            konteksts="Pasākumā nepietiek zināt recepti - jāzina arī, cik "
                      "cilvēkiem tā jāpārrēķina.",
            kapec="Attiecība pasaka garšu, skolēnu skaits - daudzumu."),

    Petijums("Pagatavo maisījumu pats",
             vajag="divas glāzes, karote un ūdens",
             soli=[
                 "Izvēlies attiecību 1 : 3 un vienu karoti par vienu daļu.",
                 "Ielej pirmajā glāzē 1 karoti, otrajā - 3 karotes ūdens.",
                 "Pieraksti, cik karotes sanāca kopā.",
                 "Atkārto ar 2 karotēm par vienu daļu un salīdzini kopumu.",
             ],
             secinajums="Daļas lielums mainījās, attiecība palika tā pati - "
                        "un kopums pieauga tikpat reižu."),

    Kopsavilkums([
        "Sāku no tās sastāvdaļas, kuras daudzums ir dots.",
        "Atrodu vienu daļu, dalot doto daudzumu ar tās daļu skaitu.",
        "Aprēķinu pārējās sastāvdaļas, reizinot vienu daļu.",
        "Saskaitu visu kopā un zinu maisījuma daudzumu.",
    ]),

    Majas([
        "Pagatavo dzērienu attiecībā 1 : 5 un pieraksti abus daudzumus.",
        "Atrodi recepti, kurā ir trīs sastāvdaļas, un pieraksti to kā "
        "attiecību.",
        "Pārrēķini to pašu recepti divreiz lielākam daudzumam.",
    ]),
]
