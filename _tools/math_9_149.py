# -*- coding: utf-8 -*-
"""9. klase, 149. stunda: «Kas ir ievilktais leņķis?»

Ievilktā leņķa virsotne ir uz riņķa līnijas, un tas ir PUSE no centra
leņķa, kas balstās uz tā paša loka. Stadionā no jebkuras vietas uz
tribīnes vārti «redzami» vienā un tajā pašā leņķī.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, uz_rinka)

TEMA = "Kas ir ievilktais leņķis?"

MERKIS = ("Definēsim ievilkto leņķi un formulēsim tā sakarību ar centra "
          "leņķi.")


def _zim(gc, ar_centru=True):
    """Loks AB (A pie 200°, B pie 340°) un ievilktais leņķis ar virsotni C."""
    punkti = [("O", 0, 0, 0), uz_rinka("A", 200), uz_rinka("B", 340),
              uz_rinka("C", gc)]
    nogr = ["CA", "CB"] + (["OA", "OB"] if ar_centru else [])
    lenki = [("ACB", "α")] + ([("AOB", "2α")] if ar_centru else [])
    return geometrija(punkti, nogriezni=nogr, lenki=lenki, rinki=[("O", 5)])


SATURS = [
    Sakums("Ievilktais leņķis - puse no centra leņķa",
           zimejums=_zim(90),
           paraksts="∠ACB balstās uz loka AB, tāpat kā ∠AOB.",
           fakti=["Ievilktā leņķa virsotne ir uz riņķa līnijas.",
                  "Malas ir hordas.",
                  "Ievilktais leņķis = {1|2} centra leņķa."]),

    Doma("Ievilktais leņķis",
         "Ievilktais leņķis ir vienāds ar pusi no centra leņķa, kas balstās "
         "uz tā paša loka.",
         soli=[
             "Atrodi loku, uz kura leņķis balstās (tas ir «pretī»).",
             "Centra leņķis = loka grādu mērs.",
             "Ievilktais = puse.",
             "Loks 140° ⇒ ievilktais 70°.",
         ]),

    Slidnis("C pārvietojas pa lielo loku", [
        {"v": "C pie 90°", "teksts": "∠ACB = 70°, ∠AOB = 140°",
         "zim": _zim(90)},
        {"v": "C pie 40°", "teksts": "∠ACB joprojām 70°",
         "zim": _zim(40, ar_centru=False)},
        {"v": "C pie 150°", "teksts": "∠ACB joprojām 70°",
         "zim": _zim(150, ar_centru=False)},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Centra leņķis 110°. Ievilktais uz tā paša loka (°)?",
         "atb": ["55"], "padoms": "Puse."},
        {"jaut": "Ievilktais leņķis 38°. Centra leņķis (°)?", "atb": ["76"],
         "padoms": "Divreiz."},
        {"jaut": "Loks 200°. Ievilktais leņķis uz tā (°)?", "atb": ["100"],
         "padoms": "Puse no loka."},
        {"jaut": "Ievilktais leņķis uz diametra (°)?", "atb": ["90"],
         "padoms": "Puse no 180°."},
    ]),

    Varianti("Ievilktais vai centra?", [
        {"jaut": "Virsotne centrā, malas - rādiusi.",
         "opcijas": ["Centra leņķis", "Ievilktais leņķis", "Nav nosaukuma",
                     "Pieskares leņķis"],
         "pareizi": 0, "padoms": "Virsotne O."},
        {"jaut": "Virsotne uz riņķa līnijas, malas - hordas.",
         "opcijas": ["Ievilktais leņķis", "Centra leņķis", "Taisns leņķis",
                     "Blakusleņķis"],
         "pareizi": 0, "padoms": "Definīcija."},
    ]),

    Pasaule("Futbola sitiens no soda laukuma malas",
            Ievadi("", [
                {"jaut": "Vārti redzami no centra punkta O aiz tiem 50° leņķī. "
                         "Cik grādu leņķī tos redz spēlētājs uz tās pašas "
                         "riņķa līnijas?", "atb": ["25"],
                 "padoms": "Ievilktais = puse."},
            ]),
            pavediens="sports",
            konteksts="Visi punkti uz vienas riņķa līnijas «redz» vārtus "
                      "vienādā leņķī - vienādi labas sitiena vietas.",
            kapec="Ievilktais leņķis nav atkarīgs no vietas uz loka."),

    Kopsavilkums([
        "Definēju ievilkto leņķi.",
        "Zinu: ievilktais = puse centra leņķa.",
        "Aprēķinu leņķus no lokiem.",
    ]),

    Majas([
        "Uzzīmē riņķa līniju, centra leņķi 100° un divus ievilktos leņķus.",
        "Izmēri tos ar transportieri.",
        "Kāds ir ievilktais leņķis, kas balstās uz 90° loka?",
    ]),
]
