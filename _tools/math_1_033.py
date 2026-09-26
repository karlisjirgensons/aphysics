# -*- coding: utf-8 -*-
"""1. klase, 33. stunda: «Ko dara ar lineālu, ja neesi zīmētājs?»

Lineāls ir skaitļu taisne: saskaitot lec pa labi, atņemot - pa kreisi.
Skaitļi ir iedaļās, nevis rūtiņās - lec no iedaļas uz iedaļu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, lineals, taisne)

TEMA = "Ko dara ar lineālu, ja neesi zīmētājs?"

MERKIS = ("Šodien saskaitīsim un atņemsim, lecot pa lineālu kā pa skaitļu "
          "taisni.")


def _lec(no, uz):
    solis = 1 if uz > no else -1
    return taisne(0, 10, 1, [(uz, str(uz))],
                  bultas=[(i, i + solis, "") for i in range(no, uz, solis)])


SATURS = [
    Sakums("Lineāls - arī skaitļu taisne!",
           zimejums=lineals(10),
           paraksts="Skaitļi pie iedaļām no 0 līdz 10.",
           fakti=["Saskaitot lec pa labi.",
                  "Atņemot lec pa kreisi.",
                  "Lec no iedaļas uz iedaļu."]),

    Slidnis("3 + 4 un 7 − 4", [
        {"v": "3 + 4", "teksts": "No 3 četri lēcieni pa labi: 7",
         "zim": _lec(3, 7)},
        {"v": "7 − 4", "teksts": "No 7 četri lēcieni pa kreisi: 3",
         "zim": _lec(7, 3)},
    ]),

    Doma("Lēcieni pa taisni",
         "Pirmais skaitlis - kur stāvi; otrais - cik lēcienu.",
         soli=[
             "Noliec pirkstu uz pirmā skaitļa.",
             "«+» - lec pa labi, «−» - pa kreisi.",
             "Skaiti lēcienus, nevis iedaļas.",
             "Kur apstājies - tā ir atbilde.",
         ]),

    Ievadi("Lec pa taisni", [
        {"jaut": "2 + 5 = ?", "zim": _lec(2, 7), "atb": ["7"],
         "padoms": "Kur beidzas bultas?"},
        {"jaut": "9 − 3 = ?", "zim": _lec(9, 6), "atb": ["6"],
         "padoms": "Kur beidzas bultas?"},
        {"jaut": "4 + 4 = ?", "atb": ["8"], "padoms": "No 4 četri lēcieni."},
        {"jaut": "10 − 6 = ?", "atb": ["4"],
         "padoms": "No 10 seši lēcieni pa kreisi."},
        {"jaut": "1 + 8 = ?", "atb": ["9"], "padoms": "No 8 viens lēciens."},
        {"jaut": "8 − 5 = ?", "atb": ["3"], "padoms": "No 8 pieci pa kreisi."},
    ], pamats=4),

    Varianti("Kurš piemērs zīmējumā?", [
        {"jaut": "Kas uzzīmēts?", "zim": _lec(5, 8),
         "opcijas": ["5 + 3 = 8", "8 − 3 = 5", "5 + 8"], "pareizi": 0,
         "padoms": "No 5 uz labo pusi."},
        {"jaut": "Kas uzzīmēts?", "zim": _lec(6, 2),
         "opcijas": ["6 − 4 = 2", "2 + 4 = 6", "6 − 2 = 4"], "pareizi": 0,
         "padoms": "No 6 uz kreiso pusi 4 lēcieni."},
    ]),

    Pasaule("Vardīte pa akmeņiem",
            Ievadi("", [
                {"jaut": "Vardīte sēž uz 3. akmens un palec 5 akmeņus uz "
                         "priekšu. Uz kura tagad?", "atb": ["8"],
                 "padoms": "3 + 5."},
                {"jaut": "Tad lec 6 atpakaļ. Uz kura?", "atb": ["2"],
                 "padoms": "8 − 6."},
            ]),
            pavediens="daba",
            konteksts="Pāri strautam akmeņi sanumurēti no 0 līdz 10.",
            kapec="Akmeņu rinda ir skaitļu taisne."),

    Kopsavilkums([
        "Lietoju lineālu kā skaitļu taisni.",
        "Saskaitot lecu pa labi, atņemot - pa kreisi.",
        "Skaitu lēcienus, nevis iedaļas.",
    ]),

    Majas([
        "Ar lineālu izrēķini 4 + 5 un 9 − 5.",
        "Uzzīmē skaitļu taisni no 0 līdz 10 un parādi 6 + 3.",
        "Uz grīdas sanumurē 10 papīra lapas un lec!",
    ]),
]
