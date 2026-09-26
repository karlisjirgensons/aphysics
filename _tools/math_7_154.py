# -*- coding: utf-8 -*-
"""7. klase, 154. stunda: «Kādas ir nevienādību īpašības?»

Skaitlisku nevienādību īpašības: abām pusēm var pieskaitīt vienu un to pašu
skaitli un reizināt ar pozitīvu skaitli - zīme saglabājas. Uz skaitļu
taisnes tas ir abu punktu pārbīdīšana vai «izstiepšana».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kādas ir nevienādību īpašības?"

MERKIS = ("Formulēsim un pamatosim skaitlisku nevienādību īpašības, "
          "izmantojot skaitļu taisni.")

SATURS = [
    Sakums("2 < 5. Pieskaiti 3 abām pusēm: 5 < 8",
           zimejums=taisne(0, 10, 1, [(2, "2"), (5, "5")],
                           bultas=[(2, 5, "+3"), (5, 8, "+3")]),
           paraksts="Abi punkti pārbīdās pa labi - secība saglabājas.",
           fakti=["Pieskaitot vienu skaitli, attālums nemainās.",
                  "Reizinot ar pozitīvu - attālums izstiepjas, secība paliek.",
                  "Reizinot ar negatīvu - secība apgriežas (nākamā stunda)."]),

    Doma("Īpašības",
         "Ja a < b, tad: 1) a + c < b + c jebkuram c; 2) ac < bc, ja c > 0. "
         "Tāpat ar >, ≤, ≥. Tranzitivitāte: ja a < b un b < c, tad a < c.",
         soli=[
             "Pieskaitīt vai atņemt vienu skaitli abām pusēm - zīme nemainās.",
             "Reizināt vai dalīt abas puses ar pozitīvu - zīme nemainās.",
             "Uz taisnes: pārbīde vai izstiepšana nemaina secību.",
         ],
         pieze="Tās pašas darbības, ko lietojām vienādojumiem, tikai "
               "reizinot jāuzmanās ar zīmi."),

    Paraugs("Pamato",
            uzd="Zināms, ka a < b. Salīdzini a − 7 un b − 7; 3a un 3b.",
            soli=[
                ("a − 7 < b − 7", "(abām pusēm − 7)"),
                ("3a < 3b", "(abas puses · 3, 3 > 0)"),
            ],
            atbilde="a − 7 < b − 7; 3a < 3b"),

    Varianti("Kura zīme?", [
        {"jaut": "x < y. Kā saistīti x + 4 un y + 4?",
         "opcijas": ["x + 4 < y + 4", "x + 4 > y + 4", "Vienādi",
                     "Nevar zināt"],
         "pareizi": 0, "padoms": "Pieskaita."},
        {"jaut": "m > n. Kā saistīti {m|2} un {n|2}?",
         "opcijas": ["{m|2} > {n|2}", "{m|2} < {n|2}", "Vienādi",
                     "Nevar zināt"],
         "pareizi": 0, "padoms": "Dala ar pozitīvu."},
        {"jaut": "a < b un b < 10. Ko var secināt?",
         "opcijas": ["a < 10", "a > 10", "a = 10", "Neko"],
         "pareizi": 0, "padoms": "Tranzitivitāte."},
        {"jaut": "p ≥ q. Kā saistīti 5p − 1 un 5q − 1?",
         "opcijas": ["5p − 1 ≥ 5q − 1", "5p − 1 ≤ 5q − 1", "Vienādi",
                     "Nevar zināt"],
         "pareizi": 0, "padoms": "· 5, tad − 1."},
    ], pamats=4),

    Ievadi("Aprēķini robežas", [
        {"jaut": "2 < x < 5. Kāda ir mazākā robeža izteiksmei x + 10?",
         "atb": ["12"], "padoms": "2 + 10."},
        {"jaut": "2 < x < 5. Lielākā robeža izteiksmei 3x?",
         "atb": ["15"], "padoms": "3 · 5."},
        {"jaut": "Ja x ≥ 4, tad 2x + 1 ≥ ?",
         "atb": ["9"], "padoms": "2 · 4 + 1."},
    ]),

    Pasaule("Algu salīdzināšana",
            Varianti("", [
                {"jaut": "Annai alga lielāka nekā Pēterim. Abiem pielika pa "
                         "100 €. Kurš tagad pelna vairāk?",
                 "opcijas": ["Joprojām Anna", "Pēteris", "Vienādi",
                             "Nevar zināt"],
                 "pareizi": 0, "padoms": "Pieskaitot secība saglabājas."},
                {"jaut": "Abiem algu palielina par 10 % (· 1,1). Kurš pelna "
                         "vairāk?",
                 "opcijas": ["Joprojām Anna", "Pēteris", "Vienādi",
                             "Nevar zināt"],
                 "pareizi": 0, "padoms": "Reizina ar pozitīvu."},
                {"jaut": "Starpība pēc +10 % ...",
                 "opcijas": ["palielinās", "samazinās", "nemainās",
                             "kļūst 0"],
                 "pareizi": 0, "padoms": "Izstiepjas."},
            ]),
            pavediens="veikals",
            konteksts="Vienāds pielikums saglabā starpību, procentuāls to "
                      "palielina.",
            kapec="Nevienādību īpašības apraksta taisnīgumu."),

    Kopsavilkums([
        "Pieskaitu vienu skaitli abām pusēm - zīme nemainās.",
        "Reizinu ar pozitīvu - zīme nemainās.",
        "Lietoju tranzitivitāti.",
        "Pamatoju īpašības uz skaitļu taisnes.",
    ]),

    Majas([
        "Ja 3 < x < 7, atrodi robežas 2x − 5.",
        "Pamato uz skaitļu taisnes: a < b ⇒ a + 5 < b + 5.",
        "Izdomā piemēru ar tranzitivitāti.",
    ]),
]
