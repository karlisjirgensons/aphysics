# -*- coding: utf-8 -*-
"""9. klase, 135. stunda: «Kā progresiju attēlot grafiski?»

Aritmētiskās progresijas punkti (n; a_n) guļ uz taisnes y = dx + (a_1 − d):
diference ir slīpums. Tā progresija sasaistās ar lineāro funkciju no 8.
klases un 9.6. temata.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, plakne)

TEMA = "Kā progresiju attēlot grafiski?"

MERKIS = ("Attēlosim aritmētisko progresiju grafiski un saistīsim to ar "
          "lineāru funkciju.")


def _progresija(a1, d, n=6, **plakne_iest):
    punkti = [(k, a1 + (k - 1) * d, "") for k in range(1, n + 1)]
    return plakne(grafiki=[(d, a1 - d, "")], punkti=punkti, **plakne_iest)


SATURS = [
    Sakums("Punkti uz taisnes",
           zimejums=_progresija(2, 3, no_x=0, lidz_x=7, no_y=0, lidz_y=18,
                                solis_y=2),
           paraksts="2, 5, 8, 11, 14, 17 - slīpums d = 3.",
           fakti=["Punkti (n; a_n) guļ uz vienas taisnes.",
                  "Slīpums = diference d.",
                  "a_n = 3n − 1 - kā lineāra funkcija y = 3x − 1."]),

    Slidnis("Diference = slīpums", [
        {"v": "d = 3", "teksts": "Augoša, stāva",
         "zim": _progresija(2, 3, no_x=0, lidz_x=7, no_y=-6, lidz_y=18,
                            solis_y=3)},
        {"v": "d = 1", "teksts": "Augoša, lēzena",
         "zim": _progresija(2, 1, no_x=0, lidz_x=7, no_y=-6, lidz_y=18,
                            solis_y=3)},
        {"v": "d = −2", "teksts": "Dilstoša",
         "zim": _progresija(8, -2, no_x=0, lidz_x=7, no_y=-6, lidz_y=18,
                            solis_y=3)},
    ]),

    Doma("Progresija un lineāra funkcija",
         "a_n = a_1 + (n − 1)d = dn + (a_1 − d) - tā ir lineāra funkcija ar "
         "slīpumu d, tikai n ir naturāls.",
         soli=[
             "Slīpums k = d.",
             "Krustpunkts ar vertikālo asi: a_1 − d (tas ir «a_0»).",
             "Punktus nesavieno - n ir tikai 1, 2, 3, ...",
         ]),

    Ievadi("No grafika uz formulu", [
        {"jaut": "Punkti (1; 5), (2; 9), (3; 13). d = ?", "atb": ["4"],
         "padoms": "9 − 5."},
        {"jaut": "Tai pašai a_n = 4n + ?", "atb": ["1"],
         "padoms": "5 − 4."},
        {"jaut": "Punkti uz taisnes y = −2x + 20. a_1 = ?", "atb": ["18"],
         "padoms": "x = 1."},
        {"jaut": "Tai pašai d = ?", "atb": ["−2", "-2"], "padoms": "Slīpums."},
    ]),

    Varianti("Kurš grafiks?", [
        {"jaut": "a_n = 10 − n",
         "opcijas": ["Punkti uz dilstošas taisnes", "Punkti uz augošas taisnes",
                     "Horizontāli punkti", "Parabola"],
         "pareizi": 0, "padoms": "d = −1."},
        {"jaut": "d = 0",
         "opcijas": ["Punkti uz horizontāles", "Vertikāla taisne",
                     "Dilstoša", "Nav grafika"],
         "pareizi": 0, "padoms": "Visi vienādi."},
    ]),

    Pasaule("Svece deg",
            Ievadi("", [
                {"jaut": "Svece 24 cm, katru stundu īsāka par 1,5 cm. Garums "
                         "pēc 1. stundas beigām a_1 = ? cm", "atb": ["22,5"],
                 "padoms": "24 − 1,5."},
                {"jaut": "Pēc cik stundām svece izdegs?", "atb": ["16"],
                 "padoms": "24 : 1,5."},
            ]),
            pavediens="maja",
            konteksts="Degošas sveces garums ik stundu - dilstoša progresija.",
            kapec="Negatīvs slīpums - garums sarūk vienmērīgi.",
            zimejums=_progresija(22.5, -1.5, n=8, no_x=0, lidz_x=16, no_y=0,
                                 lidz_y=24, solis=2, solis_y=4)),

    Kopsavilkums([
        "Attēloju progresiju ar punktiem uz taisnes.",
        "Saistu diferenci ar slīpumu.",
        "Atrodu formulu no grafika.",
    ]),

    Majas([
        "Uzzīmē a_n = 2n − 3 pirmos 6 punktus.",
        "Uzraksti formulu progresijai, kuras punkti ir (1; 7), (2; 4), ...",
        "Novēro sveci vai ledu, kas kūst, un uzraksti progresiju.",
    ]),
]
