# -*- coding: utf-8 -*-
"""6. klase, 44. stunda: «Kas notiek, reizinot ar 10, 100 un 1000?»

Mikrotemats par četriem algoritmiem, kas visi ir viens un tas pats: komata
pārcelšana. Sākumā - visvienkāršākais virziens. Svarīgi, ka skolēni likumu
formulē paši, vērojot, kā cipari pārbīdās pa vietām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kas notiek, reizinot ar 10, 100 un 1000?"

MERKIS = ("Pētīsim un formulēsim algoritmu reizināšanai ar 10, 100 un 1000.")

SATURS = [
    Sakums("Gaismas ātrums vienā rindā",
           zimejums=restis([["3", ",", "0", "0"],
                            ["3", "0", ",", "0"],
                            ["3", "0", "0", ","]]),
           paraksts="3,00 → 30,0 → 300, - katru reizi komats pārceļas par "
                    "vienu vietu pa labi.",
           fakti=["Gaisma sekundē veic 300 000 km - tas ir 0,3 · 1 000 000.",
                  "Reizinot ar 10, komats pārceļas par vienu vietu pa labi.",
                  "Cipari nemainās - mainās tikai to vietas vērtība."]),

    Doma("Komats ceļo pa labi",
         "Reizinot ar 10, 100 vai 1000, komatu pārceļ par tik vietām pa "
         "labi, cik nulles ir reizinātājā.",
         soli=[
             "Saskaiti nulles reizinātājā.",
             "Pārcel komatu par tik vietām pa labi.",
             "Ja ciparu nepietiek, beigās pieraksti nulles.",
             "Pārbaudi: skaitlim jākļūst lielākam.",
         ],
         pieze="Kāpēc tā? 2,5 · 10 = {25|10} · 10 = 25. Saucējs saīsinās, un "
               "katrs cipars pārceļas par vienu vietas vērtību uz augšu."),

    Paraugs("Reizini ar 100",
            uzd="Cik ir 3,74 · 100?",
            soli=[
                ("100 - divas nulles",
                 "Tik vietas komats pārceļas."),
                ("3,74 → 37,4 → 374",
                 "Divi soļi pa labi."),
                ("Pārbaude: 3,74 ir apmēram 4; 4 · 100 = 400",
                 "374 ir ticams."),
            ],
            atbilde="374"),

    Ievadi("Pārcel komatu pa labi", [
        {"jaut": "Cik ir 2,5 · 10?",
         "atb": ["25"], "padoms": "Viena vieta pa labi."},
        {"jaut": "Cik ir 0,47 · 100?",
         "atb": ["47"], "padoms": "Divas vietas pa labi."},
        {"jaut": "Cik ir 1,2 · 1000?",
         "atb": ["1200"], "padoms": "Trīs vietas; beigās pieraksta nulles."},
        {"jaut": "Cik ir 0,003 · 1000?",
         "atb": ["3"], "padoms": "Trīs vietas pa labi."},
        {"jaut": "Cik ir 12,08 · 10?",
         "atb": ["120,8", "120.8"], "padoms": "Viena vieta pa labi."},
        {"jaut": "Cik ir 0,05 · 100?",
         "atb": ["5"], "padoms": "Divas vietas pa labi."},
    ], pamats=4,
        ievads="Nulles skaits reizinātājā ir soļu skaits."),

    Pasaule("Cik tālu tas ir tiešām?",
            Kustiba("", [
                {"jaut": "Kartē attālums ir 0,4 cm, mērogs 1 : 1000. Cik cm "
                         "tas ir dabā?",
                 "atb": 400, "beigas": 1000, "iedala": 200,
                 "mers": "centimetri", "merkis": "dabā", "objekts": "Mērītājs",
                 "padoms": "0,4 · 1000."},
                {"jaut": "Kartē 0,25 cm, mērogs 1 : 1000. Cik cm dabā?",
                 "atb": 250, "beigas": 1000, "iedala": 200,
                 "mers": "centimetri", "merkis": "dabā", "objekts": "Mērītājs",
                 "padoms": "0,25 · 1000."},
                {"jaut": "Detaļas zīmējumā 0,8 cm, palielinājums 100 reižu. "
                         "Cik cm dabā?",
                 "atb": 80, "beigas": 1000, "iedala": 200,
                 "mers": "centimetri", "merkis": "dabā", "objekts": "Mērītājs",
                 "padoms": "0,8 · 100."},
                {"jaut": "Mikroskopā 0,06 cm, palielinājums 10 000 reižu. "
                         "Cik cm ekrānā?",
                 "atb": 600, "beigas": 1000, "iedala": 200,
                 "mers": "centimetri", "merkis": "ekrānā",
                 "objekts": "Mērītājs",
                 "padoms": "0,06 · 10 000 - četras vietas pa labi."},
            ]),
            pavediens="tehnika",
            konteksts="Mēroga pārrēķins ir tieši reizināšana ar 10, 100 vai "
                      "1000 - komats pārceļas, cipari paliek.",
            kapec="Katra izlaista vieta nozīmē desmitkārtīgu kļūdu."),

    Petijums("Atrodi likumu pats",
             vajag="burtnīca un kalkulators",
             soli=[
                 "Izrēķini ar kalkulatoru 4,6 · 10; 4,6 · 100; 4,6 · 1000.",
                 "Pieraksti rezultātus vienu zem otra, līdzinot komatus.",
                 "Apvelc, par cik vietām komats pārcēlās katrā rindā.",
                 "Pieraksti likumu vienā teikumā.",
             ],
             secinajums="Komats pārceļas par tik vietām pa labi, cik nulles "
                        "ir reizinātājā."),

    Varianti("Cik vietas un uz kuru pusi?", [
        {"jaut": "Reizinot ar 1000, komats pārceļas...",
         "opcijas": ["par trim vietām pa labi",
                     "par trim vietām pa kreisi",
                     "par vienu vietu pa labi", "nekur"],
         "pareizi": 0,
         "padoms": "1000 ir trīs nulles."},
        {"jaut": "Cik ir 0,07 · 10?",
         "opcijas": ["0,7", "7", "0,007", "70"],
         "pareizi": 0,
         "padoms": "Viena vieta pa labi."},
        {"jaut": "Kāpēc skaitlis kļūst lielāks?",
         "opcijas": ["Jo reizinātājs ir lielāks par 1",
                     "Jo pieliek nulles",
                     "Jo komats pazūd", "Tas nekļūst lielāks"],
         "pareizi": 0,
         "padoms": "10 ir lielāks par 1."},
        {"jaut": "Cik ir 5 · 100?",
         "opcijas": ["500", "5,00", "0,05", "50"],
         "pareizi": 0,
         "padoms": "Veselam skaitlim komats ir aiz pēdējā cipara."},
    ], pamats=4),

    Kopsavilkums([
        "Reizinu ar 10, 100 un 1000, pārceļot komatu pa labi.",
        "Zinu, ka soļu skaits ir nuļļu skaits reizinātājā.",
        "Pierakstu nulles beigās, ja ciparu nepietiek.",
        "Pamatoju, kāpēc skaitlis kļūst lielāks.",
    ]),

    Majas([
        "Izrēķini 0,085 · 1000 un 6,4 · 100.",
        "Pārvērt savu augumu no metriem centimetros, izmantojot šo likumu.",
        "Pieraksti trīs mērvienību pārveidojumus, kuros reizina ar 1000.",
    ]),
]
