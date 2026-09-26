# -*- coding: utf-8 -*-
"""9. klase, 27. stunda: «Kā to pierādīt?»

Trapeces viduslīnijas īpašības pierādījums ar diagonāli: tā sadala trapeci
divos trijstūros, un viduslīnija sadalās divās trijstūru viduslīnijās.
Iepriekšējā temata rezultāts kļūst par jauna pierādījuma instrumentu.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija,
                         trapece)

TEMA = "Kā to pierādīt?"

MERKIS = ("Pierādīsim trapeces viduslīnijas īpašību, lietojot trijstūra "
          "viduslīniju.")

# P - diagonāles AC un viduslīnijas MN krustpunkts.
_T = trapece(10, 4, 4, nobide=2, viduspunkti=True) + [("P", 3, 2, -60)]


def _zim(izcelti=(), iekrasot=(), malas=()):
    return geometrija(_T, nogriezni=TRAPECES_MALAS + ["AC"],
                      izcelti=list(izcelti), iekrasot=list(iekrasot),
                      malas=list(malas))


SATURS = [
    Sakums("Viena diagonāle - divi trijstūri",
           zimejums=_zim(izcelti=["MP", "PN"],
                         iekrasot=[("ACD", 1)]),
           paraksts="Diagonāle AC sadala viduslīniju MN divās daļās.",
           fakti=["MP - trijstūra ACD viduslīnija.",
                  "PN - trijstūra ABC viduslīnija.",
                  "Tātad MN = {b|2} + {a|2}."]),

    Slidnis("Pierādījums", [
        {"v": "Dots", "teksts": "ABCD - trapece, AB ∥ DC, M un N - sānu malu "
                                "viduspunkti. Pierādīt: MN ∥ AB, "
                                "MN = {AB + DC|2}.",
         "zim": _zim(izcelti=["MN"])},
        {"v": "1", "teksts": "Novelk diagonāli AC; P = AC ∩ MN.",
         "zim": _zim(izcelti=["MN"])},
        {"v": "2", "teksts": "△ACD: M - AD viduspunkts, MP ∥ DC, tātad P - "
                             "AC viduspunkts un MP = {DC|2}.",
         "zim": _zim(izcelti=["MP"], iekrasot=[("ACD", 1)])},
        {"v": "3", "teksts": "△ABC: P un N - AC un BC viduspunkti, tātad "
                             "PN ∥ AB un PN = {AB|2}.",
         "zim": _zim(izcelti=["PN"], iekrasot=[("ABC", 0)])},
        {"v": "4", "teksts": "MN = MP + PN = {DC|2} + {AB|2} = "
                             "{AB + DC|2}.",
         "zim": _zim(izcelti=["MP", "PN"])},
    ]),

    Doma("Trapeces viduslīnijas īpašība",
         "Trapeces viduslīnija ir paralēla pamatiem un vienāda ar pamatu "
         "summas pusi: m = {a + b|2}.",
         pieze="Pierādījumā izmantojām jau pierādītu teorēmu - trijstūra "
               "viduslīnijas īpašību. Tā matemātika aug no iepriekšējā."),

    Varianti("Pierādījuma soļi", [
        {"jaut": "Kāpēc P ir diagonāles AC viduspunkts?",
         "opcijas": ["Taisne caur M ∥ DC krusto AC viduspunktā (Taless)",
                     "Tā izskatās", "Jo AC = BD", "Jo trapece vienādsānu"],
         "pareizi": 0, "padoms": "Talesa teorēma trijstūrī ACD."},
        {"jaut": "Kuras teorēmas lietojām?",
         "opcijas": ["Trijstūra viduslīnijas īpašību", "Pitagora teorēmu",
                     "Līdzības pazīmi pēc 3 malām", "Sinusu teorēmu"],
         "pareizi": 0, "padoms": "Divas reizes."},
        {"jaut": "MP = {DC|2}, jo MP ir...",
         "opcijas": ["△ACD viduslīnija", "△ABC viduslīnija",
                     "trapeces augstums", "diagonāle"],
         "pareizi": 0, "padoms": "M ∈ AD, P ∈ AC."},
    ]),

    Ievadi("Diagonāle dala viduslīniju", [
        {"jaut": "a = 12, b = 6. MP = ?", "atb": ["3"],
         "padoms": "{b|2}."},
        {"jaut": "a = 12, b = 6. PN = ?", "atb": ["6"],
         "padoms": "{a|2}."},
        {"jaut": "Par cik PN garāks nekā MP, ja a = 14, b = 8?",
         "atb": ["3"], "padoms": "7 − 4 = {a − b|2}."},
        {"jaut": "MP = 2,5, PN = 4. Pamati a un b: a = ?", "atb": ["8"],
         "padoms": "a = 2 · PN."},
    ]),

    Pasaule("Tilta balsts",
            Ievadi("", [
                {"jaut": "Tilta balsta trapece: apakšā 18 m, augšā 10 m. "
                         "Horizontāla sija pa viduslīniju. Garums (m)?",
                 "atb": ["14"], "padoms": "(18 + 10) : 2."},
                {"jaut": "Slīpa stiegra (diagonāle) sadala siju. Īsākā daļa "
                         "(m)?", "atb": ["5"], "padoms": "10 : 2."},
            ]),
            pavediens="tehnika",
            konteksts="Tilta balstos sijas un stiegras veido tieši šo "
                      "zīmējumu.",
            kapec="Pierādījuma soļi ir arī aprēķina soļi."),

    Kopsavilkums([
        "Atstāstu pierādījumu ar diagonāli.",
        "Lietoju trijstūra viduslīnijas īpašību jaunā situācijā.",
        "Zinu, kā diagonāle dala viduslīniju.",
    ]),

    Majas([
        "Pieraksti pierādījumu ar diagonāli BD (nevis AC).",
        "Pierādi: diagonāļu viduspunktu attālums ir {a − b|2}.",
        "Pārbaudi to uz uzzīmētas trapeces.",
    ]),
]
