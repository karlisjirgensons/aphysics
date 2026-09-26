# -*- coding: utf-8 -*-
"""9. klase, 153. stunda: «Kādas īpašības ir hordai?»

Perpendikuls no centra uz hordu dala to uz pusēm; tāpēc
R^2 = d^2 + ({h|2})^2, kur d - hordas attālums līdz centram. Stāsts:
cik dziļš ir apaļas caurules ūdens līmenis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, uz_rinka)

TEMA = "Kādas īpašības ir hordai?"

MERKIS = ("Lietosim sakarību starp hordu, tās attālumu līdz centram un "
          "rādiusu.")

_ZIM = geometrija([("O", 0, 0, 90), uz_rinka("A", 216.87),
                   uz_rinka("B", 323.13), ("M", 0, -3, -90)],
                  nogriezni=["AB", "OA", "OM"], taisni=["OMB"],
                  malas=[("OA", "R = 5"), ("OM", "3"), ("AM", "4")],
                  rinki=[("O", 5)])

SATURS = [
    Sakums("Horda, rādiuss un attālums - Pitagora trijstūris",
           zimejums=_ZIM,
           paraksts="R = 5, attālums 3 ⇒ puse hordas 4, horda 8.",
           fakti=["OM ⊥ AB dala hordu uz pusēm.",
                  "R^2 = OM^2 + AM^2.",
                  "Jo tuvāk centram, jo garāka horda."]),

    Doma("Hordas īpašība",
         "Perpendikuls no centra uz hordu dala to uz pusēm: "
         "R^2 = d^2 + ({h|2})^2.",
         soli=[
             "Novelc perpendikulu OM uz hordu.",
             "Novelc rādiusu uz hordas galu.",
             "Pitagors taisnleņķa trijstūrī OMA.",
             "Horda h = 2 · AM.",
         ],
         pieze="Vienādas hordas atrodas vienādā attālumā no centra."),

    Paraugs("Attālums līdz centram",
            uzd="Riņķa līnijas rādiuss 13 cm, horda 24 cm. Cik tālu horda ir "
                "no centra?",
            soli=[
                ("AM = 24 : 2 = 12", "Puse hordas."),
                ("d^2 = 13^2 − 12^2 = 25", "Pitagors."),
                ("d = 5 cm", "Attālums."),
            ],
            atbilde="5 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "R = 10, d = 6. Horda = ?", "atb": ["16"],
         "padoms": "Puse 8."},
        {"jaut": "Horda 30, d = 8. R = ?", "atb": ["17"],
         "padoms": "√(64 + 225)."},
        {"jaut": "R = 5, horda 6. d = ?", "atb": ["4"], "padoms": "3, 4, 5."},
        {"jaut": "Garākā horda, ja R = 7?", "atb": ["14"],
         "padoms": "Diametrs."},
    ]),

    Varianti("Patiess?", [
        {"jaut": "Diametrs, kas perpendikulārs hordai, dala to uz pusēm.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 0, "padoms": "Īpašība."},
        {"jaut": "Garāka horda atrodas tālāk no centra.",
         "opcijas": ["Patiess", "Aplams"], "jaukt": False,
         "pareizi": 1, "padoms": "Tuvāk centram - garāka."},
    ]),

    Pasaule("Ūdens caurulē",
            Ievadi("", [
                {"jaut": "Caurules iekšējais diametrs 100 cm; ūdens virsmas "
                         "platums 80 cm. Cik cm virsma ir no centra?",
                 "atb": ["30"], "padoms": "√(2500 − 1600)."},
                {"jaut": "Ūdens zem centra. Cik cm dziļš ūdens?",
                 "atb": ["20"], "padoms": "50 − 30."},
            ]),
            pavediens="planeta",
            konteksts="Kanalizācijas un lietus ūdens caurules parasti nav "
                      "pilnas - ūdens virsma ir horda.",
            kapec="Hordas īpašība dod ūdens dziļumu bez mērīšanas iekšā."),

    Kopsavilkums([
        "Zinu, ka perpendikuls no centra dala hordu uz pusēm.",
        "Lietoju R^2 = d^2 + ({h|2})^2.",
        "Atrodu hordu, rādiusu vai attālumu.",
    ]),

    Majas([
        "R = 25, horda 48. Atrodi attālumu līdz centram.",
        "Divas paralēlas hordas 12 un 16, R = 10. Cik tālu tās viena no otras?",
        "Izmēri glāzē ūdens virsmas platumu, kad glāze sasvērta.",
    ]),
]
