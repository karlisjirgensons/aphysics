# -*- coding: utf-8 -*-
"""7. klase, 167. stunda: «Cik droši jau protu?»

Temata noslēgums pirms pārbaudes darba: jaukti uzdevumi ar vienādojumiem un
nevienādībām. Katram uzdevumam vispirms jāizlemj, kurš rīks vajadzīgs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, Zimejums, restis)

TEMA = "Cik droši jau protu?"

MERKIS = ("Patstāvīgi risināsim jauktus uzdevumus ar vienādojumiem un "
          "nevienādībām.")

SATURS = [
    Sakums("Atkārtojuma karte",
           zimejums=restis([["tips", "ko atceros"],
                            ["ax + b = c", "pārnes, dala"],
                            ["ax + b < c", "dalot ar −, zīme mainās"],
                            ["a < x < b", "visām trim daļām"],
                            ["sistēma", "šķēlums"]]),
           fakti=["Pārbaudi katru atbildi.",
                  "Nevienādībai - arī robežu."]),

    Doma("Plāns katram uzdevumam",
         "Pirms risini, nosaki: vienādojums vai nevienādība? Vai būs "
         "jādala ar negatīvu? Vai atbilde ir skaitlis vai intervāls?",
         soli=[
             "Nosaki tipu.",
             "Risini ar ekvivalentām darbībām.",
             "Pieraksti atbildi pareizā formā.",
             "Pārbaudi.",
         ]),

    Ievadi("Vienādojumi", [
        {"jaut": "5(x − 2) = 3x + 4",
         "atb": ["7"], "padoms": "2x = 14."},
        {"jaut": "{x|3} + {x|6} = 5",
         "atb": ["10"], "padoms": "· 6: 3x = 30."},
        {"jaut": "7 − 2(x + 1) = x − 10",
         "atb": ["5"], "padoms": "5 − 2x = x − 10."},
        {"jaut": "Proporcija x : 12 = 5 : 4",
         "atb": ["15"], "padoms": "4x = 60."},
    ]),

    Ievadi("Nevienādības (robeža)", [
        {"jaut": "3x − 7 > 8. x > ?",
         "atb": ["5"], "padoms": "3x > 15."},
        {"jaut": "4 − 3x ≥ −8. x ≤ ?",
         "atb": ["4"], "padoms": "−3x ≥ −12."},
        {"jaut": "−1 ≤ 2x + 1 < 9. Cik veselu x?",
         "atb": ["5"], "padoms": "−1 ≤ x < 4."},
        {"jaut": "x > 2 un x ≤ 6. Cik veselu x?",
         "atb": ["4"], "padoms": "3; 4; 5; 6."},
    ]),

    Varianti("Atpazīsti kļūdu", [
        {"jaut": "−5x < 15 ⇒ x < −3",
         "opcijas": ["Kļūda: jābūt x > −3", "Pareizi", "Kļūda: x < 3",
                     "Kļūda: x > 3"],
         "pareizi": 0, "padoms": "Dala ar negatīvu."},
        {"jaut": "2(x + 3) = 10 ⇒ 2x + 3 = 10",
         "opcijas": ["Kļūda: 2x + 6 = 10", "Pareizi", "Kļūda: x + 3 = 10",
                     "Kļūda: 2x = 13"],
         "pareizi": 0, "padoms": "Reizina abus."},
    ]),

    Pasaule("Ceļojuma plāns",
            Ievadi("", [
                {"jaut": "Brauciens 360 km; pirmajā dienā nobrauca 2 reizes "
                         "vairāk nekā otrajā. Cik km otrajā?",
                 "atb": ["120"], "padoms": "3x = 360."},
                {"jaut": "Degviela 1,6 € par l, patēriņš 6 l uz 100 km. "
                         "Cik € par 360 km?",
                 "atb": ["34,56"], "padoms": "21,6 l · 1,6."},
                {"jaut": "Budžets degvielai ≤ 50 €. Cik km vēl var nobraukt "
                         "(pilni desmiti km) pēc šiem 360 km?",
                 "atb": ["160"], "padoms": "15,44 € : 0,096 € ≈ 160,8 km."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojuma plānā ir gan vienādojumi (posmi), gan "
                      "nevienādības (budžets).",
            kapec="Viss temats vienā uzdevumā."),

    Kopsavilkums([
        "Atrisinu lineāru vienādojumu un proporciju.",
        "Atrisinu lineāru nevienādību un sistēmu.",
        "Atpazīstu biežākās kļūdas.",
        "Lietoju abus rīkus reālā problēmā.",
    ]),

    Majas([
        "Atkārto 5 kļūdainākos uzdevumus no temata.",
        "Uzraksti sev «špikeri» (kas jāatceras).",
        "Atrisini vēl 3 jauktus uzdevumus.",
    ]),
]
