# -*- coding: utf-8 -*-
"""9. klase, 107. stunda: «Kā situāciju pierakstīt ar diviem nezināmajiem?»

No teksta uz vienādojumu ar x un y: vispirms nosauc, ko apzīmē katrs
burts, tad atrod teikumu, kas dod vienādību. Viens vienādojums vēl neļauj
atrast abus - tam vajadzēs sistēmu (nākamais mikrotemats).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā situāciju pierakstīt ar diviem nezināmajiem?"

MERKIS = ("Veidosim vienādojumu ar diviem nezināmajiem praktiskai "
          "situācijai.")

SATURS = [
    Sakums("Kas paslēpts šajā čekā?",
           zimejums=restis([["prece", "cena", "skaits"],
                            ["kruasāns", "1,20 €", "x"],
                            ["kafija", "2,50 €", "y"],
                            ["kopā", "12,10 €", ""]]),
           paraksts="1,2x + 2,5y = 12,1.",
           fakti=["Divi nezināmie - divi burti.",
                  "Katram burtam pieraksti nozīmi un mērvienību.",
                  "Vienādība nāk no teikuma «kopā...»."]),

    Doma("No teksta uz vienādojumu",
         "Apzīmē abus nezināmos, izsaki katru daļu ar tiem un pielīdzini "
         "kopējam lielumam.",
         soli=[
             "«x - ..., y - ...» - ar vārdiem.",
             "Katra teksta daļa - izteiksme ar x vai y.",
             "Atrodi, kas ir «kopā», «tikpat», «par ... vairāk».",
             "Pieraksti vienādojumu un pārbaudi ar iedomātu pāri.",
         ]),

    Paraugs("Vecumi",
            uzd="Tēvs ir par 26 gadiem vecāks nekā dēls, kopā viņiem ir "
                "50 gadu. Pieraksti vienādojumus.",
            soli=[
                ("x - tēva vecums, y - dēla vecums", "Apzīmējumi."),
                ("x − y = 26", "«Par 26 vecāks»."),
                ("x + y = 50", "«Kopā 50»."),
            ],
            atbilde="divi vienādojumi: x − y = 26, x + y = 50"),

    Varianti("Kurš vienādojums der?", [
        {"jaut": "Klasē ir 28 skolēni; x - zēni, y - meitenes.",
         "opcijas": ["x + y = 28", "x − y = 28", "xy = 28", "x = 28y"],
         "pareizi": 0, "padoms": "Kopā."},
        {"jaut": "Meiteņu ir par 4 vairāk nekā zēnu.",
         "opcijas": ["y − x = 4", "x − y = 4", "x + y = 4", "y = 4x"],
         "pareizi": 0, "padoms": "y lielāks."},
        {"jaut": "Zīmulis x €, pildspalva y €; 3 zīmuļi un 2 pildspalvas "
                 "maksā 5,40 €.",
         "opcijas": ["3x + 2y = 5,4", "2x + 3y = 5,4", "x + y = 5,4",
                     "5xy = 5,4"],
         "pareizi": 0, "padoms": "Skaits · cena."},
        {"jaut": "Pildspalva ir 3 reizes dārgāka par zīmuli.",
         "opcijas": ["y = 3x", "x = 3y", "y = x + 3", "x + y = 3"],
         "pareizi": 0, "padoms": "y - pildspalva."},
    ]),

    Ievadi("Pārbaudi ar pāri", [
        {"jaut": "Čekā 1,2x + 2,5y = 12,1. Ja kafija ir viena (y = 1), cik "
                 "kruasānu?", "atb": ["8"], "padoms": "1,2x = 9,6."},
        {"jaut": "Klasē 28 skolēni, zēnu 12. Cik meiteņu?", "atb": ["16"],
         "padoms": "x + y = 28."},
        {"jaut": "Tēva un dēla uzdevumā: ja dēlam 12, cik tēvam?",
         "atb": ["38"], "padoms": "12 + 26 - un 38 + 12 = 50 ✔."},
    ]),

    Pasaule("Sporta klubs",
            Ievadi("", [
                {"jaut": "Klubā x pieaugušo (40 €/mēn.) un y skolēnu (25 €/mēn.). "
                         "Ieņēmumi 2150 €. 40x + 25y = ? ", "atb": ["2150"],
                 "padoms": "Kopsumma."},
                {"jaut": "Ja pieaugušo ir 30, cik skolēnu?", "atb": ["38"],
                 "padoms": "1200 + 25y = 2150."},
            ]),
            pavediens="sports",
            konteksts="Kluba grāmatvede zina tikai kopējos ieņēmumus un "
                      "cenas.",
            kapec="Vienam vienādojumam ar diviem nezināmajiem ir daudz pāru - "
                  "vajag vēl vienu faktu."),

    Kopsavilkums([
        "Apzīmēju divus nezināmos ar nozīmi.",
        "Pierakstu vienādojumu no teksta.",
        "Saprotu, ka vienam vienādojumam atbilst daudz pāru.",
    ]),

    Majas([
        "Pieraksti vienādojumu: 5 lielas un 3 mazas pudeles kopā 7 litri.",
        "Izdomā čeku ar divām precēm un uzraksti vienādojumu.",
        "Atrodi 2 atrisinājumus savam vienādojumam.",
    ]),
]
