# -*- coding: utf-8 -*-
"""9. klase, 26. stunda: «Kāda ir sakarība ar pamatiem?»

Pētnieciska stunda: mērījumi vairākās trapecēs, tabula un pieņēmums
m = {a + b|2}. Pierādījums nāk nākamajā stundā - te pieņēmumu pārbauda un
saprot kā vidējo aritmētisko.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Pasaule, Petijums, Sakums, Slidnis, Varianti,
                         geometrija, restis, trapece)

TEMA = "Kāda ir sakarība ar pamatiem?"

MERKIS = ("Formulēsim pieņēmumu par viduslīnijas garumu un pārbaudīsim to "
          "ar mērījumiem.")


def _zim(a, b, nobide=None):
    """Trapece ar pamatiem a, b; uzrakstīts arī viduslīnijas garums."""
    m = (a + b) / 2.0
    teksts = ("%g" % m).replace(".", ",")
    return geometrija(trapece(a, b, 4, nobide=nobide, viduspunkti=True),
                      nogriezni=TRAPECES_MALAS, izcelti=["MN"],
                      malas=[("AB", "%g" % a), ("DC", "%g" % b),
                             ("MN", teksts)])


SATURS = [
    Sakums("Viduslīnija ir kaut kur starp pamatiem",
           zimejums=_zim(10, 4, nobide=2),
           paraksts="Pamati 10 un 4. Viduslīnija 7 - kāpēc tieši 7?",
           fakti=["Viduslīnija ir īsāka par garāko pamatu.",
                  "Un garāka par īsāko pamatu.",
                  "Varbūt tā ir tieši «pa vidu»?"]),

    Slidnis("Mēram trīs trapeces", [
        {"v": "10 un 4", "teksts": "Izmērīts MN = 7", "zim": _zim(10, 4, 2)},
        {"v": "9 un 5", "teksts": "Izmērīts MN = 7", "zim": _zim(9, 5)},
        {"v": "8 un 2", "teksts": "Izmērīts MN = 5", "zim": _zim(8, 2, 5)},
    ], ievads="Pieraksti katrā: a, b un MN. Kā MN iegūt no a un b?"),

    Petijums("Pieņēmums no tabulas", [
        "Aizpildi tabulu ar saviem mērījumiem (mājasdarbs no iepriekšējās "
        "stundas).",
        "Katrai trapecei aprēķini a + b.",
        "Salīdzini a + b ar MN. Kas kopīgs?",
        "Formulē pieņēmumu vienā teikumā.",
    ], vajag="lineāls, trīs uzzīmētas trapeces",
       secinajums="Pieņēmums: MN = {a + b|2} - pamatu vidējais "
                  "aritmētiskais."),

    Doma("Pieņēmums",
         "Trapeces viduslīnija ir pamatu vidējais aritmētiskais: "
         "m = {a + b|2}.",
         soli=[
             "a un b - pamatu garumi, m - viduslīnija.",
             "m vienmēr ir starp b un a.",
             "Pieņēmumu apstiprina mērījumi; pierādīsim nākamajā stundā.",
         ]),

    Ievadi("Pārbaudi pieņēmumu", [
        {"jaut": "a = 12, b = 6. m = ?", "atb": ["9"],
         "padoms": "(12 + 6) : 2."},
        {"jaut": "a = 15, b = 8. m = ?", "atb": ["11,5"],
         "padoms": "23 : 2."},
        {"jaut": "a = 7,4, b = 3,6. m = ?", "atb": ["5,5"],
         "padoms": "11 : 2."},
        {"jaut": "a = 20, b = 20. m = ? (paralelograms!)", "atb": ["20"],
         "padoms": "Formula der arī tad."},
    ]),

    Varianti("Vai mērījums ticams?", [
        {"jaut": "Pamati 10 un 6, izmērīts MN = 8,1.",
         "opcijas": ["Ticams - mērījuma kļūda 0,1", "Pieņēmums aplams",
                     "Mērīja pamatu", "Nevar būt"],
         "pareizi": 0, "padoms": "Aprēķins dod 8."},
        {"jaut": "Pamati 10 un 6, izmērīts MN = 11.",
         "opcijas": ["Kļūda - MN nevar būt garāks par a", "Ticams",
                     "Pieņēmums aplams", "Tā gadās"],
         "pareizi": 0, "padoms": "MN ir starp 6 un 10."},
    ]),

    Pasaule("Kāpņu pakāpieni",
            Ievadi("", [
                {"jaut": "Kāpnes sašaurinās: apakšējais pakāpiens 1,2 m, "
                         "augšējais 0,8 m, vienmērīgi. Vidējais pakāpiens (m)?",
                 "atb": ["1"], "padoms": "(1,2 + 0,8) : 2."},
                {"jaut": "Apakšā 1,5 m, vidū 1,2 m. Augšā (m)?",
                 "atb": ["0,9"], "padoms": "1,2 · 2 − 1,5."},
            ]),
            pavediens="maja",
            konteksts="Vienmērīgi sašaurinātas kāpnes no sāniem ir trapece; "
                      "vidējais pakāpiens ir viduslīnija.",
            kapec="Viduslīnija ir abu pamatu vidējais.",
            zimejums=restis([["apakšā", "vidū", "augšā"],
                             ["1,2 m", None, "0,8 m"]])),

    Kopsavilkums([
        "Formulēju pieņēmumu no mērījumiem.",
        "Aprēķinu viduslīniju m = {a + b|2}.",
        "Izvērtēju, vai mērījums ir ticams.",
    ]),

    Majas([
        "Uzzīmē trapeci ar pamatiem 11 cm un 5 cm un izmēri viduslīniju.",
        "Paskaidro vārdiem, kāpēc m ir starp b un a.",
        "Padomā, kā pieņēmumu pierādīt ar trijstūra viduslīniju.",
    ]),
]
