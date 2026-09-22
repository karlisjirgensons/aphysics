# -*- coding: utf-8 -*-
"""6. klase, 124. stunda: «Kā mainās temperatūra?»

Jauns temats sākas nevis ar likumu, bet ar situāciju. Temperatūras un naudas
izmaiņas skolēns prot izstāstīt arī bez matemātikas - un tieši šo stāstu te
pārraksta ar plusiem un mīnusiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā mainās temperatūra?"

MERKIS = ("Interpretēsim vienkāršas veselu skaitļu summas ar temperatūras "
          "vai naudas piemēriem.")

SATURS = [
    Sakums("Stāsts, kas pārrakstīts ar zīmēm",
           zimejums=taisne(-10, 6, 4, [(-6, "sākums"), (2, "beigas")],
                           bultas=[(-6, 2, "+8")]),
           paraksts="Bija −6 °C, kļuva par 8 grādiem siltāks: "
                    "−6 + 8 = 2.",
           fakti=["Sildīšanās ir pieskaitīšana, atdzišana - atņemšana.",
                  "Sākuma vērtība var būt negatīva.",
                  "Rezultāts var būt gan virs, gan zem nulles."]),

    Doma("Sākums plus izmaiņa ir rezultāts",
         "Katru temperatūras vai naudas izmaiņu pieraksta kā summu: sākuma "
         "vērtībai pieskaita izmaiņu ar tās zīmi.",
         soli=[
             "Pieraksti sākuma vērtību ar zīmi.",
             "Nosaki, vai lielums auga vai sarūka.",
             "Pieaugumu raksti ar plusu, samazinājumu - ar mīnusu.",
             "Pārvieties pa skaitļu taisni un nolasi rezultātu.",
             "Pārbaudi, vai atbilde iederas stāstā.",
         ],
         pieze="Naudā tas pats: konts −20 € un ienākums 50 € dod "
               "−20 + 50 = 30 €. Vispirms parāds tiek dzēsts, tikai tad "
               "sākas uzkrājums."),

    Paraugs("Pārraksti stāstu ar zīmēm",
            uzd="No rīta bija −6 °C. Dienā kļuva par 8 grādiem siltāks. Cik "
                "grādu ir tagad?",
            soli=[
                ("Sākums: −6",
                 "Zem nulles."),
                ("Izmaiņa: +8",
                 "Kļuva siltāks."),
                ("−6 + 8",
                 "Astoņi soļi pa labi."),
                ("= 2",
                 "Divi grādi virs nulles."),
            ],
            atbilde="2 °C"),

    Ievadi("Izrēķini izmaiņu", [
        {"jaut": "Bija −6 °C, kļuva par 8 grādiem siltāks. Cik ir tagad?",
         "atb": ["2"], "padoms": "−6 + 8."},
        {"jaut": "Bija −3 °C, kļuva par 5 grādiem aukstāks. Cik ir tagad?",
         "atb": ["-8", "−8"], "padoms": "−3 − 5."},
        {"jaut": "Bija 4 °C, kļuva par 9 grādiem aukstāks. Cik ir tagad?",
         "atb": ["-5", "−5"], "padoms": "4 − 9."},
        {"jaut": "Kontā bija −20 €, iemaksāja 50 €. Cik ir tagad?",
         "atb": ["30"], "padoms": "−20 + 50."},
        {"jaut": "Kontā bija 15 €, iztērēja 40 €. Cik ir tagad?",
         "atb": ["-25", "−25"], "padoms": "15 − 40."},
        {"jaut": "Bija −12 °C, kļuva par 12 grādiem siltāks. Cik ir tagad?",
         "atb": ["0"], "padoms": "Pretēju skaitļu summa."},
    ], pamats=4,
        ievads="Vispirms pieraksti sākumu ar zīmi, tikai tad izmaiņu."),

    Varianti("Kā to pierakstīt?", [
        {"jaut": "«Bija −5 °C, kļuva par 3 grādiem siltāks.» Kurš pieraksts "
                 "der?",
         "opcijas": ["−5 + 3", "−5 − 3", "5 + 3", "3 − 5 = −2 nav pareizi"],
         "pareizi": 0,
         "padoms": "Siltāks - pieskaita."},
        {"jaut": "«Bija 2 °C, kļuva par 7 grādiem aukstāks.» Kurš pieraksts "
                 "der?",
         "opcijas": ["2 − 7", "2 + 7", "−2 − 7", "7 − 2"],
         "pareizi": 0,
         "padoms": "Aukstāks - atņem."},
        {"jaut": "Kontā −30 €, iemaksā 30 €. Rezultāts ir...",
         "opcijas": ["0", "−60", "60", "−30"],
         "pareizi": 0,
         "padoms": "Pretēju skaitļu summa."},
        {"jaut": "Kad rezultāts paliek negatīvs?",
         "opcijas": ["Kad pieaugums ir mazāks par sākotnējo parādu",
                     "Vienmēr", "Nekad",
                     "Kad pieaugums ir liels"],
         "pareizi": 0,
         "padoms": "−20 + 10 = −10."},
    ], pamats=4),

    Pasaule("Kā mainījās konts?",
            Ievadi("", [
                {"jaut": "Kontā −40 €, iemaksā 25 €. Cik eiro ir kontā?",
                 "atb": ["-15", "−15"], "padoms": "−40 + 25."},
                {"jaut": "Vēl iemaksā 30 €. Cik eiro ir tagad?",
                 "atb": ["15"], "padoms": "−15 + 30."},
                {"jaut": "Iztērē 20 €. Cik eiro ir tagad?",
                 "atb": ["-5", "−5"], "padoms": "15 − 20."},
                {"jaut": "Cik eiro jāiemaksā, lai kontā būtu nulle?",
                 "atb": ["5"], "padoms": "Pretējais skaitlis."},
            ]),
            pavediens="veikals",
            konteksts="Bankas izrakstā katra rinda ir viena izmaiņa ar zīmi, "
                      "un atlikums ir visu summu rezultāts.",
            kapec="Konta atlikums ir tieši tas pats, kas punkts uz skaitļu "
                  "taisnes."),

    Zimejums("Divas izmaiņas pēc kārtas",
             taisne(-10, 6, 4, [(-8, "sākums"), (-3, "pēc 1."),
                                (2, "pēc 2.")],
                    bultas=[(-8, -3, "+5"), (-3, 2, "+5")]),
             paskaidro="Divi soļi pa 5 vienībām: −8 + 5 + 5 = 2. Katra "
                       "bultiņa ir viena izmaiņa.",
             ievads="Vairākas izmaiņas seko viena otrai."),

    Kopsavilkums([
        "Pārrakstu temperatūras un naudas izmaiņas ar zīmēm.",
        "Pieskaitu pieaugumu un atņemu samazinājumu.",
        "Aprēķinu rezultātu, kas var būt gan pozitīvs, gan negatīvs.",
        "Pārbaudu, vai atbilde iederas stāstā.",
    ]),

    Majas([
        "Pieraksti ar zīmēm trīs šodienas temperatūras izmaiņas.",
        "Izrēķini, kāda būtu temperatūra pēc katras.",
        "Izdomā naudas stāstu, kurā rezultāts ir tieši nulle.",
    ]),
]
