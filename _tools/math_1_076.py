# -*- coding: utf-8 -*-
"""1. klase, 76. stunda: «Cik rāda pulkstenis?»

Pilnas stundas: lielais (minūšu) rādītājs rāda uz 12, mazais (stundu) - uz
stundu. Datumu atrod kalendārā: mēnesis un diena.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, pulkstenis, restis)

TEMA = "Cik rāda pulkstenis?"

MERKIS = ("Šodien nolasīsim un parādīsim pilnas stundas pulkstenī un "
          "atradīsim datumu kalendārā.")

_KALENDARS = restis([["P", "O", "T", "C", "Pk", "S", "Sv"],
                     [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14],
                     [15, 16, 17, 18, 19, 20, 21]])

SATURS = [
    Sakums("Lielais rādītājs uz 12 - kas tas nozīmē?",
           zimejums=pulkstenis(3),
           paraksts="Lielais uz 12, mazais uz 3 - pulksten trīs.",
           fakti=["Lielais rādītājs - minūtes.",
                  "Mazais rādītājs - stundas.",
                  "Pilnā stundā lielais rāda uz 12."]),

    Slidnis("Pilnas stundas", [
        {"v": "8:00", "teksts": "Astoņi - skola sākas",
         "zim": pulkstenis(8)},
        {"v": "12:00", "teksts": "Divpadsmit - pusdienas",
         "zim": pulkstenis(12)},
        {"v": "3:00", "teksts": "Trīs - mājās", "zim": pulkstenis(3)},
    ]),

    Doma("Kā nolasīt",
         "Ja lielais rādītājs uz 12, nolasi, uz kuru skaitli rāda mazais.",
         soli=[
             "Atrodi lielo rādītāju - vai tas uz 12?",
             "Atrodi mazo - uz kuru skaitli tas rāda?",
             "Pasaki: pulksten ... (piem., septiņi).",
         ]),

    Ievadi("Cik pulkstenis?", [
        {"jaut": "Cik stundas?", "zim": pulkstenis(7), "atb": ["7"],
         "padoms": "Mazais rādītājs."},
        {"jaut": "Cik stundas?", "zim": pulkstenis(10), "atb": ["10"],
         "padoms": "Mazais rādītājs."},
        {"jaut": "Cik stundas?", "zim": pulkstenis(1), "atb": ["1"],
         "padoms": "Mazais rādītājs."},
        {"jaut": "Cik stundas?", "zim": pulkstenis(5), "atb": ["5"],
         "padoms": "Mazais rādītājs."},
    ]),

    Ievadi("Kalendārs", [
        {"jaut": "Kurā datumā ir pirmā piektdiena?", "zim": _KALENDARS,
         "atb": ["5"], "padoms": "Aile «Pk»."},
        {"jaut": "Kura nedēļas diena ir 16. datums? Cik pēc kārtas nedēļā?",
         "zim": _KALENDARS, "atb": ["2"], "padoms": "Otrdiena - 2."},
        {"jaut": "Šodien 9. datums. Kāds datums būs pēc nedēļas?",
         "zim": _KALENDARS, "atb": ["16"], "padoms": "9 + 7."},
    ]),

    Pasaule("Mana diena",
            Varianti("", [
                {"jaut": "Skola sākas pulksten 8. Kurš pulkstenis?",
                 "zim": pulkstenis(8),
                 "opcijas": ["tieši laikā", "par agru", "par vēlu"],
                 "jaukt": False, "pareizi": 0, "padoms": "Mazais uz 8."},
                {"jaut": "Treniņš sākas 4, pulkstenis rāda 3. Cik stundas "
                         "vēl?", "opcijas": ["1", "3", "4"], "pareizi": 0,
                 "padoms": "No 3 līdz 4."},
            ]),
            pavediens="skola",
            konteksts="Pa dienu daudz ko nosaka pulkstenis.",
            kapec="Kas zina laiku, nenokavē."),

    Kopsavilkums([
        "Nolasu pilnas stundas pulkstenī.",
        "Zinu, kurš rādītājs ko rāda.",
        "Atrodu datumu kalendārā.",
    ]),

    Majas([
        "Paskaties pulkstenī, kad ceļies un kad ej gulēt.",
        "Atrodi kalendārā savu dzimšanas dienu.",
        "Parādi ar rokām pulksten 9.",
    ]),
]
