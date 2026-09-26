# -*- coding: utf-8 -*-
"""9. klase, 157. stunda: «Kā konstruēt ievilktu riņķa līniju?»

Ievilktās riņķa līnijas centrs ir vienādā attālumā no visām malām, tātad
uz visu trīs bisektrišu - to krustpunktā. Rādiusu konstruē kā perpendikulu
no centra uz malu; aprēķinā r = S : p (p - pusperimetrs), taisnleņķa
trijstūrī r = (a + b − c) : 2. Zīmējumā 6-8-10 trijstūris ar r = 2.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā konstruēt ievilktu riņķa līniju?"

MERKIS = ("Konstruēsim trijstūrī ievilktu riņķa līniju un pamatosim centra "
          "vietu.")

_PUNKTI = [("A", 0, 0, -135), ("B", 8, 0, -45), ("C", 0, 6, 90),
           ("_La", 24.0 / 7, 24.0 / 7), ("_Lb", 0, 8.0 / 3),
           ("_Lc", 3, 0)]
_I = ("I", 2, 2, 200)
_K = ("K", 2, 0, -90)


def _solis(n):
    """Konstrukcijas n. solis: 1 - trijstūris ... 5 - riņķa līnija."""
    punkti = list(_PUNKTI)
    izcelti = []
    if n >= 2:
        izcelti.append(("A", "_La"))
    if n >= 3:
        izcelti.append(("B", "_Lb"))
        punkti.append(_I)
    if n >= 4:
        izcelti.append(("C", "_Lc"))
    taisni, nogriezni, rinki = [], ["AB", "BC", "CA"], []
    if n >= 5:
        punkti.append(_K)
        nogriezni.append("IK")
        taisni.append("IKB")
        rinki.append(("I", 2))
    return geometrija(punkti, nogriezni=nogriezni, izcelti=izcelti,
                      taisni=taisni, rinki=rinki)


SATURS = [
    Sakums("Lielākais aplis, kas ietilpst trijstūrī",
           zimejums=_solis(5),
           paraksts="Ievilktā riņķa līnija pieskaras visām trim malām.",
           fakti=["Centrs I - bisektrišu krustpunkts.",
                  "Rādiuss r = IK ⊥ AB.",
                  "r = S : p, kur p - pusperimetrs."]),

    Slidnis("Konstrukcija soli pa solim", [
        {"v": "1", "teksts": "Dots trijstūris ABC", "zim": _solis(1)},
        {"v": "2", "teksts": "Konstruē leņķa A bisektrisi",
         "zim": _solis(2)},
        {"v": "3", "teksts": "Leņķa B bisektrise - krustpunkts I",
         "zim": _solis(3)},
        {"v": "4", "teksts": "Pārbaude: arī C bisektrise iet caur I",
         "zim": _solis(4)},
        {"v": "5", "teksts": "IK ⊥ AB ir rādiuss - velc riņķa līniju",
         "zim": _solis(5)},
    ]),

    Doma("Kāpēc bisektrises?",
         "Katrs leņķa bisektrises punkts ir vienādā attālumā no leņķa "
         "malām, tātad bisektrišu krustpunkts - no visām trim malām.",
         soli=[
             "I uz A bisektrises: attālums līdz AB = attālums līdz AC.",
             "I uz B bisektrises: attālums līdz AB = attālums līdz BC.",
             "Visi trīs attālumi vienādi - tas ir r.",
         ],
         pieze="Tāpēc trešā bisektrise arī iet caur I: pietiek konstruēt "
               "divas."),

    Paraugs("Ievilktās riņķa līnijas rādiuss",
            uzd="Trijstūra malas 13, 14 un 15 cm, laukums 84 cm^2. Atrodi r.",
            soli=[
                ("p = (13 + 14 + 15) : 2 = 21", "Pusperimetrs."),
                ("r = S : p = 84 : 21", "S = p · r."),
                ("r = 4 cm", "Aprēķins."),
            ],
            atbilde="4 cm"),

    Petijums("Konstruē pats", [
        "Uzzīmē jebkuru trijstūri ABC.",
        "Ar cirkuli konstruē leņķu A un B bisektrises.",
        "Krustpunktā I no I novelc perpendikulu uz AB.",
        "Ar cirkuli (centrs I, rādiuss IK) velc riņķa līniju.",
    ], vajag="cirkulis, lineāls, zīmēšanas trijstūris",
       secinajums="Ja konstruēts precīzi, riņķa līnija pieskaras visām trim "
                  "malām."),

    Ievadi("Aprēķini r", [
        {"jaut": "Taisnleņķa trijstūris 6, 8, 10. r = ?", "atb": ["2"],
         "padoms": "(6 + 8 − 10) : 2."},
        {"jaut": "Taisnleņķa trijstūris 5, 12, 13. r = ?", "atb": ["2"],
         "padoms": "(5 + 12 − 13) : 2."},
        {"jaut": "S = 54, P = 36. r = ?", "atb": ["3"],
         "padoms": "p = 18."},
        {"jaut": "r = 3, p = 20. S = ?", "atb": ["60"], "padoms": "S = p · r."},
    ]),

    Varianti("Centrs", [
        {"jaut": "Ievilktās riņķa līnijas centrs ir...",
         "opcijas": ["bisektrišu krustpunkts",
                     "vidusperpendikulu krustpunkts",
                     "mediānu krustpunkts", "augstumu krustpunkts"],
         "pareizi": 0, "padoms": "Vienādi tālu no malām."},
        {"jaut": "Kur atrodas ievilktās riņķa līnijas centrs platleņķa "
                 "trijstūrim?",
         "opcijas": ["vienmēr iekšpusē", "ārpusē", "uz garākās malas",
                     "virsotnē"],
         "pareizi": 0, "padoms": "Bisektrises krustojas iekšā."},
    ]),

    Pasaule("Puķu dobe parkā",
            Ievadi("", [
                {"jaut": "Trijstūra parka malas 30, 40 un 50 m (taisnleņķa). "
                         "Lielākās apaļās dobes rādiuss (m)?", "atb": ["10"],
                 "padoms": "(30 + 40 − 50) : 2."},
                {"jaut": "Cik m^2 aizņems dobe? π ≈ 3,14.",
                 "atb": ["314"], "padoms": "π · 10^2."},
            ]),
            pavediens="daba",
            konteksts="Trijstūra formas parkā grib iekārtot pēc iespējas "
                      "lielāku apaļu puķu dobi.",
            kapec="Lielākais aplis trijstūrī ir ievilktais - tā centru "
                  "atrod ar bisektrisēm."),

    Kopsavilkums([
        "Konstruēju ievilktu riņķa līniju ar divām bisektrisēm.",
        "Pamatoju, kāpēc centrs ir bisektrišu krustpunktā.",
        "Aprēķinu r = S : p.",
    ]),

    Majas([
        "Konstruē ievilktu riņķa līniju vienādmalu trijstūrī ar malu 8 cm.",
        "Taisnleņķa trijstūra katetes 9 un 12. Aprēķini r.",
        "Salīdzini: kur ir apvilktās un kur ievilktās riņķa līnijas centrs?",
    ]),
]
