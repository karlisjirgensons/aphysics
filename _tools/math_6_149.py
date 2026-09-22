# -*- coding: utf-8 -*-
"""6. klase, 149. stunda: «Kā reizina un dala veselus skaitļus?»

Abas darbības vienā stundā, jo tām ir viens zīmju likums. Jaunais te ir
tikai pieraksts un pārbaude: dalījumu vienmēr var pārbaudīt ar reizināšanu,
un tieši tas ļauj kļūdu pamanīt pašam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā reizina un dala veselus skaitļus?"

MERKIS = ("Reizināsim un dalīsim veselus skaitļus, lietojot zīmju likumu.")

SATURS = [
    Sakums("Viens likums divām darbībām",
           fakti=["Vienādas zīmes dod plusu, dažādas - mīnusu.",
                  "Tas pats der gan reizināšanai, gan dalīšanai.",
                  "Dalījumu pārbauda ar reizināšanu."]),

    Doma("Vispirms zīme, tad moduļi",
         "Veselus skaitļus ar zīmēm reizina un dala divos soļos: nosaka "
         "rezultāta zīmi un tad veic darbību ar moduļiem.",
         soli=[
             "Salīdzini abu skaitļu zīmes un nosaki rezultāta zīmi.",
             "Veic darbību ar moduļiem.",
             "Pieliec rezultātam noteikto zīmi.",
             "Pārbaudi dalījumu ar reizināšanu.",
             "Atceries: ar nulli dalīt nedrīkst.",
         ],
         pieze="Nulli drīkst dalīt ar jebkuru skaitli - rezultāts ir nulle. "
               "Bet dalīt *ar* nulli nedrīkst: nav tāda skaitļa, kurš, "
               "reizināts ar nulli, dotu ko citu nekā nulli."),

    Paraugs("Reizini un dali",
            uzd="Cik ir (−36) : (−4) un (−36) : 4?",
            soli=[
                ("(−36) : (−4): zīmes vienādas",
                 "Rezultāts pozitīvs."),
                ("36 : 4 = 9",
                 "Rezultāts 9."),
                ("(−36) : 4: zīmes atšķiras",
                 "Rezultāts negatīvs."),
                ("36 : 4 = 9, zīme mīnus",
                 "Rezultāts −9. Pārbaude: (−9) · 4 = −36."),
            ],
            atbilde="9 un −9"),

    Ievadi("Izrēķini ar zīmēm", [
        {"jaut": "Cik ir (−36) : (−4)?",
         "atb": ["9"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir (−36) : 4?",
         "atb": ["-9", "−9"], "padoms": "Dažādas zīmes."},
        {"jaut": "Cik ir 48 : (−6)?",
         "atb": ["-8", "−8"], "padoms": "48 : 6, zīme mīnus."},
        {"jaut": "Cik ir (−7) · (−8)?",
         "atb": ["56"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir 0 : (−5)?",
         "atb": ["0"], "padoms": "Nulli drīkst dalīt."},
        {"jaut": "Cik ir (−100) : (−25)?",
         "atb": ["4"], "padoms": "100 : 25."},
    ], pamats=4,
        ievads="Pēc katra dalījuma pārbaudi to ar reizināšanu."),

    Pasaule("Cik ilgi pietiks?",
            Kustiba("", [
                {"jaut": "Katru dienu konts sarūk par 15 € jeb −15. Pēc cik "
                         "dienām sarūk par 60 €? Rēķini (−60) : (−15).",
                 "atb": 4, "beigas": 20, "iedala": 5, "mers": "dienas",
                 "merkis": "dienu skaits", "objekts": "Konts",
                 "padoms": "60 : 15."},
                {"jaut": "Temperatūra krīt par 3 grādiem stundā. Pēc cik "
                         "stundām tā nokritīs par 18 grādiem?",
                 "atb": 6, "beigas": 20, "iedala": 5, "mers": "stundas",
                 "merkis": "stundu skaits", "objekts": "Termometrs",
                 "padoms": "18 : 3."},
                {"jaut": "Zonde nolaižas par 8 m minūtē. Pēc cik minūtēm tā "
                         "būs −40 m dziļumā?",
                 "atb": 5, "beigas": 20, "iedala": 5, "mers": "minūtes",
                 "merkis": "minūšu skaits", "objekts": "Zonde",
                 "padoms": "40 : 8."},
                {"jaut": "Krājumi sarūk par 25 vienībām dienā. Pēc cik "
                         "dienām sarūk par 200?",
                 "atb": 8, "beigas": 20, "iedala": 5, "mers": "dienas",
                 "merkis": "dienu skaits", "objekts": "Noliktava",
                 "padoms": "200 : 25."},
            ]),
            pavediens="tehnika",
            konteksts="Ja izmaiņa katru reizi ir vienāda, laiku līdz "
                      "noteiktam stāvoklim atrod ar dalīšanu.",
            kapec="Divi negatīvi skaitļi dalījumā dod pozitīvu laiku."),

    Varianti("Kāda ir zīme?", [
        {"jaut": "(−45) : (−9) ir...",
         "opcijas": ["5", "−5", "54", "−54"],
         "pareizi": 0,
         "padoms": "Vienādas zīmes."},
        {"jaut": "45 : (−9) ir...",
         "opcijas": ["−5", "5", "−54", "54"],
         "pareizi": 0,
         "padoms": "Dažādas zīmes."},
        {"jaut": "Ar nulli dalīt...",
         "opcijas": ["nedrīkst", "drīkst, rezultāts nulle",
                     "drīkst, rezultāts viens", "drīkst vienmēr"],
         "pareizi": 0,
         "padoms": "Nav tāda skaitļa."},
        {"jaut": "Kā pārbaudīt, vai (−36) : 4 = −9?",
         "opcijas": ["(−9) · 4 = −36", "(−36) · 4", "−9 : 4", "4 : (−9)"],
         "pareizi": 0,
         "padoms": "Rezultāts reiz dalītājs."},
    ], pamats=4),

    Kopsavilkums([
        "Reizinu un dalu veselus skaitļus ar zīmēm.",
        "Nosaku rezultāta zīmi pirms darbības ar moduļiem.",
        "Pārbaudu dalījumu ar reizināšanu.",
        "Zinu, ka ar nulli dalīt nedrīkst.",
    ]),

    Majas([
        "Izrēķini (−54) : 6; (−54) : (−6); 54 : (−6).",
        "Katram pieraksti pārbaudi.",
        "Paskaidro, kāpēc ar nulli dalīt nedrīkst.",
    ]),
]
