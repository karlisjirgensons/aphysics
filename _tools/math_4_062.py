# -*- coding: utf-8 -*-
"""4. klase, 62. stunda: «Kā uzzīmēt 40° leņķi?»

No mērīšanas uz zīmēšanu: novelk vienu malu, transportiera centru liek
galapunktā, pie vajadzīgā skaitļa atzīmē punktu un savieno. Tā pati skala,
kas mērot, tikai darbība otrādi. Pārbaude - spriedums «šaurs vai plats».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, lenkis)

TEMA = "Kā uzzīmēt 40° leņķi?"

MERKIS = ("Zīmēsim dota lieluma leņķi ar transportieri un pierakstīsim tā "
          "lielumu.")

SATURS = [
    Sakums("Kā dizaineris zīmē zvaigzni?",
           zimejums=lenkis([(0, ""), (36, "36°")], loki=[(0, 36, "")]),
           paraksts="Piecstaru zvaigznes smailē ir 36° leņķis.",
           fakti=["Precīzai zvaigznei visi smailes leņķi ir vienādi.",
                  "Tos zīmē ar transportieri, nevis uz aci."]),

    Doma("Mala, centrs, atzīme, savieno",
         "Lai uzzīmētu leņķi, novelc vienu malu, noliec transportieri un pie "
         "vajadzīgā skaitļa atzīmē punktu - caur to iet otrā mala.",
         soli=[
             "Novelc staru BA - tā būs viena mala.",
             "Transportiera centru liec punktā B, nulli - uz BA.",
             "Skalā, kas sākas ar 0 uz BA, atrodi 40 un atzīmē punktu C.",
             "Novelc staru BC un pieraksti: ∠ABC = 40°.",
         ],
         pieze="Pārbaude: 40° ir šaurs - zīmējumā leņķim jābūt mazākam par "
               "burtnīcas stūri."),

    Slidnis("Zīmējam 40° soli pa solim",
            soli=[
                {"v": "1. mala", "teksts": "Novelk staru BA.",
                 "zim": lenkis([(0, "A")])},
                {"v": "atzīme pie 40", "teksts": "Pie 40 uzliek punktu C.",
                 "zim": lenkis([(0, "A"), (40, "C")], r=34)},
                {"v": "∠ABC = 40°", "teksts": "Savieno B ar C - gatavs.",
                 "zim": lenkis([(0, "A"), (40, "C")],
                               loki=[(0, 40, "40°")])},
            ]),

    Varianti("Kas nav kārtībā?", [
        {"jaut": "Jānim vajadzēja 40°, bet sanāca plats leņķis. Kāpēc?",
         "opcijas": ["lasīja otru skalu (140°)", "lineāls par īsu",
                     "viss pareizi"], "pareizi": 0,
         "padoms": "40 + 140 = 180."},
        {"jaut": "Kur jāliek transportiera centrs, zīmējot leņķi?",
         "opcijas": ["malas galapunktā - virsotnē", "malas vidū",
                     "jebkur uz lapas"], "pareizi": 0,
         "padoms": "Tur būs virsotne."},
        {"jaut": "Vajag 120°. Kāds leņķis sanāks?",
         "opcijas": ["plats", "šaurs", "taisns"], "pareizi": 0,
         "padoms": "120 > 90."},
        {"jaut": "Kurš pieraksts pareizs?",
         "opcijas": ["∠MNK = 65°", "∠MNK = 65", "MNK = 65°",
                     "∠65° = MNK"], "pareizi": 0,
         "padoms": "Zīme, burti, grādi."},
    ], pamats=4),

    Ievadi("Plāno zīmējumu", [
        {"jaut": "Vajag 40°. Ja lasa nepareizo skalu, cik grādu sanāks?",
         "atb": ["140"], "padoms": "180 − 40."},
        {"jaut": "Uzzīmē 25° un 65° blakus (viena mala kopīga). Cik grādu "
                 "kopā?", "atb": ["90"], "padoms": "25 + 65."},
        {"jaut": "Cik grādu jāatzīmē, lai leņķis būtu par 15° mazāks nekā "
                 "taisns?", "atb": ["75"], "padoms": "90 − 15."},
        {"jaut": "Zvaigznes smailes leņķis 36°. Cik grādu piecās smailēs "
                 "kopā?", "atb": ["180"], "padoms": "5 · 36."},
    ]),

    Pasaule("Saules paneļa slīpums",
            Ievadi("", [
                {"jaut": "Latvijā saules paneļus ieteicams slīpināt ap 40°. "
                         "Cik grādu trūkst līdz taisnam leņķim?",
                 "atb": ["50"], "padoms": "90 − 40."},
                {"jaut": "Ziemā slīpumu palielina par 15°. Cik grādu tad?",
                 "atb": ["55"], "padoms": "40 + 15."},
                {"jaut": "Vasarā slīpumu samazina par 15° no 40°. Cik?",
                 "atb": ["25"], "padoms": "40 − 15."},
                {"jaut": "Par cik grādiem ziemas slīpums lielāks nekā "
                         "vasaras?", "atb": ["30"], "padoms": "55 − 25."},
            ]),
            pavediens="planeta",
            konteksts="Saules panelis ražo visvairāk, ja stāv pareizā leņķī "
                      "pret sauli - to uzstāda ar transportieri.",
            kapec="Pareizs leņķis dod vairāk elektrības no tās pašas "
                  "saules."),

    Petijums("Zīmē un pārbaudi",
             soli=[
                 "Uzzīmē leņķus 40°, 75°, 90° un 130°.",
                 "Katram pirms zīmēšanas pasaki: šaurs vai plats?",
                 "Apmainies ar klasesbiedru un izmēri viņa leņķus.",
                 "Salīdziniet: vai mērījumi sakrīt?",
             ],
             vajag="transportieris, lineāls, zīmulis",
             secinajums="Precīzs zīmējums - pirmā pārbaude, citu mērījums - "
                        "otrā."),

    Kopsavilkums([
        "Zīmēju dota lieluma leņķi ar transportieri.",
        "Pierakstu leņķa lielumu ar ∠ un grādiem.",
        "Pārbaudu, vai nav nolasīta nepareiza skala.",
    ]),

    Majas([
        "Uzzīmē piecstaru zvaigzni, kuras smailēs ir 36°.",
        "Uzzīmē 3 leņķus un palūdz mājiniekiem uzminēt to lielumu.",
        "Uzzīmē leņķi, kas ir tieši puse no taisnā.",
    ]),
]
