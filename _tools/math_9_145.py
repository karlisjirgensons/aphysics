# -*- coding: utf-8 -*-
"""9. klase, 145. stunda: «Kur ir centrs taisnleņķa trijstūrim?»

Apvilktās riņķa līnijas centrs: šaurleņķa trijstūrim - iekšā, taisnleņķa
- hipotenūzas viduspunktā, platleņķa - ārpusē. Tāpēc taisnleņķa trijstūrī
R = {c|2} - mediāna pret hipotenūzu ir puse no tās.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, uz_rinka)

TEMA = "Kur ir centrs taisnleņķa trijstūrim?"

MERKIS = ("Pētīsim un pamatosim apvilktās riņķa līnijas centra vietu dažāda "
          "veida trijstūriem.")


def _trijsturis(lenki):
    """Trijstūris ar virsotnēm uz riņķa līnijas dotajos leņķos."""
    punkti = [uz_rinka(v, g) for v, g in zip("ABC", lenki)]
    return geometrija(punkti + [("O", 0, 0, -60)],
                      nogriezni=["AB", "BC", "CA"], izcelti=["OA"],
                      rinki=[("O", 5)])


SATURS = [
    Sakums("Hipotenūza ir diametrs",
           zimejums=_trijsturis((180, 0, 60)),
           paraksts="Taisnleņķa trijstūrī O ir hipotenūzas AB viduspunktā.",
           fakti=["R = {c|2} - puse no hipotenūzas.",
                  "Mediāna pret hipotenūzu = R = {c|2}.",
                  "Visas trīs virsotnes vienādi tālu no O."]),

    Slidnis("Kur ir O?", [
        {"v": "Šaurleņķa", "teksts": "O - trijstūra iekšpusē",
         "zim": _trijsturis((200, 340, 90))},
        {"v": "Taisnleņķa", "teksts": "O - uz hipotenūzas, tās viduspunktā",
         "zim": _trijsturis((180, 0, 60))},
        {"v": "Platleņķa", "teksts": "O - ārpus trijstūra",
         "zim": _trijsturis((160, 20, 70))},
    ]),

    Doma("Centra vieta",
         "Taisnleņķa trijstūrim apvilktās riņķa līnijas centrs ir "
         "hipotenūzas viduspunkts, un R = {c|2}.",
         soli=[
             "Šaurleņķa - centrs iekšā.",
             "Taisnleņķa - hipotenūzas viduspunktā.",
             "Platleņķa - ārpusē, pretī platajam leņķim.",
         ]),

    Ievadi("Aprēķini R", [
        {"jaut": "Taisnleņķa trijstūra hipotenūza 10 cm. R = ? cm",
         "atb": ["5"], "padoms": "{c|2}."},
        {"jaut": "Katetes 6 un 8. R = ?", "atb": ["5"],
         "padoms": "c = 10."},
        {"jaut": "Katetes 5 un 12. R = ?", "atb": ["6,5"],
         "padoms": "c = 13."},
        {"jaut": "R = 8,5. Hipotenūza?", "atb": ["17"], "padoms": "2R."},
    ]),

    Varianti("Kāds trijstūris?", [
        {"jaut": "Centrs O ir uz malas AC.",
         "opcijas": ["Taisnleņķa, ∠B = 90°", "Šaurleņķa", "Platleņķa",
                     "Vienādmalu"],
         "pareizi": 0, "padoms": "AC - hipotenūza."},
        {"jaut": "Centrs O ir ārpus trijstūra.",
         "opcijas": ["Platleņķa", "Šaurleņķa", "Taisnleņķa",
                     "Vienādsānu noteikti"],
         "pareizi": 0, "padoms": "Viens leņķis > 90°."},
    ]),

    Pasaule("Futbola vārti un stūris",
            Ievadi("", [
                {"jaut": "Laukuma stūris - taisns leņķis; punkti 30 m un 40 m "
                         "no stūra uz malām. Tiesnesis grib stāvēt vienādi tālu "
                         "no stūra un abiem punktiem. Cik m no katra?",
                 "atb": ["25"], "padoms": "c = 50, R = 25."},
            ]),
            pavediens="sports",
            konteksts="Taisnleņķa trijstūrim punkts vienādā attālumā no "
                      "virsotnēm ir hipotenūzas vidū.",
            kapec="Nav jākonstruē - pietiek ar viduspunktu."),

    Kopsavilkums([
        "Nosaku centra vietu pēc trijstūra veida.",
        "Lietoju R = {c|2} taisnleņķa trijstūrī.",
        "Zinu, ka mediāna pret hipotenūzu ir {c|2}.",
    ]),

    Majas([
        "Uzzīmē trīs trijstūrus un konstruē apvilktās riņķa līnijas.",
        "Katetes 9 un 12: atrodi R.",
        "Pierādi: mediāna pret hipotenūzu ir puse hipotenūzas.",
    ]),
]
