# -*- coding: utf-8 -*-
"""6. klase, 162. stunda: «Kur risinājumā ir kļūda?»

Mikrotemata noslēgums. Tagad kļūdas var būt visur: zīmē, darbību secībā,
pierakstā vai komatā. Tāpēc svarīgi ir ne tikai atrast kļūdu, bet nosaukt
tās veidu - tā to vieglāk nepieļaut otrreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kur risinājumā ir kļūda?"

MERKIS = ("Izvērtēsim cita risinājumu un raksturosim kļūdas veidu.")

SATURS = [
    Sakums("Četri kļūdu veidi",
           zimejums=restis([["zīme", "secība", "komats", "pieraksts"]]),
           paraksts="Gandrīz katra kļūda šajā tematā ir viena no šīm "
                    "četrām.",
           fakti=["Zīmes kļūda: sajaukts pluss ar mīnusu.",
                  "Secības kļūda: saskaitīts pirms reizināšanas.",
                  "Komata kļūda: rezultāts desmitkārt lielāks vai mazāks."]),

    Doma("Vispirms novērtē, tad meklē soli",
         "Kļūdu meklē trijos soļos: novērtē, kādai jābūt atbildei, atrod "
         "pirmo soli, kas nesakrīt, un nosauc kļūdas veidu.",
         soli=[
             "Novērtē atbildes lielumu un zīmi.",
             "Salīdzini ar doto atbildi.",
             "Pārbaudi katru soli no sākuma.",
             "Atrodi pirmo nesakritību.",
             "Nosauc kļūdas veidu: zīme, secība, komats vai pieraksts.",
         ],
         pieze="Ja atbilde atšķiras desmitkārt, kļūda gandrīz vienmēr ir "
               "komatā; ja tikai ar zīmi - zīmju likumā. Novērtējums pasaka, "
               "kur meklēt."),

    Paraugs("Atrodi un nosauc kļūdu",
            uzd="Skolēns rēķina: 4 + 6 · (−2) = −20. Kur ir kļūda?",
            soli=[
                ("Novērtējums: reizinājums ir −12, tad 4 − 12",
                 "Atbildei jābūt ap −8."),
                ("−20 ir par mazu",
                 "Kļūda ir kaut kur."),
                ("Skolēns rēķināja (4 + 6) · (−2)",
                 "Vispirms saskaitīja."),
                ("Kļūdas veids: darbību secība",
                 "Reizināšana ir pirms saskaitīšanas."),
            ],
            atbilde="pareizi ir −8; kļūda secībā"),

    Ievadi("Izlabo un nosauc", [
        {"jaut": "Skolēns: 4 + 6 · (−2) = −20. Kāda ir pareizā atbilde?",
         "atb": ["-8", "−8"], "padoms": "Vispirms reizināšana."},
        {"jaut": "Skolēns: (−3) · (−4) = −12. Kāda ir pareizā atbilde?",
         "atb": ["12"], "padoms": "Vienādas zīmes."},
        {"jaut": "Skolēns: 0,4 · 0,2 = 0,8. Kāda ir pareizā atbilde?",
         "atb": ["0,08", "0.08"], "padoms": "Divi cipari aiz komata."},
        {"jaut": "Skolēns: (−10) : (−2) = −5. Kāda ir pareizā atbilde?",
         "atb": ["5"], "padoms": "Vienādas zīmes."},
        {"jaut": "Skolēns: (−2) otrajā pakāpē = −4. Kāda ir pareizā atbilde?",
         "atb": ["4"], "padoms": "Divi mīnusi."},
        {"jaut": "Skolēns: 12 − 4 · 2 = 16. Kāda ir pareizā atbilde?",
         "atb": ["4"], "padoms": "12 − 8."},
    ], pamats=4,
        ievads="Vispirms novērtē, kādai jābūt atbildei."),

    Varianti("Kāds ir kļūdas veids?", [
        {"jaut": "4 + 6 · (−2) = −20. Kļūdas veids ir...",
         "opcijas": ["darbību secība", "zīme", "komats", "pieraksts"],
         "pareizi": 0,
         "padoms": "Vispirms saskaitīts."},
        {"jaut": "(−3) · (−4) = −12. Kļūdas veids ir...",
         "opcijas": ["zīme", "darbību secība", "komats", "pieraksts"],
         "pareizi": 0,
         "padoms": "Divi mīnusi dod plusu."},
        {"jaut": "0,4 · 0,2 = 0,8. Kļūdas veids ir...",
         "opcijas": ["komats", "zīme", "darbību secība", "pieraksts"],
         "pareizi": 0,
         "padoms": "Ciparu skaits aiz komata."},
        {"jaut": "Ja atbilde atšķiras desmitkārt, kļūda visticamāk ir...",
         "opcijas": ["komatā", "zīmē", "secībā", "pierakstā"],
         "pareizi": 0,
         "padoms": "Komats pārcelts par vienu vietu."},
    ], pamats=4),

    Petijums("Kļūdu saraksts",
             vajag="savi un soļabiedra darbi",
             soli=[
                 "Pārskati piecus savus pēdējos risinājumus.",
                 "Atzīmē katru kļūdu un nosauc tās veidu.",
                 "Saskaiti, cik reižu atkārtojās katrs veids.",
                 "Pieraksti, kurš veids tev ir biežākais.",
                 "Izdomā vienu pārbaudes paņēmienu tieši šim veidam.",
             ],
             secinajums="Katram ir savs biežākais kļūdas veids - un tieši "
                        "tam vajag savu pārbaudi."),

    Pasaule("Vai aprēķins ir pareizs?",
            Ievadi("", [
                {"jaut": "Čekā: 3 preces pa 2,5 € = 75 €. Kāda ir pareizā "
                         "summa?",
                 "atb": ["7,5", "7.5"], "padoms": "Komata kļūda."},
                {"jaut": "Kontā: −40 + 25 = −65. Kāda ir pareizā summa?",
                 "atb": ["-15", "−15"], "padoms": "Zīmju kļūda."},
                {"jaut": "Cena 20 €, atlaide 25 %, rezultāts 5 €. Kāda ir "
                         "pareizā cena?",
                 "atb": ["15"], "padoms": "5 € ir atlaide, ne cena."},
                {"jaut": "Temperatūra no −6 °C uz 2 °C, izmaiņa 4 grādi. "
                         "Kāda ir pareizā izmaiņa?",
                 "atb": ["8"], "padoms": "2 − (−6)."},
            ]),
            pavediens="veikals",
            konteksts="Rēķinu pārbaude ikdienā ir tieši šī prasme: novērtēt, "
                      "salīdzināt un nosaukt, kur kļūda.",
            kapec="Nosaukta kļūda atkārtojas retāk nekā nenosaukta."),

    Kopsavilkums([
        "Izvērtēju cita risinājumu pa soļiem.",
        "Sāku ar atbildes novērtējumu.",
        "Atrodu pirmo kļūdaino soli.",
        "Nosaucu kļūdas veidu: zīme, secība, komats vai pieraksts.",
    ]),

    Majas([
        "Atrodi savos darbos pa vienai katra veida kļūdai.",
        "Pieraksti, kurš veids tev ir biežākais.",
        "Izdomā pārbaudi, kas tieši šo veidu pamanītu.",
    ]),
]
