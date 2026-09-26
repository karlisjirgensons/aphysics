# -*- coding: utf-8 -*-
"""1. klase, 9. stunda: «Kura diena bija vakar?»

Nedēļas dienas ir virkne, kas atkārtojas: pēc svētdienas atkal pirmdiena.
Vakar - solis atpakaļ, rīt - solis uz priekšu, parīt - divi soļi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Kura diena bija vakar?"

MERKIS = ("Šodien nosauksim nedēļas dienas pēc kārtas un noteiksim, kura "
          "diena bija vakar un būs rīt.")

_DIENAS = ["pirmdiena", "otrdiena", "trešdiena", "ceturtdiena",
           "piektdiena", "sestdiena", "svētdiena"]
_TABULA = restis([["P", "O", "T", "C", "Pk", "S", "Sv"],
                  [1, 2, 3, 4, 5, 6, 7]])


def _karta(sodien, nobide, jaut):
    i = _DIENAS.index(sodien)
    pareiza = _DIENAS[(i + nobide) % 7]
    citas = [_DIENAS[(i + n) % 7] for n in (-nobide, 3, 0) if n != nobide]
    citas = [c for c in dict.fromkeys(citas) if c != pareiza][:2]
    return {"jaut": "Šodien ir %s. %s" % (sodien, jaut),
            "opcijas": [pareiza] + citas, "pareizi": 0,
            "padoms": "Skaiti pa nedēļas dienām."}


SATURS = [
    Sakums("Kāpēc pēc svētdienas atkal nāk pirmdiena?",
           zimejums=_TABULA,
           paraksts="7 dienas - un nedēļa sākas no jauna.",
           fakti=["Nedēļa ir virkne, kas atkārtojas.",
                  "Vakar - viena diena atpakaļ.",
                  "Rīt - viena diena uz priekšu."]),

    Doma("Solis atpakaļ, solis uz priekšu",
         "Vakar ir diena pirms šodienas, rīt - diena pēc šodienas.",
         soli=[
             "Atrodi šodienu tabulā.",
             "Vakar - solis pa kreisi.",
             "Rīt - solis pa labi; parīt - divi soļi.",
             "Pēc svētdienas atgriezies pie pirmdienas.",
         ]),

    Varianti("Kura diena?", [
        _karta("trešdiena", -1, "Kura diena bija vakar?"),
        _karta("trešdiena", 1, "Kura diena būs rīt?"),
        _karta("piektdiena", 2, "Kura diena būs parīt?"),
        _karta("svētdiena", 1, "Kura diena būs rīt?"),
        _karta("pirmdiena", -1, "Kura diena bija vakar?"),
        _karta("otrdiena", -2, "Kura diena bija aizvakar?"),
    ], pamats=4),

    Ievadi("Skaiti dienas", [
        {"jaut": "Cik dienu ir nedēļā?", "atb": ["7"],
         "padoms": "No pirmdienas līdz svētdienai."},
        {"jaut": "Cik skolas dienu ir nedēļā?", "atb": ["5"],
         "padoms": "No pirmdienas līdz piektdienai."},
        {"jaut": "Kura diena pēc kārtas ir ceturtdiena?", "atb": ["4"],
         "padoms": "Skaiti no pirmdienas."},
    ]),

    Pasaule("Kad ir peldēšana?",
            Varianti("", [
                {"jaut": "Peldēšana ir ceturtdienā. Šodien ir otrdiena. Pēc "
                         "cik dienām?",
                 "opcijas": ["pēc 2 dienām", "rīt", "pēc 3 dienām"],
                 "jaukt": False, "pareizi": 0,
                 "padoms": "Trešdiena, ceturtdiena."},
                {"jaut": "Brīvdienas ir sestdiena un svētdiena. Šodien ir "
                         "piektdiena. Kad sāksies brīvdienas?",
                 "opcijas": ["rīt", "parīt", "šodien"], "jaukt": False,
                 "pareizi": 0, "padoms": "Pēc piektdienas ir sestdiena."},
            ]),
            pavediens="sports",
            konteksts="Klasei katru nedēļu ir peldēšana baseinā.",
            kapec="Nedēļas dienas palīdz saplānot, kas notiks."),

    Kopsavilkums([
        "Nosaucu nedēļas dienas pēc kārtas.",
        "Nosaku, kura diena bija vakar un būs rīt.",
        "Zinu, ka pēc svētdienas atkal nāk pirmdiena.",
    ]),

    Majas([
        "Katru vakaru pasaki, kura diena būs rīt.",
        "Uzzīmē nedēļas kalendāru un atzīmē savas nodarbības.",
        "Kura diena būs pēc 7 dienām? Pārbaudi!",
    ]),
]
