# -*- coding: utf-8 -*-
"""9. klase, 163. stunda: «Kā uzzīmēt parketu?»

Parkets bez spraugām: pie katras virsotnes leņķu summa ir 360°. No vienāda
regulāra daudzstūra der tikai trijstūris (6 · 60°), kvadrāts (4 · 90°) un
sešstūris (3 · 120°); piecstūris neder, jo 360 : 108 nav vesels. Jaukti
parketi: 135° + 135° + 90°, 60° + 60° + 120° + 120° u. c.
"""

import math

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā uzzīmēt parketu?"

MERKIS = ("Plānosim un veidosim parketu no regulāriem daudzstūriem un "
          "pamatosim izvēli.")


def _ap_virsotni(n, cik, s=2.0):
    """cik regulāri n-stūri ar kopīgu virsotni, katrs nākamais blakus.

    Iet pa malu pretēji pulksteņa rādītājam: n-stūris aizņem leņķi starp
    virzieniem φ un φ + leņķis, tāpēc nākamais sākas tur, kur beidzās
    iepriekšējais. Ja leņķi 360° nepiepilda, paliek redzama sprauga.
    """
    lenkis = 180.0 - 360.0 / n
    punkti, malas, krasas, lenki = [("_V", 0, 0)], [], [], []
    for k in range(cik):
        virz = k * lenkis
        x = y = 0.0
        vardi = ["_V"]
        for i in range(1, n):
            a = math.radians(virz + (i - 1) * 360.0 / n)
            x, y = x + s * math.cos(a), y + s * math.sin(a)
            vardi.append("_%d_%d" % (k, i))
            punkti.append((vardi[-1], x, y))
        malas += [(vardi[i], vardi[(i + 1) % n]) for i in range(n)]
        krasas.append((vardi, k % 2))
        # Uzraksts tikai pirmajam - šauros trijstūros seši skaitļi saplūst.
        lenki.append(((vardi[1], "_V", vardi[-1]),
                      "%d°" % round(lenkis) if k == 0 else ""))
    return geometrija(punkti, nogriezni=malas, iekrasot=krasas,
                      lenki=lenki)


SATURS = [
    Sakums("Kāpēc flīzes ir kvadrāti un sešstūri, bet ne piecstūri?",
           zimejums=_ap_virsotni(6, 3),
           paraksts="Trīs sešstūri pie vienas virsotnes: 3 · 120° = 360°.",
           fakti=["Parketā pie virsotnes leņķu summa ir 360°.",
                  "Der tikai trijstūri, kvadrāti un sešstūri.",
                  "Jauktā parketā var likt dažādus daudzstūrus."]),

    Slidnis("Kuri daudzstūri piepilda plakni?", [
        {"v": "6 × 60°", "teksts": "Trijstūri: 360° - der",
         "zim": _ap_virsotni(3, 6)},
        {"v": "4 × 90°", "teksts": "Kvadrāti: 360° - der",
         "zim": _ap_virsotni(4, 4)},
        {"v": "3 × 108°", "teksts": "Piecstūri: 324° - paliek sprauga",
         "zim": _ap_virsotni(5, 3)},
        {"v": "3 × 120°", "teksts": "Sešstūri: 360° - der",
         "zim": _ap_virsotni(6, 3)},
    ]),

    Doma("Parketa nosacījums",
         "Daudzstūri veido parketu, ja pie katras virsotnes to leņķu summa "
         "ir tieši 360°.",
         soli=[
             "Viena veida n-stūris der, ja 360° dalās ar tā leņķi.",
             "60°, 90°, 120° der; 108°, 135°, 144° neder.",
             "Jauktam parketam meklē leņķus ar summu 360°.",
         ],
         pieze="Piemērs: astoņstūris, astoņstūris, kvadrāts - "
               "135° + 135° + 90° = 360°."),

    Ievadi("Aprēķini", [
        {"jaut": "Cik vienādmalu trijstūru satiekas vienā virsotnē?",
         "atb": ["6"], "padoms": "360 : 60."},
        {"jaut": "Divi regulāri astoņstūri un vēl viens regulārs n-stūris. "
                 "n = ?", "atb": ["4"], "padoms": "360 − 270 = 90°."},
        {"jaut": "Divi sešstūri un divi regulāri n-stūri. n = ?",
         "atb": ["3"], "padoms": "(360 − 240) : 2 = 60°."},
        {"jaut": "Divi regulāri divpadsmitstūri (150°) un viens n-stūris. "
                 "n = ?", "atb": ["3"], "padoms": "360 − 300 = 60°."},
    ]),

    Varianti("Der parketam?", [
        {"jaut": "Tikai regulāri piecstūri",
         "opcijas": ["Der", "Neder"], "jaukt": False, "pareizi": 1,
         "padoms": "360 : 108 nav vesels."},
        {"jaut": "Tikai regulāri astoņstūri",
         "opcijas": ["Der", "Neder"], "jaukt": False, "pareizi": 1,
         "padoms": "360 : 135 nav vesels."},
        {"jaut": "Trijstūris, trijstūris, sešstūris, sešstūris",
         "opcijas": ["Der", "Neder"], "jaukt": False, "pareizi": 0,
         "padoms": "60 + 60 + 120 + 120 = 360."},
    ]),

    Petijums("Uzzīmē savu parketu", [
        "Izvēlies 1-2 veidu regulārus daudzstūrus.",
        "Pārbaudi: leņķu summa pie virsotnes 360°.",
        "Uz rūtiņu vai izometriskā papīra uzzīmē vismaz 10 figūras.",
        "Izkrāso un uzraksti, kāpēc tavs parkets der.",
    ], vajag="papīrs, lineāls, cirkulis, krāsas",
       secinajums="Parkets der, ja katrā virsotnē sanāk tieši 360°."),

    Pasaule("Flīzes vannasistabā",
            Ievadi("", [
                {"jaut": "Grīda 2 m × 1,5 m, kvadrātflīzes 25 × 25 cm. Cik "
                         "flīžu vajag?", "atb": ["48"], "padoms": "8 · 6."},
                {"jaut": "Flīze maksā 1,20 €. Cik maksās visas?",
                 "atb": ["57,60", "57,6"], "padoms": "48 · 1,20."},
            ]),
            pavediens="maja",
            konteksts="Kvadrātflīzes veido vienkāršāko parketu: 4 · 90° pie "
                      "katras virsotnes.",
            kapec="Parketa nosacījums garantē, ka flīzes sakļaujas bez "
                  "spraugām."),

    Kopsavilkums([
        "Zinu parketa nosacījumu: 360° pie virsotnes.",
        "Pamatoju, kuri regulāri daudzstūri der parketam.",
        "Plānoju jauktu parketu.",
    ]),

    Majas([
        "Atrodi vēl vienu jauktu parketu un pamato ar leņķiem.",
        "Nofotografē bruģi vai flīzes un nosaki, kādi daudzstūri tur ir.",
        "Kāpēc bites būvē sešstūrus, nevis kvadrātus? Pameklē.",
    ]),
]
