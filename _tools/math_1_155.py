# -*- coding: utf-8 -*-
"""1. klase, 155. stunda: «Vai cita pieraksts strādā?»

Izpilda cita skolēna algoritmu. Ja figūra nenoslēdzas vai sanāk cita,
atrod kļūdaino soli un izlabo. Pārbaude: bultiņu uz labo tikpat, cik uz
kreiso; uz augšu tikpat, cik uz leju.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Varianti, celjs)

TEMA = "Vai cita pieraksts strādā?"

MERKIS = ("Šodien izpildīsim cita skolēna algoritmu un, ja vajag, "
          "izlabosim to.")


def _z(soli):
    return celjs(5, 5, (1, 3), None, soli)


SATURS = [
    Sakums("Anna rakstīja: →→→↑↑←←←↓↓↓ - kas nav kārtībā?",
           zimejums=_z("→→→↑↑←←←↓↓↓"),
           paraksts="Uz augšu 2, uz leju 3 - figūra nenoslēdzas.",
           fakti=["→ tikpat, cik ←.",
                  "↑ tikpat, cik ↓.",
                  "Tad figūra noslēdzas."]),

    Doma("Pārbaudi algoritmu",
         "Izpildi soli pa solim - un saskaiti bultiņas.",
         soli=[
             "Saskaiti → un ←: vai vienādi?",
             "Saskaiti ↑ un ↓: vai vienādi?",
             "Ja nē - atrodi, kur pietrūkst vai ir lieks.",
         ]),

    Varianti("Vai strādā?", [
        {"jaut": "→→↑↑←←↓↓", "zim": _z("→→↑↑←←↓↓"),
         "opcijas": ["strādā", "nestrādā"], "jaukt": False, "pareizi": 0,
         "padoms": "2 un 2, 2 un 2."},
        {"jaut": "→→→↑↑←←↓↓", "zim": _z("→→→↑↑←←↓↓"),
         "opcijas": ["nestrādā - trūkst ←", "strādā"], "jaukt": False,
         "pareizi": 0, "padoms": "→ 3, ← 2."},
        {"jaut": "→↑↑←↓↓", "zim": _z("→↑↑←↓↓"),
         "opcijas": ["strādā", "nestrādā"], "jaukt": False, "pareizi": 0,
         "padoms": "1 un 1, 2 un 2."},
    ]),

    Varianti("Kā izlabot?", [
        {"jaut": "→→→↑↑←←←↓↓↓ - ko pielikt?",
         "opcijas": ["vēl vienu ↑", "vēl vienu →", "neko"],
         "pareizi": 0, "padoms": "↑ 2, ↓ 3."},
    ]),

    Petijums("Apmaiņa pārī", [
        "Uzraksti algoritmu savai figūrai.",
        "Samainieties ar pāri.",
        "Izpildi drauga algoritmu rūtiņās.",
        "Ja nestrādā - atrodi un izlabo kļūdu.",
    ], vajag="rūtiņu burtnīca"),

    Pasaule("Kļūda robota programmā",
            Varianti("", [
                {"jaut": "Robotam jāaizbrauc apkārt galdam un jāatgriežas. "
                         "Programma: →→↑↑←↓↓. Kas notiks?",
                 "opcijas": ["neatgriezīsies - trūkst ←", "atgriezīsies"],
                 "jaukt": False, "pareizi": 0, "padoms": "→ 2, ← 1."},
            ]),
            pavediens="tehnika",
            konteksts="Programmētāji pārbauda cits cita programmas.",
            kapec="Kļūdu atrast palīdz skaitīšana."),

    Kopsavilkums([
        "Izpildu cita algoritmu.",
        "Pārbaudu bultiņu skaitu.",
        "Atrodu un izlaboju kļūdu.",
    ]),

    Majas([
        "Uzraksti algoritmu ar apzinātu kļūdu mājiniekam.",
        "Vai viņš atrada kļūdu?",
        "Izlabojiet kopā.",
    ]),
]
