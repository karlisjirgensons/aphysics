# -*- coding: utf-8 -*-
"""5. klase, 36. stunda: «Kā atrast visus dalītājus?»

34. stundas sadalījums te sāk strādāt: dalītājus vairs nemeklē pēc kārtas,
bet saliek no pirmreizinātājiem. Blakus paliek arī pāru paņēmiens, jo tas
pats pasaka, kad meklēšanu drīkst pārtraukt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā atrast visus dalītājus?"

MERKIS = ("Iemācīsimies noteikt visus skaitļa dalītājus, izmantojot pārus un "
          "sadalījumu pirmreizinātājos.")

SATURS = [
    Sakums("Vai visi dalītāji ir atrasti?",
           fakti=["24 dalās ar 1, 2, 3, 4, 6, 8, 12 un 24.",
                  "Tie ir astoņi, un neviena vairs nav.",
                  "Bet kā zināt, ka neviens nav palaists garām?"]),

    Doma("Dalītāji nāk pāros",
         "Katram dalītājam ir savs pāris: ja a ir dalītājs, tad arī "
         "skaitlis : a ir dalītājs.",
         soli=[
             "Sāc ar 1 un pieraksti tā pāri - pašu skaitli.",
             "Pārbaudi 2, tad 3, tad 4 un tā tālāk.",
             "Katram atrastajam dalītājam pieraksti arī tā pāri.",
             "Beidz, kad pāri sāk atkārtoties.",
             "Sakārto visus atrastos dalītājus pēc lieluma.",
         ],
         pieze="Skaitlim 36 pāri ir 1 un 36, 2 un 18, 3 un 12, 4 un 9, 6 un "
               "6. Pēdējais pāris ir viens un tas pats skaitlis, tāpēc "
               "dalītāju ir nevis desmit, bet deviņi."),

    Paraugs("Visi 36 dalītāji",
            uzd="Atrodi visus skaitļa 36 dalītājus.",
            soli=[
                ("1 un 36",
                 "Pirmais pāris ir vienmēr."),
                ("2 un 18, 3 un 12",
                 "36 dalās gan ar 2, gan ar 3."),
                ("4 un 9",
                 "36 : 4 = 9."),
                ("6 un 6 - pāris sakrīt",
                 "Te meklēšanu var beigt."),
                ("1, 2, 3, 4, 6, 9, 12, 18, 36",
                 "Deviņi dalītāji."),
            ],
            atbilde="36 dalītāji: 1, 2, 3, 4, 6, 9, 12, 18 un 36"),

    Ievadi("Saskaiti dalītājus", [
        {"jaut": "Cik dalītāju ir skaitlim 24?", "atb": ["8"],
         "padoms": "1, 2, 3, 4, 6, 8, 12, 24."},
        {"jaut": "Cik dalītāju ir skaitlim 36?", "atb": ["9"],
         "padoms": "Pāris 6 un 6 sakrīt."},
        {"jaut": "Cik dalītāju ir skaitlim 12?", "atb": ["6"],
         "padoms": "1, 2, 3, 4, 6, 12."},
        {"jaut": "Kāds ir skaitļa 24 dalītāja 3 pāris?", "atb": ["8"],
         "padoms": "24 : 3."},
        {"jaut": "Kāds ir skaitļa 100 dalītāja 4 pāris?", "atb": ["25"],
         "padoms": "100 : 4."},
        {"jaut": "Cik dalītāju ir skaitlim 13?", "atb": ["2"],
         "padoms": "Pirmskaitlim vienmēr divi."},
        {"jaut": "Kurš ir lielākais skaitļa 45 dalītājs, kas mazāks par 45?",
         "atb": ["15"], "padoms": "45 : 3."},
        {"jaut": "Cik dalītāju ir skaitlim 16?", "atb": ["5"],
         "padoms": "1, 2, 4, 8, 16 - pāris 4 un 4 sakrīt."},
    ], pamats=4,
        ievads="Dalītāji nāk pāros - pieraksti abus uzreiz."),

    Varianti("Kad meklēšanu var beigt?", [
        {"jaut": "Kad dalītāju meklēšanu drīkst pārtraukt?",
         "opcijas": ["Kad pāri sāk atkārtoties",
                     "Kad atrasti pieci dalītāji",
                     "Kad sasniegta puse no skaitļa",
                     "Nekad - jāpārbauda visi"],
         "pareizi": 0,
         "padoms": "36 gadījumā tas notiek pie 6 un 6."},
        {"jaut": "Kāpēc skaitlim 36 ir nepāra skaits dalītāju?",
         "opcijas": ["Jo viens pāris sakrīt: 6 un 6",
                     "Jo 36 ir pāra skaitlis",
                     "Jo 36 ir liels",
                     "Tā ir kļūda"],
         "pareizi": 0,
         "padoms": "36 = 6 · 6."},
        {"jaut": "Kuri divi dalītāji ir katram skaitlim?",
         "opcijas": ["1 un pats skaitlis", "1 un 2", "2 un 3",
                     "Pats skaitlis un 0"],
         "pareizi": 0,
         "padoms": "Šie divi ir vienmēr."},
        {"jaut": "Skaitlim ir tieši divi dalītāji. Kas tas par skaitli?",
         "opcijas": ["Pirmskaitlis", "Pāra skaitlis", "Kvadrāts",
                     "Skaitlis 1"],
         "pareizi": 0,
         "padoms": "Tikai 1 un pats skaitlis."},
    ], pamats=4),

    Pasaule("Kā sadalīt ceļu vienādos posmos?",
            Ievadi("", [
                {"jaut": "Ceļš ir 36 km. Cik kilometru ir vienā posmā, ja "
                         "posmu ir 4?",
                 "atb": ["9"], "padoms": "36 : 4."},
                {"jaut": "Cik posmu sanāk, ja katrs ir 6 km?",
                 "atb": ["6"], "padoms": "36 : 6."},
                {"jaut": "Vai 36 km var sadalīt 5 vienādos veselos posmos? "
                         "Raksti atlikumu kilometros.",
                 "atb": ["1"], "padoms": "36 : 5 = 7, atlikums 1."},
                {"jaut": "Ceļš 24 km, atpūtas vietas ik pēc 8 km. Cik "
                         "atpūtas vietu sanāk ceļā, ieskaitot galapunktu?",
                 "atb": ["3"], "padoms": "24 : 8."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojumā attālumu dala posmos - un posma garumam "
                      "jābūt ceļa dalītājam, citādi pēdējais posms ir citāds.",
            kapec="Dalītāji ir tieši tie posmu garumi, kas sadalās bez "
                  "atlikuma."),

    Kopsavilkums([
        "Atrodu visus skaitļa dalītājus, meklējot tos pāros.",
        "Zinu, kad meklēšanu var pārtraukt.",
        "Lietoju sadalījumu pirmreizinātājos, lai neko nepalaistu garām.",
        "Zinu, ka 1 un pats skaitlis ir dalītāji vienmēr.",
    ]),

    Majas([
        "Atrodi visus skaitļa 48 dalītājus un saskaiti tos.",
        "Atrodi skaitli līdz 50 ar visvairāk dalītājiem.",
        "Atrodi trīs skaitļus, kuriem ir nepāra skaits dalītāju.",
    ]),
]
