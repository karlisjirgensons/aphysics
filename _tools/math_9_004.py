# -*- coding: utf-8 -*-
"""9. klase, 4. stunda: «Kas ir trijstūra viduslīnija?»

Viduslīnija savieno divu malu viduspunktus. Katram trijstūrim tās ir trīs,
un tās sadala trijstūri četros vienādos trijstūros - to redz slīdnī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija)

TEMA = "Kas ir trijstūra viduslīnija?"

MERKIS = "Definēsim trijstūra viduslīniju un iemācīsimies to uzzīmēt."

_A, _B, _C = (0, 0), (10, 0), (3, 7)
_M = ((_A[0] + _C[0]) / 2.0, (_A[1] + _C[1]) / 2.0)      # AC viduspunkts
_N = ((_B[0] + _C[0]) / 2.0, (_B[1] + _C[1]) / 2.0)      # BC viduspunkts
_K = ((_A[0] + _B[0]) / 2.0, (_A[1] + _B[1]) / 2.0)      # AB viduspunkts


def _trijsturis(linijas, svitras=True, iekrasot=()):
    punkti = [("A",) + _A, ("B",) + _B, ("C",) + _C, ("M",) + _M,
              ("N",) + _N, ("K",) + _K]
    sv = ([("AM", 1), ("MC", 1), ("CN", 2), ("NB", 2), ("AK", 3),
           ("KB", 3)] if svitras else [])
    return geometrija(punkti, nogriezni=["AB", "BC", "CA"],
                      izcelti=linijas, svitras=sv, iekrasot=iekrasot)


SATURS = [
    Sakums("Kur jumtā ir viduslīnija?",
           zimejums=_trijsturis(["MN"], svitras=True),
           paraksts="Šķērssija MN savieno jumta slīpo malu viduspunktus.",
           fakti=["Viduslīnija savieno divu malu viduspunktus.",
                  "Trijstūrim ir trīs viduslīnijas.",
                  "Viduslīnija nav mediāna - mediāna iet uz virsotni."]),

    Doma("Definīcija",
         "Trijstūra viduslīnija ir nogrieznis, kas savieno divu malu "
         "viduspunktus.",
         soli=[
             "Atrodi divu malu viduspunktus (izmēri vai konstruē).",
             "Atzīmē tos ar vienādām svītriņām.",
             "Savieno viduspunktus - tā ir viduslīnija.",
             "Viduslīnija MN «pieder» trešajai malai AB - tā ir pretī tai.",
         ]),

    Slidnis("Trīs viduslīnijas", [
        {"v": "MN", "teksts": "Viduslīnija pretī malai AB",
         "zim": _trijsturis(["MN"])},
        {"v": "NK", "teksts": "Viduslīnija pretī malai AC",
         "zim": _trijsturis(["MN", "NK"])},
        {"v": "KM", "teksts": "Viduslīnija pretī malai BC",
         "zim": _trijsturis(["MN", "NK", "KM"])},
        {"v": "4 daļas", "teksts": "Viduslīnijas sadala trijstūri 4 vienādos "
                                   "trijstūros",
         "zim": _trijsturis(["MN", "NK", "KM"], svitras=False,
                            iekrasot=[("KNM", 1)])},
    ]),

    Varianti("Atpazīsti viduslīniju", [
        {"jaut": "M - AC viduspunkts, N - BC viduspunkts. Kas ir MN?",
         "opcijas": ["Viduslīnija", "Mediāna", "Augstums", "Bisektrise"],
         "pareizi": 0, "padoms": "Savieno divu malu viduspunktus."},
        {"jaut": "M - AC viduspunkts. Kas ir BM?",
         "opcijas": ["Mediāna", "Viduslīnija", "Augstums", "Mala"],
         "pareizi": 0, "padoms": "Iet no virsotnes uz viduspunktu."},
        {"jaut": "Pretī kurai malai ir viduslīnija KN (K ∈ AB, N ∈ BC)?",
         "opcijas": ["AC", "AB", "BC", "Nevienai"],
         "pareizi": 0, "padoms": "Mala, kuru KN nepieskaras."},
        {"jaut": "Cik viduslīniju ir trijstūrim?",
         "opcijas": ["3", "1", "2", "6"],
         "pareizi": 0, "padoms": "Katram malu pārim viena."},
    ]),

    Ievadi("Viduspunkti", [
        {"jaut": "AC = 12 cm, M - AC viduspunkts. AM = ? cm", "atb": ["6"],
         "padoms": "Puse no AC."},
        {"jaut": "CN = 4,5 cm, N - BC viduspunkts. BC = ? cm", "atb": ["9"],
         "padoms": "Divreiz CN."},
        {"jaut": "Uz skaitļu ass A = 2, B = 10. Viduspunkts = ?",
         "atb": ["6"], "padoms": "(2 + 10) : 2."},
        {"jaut": "A(0; 0), C(4; 6). AC viduspunkta y koordināta = ?",
         "atb": ["3"], "padoms": "(0 + 6) : 2."},
    ]),

    Pasaule("A veida kāpnes",
            Ievadi("", [
                {"jaut": "Kāpņu kājas ir 2 m garas. Drošības virvi sien kāju "
                         "viduspunktos. Cik m no augšas tā ir piesieta?",
                 "atb": ["1"], "padoms": "Puse no 2 m."},
                {"jaut": "Starp kājām pie grīdas ir 1,2 m. Virve ir "
                         "viduslīnija. Cik m gara ir virve?",
                 "atb": ["0,6"], "padoms": "Nākamajā stundā pierādīsim: puse."},
            ]),
            pavediens="maja",
            konteksts="Kāpņu kājas un grīda veido trijstūri; virve starp kāju "
                      "viduspunktiem ir tā viduslīnija.",
            kapec="Viduslīnija vienmēr ir puse no pretējās malas."),

    Kopsavilkums([
        "Definēju trijstūra viduslīniju.",
        "Atšķiru viduslīniju no mediānas.",
        "Uzzīmēju visas trīs viduslīnijas.",
    ]),

    Majas([
        "Uzzīmē trijstūri un visas trīs viduslīnijas.",
        "Izmēri viduslīniju un pretējo malu. Ko pamani?",
        "Pārbaudi, vai 4 mazie trijstūri ir vienādi (izgriez un uzliec).",
    ]),
]
