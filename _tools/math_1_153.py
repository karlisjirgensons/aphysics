# -*- coding: utf-8 -*-
"""1. klase, 153. stunda: «Kā uzzīmēt pēc nosacījumiem?»

Zīmē figūru pēc nosacījumiem: sešstūris; daudzstūris ar divām vienādām
malām; četrstūris ar vienu taisnu stūri. Pārbauda katru nosacījumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, figura)

TEMA = "Kā uzzīmēt pēc nosacījumiem?"

MERKIS = ("Šodien zīmēsim figūras pēc dotiem nosacījumiem un pārbaudīsim "
          "tos.")

_SESS = figura([(1, 0), (4, 0), (5, 2), (4, 4), (1, 4), (0, 2)])
_VIENADAS = figura([(0, 0), (4, 0), (2, 4)])

SATURS = [
    Sakums("Uzzīmē sešstūri! Cik stūru?",
           zimejums=_SESS,
           paraksts="6 stūri, 6 malas.",
           fakti=["Izlasi katru nosacījumu.",
                  "Zīmē rūtiņu lapā.",
                  "Pārbaudi katru nosacījumu."]),

    Doma("Nosacījumi",
         "Figūra der, ja izpildīti visi nosacījumi.",
         soli=[
             "Cik stūru vajag?",
             "Kādām malām jābūt (vienādām, taisnām)?",
             "Uzzīmē un pārbaudi pa vienam.",
         ]),

    Varianti("Vai der?", [
        {"jaut": "Nosacījums: sešstūris.", "zim": _SESS,
         "opcijas": ["der", "neder"], "jaukt": False, "pareizi": 0,
         "padoms": "Saskaiti stūrus."},
        {"jaut": "Nosacījums: trijstūris ar divām vienādām malām.",
         "zim": _VIENADAS, "opcijas": ["der", "neder"], "jaukt": False,
         "pareizi": 0, "padoms": "Sānu malas vienādas."},
        {"jaut": "Nosacījums: četrstūris ar taisniem stūriem.",
         "zim": figura([(0, 0), (5, 0), (6, 3), (1, 3)]),
         "opcijas": ["neder", "der"], "jaukt": False, "pareizi": 0,
         "padoms": "Stūri slīpi."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik malu ir sešstūrim?", "atb": ["6"],
         "padoms": "Tikpat, cik stūru."},
        {"jaut": "Cik vienādu malu ir kvadrātam?", "atb": ["4"],
         "padoms": "Visas."},
    ]),

    Petijums("Zīmē pēc nosacījuma", [
        "Uzzīmē sešstūri rūtiņu lapā.",
        "Uzzīmē četrstūri ar divām vienādām malām.",
        "Uzzīmē piecstūri ar vienu taisnu stūri.",
        "Pārbaudi ar pāri.",
    ], vajag="rūtiņu burtnīca, lineāls"),

    Pasaule("Karodziņš",
            Varianti("", [
                {"jaut": "Karodziņam jābūt trijstūrim ar taisnu stūri pie "
                         "kāta. Kurš der?",
                 "zim": figura([(0, 0), (0, 4), (4, 4)]),
                 "opcijas": ["šis der", "neder"], "jaukt": False,
                 "pareizi": 0, "padoms": "Taisnais stūris augšā kreisajā."},
            ]),
            pavediens="sports",
            konteksts="Sporta dienai katra komanda zīmē karodziņu.",
            kapec="Nosacījumi - visiem vienādi karodziņi."),

    Kopsavilkums([
        "Zīmēju figūru pēc nosacījumiem.",
        "Pārbaudu katru nosacījumu.",
        "Zinu, kad figūra neder.",
    ]),

    Majas([
        "Uzzīmē astoņstūri.",
        "Uzzīmē trijstūri ar trim vienādām malām.",
        "Palūdz kādu pārbaudīt.",
    ]),
]
