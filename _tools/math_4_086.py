# -*- coding: utf-8 -*-
"""4. klase, 86. stunda: «Kad noder kalkulators?»

Mikrotemata noslēgums. Kalkulators ir rīks, nevis aizvietotājs: to lieto
lieliem, neērtiem skaitļiem, bet rezultātu vienmēr pārbauda - ar
novērtējumu vai ar pretējo darbību. Stundā izlemj, kad galva ir ātrāka.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kad noder kalkulators?"

MERKIS = ("Lietosim kalkulatoru daudzciparu skaitļu reizināšanai un "
          "dalīšanai un pārbaudīsim dalījumu ar reizināšanu.")

SATURS = [
    Sakums("Kurš ātrāks - tu vai kalkulators?",
           zimejums=restis([["rēķins", "ātrāk"],
                            ["30 · 20", "galvā"],
                            ["4876 : 53", "kalkulators"],
                            ["25 · 4", "galvā"],
                            ["387 · 29", "kalkulators"]],
                           "sacensība"),
           fakti=["Kamēr kalkulatoru atrod, 30 · 20 jau izrēķināts.",
                  "Neērtiem skaitļiem kalkulators ir drošāks."]),

    Doma("Kalkulators rēķina, tu pārbaudi",
         "Kalkulatoru lieto neērtiem skaitļiem, bet rezultātu pārbauda ar "
         "novērtējumu un pretējo darbību.",
         soli=[
             "Novērtē atbildi galvā.",
             "Ievadi skaitļus rūpīgi, cipars pa ciparam.",
             "Salīdzini ar novērtējumu.",
             "Pārbaudi ar pretējo darbību: dalījums · dalītājs.",
         ],
         pieze="Ja ekrānā ir komats (92,0), bet gaidīji veselu skaitli, "
               "paskaties vēlreiz uz ievadītajiem skaitļiem."),

    Paraugs("4876 : 53 ar pārbaudi",
            uzd="Izdali ar kalkulatoru 4876 : 53 un pārbaudi.",
            soli=[
                ("5000 : 50 = 100", "Novērtējums."),
                ("4876 : 53 = 92", "Kalkulatorā."),
                ("92 · 53 = 4876", "Pārbaude ar reizināšanu."),
            ],
            atbilde="92"),

    Varianti("Galva vai kalkulators?", [
        {"jaut": "500 · 20",
         "opcijas": ["galvā", "kalkulators"], "pareizi": 0,
         "padoms": "5 · 2 un 000."},
        {"jaut": "3847 : 47",
         "opcijas": ["kalkulators", "galvā"], "pareizi": 0,
         "padoms": "Neērti skaitļi."},
        {"jaut": "99 · 12",
         "opcijas": ["galvā", "kalkulators"], "pareizi": 0,
         "padoms": "1200 − 12."},
        {"jaut": "Kalkulators rāda 8,7 dalījumam 6003 : 69. Ko darīt?",
         "opcijas": ["pārbaudīt ievadi - novērtējums ir ap 90",
                     "pierakstīt 8,7", "noapaļot uz 9"], "pareizi": 0,
         "padoms": "6000 : 60 = 100 - tātad ap 90."},
    ], pamats=4),

    Ievadi("Ar kalkulatoru un pārbaudi", [
        {"jaut": "387 · 29 = ?", "atb": ["11223", "11 223"],
         "padoms": "Novērtē: 400 · 30 = 12 000."},
        {"jaut": "6003 : 69 = ?", "atb": ["87"],
         "padoms": "Pārbaude: 87 · 69."},
        {"jaut": "Pārbaude: 87 · 69 = ?", "atb": ["6003"],
         "padoms": "Jāsanāk dalāmajam."},
        {"jaut": "3847 : 47 = 81 (atl. ?)", "atb": ["40"],
         "padoms": "47 · 81 = 3807."},
    ]),

    Pasaule("Klases budžeta pārbaude",
            Ievadi("", [
                {"jaut": "Mācību gada budžets 4876 € uz 53 skolēniem (divām "
                         "klasēm). Cik katram?",
                 "atb": ["92"], "padoms": "4876 : 53."},
                {"jaut": "Grāmatas: 53 skolēni pa 29 €. Cik kopā?",
                 "atb": ["1537"], "padoms": "53 · 29."},
                {"jaut": "Cik paliek no 4876 € pēc grāmatām?",
                 "atb": ["3339"], "padoms": "4876 − 1537."},
                {"jaut": "Pārbaude: vai 1537 ≈ 50 · 30 = 1500? Raksti "
                         "«jā» vai «nē».",
                 "atb": ["jā", "ja"], "tastatura": "text",
                 "padoms": "1537 ir tuvu 1500."},
            ]),
            pavediens="skola",
            konteksts="Skolas grāmatvedis rēķina ar kalkulatoru, bet katru "
                      "summu pārbauda - kļūda maksā naudu.",
            kapec="Kalkulators rēķina, bet atbildīgs par rezultātu esi tu."),

    Kopsavilkums([
        "Izvēlos, kad rēķināt galvā un kad ar kalkulatoru.",
        "Pārbaudu kalkulatora rezultātu ar novērtējumu.",
        "Pārbaudu dalījumu ar reizināšanu.",
    ]),

    Majas([
        "Ar kalkulatoru izrēķini ģimenes nedēļas pārtikas izmaksas un "
        "pārbaudi ar novērtējumu.",
        "Sarīko sacensību: tu galvā, mājinieks ar kalkulatoru - 25 · 4.",
        "Izdali ar kalkulatoru un pārbaudi ar reizināšanu: 5238 : 54.",
    ]),
]
