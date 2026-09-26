# -*- coding: utf-8 -*-
"""9. klase, 25. stunda: «Kas ir trapeces viduslīnija?»

Trapeces viduslīnija savieno sānu malu viduspunktus. Tā atšķiras no
trijstūra viduslīnijas tikai ar to, ka pretī ir divi pamati, nevis viena
mala - to nākamajās stundās izmantos formulai.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija,
                         trapece)

TEMA = "Kas ir trapeces viduslīnija?"

MERKIS = "Definēsim trapeces viduslīniju un uzzīmēsim to."

_T = trapece(10, 4, 4, nobide=2, viduspunkti=True)


def _zim(izcelti=("MN",), svitras=True):
    sv = [("AM", 1), ("MD", 1), ("BN", 2), ("NC", 2)] if svitras else []
    return geometrija(_T, nogriezni=TRAPECES_MALAS, izcelti=list(izcelti),
                      svitras=sv)


SATURS = [
    Sakums("Kur trapecē ir viduslīnija?",
           zimejums=_zim(),
           paraksts="M un N - sānu malu viduspunkti.",
           fakti=["Viduslīnija savieno sānu malu viduspunktus.",
                  "Trapecei ir tikai viena viduslīnija.",
                  "Tā ir paralēla abiem pamatiem."]),

    Doma("Definīcija",
         "Trapeces viduslīnija ir nogrieznis, kas savieno tās sānu malu "
         "viduspunktus.",
         soli=[
             "Atrodi sānu malas (tās, kas nav paralēlas).",
             "Atzīmē katras viduspunktu.",
             "Savieno viduspunktus.",
         ],
         pieze="Nogrieznis starp pamatu viduspunktiem NAV viduslīnija."),

    Slidnis("Viduslīnija dažādās trapecēs", [
        {"v": "Vispārīga", "teksts": "MN savieno sānu malu viduspunktus",
         "zim": _zim()},
        {"v": "Vienādsānu", "teksts": "MN - uz simetrijas ass pusē augstuma",
         "zim": geometrija(trapece(10, 4, 4, viduspunkti=True),
                           nogriezni=TRAPECES_MALAS, izcelti=["MN"])},
        {"v": "Taisnleņķa", "teksts": "MN ⊥ taisnajai sānu malai",
         "zim": geometrija(trapece(10, 5, 4, nobide=0, viduspunkti=True),
                           nogriezni=TRAPECES_MALAS, izcelti=["MN"],
                           taisni=["BAD", "NMA"])},
    ]),

    Varianti("Viduslīnija vai nē?", [
        {"jaut": "Nogrieznis savieno AD un BC viduspunktus (AB ∥ DC).",
         "opcijas": ["Viduslīnija", "Diagonāle", "Augstums", "Nekas"],
         "pareizi": 0, "padoms": "AD un BC ir sānu malas."},
        {"jaut": "Nogrieznis savieno AB un DC viduspunktus.",
         "opcijas": ["Nav viduslīnija", "Viduslīnija", "Diagonāle",
                     "Pamats"],
         "pareizi": 0, "padoms": "AB un DC ir pamati."},
        {"jaut": "Cik viduslīniju ir trapecei?",
         "opcijas": ["1", "2", "3", "4"],
         "pareizi": 0, "padoms": "Viens sānu malu pāris."},
    ]),

    Ievadi("Viduspunkti un augstums", [
        {"jaut": "AD = 6 cm, M - viduspunkts. AM = ? cm", "atb": ["3"],
         "padoms": "Puse."},
        {"jaut": "Trapeces augstums 8 cm. Cik cm virs AB ir viduslīnija?",
         "atb": ["4"], "padoms": "Pusē augstuma."},
        {"jaut": "Uz skaitļu ass sānu malas gali ir 2 un 14. Viduspunkts?",
         "atb": ["8"], "padoms": "(2 + 14) : 2."},
    ]),

    Pasaule("Plaukts slīpā sienā",
            Ievadi("", [
                {"jaut": "Mansarda sienas šķērsgriezums - trapece ar "
                         "augstumu 2,4 m. Plauktu liek viduslīnijas "
                         "augstumā. Cik m no grīdas?", "atb": ["1,2"],
                 "padoms": "Puse no 2,4."},
                {"jaut": "Ja plauktu liek 0,3 m zemāk, cik m no grīdas?",
                 "atb": ["0,9"], "padoms": "1,2 − 0,3."},
            ]),
            pavediens="maja",
            konteksts="Viduslīnijas augstumā mansarda istaba ir tieši pusē - "
                      "tur plaukts izskatās līdzsvarots.",
            kapec="Viduslīnija ir pusē augstuma."),

    Kopsavilkums([
        "Definēju trapeces viduslīniju.",
        "Uzzīmēju to dažādās trapecēs.",
        "Zinu, ka tā ir paralēla pamatiem, pusē augstuma.",
    ]),

    Majas([
        "Uzzīmē trīs dažādas trapeces un to viduslīnijas.",
        "Izmēri viduslīniju un abus pamatus. Vai pamani sakarību?",
        "Pieraksti mērījumus tabulā - nākamajā stundā tos izmantosim.",
    ]),
]
