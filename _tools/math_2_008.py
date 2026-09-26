# -*- coding: utf-8 -*-
"""2. klase, 8. stunda: «Vai vari atšifrēt cita grupējumu?»

Apgrieztais uzdevums grupēšanai: grupas jau ir, bet pazīme noslēpta. Lai to
atrastu, jāsalīdzina grupas savā starpā - kas ir visiem vienā grupā un nav
nevienam otrā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes, restis)

TEMA = "Vai vari atšifrēt cita grupējumu?"

MERKIS = ("Šodien uzminēsim, pēc kādas pazīmes kāds cits sagrupējis "
          "priekšmetus vai skaitļus, un raksturosim katru grupu.")

SATURS = [
    Sakums("Pēc kā draugs sadalīja šīs figūras?",
           zimejums=bildes([["kvadrats", "trijsturis", "kvadrats*"],
                            ["aplis", "aplis*", "aplis"]],
                           uzraksti=["1. grupa", "2. grupa"]),
           paraksts="Pirmajā grupā visām ir stūri.",
           fakti=["Pazīme ir noslēpums, bet grupas to izstāsta.",
                  "Meklē, kas vienai grupai ir un otrai nav."]),

    Doma("Kā atšifrēt grupējumu",
         "Pazīme ir tā, kas ir visiem vienā grupā un nav nevienam otrā.",
         soli=[
             "Apskati pirmo grupu - kas visiem kopīgs?",
             "Apskati otro grupu - vai tur tā ir kādam?",
             "Ja nav nevienam - pazīme atrasta.",
             "Pārbaudi ar jaunu priekšmetu: kur tu to liktu?",
         ]),

    Varianti("Atšifrē pazīmi", [
        {"jaut": "1. grupa: 12, 42, 72. 2. grupa: 15, 45, 75.",
         "opcijas": ["pēdējais cipars 2 vai 5", "lielāki nekā 40",
                     "divciparu vai viencipara"], "pareizi": 0,
         "padoms": "Salīdzini pēdējos ciparus."},
        {"jaut": "1. grupa: 3, 8, 6. 2. grupa: 30, 80, 60.",
         "opcijas": ["viencipara un divciparu", "beidzas ar 3",
                     "mazāki nekā 5"], "pareizi": 0,
         "padoms": "Saskaiti ciparus."},
        {"jaut": "1. grupa: vista, pīle, zoss. 2. grupa: govs, zirgs, aita.",
         "opcijas": ["2 kājas vai 4 kājas", "lido vai peld",
                     "liels vai mazs"], "pareizi": 0,
         "padoms": "Saskaiti kājas."},
        {"jaut": "1. grupa: 21, 25, 29. 2. grupa: 51, 55, 59.",
         "opcijas": ["sākas ar 2 vai ar 5", "beidzas ar 1",
                     "lielāki nekā 50"], "pareizi": 0,
         "padoms": "Salīdzini pirmos ciparus."},
        {"jaut": "1. grupa: janvāris, jūnijs, jūlijs. 2. grupa: marts, "
                 "maijs.",
         "opcijas": ["sākas ar j vai ar m", "ziemas vai vasaras mēneši",
                     "garš vai īss vārds"], "pareizi": 0,
         "padoms": "Paskaties pirmo burtu."},
        {"jaut": "1. grupa: 10, 11, 12. 2. grupa: 90, 91, 92.",
         "opcijas": ["mazāki vai lielāki nekā 50", "beidzas ar 0",
                     "viencipara"], "pareizi": 0,
         "padoms": "Salīdzini, cik lieli tie ir."},
    ], pamats=4),

    Ievadi("Kur liktu jauno?", [
        {"jaut": "1. grupa: 14, 24, 34. 2. grupa: 17, 27, 37. Kurā grupā "
                 "liktu 44? Raksti grupas numuru.", "atb": ["1"],
         "padoms": "Pēdējais cipars 4."},
        {"jaut": "Tās pašas grupas. Kurā grupā liktu 57?", "atb": ["2"],
         "padoms": "Pēdējais cipars 7."},
    ]),

    Pasaule("Kā sakārtota skolas bibliotēka?",
            Varianti("", [
                {"jaut": "Pēc kā grāmatas sadalītas plauktos?",
                 "opcijas": ["pēc tā, par ko ir grāmata",
                             "pēc lapu skaita", "pēc krāsas"],
                 "pareizi": 0, "padoms": "Nolasi plauktu nosaukumus."},
                {"jaut": "Kurā plauktā liksi grāmatu «Planētas»?",
                 "opcijas": ["daba un kosmoss", "pasakas", "sports"],
                 "pareizi": 0, "padoms": "Planētas ir kosmosā."},
            ]),
            pavediens="skola",
            zimejums=restis([["pasakas", "daba un kosmoss", "sports"],
                             ["Pelnrušķīte", "Putni", "Futbols"],
                             ["Sprīdītis", "Mēness", "Hokejs"]]),
            konteksts="Skolas bibliotēkā grāmatas saliktas trīs plauktos.",
            kapec="Atšifrējot grupējumu, grāmatu atrod bez meklēšanas."),

    Kopsavilkums([
        "Nosaku pazīmi, pēc kuras sagrupēts.",
        "Raksturoju katru grupu.",
        "Ievietoju jaunu priekšmetu pareizajā grupā.",
    ]),

    Majas([
        "Sagrupē 8 priekšmetus pēc slepenas pazīmes.",
        "Lai mājinieks atšifrē tavu pazīmi.",
        "Tad apmainieties lomām.",
    ]),
]
