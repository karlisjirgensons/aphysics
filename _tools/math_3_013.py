# -*- coding: utf-8 -*-
"""3. klase, 13. stunda: «Kuri skaitļi dalās ar 5 un kuri ar 10?»

Pirmā dalāmības pazīme. Tā nav jauns rēķins, bet skatiens uz skaitli no
malas: pēdējais cipars pasaka atbildi, un pārējos var neskatīties. Simta
kvadrāts to padara redzamu - iekrāsotās rūtiņas sakārtojas kolonnās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kuri skaitļi dalās ar 5 un kuri ar 10?"

MERKIS = ("Atradīsim, pēc kā var uzreiz pateikt, vai skaitlis dalās ar 5 vai "
          "ar 10, un pamatosim to.")

SATURS = [
    Sakums("Vai var pateikt atbildi, neizrēķinot?",
           zimejums=restis([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                            [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                            [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]],
                           "simta kvadrāta pirmās trīs rindas"),
           paraksts="Skaitļi, kas dalās ar 5, sakrīt divās taisnās kolonnās.",
           fakti=["Skaitlis dalās ar 5, ja beidzas ar 0 vai 5.",
                  "Skaitlis dalās ar 10, ja beidzas ar 0.",
                  "Pārējie cipari šeit neko nemaina."]),

    Doma("Atbildi pasaka pēdējais cipars",
         "Ar 5 dalās skaitļi, kas beidzas ar 0 vai 5; ar 10 - tikai tie, kas "
         "beidzas ar 0.",
         soli=[
             "Paskaties tikai uz pēdējo ciparu.",
             "Ja tas ir 0 vai 5, skaitlis dalās ar 5.",
             "Ja tas ir 0, skaitlis dalās arī ar 10.",
             "Pārējos ciparus pārbaudīt nevajag.",
         ],
         pieze="Tas strādā tāpēc, ka visi desmiti jau dalās gan ar 5, gan ar "
               "10 - izšķir tikai tas, cik vienu ir pāri."),

    Paraugs("Vai 135 dalās ar 5?",
            uzd="Pārbaudi, vai 135 dalās ar 5 un vai tas dalās ar 10.",
            soli=[
                ("135 - pēdējais cipars ir 5",
                 "Skatās tikai uz pēdējo ciparu."),
                ("Dalās ar 5",
                 "Pēdējais cipars ir 5, tātad dalīšana iznāks bez atlikuma."),
                ("Ar 10 nedalās",
                 "Ar 10 dalās tikai tie skaitļi, kas beidzas ar 0."),
            ],
            atbilde="ar 5 dalās, ar 10 - nedalās"),

    Ievadi("Pārbaudi pēdējo ciparu", [
        {"jaut": "Vai 45 dalās ar 5? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Pēdējais cipars ir 5."},
        {"jaut": "Vai 72 dalās ar 5? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Pēdējais cipars nav ne 0, ne 5.",
         "tastatura": "text"},
        {"jaut": "Vai 90 dalās ar 10? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Pēdējais cipars ir 0.",
         "tastatura": "text"},
        {"jaut": "Cik ir 45 : 5?", "atb": ["9"], "padoms": "9 · 5 = 45."},
        {"jaut": "Cik ir 80 : 10?", "atb": ["8"], "padoms": "Noņem nulli."},
        {"jaut": "Cik ir 65 : 5?", "atb": ["13"],
         "padoms": "50 : 5 = 10 un 15 : 5 = 3."},
    ], pamats=4,
        ievads="Pirmajos uzdevumos raksti vārdu, pārējos - skaitli."),

    Petijums("Iekrāso simta kvadrātu",
             vajag="simta kvadrāts un divas krāsas",
             soli=[
                 "Uzzīmē 10 x 10 tabulu ar skaitļiem no 1 līdz 100.",
                 "Iekrāso visus skaitļus, kas dalās ar 5.",
                 "Ar otru krāsu apvelc tos, kas dalās arī ar 10.",
                 "Apraksti, kā iekrāsotās rūtiņas izkārtojušās.",
             ],
             secinajums="Sanāk divas taisnas kolonnas - tāpēc atbildi var "
                        "pateikt pēc pēdējā cipara vien."),

    Zimejums("Divas kolonnas",
             restis([[5, 10], [15, 20], [25, 30], [35, 40], [45, 50]],
                    "kreisā beidzas ar 5, labā ar 0"),
             paskaidro="Labās kolonnas skaitļi dalās gan ar 5, gan ar 10; "
                       "kreisās - tikai ar 5.",
             ievads="Tā izskatās piecnieku rinda, salikta pa pāriem."),

    Varianti("Kurš skaitlis der?", [
        {"jaut": "Kurš skaitlis dalās ar 10?",
         "opcijas": ["70", "75", "17", "105"],
         "pareizi": 0, "padoms": "Jābeidzas ar 0."},
        {"jaut": "Kurš skaitlis *nedalās* ar 5?",
         "opcijas": ["62", "60", "65", "55"],
         "pareizi": 0, "padoms": "Pēdējais cipars ir 2."},
        {"jaut": "Kurš apgalvojums ir patiess?",
         "opcijas": ["Katrs skaitlis, kas dalās ar 10, dalās arī ar 5",
                     "Katrs skaitlis, kas dalās ar 5, dalās arī ar 10",
                     "Neviens skaitlis nedalās ar abiem",
                     "Ar 10 dalās visi pāra skaitļi"],
         "pareizi": 0, "padoms": "10 pats sastāv no diviem pieciniekiem."},
        {"jaut": "Cik skaitļu no 1 līdz 50 dalās ar 10?",
         "opcijas": ["5", "10", "4", "50"],
         "pareizi": 0, "padoms": "10, 20, 30, 40, 50."},
    ], pamats=4),

    Pasaule("Kā samaksāt bez sīknaudas?",
            Ievadi("", [
                {"jaut": "Prece maksā 35 eiro. Cik piecu eiro naudas zīmju "
                         "vajag?",
                 "atb": ["7"], "padoms": "35 : 5."},
                {"jaut": "Prece maksā 60 eiro. Cik desmit eiro naudas zīmju "
                         "vajag?",
                 "atb": ["6"], "padoms": "60 : 10."},
                {"jaut": "Vai 48 eiro var samaksāt tikai ar piecu eiro "
                         "naudas zīmēm? Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"], "padoms": "48 nebeidzas ne ar 0, ne ar "
                                                "5.",
                 "tastatura": "text"},
                {"jaut": "Cik desmit eiro naudas zīmju vajag 90 eiro?",
                 "atb": ["9"], "padoms": "90 : 10."},
            ]),
            pavediens="veikals",
            konteksts="Naudas zīmes ir 5, 10, 20 un 50 eiro - tāpēc veikalā "
                      "dalāmība ar 5 un 10 ir redzama katru dienu.",
            kapec="Pēc pēdējā cipara uzreiz zini, vai sīknauda būs "
                  "vajadzīga."),

    Kopsavilkums([
        "Zinu dalāmības pazīmi ar 5 un ar 10.",
        "Pārbaudu to, skatoties tikai uz pēdējo ciparu.",
        "Zinu, ka katrs skaitlis, kas dalās ar 10, dalās arī ar 5.",
        "Lietoju pazīmi naudas un mērvienību uzdevumos.",
    ]),

    Majas([
        "Atrodi mājās piecus skaitļus, kas dalās ar 10.",
        "Paskaties uz mājas numuriem savā ielā - cik no tiem dalās ar 5?",
        "Uzraksti trīs skaitļus, kas dalās ar 5, bet ne ar 10.",
    ]),
]
