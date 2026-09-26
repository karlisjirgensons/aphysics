# -*- coding: utf-8 -*-
"""1. klase, 91. stunda: «Cik gara ir šī lauztā līnija?»

Lauzta līnija 10-20 cm garumā: posmus izmēra un saskaita ar desmita
pāriešanu (7 cm + 6 cm = 13 cm). Zīmē līniju pēc nosacījumiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, linijas)

TEMA = "Cik gara ir šī lauztā līnija?"

MERKIS = ("Šodien zīmēsim lauztu līniju pēc nosacījumiem un aprēķināsim "
          "tās garumu.")


def _lauzta(punkti, garumi):
    nogr = [(punkti[i][0], punkti[i][1], punkti[i + 1][0], punkti[i + 1][1])
            for i in range(len(punkti) - 1)]
    uzr = [((a + c) / 2.0, (b + d) / 2.0 + 0.7, "%d cm" % g)
           for (a, b, c, d), g in zip(nogr, garumi)]
    return linijas(nogr, uzraksti=uzr, punkti=punkti, platums=12,
                   augstums=6)


SATURS = [
    Sakums("7 cm + 6 cm - cik gara līnija?",
           zimejums=_lauzta([(0, 1), (5, 5), (11, 1)], [7, 6]),
           paraksts="7 + 6 = 13 - līnija 13 cm.",
           fakti=["Saskaiti posmu garumus.",
                  "Ja vajag - caur 10: 7 + 3 + 3.",
                  "Rezultātu raksti ar cm."]),

    Doma("Garums pēc nosacījuma",
         "Ja zināms visas līnijas garums un viens posms, otru atrod ar "
         "atņemšanu.",
         soli=[
             "Izmēri katru posmu.",
             "Saskaiti: 7 cm + 6 cm = 13 cm.",
             "Zīmējot - izvēlies posmus, kas kopā dod vajadzīgo.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "Posmi 8 cm un 5 cm. Kopā (cm)?",
         "zim": _lauzta([(0, 1), (6, 5), (11, 1)], [8, 5]), "atb": ["13"],
         "padoms": "8 + 2 + 3."},
        {"jaut": "Posmi 4 cm, 5 cm un 6 cm. Kopā (cm)?",
         "zim": _lauzta([(0, 1), (3, 5), (7, 1), (11, 5)], [4, 5, 6]),
         "atb": ["15"], "padoms": "4 + 6 = 10, un 5."},
        {"jaut": "Līnija 14 cm, pirmais posms 9 cm. Otrais (cm)?",
         "atb": ["5"], "padoms": "9 + ? = 14."},
        {"jaut": "Trīs posmi pa 6 cm. Kopā (cm)?", "atb": ["18"],
         "padoms": "6 + 6 + 6."},
    ]),

    Varianti("Kura līnija der?", [
        {"jaut": "Vajag 12 cm garu līniju no 2 posmiem.",
         "opcijas": ["7 cm un 5 cm", "7 cm un 6 cm", "5 cm un 5 cm"],
         "pareizi": 0, "padoms": "7 + 5 = 12."},
        {"jaut": "Vajag 16 cm no 2 vienādiem posmiem.",
         "opcijas": ["8 cm un 8 cm", "6 cm un 6 cm", "9 cm un 7 cm"],
         "pareizi": 0, "padoms": "8 + 8 = 16."},
    ]),

    Petijums("Zīmē pēc nosacījuma", [
        "Uzzīmē lauztu līniju ar 2 posmiem - kopā 13 cm.",
        "Uzzīmē līniju ar 3 posmiem - kopā 15 cm.",
        "Izmēri un pārbaudi.",
    ], vajag="lineāls, zīmulis, burtnīca"),

    Pasaule("Takas parkā",
            Ievadi("", [
                {"jaut": "Karte: taka no vārtiem līdz strūklakai 9 cm, līdz "
                         "soliņam vēl 7 cm. Cik cm kartē?", "atb": ["16"],
                 "padoms": "9 + 1 + 6."},
            ]),
            pavediens="celojums",
            konteksts="Parka kartē takas ir lauztas līnijas.",
            kapec="Kartē garumu saskaita tāpat kā burtnīcā."),

    Kopsavilkums([
        "Aprēķinu lauztas līnijas garumu līdz 20 cm.",
        "Zīmēju līniju pēc nosacījuma.",
        "Atrodu trūkstošā posma garumu.",
    ]),

    Majas([
        "Uzzīmē lauztu līniju 17 cm garumā.",
        "Ar diegu izmēri lauztu ceļu kartē.",
        "Izdomā uzdevumu par takām.",
    ]),
]
