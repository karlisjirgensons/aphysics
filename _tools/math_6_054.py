# -*- coding: utf-8 -*-
"""6. klase, 54. stunda: «Kā parasto daļu pārvērst decimāldaļā?»

Pēdējais mikrotemats tematā savieno abus pierakstus. Pārvēršanai ir divi
ceļi, un abi ir vajadzīgi: paplašināšana ir ātrāka, dalīšana - vienmēr
iespējama. Te parādās arī pirmā daļa, kas decimālpierakstā nebeidzas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā parasto daļu pārvērst decimāldaļā?"

MERKIS = ("Iemācīsimies izteikt parasto daļu kā decimāldaļu, dalot "
          "skaitītāju ar saucēju vai lietojot daļas pamatīpašību.")

SATURS = [
    Sakums("Viens skaitlis - divi pieraksti",
           zimejums=restis([["1/2", "1/4", "1/5", "3/4"],
                            ["0,5", "0,25", "0,2", "0,75"]]),
           paraksts="Šīs vienādības ir vērts zināt no galvas - tās atgriežas "
                    "procentos, atlaidēs un mēriem.",
           fakti=["{1|2} un 0,5 ir viens un tas pats skaitlis.",
                  "Daļu var pārvērst, paplašinot saucēju līdz 10 vai 100.",
                  "Ja tā nevar, skaitītāju dala ar saucēju."]),

    Doma("Divi ceļi: paplašināt vai dalīt",
         "Parasto daļu izsaka kā decimāldaļu, saucēju paplašinot līdz 10, "
         "100 vai 1000, vai arī dalot skaitītāju ar saucēju.",
         soli=[
             "Paskaties, vai saucēju var paplašināt līdz 10, 100 vai 1000.",
             "Ja var - reizini abus locekļus un pieraksti decimāldaļu.",
             "Ja nevar - dali skaitītāju ar saucēju.",
             "Dalot pieraksti nulles, līdz atlikums kļūst par nulli.",
             "Ja atlikums atkārtojas, atbildi noapaļo un pasaki, līdz "
             "kurai vietai.",
         ],
         pieze="Saucēju līdz desmitam var paplašināt tad, ja tajā ir tikai "
               "reizinātāji 2 un 5. Tāpēc {3|8} pārvēršas precīzi, bet "
               "{1|3} - nē."),

    Paraugs("Abi ceļi vienam uzdevumam",
            uzd="Izsaki {3|4} un {1|3} kā decimāldaļas.",
            soli=[
                ("{3|4} = {3 · 25|4 · 25} = {75|100}",
                 "Saucēju paplašina līdz simtam."),
                ("{75|100} = 0,75",
                 "Simtdaļas raksta ar diviem cipariem aiz komata."),
                ("{1|3}: 1 : 3 = 0,333...",
                 "Saucēju 3 līdz desmitam paplašināt nevar."),
                ("Noapaļo: apmēram 0,33",
                 "Atlikums atkārtojas bezgalīgi."),
            ],
            atbilde="0,75 un apmēram 0,33"),

    Ievadi("Pārvērt decimāldaļā", [
        {"jaut": "Cik ir {1|2} decimāldaļā?",
         "atb": ["0,5", "0.5"], "padoms": "{5|10}."},
        {"jaut": "Cik ir {1|4} decimāldaļā?",
         "atb": ["0,25", "0.25"], "padoms": "{25|100}."},
        {"jaut": "Cik ir {3|5} decimāldaļā?",
         "atb": ["0,6", "0.6"], "padoms": "{6|10}."},
        {"jaut": "Cik ir {7|20} decimāldaļā?",
         "atb": ["0,35", "0.35"], "padoms": "{35|100}."},
        {"jaut": "Cik ir {3|8} decimāldaļā?",
         "atb": ["0,375", "0.375"], "padoms": "3 : 8."},
        {"jaut": "Cik ir {9|25} decimāldaļā?",
         "atb": ["0,36", "0.36"], "padoms": "{36|100}."},
    ], pamats=4,
        ievads="Vispirms mēģini paplašināt - tas ir ātrāk nekā dalīt."),

    Varianti("Kurš ceļš te der?", [
        {"jaut": "{7|8} - kurš ceļš ir ērtāks?",
         "opcijas": ["Dalīt 7 : 8", "Paplašināt līdz 10",
                     "Paplašināt līdz 100", "Nevienu nevar"],
         "pareizi": 0,
         "padoms": "8 · 125 = 1000, bet dalīt ir īsāk."},
        {"jaut": "Kuru daļu decimālpierakstā nevar izteikt precīzi?",
         "opcijas": ["{1|3}", "{1|4}", "{1|5}", "{1|8}"],
         "pareizi": 0,
         "padoms": "Saucējā ir 3."},
        {"jaut": "{1|3} decimāldaļā ir apmēram...",
         "opcijas": ["0,33", "0,3", "0,13", "3,0"],
         "pareizi": 0,
         "padoms": "1 : 3 = 0,333..."},
        {"jaut": "Kurus saucējus var paplašināt līdz 10, 100 vai 1000?",
         "opcijas": ["Tos, kuros ir tikai 2 un 5", "Visus",
                     "Tikai pāra", "Tikai tos, kas mazāki par 10"],
         "pareizi": 0,
         "padoms": "10 = 2 · 5."},
    ], pamats=4),

    Pasaule("Cik tas ir decimālpierakstā?",
            Ievadi("", [
                {"jaut": "Skolēns atbildēja pareizi uz {3|4} jautājumiem. "
                         "Cik tas ir decimāldaļā?",
                 "atb": ["0,75", "0.75"], "padoms": "{75|100}."},
                {"jaut": "Cik procentu tas ir?",
                 "atb": ["75"], "padoms": "0,75 ir 75 simtdaļas."},
                {"jaut": "Otrs atbildēja uz {17|20}. Cik tas ir decimāldaļā?",
                 "atb": ["0,85", "0.85"], "padoms": "{85|100}."},
                {"jaut": "Trešais atbildēja uz {5|8}. Cik tas ir "
                         "decimāldaļā?",
                 "atb": ["0,625", "0.625"], "padoms": "5 : 8."},
            ]),
            pavediens="skola",
            konteksts="Pārbaudes darba rezultātu pieraksta gan kā daļu, gan "
                      "kā procentus - tas ir viens un tas pats skaitlis.",
            kapec="Pāreja uz decimālpierakstu ir pirmais solis uz "
                  "procentiem."),

    Zimejums("Daļas, kuras der zināt no galvas",
             restis([["1/8", "1/5", "1/4", "1/2"],
                     ["0,125", "0,2", "0,25", "0,5"]]),
             paskaidro="Šīs četras vienādības atkārtojas gandrīz katrā "
                       "uzdevumā ar procentiem un atlaidēm.",
             ievads="Ja šīs zina no galvas, rēķins kļūst divreiz ātrāks."),

    Kopsavilkums([
        "Pārvēršu parasto daļu decimāldaļā abos ceļos.",
        "Izvēlos paplašināšanu, ja saucējs to atļauj.",
        "Dalu skaitītāju ar saucēju, ja paplašināt nevar.",
        "Zinu, kad rezultāts ir precīzs un kad - noapaļots.",
    ]),

    Majas([
        "Pārvērt decimāldaļās {2|5}, {5|8} un {1|6}.",
        "Iemācies no galvas četras vienādības no šīs stundas.",
        "Atrodi daļu, kuras decimālpieraksts nebeidzas, un pieraksti, kāpēc.",
    ]),
]
