# -*- coding: utf-8 -*-
"""1. klase, 167. stunda: «Cik kubu būs nākamajā?»

Telpisku figūru virkne: kāpnes 1, 3, 6 kubi (katrā nākamajā klāt jauna
kolonna, par 1 augstāka), vai torņi 2, 4, 6. Atrod likumu un aprēķina kubu
skaitu nākamajā figūrā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, kubi)

TEMA = "Cik kubu būs nākamajā?"

MERKIS = ("Šodien veidosim telpisku figūru virkni un aprēķināsim kubu "
          "skaitu nākamajā figūrā.")


def _kapnes(n):
    return kubi([(x, 0, z) for x in range(n) for z in range(n - x)])


def _tornis(n):
    return kubi([(x, 0, z) for x in range(2) for z in range(n)])


SATURS = [
    Sakums("Kāpnes: 1, 3, 6 kubi - cik nākamajās?",
           zimejums=_kapnes(3),
           paraksts="Katrās nākamajās klāt kolonna par 1 augstāka.",
           fakti=["Atrodi, kas mainās.",
                  "1, 3, 6: +2, +3, tātad +4.",
                  "Nākamās kāpnes - 10 kubi."]),

    Slidnis("Kāpņu virkne", [
        {"v": "1", "teksts": "1 kubs", "zim": _kapnes(1)},
        {"v": "3", "teksts": "+2 = 3 kubi", "zim": _kapnes(2)},
        {"v": "6", "teksts": "+3 = 6 kubi", "zim": _kapnes(3)},
        {"v": "10", "teksts": "+4 = 10 kubi", "zim": _kapnes(4)},
    ]),

    Doma("Figūru virkne",
         "Kā skaitļu virknē: atrodi, par cik mainās katrs solis.",
         soli=[
             "Saskaiti kubus katrā figūrā.",
             "Atrodi, par cik tie mainās.",
             "Turpini ar likumu.",
         ]),

    Ievadi("Nākamā figūra", [
        {"jaut": "Torņi: 2, 4, 6 kubi. Nākamais?", "zim": _tornis(3),
         "atb": ["8"], "padoms": "+2."},
        {"jaut": "Kāpnes: 1, 3, 6, 10. Nākamās?", "atb": ["15"],
         "padoms": "+5."},
        {"jaut": "Rindas: 3, 6, 9 kubi. Nākamā?", "atb": ["12"],
         "padoms": "+3."},
    ]),

    Varianti("Kāds likums?", [
        {"jaut": "Torņi: 2, 4, 6, 8",
         "opcijas": ["katru reizi +2", "katru reizi +1",
                     "katru reizi divreiz"], "pareizi": 0,
         "padoms": "4 − 2 = 2."},
    ]),

    Pasaule("Piramīda no kastēm",
            Ievadi("", [
                {"jaut": "Veikalā kastes sakrāj kāpnēs: 1, 3, 6 kastes. Cik "
                         "kastu būs 4 pakāpienu kāpnēs?", "atb": ["10"],
                 "padoms": "6 + 4."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā kastes krauj skaistās kaudzēs.",
            kapec="Likums ļauj aprēķināt, neuzbūvējot."),

    Kopsavilkums([
        "Veidoju telpisku figūru virkni.",
        "Atrodu likumu.",
        "Aprēķinu kubu skaitu nākamajā figūrā.",
    ]),

    Majas([
        "Uzbūvē kāpnes no klucīšiem: 1, 2, 3 pakāpieni.",
        "Saskaiti kubus.",
        "Cik vajadzēs 5 pakāpieniem?",
    ]),
]
