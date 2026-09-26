# -*- coding: utf-8 -*-
"""9. klase, 144. stunda: «Kā konstruēt apvilktu riņķa līniju?»

Konstrukcija ar cirkuli un lineālu: divu malu vidusperpendikuli, to
krustpunkts O, rādiuss OA. Eksāmena 19. uzdevums (2025): punkts, kurā
krustojas vidusperpendikuli, ir apvilktās riņķa līnijas centrs.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Pasaule, Petijums,
                         Sakums, Slidnis, Varianti, geometrija, uz_rinka)

TEMA = "Kā konstruēt apvilktu riņķa līniju?"

MERKIS = ("Ar cirkuli un lineālu konstruēsim ap trijstūri apvilktu riņķa "
          "līniju.")

_P = [uz_rinka("A", 200), uz_rinka("B", 320), uz_rinka("C", 80),
      ("O", 0, 0, -45)]


def _zim(solis):
    izc = []
    if solis >= 2:
        izc.append(("O", "_m1"))
    if solis >= 3:
        izc.append(("O", "_m2"))
    punkti = _P + [("_m1", (_P[0][1] + _P[1][1]) / 2, (_P[0][2] + _P[1][2]) / 2),
                   ("_m2", (_P[1][1] + _P[2][1]) / 2, (_P[1][2] + _P[2][2]) / 2)]
    if solis < 3:
        punkti = [p for p in punkti if p[0] != "O"] + (
            [("_O", 0, 0)] if solis == 2 else [])
        izc = [("_O", "_m1")] if solis == 2 else []
    return geometrija(punkti, nogriezni=["AB", "BC", "CA"], izcelti=izc,
                      rinki=[("O", 5)] if solis >= 4 else [])


SATURS = [
    Sakums("Riņķa līnija caur visām trim virsotnēm",
           zimejums=_zim(4),
           paraksts="Apvilktā riņķa līnija - caur A, B un C.",
           fakti=["Centrs - malu vidusperpendikulu krustpunkts.",
                  "Rādiuss R = OA = OB = OC.",
                  "Ap jebkuru trijstūri var apvilkt tieši vienu."]),

    Slidnis("Konstrukcija", [
        {"v": "1", "teksts": "Trijstūris ABC", "zim": _zim(1)},
        {"v": "2", "teksts": "AB vidusperpendikuls (ar cirkuli no A un B "
                             "vienādi loki)", "zim": _zim(2)},
        {"v": "3", "teksts": "BC vidusperpendikuls; krustpunkts O",
         "zim": _zim(3)},
        {"v": "4", "teksts": "Riņķa līnija ar centru O un rādiusu OA",
         "zim": _zim(4)},
    ]),

    Doma("Konstrukcijas soļi",
         "Konstruē divu malu vidusperpendikulus, krustpunkts ir centrs O, "
         "rādiuss - attālums līdz virsotnei.",
         soli=[
             "No A un B ar vienādu rādiusu (> {AB|2}) loki abās pusēs.",
             "Lokos krustpunktus savieno - vidusperpendikuls.",
             "Atkārto ar otru malu.",
             "Cirkuli ieliek O, atver līdz A un velk riņķa līniju.",
         ]),

    Petijums("Konstruē pats", [
        "Uzzīmē šaurleņķa trijstūri ar malām 6, 7 un 8 cm.",
        "Konstruē divu malu vidusperpendikulus.",
        "Pārbaudi ar trešo vidusperpendikulu - vai tas iet caur O?",
        "Novelc apvilkto riņķa līniju un izmēri R.",
    ], vajag="cirkulis, lineāls",
       secinajums="Visi trīs vidusperpendikuli krustojas vienā punktā."),

    Varianti("Eksāmens 2025, 19. uzdevums", [
        {"jaut": "Trijstūrim ABC konstruēti malu vidusperpendikuli, tie "
                 "krustojas punktā O. Punkts O ir...",
         "opcijas": ["apvilktās riņķa līnijas centrs",
                     "augstumu krustpunkts", "mediānu krustpunkts",
                     "ievilktās riņķa līnijas centrs"],
         "pareizi": 0, "padoms": "Vienādi tālu no virsotnēm."},
        {"jaut": "Cik vidusperpendikulu minimāli vajag konstruēt?",
         "opcijas": ["2", "1", "3", "4"],
         "pareizi": 0, "padoms": "Krustpunktam pietiek ar diviem."},
    ]),

    Pasaule("Apaļais galds trim krēsliem",
            Varianti("", [
                {"jaut": "Trīs vecas kolonnas stāv trijstūrī. Arhitekts grib "
                         "apaļu jumtu, kura mala iet caur visām. Kā atrast "
                         "centru?",
                 "opcijas": ["Divu vidusperpendikulu krustpunkts",
                             "Viduspunkts starp divām kolonnām",
                             "Bisektrišu krustpunkts", "Jebkur iekšā"],
                 "pareizi": 0, "padoms": "Apvilktā riņķa līnija."},
            ]),
            pavediens="maja",
            konteksts="Restaurācijā bieži jāatrod senā apļa centrs pēc trim "
                      "saglabātiem punktiem.",
            kapec="Trīs punkti nosaka tieši vienu riņķa līniju."),

    Kopsavilkums([
        "Konstruēju vidusperpendikulu ar cirkuli.",
        "Konstruēju ap trijstūri apvilktu riņķa līniju.",
        "Zinu, ka centrs ir vidusperpendikulu krustpunkts.",
    ]),

    Majas([
        "Konstruē apvilktu riņķa līniju trijstūrim 5, 5, 6 cm.",
        "Atrodi apaļa šķīvja centru, atzīmējot 3 punktus uz tā malas.",
        "Kāpēc caur 3 punktiem uz vienas taisnes riņķa līniju novilkt nevar?",
    ]),
]
