# -*- coding: utf-8 -*-
"""6. klase, 140. stunda: «Kur radusies kļūda?»

Mikrotemata noslēgums. Kļūdas ar negatīviem skaitļiem ir paredzamas: pazūd
zīme, aizmirstas iekavas, sajaukta atņemšana ar pieskaitīšanu. Kad tās ir
nosauktas vārdā, tās kļūst vieglāk pamanīt arī savā darbā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kur radusies kļūda?"

MERKIS = ("Izvērtēsim cita risinājumu un raksturosim kļūdas cēloni.")

SATURS = [
    Sakums("Trīs kļūdas, kas atkārtojas",
           zimejums=restis([["−5 − (−3) = −8", "−5 + 3 = −8", "5 − 8 = 3"],
                            ["zīme", "iekavas", "secība"]]),
           paraksts="Visas trīs ir nepareizas, un katrai ir savs cēlonis.",
           fakti=["Pazudusi zīme ir biežākā kļūda.",
                  "Aizmirstas iekavas maina darbības nozīmi.",
                  "Sajaukta secība: 5 − 8 nav tas pats, kas 8 − 5."]),

    Doma("Nosauc kļūdu vārdā",
         "Kļūdu meklē pa soļiem: vispirms novērtē, kādai jābūt zīmei, tad "
         "pārbauda katru soli un nosauc kļūdas cēloni.",
         soli=[
             "Novērtē, kāda zīme būtu jābūt atbildei.",
             "Salīdzini to ar doto atbildi.",
             "Pārbaudi katru soli no sākuma.",
             "Atrodi pirmo soli, kurā rezultāts nesakrīt.",
             "Nosauc cēloni: zīme, iekavas vai secība.",
         ],
         pieze="Nepareiza zīme visbiežāk nozīmē, ka atņemšana nav pārrakstīta "
               "par saskaitīšanu. Tāpēc, meklējot kļūdu, vispirms pārbauda "
               "tieši šo soli."),

    Paraugs("Atrodi kļūdu",
            uzd="Skolēns rēķina: −5 − (−3) = −8. Kur ir kļūda?",
            soli=[
                ("Novērtējums: atņemam negatīvu, tātad rezultātam jāaug",
                 "−8 ir mazāks par −5 - aizdomīgi."),
                ("Pareizi: −5 − (−3) = −5 + 3",
                 "Divas maiņas reizē."),
                ("= −2",
                 "3 soļi pa labi no −5."),
                ("Kļūdas cēlonis: mazinātāja zīme nav mainīta",
                 "Skolēns saskaitīja, nemainot zīmi."),
            ],
            atbilde="pareizi ir −2; kļūda ir nemainītā zīmē"),

    Ievadi("Izlabo kļūdaino atbildi", [
        {"jaut": "Skolēns: −5 − (−3) = −8. Kāda ir pareizā atbilde?",
         "atb": ["-2", "−2"], "padoms": "−5 + 3."},
        {"jaut": "Skolēns: −5 + 3 = −8. Kāda ir pareizā atbilde?",
         "atb": ["-2", "−2"], "padoms": "Zīmes atšķiras - moduļus atņem."},
        {"jaut": "Skolēns: 5 − 8 = 3. Kāda ir pareizā atbilde?",
         "atb": ["-3", "−3"], "padoms": "Secība ir svarīga."},
        {"jaut": "Skolēns: −4 − 6 = 2. Kāda ir pareizā atbilde?",
         "atb": ["-10", "−10"], "padoms": "Abas bultiņas pa kreisi."},
        {"jaut": "Skolēns: 7 + (−9) = 16. Kāda ir pareizā atbilde?",
         "atb": ["-2", "−2"], "padoms": "Zīmes atšķiras."},
        {"jaut": "Skolēns: −3 − (−3) = −6. Kāda ir pareizā atbilde?",
         "atb": ["0"], "padoms": "Pretēju skaitļu starpība."},
    ], pamats=4,
        ievads="Vispirms pasaki, kādai jābūt zīmei."),

    Varianti("Kāds ir kļūdas cēlonis?", [
        {"jaut": "−5 − (−3) = −8. Kāds ir cēlonis?",
         "opcijas": ["Mazinātāja zīme nav mainīta",
                     "Nepareizi saskaitīti moduļi",
                     "Sajaukta secība", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Atņemt negatīvu nozīmē pieskaitīt."},
        {"jaut": "5 − 8 = 3. Kāds ir cēlonis?",
         "opcijas": ["Sajaukta mazināmā un mazinātāja secība",
                     "Pazudusi iekava",
                     "Nepareizi saskaitīti moduļi", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Rēķināts 8 − 5."},
        {"jaut": "−4 − 6 = 2. Kāds ir cēlonis?",
         "opcijas": ["Moduļi atņemti, lai gan zīmes vienādas",
                     "Pazudusi iekava",
                     "Sajaukta secība", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Vienādas zīmes - moduļus saskaita."},
        {"jaut": "Ar ko sāk kļūdas meklēšanu?",
         "opcijas": ["Ar zīmes novērtēšanu", "Ar pārrēķināšanu",
                     "Ar pēdējo soli", "Ar jaunu risinājumu"],
         "pareizi": 0,
         "padoms": "Nepareiza zīme redzama uzreiz."},
    ], pamats=4),

    Petijums("Pārbaudi soļabiedra darbu",
             vajag="divu skolēnu risinājumi",
             soli=[
                 "Samainieties burtnīcām.",
                 "Katram uzdevumam vispirms novērtē atbildes zīmi.",
                 "Atrodi pirmo soli, kurā rezultāts nesakrīt.",
                 "Pieraksti kļūdas cēloni vienā no trim vārdiem: zīme, "
                 "iekavas, secība.",
                 "Pārrunājiet, kura kļūda bija biežākā.",
             ],
             secinajums="Lielākā daļa kļūdu ar negatīviem skaitļiem ir viena "
                        "no trim - un tās var iemācīties pamanīt."),

    Pasaule("Vai bankas izraksts ir pareizs?",
            Ievadi("", [
                {"jaut": "Bija −80 €, iemaksāja 50 €, izrakstā rakstīts "
                         "−130 €. Kāda ir pareizā summa?",
                 "atb": ["-30", "−30"], "padoms": "−80 + 50."},
                {"jaut": "Bija 40 €, atcēla maksājumu 15 € jeb atņēma −15 €. "
                         "Kāda ir pareizā summa?",
                 "atb": ["55"], "padoms": "40 + 15."},
                {"jaut": "Bija −20 €, rēķins 35 €. Kāda ir pareizā summa?",
                 "atb": ["-55", "−55"], "padoms": "−20 − 35."},
                {"jaut": "Bija −55 €, iemaksāja 55 €. Kāda ir summa?",
                 "atb": ["0"], "padoms": "Pretēji skaitļi."},
            ]),
            pavediens="veikals",
            konteksts="Kļūdu izrakstā pamana tas, kurš prot novērtēt, kādai "
                      "jābūt zīmei.",
            kapec="Nepareiza zīme ir pamanāma pirms jebkura rēķina."),

    Kopsavilkums([
        "Izvērtēju cita risinājumu pa soļiem.",
        "Sāku ar atbildes zīmes novērtēšanu.",
        "Atrodu pirmo kļūdaino soli.",
        "Nosaucu kļūdas cēloni: zīme, iekavas vai secība.",
    ]),

    Majas([
        "Atrodi savā vecā darbā kļūdu ar negatīvu skaitli.",
        "Pieraksti tās cēloni vienā vārdā.",
        "Uzraksti kādam uzdevumu ar apzinātu kļūdu un palūdz to atrast.",
    ]),
]
