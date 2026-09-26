# -*- coding: utf-8 -*-
"""9. klase, 24. stunda: «Kā pierādīt trapeces īpašību?»

Divi īsi pierādījumi ar trijstūru vienādību: vienādsānu trapecei pamata
leņķi ir vienādi (augstumi nogriež divus vienādus taisnleņķa trijstūrus) un
diagonāles ir vienādas (trijstūri ABD un BAC).
"""

from math_saturs import (TRAPECES_MALAS, Doma, Kopsavilkums, Majas, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija, trapece)

TEMA = "Kā pierādīt trapeces īpašību?"

MERKIS = ("Pierādīsim vienādsānu trapeces īpašības un pazīmi.")

_T = trapece(10, 4, 4, pedas=True)


def _zim(izcelti=(), iekrasot=(), svitras=(), taisni=(), pedas=True,
         lenki=()):
    return geometrija(_T if pedas else _T[:4], nogriezni=TRAPECES_MALAS,
                      izcelti=list(izcelti), iekrasot=list(iekrasot),
                      svitras=list(svitras), taisni=list(taisni),
                      lenki=list(lenki))


SATURS = [
    Sakums("Kāpēc galdnieks mēra diagonāles?",
           zimejums=_zim(izcelti=["AC", "BD"], pedas=False,
                         svitras=[("AD", 1), ("BC", 1)]),
           paraksts="Vienādas diagonāles - trapece ir simetriska.",
           fakti=["Īpašība: vienādsānu trapecei AC = BD.",
                  "Pazīme: ja AC = BD, trapece ir vienādsānu.",
                  "Pierādījumam pietiek ar trijstūru vienādību."]),

    Slidnis("1. pierādījums: ∠A = ∠B", [
        {"v": "Dots", "teksts": "ABCD - trapece, AB ∥ DC, AD = BC.",
         "zim": _zim(pedas=False, svitras=[("AD", 1), ("BC", 1)])},
        {"v": "1", "teksts": "Novelk augstumus DH un CK: DH = CK (attālums "
                             "starp paralēlām taisnēm).",
         "zim": _zim(izcelti=["DH", "CK"], taisni=["DHB", "CKA"])},
        {"v": "2", "teksts": "△AHD = △BKC: hipotenūzas AD = BC, katetes "
                             "DH = CK.",
         "zim": _zim(izcelti=["DH", "CK"], iekrasot=[("AHD", 1),
                                                     ("BKC", 1)])},
        {"v": "3", "teksts": "Vienādos trijstūros pretī vienādām malām - "
                             "vienādi leņķi: ∠A = ∠B.",
         "zim": _zim(pedas=False, lenki=[("BAD", "", 1), ("ABC", "", 1)])},
    ]),

    Slidnis("2. pierādījums: AC = BD", [
        {"v": "1", "teksts": "Aplūko △ABD un △BAC.",
         "zim": _zim(izcelti=["AC", "BD"], pedas=False)},
        {"v": "2", "teksts": "AB - kopīga, AD = BC (dots), ∠A = ∠B "
                             "(1. pierādījums).",
         "zim": _zim(izcelti=["AC", "BD"], pedas=False,
                     lenki=[("BAD", "", 1), ("ABC", "", 1)])},
        {"v": "3", "teksts": "△ABD = △BAC pēc pazīmes «mala, leņķis, "
                             "mala». Tātad BD = AC.",
         "zim": _zim(izcelti=["AC", "BD"], pedas=False)},
    ]),

    Doma("Īpašība un pazīme",
         "Trapece ir vienādsānu ⇔ tās pamata leņķi vienādi ⇔ tās diagonāles "
         "vienādas.",
         soli=[
             "Īpašība: no «vienādsānu» izriet vienādi leņķi un diagonāles.",
             "Pazīme: no vienādām diagonālēm izriet «vienādsānu».",
             "Pierādījumā katram vienādības solim - iemesls.",
         ]),

    Varianti("Aizpildi iemeslu", [
        {"jaut": "DH = CK, jo...",
         "opcijas": ["abi ir attālums starp paralēlajiem pamatiem",
                     "trapece ir vienādsānu", "tie ir krustleņķi",
                     "dots"],
         "pareizi": 0, "padoms": "Augstumi starp paralēlām taisnēm."},
        {"jaut": "△AHD = △BKC pēc...",
         "opcijas": ["hipotenūzas un katetes", "trim leņķiem",
                     "diviem leņķiem", "vienas malas"],
         "pareizi": 0, "padoms": "Taisnleņķa trijstūru pazīme."},
        {"jaut": "Trijstūros ABD un BAC kopīgā mala ir...",
         "opcijas": ["AB", "AC", "BD", "DC"],
         "pareizi": 0, "padoms": "Pieder abiem."},
        {"jaut": "Ko nozīmē zīme ⇔?",
         "opcijas": ["Izriet abos virzienos", "Tikai «no kreisās uz labo»",
                     "Nav vienāds", "Līdzīgs"],
         "pareizi": 0, "padoms": "Īpašība un pazīme kopā."},
    ]),

    Pasaule("Rāmja pārbaude",
            Varianti("", [
                {"jaut": "Galdnieks salicis trapeces rāmi. Diagonāles 82 cm "
                         "un 84 cm. Ko tas nozīmē?",
                 "opcijas": ["Rāmis nav vienādsānu - sāni atšķiras",
                             "Viss kārtībā", "Tas ir taisnstūris",
                             "Pamati nav paralēli noteikti"],
                 "pareizi": 0, "padoms": "Pazīme: diagonālēm jābūt vienādām."},
                {"jaut": "Pēc labošanas abas diagonāles 83 cm, pamati ∥. "
                         "Secinājums?",
                 "opcijas": ["Rāmis ir vienādsānu trapece", "Nekas",
                             "Rāmis ir kvadrāts", "Jāmēra leņķi"],
                 "pareizi": 0, "padoms": "Pazīme."},
            ]),
            pavediens="maja",
            konteksts="Diagonāles izmērīt ar mērlenti ir vieglāk nekā leņķus "
                      "ar transportieri.",
            kapec="Pazīme ļauj pārbaudīt formu ar vienu mērījumu."),

    Kopsavilkums([
        "Pierādu, ka vienādsānu trapecei pamata leņķi vienādi.",
        "Pierādu, ka tās diagonāles vienādas.",
        "Atšķiru īpašību no pazīmes.",
    ]),

    Majas([
        "Pieraksti abus pierādījumus burtnīcā ar iemesliem.",
        "Pierādi pazīmi: ja trapecei ∠A = ∠B, tā ir vienādsānu.",
        "Pārbaudi ar mērlenti kādu trapeces formas priekšmetu.",
    ]),
]
