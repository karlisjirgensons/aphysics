# -*- coding: utf-8 -*-
"""9. klase, 154. stunda: «Cik kopīgu punktu var būt taisnei un riņķa līnijai?»

Taisnes attālums līdz centram d salīdzina ar rādiusu R: d > R - neviena
kopīga punkta, d = R - viens (pieskare), d < R - divi (sekante). Sekantes
nogrieztā horda nāk no iepriekšējās stundas hordas īpašības.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija)

TEMA = "Cik kopīgu punktu var būt taisnei un riņķa līnijai?"

MERKIS = ("Noteiksim taisnes un riņķa līnijas savstarpējo novietojumu pēc "
          "attāluma līdz centram.")


def _taisne(d):
    """Riņķa līnija R = 5 un horizontāla taisne attālumā d zem centra."""
    pamats = "T" if d == 5 else "H"
    punkti = [("O", 0, 0, 90), ("_P", -7, -d), ("_Q", 7, -d),
              (pamats, 0, -d, -90)]
    if d < 5:
        punkti += [("A", -4, -d, -120), ("B", 4, -d, -60)]
    return geometrija(punkti, nogriezni=[("_P", "_Q"), ("O", pamats)],
                      taisni=[("O", pamats, "_Q")],
                      malas=[(("O", pamats), "d = %d" % d)],
                      rinki=[("O", 5)])


SATURS = [
    Sakums("Taisne tuvojas riņķa līnijai - cik kopīgu punktu?",
           zimejums=_taisne(3),
           paraksts="R = 5, d = 3: taisne krusto riņķa līniju divos punktos.",
           fakti=["d - attālums no centra līdz taisnei (perpendikuls).",
                  "Salīdzina d ar rādiusu R.",
                  "Kopīgo punktu var būt 0, 1 vai 2."]),

    Slidnis("Taisne tuvojas centram", [
        {"v": "d = 7", "teksts": "d > R - kopīgu punktu nav",
         "zim": _taisne(7)},
        {"v": "d = 5", "teksts": "d = R - viens punkts T: pieskare",
         "zim": _taisne(5)},
        {"v": "d = 3", "teksts": "d < R - divi punkti: sekante",
         "zim": _taisne(3)},
    ]),

    Doma("Trīs gadījumi",
         "Ja d > R, kopīgu punktu nav; ja d = R, ir viens (pieskare); ja "
         "d < R, ir divi (sekante).",
         soli=[
             "No centra novelc perpendikulu uz taisni - tas ir d.",
             "Salīdzini d ar R.",
             "Sekantei hordu AB atrod ar Pitagoru: AH^2 = R^2 − d^2.",
         ],
         pieze="Pieskarei ir tieši viens kopīgs punkts - pieskaršanās punkts."),

    Ievadi("Cik kopīgu punktu?", [
        {"jaut": "R = 6, d = 4", "atb": ["2"], "padoms": "d < R."},
        {"jaut": "R = 6, d = 6", "atb": ["1"], "padoms": "d = R."},
        {"jaut": "R = 6, d = 9", "atb": ["0"], "padoms": "d > R."},
        {"jaut": "Diametrs 10, d = 5", "atb": ["1"],
         "padoms": "Rādiuss ir 5."},
    ]),

    Ievadi("Sekantes horda", [
        {"jaut": "R = 5, d = 3. Hordas AB garums?", "atb": ["8"],
         "padoms": "AH = √(25 − 9) = 4."},
        {"jaut": "R = 13, d = 5. AB = ?", "atb": ["24"],
         "padoms": "AH = 12."},
        {"jaut": "R = 10, AB = 12. d = ?", "atb": ["8"],
         "padoms": "√(100 − 36)."},
        {"jaut": "R = 8, d - vesels skaitlis. Lielākais d, lai būtu divi "
                 "kopīgi punkti?", "atb": ["7"], "padoms": "d < 8."},
    ]),

    Varianti("Nosauc taisni", [
        {"jaut": "Taisnei ar riņķa līniju ir divi kopīgi punkti. Tā ir...",
         "opcijas": ["sekante", "pieskare", "horda", "rādiuss"],
         "pareizi": 0, "padoms": "Divi punkti - sekante."},
        {"jaut": "Taisnei ar riņķa līniju ir viens kopīgs punkts. Tā ir...",
         "opcijas": ["pieskare", "sekante", "diametrs", "loks"],
         "pareizi": 0, "padoms": "Viens punkts - pieskare."},
        {"jaut": "Ar ko atšķiras horda no sekantes?",
         "opcijas": ["horda ir nogrieznis, sekante - taisne",
                     "nekā", "horda iet caur centru",
                     "sekante ir īsāka"],
         "pareizi": 0, "padoms": "Sekante turpinās abos virzienos."},
    ]),

    Pasaule("Radara zona",
            Ievadi("", [
                {"jaut": "Radars redz 5 km rādiusā. Kuģu ceļš iet 3 km no "
                         "radara. Cik km ceļa ir radara zonā?",
                 "atb": ["8"], "padoms": "Horda: 2 · √(25 − 9)."},
                {"jaut": "Cik km no radara jāiet ceļam, lai tas zonai tikai "
                         "pieskartos?", "atb": ["5"], "padoms": "d = R."},
                {"jaut": "Ceļš iet 6 km no radara. Cik km ceļa ir zonā?",
                 "atb": ["0"], "padoms": "d > R."},
            ]),
            pavediens="celojums",
            konteksts="Ostas radars redz kuģus līdz 5 km attālumā; kuģu ceļš "
                      "ir taisne.",
            kapec="Taisnes un riņķa līnijas novietojums nosaka, vai kuģis "
                  "vispār nonāk radara redzeslokā.",
            zimejums=_taisne(3)),

    Kopsavilkums([
        "Salīdzinu attālumu d ar rādiusu R.",
        "Atšķiru sekanti, pieskari un taisni bez kopīgiem punktiem.",
        "Aprēķinu hordu, ko nogriež sekante.",
    ]),

    Majas([
        "Uzzīmē riņķa līniju R = 3 cm un trīs taisnes: d = 2, 3 un 4 cm.",
        "R = 17, d = 8. Aprēķini sekantes nogriezto hordu.",
        "Kur dzīvē taisne pieskaras aplim? Atrodi divus piemērus.",
    ]),
]
