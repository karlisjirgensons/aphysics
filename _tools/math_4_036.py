# -*- coding: utf-8 -*-
"""4. klase, 36. stunda: «Kuri skaitļi dalās ar 2, 3, 5 un 9?»

Mikrotemata noslēgums un mazs pētījums: skolēns pats pamana pazīmes no
piemēriem. Ar 2 un 5 izšķir pēdējais cipars, ar 3 un 9 - ciparu summa.
Pazīmes vēl nepierāda (to dara 5. klasē), bet pamato ar piemēriem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kuri skaitļi dalās ar 2, 3, 5 un 9?"

MERKIS = ("Aplūkosim piemērus, formulēsim dalāmības pazīmes ar 2, 3, 5 un 9 "
          "un pamatosim savus spriedumus.")

SATURS = [
    Sakums("Vai 3 bērni var godīgi sadalīt 1236 kartiņas?",
           zimejums=restis([["ar 2", "pēdējais cipars pāra"],
                            ["ar 5", "pēdējais cipars 0 vai 5"],
                            ["ar 3", "ciparu summa dalās ar 3"],
                            ["ar 9", "ciparu summa dalās ar 9"]],
                           "dalāmības pazīmes"),
           paraksts="Var uzzināt, vai dalās, pat neizdalot!",
           fakti=["Dalāmības pazīme ir īsceļš - bez dalīšanas.",
                  "1236: 1 + 2 + 3 + 6 = 12 - dalās ar 3."]),

    Doma("Pēdējais cipars vai ciparu summa pasaka priekšā",
         "Ar 2 un 5 skatās pēdējo ciparu; ar 3 un 9 - visu ciparu summu.",
         soli=[
             "Dalās ar 2, ja pēdējais cipars ir 0, 2, 4, 6 vai 8.",
             "Dalās ar 5, ja pēdējais cipars ir 0 vai 5.",
             "Dalās ar 3, ja ciparu summa dalās ar 3.",
             "Dalās ar 9, ja ciparu summa dalās ar 9.",
         ],
         pieze="Kas dalās ar 9, tas dalās arī ar 3 - bet ne otrādi: "
               "12 dalās ar 3, bet ne ar 9."),

    Paraugs("Vai 4185 dalās ar 9?",
            uzd="Pārbaudi, vai 4185 dalās ar 2, 3, 5 un 9.",
            soli=[
                ("pēdējais cipars 5", "Ar 2 nedalās, ar 5 dalās."),
                ("4 + 1 + 8 + 5 = 18", "Ciparu summa."),
                ("18 dalās ar 9 un ar 3", "Tātad 4185 dalās ar 3 un 9."),
            ],
            atbilde="dalās ar 3, 5 un 9; ar 2 nedalās"),

    Petijums("Atklāj pazīmi pats",
             soli=[
                 "Uzraksti skaitļus 3, 6, 9, 12, ..., 60 (reizinājumi ar 3).",
                 "Katram saskaiti ciparus: 1 + 2 = 3, 1 + 5 = 6, ...",
                 "Ko pamani? Vai ciparu summa arī ir reizinājums ar 3?",
                 "Atkārto ar 9, 18, 27, ... 90.",
             ],
             vajag="burtnīca, zīmulis",
             secinajums="Reizinājumu ar 3 ciparu summa dalās ar 3, ar 9 - "
                        "dalās ar 9."),

    Ievadi("Pārbaudi pēc pazīmes", [
        {"jaut": "Kāda ir skaitļa 2718 ciparu summa?", "atb": ["18"],
         "padoms": "2 + 7 + 1 + 8."},
        {"jaut": "Kāds cipars jāieliek 43☐, lai dalītos ar 5 un 2?",
         "atb": ["0"], "padoms": "Beigās 0."},
        {"jaut": "Mazākais cipars, ko ielikt 5☐1, lai dalītos ar 3?",
         "atb": ["0"], "padoms": "5 + 0 + 1 = 6."},
        {"jaut": "Kāds cipars jāieliek 7☐2, lai dalītos ar 9?",
         "atb": ["0", "9"], "padoms": "7 + ☐ + 2 = 9 vai 18."},
    ]),

    Varianti("Dalās vai nedalās?", [
        {"jaut": "Vai 3456 dalās ar 2?",
         "opcijas": ["jā", "nē"], "pareizi": 0, "padoms": "Beigās 6."},
        {"jaut": "Vai 1001 dalās ar 3?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "1 + 0 + 0 + 1 = 2."},
        {"jaut": "Kurš skaitlis dalās ar 9?",
         "opcijas": ["5058", "5050", "5005", "5500"], "pareizi": 0,
         "padoms": "5 + 0 + 5 + 8 = 18."},
        {"jaut": "Kurš skaitlis dalās gan ar 2, gan ar 5?",
         "opcijas": ["730", "735", "732", "725"], "pareizi": 0,
         "padoms": "Beigās 0."},
        {"jaut": "Vai tas, kas dalās ar 3, noteikti dalās ar 9?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "6 dalās ar 3, bet ne ar 9."},
        {"jaut": "Kurš skaitlis dalās ar 3, bet ne ar 9?",
         "opcijas": ["21", "18", "27", "36"], "pareizi": 0,
         "padoms": "2 + 1 = 3."},
    ], pamats=4),

    Zimejums("Kurš ar ko dalās",
             restis([["skaitlis", ": 2", ": 3", ": 5", ": 9"],
                     ["90", "jā", "jā", "jā", "jā"],
                     ["75", "nē", "jā", "jā", "nē"],
                     ["64", "jā", "nē", "nē", "nē"]],
                    "pazīmes darbībā"),
             paskaidro="90 dalās ar visiem četriem: beigās 0 un 9 + 0 = 9.",
             ievads="Viena tabula - četras pazīmes."),

    Pasaule("Kartiņu sadalīšana",
            Ievadi("", [
                {"jaut": "1236 kartiņas - vai tās var sadalīt 3 bērniem "
                         "vienādi? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "tastatura": "text",
                 "padoms": "1 + 2 + 3 + 6 = 12."},
                {"jaut": "Cik kartiņu katram no 3?",
                 "atb": ["412"], "padoms": "1236 : 3."},
                {"jaut": "Vai 1236 var sadalīt 5 bērniem vienādi? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["nē", "ne"], "tastatura": "text",
                 "padoms": "Beigās 6."},
                {"jaut": "Mazākais kartiņu skaits, kas jāpieliek pie 1236, "
                         "lai sadalītu 9 bērniem?",
                 "atb": ["6"], "padoms": "Summa 12 → 18."},
            ]),
            pavediens="skola",
            konteksts="Kolekcionāri dala kartiņas godīgi - un pazīme ļauj "
                      "uzzināt, vai tas izdosies, pirms sāk skaitīt.",
            kapec="Pazīme ietaupa laiku - dalīt nav jāsāk."),

    Kopsavilkums([
        "Zinu dalāmības pazīmes ar 2, 3, 5 un 9.",
        "Pārbaudu dalāmību bez dalīšanas.",
        "Pamatoju spriedumu ar piemēriem.",
    ]),

    Majas([
        "Pārbaudi, ar ko dalās tavs dzimšanas gads.",
        "Atrodi četrciparu skaitli, kas dalās ar 2, 3, 5 un 9 vienlaikus.",
        "Paskaidro mājiniekiem, kā pārbaudīt dalāmību ar 9.",
    ]),
]
