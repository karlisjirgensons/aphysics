# -*- coding: utf-8 -*-
"""9. klase, 5. stunda: «Kādas ir viduslīnijas īpašības?»

Viduslīnija ir paralēla trešajai malai un ir tās puse. Pierādījums iet pa
soļiem ar Talesa teorēmu un paralelogramu - tieši tā, kā to prasa
eksāmenā: katram solim savs pamatojums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kādas ir viduslīnijas īpašības?"

MERKIS = ("Formulēsim un pierādīsim trijstūra viduslīnijas īpašību.")

_PUNKTI = [("A", 0, 0), ("B", 10, 0), ("C", 3, 7), ("M", 1.5, 3.5),
           ("N", 6.5, 3.5)]
_K = ("K", 5, 0)            # AB viduspunkts - tikai pierādījuma 2. un 3. solī


def _zim(izcelti, malas=(), svitras=(), iekrasot=()):
    ar_k = "K" in repr((izcelti, svitras, iekrasot))
    return geometrija(_PUNKTI + ([_K] if ar_k else []),
                      nogriezni=["AB", "BC", "CA"],
                      izcelti=izcelti, malas=list(malas),
                      svitras=list(svitras), iekrasot=list(iekrasot))


SATURS = [
    Sakums("Kāpēc virve ir tieši puse?",
           zimejums=_zim(["MN"], malas=[("AB", "1,2 m"), ("MN", "?")],
                         svitras=[("AM", 1), ("MC", 1), ("CN", 2),
                                  ("NB", 2)]),
           paraksts="Iepriekšējās stundas kāpnes: MN = 0,6 m.",
           fakti=["Viduslīnija ir paralēla trešajai malai.",
                  "Viduslīnija ir puse no trešās malas.",
                  "To var pierādīt ar Talesa teorēmu."]),

    Doma("Viduslīnijas īpašība",
         "Trijstūra viduslīnija ir paralēla trešajai malai un vienāda ar tās "
         "pusi: MN ∥ AB un MN = {AB|2}.",
         pieze="Otrādi: ja caur vienas malas viduspunktu velk paralēli "
               "otrai malai, tā iet caur trešās malas viduspunktu."),

    Slidnis("Pierādījums pa soļiem", [
        {"v": "Dots", "teksts": "CM = MA, CN = NB. Jāpierāda: MN ∥ AB, "
                                "MN = {AB|2}.",
         "zim": _zim(["MN"], svitras=[("AM", 1), ("MC", 1), ("CN", 2),
                                      ("NB", 2)])},
        {"v": "1", "teksts": "Caur M velk taisni ∥ AB. Tā kā CM = MA, "
                             "Talesa teorēma: tā krusto BC viduspunktā N. "
                             "Tātad MN ∥ AB.",
         "zim": _zim(["MN"], svitras=[("AM", 1), ("MC", 1)])},
        {"v": "2", "teksts": "Caur N velk NK ∥ AC. Tā kā CN = NB, tā krusto "
                             "AB viduspunktā K: AK = KB = {AB|2}.",
         "zim": _zim(["MN", "NK"], svitras=[("AK", 3), ("KB", 3)])},
        {"v": "3", "teksts": "AMNK: MN ∥ AK un NK ∥ AM - paralelograms. "
                             "Tātad MN = AK = {AB|2}.",
         "zim": _zim(["MN", "NK"], iekrasot=[("AKNM", 1)])},
    ], ievads="Katram solim ir pamatojums - tā pieraksta pierādījumu."),

    Petijums("Pārbaudi ar mērījumu", [
        "Uzzīmē trīs dažādus trijstūrus: šaurleņķa, taisnleņķa, platleņķa.",
        "Katrā novelc vienu viduslīniju.",
        "Izmēri viduslīniju un pretējo malu, aprēķini attiecību.",
        "Pārbaudi paralelitāti ar trijstūri un lineālu.",
    ], vajag="lineāls, zīmēšanas trijstūris",
       secinajums="Attiecība vienmēr ir 1 : 2 - neatkarīgi no trijstūra "
                  "veida."),

    Ievadi("Lieto īpašību", [
        {"jaut": "AB = 14 cm. Viduslīnija MN = ? cm", "atb": ["7"],
         "padoms": "Puse no AB."},
        {"jaut": "MN = 4,5 cm. AB = ? cm", "atb": ["9"],
         "padoms": "AB = 2 · MN."},
        {"jaut": "∠CAB = 50°, MN ∥ AB. ∠CMN = ?°", "atb": ["50"],
         "padoms": "Kāpšļu leņķi pie paralēlām taisnēm."},
        {"jaut": "∠ABC = 65°. ∠CNM = ?°", "atb": ["65"],
         "padoms": "NM ∥ BA."},
    ]),

    Varianti("Patiess vai aplams?", [
        {"jaut": "Viduslīnija ir paralēla vienai no trijstūra malām.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 0, "padoms": "Tai malai, kuru tā nekrusto."},
        {"jaut": "Viduslīnija ir puse no jebkuras malas.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 1, "padoms": "Tikai no trešās, paralēlās malas."},
        {"jaut": "Taisne caur AC viduspunktu, paralēla AB, iet caur BC "
                 "viduspunktu.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 0, "padoms": "Talesa teorēma."},
    ]),

    Pasaule("Tilta kopne",
            Ievadi("", [
                {"jaut": "Kopnes trijstūra pamats 16 m. Horizontālā sija "
                         "savieno slīpo siju viduspunktus. Garums (m)?",
                 "atb": ["8"], "padoms": "Viduslīnija."},
                {"jaut": "Kopnes augstums 6 m. Cik m virs pamata ir sija?",
                 "atb": ["3"], "padoms": "Viduspunkti ir pusē augstuma."},
                {"jaut": "Cik m tērauda vajag trijstūrim 16 m, 10 m, 10 m un "
                         "sijai kopā?", "atb": ["44"],
                 "padoms": "16 + 10 + 10 + 8."},
            ]),
            pavediens="tehnika",
            konteksts="Dzelzceļa tilta kopne ir trijstūri; sijas bieži liek "
                      "pa viduslīnijām.",
            kapec="Inženieris sijas garumu zina bez mērīšanas."),

    Kopsavilkums([
        "Formulēju viduslīnijas īpašību.",
        "Atstāstu pierādījumu ar Talesa teorēmu.",
        "Lietoju īpašību malām un leņķiem.",
    ]),

    Majas([
        "Pieraksti pierādījumu burtnīcā: dots, jāpierāda, soļi ar "
        "pamatojumu.",
        "Trijstūra malas 6, 8 un 10 cm. Aprēķini visas viduslīnijas.",
        "Paskaidro, kāpēc trīs viduslīniju summa ir puse no perimetra.",
    ]),
]
