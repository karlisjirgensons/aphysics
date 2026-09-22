# -*- coding: utf-8 -*-
"""6. klase, 132. stunda: «Kāpēc atņemšanu var aizstāt?»

Likuma stunda. Pēc iepriekšējās virknes tas jau ir redzēts; te to pieraksta
un lieto. Galvenais ieguvums: visa izteiksme pārvēršas par summu, un tālāk
strādā tikai viens algoritms.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāpēc atņemšanu var aizstāt?"

MERKIS = ("Pierakstīsim atņemšanu kā pretējā skaitļa pieskaitīšanu un "
          "skaidrosim, kad tas palīdz.")

SATURS = [
    Sakums("Viena darbība divu vietā",
           zimejums=restis([["a − b", "=", "a + (−b)"],
                            ["7 − 3", "=", "7 + (−3)"]]),
           paraksts="Atņemšanu vienmēr var pierakstīt kā saskaitīšanu ar "
                    "pretējo skaitli.",
           fakti=["Atņemt skaitli nozīmē pieskaitīt tā pretējo.",
                  "Pēc pārveidošanas izteiksmē ir tikai saskaitīšana.",
                  "Tad der viens algoritms - par summas zīmi."]),

    Doma("Maini darbību un skaitļa zīmi reizē",
         "Atņemšanu aizstāj ar saskaitīšanu, vienlaikus mainot mazinātāja "
         "zīmi uz pretējo; izteiksmes vērtība nemainās.",
         soli=[
             "Atrodi izteiksmē atņemšanas zīmi.",
             "Nomaini to uz saskaitīšanu.",
             "Vienlaikus nomaini mazinātāja zīmi.",
             "Pārraksti visu izteiksmi kā summu.",
             "Saskaiti pēc zināmā likuma.",
         ],
         pieze="Abas maiņas notiek reizē - ja nomaina tikai vienu, "
               "izteiksmes vērtība mainās. Tāpēc ērti pārrakstīt visu "
               "izteiksmi no jauna, nevis labot to pašu rindu."),

    Paraugs("Pārraksti par summu",
            uzd="Pārraksti un izrēķini −5 − (−8) un 4 − 9.",
            soli=[
                ("−5 − (−8) = −5 + 8",
                 "Darbība un zīme maina abas."),
                ("= 3",
                 "8 − 5, zīme pluss."),
                ("4 − 9 = 4 + (−9)",
                 "Tā pati maiņa."),
                ("= −5",
                 "9 − 4, zīme mīnus."),
            ],
            atbilde="3 un −5"),

    Ievadi("Pārraksti un izrēķini", [
        {"jaut": "Cik ir −5 − (−8)?",
         "atb": ["3"], "padoms": "−5 + 8."},
        {"jaut": "Cik ir 4 − 9?",
         "atb": ["-5", "−5"], "padoms": "4 + (−9)."},
        {"jaut": "Cik ir −7 − 3?",
         "atb": ["-10", "−10"], "padoms": "−7 + (−3)."},
        {"jaut": "Cik ir 6 − (−6)?",
         "atb": ["12"], "padoms": "6 + 6."},
        {"jaut": "Cik ir −12 − (−5)?",
         "atb": ["-7", "−7"], "padoms": "−12 + 5."},
        {"jaut": "Cik ir 0 − (−9)?",
         "atb": ["9"], "padoms": "0 + 9."},
    ], pamats=4,
        ievads="Vispirms pārraksti par summu, tikai tad rēķini."),

    Varianti("Kā pārrakstīt?", [
        {"jaut": "7 − 3 kā summa ir...",
         "opcijas": ["7 + (−3)", "−7 + 3", "7 + 3", "−7 − 3"],
         "pareizi": 0,
         "padoms": "Mazinātājam maina zīmi."},
        {"jaut": "−4 − (−9) kā summa ir...",
         "opcijas": ["−4 + 9", "−4 + (−9)", "4 + 9", "4 − 9"],
         "pareizi": 0,
         "padoms": "Mīnuss mīnusa priekšā."},
        {"jaut": "Kas mainās, pārrakstot atņemšanu?",
         "opcijas": ["Gan darbība, gan mazinātāja zīme",
                     "Tikai darbība", "Tikai zīme",
                     "Mazināmā zīme"],
         "pareizi": 0,
         "padoms": "Abas reizē."},
        {"jaut": "Kāpēc tas palīdz?",
         "opcijas": ["Jo paliek tikai viens algoritms",
                     "Jo izteiksme kļūst īsāka",
                     "Jo skaitļi kļūst mazāki", "Tas nepalīdz"],
         "pareizi": 0,
         "padoms": "Visa izteiksme kļūst par summu."},
    ], pamats=4),

    Pasaule("Cik liela ir temperatūras starpība?",
            Ievadi("", [
                {"jaut": "Dienā 3 °C, naktī −8 °C. Par cik grādiem diena "
                         "siltāka?",
                 "atb": ["11"], "padoms": "3 − (−8) = 3 + 8."},
                {"jaut": "Kalnā −15 °C, ielejā −4 °C. Par cik grādiem ieleja "
                         "siltāka?",
                 "atb": ["11"], "padoms": "−4 − (−15)."},
                {"jaut": "Vakar −2 °C, šodien −9 °C. Par cik grādiem kļuvis "
                         "aukstāks?",
                 "atb": ["7"], "padoms": "−2 − (−9)."},
                {"jaut": "Rīta 1 °C, vakara −6 °C. Kāda ir starpība?",
                 "atb": ["7"], "padoms": "1 + 6."},
            ]),
            pavediens="planeta",
            konteksts="Temperatūras starpību rēķina ar atņemšanu, un tieši "
                      "negatīvie skaitļi to padara neparastu.",
            kapec="Atņemt negatīvu nozīmē pieskaitīt tā moduli."),

    Zimejums("Divas darbības - viens rezultāts",
             restis([["−5 − (−8)", "−5 + 8"],
                     ["3", "3"]]),
             paskaidro="Abas izteiksmes ir viena un tā pati. Otro ir "
                       "vieglāk izrēķināt.",
             ievads="Pārrakstīšana nemaina vērtību."),

    Kopsavilkums([
        "Pierakstu atņemšanu kā pretējā skaitļa pieskaitīšanu.",
        "Mainu darbību un mazinātāja zīmi vienlaikus.",
        "Pārveidoju visu izteiksmi par summu.",
        "Paskaidroju, kāpēc tas atvieglo rēķināšanu.",
    ]),

    Majas([
        "Pārraksti par summām: −3 − 7; 5 − (−2); −8 − (−8).",
        "Izrēķini visas trīs.",
        "Pieraksti, kura no tām bija vieglākā un kāpēc.",
    ]),
]
