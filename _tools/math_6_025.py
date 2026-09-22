# -*- coding: utf-8 -*-
"""6. klase, 25. stunda: «Kad reizinājumu var saīsināt?»

Stunda par to, kā strādāt ar mazākiem skaitļiem. Saīsināt pirms reizināšanas
nav triks - tas ir vienīgais veids, kā {14|15} · {25|28} izrēķināt galvā,
nerakstot četrciparu skaitļus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kad reizinājumu var saīsināt?"

MERKIS = ("Mācīsimies saskatīt iespēju saīsināt pirms reizināšanas un "
          "paskaidrot, kāpēc tā drīkst darīt.")

SATURS = [
    Sakums("Mazāki skaitļi - mazāk kļūdu",
           fakti=["{14|15} · {25|28} ar lieliem skaitļiem prasa 350 un 420.",
                  "Saīsinot pirms reizināšanas, paliek {1|3} · {5|2}.",
                  "Rezultāts ir tas pats, bet rēķins ietilpst galvā."]),

    Doma("Saīsināt drīkst pa diagonāli",
         "Reizinot daļas, kopīgu dalītāju drīkst izsvītrot jebkurā "
         "skaitītājā un jebkurā saucējā - arī pa diagonāli.",
         soli=[
             "Pieraksti reizinājumu, bet neizrēķini to.",
             "Meklē kopīgu dalītāju kādam skaitītājam un kādam saucējam.",
             "Izdali abus ar šo skaitli un pieraksti jaunos.",
             "Atkārto, kamēr kopīgu dalītāju vairs nav.",
             "Tikai tagad sareizini to, kas palicis.",
         ],
         pieze="Tas ir atļauts tāpēc, ka viss reizinājums ir viena liela "
               "daļa: {a · c|b · d}. Saīsināt lielu daļu drīkst vienmēr - "
               "vienalga, no kura reizinātāja skaitlis nāk."),

    Paraugs("Saīsini pirms reizināšanas",
            uzd="Cik ir {14|15} · {25|28}?",
            soli=[
                ("14 un 28 dalās ar 14",
                 "Skaitītājs no pirmās, saucējs no otrās daļas."),
                ("{1|15} · {25|2}",
                 "14 : 14 = 1; 28 : 14 = 2."),
                ("15 un 25 dalās ar 5",
                 "Tagad otra diagonāle."),
                ("{1|3} · {5|2} = {5|6}",
                 "15 : 5 = 3; 25 : 5 = 5."),
            ],
            atbilde="{5|6}"),

    Ievadi("Saīsini un tad reizini", [
        {"jaut": "Cik ir {2|3} · {3|4}? Atbildi raksti kā a/b.",
         "atb": ["1/2", "6/12"], "padoms": "Saīsini 3 pret 3."},
        {"jaut": "Cik ir {5|8} · {4|15}? Atbildi raksti kā a/b.",
         "atb": ["1/6"], "padoms": "5 pret 15 un 4 pret 8."},
        {"jaut": "Cik ir {9|10} · {5|6}? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "9 pret 6 (ar 3) un 5 pret 10 (ar 5)."},
        {"jaut": "Cik ir {7|12} · {6|7}? Atbildi raksti kā a/b.",
         "atb": ["1/2"], "padoms": "7 pret 7 un 6 pret 12."},
        {"jaut": "Cik ir {3|8} · {16|9}? Atbildi raksti kā a/b.",
         "atb": ["2/3"], "padoms": "3 pret 9 un 16 pret 8."},
        {"jaut": "Cik ir {21|25} · {10|7}? Atbildi raksti kā a/b.",
         "atb": ["6/5", "1 1/5"], "padoms": "21 pret 7 un 10 pret 25."},
    ], pamats=4,
        ievads="Pirms rakstīt lielus skaitļus, paskaties pa diagonāli."),

    Varianti("Vai tā drīkst?", [
        {"jaut": "Vai {4|9} · {3|8} rēķinā drīkst saīsināt 4 un 8?",
         "opcijas": ["Jā, tie ir dažādās daļās, bet vienā reizinājumā",
                     "Nē, tie ir dažādās daļās",
                     "Jā, bet tikai pēc reizināšanas",
                     "Nē, 4 nedalās ar 8"],
         "pareizi": 0,
         "padoms": "Viss reizinājums ir viena daļa."},
        {"jaut": "Vai saīsināt drīkst divus skaitītājus savā starpā?",
         "opcijas": ["Nē, tikai skaitītāju ar saucēju",
                     "Jā, vienmēr", "Jā, ja tie ir vienādi",
                     "Nē, nekad nedrīkst saīsināt"],
         "pareizi": 0,
         "padoms": "Saīsina daļas augšu ar apakšu."},
        {"jaut": "Kāpēc saīsina pirms reizināšanas?",
         "opcijas": ["Lai skaitļi paliktu mazi", "Lai atbilde būtu citāda",
                     "Tā prasa likums", "Lai rēķins būtu garāks"],
         "pareizi": 0,
         "padoms": "Rezultāts ir tas pats, darbs - mazāks."},
        {"jaut": "{6|7} · {7|6} ir vienāds ar...",
         "opcijas": ["1", "{42|42} nav vienāds ar 1", "0", "{13|13}"],
         "pareizi": 0,
         "padoms": "Viss saīsinās."},
    ], pamats=4),

    Pasaule("Cik degvielas paliek tvertnē?",
            Ievadi("", [
                {"jaut": "Tvertnē ir {3|4} no 80 l. Cik litru tajā ir?",
                 "atb": ["60"], "padoms": "{3|4} · 80."},
                {"jaut": "No tiem {2|3} iztērē pirmajā posmā. Cik litru "
                         "iztērēti?",
                 "atb": ["40"], "padoms": "{2|3} · 60."},
                {"jaut": "Kāda daļa no pilnas tvertnes ir iztērēta? Atbildi "
                         "raksti kā a/b.",
                 "atb": ["1/2", "6/12"], "padoms": "{3|4} · {2|3}."},
                {"jaut": "Cik litru paliek tvertnē?",
                 "atb": ["40"], "padoms": "80 − 40."},
            ]),
            pavediens="celojums",
            konteksts="Degvielas rādītājs rāda daļu, nevis litrus - tāpēc "
                      "rēķina ar daļām un saīsina pirms reizināšanas.",
            kapec="Saīsinot skaitļi paliek tādi, kurus var pārbaudīt galvā."),

    Kopsavilkums([
        "Saskatu kopīgu dalītāju skaitītājā un saucējā pirms reizināšanas.",
        "Saīsinu arī pa diagonāli un paskaidroju, kāpēc tā drīkst.",
        "Rēķinu ar mazākiem skaitļiem un pieļauju mazāk kļūdu.",
        "Pārbaudu, vai rezultātu vēl var saīsināt.",
    ]),

    Majas([
        "Izrēķini {12|25} · {5|9}, saīsinot pirms reizināšanas.",
        "Atrodi reizinājumu, kurā saīsināt nevar nemaz.",
        "Pieraksti vienu rēķinu abos veidos un salīdzini, kurš bija īsāks.",
    ]),
]
