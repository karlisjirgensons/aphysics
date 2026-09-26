# -*- coding: utf-8 -*-
"""2. klase, 75. stunda: «Kāds stāsts der izteiksmei?»

Apgrieztais uzdevums: dota izteiksme, jāizdomā situācija. Katrai darbības
zīmei atbilst notikums stāstā - «+» ir «pielika, atnāca, nopirka klāt»,
«−» - «paņēma, aizgāja, iztērēja».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kāds stāsts der izteiksmei?"

MERKIS = ("Šodien veidosim tekstu, kas atbilst dotai divu darbību "
          "izteiksmei.")

SATURS = [
    Sakums("Kāds stāsts slēpjas aiz 30 + 12 − 5?",
           fakti=["Piemēram: autobusā 30 cilvēki, iekāpa 12, izkāpa 5.",
                  "Vai: bija 30 €, dabūja 12 €, iztērēja 5 €.",
                  "Viena izteiksme - daudz stāstu."]),

    Doma("No izteiksmes uz stāstu",
         "Katrai zīmei - savs notikums stāstā.",
         soli=[
             "Pirmais skaitlis - kas bija sākumā.",
             "«+» - kaut kas nāca klāt: atnāca, pielika, dabūja.",
             "«−» - kaut kas aizgāja: paņēma, apēda, iztērēja.",
             "Beigās - jautājums: cik tagad?",
         ]),

    Varianti("Vai stāsts der?", [
        {"jaut": "Izteiksme 40 − 15 + 10. Stāsts: «Plauktā 40 grāmatas, 15 "
                 "paņēma, 10 atnesa atpakaļ.»", "opcijas": ["der", "neder"],
         "jaukt": False, "pareizi": 0, "padoms": "Paņēma - mīnus, atnesa - "
                                                   "plus."},
        {"jaut": "Izteiksme 25 + 8 + 7. Stāsts: «Dārzā 25 puķes, 8 "
                 "nogrieza, 7 iestādīja.»", "opcijas": ["der", "neder"],
         "jaukt": False, "pareizi": 1, "padoms": "Nogrieza - tas ir mīnus."},
        {"jaut": "Izteiksme 60 − (20 + 15). Stāsts: «Bija 60 €, nopirka "
                 "bumbu par 20 € un cepuri par 15 €.»",
         "opcijas": ["der", "neder"], "jaukt": False, "pareizi": 0,
         "padoms": "Abi pirkumi kopā atņemti."},
        {"jaut": "Izteiksme 50 − 12 − 8. Stāsts: «Kastē 50 āboli, 12 "
                 "apēda, 8 ielika klāt.»", "opcijas": ["der", "neder"],
         "jaukt": False, "pareizi": 1, "padoms": "Ielika - tas ir plus."},
    ]),

    Ievadi("Izrēķini stāstu", [
        {"jaut": "Plauktā 40 grāmatas, 15 paņēma, 10 atnesa atpakaļ. Cik "
                 "tagad?", "atb": ["35"], "padoms": "40 − 15 + 10."},
        {"jaut": "Bija 60 €, bumba 20 €, cepure 15 €. Cik palika?",
         "atb": ["25"], "mers": "€", "padoms": "60 − (20 + 15)."},
    ]),

    Varianti("Kura izteiksme stāstam?", [
        {"jaut": "Vilcienā 45 pasažieri. Stacijā izkāpa 20, iekāpa 13.",
         "opcijas": ["45 − 20 + 13", "45 + 20 − 13", "45 − (20 + 13)"],
         "pareizi": 0, "padoms": "Izkāpa - mīnus, iekāpa - plus."},
        {"jaut": "Mārtiņam 17 kartītes. Viņš dabūja 9, tad vēl 4.",
         "opcijas": ["17 + 9 + 4", "17 + 9 − 4", "17 − 9 + 4"],
         "pareizi": 0, "padoms": "Divreiz dabūja."},
    ]),

    Pasaule("Stāsts par zoodārzu",
            Ievadi("", [
                {"jaut": "Izteiksme: 38 + 24 − 15. Zoodārzā bija 38 "
                         "pingvīni, atveda 24, 15 aizveda uz citu zoodārzu. "
                         "Cik tagad?", "atb": ["47"],
                 "padoms": "62 − 15."},
            ]),
            pavediens="daba",
            konteksts="Zoodārzi apmainās ar dzīvniekiem.",
            kapec="Izteiksme ir īss stāsts ar skaitļiem."),

    Kopsavilkums([
        "Izdomāju stāstu dotai izteiksmei.",
        "Katrai zīmei atrodu notikumu.",
        "Pārbaudu, vai stāsts atbilst izteiksmei.",
    ]),

    Majas([
        "Izdomā stāstu izteiksmei 20 + 15 − 10.",
        "Izdomā stāstu izteiksmei 50 − (10 + 20).",
        "Nolasi stāstus mājiniekam - lai uzmin izteiksmi.",
    ]),
]
