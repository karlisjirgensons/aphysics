# -*- coding: utf-8 -*-
"""6. klase, 169. stunda: «Cik droši rēķinu ar racionāliem skaitļiem?»

Gada noslēguma bloka pirmā stunda. Te nav jauna satura - ir atskats uz
skaitļiem: daļām, decimāldaļām un negatīvajiem. Viens likumu kopums, kas
jāprot droši pirms 7. klases.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik droši rēķinu ar racionāliem skaitļiem?"

MERKIS = ("Atkārtosim darbības ar racionāliem skaitļiem un novērtēsim savu "
          "prasmi.")

SATURS = [
    Sakums("Gads četros likumos",
           zimejums=restis([["zīmes", "kopsaucējs", "komats", "secība"]]),
           paraksts="Šie četri likumi atrisina gandrīz katru šī gada "
                    "aprēķinu.",
           fakti=["Zīmju likums der visām četrām darbībām.",
                  "Daļām vajag kopsaucēju, decimāldaļām - līdzinātus "
                  "komatus.",
                  "Darbību secība nemainās no skaitļu veida."]),

    Doma("Četri likumi, kas der visam",
         "Racionālu skaitļu aprēķinos vienmēr strādā viens un tas pats "
         "kopums: zīmju likums, kopsaucējs, komata likums un darbību secība.",
         soli=[
             "Nosaki skaitļu veidu un izvēlies vienotu pierakstu.",
             "Nosaki rezultāta zīmi.",
             "Sagatavo skaitļus: kopsaucējs vai komats.",
             "Ievēro darbību secību.",
             "Pārbaudi rezultātu ar pretējo darbību.",
         ],
         pieze="Septītajā klasē šiem skaitļiem pievienosies burti, bet "
               "likumi paliks tie paši. Tāpēc tieši tos vērts prast droši."),

    Paraugs("Četras darbības ar zīmēm",
            uzd="Izrēķini −{1|2} + 0,25; (−3) · {2|3}; (−6) : (−0,5).",
            soli=[
                ("−0,5 + 0,25 = −0,25",
                 "Decimāldaļās ērtāk."),
                ("(−3) · {2|3} = −2",
                 "Saīsina 3 ar 3."),
                ("(−6) : (−0,5) = 12",
                 "Vienādas zīmes; 60 : 5."),
                ("Visos trijos zīme noteikta pirms rēķina",
                 "Tas ir kopīgais solis."),
            ],
            atbilde="−0,25; −2; 12"),

    Ievadi("Atkārto darbības", [
        {"jaut": "Cik ir −{1|2} + 0,25?",
         "atb": ["-0,25", "−0,25", "-0.25"], "padoms": "−0,5 + 0,25."},
        {"jaut": "Cik ir (−3) · {2|3}?",
         "atb": ["-2", "−2"], "padoms": "Saīsina."},
        {"jaut": "Cik ir (−6) : (−0,5)?",
         "atb": ["12"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir −7 + 12 − (−3)?",
         "atb": ["8"], "padoms": "15 − 7."},
        {"jaut": "Cik ir (−2) trešajā pakāpē?",
         "atb": ["-8", "−8"], "padoms": "Trīs mīnusi."},
        {"jaut": "Cik ir {3|4} : (−{1|4})?",
         "atb": ["-3", "−3"], "padoms": "{3|4} · 4, zīme mīnus."},
    ], pamats=4),

    Varianti("Kurš likums te vajadzīgs?", [
        {"jaut": "Izteiksmē {1|3} + {1|4} vajadzīgs...",
         "opcijas": ["kopsaucējs", "komata likums",
                     "zīmju likums", "pakāpes likums"],
         "pareizi": 0,
         "padoms": "Saucēji atšķiras."},
        {"jaut": "Izteiksmē 0,4 · 0,2 vajadzīgs...",
         "opcijas": ["komata likums", "kopsaucējs",
                     "darbību secība", "pakāpes likums"],
         "pareizi": 0,
         "padoms": "Ciparu skaits aiz komata."},
        {"jaut": "Izteiksmē (−3) · (−4) vajadzīgs...",
         "opcijas": ["zīmju likums", "kopsaucējs",
                     "komata likums", "nekas"],
         "pareizi": 0,
         "padoms": "Abas zīmes mīnusi."},
        {"jaut": "Izteiksmē 4 + 6 · 2 vajadzīgs...",
         "opcijas": ["darbību secība", "kopsaucējs",
                     "zīmju likums", "komata likums"],
         "pareizi": 0,
         "padoms": "Reizināšana pirms saskaitīšanas."},
    ], pamats=4),

    Pasaule("Kā rēķina reālos datus?",
            Ievadi("", [
                {"jaut": "Temperatūra no −2,5 °C pieaug par 4 grādiem. Cik "
                         "grādu ir?",
                 "atb": ["1,5", "1.5"], "padoms": "−2,5 + 4."},
                {"jaut": "Kontā −30 €, iemaksā {3|4} no 60 €. Cik eiro ir?",
                 "atb": ["15"], "padoms": "−30 + 45."},
                {"jaut": "3 kastes pa 2,5 kg. Cik kg kopā?",
                 "atb": ["7,5", "7.5"], "padoms": "3 · 2,5."},
                {"jaut": "No 7,5 kg paņem {1|3}. Cik kg paliek?",
                 "atb": ["5"], "padoms": "7,5 − 2,5."},
            ]),
            pavediens="veikals",
            konteksts="Ikdienas datos skaitļi ir sajaukti - un tieši tāpēc "
                      "visi likumi jāprot vienlaikus.",
            kapec="Viens likumu kopums der visiem racionālajiem skaitļiem."),

    Kopsavilkums([
        "Rēķinu ar daļām, decimāldaļām un negatīviem skaitļiem.",
        "Lietoju zīmju likumu visām četrām darbībām.",
        "Sagatavoju skaitļus: kopsaucējs vai līdzināti komati.",
        "Ievēroju darbību secību un pārbaudu rezultātu.",
    ]),

    Majas([
        "Izrēķini piecas izteiksmes ar dažādu veidu skaitļiem.",
        "Katrai pieraksti, kurš likums bija vajadzīgs.",
        "Atzīmē to, kurā biji visnedrošākais.",
    ]),
]
