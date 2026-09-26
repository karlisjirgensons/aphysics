# -*- coding: utf-8 -*-
"""7. klase, 32. stunda: «Kā izskatās strukturēts risinājums?»

Eksāmenā vērtē ne tikai atbildi, bet arī pierakstu: kas dots, kas
jāatrod, kādi soļi un kāpēc. Stunda iemāca risinājuma uzbūvi «dots - jāatrod
- risinājums ar pamatojumu - atbilde» un liek izvērtēt citu pierakstus.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija, restis)

TEMA = "Kā izskatās strukturēts risinājums?"

MERKIS = ("Iemācīsimies veidot strukturētu risinājuma pierakstu un "
          "izvērtēt citu pierakstus.")

SATURS = [
    Sakums("Pareiza atbilde - puse punktu",
           fakti=["Eksāmenā bez pamatojuma pareiza atbilde saņem maz "
                  "punktu.",
                  "Skolotājam jāredz, kā tu domāji.",
                  "Pieraksts ir ceļa karte citam lasītājam."]),

    Doma("Dots - jāatrod - risinājums - atbilde",
         "Strukturēts risinājums sastāv no četrām daļām: kas dots, kas "
         "jāatrod, risinājuma soļi ar pamatojumu un atbilde.",
         soli=[
             "Dots: visi zināmie lielumi un fakti ar simboliem.",
             "Jāatrod: ko meklē.",
             "Risinājums: katrs solis rindā, iekavās - kāpēc tā drīkst.",
             "Atbilde: pilns teikums vai vienādība ar mērvienību.",
         ],
         pieze="Pamatojums ir definīcija, īpašība vai jau aprēķināts solis: "
               "«(M - viduspunkts)», «(B ∈ AC)»."),

    Zimejums("Uzdevuma skice",
             geometrija([("A", 0, 0), ("M", 4, 0), ("B", 8, 0),
                         ("K", 11, 0)],
                        nogriezni=["AK"], svitras=[("AM", 1), ("MB", 1)],
                        malas=[("BK", "3 cm")]),
             paskaidro="M - AB viduspunkts, AM = 4 cm, BK = 3 cm."),

    Paraugs("Parauga pieraksts",
            uzd="M ir AB viduspunkts, B ∈ AK. AM = 4 cm, BK = 3 cm. Atrodi "
                "MK.",
            soli=[
                ("Dots: M - AB viduspunkts; B ∈ AK; AM = 4 cm; BK = 3 cm",
                 "Viss zināmais."),
                ("Jāatrod: MK", "Ko meklē."),
                ("MB = AM = 4 cm", "(M - AB viduspunkts)"),
                ("MK = MB + BK = 4 + 3 = 7 (cm)", "(B ∈ MK)"),
            ],
            atbilde="MK = 7 cm"),

    Varianti("Izvērtē pierakstu", [
        {"jaut": "Anna uzrakstīja: «MK = 7 cm». Ko trūkst?",
         "opcijas": ["Soļu un pamatojuma", "Nekā", "Tikai mērvienības",
                     "Zīmējuma krāsas"],
         "pareizi": 0,
         "padoms": "Nav redzams, no kurienes 7."},
        {"jaut": "Pēteris uzrakstīja: «MB = 4, jo tā ir.» Kas ir slikti?",
         "opcijas": ["Pamatojums nav īpašība - jāsaka «M - viduspunkts»",
                     "Nav mērvienības, citādi viss labi",
                     "Nekas", "Jāraksta ar krāsu"],
         "pareizi": 0,
         "padoms": "«Jo tā ir» nav pamatojums."},
        {"jaut": "Kura rinda ir labākais pamatojums vienādībai AC = AB + BC?",
         "opcijas": ["(B ∈ AC)", "(jo tā vajag)", "(no zīmējuma redzams)",
                     "(AC ir garāks)"],
         "pareizi": 0,
         "padoms": "Pamatojums ir fakts no «dots»."},
        {"jaut": "Kur rakstīt mērvienību aprēķinā?",
         "opcijas": ["Pie rezultāta: 4 + 3 = 7 (cm)",
                     "Nekur", "Tikai virsrakstā",
                     "Pie katra skaitļa formulā obligāti"],
         "pareizi": 0,
         "padoms": "Latvijā pieņemts rezultātu ar mērvienību iekavās."},
    ], pamats=4),

    Zimejums("Pieraksta shēma",
             restis([["Dots", "zināmie fakti"],
                     ["Jāatrod", "meklējamais"],
                     ["Risinājums", "solis (pamatojums)"],
                     ["Atbilde", "vienādība ar mērvienību"]]),
             paskaidro="Četras daļas - vienmēr šādā secībā."),

    Pasaule("Instrukcija robotam",
            Varianti("", [
                {"jaut": "Programmētājs raksta robotam soļus. Kāpēc "
                         "secība ir svarīga?",
                 "opcijas": ["Katrs solis lieto iepriekšējo rezultātu",
                             "Tā ir skaistāk",
                             "Robots lasa no beigām",
                             "Secība nav svarīga"],
                 "pareizi": 0,
                 "padoms": "Tāpat kā risinājumā."},
                {"jaut": "Kas programmā atbilst «dots»?",
                 "opcijas": ["Ievaddati", "Rezultāts", "Kļūdas",
                             "Komentāri"],
                 "pareizi": 0,
                 "padoms": "Ar ko sāk."},
                {"jaut": "Kas programmā atbilst pamatojumam iekavās?",
                 "opcijas": ["Komentārs, kas paskaidro soli",
                             "Ievaddati", "Kļūdas paziņojums",
                             "Programmas nosaukums"],
                 "pareizi": 0,
                 "padoms": "Citam programmētājam jāsaprot, kāpēc."},
            ]),
            pavediens="tehnika",
            konteksts="Labs kods, tāpat kā labs risinājums, ir soļos ar "
                      "paskaidrojumiem.",
            kapec="Strukturēts pieraksts ir saprotams citam."),

    Kopsavilkums([
        "Rakstu risinājumu: dots, jāatrod, risinājums, atbilde.",
        "Katram solim pievienoju pamatojumu iekavās.",
        "Izvērtēju citu pierakstus.",
        "Atbildē rakstu mērvienību.",
    ]),

    Majas([
        "Pārraksti kādu sava iepriekšējā darba uzdevumu strukturēti.",
        "Uzraksti risinājumu ar kļūdainu pamatojumu un palūdz drauga "
        "atrast kļūdu.",
        "Salīdzini savu pierakstu ar paraugu.",
    ]),
]
