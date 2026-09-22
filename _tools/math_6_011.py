# -*- coding: utf-8 -*-
"""6. klase, 11. stunda: «Kad otrs lielums aug tikpat reižu?»

Jauns mikrotemats. Attiecība bija par vienu mirkli; proporcionalitāte ir par
visu tabulu. Stunda sākas ar šķirošanu - kur tā ir un kur nav -, jo tieši
šeit visbiežāk kļūdās: ne viss, kas aug, aug proporcionāli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti)

TEMA = "Kad otrs lielums aug tikpat reižu?"

MERKIS = ("Mācīsimies atšķirt tieši proporcionālus lielumus no pārējiem un "
          "minēt piemērus no dzīves.")

SATURS = [
    Sakums("Divas reizes vairāk kilometru - divas reizes vairāk degvielas?",
           fakti=["Elektroauto patērē apmēram 15 kWh uz 100 km.",
                  "Divas reizes garāks ceļš - divas reizes vairāk enerģijas.",
                  "Bet divas reizes ātrāks brauciens nemaksā divas reizes "
                  "mazāk."]),

    Doma("Tikpat reižu - un ne citādi",
         "Divi lielumi ir tieši proporcionāli, ja, vienam pieaugot n reižu, "
         "otrs pieaug tieši tikpat reižu.",
         soli=[
             "Paņem divus situācijas skaitļu pārus.",
             "Noskaidro, cik reižu pieauga pirmais lielums.",
             "Noskaidro, cik reižu pieauga otrais.",
             "Ja abi skaitļi sakrīt katrā pārī, lielumi ir proporcionāli.",
             "Pārbaudi arī galējo gadījumu: nullei jāatbilst nulle.",
         ],
         pieze="Vecums un auguma garums nav proporcionāli: divreiz vecāks "
               "cilvēks nav divreiz garāks. Tieši tāpēc katru situāciju "
               "pārbauda, nevis min."),

    Slidnis("Vairāk kilometru - vairāk enerģijas",
            [{"v": "100 km", "teksts": "15 kWh · 1 = 15 kWh", "josla": 25},
             {"v": "200 km", "teksts": "15 kWh · 2 = 30 kWh", "josla": 50},
             {"v": "300 km", "teksts": "15 kWh · 3 = 45 kWh", "josla": 75},
             {"v": "400 km", "teksts": "15 kWh · 4 = 60 kWh", "josla": 100}],
            ievads="Spied soli pa solim: cik reižu aug ceļš, tikpat reižu aug "
                   "arī enerģija. Josla aug vienmērīgi - tā izskatās tieša "
                   "proporcionalitāte."),

    Paraugs("Vai šie lielumi ir proporcionāli?",
            uzd="Par 3 burtnīcām maksā 2,40 €, par 6 burtnīcām - 4,80 €, "
                "par 9 burtnīcām - 7,20 €. Vai skaits un cena ir tieši "
                "proporcionāli?",
            soli=[
                ("3 → 6: skaits aug 2 reizes",
                 "Salīdzina pirmos divus pārus."),
                ("2,40 → 4,80: cena aug 2 reizes",
                 "Tikpat reižu - pagaidām sakrīt."),
                ("3 → 9: skaits aug 3 reizes; 2,40 → 7,20: arī 3 reizes",
                 "Pārbauda vēl vienu pāri."),
                ("Vienai burtnīcai vienmēr 0,80 €",
                 "Dalījums ir nemainīgs - tā ir pazīme."),
            ],
            atbilde="jā, lielumi ir tieši proporcionāli"),

    Varianti("Proporcionāli vai nē?", [
        {"jaut": "Nopirkto biļešu skaits un samaksātā summa.",
         "opcijas": ["Proporcionāli", "Nav proporcionāli",
                     "Tikai dažreiz", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Katra biļete maksā vienādi."},
        {"jaut": "Cilvēka vecums un viņa auguma garums.",
         "opcijas": ["Nav proporcionāli", "Proporcionāli",
                     "Proporcionāli līdz 18 gadiem", "Vienmēr vienādi"],
         "pareizi": 0,
         "padoms": "Divreiz vecāks nav divreiz garāks."},
        {"jaut": "Kvadrāta malas garums un tā laukums.",
         "opcijas": ["Nav proporcionāli", "Proporcionāli",
                     "Proporcionāli tikai lieliem kvadrātiem",
                     "Laukums nemainās"],
         "pareizi": 0,
         "padoms": "Divreiz garāka mala dod četrreiz lielāku laukumu."},
        {"jaut": "Strādāto stundu skaits un nopelnītā summa ar vienādu "
                 "stundas likmi.",
         "opcijas": ["Proporcionāli", "Nav proporcionāli",
                     "Tikai virs 8 stundām", "Nav nosakāmi"],
         "pareizi": 0,
         "padoms": "Katra stunda maksā vienādi."},
    ], pamats=4),

    Ievadi("Cik reižu pieauga?", [
        {"jaut": "Ceļš pieauga no 50 km uz 150 km. Cik reižu?",
         "atb": ["3"], "padoms": "150 : 50."},
        {"jaut": "Ja lielumi ir proporcionāli, cik reižu pieaugs degviela?",
         "atb": ["3"], "padoms": "Tikpat reižu, cik ceļš."},
        {"jaut": "4 kg kartupeļu maksā 3 €. Cik eiro maksā 8 kg?",
         "atb": ["6"], "padoms": "Masa aug 2 reizes."},
        {"jaut": "Cik eiro maksā 12 kg?",
         "atb": ["9"], "padoms": "Masa aug 3 reizes salīdzinot ar 4 kg."},
        {"jaut": "2 m auduma maksā 7 €. Cik eiro maksā 6 m?",
         "atb": ["21"], "padoms": "Garums aug 3 reizes."},
        {"jaut": "Ja 5 vienādas kastes sver 40 kg, cik kg sver 1 kaste?",
         "atb": ["8"], "padoms": "40 : 5."},
    ], pamats=4),

    Pasaule("Cik enerģijas prasīs brauciens?",
            Ievadi("", [
                {"jaut": "Elektroauto uz 100 km patērē 15 kWh. Cik kWh "
                         "vajag 300 km?",
                 "atb": ["45"], "padoms": "3 · 15."},
                {"jaut": "Cik kWh vajag 50 km?",
                 "atb": ["7,5", "7.5"], "padoms": "Puse no 15."},
                {"jaut": "Baterijā ir 60 kWh. Cik km var nobraukt?",
                 "atb": ["400"], "padoms": "60 : 15 = 4; 4 · 100."},
                {"jaut": "Cik kWh vajag, lai nobrauktu 250 km?",
                 "atb": ["37,5", "37.5"], "padoms": "2,5 · 15."},
            ]),
            pavediens="celojums",
            konteksts="Pirms gara brauciena vadītājs rēķina nevis litrus, "
                      "bet to, cik reižu garāks ir ceļš.",
            kapec="Proporcionalitāte ļauj no viena mērījuma iegūt visus "
                  "pārējos."),

    Kopsavilkums([
        "Zinu, ka tieši proporcionāli lielumi aug tikpat reižu.",
        "Pārbaudu proporcionalitāti ar vairākiem skaitļu pāriem.",
        "Minu piemērus no dzīves un pamatoju, kāpēc tie der.",
        "Atpazīstu situācijas, kurās proporcionalitātes nav.",
    ]),

    Majas([
        "Atrodi veikala čekā divas rindas ar vienu un to pašu preci un "
        "pārbaudi proporcionalitāti.",
        "Izdomā divus lielumus, kas *nav* proporcionāli, un paskaidro, kāpēc.",
        "Pieraksti, cik reižu palielinās tavs ceļš uz skolu, ja ej turp un "
        "atpakaļ divas reizes dienā.",
    ]),
]
