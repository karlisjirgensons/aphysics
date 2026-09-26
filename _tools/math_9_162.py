# -*- coding: utf-8 -*-
"""9. klase, 162. stunda: «Kādas sakarības ir regulāram daudzstūrim?»

Regulāram daudzstūrim apvilktās (R) un ievilktās (r) riņķa līnijas centrs
ir viens. Centra leņķis 360° : n; trijstūrī OAM (M - malas viduspunkts)
R - hipotenūza, r - katete, {a|2} - otra katete. Sešstūrim a = R,
kvadrātam a = R√2, vienādmalu trijstūrim R = 2r. Stāsts: uzgriežņu atslēga.
"""

import math

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, geometrija, regulars)

TEMA = "Kādas sakarības ir regulāram daudzstūrim?"

MERKIS = ("Lietosim sakarības starp regulāra daudzstūra malu un riņķa līniju "
          "rādiusiem.")


def _zim(n):
    """n-stūris ar centru O, rādiusu OA, apotēmu OM un abām riņķa līnijām."""
    punkti, malas = regulars(n)
    r = 5 * math.cos(math.pi / n)
    punkti += [("O", 0, 0, 90), ("M", 0, -r, -90)]
    return geometrija(punkti, nogriezni=malas + ["OA", "OM"],
                      taisni=["OMB"], malas=[("OA", "R"), ("OM", "r")],
                      rinki=[("O", 5), ("O", r, 1)])


SATURS = [
    Sakums("Divas riņķa līnijas ar vienu centru",
           zimejums=_zim(6),
           paraksts="R - līdz virsotnei, r - līdz malas viduspunktam.",
           fakti=["Centra leņķis = 360° : n.",
                  "△OAM ir taisnleņķa: R^2 = r^2 + ({a|2})^2.",
                  "Sešstūrim a = R."]),

    Slidnis("Trīs biežākie daudzstūri", [
        {"v": "n = 3", "teksts": "R = 2r, a = R√3", "zim": _zim(3)},
        {"v": "n = 4", "teksts": "a = 2r, a = R√2", "zim": _zim(4)},
        {"v": "n = 6", "teksts": "a = R, r = {a√3|2}", "zim": _zim(6)},
    ]),

    Doma("Viens taisnleņķa trijstūris",
         "Katram regulāram daudzstūrim R, r un {a|2} veido taisnleņķa "
         "trijstūri ar leņķi 180° : n pie centra.",
         soli=[
             "Centra leņķis AOB = 360° : n; OM to dala uz pusēm.",
             "OA = R - hipotenūza, OM = r un AM = {a|2} - katetes.",
             "Sešstūrī △AOB ir vienādmalu, tāpēc a = R.",
             "Kvadrātā diagonāle = 2R, tāpēc a = R√2.",
         ]),

    Paraugs("Sešstūris",
            uzd="Regulāra sešstūra mala 6 cm. Atrodi R un r.",
            soli=[
                ("R = a = 6 cm", "△AOB vienādmalu."),
                ("r^2 = 6^2 − 3^2 = 27", "Pitagors △OAM."),
                ("r = √27 = 3√3 ≈ 5,2 cm", "Sakne."),
            ],
            atbilde="R = 6 cm, r = 3√3 ≈ 5,2 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Sešstūrim R = 7. Perimetrs?", "atb": ["42"],
         "padoms": "a = R."},
        {"jaut": "Kvadrāta mala 10. r = ?", "atb": ["5"],
         "padoms": "r = {a|2}."},
        {"jaut": "Kvadrāta mala 10. R^2 = ?", "atb": ["50"],
         "padoms": "R^2 = 5^2 + 5^2."},
        {"jaut": "Vienādmalu trijstūrim r = 4. R = ?", "atb": ["8"],
         "padoms": "R = 2r."},
        {"jaut": "Regulāra astoņstūra centra leņķis (°)?", "atb": ["45"],
         "padoms": "360 : 8."},
    ]),

    Pasaule("Uzgriežņu atslēga",
            Ievadi("", [
                {"jaut": "Sešstūra uzgriežņa mala 10 mm. Atslēgas izmērs - "
                         "attālums starp pretējām malām (2r), mm? Noapaļo "
                         "līdz veselam.", "atb": ["17"],
                 "padoms": "2r = a√3 ≈ 17,3."},
                {"jaut": "Attālums starp pretējām virsotnēm (mm)?",
                 "atb": ["20"], "padoms": "2R = 2a."},
            ]),
            pavediens="tehnika",
            konteksts="Uzgriežņu atslēgu izmēru nosaka attālums starp "
                      "sešstūra pretējām malām.",
            kapec="Tāpēc M10 skrūvei der 17 mm atslēga - tā ir 2r, nevis "
                  "mala.",
            zimejums=_zim(6)),

    Pasaule("Sija no baļķa",
            Ievadi("", [
                {"jaut": "No apaļa baļķa (d = 40 cm) izzāģē lielāko "
                         "kvadrātsiju. Tās mala (cm)? Noapaļo līdz veselam.",
                 "atb": ["28"], "padoms": "a = R√2 = 20√2."},
            ]),
            pavediens="maja",
            konteksts="Kvadrāts ir ievilkts baļķa griezuma aplī.",
            kapec="Kvadrāta diagonāle ir baļķa diametrs."),

    Kopsavilkums([
        "Zīmēju R, r un {a|2} vienā taisnleņķa trijstūrī.",
        "Zinu sakarības sešstūrim, kvadrātam un trijstūrim.",
        "Aprēķinu malu, ja zināms rādiuss, un otrādi.",
    ]),

    Majas([
        "Ar cirkuli konstruē regulāru sešstūri: mala = rādiuss.",
        "Vienādmalu trijstūra mala 12. Aprēķini R un r.",
        "Izmēri uzgriezni un pārbaudi 2r = a√3.",
    ]),
]
