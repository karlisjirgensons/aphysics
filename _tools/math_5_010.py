# -*- coding: utf-8 -*-
"""5. klase, 10. stunda: «Kas atšķir decimālo sistēmu no romiešu?»

Mikrotemata kopsavilkuma stunda. Te salīdzina trīs jau redzētas sistēmas un
nosauc to, kas decimālo padara ērtu: vietas nozīme un nulle. Ar to arī
noslēdzas atbilde uz 1. stundas jautājumu, kāpēc ciparu vieta ir svarīga.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, kolonnas)

TEMA = "Kas atšķir decimālo sistēmu no romiešu?"

MERKIS = ("Salīdzināsim decimālo, bināro un romiešu pierakstu un pateiksim, "
          "kāpēc rēķinos lieto tieši decimālo.")

SATURS = [
    Sakums("Kāpēc pasaule pārgāja uz mūsu cipariem?",
           zimejums=kolonnas([("mūsu", 2), ("binārais", 4), ("romiešu", 3)]),
           paraksts="Zīmju skaits skaitlim 14: 14, 1110 un XIV.",
           fakti=["Viens daudzums, trīs pieraksti.",
                  "Rakstiski rēķināt var tikai tur, kur ir vietas nozīme."]),

    Doma("Vietas nozīme un nulle padara rēķināšanu iespējamu",
         "Decimālajā sistēmā cipara vērtību nosaka tā vieta, un nulle "
         "notur vietu tukšu.",
         soli=[
             "Decimālā: desmit cipari, vietas 1, 10, 100 - ir nulle.",
             "Binārā: divi cipari, vietas 1, 2, 4 - arī ir nulle un vietas "
             "nozīme.",
             "Romiešu: septiņas zīmes, vietas nozīmes nav, nulles nav.",
             "Tieši nulle un vietas nozīme ļauj rēķināt stabiņā.",
         ],
         pieze="Romiešu pierakstā nevar uzrakstīt «tukšu vietu», tāpēc "
               "skaitli 205 ar vietu sistēmu nav kā parādīt - raksta CCV."),

    Varianti("Kura sistēma?", [
        {"jaut": "Kurā sistēmā ir tikai divi cipari?",
         "opcijas": ["Binārajā", "Decimālajā", "Romiešu", "Visās trijās"],
         "pareizi": 0,
         "padoms": "0 un 1."},
        {"jaut": "Kurā no šīm sistēmām nav nulles?",
         "opcijas": ["Romiešu", "Decimālajā", "Binārajā", "Nevienā"],
         "pareizi": 0,
         "padoms": "Padomā, kā romieši rakstītu «nekā»."},
        {"jaut": "Kas ir kopīgs decimālajai un binārajai sistēmai?",
         "opcijas": ["Cipara vērtību nosaka tā vieta",
                     "Abās ir desmit cipari",
                     "Abās lieto burtus",
                     "Abās nav nulles"],
         "pareizi": 0,
         "padoms": "Abās katra nākamā vieta ir vairāk vērta."},
        {"jaut": "Kāpēc ar romiešu cipariem neraksta aprēķinus?",
         "opcijas": ["Nav vietas nozīmes, tāpēc nevar rēķināt stabiņā",
                     "Tie ir par gariem",
                     "Tos grūti izlasīt",
                     "Tajos ir pārāk daudz zīmju"],
         "pareizi": 0,
         "padoms": "Stabiņā rēķina pa vietām."},
        {"jaut": "Kurā sistēmā skaitlis 8 rakstās visīsāk?",
         "opcijas": ["Decimālajā", "Binārajā", "Romiešu",
                     "Visās vienādi"],
         "pareizi": 0,
         "padoms": "Decimālā: 8; binārā: 1000; romiešu: VIII."},
        {"jaut": "Kas notiek ar skaitli, ja decimālajā pierakstā beigās "
                 "pieliek nulli?",
         "opcijas": ["Tas kļūst desmit reizes lielāks",
                     "Tas nemainās",
                     "Tas kļūst par vienu lielāks",
                     "Tas kļūst desmit reizes mazāks"],
         "pareizi": 0,
         "padoms": "Visi cipari pārceļas uz nākamo vietu."},
    ], pamats=4),

    Ievadi("Viens skaitlis, trīs pieraksti", [
        {"jaut": "XII - kāds tas ir decimālajā pierakstā?", "atb": ["12"],
         "padoms": "10 + 1 + 1."},
        {"jaut": "Binārais 110 - kāds decimālajā pierakstā?", "atb": ["6"],
         "padoms": "4 + 2."},
        {"jaut": "Cik zīmju vajag, lai uzrakstītu 8 ar romiešu cipariem?",
         "atb": ["4"], "padoms": "VIII."},
        {"jaut": "Cik ciparu ir binārajam skaitlim, kas atbilst decimālajam "
                 "8?", "atb": ["4"], "padoms": "1000."},
    ]),

    Pasaule("Kurš pieraksts ir īsākais?",
            Ievadi("", [
                {"jaut": "Cik ciparu ir skaitlim 1 000 mūsu pierakstā?",
                 "atb": ["4"], "padoms": "1, 0, 0, 0."},
                {"jaut": "Cik zīmju ir skaitlim 1 000 romiešu pierakstā?",
                 "atb": ["1"], "padoms": "M."},
                {"jaut": "Cik ciparu ir skaitlim 8 binārajā pierakstā?",
                 "atb": ["4"], "padoms": "1000."},
                {"jaut": "Cik zīmju ir skaitlim 8 romiešu pierakstā?",
                 "atb": ["4"], "padoms": "VIII."},
            ]),
            pavediens="dati",
            konteksts="Dators glabā bināri, cilvēks raksta decimāli, bet "
                      "vecos uzrakstos vēl ir romiešu cipari.",
            kapec="Katra sistēma ir ērta savam darbam - universālas nav."),

    Kopsavilkums([
        "Zinu, ka viens daudzums var būt pierakstīts dažādās sistēmās.",
        "Nosaucu decimālās sistēmas divas priekšrocības: vietas nozīme un "
        "nulle.",
        "Paskaidroju, kāpēc ar romiešu cipariem nerēķina stabiņā.",
    ]),

    Majas([
        "Uzraksti skaitli 2026 visās trijās sistēmās, ja vari.",
        "Padomā, kā romieši būtu uzrakstījuši skaitli nulle.",
        "Pameklē, kādas vēl skaitļu pieraksta sistēmas ir bijušas pasaulē.",
    ]),
]
