# -*- coding: utf-8 -*-
"""2. klase, 6. stunda: «Kā skaitļus sadalīt divās grupās?»

Skaitļus ievieto Venna diagrammā un meklē tādu pazīmju pāri, kurā grupas
nepārklājas - katrs skaitlis ir tieši vienā grupā. Ja pazīmes izvēlas
neuzmanīgi, kopīgā daļa nav tukša, un tas ir jāpamana.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, venna)

TEMA = "Kā skaitļus sadalīt divās grupās?"

MERKIS = ("Šodien ievietosim skaitļus Venna diagrammā un izdomāsim "
          "sadalījumu divās grupās, kas nepārklājas.")

_JA_NE = ["Jā, katrs ir tikai vienā", "Nē, kādam der abas"]

SATURS = [
    Sakums("Vai var būt skaitlis, kas ir gan viencipara, gan divciparu?",
           zimejums=venna([3, 7, 9], [12, 45, 80], [], ("viencipara",
                                                        "divciparu")),
           paraksts="Kopīgā daļa ir tukša - tādu skaitļu nav.",
           fakti=["Dažas grupas pārklājas, dažas - nekad.",
                  "Ja nepārklājas, katrs skaitlis ir tieši vienā grupā."]),

    Doma("Grupas, kas nepārklājas",
         "Sadalījums ir labs, ja katrs skaitlis nonāk tieši vienā grupā.",
         soli=[
             "Izvēlies pazīmi pirmajai grupai.",
             "Otrā grupa - tie, kam šīs pazīmes nav.",
             "Pārbaudi katru skaitli: vai tas der tikai vienai grupai?",
             "Kopīgā daļa paliek tukša.",
         ],
         pieze="«Beidzas ar 0» un «mazāks nekā 50» pārklājas - skaitlis 20 "
               "der abām grupām."),

    Varianti("Kur ievietot?", [
        {"jaut": "Grupas: «mazāks nekā 50» un «beidzas ar 0». Kur ir 20?",
         "opcijas": ["kopīgajā daļā", "tikai «mazāks nekā 50»",
                     "tikai «beidzas ar 0»", "ārpus apļiem"],
         "jaukt": False, "pareizi": 0, "padoms": "20 der abām."},
        {"jaut": "Tās pašas grupas. Kur ir 73?",
         "opcijas": ["kopīgajā daļā", "tikai «mazāks nekā 50»",
                     "tikai «beidzas ar 0»", "ārpus apļiem"],
         "jaukt": False, "pareizi": 3, "padoms": "73 neder nevienai."},
        {"jaut": "Tās pašas grupas. Kur ir 90?",
         "opcijas": ["kopīgajā daļā", "tikai «mazāks nekā 50»",
                     "tikai «beidzas ar 0»", "ārpus apļiem"],
         "jaukt": False, "pareizi": 2, "padoms": "90 nav mazāks nekā 50."},
        {"jaut": "Tās pašas grupas. Kur ir 14?",
         "opcijas": ["kopīgajā daļā", "tikai «mazāks nekā 50»",
                     "tikai «beidzas ar 0»", "ārpus apļiem"],
         "jaukt": False, "pareizi": 1, "padoms": "14 nebeidzas ar 0."},
    ]),

    Varianti("Vai grupas nepārklājas?", [
        {"jaut": "«mazāks nekā 30» un «lielāks nekā 40»",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 0,
         "padoms": "Vai kāds skaitlis ir gan mazāks nekā 30, gan lielāks "
                   "nekā 40?"},
        {"jaut": "«sākas ar 2» un «beidzas ar 2»",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 1,
         "padoms": "Padomā par 22."},
        {"jaut": "«viencipara» un «lielāks nekā 5»",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 1,
         "padoms": "Padomā par 7."},
        {"jaut": "«beidzas ar 5» un «beidzas ar 0»",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 0,
         "padoms": "Skaitlim ir tikai viens pēdējais cipars."},
    ]),

    Ievadi("Nolasi diagrammu", [
        {"jaut": "Cik skaitļu ir kopīgajā daļā?",
         "zim": venna([5, 15], [30, 60], [10, 20, 40], ("mazāks nekā 50",
                                                         "beidzas ar 0")),
         "atb": ["3"], "padoms": "Skaiti vidū."},
        {"jaut": "Cik skaitļu beidzas ar 0?",
         "zim": venna([5, 15], [30, 60], [10, 20, 40], ("mazāks nekā 50",
                                                         "beidzas ar 0")),
         "atb": ["5"], "padoms": "Viss labais aplis: 2 + 3."},
    ]),

    Pasaule("Kā sadalīt komandas?",
            Varianti("", [
                {"jaut": "Kurš sadalījums der, lai katrs būtu tieši vienā "
                         "komandā?",
                 "opcijas": ["numurs mazāks nekā 13 / numurs 13 vai lielāks",
                             "numurs beidzas ar 1 / numurs mazāks nekā 10",
                             "numurs sākas ar 1 / numurs beidzas ar 1"],
                 "pareizi": 0, "padoms": "Pārbaudi numuru 11."},
                {"jaut": "Cik bērnu būs katrā komandā?",
                 "opcijas": ["12 un 12", "13 un 11", "10 un 14"],
                 "pareizi": 0, "padoms": "No 1 līdz 12 un no 13 līdz 24."},
            ]),
            pavediens="sports",
            konteksts="Sporta stundā 24 bērniem ir numuri no 1 līdz 24. "
                      "Skolotājs grib divas komandas.",
            kapec="Labs sadalījums nevienu neatstāj ārpusē un nevienu "
                  "neieliek divreiz."),

    Kopsavilkums([
        "Ievietoju skaitļus Venna diagrammā.",
        "Izdomāju divas grupas, kas nepārklājas.",
        "Pamanu, ja kāds skaitlis der abām grupām.",
    ]),

    Majas([
        "Uzraksti 10 skaitļus no kalendāra.",
        "Sadali tos divās grupās, kas nepārklājas.",
        "Lai mājinieks uzmin, pēc kādas pazīmes tu dalīji.",
    ]),
]
