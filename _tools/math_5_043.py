# -*- coding: utf-8 -*-
"""5. klase, 43. stunda: «Kas ir bāze un kas - kāpinātājs?»

Nosaukumi diviem cipariem, kas jau pazīstami no 42. stundas. Nosaukumi paši
par sevi nav mērķis - tie vajadzīgi, lai varētu uzdot uzdevumu vārdos («bāze
ir 3, kāpinātājs 4») un lai pamanītu, cik dažādi rīkojas abi cipari.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas ir bāze un kas - kāpinātājs?"

MERKIS = ("Iemācīsimies nosaukt pakāpes elementus un veidot izteiksmes pēc "
          "apraksta.")

SATURS = [
    Sakums("Divi cipari, divas dažādas lomas",
           fakti=["Pierakstā 2⁵ lielais cipars ir bāze.",
                  "Mazais cipars augšā ir kāpinātājs.",
                  "Bāze pasaka, ko reizina; kāpinātājs - cik reižu."]),

    Doma("Bāze - ko reizina, kāpinātājs - cik reižu",
         "Samainot tos vietām, sanāk cits skaitlis: 2⁵ ir 32, bet 5² ir 25.",
         soli=[
             "Atrodi lielo ciparu - tā ir bāze.",
             "Atrodi mazo ciparu augšā - tas ir kāpinātājs.",
             "Izlasi: «bāze kāpinātāja pakāpē».",
             "Uzraksti reizinājumu: bāze, atkārtota kāpinātāja reižu skaitā.",
             "Izrēķini vērtību.",
         ],
         pieze="Kāpinātājs 1 nozīmē, ka reizinātājs ir viens pats: 7¹ = 7. "
               "Tāpēc parasti to neraksta - bet zināt to vajag."),

    Zimejums("Bāze tā pati, kāpinātājs cits",
             restis([["2¹", "2²", "2³", "2⁴"], [2, 4, 8, 16]],
                    "augšā pieraksts, apakšā vērtība"),
             paskaidro="Bāze visur ir 2. Katru reizi, kad kāpinātājs aug par "
                       "1, vērtība dubultojas.",
             ievads="Kāpinātājs aug pa vienam."),

    Paraugs("Uzraksti izteiksmi pēc apraksta",
            uzd="Bāze ir 3, kāpinātājs 4. Uzraksti pakāpi un izrēķini to.",
            soli=[
                ("Bāze 3 - lielais cipars",
                 "To reizina."),
                ("Kāpinātājs 4 - mazais cipars augšā",
                 "Tik reižu."),
                ("3⁴ = 3 · 3 · 3 · 3",
                 "Pieraksts un tā nozīme."),
                ("= 81",
                 "9 · 9 = 81."),
            ],
            atbilde="3⁴ = 81"),

    Ievadi("Bāze un kāpinātājs", [
        {"jaut": "Kāda ir bāze pierakstā 2⁵?", "atb": ["2"],
         "padoms": "Lielais cipars."},
        {"jaut": "Kāds ir kāpinātājs pierakstā 2⁵?", "atb": ["5"],
         "padoms": "Mazais cipars augšā."},
        {"jaut": "Bāze 3, kāpinātājs 4. Cik ir šīs pakāpes vērtība?",
         "atb": ["81"], "padoms": "3 · 3 · 3 · 3."},
        {"jaut": "Bāze 5, kāpinātājs 2. Cik ir vērtība?", "atb": ["25"],
         "padoms": "5 · 5."},
        {"jaut": "Cik ir 2⁵?", "atb": ["32"], "padoms": "Divnieks piecas "
                                                        "reizes."},
        {"jaut": "Cik ir 5²?", "atb": ["25"],
         "padoms": "Pavisam cits skaitlis nekā 2⁵."},
        {"jaut": "Cik ir 7¹?", "atb": ["7"],
         "padoms": "Viens vienīgs reizinātājs."},
        {"jaut": "Bāze 10, kāpinātājs 4. Cik ir vērtība?", "atb": ["10000"],
         "padoms": "Tik nulles, cik kāpinātājs."},
    ], pamats=4,
        ievads="Bāze - ko reizina; kāpinātājs - cik reižu."),

    Varianti("Kurš cipars ko nozīmē?", [
        {"jaut": "Pierakstā 4³ skaitlis 3 ir...",
         "opcijas": ["kāpinātājs", "bāze", "reizinājums", "dalītājs"],
         "pareizi": 0,
         "padoms": "Mazais cipars augšā."},
        {"jaut": "Vai 2⁵ un 5² ir viens un tas pats?",
         "opcijas": ["Nē: 32 un 25", "Jā, abi ir 32", "Jā, abi ir 25",
                     "Nē: 25 un 32"],
         "pareizi": 0,
         "padoms": "Izrēķini abus."},
        {"jaut": "Kāpēc 10⁴ ir 10 000?",
         "opcijas": ["Katrs desmitnieks pieliek vienu nulli",
                     "Jo 10 · 4 = 40",
                     "Jo 4 nulles ir vienmēr",
                     "Tā nav taisnība"],
         "pareizi": 0,
         "padoms": "10 · 10 = 100, 100 · 10 = 1 000..."},
        {"jaut": "Ko nozīmē kāpinātājs 1?",
         "opcijas": ["Reizinātājs ir viens pats", "Vērtība ir 1",
                     "Bāze pazūd", "Tāda nav"],
         "pareizi": 0,
         "padoms": "7¹ = 7."},
    ], pamats=4),

    Pasaule("Cik failu ietilpst?",
            Ievadi("", [
                {"jaut": "Mapē ir 10³ faili. Cik tas ir?", "atb": ["1000"],
                 "padoms": "Trīs nulles."},
                {"jaut": "Ekrānā 2¹⁰ punktu rindā. Cik tas ir?",
                 "atb": ["1024"], "padoms": "Divnieks desmit reizes."},
                {"jaut": "Krāsu ir 2⁸. Cik tas ir?", "atb": ["256"],
                 "padoms": "2⁴ · 2⁴."},
                {"jaut": "Cik ir 10⁶ - tik baitu ir megabaitā pēc apaļā "
                         "rēķina?",
                 "atb": ["1000000"], "padoms": "Sešas nulles."},
            ]),
            pavediens="dati",
            konteksts="Datoros gandrīz viss skaitās divnieka pakāpēs, bet "
                      "cilvēki runā desmitnieka pakāpēs.",
            kapec="Bāze pasaka, kas dubultojas vai desmitkāršojas."),

    Kopsavilkums([
        "Nosaucu pakāpes elementus: bāzi un kāpinātāju.",
        "Veidoju pakāpi pēc apraksta vārdos.",
        "Zinu, ka 2⁵ un 5² ir dažādi skaitļi.",
        "Zinu, ko nozīmē kāpinātājs 1.",
    ]),

    Majas([
        "Uzraksti trīs pakāpes ar bāzi 2 un trīs ar kāpinātāju 2.",
        "Izrēķini tās un salīdzini, kuras aug ātrāk.",
        "Pastāsti kādam mājās, kāpēc 2⁵ nav 5².",
    ]),
]
