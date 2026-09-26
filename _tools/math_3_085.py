# -*- coding: utf-8 -*-
"""3. klase, 85. stunda: «Kur uz skaitļu taisnes ir puse?»

Daļa kā skaitlis, nevis kā figūras gabals. Skaitļu taisne ir tas modelis, kas
daļu pārvērš par *vietu*: starp 0 un 1 ir bezgalīgi daudz skaitļu, un daļas
ir pirmie no tiem, ko skolēns satiek.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kur uz skaitļu taisnes ir puse?"

MERKIS = ("Atliksim daļskaitli uz skaitļu taisnes un pamatosim tā vietu.")

SATURS = [
    Sakums("Vai starp 0 un 1 ir kādi skaitļi?",
           zimejums=taisne(0, 1, 1, [(0.5, "1/2")]),
           paraksts="Puse atrodas tieši pa vidu starp 0 un 1.",
           fakti=["Daļa ir skaitlis, tāpat kā 3 vai 17.",
                  "Īsta daļa vienmēr atrodas starp 0 un 1."]),

    Doma("Daļa ir vieta uz skaitļu taisnes",
         "Saucējs pasaka, cik daļās sadalīt posmu no 0 līdz 1; skaitītājs - "
         "cik daļas noskaitīt.",
         soli=[
             "Uzzīmē nogriezni no 0 līdz 1.",
             "Sadali to tik vienādās daļās, cik pasaka saucējs.",
             "Skaiti no nulles tik daļu, cik pasaka skaitītājs.",
             "Atzīmē punktu - tur atrodas daļa.",
         ],
         pieze="Tieši tāpēc {1|2} ir tieši pa vidu: posms sadalīts divās "
               "daļās, un noskaitīta viena."),

    Paraugs("Kur atrodas {3|4}?",
            uzd="Atzīmē uz skaitļu taisnes daļu {3|4}.",
            soli=[
                ("Posmu no 0 līdz 1 sadala 4 daļās",
                 "Saucējs ir 4."),
                ("Skaita trīs daļas no nulles",
                 "Skaitītājs ir 3."),
                ("Punkts ir starp {1|2} un 1",
                 "Trīs ceturtdaļas ir vairāk par pusi, bet mazāk par veselo."),
            ],
            atbilde="starp {1|2} un 1"),

    Zimejums("Ceturtdaļas uz taisnes",
             taisne(0, 1, 1, [(0.25, "1/4"), (0.5, "2/4"), (0.75, "3/4")]),
             paskaidro="Četras vienādas daļas starp 0 un 1; {2|4} sakrīt ar "
                       "{1|2}.",
             ievads="Posms sadalīts ceturtdaļās."),

    Ievadi("Kur atrodas daļa?", [
        {"jaut": "Cik daļās jāsadala posms no 0 līdz 1 daļai {3|5}?",
         "atb": ["5"], "padoms": "To pasaka saucējs."},
        {"jaut": "Cik daļas jānoskaita?", "atb": ["3"],
         "padoms": "To pasaka skaitītājs."},
        {"jaut": "Kura daļa sakrīt ar {1|2}: {2|4} vai {3|4}? Ieraksti "
                 "skaitītāju.",
         "atb": ["2"], "padoms": "Divas ceturtdaļas ir puse."},
        {"jaut": "Cik astotdaļu ir līdz {1|2}?", "atb": ["4"],
         "padoms": "8 : 2."},
        {"jaut": "Cik desmitdaļu ir līdz {1|2}?", "atb": ["5"],
         "padoms": "10 : 2."},
        {"jaut": "Cik ceturtdaļu ir vienā veselajā?", "atb": ["4"],
         "padoms": "Visas četras."},
    ], pamats=4),

    Varianti("Kur tā atrodas?", [
        {"jaut": "Kur atrodas {1|4}?",
         "opcijas": ["Starp 0 un {1|2}", "Starp {1|2} un 1",
                     "Uz 1", "Aiz 1"],
         "pareizi": 0, "padoms": "Viena ceturtdaļa ir mazāk par pusi."},
        {"jaut": "Kura daļa ir vistuvāk 1?",
         "opcijas": ["{7|8}", "{1|2}", "{1|8}", "{3|8}"],
         "pareizi": 0, "padoms": "Vistuvāk ir lielākā daļa."},
        {"jaut": "Kura daļa atrodas tieši pa vidu starp 0 un 1?",
         "opcijas": ["{1|2}", "{1|3}", "{1|4}", "{2|3}"],
         "pareizi": 0, "padoms": "Divas vienādas daļas."},
        {"jaut": "Kura daļa ir vienāda ar 1?",
         "opcijas": ["{5|5}", "{1|5}", "{5|1}", "{4|5}"],
         "pareizi": 0, "padoms": "Visas daļas ir noskaitītas."},
    ], pamats=4),

    Pasaule("Cik tālu ir skrējiens?",
            Ievadi("", [
                {"jaut": "Distance 400 m. Cik metru ir {1|2}?",
                 "atb": ["200"], "padoms": "400 : 2."},
                {"jaut": "Cik metru ir {1|4}?", "atb": ["100"],
                 "padoms": "400 : 4."},
                {"jaut": "Cik metru ir {3|4}?", "atb": ["300"],
                 "padoms": "3 · 100."},
                {"jaut": "Skrējējs ir 300 m no starta. Cik metru vēl "
                         "atlicis?",
                 "atb": ["100"], "padoms": "400 − 300."},
            ]),
            pavediens="sports",
            konteksts="Stadiona aplis ir 400 m, un skrējējam vienmēr saka, "
                      "cik daļas jau aiz muguras.",
            kapec="Daļa uz distances ir tā pati vieta, kas uz skaitļu "
                  "taisnes."),

    Kopsavilkums([
        "Atlieku daļskaitli uz skaitļu taisnes.",
        "Pamatoju daļas vietu ar saucēju un skaitītāju.",
        "Zinu, ka īsta daļa atrodas starp 0 un 1.",
        "Zinu, ka {2|4} un {1|2} ir viena un tā pati vieta.",
    ]),

    Majas([
        "Uzzīmē skaitļu taisni no 0 līdz 1 un atzīmē tajā {1|2} un {3|4}.",
        "Atzīmē uz tās pašas taisnes {1|8}.",
        "Pasaki, kura no trim daļām ir vistuvāk nullei.",
    ]),
]
