# -*- coding: utf-8 -*-
"""6. klase, 142. stunda: «Kā rēķināt ar negatīvām decimāldaļām?»

Tas pats, kas iepriekšējā stundā, tikai decimālpierakstā - un te kopsaucējs
nav vajadzīgs. Toties parādās cita kļūda: cipari jālīdzina pēc komata, un
zīme jāņem no lielākā moduļa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā rēķināt ar negatīvām decimāldaļām?"

MERKIS = ("Saskaitīsim un atņemsim pozitīvas un negatīvas decimāldaļas un "
          "skaidrosim darbības.")

SATURS = [
    Sakums("Kopsaucējs nav vajadzīgs",
           fakti=["Decimāldaļas līdzina pēc komata, ne pēc pēdējā cipara.",
                  "Zīmju likums ir tas pats, kas veseliem skaitļiem.",
                  "Trūkstošās vietas aizpilda ar nullēm."]),

    Doma("Līdzini komatus, tad lieto zīmju likumu",
         "Decimāldaļas ar zīmēm saskaita tāpat kā veselus skaitļus: "
         "salīdzina zīmes, tad saskaita vai atņem moduļus, līdzinot komatus.",
         soli=[
             "Pieraksti abus skaitļus ar zīmēm.",
             "Salīdzini zīmes: vienādas vai dažādas.",
             "Ja vienādas - moduļus saskaiti; ja dažādas - atņem.",
             "Līdzini komatus un rēķini pa vietām.",
             "Rezultātam pieliec lielākā moduļa zīmi.",
         ],
         pieze="Atņemšanu vispirms pārraksta: −2,5 − 1,3 ir "
               "−2,5 + (−1,3) = −3,8. Ja to neizdara, viegli sajaukt, ko ar "
               "ko atņemt."),

    Paraugs("Divas decimāldaļas ar zīmēm",
            uzd="Cik ir −2,5 + 1,3 un −2,5 − 1,3?",
            soli=[
                ("−2,5 + 1,3: zīmes atšķiras",
                 "Moduļus atņem: 2,5 − 1,3 = 1,2."),
                ("Zīme no lielākā moduļa: mīnuss",
                 "Rezultāts −1,2."),
                ("−2,5 − 1,3 = −2,5 + (−1,3)",
                 "Pārraksta par summu."),
                ("Zīmes vienādas: 2,5 + 1,3 = 3,8, zīme mīnus",
                 "Rezultāts −3,8."),
            ],
            atbilde="−1,2 un −3,8"),

    Ievadi("Rēķini ar decimāldaļām", [
        {"jaut": "Cik ir −2,5 + 1,3?",
         "atb": ["-1,2", "−1,2", "-1.2"], "padoms": "2,5 − 1,3, zīme mīnus."},
        {"jaut": "Cik ir −2,5 − 1,3?",
         "atb": ["-3,8", "−3,8", "-3.8"], "padoms": "2,5 + 1,3, zīme mīnus."},
        {"jaut": "Cik ir 4,2 + (−6,7)?",
         "atb": ["-2,5", "−2,5", "-2.5"], "padoms": "6,7 − 4,2."},
        {"jaut": "Cik ir −0,8 + 0,8?",
         "atb": ["0"], "padoms": "Pretēji skaitļi."},
        {"jaut": "Cik ir −1,5 − (−4,5)?",
         "atb": ["3"], "padoms": "−1,5 + 4,5."},
        {"jaut": "Cik ir −0,25 + (−0,75)?",
         "atb": ["-1", "−1"], "padoms": "Vienādas zīmes."},
    ], pamats=4,
        ievads="Vispirms pārraksti atņemšanu par saskaitīšanu."),

    Pasaule("Cik dziļi nolaižas aparāts?",
            Kustiba("", [
                {"jaut": "Aparāts ir −2,5 m dziļumā un nolaižas vēl par "
                         "1,5 m. Kur tas ir?",
                 "atb": -4, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Aparāts", "padoms": "−2,5 − 1,5."},
                {"jaut": "No −4 m tas paceļas par 6,5 m. Kur tas ir?",
                 "atb": 2.5, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Aparāts", "padoms": "−4 + 6,5."},
                {"jaut": "No 2,5 m tas nolaižas par 7,5 m. Kur tas ir?",
                 "atb": -5, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Aparāts", "padoms": "2,5 − 7,5."},
                {"jaut": "No −5 m tas paceļas par 5 m. Kur tas ir?",
                 "atb": 0, "sakums": -10, "beigas": 10, "iedala": 5,
                 "mers": "metri", "merkis": "jaunā vieta",
                 "objekts": "Aparāts", "padoms": "Pretēji skaitļi."},
            ]),
            pavediens="planeta",
            konteksts="Zemūdens aparāta dziļumu mēra ar desmitdaļu "
                      "precizitāti - tāpēc visi skaitļi ir decimāldaļas.",
            kapec="Zīmju likums nemainās no tā, ka skaitlim ir komats."),

    Varianti("Kur slēpjas kļūda?", [
        {"jaut": "Skolēns: −2,5 + 1,3 = −3,8. Kas nav labi?",
         "opcijas": ["Moduļi saskaitīti, lai gan zīmes atšķiras",
                     "Nepareizi likts komats",
                     "Sajaukta secība", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Dažādas zīmes - moduļus atņem."},
        {"jaut": "Skolēns: −1,5 − (−4,5) = −6. Kas nav labi?",
         "opcijas": ["Mazinātāja zīme nav mainīta",
                     "Nepareizi saskaitīti moduļi",
                     "Aizmirsts komats", "Kļūdas nav"],
         "pareizi": 0,
         "padoms": "Pareizi ir −1,5 + 4,5."},
        {"jaut": "Kā līdzina decimāldaļas, rēķinot rakstos?",
         "opcijas": ["Pēc komata", "Pēc pēdējā cipara",
                     "Pa kreisi", "Nav svarīgi"],
         "pareizi": 0,
         "padoms": "Vietas vērtībām jāsakrīt."},
        {"jaut": "−0,3 + 0,7 ir vienāds ar...",
         "opcijas": ["0,4", "−0,4", "1", "−1"],
         "pareizi": 0,
         "padoms": "0,7 − 0,3, zīme pluss."},
    ], pamats=4),

    Kopsavilkums([
        "Saskaitu un atņemu decimāldaļas ar zīmēm.",
        "Līdzinu komatus un rēķinu pa vietām.",
        "Lietoju to pašu zīmju likumu, kas veseliem skaitļiem.",
        "Pārrakstu atņemšanu par saskaitīšanu.",
    ]),

    Majas([
        "Izrēķini −3,4 + 1,9; −3,4 − 1,9 un 2,1 − (−0,9).",
        "Pieraksti katram, kāda bija rezultāta zīme un kāpēc.",
        "Atrodi laika ziņās divas temperatūras ar desmitdaļām un aprēķini "
        "to starpību.",
    ]),
]
