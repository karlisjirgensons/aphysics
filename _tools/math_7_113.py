# -*- coding: utf-8 -*-
"""7. klase, 113. stunda: «Kā situāciju pierakstīt ar burtiem?»

Algebriska izteiksme ir aprēķina «recepte», kurā nezināmais skaitlis
apzīmēts ar burtu. Stunda iemāca pārtulkot vārdus («par 5 vairāk»,
«divreiz mazāk», «kopā») darbībās ar burtiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā situāciju pierakstīt ar burtiem?"

MERKIS = ("Aprakstīsim situāciju ar algebrisku izteiksmi, apzīmējot "
          "nezināmos lielumus ar burtiem.")

SATURS = [
    Sakums("Vārdnīca: no latviešu valodas uz algebru",
           zimejums=restis([["vārdiem", "ar burtiem"],
                            ["par 5 vairāk nekā x", "x + 5"],
                            ["par 3 mazāk nekā x", "x − 3"],
                            ["3 reizes vairāk nekā x", "3x"],
                            ["divreiz mazāk nekā x", "x : 2"]]),
           fakti=["Burts aizstāj skaitli, kuru vēl nezinām.",
                  "Izteiksme der jebkuram šī skaitļa lielumam."]),

    Doma("Burts - vieta skaitlim",
         "Algebriska izteiksme ir pieraksts ar skaitļiem, burtiem un darbību "
         "zīmēm. Burts (mainīgais) apzīmē skaitli, kas var mainīties vai vēl "
         "nav zināms.",
         soli=[
             "Nosaki, kurš lielums nav zināms - apzīmē to ar burtu.",
             "«Vairāk par» - saskaitīšana; «mazāk par» - atņemšana.",
             "«Reizes vairāk» - reizināšana; «reizes mazāk» - dalīšana.",
             "Pārbaudi ar kādu skaitli: vai izteiksme dod pareizo?",
         ],
         pieze="Reizinājumu ar burtu raksta bez zīmes: 3 · x = 3x. Skaitli "
               "raksta pirms burta."),

    Paraugs("Pārtulko",
            uzd="Annai ir x eiro. Pēterim ir 3 reizes vairāk, bet Līgai - par "
                "4 eiro mazāk nekā Pēterim. Cik ir Līgai? Cik visiem kopā?",
            soli=[
                ("Pēterim: 3x", "3 reizes vairāk."),
                ("Līgai: 3x − 4", "Par 4 mazāk nekā Pēterim."),
                ("Kopā: x + 3x + (3x − 4)", "Saskaita."),
                ("Pārbaude, x = 10: 10 + 30 + 26 = 66", "Ar skaitli."),
            ],
            atbilde="Līgai 3x − 4; kopā x + 3x + 3x − 4"),

    Varianti("Kura izteiksme?", [
        {"jaut": "Skaitlis, par 7 lielāks nekā a",
         "opcijas": ["a + 7", "7a", "a − 7", "7 − a"],
         "pareizi": 0, "padoms": "Vairāk - pluss."},
        {"jaut": "Skaitļu m un n summa, reizināta ar 2",
         "opcijas": ["2(m + n)", "2m + n", "m + 2n", "2mn"],
         "pareizi": 0, "padoms": "Vispirms summa - iekavās."},
        {"jaut": "Puse no skaitļa y",
         "opcijas": ["{y|2}", "2y", "y − 2", "y + {1|2}"],
         "pareizi": 0, "padoms": "Dala ar 2."},
        {"jaut": "Taisnstūra perimetrs ar malām a un b",
         "opcijas": ["2(a + b)", "ab", "a + b", "2ab"],
         "pareizi": 0, "padoms": "Visas četras malas."},
    ], pamats=4),

    Ievadi("Aprēķini izteiksmes vērtību", [
        {"jaut": "3x − 4, ja x = 10",
         "atb": ["26"], "padoms": "30 − 4."},
        {"jaut": "2(m + n), ja m = 3, n = 5",
         "atb": ["16"], "padoms": "2 · 8."},
        {"jaut": "Biļete maksā b eiro. 5 biļetes un 2 € rezervācija: "
                 "5b + 2. Cik €, ja b = 7?",
         "atb": ["37"], "padoms": "35 + 2."},
        {"jaut": "Tējkanna uzvārās t minūtēs, kafija - par 3 min ilgāk. "
                 "Cik min kafijai, ja t = 4?",
         "atb": ["7"], "padoms": "t + 3."},
    ]),

    Pasaule("Mobilā spēle",
            Varianti("", [
                {"jaut": "Par katru līmeni iegūst p punktus, par bonusu - "
                         "50. Punkti pēc n līmeņiem un viena bonusa?",
                 "opcijas": ["pn + 50", "p + n + 50", "50pn", "p(n + 50)"],
                 "pareizi": 0, "padoms": "n reizes pa p, plus 50."},
                {"jaut": "Dārgakmens maksā d monētas. Par 200 monētām "
                         "nopirka k dārgakmeņus. Cik monētu palika?",
                 "opcijas": ["200 − kd", "200 − k − d", "kd − 200",
                             "200 : kd"],
                 "pareizi": 0, "padoms": "Iztērēts k · d."},
                {"jaut": "Ja p = 120, n = 5 - cik punktu?",
                 "opcijas": ["650", "175", "600", "6000"],
                 "pareizi": 0, "padoms": "600 + 50."},
            ]),
            pavediens="dati",
            konteksts="Spēļu izstrādātāji punktu sistēmu raksta kā "
                      "izteiksmes ar mainīgajiem.",
            kapec="Izteiksme der jebkuram spēlētājam."),

    Kopsavilkums([
        "Pārtulkoju vārdus darbībās ar burtiem.",
        "Rakstu reizinājumu ar burtu bez zīmes: 3x.",
        "Lieku iekavas, ja darbība attiecas uz summu.",
        "Pārbaudu izteiksmi ar skaitli.",
    ]),

    Majas([
        "Uzraksti izteiksmi savas kabatas naudas aprēķinam.",
        "Pārtulko: «skaitlis, par 3 mazāks nekā x divkāršots».",
        "Izdomā situāciju izteiksmei 4a + 10.",
    ]),
]
