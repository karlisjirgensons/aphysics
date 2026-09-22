# -*- coding: utf-8 -*-
"""5. klase, 33. stunda: «Kā atrast pirmskaitļus?»

Eratostena sieta stunda. Pirmskaitļus te nemeklē pa vienam, bet svītro visus
saliktos - un tieši tāpēc no attēla pašam kļūst redzams, kāpēc pirmskaitļu
tālāk paliek arvien mazāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā atrast pirmskaitļus?"

MERKIS = ("Mācīsimies meklēt un pierakstīt pirmskaitļus, pārbaudot dalāmību "
          "vai svītrojot saliktos skaitļus.")

SATURS = [
    Sakums("Kā atrast visus pirmskaitļus uzreiz?",
           zimejums=restis([[1, 2, 3, 4, 5, 6],
                            [7, 8, 9, 10, 11, 12],
                            [13, 14, 15, 16, 17, 18]]),
           paraksts="Skaitļi no 1 līdz 18. Kurus var izsvītrot?",
           fakti=["Pa vienam pārbaudīt ir gari.",
                  "Ātrāk ir izsvītrot visus, kas kādam dalās."]),

    Doma("Svītro reizinājumus, paliek pirmskaitļi",
         "Katrs saliktais skaitlis ir kāda mazāka skaitļa reizinājums - "
         "tāpēc tos var izsvītrot pa rindām.",
         soli=[
             "Izsvītro 1 - tas nav pirmskaitlis.",
             "Atstāj 2, bet izsvītro visus pārējos pāra skaitļus.",
             "Atstāj 3, bet izsvītro 6, 9, 12, 15...",
             "Atstāj 5, bet izsvītro 10, 15, 20...",
             "Kas palicis neizsvītrots, tie ir pirmskaitļi.",
         ],
         pieze="Šo paņēmienu pirms vairāk nekā 2 000 gadiem izdomāja grieķu "
               "zinātnieks Eratostens, un to joprojām sauc par Eratostena "
               "sietu: skaitļi tiek izsijāti, paliek tikai pirmskaitļi."),

    Zimejums("Kas paliek pēc sijāšanas",
             restis([[2, 3, 5, 7], [11, 13, 17, 19]]),
             paskaidro="Visi pirmskaitļi līdz 20 - to ir astoņi.",
             ievads="Kad izsvītroti visi 2, 3 un 5 reizinājumi."),

    Paraugs("Izsijā skaitļus līdz 20",
            uzd="Atrodi visus pirmskaitļus no 1 līdz 20.",
            soli=[
                ("Svītro 1",
                 "Tam ir tikai viens dalītājs."),
                ("Paliek 2, svītro 4, 6, 8, 10, 12, 14, 16, 18, 20",
                 "Visi pāra skaitļi, izņemot pašu 2."),
                ("Paliek 3, svītro 9 un 15",
                 "6, 12 un 18 jau izsvītroti."),
                ("Paliek 5 un 7 - to reizinājumi jau izsvītroti",
                 "10, 15 un 20 nosvītroja 2 un 3."),
                ("Palikuši: 2, 3, 5, 7, 11, 13, 17, 19",
                 "Astoņi pirmskaitļi."),
            ],
            atbilde="2, 3, 5, 7, 11, 13, 17, 19"),

    Ievadi("Pārbaudi dalāmību", [
        {"jaut": "Cik pirmskaitļu ir no 1 līdz 20?", "atb": ["8"],
         "padoms": "2, 3, 5, 7, 11, 13, 17, 19."},
        {"jaut": "Cik pirmskaitļu ir no 1 līdz 10?", "atb": ["4"],
         "padoms": "2, 3, 5, 7."},
        {"jaut": "Kurš ir lielākais pirmskaitlis, kas mazāks par 30?",
         "atb": ["29"], "padoms": "28 un 27 ir salikti."},
        {"jaut": "Ar kuru skaitli dalās 21? Nosauc dalītāju, kas nav 1 un "
                 "nav 21.",
         "atb": ["3", "7"], "padoms": "2 + 1 = 3, tāpēc dalās ar 3."},
        {"jaut": "Ar kuru mazāko skaitli, lielāku par 1, dalās 91?",
         "atb": ["7"], "padoms": "91 = 7 · 13."},
        {"jaut": "Cik pirmskaitļu ir starp 20 un 30?", "atb": ["2"],
         "padoms": "23 un 29."},
        {"jaut": "Vai 39 ir pirmskaitlis? Ja nē, nosauc tā dalītāju, kas nav "
                 "1 un nav 39.",
         "atb": ["3", "13"], "padoms": "3 + 9 = 12, tāpēc dalās ar 3."},
        {"jaut": "Cik pirmskaitļu ir no 1 līdz 30?", "atb": ["10"],
         "padoms": "Astoņiem līdz 20 pievieno 23 un 29."},
    ], pamats=4,
        ievads="Ja skaitlis dalās ar kaut ko citu, tas nav pirmskaitlis."),

    Varianti("Kā strādā siets?", [
        {"jaut": "Kāpēc pēc 2 izsvītrošanas var izlaist 4, 6 un 8?",
         "opcijas": ["Tie jau ir izsvītroti kā 2 reizinājumi",
                     "Tie ir pirmskaitļi",
                     "Tie ir par maziem",
                     "Tos svītro vēlāk"],
         "pareizi": 0,
         "padoms": "Katrs pāra skaitlis ir 2 reizinājums."},
        {"jaut": "Kāpēc 1 izsvītro uzreiz?",
         "opcijas": ["Tas nav pirmskaitlis",
                     "Tas ir salikts skaitlis",
                     "Tas dalās ar 2",
                     "Tas ir lielākais dalītājs"],
         "pareizi": 0,
         "padoms": "Tam ir tikai viens dalītājs."},
        {"jaut": "Skaitlis beidzas ar 5 un ir lielāks par 5. Vai tas ir "
                 "pirmskaitlis?",
         "opcijas": ["Nē, tas dalās ar 5", "Jā, vienmēr",
                     "Tikai tad, ja ir nepāra", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "15, 25, 35 - visi dalās ar 5."},
        {"jaut": "Kāpēc pirmskaitļu tālāk paliek arvien mazāk?",
         "opcijas": ["Jo lieliem skaitļiem ir vairāk iespējamo dalītāju",
                     "Jo lieli skaitļi ir pāra",
                     "Jo tie beidzas",
                     "Tas nav tiesa"],
         "pareizi": 0,
         "padoms": "Jo vairāk skaitļu pa priekšu, jo vairāk sietu."},
    ], pamats=4),

    Pasaule("Cik gabalos nesadalās?",
            Ievadi("", [
                {"jaut": "Dēļu ir 29, liek rindās pa 4. Cik dēļu paliek "
                         "pāri?",
                 "atb": ["1"], "padoms": "29 : 4 = 7, atlikums 1."},
                {"jaut": "Flīžu ir 21, rindā pa 3. Cik rindu?",
                 "atb": ["7"], "padoms": "21 : 3."},
                {"jaut": "Skrūvju ir 91, paciņā pa 7. Cik paciņu?",
                 "atb": ["13"], "padoms": "91 : 7."},
                {"jaut": "Podiņu ir 23. Cik podiņu paliek pāri, liekot "
                         "rindās pa 5?",
                 "atb": ["3"], "padoms": "23 : 5 = 4, atlikums 3."},
            ]),
            pavediens="maja",
            konteksts="Veikalā materiālu pako pa 6, 10 vai 12 - pirmskaitļi "
                      "iepakojumos gandrīz nekad neparādās.",
            kapec="Skaitlis, kas nedalās, vienmēr atstāj atlikumu."),

    Kopsavilkums([
        "Meklēju pirmskaitļus, izsvītrojot saliktos skaitļus.",
        "Pārbaudu dalāmību ar 2, 3, 5 un 7.",
        "Uzrakstu visus pirmskaitļus līdz 30.",
        "Saprotu, kāpēc pirmskaitļu tālāk kļūst arvien mazāk.",
    ]),

    Majas([
        "Uzraksti skaitļus no 1 līdz 50 un izsijā tos ar Eratostena sietu.",
        "Saskaiti, cik pirmskaitļu palika.",
        "Atrodi, starp kuriem diviem pirmskaitļiem ir vislielākā atstarpe.",
    ]),
]
