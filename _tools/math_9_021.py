# -*- coding: utf-8 -*-
"""9. klase, 21. stunda: «Kādi ir trapeču veidi?»

Vienādsānu trapece (sānu malas vienādas, simetriska) un taisnleņķa trapece
(viena sānu mala perpendikulāra pamatiem). Slīdnis pārvērš vienu trapeci
otrā, bīdot augšējo pamatu.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija,
                         trapece)

TEMA = "Kādi ir trapeču veidi?"

MERKIS = ("Nošķirsim vienādsānu un taisnleņķa trapeci un raksturosim to "
          "īpašības.")

_VIENADSANU = geometrija(trapece(10, 4, 4), nogriezni=TRAPECES_MALAS,
                         svitras=[("AD", 1), ("BC", 1)],
                         lenki=[("BAD", "", 1), ("ABC", "", 1)])
_TAISNLENKA = geometrija(trapece(10, 5, 4, nobide=0),
                         nogriezni=TRAPECES_MALAS, taisni=["BAD", "ADC"])

SATURS = [
    Sakums("Kāpēc galda kājas bieži ir trapeces?",
           zimejums=_VIENADSANU,
           paraksts="Vienādsānu trapece - simetriska kā tauriņa spārni.",
           fakti=["Vienādsānu trapecei sānu malas vienādas.",
                  "Taisnleņķa trapecei viena sānu mala ⊥ pamatiem.",
                  "Citām trapecēm īpaša nosaukuma nav."]),

    Slidnis("Bīdi augšējo pamatu", [
        {"v": "Vidū", "teksts": "Vienādsānu trapece: AD = BC, simetrijas ass",
         "zim": _VIENADSANU},
        {"v": "Pa kreisi", "teksts": "Taisnleņķa trapece: AD ⊥ AB",
         "zim": _TAISNLENKA},
        {"v": "Pa labi", "teksts": "Vispārīga trapece: malas nevienādas",
         "zim": geometrija(trapece(10, 4, 4, nobide=4.5),
                           nogriezni=TRAPECES_MALAS)},
    ]),

    Doma("Vienādsānu trapeces īpašības",
         "Vienādsānu trapecei pamata leņķi ir vienādi un diagonāles ir "
         "vienādas.",
         soli=[
             "∠A = ∠B un ∠C = ∠D.",
             "AC = BD.",
             "Simetrijas ass iet caur abu pamatu viduspunktiem.",
             "Taisnleņķa trapecei divi leņķi ir 90°.",
         ]),

    Varianti("Kāda trapece?", [
        {"jaut": "Sānu malas 5 cm un 5 cm.",
         "opcijas": ["Vienādsānu", "Taisnleņķa", "Paralelograms",
                     "Vispārīga"],
         "pareizi": 0, "padoms": "Vienādas sānu malas."},
        {"jaut": "Viens leņķis ir 90°.",
         "opcijas": ["Taisnleņķa", "Vienādsānu", "Kvadrāts", "Rombs"],
         "pareizi": 0, "padoms": "Tad arī blakus leņķis ir 90°."},
        {"jaut": "Vai trapece var būt gan vienādsānu, gan taisnleņķa?",
         "opcijas": ["Nē - tad tas būtu taisnstūris", "Jā, vienmēr",
                     "Jā, ja pamati vienādi", "Tikai kvadrāts"],
         "pareizi": 0, "padoms": "Visi 4 leņķi būtu 90°."},
        {"jaut": "Vienādsānu trapecē ∠A = 70°. ∠B = ?",
         "opcijas": ["70°", "110°", "20°", "90°"],
         "pareizi": 0, "padoms": "Pamata leņķi vienādi."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Vienādsānu trapece: pamati 11 un 5, sānu mala 4. "
                 "Perimetrs?", "atb": ["24"], "padoms": "11 + 5 + 4 + 4."},
        {"jaut": "Vienādsānu trapece: diagonāle AC = 9 cm. BD = ? cm",
         "atb": ["9"], "padoms": "Diagonāles vienādas."},
        {"jaut": "Taisnleņķa trapece: ∠A = 90°. ∠D = ?°", "atb": ["90"],
         "padoms": "∠A + ∠D = 180°."},
        {"jaut": "Vienādsānu trapece: perimetrs 34, pamati 12 un 8. Sānu "
                 "mala?", "atb": ["7"], "padoms": "(34 − 20) : 2."},
    ]),

    Pasaule("Popkorna trauks",
            Ievadi("", [
                {"jaut": "Trauka sāna ir vienādsānu trapece: apakšā 10 cm, "
                         "augšā 16 cm, sānu malas 20 cm. Cik cm apmales "
                         "vienai sānai (perimetrs)?", "atb": ["66"],
                 "padoms": "10 + 16 + 20 + 20."},
                {"jaut": "Traukam ir 4 šādas sānas. Cik cm līmlentes "
                         "vajag tikai augšējām malām?", "atb": ["64"],
                 "padoms": "4 · 16."},
            ]),
            pavediens="virtuve",
            konteksts="Kino popkorna trauka sānas ir vienādsānu trapeces - "
                      "tās paplašinās uz augšu.",
            kapec="Vienādsānu trapecei pietiek zināt vienu sānu malu."),

    Kopsavilkums([
        "Atšķiru vienādsānu un taisnleņķa trapeci.",
        "Zinu vienādsānu trapeces leņķu un diagonāļu īpašību.",
        "Aprēķinu perimetru.",
    ]),

    Majas([
        "Uzzīmē vienādsānu un taisnleņķa trapeci un atzīmē īpašības.",
        "Izmēri vienādsānu trapeces diagonāles - vai tās vienādas?",
        "Kurām trapecēm ir simetrijas ass?",
    ]),
]
