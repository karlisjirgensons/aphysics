# -*- coding: utf-8 -*-
"""5. klase, 32. stunda: «Kas ir pirmskaitlis?»

Definīcija, kas izriet no 30. stundas taisnstūriem: pirmskaitlim ir tikai
viens taisnstūris - viena rinda. Atsevišķi tiek runāts par 1, jo tieši tur
skolēni kļūdās visbiežāk, un iemesls nav kārtula, bet vienreizības prasība
sadalījumam pirmreizinātājos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kas ir pirmskaitlis?"

MERKIS = ("Mācīsimies nošķirt pirmskaitļus no saliktiem skaitļiem un "
          "skaidrot, kāpēc 1 nav ne viens, ne otrs.")

SATURS = [
    Sakums("Kāpēc no septiņiem taisnstūri neiznāk?",
           fakti=["7 rūtiņas var salikt tikai vienā rindā: 1 · 7.",
                  "12 rūtiņas - vairākos veidos: 2 · 6, 3 · 4.",
                  "Pirmie sauc par pirmskaitļiem, otrie - par saliktiem."]),

    Doma("Pirmskaitlim ir tieši divi dalītāji",
         "Pirmskaitlis dalās tikai ar 1 un pats ar sevi; saliktam skaitlim "
         "dalītāju ir vairāk.",
         soli=[
             "Paņem skaitli un mēģini to dalīt ar 2, 3, 5, 7...",
             "Ja neviens dalījums nav vesels - skaitlis ir pirmskaitlis.",
             "Ja kāds dalījums ir vesels - skaitlis ir salikts.",
             "Vispirms pārbaudi mazos dalītājus: 2, 3, 5 un 7.",
         ],
         pieze="Skaitlim 1 ir tikai viens dalītājs - pats 1. Tāpēc tas nav "
               "ne pirmskaitlis, ne salikts skaitlis. Ja 1 skaitītu par "
               "pirmskaitli, 6 varētu sadalīt gan kā 2 · 3, gan 1 · 2 · 3, "
               "gan 1 · 1 · 2 · 3 - sadalījums vairs nebūtu viens vienīgs."),

    Paraugs("Vai 51 ir pirmskaitlis?",
            uzd="Noskaidro, vai 51 ir pirmskaitlis.",
            soli=[
                ("Ar 2 nedalās - skaitlis ir nepāra",
                 "Pēdējais cipars ir 1."),
                ("Ar 3 dalās: 5 + 1 = 6, un 6 dalās ar 3",
                 "Ciparu summa ir dalāmības ar 3 pazīme."),
                ("51 : 3 = 17",
                 "Dalījums ir vesels skaitlis."),
                ("Dalītāji ir 1, 3, 17 un 51 - to ir četri",
                 "Vairāk nekā divi."),
            ],
            atbilde="51 nav pirmskaitlis: 51 = 3 · 17"),

    Ievadi("Pirmskaitlis vai salikts?", [
        {"jaut": "Cik dalītāju ir skaitlim 7?", "atb": ["2"],
         "padoms": "1 un 7."},
        {"jaut": "Cik dalītāju ir skaitlim 12?", "atb": ["6"],
         "padoms": "1, 2, 3, 4, 6, 12."},
        {"jaut": "Cik dalītāju ir skaitlim 1?", "atb": ["1"],
         "padoms": "Tikai pats 1."},
        {"jaut": "Kurš ir mazākais pirmskaitlis?", "atb": ["2"],
         "padoms": "1 neskaitās."},
        {"jaut": "Kurš ir vienīgais pāra pirmskaitlis?", "atb": ["2"],
         "padoms": "Visi pārējie pāra skaitļi dalās ar 2."},
        {"jaut": "Cik ir 51 : 3?", "atb": ["17"],
         "padoms": "Tāpēc 51 nav pirmskaitlis."},
        {"jaut": "Kurš pirmskaitlis seko tūlīt pēc 13?", "atb": ["17"],
         "padoms": "14, 15 un 16 ir salikti."},
        {"jaut": "Cik dalītāju ir skaitlim 23?", "atb": ["2"],
         "padoms": "23 ir pirmskaitlis."},
    ], pamats=4,
        ievads="Dalītāji ir visi skaitļi, ar kuriem skaitlis dalās bez "
               "atlikuma."),

    Varianti("Kur ir robeža?", [
        {"jaut": "Kurš skaitlis ir pirmskaitlis?",
         "opcijas": ["29", "27", "21", "33"],
         "pareizi": 0,
         "padoms": "Pārbaudi katru: vai dalās ar 3?"},
        {"jaut": "Kāpēc 1 nav pirmskaitlis?",
         "opcijas": ["Tam ir tikai viens dalītājs",
                     "Tas ir par mazu",
                     "Tas ir nepāra",
                     "Tas dalās ar visu"],
         "pareizi": 0,
         "padoms": "Pirmskaitlim jābūt tieši diviem dalītājiem."},
        {"jaut": "Kāpēc 2 ir vienīgais pāra pirmskaitlis?",
         "opcijas": ["Visi citi pāra skaitļi dalās ar 2",
                     "Jo 2 ir mazs",
                     "Jo 2 ir pirmais skaitlis",
                     "Tas nav vienīgais"],
         "pareizi": 0,
         "padoms": "4, 6, 8... katram ir dalītājs 2."},
        {"jaut": "Skaitlim ir tieši trīs dalītāji. Kas tas par skaitli?",
         "opcijas": ["Salikts - piemēram, 9", "Pirmskaitlis",
                     "Skaitlis 1", "Tāda skaitļa nav"],
         "pareizi": 0,
         "padoms": "9 dalītāji: 1, 3 un 9."},
    ], pamats=4),

    Pasaule("Kā sadalīt dēļus vienādi?",
            Ievadi("", [
                {"jaut": "13 dēļus liek rindās pa 4. Cik dēļu paliek pāri?",
                 "atb": ["1"], "padoms": "13 : 4 = 3, atlikums 1."},
                {"jaut": "12 dēļus 3 kaudzēs. Cik dēļu kaudzē?",
                 "atb": ["4"], "padoms": "12 : 3."},
                {"jaut": "Cik dalītāju ir skaitlim 24?",
                 "atb": ["8"], "padoms": "1, 2, 3, 4, 6, 8, 12, 24."},
                {"jaut": "Kurš skaitlis no 20 līdz 24 ir pirmskaitlis?",
                 "atb": ["23"], "padoms": "Pārējie dalās ar 2 vai 3."},
            ]),
            pavediens="maja",
            konteksts="Materiālu, kura daudzums ir pirmskaitlis, nevar "
                      "sadalīt vienādās daļās - paliek viena gara rinda.",
            kapec="Pirmskaitlis nesadalās, un tieši tas padara to "
                  "īpašu."),

    Kopsavilkums([
        "Nošķiru pirmskaitļus no saliktiem skaitļiem.",
        "Zinu, ka pirmskaitlim ir tieši divi dalītāji.",
        "Skaidroju, kāpēc 1 nav ne pirmskaitlis, ne salikts skaitlis.",
        "Pārbaudu, vai skaitlis ir pirmskaitlis, meklējot tā dalītājus.",
    ]),

    Majas([
        "Uzraksti visus pirmskaitļus līdz 30.",
        "Atrodi divus pirmskaitļus, kuru starpība ir 2.",
        "Paskaidro kādam mājās, kāpēc 1 nav pirmskaitlis.",
    ]),
]
