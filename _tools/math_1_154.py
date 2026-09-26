# -*- coding: utf-8 -*-
"""1. klase, 154. stunda: «Kā pierakstīt zīmēšanas soļus?»

Kvadrāta zīmēšanu rūtiņu lapā sadala soļos un pieraksta ar bultiņām:
→→→↑↑↑←←←↓↓↓. Tas ir algoritms - to var izpildīt jebkurš.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, celjs)

TEMA = "Kā pierakstīt zīmēšanas soļus?"

MERKIS = ("Šodien sadalīsim kvadrāta zīmēšanu soļos un pierakstīsim "
          "algoritmu.")


def _z(soli):
    return celjs(5, 5, (1, 4), None, soli)


SATURS = [
    Sakums("Kā pastāstīt, kā uzzīmēt kvadrātu?",
           zimejums=_z("→→→↑↑↑←←←↓↓↓"),
           paraksts="→→→ ↑↑↑ ←←← ↓↓↓ - kvadrāts 3 × 3 rūtiņas.",
           fakti=["Algoritms - soļi pēc kārtas.",
                  "Katra bultiņa - viena rūtiņa.",
                  "Beigās atgriežas sākumā."]),

    Slidnis("Pa soļiem", [
        {"v": "→→→", "teksts": "Apakšējā mala", "zim": _z("→→→")},
        {"v": "↑↑↑", "teksts": "Labā mala", "zim": _z("→→→↑↑↑")},
        {"v": "←←←", "teksts": "Augšējā mala", "zim": _z("→→→↑↑↑←←←")},
        {"v": "↓↓↓", "teksts": "Kreisā mala - gatavs!",
         "zim": _z("→→→↑↑↑←←←↓↓↓")},
    ]),

    Doma("Algoritms",
         "Algoritms ir tik skaidri pierakstīti soļi, ka tos var izpildīt "
         "cits.",
         soli=[
             "Sadali zīmējumu malās.",
             "Katrai malai - bultiņas.",
             "Pārbaudi: vai beigās atgriezies sākumā?",
         ]),

    Ievadi("Saskaiti soļus", [
        {"jaut": "Cik soļu kopā kvadrātam 3 × 3?", "atb": ["12"],
         "padoms": "4 malas pa 3."},
        {"jaut": "Cik bultiņu → kvadrātam ar malu 4?", "atb": ["4"],
         "padoms": "Viena mala."},
        {"jaut": "Cik soļu taisnstūrim: →→→→↑↑←←←←↓↓?", "atb": ["12"],
         "padoms": "4 + 2 + 4 + 2."},
    ]),

    Varianti("Kura figūra?", [
        {"jaut": "→→↑↑←←↓↓",
         "opcijas": ["kvadrāts", "taisnstūris ar dažādām malām",
                     "trijstūris"], "pareizi": 0,
         "padoms": "Visas malas pa 2."},
        {"jaut": "→→→→↑←←←←↓",
         "opcijas": ["taisnstūris", "kvadrāts", "trijstūris"],
         "pareizi": 0, "padoms": "4 un 1."},
    ]),

    Petijums("Tavs algoritms", [
        "Uzzīmē rūtiņās taisnstūri.",
        "Pieraksti tā algoritmu ar bultiņām.",
        "Iedod pārim tikai bultiņas - lai viņš uzzīmē.",
        "Salīdziniet zīmējumus.",
    ], vajag="rūtiņu burtnīca"),

    Pasaule("Robots zīmētājs",
            Ievadi("", [
                {"jaut": "Robots zīmē kvadrātu ar malu 5 rūtiņas. Cik soļu?",
                 "atb": ["20"], "padoms": "5 + 5 + 5 + 5."},
            ]),
            pavediens="tehnika",
            konteksts="Robotam soļus jāpasaka precīzi.",
            kapec="Algoritms ir robota valoda."),

    Kopsavilkums([
        "Sadalu zīmēšanu soļos.",
        "Pierakstu algoritmu ar bultiņām.",
        "Pārbaudu, vai figūra noslēdzas.",
    ]),

    Majas([
        "Pieraksti algoritmu kvadrātam ar malu 2.",
        "Izdomā algoritmu burtam L.",
        "Lai mājinieks uzzīmē pēc tava algoritma.",
    ]),
]
