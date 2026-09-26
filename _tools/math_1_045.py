# -*- coding: utf-8 -*-
"""1. klase, 45. stunda: «Vai vari uzzīmēt tieši 7 cm?»

Nogriezni zīmē otrādi nekā mēra: atzīmē punktu pie 0, otru pie 7 un
savieno ar lineālu. Lauztu līniju zīmē pa posmiem - katram savs garums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, lineals,
                         linijas)

TEMA = "Vai vari uzzīmēt tieši 7 cm?"

MERKIS = ("Šodien uzzīmēsim noteikta garuma nogriezni un lauztu līniju ar "
          "lineālu.")

SATURS = [
    Sakums("Kā uzzīmēt līniju, kas ir tieši 7 cm?",
           zimejums=lineals(10, [(0, 7, "7 cm")]),
           paraksts="Punkts pie 0, punkts pie 7, savieno.",
           fakti=["Nogrieznis - taisna līnija ar diviem galiem.",
                  "Galus atzīmē ar punktiem.",
                  "Pārbaudi: izmēri vēlreiz."]),

    Slidnis("Nogrieznis 7 cm", [
        {"v": "1", "teksts": "Noliec lineālu un atzīmē punktu pie 0",
         "zim": lineals(10, [(0, 0.15, "")])},
        {"v": "2", "teksts": "Atzīmē otru punktu pie 7",
         "zim": lineals(10, [(0, 0.15, ""), (6.85, 7, "")])},
        {"v": "3", "teksts": "Savieno punktus gar lineālu",
         "zim": lineals(10, [(0, 7, "7 cm")])},
    ]),

    Doma("Zīmē nogriezni",
         "Vispirms divi punkti, tad līnija starp tiem.",
         soli=[
             "Atzīmē punktu pie lineāla 0.",
             "Atzīmē punktu pie vajadzīgā skaitļa.",
             "Savieno punktus, velkot gar lineālu.",
             "Pārbaudi, izmērot.",
         ]),

    Ievadi("Cik garš uzzīmēts?", [
        {"jaut": "Anna zīmēja 5 cm. Vai sanāca? Cik cm?",
         "zim": lineals(10, [(0, 5, "")]), "atb": ["5"],
         "padoms": "Nolasi pie gala."},
        {"jaut": "Jānis sāka pie 1 un beidza pie 8. Cik cm?",
         "zim": lineals(10, [(1, 8, "")]), "atb": ["7"],
         "padoms": "No 1 līdz 8 - 7 cm."},
        {"jaut": "Lauztai līnijai 2 posmi: 3 cm un 4 cm. Cik cm kopā?",
         "zim": linijas([(1, 1, 4, 4), (4, 4, 8, 1)], platums=10,
                        augstums=5), "atb": ["7"], "padoms": "3 + 4."},
    ]),

    Varianti("Kas nogāja greizi?", [
        {"jaut": "Maija sāka zīmēt no lineāla malas, nevis no 0. Nogrieznis "
                 "būs...",
         "opcijas": ["garāks, nekā vajag", "tieši pareizs",
                     "īsāks, nekā vajag"], "jaukt": False, "pareizi": 0,
         "padoms": "Mala ir pirms 0."},
    ]),

    Petijums("Zīmē burtnīcā", [
        "Uzzīmē nogriezni 7 cm.",
        "Uzzīmē nogriezni 4 cm.",
        "Uzzīmē lauztu līniju: 2 cm, 3 cm, 2 cm.",
        "Izmēri visus vēlreiz un atzīmē ✓.",
    ], vajag="lineāls, zīmulis, burtnīca"),

    Pasaule("Grāmatzīme",
            Ievadi("", [
                {"jaut": "Grāmatzīmei jābūt 9 cm garai. Tu uzzīmēji 7 cm. "
                         "Cik vēl jāpagarina?", "atb": ["2"],
                 "padoms": "9 − 7."},
            ]),
            pavediens="skola",
            konteksts="No kartona izgriež grāmatzīmi - vispirms to "
                      "uzzīmē.",
            kapec="Precīzs zīmējums - precīza grāmatzīme."),

    Kopsavilkums([
        "Zīmēju noteikta garuma nogriezni.",
        "Zīmēju lauztu līniju pa posmiem.",
        "Pārbaudu, izmērot.",
    ]),

    Majas([
        "Uzzīmē nogriežņus 3 cm, 6 cm un 10 cm.",
        "Izgriez 9 cm garu grāmatzīmi.",
        "Uzzīmē lauztu līniju ar 3 posmiem un izmēri tos.",
    ]),
]
