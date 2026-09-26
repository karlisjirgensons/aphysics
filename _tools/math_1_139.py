# -*- coding: utf-8 -*-
"""1. klase, 139. stunda: «Kā izskatās mana diena?»

Dienas plāns kā laika tabula: laiks - darbība. No tā nolasa, kas notiek
kad, cik ilgi, un saplāno savu dienu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā izskatās mana diena?"

MERKIS = ("Šodien izmantosim laika tabulu savas dienas plānam.")

_DIENA = restis([["7:00", "celšanās"], ["8:00", "skola"],
                 ["13:00", "pusdienas"], ["15:00", "pulciņš"],
                 ["21:00", "miegs"]])

SATURS = [
    Sakums("Kas notiek pulksten 13?",
           zimejums=_DIENA,
           paraksts="Tabulā - laiks un darbība.",
           fakti=["Kreisajā pusē laiks, labajā - ko dara.",
                  "Laiki iet pēc kārtas.",
                  "No tabulas var aprēķināt ilgumu."]),

    Doma("Dienas plāns",
         "Plāns palīdz neko neaizmirst un visu paspēt.",
         soli=[
             "Pieraksti galvenos notikumus.",
             "Pie katra - laiku.",
             "Sakārto pēc kārtas.",
         ]),

    Ievadi("Nolasi plānu", [
        {"jaut": "Kurā stundā sākas skola?", "zim": _DIENA, "atb": ["8"],
         "padoms": "8:00."},
        {"jaut": "Cik stundas no skolas sākuma līdz pusdienām?",
         "zim": _DIENA, "atb": ["5"], "padoms": "13 − 8."},
        {"jaut": "Cik stundas no pusdienām līdz pulciņam?", "zim": _DIENA,
         "atb": ["2"], "padoms": "15 − 13."},
    ]),

    Varianti("Kas notiek?", [
        {"jaut": "Pulksten 15:00", "zim": _DIENA,
         "opcijas": ["pulciņš", "skola", "miegs"], "pareizi": 0,
         "padoms": "Nolasi rindu."},
        {"jaut": "Kas notiek pēc pusdienām?", "zim": _DIENA,
         "opcijas": ["pulciņš", "skola", "celšanās"], "pareizi": 0,
         "padoms": "Nākamā rinda."},
    ]),

    Petijums("Mans dienas plāns", [
        "Uzraksti 5 savas dienas notikumus.",
        "Pie katra - laiku.",
        "Sakārto tabulā pēc kārtas.",
        "Aprēķini, cik stundas esi skolā.",
    ], vajag="lapa, lineāls"),

    Pasaule("Brīvdienu plāns",
            Ievadi("", [
                {"jaut": "Sestdienā: 10:00 zoodārzs, 13:00 pusdienas. Cik "
                         "stundas zoodārzā?", "atb": ["3"],
                 "padoms": "13 − 10."},
            ]),
            pavediens="celojums",
            konteksts="Ģimene plāno brīvdienu izbraucienu.",
            kapec="Plāns palīdz paspēt visu."),

    Kopsavilkums([
        "Lasu laika tabulu.",
        "Aprēķinu ilgumu no tabulas.",
        "Plānoju savu dienu.",
    ]),

    Majas([
        "Uzraksti rītdienas plānu.",
        "Vakarā pārbaudi - vai sanāca pēc plāna?",
        "Kas aizņēma visvairāk laika?",
    ]),
]
