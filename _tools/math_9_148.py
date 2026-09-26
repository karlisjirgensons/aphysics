# -*- coding: utf-8 -*-
"""9. klase, 148. stunda: «Kas ir centra leņķis un loks?»

Riņķa līnijas elementi: rādiuss, diametrs, horda, loks, centra leņķis.
Centra leņķis ir tikpat grādu, cik loks, uz kura tas balstās - pulksteņa
rādītāji ik stundu apraksta 30° loku.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, uz_rinka)

TEMA = "Kas ir centra leņķis un loks?"

MERKIS = ("Nosauksim riņķa līnijas elementus un saistīsim centra leņķi ar "
          "loku.")

_O = ("O", 0, 0, -90)


def _centra(g1, g2, uzraksts):
    return geometrija([_O, uz_rinka("A", g1), uz_rinka("B", g2)],
                      nogriezni=["OA", "OB"], lenki=[("AOB", uzraksts)],
                      rinki=[("O", 5)])


SATURS = [
    Sakums("Pulkstenis: cik grādu ir 1 stunda?",
           zimejums=_centra(90, 0, "90°"),
           paraksts="No 12 līdz 3 - ceturtdaļa apļa: 90°.",
           fakti=["Pilns aplis - 360°, 12 stundas.",
                  "1 stunda - 30° loks.",
                  "Leņķis pie centra = loka grādu mērs."]),

    Doma("Centra leņķis",
         "Leņķi ar virsotni riņķa līnijas centrā sauc par centra leņķi; tā "
         "lielums ir vienāds ar loka, uz kura tas balstās, grādu mēru.",
         soli=[
             "Horda - nogrieznis starp diviem riņķa līnijas punktiem.",
             "Diametrs - garākā horda, iet caur centru.",
             "Horda sadala riņķa līniju divos lokos.",
             "Abu loku summa ir 360°.",
         ]),

    Slidnis("Centra leņķi", [
        {"v": "60°", "teksts": "Loks AB = 60° - sestdaļa apļa",
         "zim": _centra(60, 0, "60°")},
        {"v": "120°", "teksts": "Loks AB = 120° - trešdaļa",
         "zim": _centra(120, 0, "120°")},
        {"v": "180°", "teksts": "Izstiepts leņķis - AB ir diametrs",
         "zim": geometrija([_O, uz_rinka("A", 180), uz_rinka("B", 0)],
                           nogriezni=["AB"], rinki=[("O", 5)])},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Centra leņķis 75°. Mazākais loks (°)?", "atb": ["75"],
         "padoms": "Vienāds."},
        {"jaut": "Tai pašai hordai lielākais loks (°)?", "atb": ["285"],
         "padoms": "360 − 75."},
        {"jaut": "Pulkstenī no 12 līdz 5 - cik grādu?", "atb": ["150"],
         "padoms": "5 · 30."},
        {"jaut": "Loks ir {1|8} apļa. Centra leņķis (°)?", "atb": ["45"],
         "padoms": "360 : 8."},
    ]),

    Varianti("Nosauc elementu", [
        {"jaut": "Nogrieznis starp diviem riņķa līnijas punktiem...",
         "opcijas": ["horda", "rādiuss", "loks", "pieskare"],
         "pareizi": 0, "padoms": "Definīcija."},
        {"jaut": "Horda caur centru...",
         "opcijas": ["diametrs", "rādiuss", "loks", "sekante"],
         "pareizi": 0, "padoms": "Garākā horda."},
        {"jaut": "OA = OB, jo...",
         "opcijas": ["abi ir rādiusi", "abi ir hordas", "leņķis 60°",
                     "dots"],
         "pareizi": 0, "padoms": "No centra līdz riņķa līnijai."},
    ]),

    Pasaule("Picas gabali",
            Ievadi("", [
                {"jaut": "Picu sagriež 8 vienādos gabalos. Cik grādu ir katra "
                         "gabala centra leņķis?", "atb": ["45"],
                 "padoms": "360 : 8."},
                {"jaut": "Ja pica sagriezta 12 gabalos?", "atb": ["30"],
                 "padoms": "360 : 12."},
                {"jaut": "Tev ir 3 gabali no 8. Cik grādu kopā?",
                 "atb": ["135"], "padoms": "3 · 45."},
            ]),
            pavediens="virtuve",
            konteksts="Picas griezējs dala centra leņķi vienādās daļās.",
            kapec="Centra leņķis ir «gabala platums» grādos.",
            zimejums=_centra(45, 0, "45°")),

    Kopsavilkums([
        "Nosaucu riņķa līnijas elementus.",
        "Zinu: centra leņķis = loka grādu mērs.",
        "Aprēķinu lokus un centra leņķus.",
    ]),

    Majas([
        "Uzzīmē riņķa līniju un atzīmē hordu, diametru, loku.",
        "Kādu leņķi apraksta minūšu rādītājs 20 minūtēs?",
        "Sagriez papīra apli 6 vienādos sektoros un izmēri leņķi.",
    ]),
]
