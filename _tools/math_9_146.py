# -*- coding: utf-8 -*-
"""9. klase, 146. stunda: «Kāpēc trijstūris uz diametra ir taisnleņķa?»

Talesa teorēma par riņķa līniju: ja trijstūra mala ir diametrs, pretējais
leņķis ir 90°. Pierādījums ar diviem vienādsānu trijstūriem (OA = OC = OB).
Tā pati sakarība 16. stundā deva tuneļa arkas augstumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija,
                         uz_rinka)

TEMA = "Kāpēc trijstūris uz diametra ir taisnleņķa?"

MERKIS = ("Formulēsim un pierādīsim apgalvojumu par trijstūri, kas balstās "
          "uz diametra.")


def _zim(grads, lenki=(), izcelti=()):
    punkti = [uz_rinka("A", 180), uz_rinka("B", 0), uz_rinka("C", grads),
              ("O", 0, 0, -90)]
    return geometrija(punkti, nogriezni=["AB", "BC", "CA"],
                      izcelti=list(izcelti), taisni=["ACB"],
                      lenki=list(lenki), rinki=[("O", 5)])


SATURS = [
    Sakums("Bīdi C pa riņķa līniju - leņķis paliek 90°",
           zimejums=_zim(60),
           paraksts="AB - diametrs, C - jebkurš riņķa līnijas punkts.",
           fakti=["∠ACB = 90° vienmēr.",
                  "To atklāja jau Taless (ap 600. g. p. m. ē.).",
                  "Otrādi: taisnā leņķa virsotnes ir uz riņķa līnijas."]),

    Slidnis("C dažādās vietās", [
        {"v": "30°", "teksts": "∠ACB = 90°", "zim": _zim(30)},
        {"v": "90°", "teksts": "∠ACB = 90° (vienādsānu)", "zim": _zim(90)},
        {"v": "140°", "teksts": "∠ACB = 90°", "zim": _zim(140)},
    ]),

    Doma("Leņķis uz diametra",
         "Ja trijstūra mala ir riņķa līnijas diametrs, leņķis pretī tai ir "
         "90°.",
         soli=[
             "Novelc OC - rādiuss: OA = OC = OB.",
             "△AOC un △BOC ir vienādsānu: ∠A = ∠ACO, ∠B = ∠BCO.",
             "Tātad ∠C = ∠A + ∠B.",
             "∠A + ∠B + ∠C = 180° ⇒ 2∠C = 180° ⇒ ∠C = 90°.",
         ]),

    Petijums("Pārbaudi ar trijstūri un papīru", [
        "Uzzīmē riņķa līniju un diametru AB.",
        "Atzīmē 3 dažādus punktus C uz riņķa līnijas.",
        "Ar zīmēšanas trijstūri pārbaudi ∠ACB katram.",
        "Pretēji: novieto trijstūra taisno leņķi starp divām naglām - kur "
        "stāv virsotne?",
    ], vajag="cirkulis, lineāls, zīmēšanas trijstūris",
       secinajums="Taisnā leņķa virsotnes veido riņķa līniju ar diametru AB."),

    Ievadi("Aprēķini", [
        {"jaut": "AB - diametrs, ∠CAB = 35°. ∠CBA = ?°", "atb": ["55"],
         "padoms": "∠C = 90°."},
        {"jaut": "Diametrs 10, AC = 6. BC = ?", "atb": ["8"],
         "padoms": "Pitagors."},
        {"jaut": "Taisnleņķa trijstūra katetes 9 un 12. Apvilktās riņķa līnijas "
                 "diametrs?", "atb": ["15"], "padoms": "Hipotenūza."},
    ]),

    Varianti("Patiess?", [
        {"jaut": "Ja ∠ACB = 90°, tad C ir uz riņķa līnijas ar diametru AB.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 0, "padoms": "Apgrieztā teorēma."},
        {"jaut": "Ja AB nav diametrs, ∠ACB var būt 90°.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 1, "padoms": "Tikai uz diametra."},
    ]),

    Pasaule("Galdnieka triks",
            Varianti("", [
                {"jaut": "Galdnieks pārbauda, vai pusapaļa izgriezuma forma ir "
                         "precīzs pusaplis: ieliek stūreni ar taisnu leņķi. Ja "
                         "stūrenis visur skar malu un galus...",
                 "opcijas": ["forma ir pusaplis", "forma ir kvadrāts",
                             "nevar zināt", "forma ir trijstūris"],
                 "pareizi": 0, "padoms": "Taisnais leņķis uz diametra."},
            ]),
            pavediens="maja",
            konteksts="Tā pārbauda pusapaļas arkas, logus un izgriezumus bez "
                      "cirkuļa.",
            kapec="Teorēma pārvēršas darbarīkā."),

    Kopsavilkums([
        "Formulēju teorēmu par leņķi uz diametra.",
        "Pierādu to ar vienādsānu trijstūriem.",
        "Lietoju to aprēķinos.",
    ]),

    Majas([
        "Pieraksti pierādījumu ar pamatojumiem.",
        "Diametrs 26, viena horda no diametra gala 10. Atrodi otru.",
        "Pārbaudi ar šķīvi un stūreni.",
    ]),
]
