# -*- coding: utf-8 -*-
"""3. klase, 37. stunda: «Kurš paņēmiens man der?»

Vienu un to pašu rēķinu var izdarīt vairākos veidos, un labākais ir tas, kurš
konkrētajam skolēnam ir drošākais. Stunda salīdzina trīs galvas rēķina
paņēmienus uz viena piemēra, lai izvēle būtu pamatota, nevis nejauša.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         restis)

TEMA = "Kurš paņēmiens man der?"

MERKIS = ("Salīdzināsim vairākus rēķināšanas paņēmienus un izvēlēsimies sev "
          "piemērotāko.")

SATURS = [
    Sakums("Trīs ceļi līdz vienai atbildei - kuru izvēlēsies?",
           zimejums=restis([["48 + 26"],
                            ["40+20 un 8+6"],
                            ["48+20 un +6"],
                            ["48+30 mīnus 4"]],
                           "viens rēķins, trīs paņēmieni"),
           paraksts="Visi trīs dod 74. Atšķiras tikai ceļš.",
           fakti=["Pareizu paņēmienu ir vairāki, ne viens.",
                  "Labākais ir tas, kurā tu kļūdies vismazāk."]),

    Doma("Paņēmienu izvēlas pēc skaitļiem",
         "Ja otrs saskaitāmais ir tuvu apaļam desmitam, rēķini no tā; ja nē - "
         "sadali desmitos un vienos.",
         soli=[
             "Paskaties, vai kāds skaitlis ir tuvu apaļam desmitam.",
             "Ja ir - rēķini ar apaļo un pēc tam izlabo starpību.",
             "Ja nav - sadali abus skaitļus desmitos un vienos.",
             "Pārbaudi atbildi ar otru paņēmienu.",
         ],
         pieze="Nav slikta paņēmiena, ir tikai neveiksmīga izvēle. 48 + 29 ar "
               "apaļo skaitli ir viegli, bet 48 + 26 - jau ne tik."),

    Slidnis("Trīs ceļi līdz 74",
            soli=[
                {"v": "40 + 20 = 60",
                 "teksts": "Pirmais ceļš: vispirms desmiti.", "josla": 25},
                {"v": "8 + 6 = 14",
                 "teksts": "Tad vieni; 60 + 14 = 74.", "josla": 50},
                {"v": "48 + 20 = 68",
                 "teksts": "Otrais ceļš: pa desmitiem un tad vieni.",
                 "josla": 75},
                {"v": "68 + 6 = 74",
                 "teksts": "Tā pati atbilde, cits ceļš.", "josla": 100},
            ],
            ievads="Abi ceļi ved uz 74. Izvēlies to, kurā tev ir mazāk "
                   "soļu."),

    Paraugs("Kā ērtāk rēķināt 48 + 29?",
            uzd="Izrēķini 48 + 29 ar ērtāko paņēmienu.",
            soli=[
                ("29 ≈ 30",
                 "Otrs saskaitāmais ir gandrīz apaļš desmits."),
                ("48 + 30 = 78",
                 "Rēķina ar apaļo skaitli - tas ir viegli."),
                ("78 − 1 = 77",
                 "Pieskaitīja par vienu vairāk, tāpēc vienu atņem."),
            ],
            atbilde="77"),

    Ievadi("Izvēlies ērtāko ceļu", [
        {"jaut": "57 + 19 = ?", "atb": ["76"], "padoms": "57 + 20 − 1."},
        {"jaut": "64 + 28 = ?", "atb": ["92"], "padoms": "64 + 30 − 2."},
        {"jaut": "45 + 37 = ?", "atb": ["82"], "padoms": "40 + 30 un 5 + 7."},
        {"jaut": "83 − 29 = ?", "atb": ["54"], "padoms": "83 − 30 + 1."},
        {"jaut": "72 − 38 = ?", "atb": ["34"], "padoms": "72 − 40 + 2."},
        {"jaut": "56 + 25 = ?", "atb": ["81"], "padoms": "56 + 20 + 5."},
    ], pamats=4),

    Zimejums("Kad kurš paņēmiens der",
             restis([["skaitlis tuvu desmitam", "rēķini no apaļā"],
                     ["skaitlis pa vidu", "sadali desmitos un vienos"]],
                    "izvēles noteikums"),
             paskaidro="Paņēmienu nosaka skaitļi, nevis ieradums - tāpēc "
                       "vienā uzdevumā der viens, otrā cits.",
             ievads="Divas situācijas, divi ceļi."),

    Varianti("Kurš ceļš ir īsākais?", [
        {"jaut": "Kā ērtāk rēķināt 67 + 29?",
         "opcijas": ["67 + 30 − 1", "60 + 20 un 7 + 9", "67 + 9 + 20",
                     "Pa vienam"],
         "pareizi": 0, "padoms": "29 ir gandrīz 30."},
        {"jaut": "Kā ērtāk rēķināt 94 − 48?",
         "opcijas": ["94 − 50 + 2", "94 − 40 − 8", "90 − 40 un 4 − 8",
                     "Pa vienam"],
         "pareizi": 0, "padoms": "48 ir gandrīz 50."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Pareizu paņēmienu ir vairāki",
                     "Pareizs ir tikai viens paņēmiens",
                     "Paņēmiens nav svarīgs", "Vienmēr jārēķina stabiņā"],
         "pareizi": 0, "padoms": "Ceļi ir dažādi, atbilde viena."},
        {"jaut": "Kā pārbaudīt savu atbildi?",
         "opcijas": ["Izrēķināt ar citu paņēmienu", "Izrēķināt vēlreiz "
                     "tāpat", "Pajautāt draugam", "Nekā"],
         "pareizi": 0, "padoms": "Cits ceļš pamana to pašu kļūdu."},
    ], pamats=4),

    Pasaule("Cik metru noskrēja komanda?",
            Ievadi("", [
                {"jaut": "Pirmais skrējējs 48 m, otrais 29 m. Cik kopā?",
                 "atb": ["77"], "padoms": "48 + 30 − 1."},
                {"jaut": "Trešais noskrēja 35 m. Cik trīs kopā?",
                 "atb": ["112"], "padoms": "77 + 35."},
                {"jaut": "Distance ir 150 m. Cik vēl trūkst?",
                 "atb": ["38"], "padoms": "150 − 112."},
                {"jaut": "Ceturtais noskrēja 38 m. Vai distance ir "
                         "pabeigta? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "112 + 38 = 150.",
                 "tastatura": "text"},
            ]),
            pavediens="sports",
            konteksts="Stafetē rezultātu saskaita pa posmiem - un katrs "
                      "posms ir neapaļš skaitlis.",
            kapec="Ērts paņēmiens ļauj saskaitīt uzreiz, vēl skrējiena "
                  "laikā."),

    Kopsavilkums([
        "Zinu vairākus galvas rēķina paņēmienus.",
        "Izvēlos paņēmienu pēc tā, kādi ir skaitļi.",
        "Rēķinu no apaļa desmita un izlaboju starpību.",
        "Pārbaudu atbildi ar citu paņēmienu.",
    ]),

    Majas([
        "Izrēķini 58 + 27 divos dažādos veidos.",
        "Atrodi piemēru, kurā apaļā skaitļa paņēmiens ir visērtākais.",
        "Pastāsti mājiniekiem, kurš paņēmiens tev der vislabāk.",
    ]),
]
