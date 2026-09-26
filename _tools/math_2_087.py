# -*- coding: utf-8 -*-
"""2. klase, 87. stunda: «Kur uzdevumā slēpjas nezināmais?»

Situāciju var pierakstīt kā vienādību, kurā nezināmā vietā ir simbols:
«Bija 35, pielika dažus, kļuva 52» → 35 + □ = 52. Tas ir vienādojuma
priekštecis, tikai ar kastīti burta vietā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, majina)

TEMA = "Kur uzdevumā slēpjas nezināmais?"

MERKIS = ("Šodien pierakstīsim situāciju kā vienādību, nezināmo aizstājot "
          "ar simbolu.")

SATURS = [
    Sakums("Bija 35 uzlīmes, sadabūja vēl dažas, tagad ir 52. Kā to "
           "pierakstīt?",
           zimejums=majina(52, [(35, None)]),
           paraksts="35 + □ = 52.",
           fakti=["□ - kastīte nezināmā skaitļa vietā.",
                  "Pieraksts saka to pašu, ko stāsts.",
                  "Tad nezināmo var atrast."]),

    Doma("Nezināmais ar simbolu",
         "Nezināmā vietā raksta □ un pieraksta stāstu kā vienādību.",
         soli=[
             "Atrodi, ko nezini.",
             "Uzraksti darbības pēc kārtas, kā stāstā.",
             "Nezināmā vietā liec □.",
             "Rezultātu raksti aiz «=».",
         ]),

    Varianti("Kura vienādība?", [
        {"jaut": "Bija 35 uzlīmes, sadabūja vēl, tagad 52.",
         "opcijas": ["35 + □ = 52", "35 − □ = 52", "□ − 35 = 52"],
         "pareizi": 0, "padoms": "Sadabūja - plus."},
        {"jaut": "Bija daži baloni, 8 pārplīsa, palika 17.",
         "opcijas": ["□ − 8 = 17", "□ + 8 = 17", "8 − □ = 17"],
         "pareizi": 0, "padoms": "Nezina sākumu."},
        {"jaut": "Bija 60 €, iztērēja, palika 24 €.",
         "opcijas": ["60 − □ = 24", "60 + □ = 24", "□ − 60 = 24"],
         "pareizi": 0, "padoms": "Nezina, cik iztērēja."},
        {"jaut": "Klasē bija daži bērni, atnāca 5, tagad 26.",
         "opcijas": ["□ + 5 = 26", "□ − 5 = 26", "26 + 5 = □"],
         "pareizi": 0, "padoms": "Nezina sākumu."},
    ]),

    Ievadi("Atrodi □", [
        {"jaut": "35 + □ = 52", "atb": ["17"], "padoms": "52 − 35."},
        {"jaut": "□ − 8 = 17", "atb": ["25"], "padoms": "17 + 8."},
        {"jaut": "60 − □ = 24", "atb": ["36"], "padoms": "60 − 24."},
        {"jaut": "□ + 5 = 26", "atb": ["21"], "padoms": "26 − 5."},
    ]),

    Pasaule("Cik zivju noķēra?",
            Ievadi("", [
                {"jaut": "Spainī bija 12 zivis. Vectētiņš noķēra vēl, tagad "
                         "ir 30. 12 + □ = 30. Cik noķēra?", "atb": ["18"],
                 "padoms": "30 − 12."},
            ]),
            pavediens="daba",
            konteksts="Makšķerējot ezerā, zivis liek spainī.",
            kapec="Vienādība ar □ ir īss stāsta pieraksts."),

    Kopsavilkums([
        "Atrodu, kas uzdevumā nav zināms.",
        "Pierakstu situāciju kā vienādību ar □.",
        "Atrodu nezināmo.",
    ]),

    Majas([
        "Izdomā stāstu, kurā nezināms, cik bija sākumā.",
        "Pieraksti to ar □.",
        "Lai mājinieks atrod □.",
    ]),
]
