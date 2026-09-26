# -*- coding: utf-8 -*-
"""1. klase, 19. stunda: «Kā sadalīt klucīšu virteni divās rokās?»

Saspraustu klucīšu virteni pārlauž divās daļās: cik vienā rokā, cik otrā.
Ja kopā zināms un viena daļa zināma, otru var atrast, neskatoties rokā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, bildes)

TEMA = "Kā sadalīt klucīšu virteni divās rokās?"

MERKIS = ("Šodien sadalīsim klucīšu virteni divās daļās un noteiksim, cik "
          "ir katrā rokā.")


def _virtene(a, b):
    return bildes([[("klucis", a), "", ("klucis*", b)]])


SATURS = [
    Sakums("7 klucīši - cik kreisajā, cik labajā rokā?",
           zimejums=_virtene(3, 4),
           paraksts="Kreisajā 3, labajā 4 - kopā 7.",
           fakti=["Virteni pārlauž divās daļās.",
                  "Abas daļas kopā ir visa virtene.",
                  "Zinot vienu daļu, var atrast otru."]),

    Doma("Viena daļa un otra",
         "Ja zini, cik kopā un cik vienā rokā, vari atrast, cik otrā.",
         soli=[
             "Saskaiti visu virteni.",
             "Pārlauz un saskaiti vienu daļu.",
             "Otrā daļa - cik vēl līdz visam.",
         ]),

    Ievadi("Cik otrā rokā?", [
        {"jaut": "Kopā 7. Kreisajā 3. Cik labajā?", "zim": _virtene(3, 4),
         "atb": ["4"], "padoms": "Saskaiti oranžos."},
        {"jaut": "Kopā 6. Kreisajā 2. Cik labajā?", "zim": _virtene(2, 4),
         "atb": ["4"], "padoms": "2 un vēl cik ir 6?"},
        {"jaut": "Kopā 8. Kreisajā 5. Cik labajā?", "atb": ["3"],
         "padoms": "5 un vēl cik ir 8?"},
        {"jaut": "Kopā 9. Kreisajā 6. Cik labajā?", "atb": ["3"],
         "padoms": "6 un vēl cik ir 9?"},
        {"jaut": "Kopā 10. Kreisajā 4. Cik labajā?", "atb": ["6"],
         "padoms": "4 un vēl cik ir 10?"},
        {"jaut": "Kopā 7. Labajā 5. Cik kreisajā?", "atb": ["2"],
         "padoms": "Cik un vēl 5 ir 7?"},
    ], pamats=4),

    Varianti("Kura virtene?", [
        {"jaut": "Kurā zīmējumā kopā ir 6?", "zim": _virtene(2, 4),
         "opcijas": ["Jā, 2 un 4", "Nē, tur ir 7"], "jaukt": False,
         "pareizi": 0, "padoms": "Saskaiti visus."},
        {"jaut": "Virtenē 8. Vai to var sadalīt 4 un 4?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "4 un 4 ir 8."},
    ]),

    Petijums("Spēle pārī", [
        "Saspraud virteni no 7 klucīšiem.",
        "Aiz muguras pārlauz to un parādi vienu daļu.",
        "Draugs pasaka, cik ir otrā rokā.",
        "Pārbaudiet un mainieties lomām.",
    ], vajag="saspraužami klucīši"),

    Pasaule("Konfektes kabatās",
            Ievadi("", [
                {"jaut": "Jānim ir 9 konfektes divās kabatās. Kreisajā ir 5. "
                         "Cik labajā?", "atb": ["4"],
                 "padoms": "5 un vēl cik ir 9?"},
                {"jaut": "Ja abās kabatās ir vienādi, cik katrā, ja kopā "
                         "8?", "atb": ["4"], "padoms": "4 un 4."},
            ]),
            pavediens="veikals",
            konteksts="Jānis salika konfektes divās kabatās.",
            kapec="Zinot kopā un vienu daļu, otru nav jāskatās."),

    Kopsavilkums([
        "Sadalu virteni divās daļās.",
        "Zinot kopā un vienu daļu, atrodu otru.",
        "Pārbaudu, saskaitot abas daļas.",
    ]),

    Majas([
        "Paslēp dažas no 8 pogām saujā. Lai kāds uzmin, cik tur ir.",
        "Sadali 10 zīmuļus divās kaudzēs un pieraksti.",
        "Cik dažādi var sadalīt 6 grāmatas divos plauktos?",
    ]),
]
