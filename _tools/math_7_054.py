# -*- coding: utf-8 -*-
"""7. klase, 54. stunda: «Kā izskatās funkcijas grafiks?»

Funkcijas grafiks ir visu punktu (x; f(x)) kopa. Lai to uzzīmētu,
aprēķina vērtību tabulu, atzīmē punktus un - ja argumenti var būt jebkuri -
savieno tos. Stunda to dara ar lineāru un nelineāru funkciju.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, Zimejums,
                         plakne, restis)

TEMA = "Kā izskatās funkcijas grafiks?"

MERKIS = ("Veidosim skaitļu pārus un atzīmēsim tos koordinātu plaknē, "
          "iegūstot funkcijas grafiku.")

_PUNKTI = [(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)]


def _soli(n):
    return plakne(punkti=_PUNKTI[:n], no_x=-3, lidz_x=3, no_y=-1, lidz_y=5,
                  solis=1)


SATURS = [
    Sakums("Grafiks ir punktu kopa",
           zimejums=plakne(grafiki=[([(x / 10.0, (x / 10.0) ** 2)
                                      for x in range(-22, 23)], "")],
                           punkti=_PUNKTI,
                           no_x=-3, lidz_x=3, no_y=-1, lidz_y=5, solis=1),
           paraksts="y = x²: pieci punkti, un līnija caur tiem.",
           fakti=["Katrs punkts ir pāris (arguments; vērtība).",
                  "Jo vairāk punktu, jo skaidrāk redz formu."]),

    Doma("Tabula → punkti → grafiks",
         "Funkcijas grafiks ir visu koordinātu plaknes punktu (x; f(x)) "
         "kopa. Grafiku zīmē, aprēķinot vērtību tabulu un atzīmējot punktus.",
         soli=[
             "Izvēlies dažus argumentus, arī negatīvus un 0.",
             "Aprēķini katram funkcijas vērtību.",
             "Atzīmē punktus (x; y).",
             "Ja argumenti var būt jebkuri skaitļi - savieno ar gludu līniju.",
         ],
         pieze="Ja punkti atrodas uz taisnes, pietiek ar diviem; ja uz "
               "līknes - vajag vairāk, lai redzētu formu."),

    Slidnis("Punkts pa punktam", [
        {"v": "x = −2", "teksts": "y = (−2)² = 4", "zim": _soli(1)},
        {"v": "x = −1", "teksts": "y = (−1)² = 1", "zim": _soli(2)},
        {"v": "x = 0", "teksts": "y = 0² = 0", "zim": _soli(3)},
        {"v": "x = 1", "teksts": "y = 1² = 1", "zim": _soli(4)},
        {"v": "x = 2", "teksts": "y = 2² = 4", "zim": _soli(5)},
    ], ievads="y = x²: katrs solis pievieno vienu punktu."),

    Paraugs("Uzzīmē y = 3 − x",
            uzd="Izveido tabulu x = −1; 0; 1; 2; 3 un nosaki grafika formu.",
            soli=[
                ("x = −1: y = 4; x = 0: y = 3", "3 − x."),
                ("x = 1: y = 2; x = 2: y = 1; x = 3: y = 0", "Turpina."),
                ("Punkti uz vienas taisnes", "Katru reizi −1."),
            ],
            atbilde="Grafiks ir taisne caur (0; 3) un (3; 0)."),

    Zimejums("y = 3 − x",
             plakne(grafiki=[(-1, 3, "y = 3 − x")],
                    punkti=[(-1, 4), (0, 3), (1, 2), (2, 1), (3, 0)],
                    no_x=-2, lidz_x=5, no_y=-2, lidz_y=5, solis=1),
             ievads="Tabula: (−1; 4), (0; 3), (1; 2), (2; 1), (3; 0)."),

    Ievadi("Aizpildi tabulu", [
        {"jaut": "y = 2x + 1. Cik ir y, ja x = −3?",
         "atb": ["−5", "-5"], "padoms": "−6 + 1."},
        {"jaut": "y = x² − 1. Cik ir y, ja x = −3?",
         "atb": ["8"], "padoms": "9 − 1."},
        {"jaut": "Vai punkts (2; 5) ir uz grafika y = 2x + 1? Raksti «jā» "
                 "vai «nē».",
         "atb": ["jā", "ja"], "padoms": "2 · 2 + 1 = 5."},
        {"jaut": "Vai punkts (−1; 1) ir uz grafika y = 2x + 1?",
         "atb": ["nē", "ne"], "padoms": "2 · (−1) + 1 = −1."},
    ]),

    Varianti("Kāda forma?", [
        {"jaut": "Punkti (0; 1), (1; 3), (2; 5), (3; 7). Forma?",
         "opcijas": ["Taisne", "Līkne", "Aplis", "Nevar zināt"],
         "pareizi": 0,
         "padoms": "Katru reizi +2."},
        {"jaut": "Punkti (0; 0), (1; 1), (2; 4), (3; 9). Forma?",
         "opcijas": ["Līkne", "Taisne", "Aplis", "Horizontāla taisne"],
         "pareizi": 0,
         "padoms": "Pieaugumi 1, 3, 5 - nav vienādi."},
    ]),

    Pasaule("Bumbas lidojums",
            Ievadi("", [
                {"jaut": "Bumbas augstums h(t) = 20t − 5t² (m). Cik m pēc "
                         "1 s?",
                 "atb": ["15"], "padoms": "20 − 5."},
                {"jaut": "Cik m pēc 2 s?",
                 "atb": ["20"], "padoms": "40 − 20."},
                {"jaut": "Pēc cik sekundēm bumba nokrīt (h = 0, t > 0)?",
                 "atb": ["4"], "padoms": "Pārbaudi t = 4: 80 − 80."},
            ]),
            pavediens="sports",
            konteksts="Bumbas lidojuma grafiks ir līkne - to sporta analītiķi "
                      "zīmē pēc video punktiem.",
            kapec="Punkti pa laikam veido grafiku."),

    Zimejums("Bumbas augstums",
             restis([["t, s", "0", "1", "2", "3", "4"],
                     ["h, m", "0", "15", "20", "15", "0"]]),
             paskaidro="Augšā un lejā simetriski - grafiks ir līkne."),

    Kopsavilkums([
        "Zinu, ka grafiks ir punktu (x; f(x)) kopa.",
        "Veidoju vērtību tabulu un atzīmēju punktus.",
        "Pārbaudu, vai punkts ir uz grafika.",
        "Atšķiru taisni no līknes pēc pieaugumiem.",
    ]),

    Majas([
        "Uzzīmē y = x² − 2 grafiku no x = −3 līdz 3.",
        "Uzzīmē y = 2x − 3 grafiku.",
        "Salīdzini abu grafiku formas.",
    ]),
]
