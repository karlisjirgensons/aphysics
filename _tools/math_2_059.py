# -*- coding: utf-8 -*-
"""2. klase, 59. stunda: «Kā atcerēties mēnešus?»

Gadā ir 12 mēneši; tiem ir noteikta secība un dažāds dienu skaits (28, 29,
30 vai 31). Dūres triks - kauliņš ir garais mēnesis, iedobe - īsais -
palīdz atcerēties, un kalendārs ļauj pārbaudīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kā atcerēties mēnešus?"

MERKIS = ("Šodien nosauksim mēnešus pēc kārtas, atradīsim informāciju "
          "kalendārā un noteiksim dienu skaitu mēnesī.")

_MENESI = restis([["janvāris", "februāris", "marts"],
                  ["aprīlis", "maijs", "jūnijs"],
                  ["jūlijs", "augusts", "septembris"],
                  ["oktobris", "novembris", "decembris"]], "12 mēneši")

_NOVEMBRIS = restis([["P", "O", "T", "C", "Pk", "S", "Sv"],
                     ["", "", "", "", "", "", 1],
                     [2, 3, 4, 5, 6, 7, 8],
                     [9, 10, 11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20, 21, 22],
                     [23, 24, 25, 26, 27, 28, 29],
                     [30, "", "", "", "", "", ""]], "2026. gada novembris")

SATURS = [
    Sakums("Kāpēc februārī dzimšanas dienu dažreiz nevar svinēt?",
           zimejums=_MENESI,
           fakti=["Februārī parasti ir 28 dienas.",
                  "Reizi 4 gados - 29. Kas dzimis 29. februārī, svin retāk!",
                  "Citos mēnešos - 30 vai 31 diena."]),

    Doma("Dūres triks",
         "Kauliņš uz dūres - 31 diena, iedobe starp kauliņiem - mazāk.",
         soli=[
             "Savelc dūri un skaiti no mazā pirksta kauliņa.",
             "Janvāris - kauliņš (31), februāris - iedobe (28 vai 29).",
             "Marts - kauliņš, aprīlis - iedobe (30) ... jūlijs - kauliņš.",
             "Tad sāc no jauna: augusts - atkal kauliņš (31).",
         ]),

    Ievadi("Mēneši pēc kārtas", [
        {"jaut": "Kurš pēc kārtas ir maijs?", "zim": _MENESI, "atb": ["5"],
         "padoms": "Janvāris - 1."},
        {"jaut": "Kurš pēc kārtas ir oktobris?", "zim": _MENESI,
         "atb": ["10"], "padoms": "Skaiti."},
        {"jaut": "Cik mēnešu ir gadā?", "atb": ["12"],
         "padoms": "Saskaiti tabulā."},
        {"jaut": "Cik dienu ir jūlijā?", "atb": ["31"],
         "padoms": "Jūlijs - kauliņš."},
        {"jaut": "Cik dienu ir septembrī?", "atb": ["30"],
         "padoms": "Septembris - iedobe."},
        {"jaut": "Cik dienu ir decembrī?", "atb": ["31"],
         "padoms": "Decembris - kauliņš."},
    ], pamats=4),

    Ievadi("Lasi kalendāru", [
        {"jaut": "Kurā nedēļas dienā ir 18. novembris? Raksti burtus, kā "
                 "kalendārā.", "zim": _NOVEMBRIS, "atb": ["T", "trešdiena"],
         "tastatura": "text", "padoms": "Atrodi 18 un paskaties augšā."},
        {"jaut": "Cik svētdienu ir šajā novembrī?", "zim": _NOVEMBRIS,
         "atb": ["5"], "padoms": "Pēdējā kolonnā."},
    ]),

    Varianti("Kāds mēnesis?", [
        {"jaut": "Kurš mēnesis nāk pēc augusta?",
         "opcijas": ["septembris", "jūlijs", "oktobris"], "pareizi": 0,
         "padoms": "Skola sākas."},
        {"jaut": "Kurš mēnesis ir pirms marta?",
         "opcijas": ["februāris", "aprīlis", "janvāris"], "pareizi": 0,
         "padoms": "1, 2, 3."},
    ]),

    Pasaule("Cik dienu līdz svētkiem?",
            Ievadi("", [
                {"jaut": "Šodien ir 10. novembris. Cik dienu līdz "
                         "18. novembrim?", "zim": _NOVEMBRIS, "atb": ["8"],
                 "padoms": "18 − 10."},
                {"jaut": "Lāčplēša dienu svin 11. novembrī. Cik dienu no "
                         "tās līdz 18. novembrim?", "atb": ["7"],
                 "padoms": "18 − 11 - tieši nedēļa."},
            ]),
            pavediens="skola",
            konteksts="18. novembrī Latvija svin Proklamēšanas dienu.",
            kapec="Kalendārs palīdz plānot svētkus."),

    Kopsavilkums([
        "Nosaucu mēnešus pēc kārtas.",
        "Zinu, cik dienu ir mēnesī, ar dūres triku.",
        "Atrodu datumu un nedēļas dienu kalendārā.",
    ]),

    Majas([
        "Uzraksti, kurā mēnesī ir visu ģimenes locekļu dzimšanas dienas.",
        "Sakārto tās pēc kārtas.",
        "Kurā mēnesī dzimšanas dienu ir visvairāk?",
    ]),
]
