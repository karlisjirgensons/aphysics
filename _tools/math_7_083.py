# -*- coding: utf-8 -*-
"""7. klase, 83. stunda: «Kā zīmēt pašam?»

Eksāmena uzdevumā zīmējuma bieži nav - ir tikai teksts. Stunda iemāca no
teksta izveidot zīmējumu: atzīmēt doto ar svītriņām un lokiem, un tikai
tad pierādīt. Labs zīmējums jau ir puse pierādījuma.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā zīmēt pašam?"

MERKIS = ("Veidosim zīmējumu pēc teksta un pierādīsim elementu vienādību.")


def _z(n):
    """Zīmējums pēc teksta pa soļiem."""
    p = [("A", 0, 0), ("C", 6, 0), ("B", 3, 4), ("M", 3, 0, -90)]
    nog = ["AC", "AB", "BC"]
    izc, sv = [], []
    if n >= 2:
        izc = ["BM"]
    if n >= 3:
        sv = [("AB", 1), ("BC", 1)]
    if n >= 4:
        sv += [("AM", 2), ("MC", 2)]
    return geometrija(p, nogriezni=nog, izcelti=izc, svitras=sv)


SATURS = [
    Sakums("Teksts → zīmējums → pierādījums",
           zimejums=_z(4),
           paraksts="«Vienādsānu trijstūrī ABC (AB = BC) M ir AC "
                    "viduspunkts.»",
           fakti=["Vispirms uzzīmē figūru.",
                  "Tad atzīmē visu doto ar zīmēm.",
                  "Beigās meklē trijstūrus pierādījumam."]),

    Doma("Zīmē, atzīmē, tad domā",
         "Zīmējums pēc teksta: uzzīmē figūru, nosauc punktus kā tekstā un "
         "atzīmē doto - vienādus nogriežņus ar svītriņām, vienādus leņķus ar "
         "lokiem, taisnos leņķus ar kvadrātiņu.",
         soli=[
             "Izlasi tekstu un uzzīmē pamatfigūru.",
             "Pievieno papildu nogriežņus (mediānas, diagonāles).",
             "Atzīmē doto: svītriņas, loki, taisnā leņķa zīme.",
             "Uzraksti dots un jāpierāda.",
             "Meklē vienādos trijstūrus.",
         ],
         pieze="Nezīmē speciālgadījumu: ja teksts nesaka «vienādmalu», "
               "nezīmē vienādmalu - tas var maldināt."),

    Slidnis("Zīmējums pa soļiem", [
        {"v": "1. solis", "teksts": "Trijstūris ABC.", "zim": _z(1)},
        {"v": "2. solis", "teksts": "Nogrieznis BM.", "zim": _z(2)},
        {"v": "3. solis", "teksts": "AB = BC - viena svītriņa.",
         "zim": _z(3)},
        {"v": "4. solis", "teksts": "AM = MC - divas svītriņas.",
         "zim": _z(4)},
    ]),

    Paraugs("Pierādi pēc teksta",
            uzd="Vienādsānu trijstūrī ABC (AB = BC) M ir AC viduspunkts. "
                "Pierādi, ka ∠ABM = ∠CBM.",
            soli=[
                ("AB = CB", "(dots)"),
                ("AM = CM", "(M - viduspunkts)"),
                ("BM = BM", "(kopīga mala)"),
                ("△ABM = △CBM", "(mmm)"),
                ("∠ABM = ∠CBM", "(atbilstošie leņķi)"),
            ],
            atbilde="BM ir leņķa B bisektrise."),

    Varianti("Pareizs zīmējums", [
        {"jaut": "Tekstā: «Trijstūrī ABC ∠A = ∠C». Ko atzīmē?",
         "opcijas": ["Vienādus lokus pie A un C",
                     "Svītriņas uz AB un BC",
                     "Taisnu leņķi pie B", "Neko"],
         "pareizi": 0, "padoms": "Leņķi - ar lokiem."},
        {"jaut": "Tekstā: «AD ⊥ BC». Ko zīmē?",
         "opcijas": ["Kvadrātiņu pie D", "Svītriņu uz AD",
                     "Loku pie A", "Bultu"],
         "pareizi": 0, "padoms": "Taisnais leņķis."},
        {"jaut": "Tekstā: «trijstūris ABC». Kāds jāzīmē?",
         "opcijas": ["Parasts, bez īpašām vienādībām",
                     "Vienādmalu", "Taisnleņķa", "Vienādsānu"],
         "pareizi": 0, "padoms": "Nezīmē speciālgadījumu."},
    ]),

    Pasaule("Uzdevums no eksāmena",
            Varianti("", [
                {"jaut": "«Taisnstūra ABCD diagonāles krustojas punktā O.» "
                         "Cik trijstūru būs zīmējumā?",
                 "opcijas": ["8", "4", "2", "6"],
                 "pareizi": 0, "padoms": "4 mazi un 4 lieli."},
                {"jaut": "Kurš no tiem ir vienāds ar △AOB?",
                 "opcijas": ["△COD", "△BOC", "△ABC", "△ABD"],
                 "pareizi": 0, "padoms": "Pretējais."},
                {"jaut": "Kāpēc zīmējums eksāmenā dod punktus?",
                 "opcijas": ["Tas parāda sapratni un palīdz pierādīt",
                             "Tas ir skaisti", "Tā nav",
                             "Tikai krāsains"],
                 "pareizi": 0, "padoms": "Zīmējums - puse no risinājuma."},
            ]),
            pavediens="skola",
            konteksts="9. klases eksāmena ģeometrijas uzdevumos zīmējums "
                      "bieži jāveido pašam.",
            kapec="Precīzs zīmējums rāda ceļu uz pierādījumu."),

    Kopsavilkums([
        "Veidoju zīmējumu pēc teksta.",
        "Atzīmēju doto ar svītriņām, lokiem un kvadrātiņiem.",
        "Nezīmēju speciālgadījumu, ja tas nav dots.",
        "Pierādu vienādību pēc sava zīmējuma.",
    ]),

    Majas([
        "Uzzīmē: «Paralelogramā ABCD diagonāles krustojas punktā O.»",
        "Atzīmē visus vienādos elementus.",
        "Pierādi, ka △AOB = △COD.",
    ]),
]
