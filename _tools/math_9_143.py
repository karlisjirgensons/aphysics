# -*- coding: utf-8 -*-
"""9. klase, 143. stunda: «Kur atrodas punkts vienādā attālumā no trim punktiem?»

Punkti vienādā attālumā no A un B ir uz nogriežņa AB vidusperpendikula.
Trīs punktiem - divu vidusperpendikulu krustpunkts; tas ir centrs riņķa
līnijai caur visiem trim. Stāsts: kur būvēt glābšanas depo trim ciemiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, uz_rinka)

TEMA = "Kur atrodas punkts vienādā attālumā no trim punktiem?"

MERKIS = ("Noteiksim punkta ģeometrisko vietu un saistīsim to ar "
          "vidusperpendikuliem.")

_A, _B, _C = uz_rinka("A", 210), uz_rinka("B", 330), uz_rinka("C", 100)


def _zim(rinkis=True, perp=2):
    """Trīs ciemi, vidusperpendikuli un (pēc izvēles) riņķa līnija."""
    punkti = [_A, _B, _C, ("O", 0, 0, -60),
              ("_M1", 0, -2.5), ("_M1b", 0, 4),
              ("_M2", (_B[1] + _C[1]) / 2 * 1.9, (_B[2] + _C[2]) / 2 * 1.9),
              ("_M2b", -(_B[1] + _C[1]) / 2 * 0.5,
               -(_B[2] + _C[2]) / 2 * 0.5)]
    nogr = [("A", "B"), ("B", "C"), ("C", "A")]
    izc = [("_M1", "_M1b")] + ([("_M2", "_M2b")] if perp > 1 else [])
    return geometrija(punkti, nogriezni=nogr, izcelti=izc,
                      rinki=[("O", 5)] if rinkis else [])


SATURS = [
    Sakums("Kur būvēt glābšanas depo trim ciemiem?",
           zimejums=_zim(),
           paraksts="Punkts O ir vienādi tālu no A, B un C.",
           fakti=["Vienādi tālu no A un B - uz AB vidusperpendikula.",
                  "Divu vidusperpendikulu krustpunkts - vienādi tālu no visiem.",
                  "Tas ir riņķa līnijas caur A, B, C centrs."]),

    Doma("Vidusperpendikuls",
         "Nogriežņa vidusperpendikuls ir visu to punktu kopa, kas atrodas "
         "vienādā attālumā no nogriežņa galapunktiem.",
         soli=[
             "Vidusperpendikuls iet caur nogriežņa viduspunktu.",
             "Tas ir perpendikulārs nogrieznim.",
             "Katrs tā punkts ir vienādi tālu no abiem galiem.",
             "Trīs punktiem pietiek ar diviem vidusperpendikuliem.",
         ]),

    Slidnis("Meklējam punktu O", [
        {"v": "AB", "teksts": "Vienādi tālu no A un B - vidusperpendikuls",
         "zim": _zim(rinkis=False, perp=1)},
        {"v": "BC", "teksts": "Vienādi tālu no B un C - otrs vidusperpendikuls",
         "zim": _zim(rinkis=False, perp=2)},
        {"v": "O", "teksts": "Krustpunkts: OA = OB = OC - riņķa līnijas centrs",
         "zim": _zim()},
    ]),

    Varianti("Ģeometriskā vieta", [
        {"jaut": "Punkti vienādā attālumā no A un B atrodas...",
         "opcijas": ["uz AB vidusperpendikula", "uz AB", "uz riņķa ar "
                     "centru A", "uz bisektrises"],
         "pareizi": 0, "padoms": "Definīcija."},
        {"jaut": "Vai trešais vidusperpendikuls iet caur O?",
         "opcijas": ["Jā, vienmēr", "Nē", "Tikai vienādmalu",
                     "Tikai taisnleņķa"],
         "pareizi": 0, "padoms": "OA = OC."},
        {"jaut": "Punkti 3 cm attālumā no punkta O veido...",
         "opcijas": ["riņķa līniju", "taisni", "kvadrātu", "punktu"],
         "pareizi": 0, "padoms": "Visi vienādi tālu no centra."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "OA = 7 km, O - uz AB vidusperpendikula. OB = ? km",
         "atb": ["7"], "padoms": "Vienādi."},
        {"jaut": "AB = 10, M - viduspunkts, OM = 12. OA = ?", "atb": ["13"],
         "padoms": "√(25 + 144)."},
        {"jaut": "Riņķa līnija caur A, B, C, OA = 6. Diametrs?", "atb": ["12"],
         "padoms": "2R."},
    ]),

    Pasaule("Mobilā tīkla tornis",
            Ievadi("", [
                {"jaut": "Tornis jānovieto vienādā attālumā no trim ciemiem; "
                         "tas atrasts 8 km no katra. Cik km rādiusā tornim "
                         "jāsniedz signāls?", "atb": ["8"],
                 "padoms": "R = OA."},
                {"jaut": "Pārklājuma laukums ≈ ? km² (π ≈ 3,14, līdz veseliem)",
                 "atb": ["201"], "padoms": "3,14 · 64."},
            ]),
            pavediens="tehnika",
            konteksts="Plānotāji meklē vietu, kas vienādi tuvu visām "
                      "apdzīvotajām vietām.",
            kapec="Vidusperpendikulu krustpunkts ir tieši tāds punkts."),

    Kopsavilkums([
        "Zinu vidusperpendikula īpašību.",
        "Atrodu punktu vienādā attālumā no trim punktiem.",
        "Saistu to ar riņķa līniju caur trim punktiem.",
    ]),

    Majas([
        "Kartē atzīmē 3 vietas un atrodi punktu vienādā attālumā no tām.",
        "Uzzīmē nogriezni un tā vidusperpendikulu ar cirkuli.",
        "Pārbaudi ar lineālu: vai O ir vienādi tālu no visiem trim?",
    ]),
]
