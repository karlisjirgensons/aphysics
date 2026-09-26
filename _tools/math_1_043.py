# -*- coding: utf-8 -*-
"""1. klase, 43. stunda: «Kāpēc cilvēki vienojās par centimetru?»

Plaukstas un soļi visiem atšķiras, tāpēc cilvēki vienojās par vienu
vienību - centimetru; lineālā tie ir vienādi gari. Lineālu pieliek tā, lai
priekšmeta gals ir pie 0, nevis pie lineāla malas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals)

TEMA = "Kāpēc cilvēki vienojās par centimetru?"

MERKIS = ("Šodien uzzināsim, kāpēc vajag centimetru, un iemācīsimies "
          "pareizi pielikt lineālu.")

SATURS = [
    Sakums("Tavā plaukstā un skolotājas plaukstā - vai tas pats?",
           zimejums=lineals(10, [(0, 6, "6 cm")]),
           paraksts="Centimetrs visiem ir vienāds.",
           fakti=["Plaukstas ir dažādas, centimetrs - vienāds.",
                  "Lineālā starp blakus skaitļiem ir 1 cm.",
                  "Mēri no 0, nevis no lineāla malas."]),

    Doma("Kā pieliek lineālu",
         "Priekšmeta vienu galu novieto pie 0 un nolasa skaitli pie otra "
         "gala.",
         soli=[
             "Atrodi lineālā 0 - tas nav pašā malā.",
             "Novieto priekšmeta galu tieši pie 0.",
             "Lineālu turi gar priekšmetu, taisni.",
             "Nolasi skaitli pie otra gala un pieliec «cm».",
         ]),

    Ievadi("Nolasi garumu", [
        {"jaut": "Cik cm garš?", "zim": lineals(10, [(0, 4, "")]),
         "atb": ["4"], "padoms": "Skaitlis pie gala."},
        {"jaut": "Cik cm garš?", "zim": lineals(10, [(0, 9, "")]),
         "atb": ["9"], "padoms": "Skaitlis pie gala."},
        {"jaut": "Cik cm garš?", "zim": lineals(10, [(0, 7, "")]),
         "atb": ["7"], "padoms": "Skaitlis pie gala."},
    ]),

    Varianti("Vai lineāls pielikts pareizi?", [
        {"jaut": "Priekšmets sākas pie 0.",
         "zim": lineals(10, [(0, 5, "")]),
         "opcijas": ["Pareizi", "Nepareizi"], "jaukt": False, "pareizi": 0,
         "padoms": "Gals pie 0."},
        {"jaut": "Priekšmets sākas pie 2. Vai tas ir 7 cm garš?",
         "zim": lineals(10, [(2, 7, "")]),
         "opcijas": ["Nē, tas ir 5 cm", "Jā, 7 cm"], "jaukt": False,
         "pareizi": 0, "padoms": "Skaiti centimetrus no 2 līdz 7."},
    ]),

    Petijums("Plauksta un centimetrs", [
        "Izmēri savu plaukstu ar lineālu centimetros.",
        "Izmēri blakus sēdētāja plaukstu.",
        "Pierakstiet abus skaitļus.",
        "Vai grāmatas garumu centimetros abi izmērīsiet vienādi?",
    ], vajag="lineāls"),

    Pasaule("Aizkari veikalā",
            Varianti("", [
                {"jaut": "Mamma saka pārdevējai: «Vajag 3 manas plaukstas "
                         "garu auklu.» Kāpēc tas nav labi?",
                 "opcijas": ["pārdevējai plauksta cita",
                             "3 ir par maz", "aukla ir zila"],
                 "pareizi": 0, "padoms": "Plaukstas atšķiras."},
                {"jaut": "Kā pateikt pareizi?",
                 "opcijas": ["«Vajag 50 cm»", "«Vajag drusku»",
                             "«Vajag 3 plaukstas»"],
                 "pareizi": 0, "padoms": "Centimetrs visiem vienāds."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā auklu griež pēc pircēja vēlmes.",
            kapec="Centimetrs ir vienošanās - visi saprot vienādi."),

    Kopsavilkums([
        "Zinu, kāpēc vajag centimetru.",
        "Pielieku lineālu no 0.",
        "Nolasu garumu centimetros.",
    ]),

    Majas([
        "Atrodi mājās lineālu, mērlenti vai metramēru.",
        "Atrodi tajā 0 un 1 cm.",
        "Izmēri savu īkšķi centimetros.",
    ]),
]
