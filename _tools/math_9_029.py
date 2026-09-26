# -*- coding: utf-8 -*-
"""9. klase, 29. stunda: «Kā sadalīt trapeci?»

Divi augstumi sadala trapeci taisnstūrī un diviem taisnleņķa trijstūriem.
Vienādsānu trapecē abi trijstūri ir vienādi, tāpēc AH = {a − b|2} - šis
nogrieznis būs vajadzīgs katrā turpmākajā aprēķinā.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Paraugs, Pasaule, Sakums, Slidnis, Varianti,
                         geometrija, trapece)

TEMA = "Kā sadalīt trapeci?"

MERKIS = ("Sadalīsim trapeci trijstūros un taisnstūrī un izmantosim to "
          "aprēķinos.")

_T = trapece(12, 6, 4, pedas=True)


def _zim(iekrasot=(), malas=()):
    return geometrija(_T, nogriezni=TRAPECES_MALAS + ["DH", "CK"],
                      taisni=["DHB", "CKA"], iekrasot=list(iekrasot),
                      malas=list(malas))


SATURS = [
    Sakums("Trapece = taisnstūris + 2 trijstūri",
           zimejums=_zim(iekrasot=[("AHD", 1), ("KBC", 1), ("HKCD", 0)],
                         malas=[("DC", "6"), ("AH", "3"), ("KB", "3")]),
           paraksts="Pamati 12 un 6: katrā malā paliek {12 − 6|2} = 3.",
           fakti=["HK = DC - taisnstūra mala.",
                  "Vienādsānu trapecē AH = KB = {a − b|2}.",
                  "Trijstūros var lietot Pitagora teorēmu."]),

    Slidnis("Sadali pa soļiem", [
        {"v": "Trapece", "teksts": "Pamati a = 12, b = 6",
         "zim": geometrija(_T[:4], nogriezni=TRAPECES_MALAS)},
        {"v": "Augstumi", "teksts": "DH ⊥ AB un CK ⊥ AB",
         "zim": _zim()},
        {"v": "Taisnstūris", "teksts": "HKCD - taisnstūris: HK = DC = 6",
         "zim": _zim(iekrasot=[("HKCD", 0)])},
        {"v": "Trijstūri", "teksts": "AH + KB = 12 − 6 = 6; katrs 3",
         "zim": _zim(iekrasot=[("AHD", 1), ("KBC", 1)])},
    ]),

    Doma("Noderīgi nogriežņi",
         "Vienādsānu trapecē AH = {a − b|2} un AK = {a + b|2} = m.",
         soli=[
             "HK = b (taisnstūra pretējās malas).",
             "AH + KB = a − b.",
             "Vienādsānu: △AHD = △BKC, tāpēc AH = KB.",
             "AK = AH + HK = {a − b|2} + b = {a + b|2}.",
         ]),

    Paraugs("Sānu mala",
            uzd="Vienādsānu trapecē pamati 14 cm un 8 cm, augstums 4 cm. "
                "Atrodi sānu malu.",
            soli=[
                ("AH = {14 − 8|2} = 3", "Trijstūra katete."),
                ("AD^2 = 3^2 + 4^2 = 25", "Pitagora teorēma △AHD."),
                ("AD = 5", "Sakne."),
            ],
            atbilde="5 cm"),

    Ievadi("Aprēķini (vienādsānu trapece)", [
        {"jaut": "a = 20, b = 12. AH = ?", "atb": ["4"],
         "padoms": "(20 − 12) : 2."},
        {"jaut": "a = 20, b = 12. AK = ?", "atb": ["16"],
         "padoms": "(20 + 12) : 2."},
        {"jaut": "AH = 5, b = 7. a = ?", "atb": ["17"],
         "padoms": "a = b + 2 · AH."},
        {"jaut": "a = 16, b = 10, augstums 4. Sānu mala?", "atb": ["5"],
         "padoms": "AH = 3; 3, 4, 5."},
        {"jaut": "a = 11, b = 5, sānu mala 5. Augstums?", "atb": ["4"],
         "padoms": "AH = 3; √(25 − 9)."},
        {"jaut": "Taisnleņķa: a = 9, b = 5, augstums 3. Slīpā sānu mala?",
         "atb": ["5"], "padoms": "Viens trijstūris: katete 4."},
    ], pamats=4),

    Varianti("Kurš apgalvojums der?", [
        {"jaut": "Vispārīgā (ne vienādsānu) trapecē...",
         "opcijas": ["AH + KB = a − b, bet AH ≠ KB", "AH = KB vienmēr",
                     "HK = a", "AH = {a|2}"],
         "pareizi": 0, "padoms": "Trijstūri var būt dažādi."},
        {"jaut": "Taisnleņķa trapecei ir...",
         "opcijas": ["viens taisnleņķa trijstūris un taisnstūris",
                     "divi trijstūri", "tikai taisnstūris",
                     "trīs trijstūri"],
         "pareizi": 0, "padoms": "Viena sānu mala jau ir augstums."},
    ]),

    Pasaule("Grāvja šķērsgriezums",
            Ievadi("", [
                {"jaut": "Grāvis augšā 3 m, apakšā 1 m plats (vienādsānu). "
                         "Cik m katra slīpā siena «izvirzās» uz āru?",
                 "atb": ["1"], "padoms": "(3 − 1) : 2."},
                {"jaut": "Grāvja dziļums 0,75 m. Slīpās sienas garums (m)?",
                 "atb": ["1,25"], "padoms": "√(1 + 0,5625)."},
            ]),
            pavediens="daba",
            konteksts="Meliorācijas grāvjiem sienas rok slīpas, lai zeme "
                      "neiebrūk.",
            kapec="Sadalot trapeci, grāvja sienu aprēķina ar Pitagoru."),

    Kopsavilkums([
        "Sadalu trapeci taisnstūrī un trijstūros.",
        "Lietoju AH = {a − b|2} vienādsānu trapecē.",
        "Aprēķinu sānu malu vai augstumu ar Pitagora teorēmu.",
    ]),

    Majas([
        "Vienādsānu trapecē pamati 18 un 8, sānu mala 13. Atrodi augstumu.",
        "Taisnleņķa trapecē pamati 10 un 4, augstums 8. Atrodi slīpo malu.",
        "Pierādi: vienādsānu trapecē AK = m.",
    ]),
]
