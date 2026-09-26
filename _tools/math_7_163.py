# -*- coding: utf-8 -*-
"""7. klase, 163. stunda: «Kā situāciju pierakstīt ar nevienādību?»

Vārdi «vismaz», «ne vairāk», «mazāk nekā», «pārsniedz» ir nevienādības zīmes.
Stunda iemāca pārtulkot tos un paskaidrot, ko apzīmē nezināmais.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kā situāciju pierakstīt ar nevienādību?"

MERKIS = ("Aprakstīsim praktisku situāciju ar nevienādību un paskaidrosim "
          "nezināmā nozīmi.")

SATURS = [
    Sakums("Vārdnīca: vārdi → zīmes",
           zimejums=restis([["vārdiem", "zīme"],
                            ["vismaz, ne mazāk", "≥"],
                            ["ne vairāk, līdz (ieskaitot)", "≤"],
                            ["vairāk nekā, pārsniedz", ">"],
                            ["mazāk nekā", "<"]]),
           fakti=["«Vismaz 18» ir x ≥ 18.",
                  "«Mazāk nekā 18» ir x < 18."]),

    Doma("Nosauc x un izvēlies zīmi",
         "Situāciju pieraksta ar nevienādību: nosaka, ko apzīmē x (ar "
         "mērvienību), izsaka pārējos lielumus ar x un izvēlas zīmi pēc "
         "vārdiem.",
         soli=[
             "x - ko meklē (skaits, laiks, summa)?",
             "Izsaki kopējo lielumu ar x.",
             "Izvēlies zīmi: «vismaz» ≥, «ne vairāk» ≤ ...",
             "Uzraksti nevienādību un paskaidro vārdiem.",
         ]),

    Paraugs("Pieraksti",
            uzd="Lidmašīnas bagāža nedrīkst pārsniegt 23 kg. Koferis sver "
                "4 kg, tajā ieliek x apģērba kompletus pa 1,5 kg.",
            soli=[
                ("x - kompletu skaits", "Nozīme."),
                ("Masa: 4 + 1,5x", "Izsaka."),
                ("«Nedrīkst pārsniegt» - ≤", "Zīme."),
                ("4 + 1,5x ≤ 23", "Nevienādība."),
            ],
            atbilde="4 + 1,5x ≤ 23, kur x - kompletu skaits"),

    Varianti("Kura nevienādība?", [
        {"jaut": "Klasē vismaz 20 skolēnu (x - skolēnu skaits).",
         "opcijas": ["x ≥ 20", "x > 20", "x ≤ 20", "x < 20"],
         "pareizi": 0, "padoms": "Vismaz."},
        {"jaut": "3 kafijas pa x € maksā mazāk nekā 10 €.",
         "opcijas": ["3x < 10", "3x ≤ 10", "3x > 10", "x + 3 < 10"],
         "pareizi": 0, "padoms": "Mazāk nekā."},
        {"jaut": "Ātrums pārsniedz 90 km/h.",
         "opcijas": ["v > 90", "v ≥ 90", "v < 90", "v ≤ 90"],
         "pareizi": 0, "padoms": "Pārsniedz - stingri."},
        {"jaut": "Telefons ar 20 % lādiņu tērē 5 % stundā; jāstrādā vēl t h "
                 "līdz 0.",
         "opcijas": ["20 − 5t ≥ 0", "20 − 5t > 20", "5t ≥ 20", "20t ≤ 5"],
         "pareizi": 0, "padoms": "Lādiņš nav negatīvs."},
    ], pamats=4),

    Pasaule("Laiva un krava",
            Varianti("", [
                {"jaut": "Laiva iztur līdz 300 kg. Divi cilvēki pa 75 kg un x "
                         "maisi pa 20 kg. Nevienādība?",
                 "opcijas": ["150 + 20x ≤ 300", "150 + 20x < 300",
                             "20x ≥ 300", "75 + 20x ≤ 300"],
                 "pareizi": 0, "padoms": "Līdz ieskaitot."},
                {"jaut": "Ko apzīmē x?",
                 "opcijas": ["Maisu skaitu", "Maisa masu",
                             "Cilvēku skaitu", "Laivas masu"],
                 "pareizi": 0, "padoms": "Nozīme."},
            ]),
            pavediens="celojums",
            konteksts="Kravnesības noteikumi ir nevienādības - to pārkāpšana "
                      "ir bīstama.",
            kapec="Pareiza zīme - drošība."),

    Kopsavilkums([
        "Pārtulkoju vārdus nevienādības zīmēs.",
        "Nosaucu, ko apzīmē x.",
        "Izsaku lielumus ar x.",
        "Uzrakstu nevienādību situācijai.",
    ]),

    Majas([
        "Atrodi 3 noteikumus ar «vismaz» vai «ne vairāk» un pieraksti.",
        "Uzraksti nevienādību savam mēneša budžetam.",
        "Paskaidro atšķirību starp > un ≥ ar piemēru.",
    ]),
]
