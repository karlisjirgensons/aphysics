# -*- coding: utf-8 -*-
"""7. klase, 16. stunda: «Kāda ir droša un neiespējama notikuma varbūtība?»

Drošam notikumam labvēlīgi ir visi iznākumi - P = 1; neiespējamam neviens -
P = 0. Tāpēc jebkuras varbūtības vērtība ir starp tiem. No tā izriet arī
pretējais notikums: P(nav A) = 1 − P(A).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala)

TEMA = "Kāda ir droša un neiespējama notikuma varbūtība?"

MERKIS = ("Noteiksim droša un neiespējama notikuma varbūtību un "
          "iemācīsimies aprēķināt pretējā notikuma varbūtību.")

SATURS = [
    Sakums("Izvelc zīmuli no penāļa, kurā ir tikai zīmuļi",
           fakti=["Zīmuli izvilksi noteikti: P = 1.",
                  "Lineālu neizvilksi nekad: P = 0.",
                  "Visas citas varbūtības ir starp 0 un 1."]),

    Doma("0 ≤ P(A) ≤ 1",
         "Drošam notikumam P = {n|n} = 1, neiespējamam P = {0|n} = 0. "
         "Pretējais notikums «nav A» notiek tieši tad, kad A nenotiek, "
         "un P(nav A) = 1 − P(A).",
         soli=[
             "Ja labvēlīgi ir visi iznākumi - notikums ir drošs, P = 1.",
             "Ja neviens - neiespējams, P = 0.",
             "Pretējā notikuma labvēlīgie ir visi pārējie iznākumi.",
             "Tāpēc P(A) + P(nav A) = 1.",
         ],
         pieze="Pretējā notikuma formula ir ērta, ja «nav A» ir vieglāk "
               "saskaitīt: «vismaz viens» ir pretējs «neviens»."),

    Zimejums("Visi iznākumi = A un nav A",
             dala(6, 1, "P(6) = 1/6, P(nav 6) = 5/6"),
             paskaidro="Kauliņam: viens lauciņš sešiniekam, pieci - "
                       "pārējiem. Kopā viss - 1."),

    Paraugs("Pretējais notikums",
            uzd="Met divas monētas. Kāda ir varbūtība, ka vismaz vienā "
                "uzkritīs ģerbonis?",
            soli=[
                ("Iznākumi: ĢĢ, ĢC, CĢ, CC - n = 4", "Vienādi iespējami."),
                ("Pretējais: «neviens ģerbonis» - tikai CC",
                 "To saskaitīt ir vieglāk."),
                ("P(nav A) = {1|4}", "Viens no četriem."),
                ("P(A) = 1 − {1|4} = {3|4}", "Pretējā notikuma formula."),
            ],
            atbilde="{3|4} = 75 %"),

    Varianti("Drošs, neiespējams vai gadījuma?", [
        {"jaut": "Metot kauliņu, uzkritīs skaitlis, mazāks nekā 7.",
         "opcijas": ["Drošs, P = 1", "Neiespējams, P = 0",
                     "Gadījuma, 0 < P < 1"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Visi skaitļi uz kauliņa ir mazāki nekā 7."},
        {"jaut": "Metot divus kauliņus, summa būs 1.",
         "opcijas": ["Drošs, P = 1", "Neiespējams, P = 0",
                     "Gadījuma, 0 < P < 1"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Mazākā summa ir 2."},
        {"jaut": "Nejauši izvēlēts cilvēks ir dzimis pirmdienā.",
         "opcijas": ["Drošs, P = 1", "Neiespējams, P = 0",
                     "Gadījuma, 0 < P < 1"],
         "pareizi": 2, "jaukt": False,
         "padoms": "Var būt, var nebūt."},
        {"jaut": "Starp 13 cilvēkiem divi ir dzimuši vienā mēnesī.",
         "opcijas": ["Drošs, P = 1", "Neiespējams, P = 0",
                     "Gadījuma, 0 < P < 1"],
         "pareizi": 0, "jaukt": False,
         "padoms": "12 mēneši, 13 cilvēki - kādā mēnesī noteikti divi."},
    ], pamats=4),

    Ievadi("Pretējā notikuma varbūtība", [
        {"jaut": "P(A) = 0,35. Cik ir P(nav A)?",
         "atb": ["0,65"], "padoms": "1 − 0,35."},
        {"jaut": "P(A) = {2|7}. Cik ir P(nav A)? (daļā)",
         "atb": ["{5|7}", "5/7"], "padoms": "1 − {2|7}."},
        {"jaut": "Met trīs monētas. P(vismaz viens ģerbonis) = ? (daļā)",
         "atb": ["{7|8}", "7/8"], "padoms": "Pretējais - CCC, {1|8}."},
        {"jaut": "Lietus varbūtība 15 %. Cik % nelīs (tikai skaitli)?",
         "atb": ["85"], "padoms": "100 − 15."},
    ], ievads="Daļu raksti ar slīpsvītru: 5/7."),

    Pasaule("Kvalitātes kontrole",
            Ievadi("", [
                {"jaut": "Rūpnīcā brāķa varbūtība ir 0,02. Kāda ir "
                         "varbūtība, ka detaļa ir laba?",
                 "atb": ["0,98"], "padoms": "1 − 0,02."},
                {"jaut": "Cik labu detaļu, visticamāk, būs no 5000?",
                 "atb": ["4900"], "padoms": "0,98 · 5000."},
                {"jaut": "Uzlabotā līnijā brāķa varbūtība ir 0. Kāds ir "
                         "notikums «detaļa ir laba»?",
                 "atb": ["drošs"], "padoms": "Varbūtība 1."},
            ]),
            pavediens="tehnika",
            konteksts="Viedtālruņu rūpnīcā testē katru ierīci un skaita, "
                      "cik ir brāķa.",
            kapec="«Laba» un «brāķis» ir pretēji notikumi - kopā 1."),

    Kopsavilkums([
        "Zinu, ka drošam notikumam P = 1, neiespējamam P = 0.",
        "Zinu, ka 0 ≤ P(A) ≤ 1.",
        "Lietoju P(nav A) = 1 − P(A).",
        "Ar pretējo notikumu risinu «vismaz viens» uzdevumus.",
    ]),

    Majas([
        "Izdomā vienu drošu un vienu neiespējamu notikumu ar kauliņu.",
        "Aprēķini P(vismaz viens sešinieks), metot divus kauliņus.",
        "Paskaidro, kāpēc varbūtība nevar būt 1,5.",
    ]),
]
