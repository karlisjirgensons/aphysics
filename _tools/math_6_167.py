# -*- coding: utf-8 -*-
"""6. klase, 167. stunda: «Cik droši jau rēķinu?»

Temata pēdējā mācību stunda pirms pēdējā pārbaudes darba. Patstāvīgs darbs
ar visa gada skaitļiem un pašvērtējums: kuras vietas vēl jāatkārto pirms
vasaras.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Cik droši jau rēķinu?"

MERKIS = ("Patstāvīgi rēķināsim ar racionāliem skaitļiem un novērtēsim savu "
          "prasmi.")

SATURS = [
    Sakums("Viss gads vienā uzdevumā",
           fakti=["Zīmju likums der visiem skaitļu veidiem.",
                  "Darbību secība nemainās no skaitļu veida.",
                  "Katru atbildi var pārbaudīt ar pretējo darbību."]),

    Doma("Viens ceļš visiem uzdevumiem",
         "Katru aprēķinu veic vienā un tajā pašā kārtībā: novērtē, izvēlas "
         "pierakstu, ievēro darbību secību, pārbauda rezultātu.",
         soli=[
             "Novērtē, kāda būs atbilde pēc zīmes un lieluma.",
             "Izvēlies vienotu pierakstu visiem skaitļiem.",
             "Ievēro darbību secību un raksti vienu soli rindā.",
             "Izrēķini rezultātu.",
             "Pārbaudi to ar novērtējumu un ar pretējo darbību.",
         ],
         pieze="Šie pieci soļi ir vienādi visam gadam: attiecībām, daļām, "
               "procentiem un negatīviem skaitļiem. Atšķiras tikai tas, ar "
               "ko aizpilda katru soli."),

    Paraugs("Viens uzdevums, visi soļi",
            uzd="Izrēķini (−0,5 + {3|4}) · (−8).",
            soli=[
                ("Novērtējums: iekavā mazs pozitīvs skaitlis, tad reizina "
                 "ar −8",
                 "Atbilde būs negatīva."),
                ("{3|4} = 0,75; iekavā −0,5 + 0,75 = 0,25",
                 "Decimāldaļas ērtākas."),
                ("0,25 · (−8) = −2",
                 "Zīmes atšķiras."),
                ("Pārbaude: −2 : (−8) = 0,25",
                 "Atgriežas iekavas vērtība."),
            ],
            atbilde="−2"),

    Ievadi("Izrēķini patstāvīgi", [
        {"jaut": "Cik ir (−0,5 + {3|4}) · (−8)?",
         "atb": ["-2", "−2"], "padoms": "0,25 · (−8)."},
        {"jaut": "Cik ir (−12) : 4 + 5?",
         "atb": ["2"], "padoms": "−3 + 5."},
        {"jaut": "Cik ir {2|3} · (−9)?",
         "atb": ["-6", "−6"], "padoms": "Saīsina 9 ar 3."},
        {"jaut": "Cik ir 25 % no 80 mīnus 30?",
         "atb": ["-10", "−10"], "padoms": "20 − 30."},
        {"jaut": "Cik ir (−2) otrajā pakāpē · (−3)?",
         "atb": ["-12", "−12"], "padoms": "4 · (−3)."},
        {"jaut": "Cik ir (−1,5) : 0,5 + 4?",
         "atb": ["1"], "padoms": "−3 + 4."},
    ], pamats=4,
        ievads="Katrai atbildei vispirms pasaki zīmi un aptuveno lielumu."),

    Petijums("Novērtē savu prasmi",
             vajag="burtnīca un gada uzdevumi",
             soli=[
                 "Izvēlies pa vienam uzdevumam no katra gada temata.",
                 "Atrisini tos patstāvīgi, nelūkojoties piezīmēs.",
                 "Atzīmē, kuros biji drošs un kuros ne.",
                 "Katram nedrošajam pieraksti, kas tieši sagādāja grūtības.",
                 "Izveido sarakstu, ko atkārtot pirms pārbaudes darba.",
             ],
             secinajums="Pašvērtējums ir precīzs tikai tad, kad uzdevumi "
                        "risināti bez piezīmēm - citādi šķiet, ka viss ir "
                        "skaidrs."),

    Varianti("Kurš solis ir pirmais?", [
        {"jaut": "Ar ko sāk katru aprēķinu?",
         "opcijas": ["Ar novērtējumu", "Ar rēķināšanu",
                     "Ar pārbaudi", "Ar atbildi"],
         "pareizi": 0,
         "padoms": "Novērtējums pasaka, ko gaidīt."},
        {"jaut": "Ja izteiksmē ir daļas un decimāldaļas, vispirms...",
         "opcijas": ["izvēlas vienu pierakstu", "rēķina no kreisās",
                     "noapaļo", "izlaiž grūtāko"],
         "pareizi": 0,
         "padoms": "Viens pieraksts - viens likums."},
        {"jaut": "Cik ir (−2) otrajā pakāpē · (−3)?",
         "opcijas": ["−12", "12", "−36", "36"],
         "pareizi": 0,
         "padoms": "4 · (−3)."},
        {"jaut": "Kā pārbaudīt reizinājumu?",
         "opcijas": ["Ar dalīšanu", "Ar saskaitīšanu",
                     "Ar kāpināšanu", "Nevar pārbaudīt"],
         "pareizi": 0,
         "padoms": "Pretējā darbība."},
    ], pamats=4),

    Pasaule("Kāds ir gada rezultāts?",
            Ievadi("", [
                {"jaut": "Gada sākumā kontā −40 €, katru mēnesi pievieno "
                         "15 €. Cik eiro ir pēc 4 mēnešiem?",
                 "atb": ["20"], "padoms": "−40 + 60."},
                {"jaut": "No tiem 25 % atliek uzkrājumam. Cik eiro tas ir?",
                 "atb": ["5"], "padoms": "20 : 4."},
                {"jaut": "Cik eiro paliek tēriņiem?",
                 "atb": ["15"], "padoms": "20 − 5."},
                {"jaut": "Ja izdevumi būtu 25 €, kāds būtu rezultāts eiro?",
                 "atb": ["-5", "−5"], "padoms": "20 − 25."},
            ]),
            pavediens="veikals",
            konteksts="Gada rezultātā satiekas visi šogad mācītie skaitļu "
                      "veidi: negatīvie, procenti un daļas.",
            kapec="Viens un tas pats ceļš der visiem uzdevumiem."),

    Kopsavilkums([
        "Patstāvīgi rēķinu ar visu veidu racionāliem skaitļiem.",
        "Sāku ar novērtējumu un beidzu ar pārbaudi.",
        "Izvēlos vienotu pierakstu un ievēroju darbību secību.",
        "Zinu, kuras vietas man vēl jāatkārto.",
    ]),

    Majas([
        "Atrisini piecus uzdevumus no dažādiem gada tematiem.",
        "Atzīmē tos, kuros nebiji drošs.",
        "Pieraksti, ko atkārtosi pirms pārbaudes darba.",
    ]),
]
