# -*- coding: utf-8 -*-
"""2. klase, 165. stunda: «Cik kubu ir ķermenī?»

No kubiem būvē taisnstūru skaldni: 3 kubi garumā, 2 platumā, 2 augstumā.
Viens slānis - 3 · 2 = 6, divi slāņi - 6 + 6 = 12. Reizināšana saskaita
kubus bez skaitīšanas pa vienam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, kubi)


def _bloks(garums, platums, augstums):
    """Taisnstūru skaldnis no kubiem."""
    return kubi([(x, y, z) for x in range(garums) for y in range(platums)
                 for z in range(augstums)])


TEMA = "Cik kubu ir ķermenī?"

MERKIS = ("Šodien no kubiem būvēsim ķermeni un aprēķināsim kubu skaitu, "
          "izmantojot reizināšanu.")

SATURS = [
    Sakums("Cik klucīšu ir šajā torņa pamatā?",
           zimejums=_bloks(3, 2, 2),
           paraksts="Viens slānis 3 · 2 = 6, divi slāņi - 12.",
           fakti=["Vispirms saskaiti vienu slāni.",
                  "Tad saskaiti slāņus.",
                  "Slāņu kubus saskaita vai reizina."]),

    Doma("Kubi slāņos",
         "Viena slāņa kubi = garums · platums; visi = slānis · slāņu skaits.",
         soli=[
             "Saskaiti kubus garumā: 3.",
             "Saskaiti rindas platumā: 2 - slānī 3 · 2 = 6.",
             "Saskaiti slāņus: 2.",
             "Kopā: 6 + 6 = 12.",
         ]),

    Slidnis("Būvējam slāni pa slānim", [
        {"v": "3", "teksts": "Viena rinda.", "zim": _bloks(3, 1, 1)},
        {"v": "3 · 2 = 6", "teksts": "Viens slānis.", "zim": _bloks(3, 2, 1)},
        {"v": "6 + 6 = 12", "teksts": "Divi slāņi.", "zim": _bloks(3, 2, 2)},
    ]),

    Ievadi("Cik kubu?", [
        {"jaut": "Cik kubu?", "zim": _bloks(4, 1, 2), "atb": ["8"],
         "padoms": "4 · 2."},
        {"jaut": "Cik kubu?", "zim": _bloks(2, 2, 2), "atb": ["8"],
         "padoms": "Slānī 4, divi slāņi."},
        {"jaut": "Cik kubu?", "zim": _bloks(5, 1, 3), "atb": ["15"],
         "padoms": "3 · 5."},
        {"jaut": "Cik kubu?", "zim": _bloks(3, 2, 3), "atb": ["18"],
         "padoms": "Slānī 6, trīs slāņi."},
    ]),

    Varianti("Kā saskaitīt?", [
        {"jaut": "Slānī 4 kubi, slāņu 5. Cik kubu?",
         "opcijas": ["20", "9", "45"], "pareizi": 0, "padoms": "5 · 4."},
        {"jaut": "Ja uzliek vēl vienu slāni no 6 kubiem uz 12, cik būs?",
         "opcijas": ["18", "13", "72"], "pareizi": 0, "padoms": "12 + 6."},
    ]),

    Petijums("Būvē pats", [
        "No 12 klucīšiem uzbūvē taisnstūru skaldni.",
        "Pieraksti: garums, platums, augstums.",
        "Uzbūvē citu formu no tiem pašiem 12.",
        "Cik dažādas formas izdevās?",
    ], vajag="12 vienādi klucīši"),

    Pasaule("Kastes kravas mašīnā",
            Ievadi("", [
                {"jaut": "Mašīnā kastes liek 5 garumā, 2 platumā un 3 "
                         "augstumā. Cik kastu vienā slānī?", "atb": ["10"],
                 "padoms": "5 · 2."},
                {"jaut": "Cik kastu visos 3 slāņos?", "atb": ["30"],
                 "padoms": "3 · 10."},
            ]),
            pavediens="tehnika",
            konteksts="Kravas mašīnā kastes sakrauj slāņos.",
            kapec="Reizināšana ātri pasaka, cik ietilpst."),

    Kopsavilkums([
        "Būvēju ķermeni no kubiem.",
        "Saskaitu kubus slānī ar reizināšanu.",
        "Saskaitu visus slāņus.",
    ]),

    Majas([
        "No cukura gabaliņiem vai klucīšiem uzbūvē skaldni.",
        "Aprēķini kubu skaitu, neskaitot pa vienam.",
        "Pārbaudi, saskaitot.",
    ]),
]
