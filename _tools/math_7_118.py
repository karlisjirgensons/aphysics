# -*- coding: utf-8 -*-
"""7. klase, 118. stunda: «Kad divas izteiksmes ir vienādas?»

Divas izteiksmes ir identiski vienādas, ja tām ir vienādas vērtības pie
jebkurām mainīgo vērtībām. Tabula ar dažiem skaitļiem var parādīt, ka
izteiksmes NAV vienādas, bet pierādīt vienādību var tikai ar pārveidojumu.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kad divas izteiksmes ir vienādas?"

MERKIS = ("Paskaidrosim, kas ir identiski vienādas izteiksmes, un "
          "pamatosim to ar piemēriem.")

SATURS = [
    Sakums("2(x + 3) un 2x + 6 - vienmēr vienādi?",
           zimejums=restis([["x", "−1", "0", "2", "10"],
                            ["2(x + 3)", "4", "6", "10", "26"],
                            ["2x + 6", "4", "6", "10", "26"]]),
           paraksts="Katram x - vienāda vērtība.",
           fakti=["Tabula rāda tikai dažus x.",
                  "Pierādījums - reizināšanas sadalāmības likums.",
                  "Tad vienādība der visiem x."]),

    Doma("Identiski vienādas izteiksmes",
         "Divas izteiksmes ir identiski vienādas, ja jebkurām mainīgo "
         "vērtībām to vērtības ir vienādas. Izteiksmes aizstāšanu ar "
         "identiski vienādu sauc par identisku pārveidojumu.",
         soli=[
             "Lai atspēkotu - pietiek ar vienu x, kur vērtības atšķiras.",
             "Lai pierādītu - vienu izteiksmi pārveido otrā ar likumiem.",
             "Likumi: pārvietojamības, savienojamības, sadalāmības.",
             "Tabula palīdz pārbaudīt, bet nepierāda.",
         ],
         pieze="x + x un x · x vienādi, ja x = 2 (abi 4), bet x = 3 dod 6 un "
               "9 - tās nav identiski vienādas."),

    Paraugs("Atspēko ar pretpiemēru",
            uzd="Vai (a + b)² un a² + b² ir identiski vienādas?",
            soli=[
                ("Ņem a = 1, b = 1", "Vienkāršs pāris."),
                ("(1 + 1)² = 4", "Pirmā."),
                ("1² + 1² = 2", "Otrā."),
                ("4 ≠ 2", "Pretpiemērs."),
            ],
            atbilde="Nav identiski vienādas."),

    Varianti("Identiski vienādas?", [
        {"jaut": "3(a + 2) un 3a + 6",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Sadalāmība."},
        {"jaut": "2x + 3x un 5x",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Divi x un trīs x."},
        {"jaut": "x + x un x²",
         "opcijas": ["Jā", "Nē"], "pareizi": 1, "jaukt": False,
         "padoms": "x = 3: 6 un 9."},
        {"jaut": "a − b un b − a",
         "opcijas": ["Jā", "Nē"], "pareizi": 1, "jaukt": False,
         "padoms": "a = 5, b = 2: 3 un −3."},
        {"jaut": "ab un ba",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Pārvietojamība."},
        {"jaut": "{2x|2} un x",
         "opcijas": ["Jā", "Nē"], "pareizi": 0, "jaukt": False,
         "padoms": "Saīsina."},
    ], pamats=4),

    Zimejums("Tabula nav pierādījums",
             restis([["x", "0", "1", "2"],
                     ["x² − x", "0", "0", "2"],
                     ["0", "0", "0", "0"]]),
             paskaidro="Pie x = 0 un x = 1 sakrīt, bet x = 2 - nē."),

    Pasaule("Divi kalkulatori",
            Varianti("", [
                {"jaut": "Veikals A: cena · 0,9 + 5 € piegāde. Veikals B: "
                         "(cena + 5) · 0,9. Vai vienmēr vienādi?",
                 "opcijas": ["Nē - B atlaide ir arī piegādei",
                             "Jā", "Tikai lētām precēm", "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "0,9x + 5 un 0,9x + 4,5."},
                {"jaut": "Par cik € atšķiras?",
                 "opcijas": ["0,5 €", "5 €", "0 €", "4,5 €"],
                 "pareizi": 0, "padoms": "5 − 4,5."},
                {"jaut": "Kurš izdevīgāks?",
                 "opcijas": ["B", "A", "Vienādi"],
                 "pareizi": 0, "jaukt": False, "padoms": "Mazāk."},
            ]),
            pavediens="veikals",
            konteksts="Divas «vienādas» akcijas var atšķirties - to parāda "
                      "izteiksmju salīdzināšana.",
            kapec="Identiski vienādas - visiem skaitļiem."),

    Kopsavilkums([
        "Zinu, kas ir identiski vienādas izteiksmes.",
        "Atspēkoju vienādību ar vienu pretpiemēru.",
        "Zinu, ka tabula nepierāda vienādību.",
        "Pierādu ar darbību likumiem.",
    ]),

    Majas([
        "Pārbaudi ar 3 skaitļiem: 4(x − 1) un 4x − 4.",
        "Atrodi pretpiemēru: 2(x + 5) un 2x + 5.",
        "Salīdzini divu veikalu piegādes noteikumus ar izteiksmēm.",
    ]),
]
