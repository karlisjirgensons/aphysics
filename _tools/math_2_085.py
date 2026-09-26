# -*- coding: utf-8 -*-
"""2. klase, 85. stunda: «Kā pierakstīt nogriežņu salīdzinājumu?»

Divus nogriežņus salīdzina pēc garuma un pieraksta: AB = 5 cm, CD = 8 cm,
AB < CD. Arī summa: ja AB un CD noliek vienu aiz otra, sanāk 13 cm.
Garumi pārvēršas vienādībās un nevienādībās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, lineals)

TEMA = "Kā pierakstīt nogriežņu salīdzinājumu?"

MERKIS = ("Šodien pierakstīsim ar vienādību un nevienādību situācijas, "
          "kurās doti nogriežņu garumi.")

_NOGR = lineals(12, [(0, 5, "AB"), (0, 8, "CD"), (0, 5, "EF")])

SATURS = [
    Sakums("Kā ar zīmēm pierakstīt, ka viena lente ir garāka?",
           zimejums=_NOGR,
           paraksts="AB = 5 cm, CD = 8 cm, EF = 5 cm.",
           fakti=["AB < CD - AB ir īsāks.",
                  "CD > EF - CD ir garāks.",
                  "AB = EF - vienādi gari."]),

    Doma("Garumi ar zīmēm",
         "Nogriežņa garumu pieraksta ar tā galu burtiem: AB = 5 cm.",
         soli=[
             "Izmēri abus nogriežņus.",
             "Salīdzini skaitļus.",
             "Liec zīmi: <, > vai =.",
             "Summa: AB + CD - abi vienā rindā.",
         ]),

    Varianti("Liec zīmi", [
        {"jaut": "AB ☐ CD", "zim": _NOGR, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 0, "padoms": "5 cm un 8 cm."},
        {"jaut": "AB ☐ EF", "zim": _NOGR, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 2, "padoms": "Abi 5 cm."},
        {"jaut": "CD ☐ EF", "zim": _NOGR, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 1, "padoms": "8 cm un 5 cm."},
        {"jaut": "AB + EF ☐ CD", "zim": _NOGR, "opcijas": ["<", ">", "="],
         "jaukt": False, "pareizi": 1, "padoms": "10 cm un 8 cm."},
    ]),

    Ievadi("Aprēķini garumu", [
        {"jaut": "AB + CD = ? cm", "zim": _NOGR, "atb": ["13"], "mers": "cm",
         "padoms": "5 + 8."},
        {"jaut": "CD − AB = ? cm", "zim": _NOGR, "atb": ["3"], "mers": "cm",
         "padoms": "8 − 5."},
        {"jaut": "MN = 34 cm, KL par 9 cm garāks. KL = ?", "atb": ["43"],
         "mers": "cm", "padoms": "34 + 9."},
        {"jaut": "PR = 60 cm, ST = PR − 15 cm. ST = ?", "atb": ["45"],
         "mers": "cm", "padoms": "60 − 15."},
    ]),

    Pasaule("Tilti pār upi",
            Varianti("", [
                {"jaut": "Koka tilts 45 m, akmens tilts 38 m. Kurš pieraksts "
                         "patiess?",
                 "opcijas": ["45 m > 38 m", "45 m < 38 m", "45 m = 38 m"],
                 "pareizi": 0, "padoms": "Koka tilts garāks."},
                {"jaut": "Par cik metriem koka tilts garāks?",
                 "opcijas": ["7 m", "83 m", "13 m"], "pareizi": 0,
                 "padoms": "45 − 38."},
            ]),
            pavediens="celojums",
            konteksts="Pilsētā pār upi ir divi tilti.",
            kapec="Ar zīmēm salīdzinājumu var pierakstīt īsi."),

    Kopsavilkums([
        "Pierakstu nogriežņa garumu ar burtiem.",
        "Salīdzinu garumus ar <, > un =.",
        "Aprēķinu garumu summu un starpību.",
    ]),

    Majas([
        "Uzzīmē trīs nogriežņus un nosauc tos ar burtiem.",
        "Izmēri un pieraksti garumus.",
        "Uzraksti 3 salīdzinājumus ar zīmēm.",
    ]),
]
