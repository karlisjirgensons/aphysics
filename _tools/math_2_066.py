# -*- coding: utf-8 -*-
"""2. klase, 66. stunda: «Ko diagramma pasaka par izmaiņām?»

Ja stabiņi ir sakārtoti pēc laika (mēneši, dienas), diagramma rāda
izmaiņas: kur pieauga, kur samazinājās, un par cik. To pašu var pārlikt
tabulā un otrādi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, kolonnas, restis)

TEMA = "Ko diagramma pasaka par izmaiņām?"

MERKIS = ("Šodien lasīsim diagrammu, kas rāda izmaiņas laikā, un "
          "pārkārtosim datus tabulā.")

_GAISMA = kolonnas([("sept.", 13), ("okt.", 11), ("nov.", 9),
                    ("dec.", 7)], " h")

SATURS = [
    Sakums("Kāpēc rudenī uz skolu jāiet tumsā?",
           zimejums=_GAISMA,
           paraksts="Cik stundu gaišs diennaktī (apmēram).",
           fakti=["No septembra līdz decembrim diena kļūst īsāka.",
                  "Katru mēnesi - apmēram par 2 stundām.",
                  "Stabiņi pēc kārtas parāda izmaiņas."]),

    Doma("Diagramma laikā",
         "Stabiņi sakārtoti pēc laika; blakus stabiņi rāda izmaiņu.",
         soli=[
             "Nolasi pirmo un nākamo stabiņu.",
             "Augstāks - palielinājās, zemāks - samazinājās.",
             "Par cik: atņem mazāko no lielākā.",
             "Ieraksti datus tabulā: mēnesis un skaitlis.",
         ]),

    Ievadi("Izmaiņas", [
        {"jaut": "Cik stundu gaišs oktobrī?", "zim": _GAISMA, "atb": ["11"],
         "mers": "h", "padoms": "Otrais stabiņš."},
        {"jaut": "Par cik stundām diena saīsinājās no septembra līdz "
                 "decembrim?", "zim": _GAISMA, "atb": ["6"], "mers": "h",
         "padoms": "13 − 7."},
        {"jaut": "Par cik stundām no oktobra līdz novembrim?", "zim": _GAISMA,
         "atb": ["2"], "mers": "h", "padoms": "11 − 9."},
        {"jaut": "Cik stundu tumšs decembrī? (Diennaktī 24 h.)",
         "zim": _GAISMA, "atb": ["17"], "mers": "h", "padoms": "24 − 7."},
    ]),

    Varianti("Kas notiek?", [
        {"jaut": "Tabulā: janvāris 7 h, februāris 9 h, marts 12 h. Kas "
                 "notiek ar dienu?",
         "opcijas": ["kļūst garāka", "kļūst īsāka", "nemainās"],
         "pareizi": 0, "padoms": "Skaitļi aug."},
        {"jaut": "Kurā mēnesī diena ir visīsākā?", "zim": _GAISMA,
         "opcijas": ["decembrī", "septembrī", "oktobrī"], "pareizi": 0,
         "padoms": "Zemākais stabiņš."},
    ]),

    Pasaule("Temperatūra nedēļā",
            Ievadi("", [
                {"jaut": "Pirmdien +12 °C, piektdien +5 °C. Par cik grādiem "
                         "atdzisa?", "atb": ["7"], "mers": "°C",
                 "padoms": "12 − 5."},
                {"jaut": "Svētdien sasila par 4 grādiem salīdzinot ar "
                         "piektdienu. Cik grādu svētdien?", "atb": ["9"],
                 "mers": "°C", "padoms": "5 + 4."},
            ]),
            pavediens="planeta",
            zimejums=restis([["diena", "P", "O", "T", "C", "Pk"],
                             ["°C", 12, 10, 9, 7, 5]]),
            konteksts="Skolas laika stacija mēra temperatūru katru rītu.",
            kapec="Tabula un diagramma parāda, kā mainās laiks."),

    Kopsavilkums([
        "Lasu diagrammu, kas rāda izmaiņas laikā.",
        "Nosaku, vai lielums pieaug vai samazinās, un par cik.",
        "Pārlieku datus tabulā.",
    ]),

    Majas([
        "Nedēļu katru rītu pieraksti temperatūru.",
        "Uzzīmē diagrammu pa dienām.",
        "Kurā dienā bija vissiltākais?",
    ]),
]
