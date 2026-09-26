# -*- coding: utf-8 -*-
"""9. klase, 16. stunda: «Kā līdzība palīdz taisnleņķa trijstūrī?»

Augstums pret hipotenūzu sadala taisnleņķa trijstūri divos trijstūros, kas
abi ir līdzīgi lielajam. No tā izriet CH^2 = AH · HB un katetes kvadrāts ir
hipotenūzas un projekcijas reizinājums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā līdzība palīdz taisnleņķa trijstūrī?"

MERKIS = ("Lietosim līdzību taisnleņķa trijstūrī ar augstumu pret "
          "hipotenūzu.")

_PUNKTI = [("A", 0, 0), ("B", 25, 0), ("C", 9, 12), ("H", 9, 0)]


def _zim(iekrasot=(), malas=()):
    return geometrija(_PUNKTI, nogriezni=["AB", "BC", "CA"],
                      izcelti=["CH"], taisni=["ACB", "CHB"],
                      iekrasot=list(iekrasot), malas=list(malas))


SATURS = [
    Sakums("Viens trijstūris - trīs līdzīgi",
           zimejums=_zim(iekrasot=[("AHC", 0), ("CHB", 1)],
                         malas=[("AH", "9"), ("HB", "16")]),
           paraksts="CH ⊥ AB. Cik garš ir augstums CH?",
           fakti=["△ACH ∼ △CBH ∼ △ABC - visiem ir taisns leņķis.",
                  "CH^2 = AH · HB = 9 · 16 = 144, CH = 12.",
                  "Tā aprēķina augstumu bez Pitagora teorēmas."]),

    Slidnis("Kāpēc tie ir līdzīgi", [
        {"v": "△ACH", "teksts": "∠A kopīgs ar △ABC, ∠AHC = ∠ACB = 90°",
         "zim": _zim(iekrasot=[("AHC", 0)])},
        {"v": "△CBH", "teksts": "∠B kopīgs ar △ABC, ∠CHB = ∠ACB = 90°",
         "zim": _zim(iekrasot=[("CHB", 1)])},
        {"v": "Abi", "teksts": "Abi līdzīgi △ABC, tātad arī viens otram",
         "zim": _zim(iekrasot=[("AHC", 0), ("CHB", 1)])},
    ]),

    Doma("Proporcionālie nogriežņi",
         "Taisnleņķa trijstūrī ar augstumu CH: CH^2 = AH · HB, AC^2 = AB · AH, "
         "BC^2 = AB · HB.",
         soli=[
             "AH un HB ir katešu projekcijas uz hipotenūzas.",
             "Augstums ir projekciju vidējais ģeometriskais.",
             "Katete ir hipotenūzas un savas projekcijas vidējais "
             "ģeometriskais.",
         ],
         pieze="Pārbaude: AC^2 + BC^2 = AB · AH + AB · HB = AB · AB - "
               "Pitagora teorēma."),

    Paraugs("Aprēķini visu",
            uzd="Taisnleņķa △ABC (∠C = 90°) CH ⊥ AB, AH = 9, HB = 16. Atrodi "
                "CH, AC un BC.",
            soli=[
                ("CH^2 = 9 · 16 = 144, CH = 12", "Augstums."),
                ("AC^2 = 25 · 9 = 225, AC = 15", "AB = 9 + 16 = 25."),
                ("BC^2 = 25 · 16 = 400, BC = 20", "Otra katete."),
            ],
            atbilde="CH = 12, AC = 15, BC = 20"),

    Ievadi("Aprēķini", [
        {"jaut": "AH = 4, HB = 9. CH = ?", "atb": ["6"],
         "padoms": "√(4 · 9)."},
        {"jaut": "AH = 2, HB = 8. CH = ?", "atb": ["4"],
         "padoms": "√16."},
        {"jaut": "AB = 10, AH = 3,6. AC = ?", "atb": ["6"],
         "padoms": "AC^2 = 36."},
        {"jaut": "CH = 6, AH = 3. HB = ?", "atb": ["12"],
         "padoms": "36 = 3 · HB."},
        {"jaut": "AC = 6, AB = 9. AH = ?", "atb": ["4"],
         "padoms": "36 = 9 · AH."},
        {"jaut": "AH = 1, HB = 3. CH = √? (ieraksti zemsaknes skaitli)",
         "atb": ["3"], "padoms": "CH^2 = 3."},
    ], pamats=4),

    Varianti("Izvēlies", [
        {"jaut": "Kura sakarība ir pareiza?",
         "opcijas": ["CH^2 = AH · HB", "CH = AH · HB", "CH^2 = AH + HB",
                     "CH^2 = AC · BC"],
         "pareizi": 0, "padoms": "Projekciju reizinājums."},
        {"jaut": "Kurš trijstūris atbilst △ACH (A ↔ A)?",
         "opcijas": ["△ABC", "△BAC", "△CBH", "△BCA"],
         "pareizi": 0, "padoms": "A-A, C-B, H-C."},
    ]),

    Pasaule("Tuneļa arka",
            Ievadi("", [
                {"jaut": "Pusloka arkas diametrs 10 m. Cik m augsta ir arka "
                         "1 m no malas?", "atb": ["3"],
                 "padoms": "h^2 = 1 · 9."},
                {"jaut": "Cik m augsta tā ir 2 m no malas?", "atb": ["4"],
                 "padoms": "h^2 = 2 · 8."},
                {"jaut": "Cik m augsta tā ir centrā?", "atb": ["5"],
                 "padoms": "h^2 = 5 · 5."},
            ]),
            pavediens="celojums",
            konteksts="Punkts uz arkas un diametra gali veido taisnleņķa "
                      "trijstūri (to pierādīsim 9.8. tematā).",
            kapec="Augstums pret hipotenūzu dod arkas augstumu jebkurā "
                  "vietā."),

    Kopsavilkums([
        "Pamatoju trīs līdzīgus trijstūrus.",
        "Lietoju CH^2 = AH · HB.",
        "Aprēķinu katetes no projekcijām.",
    ]),

    Majas([
        "AH = 5, HB = 20. Atrodi CH, AC un BC.",
        "Pierādi Pitagora teorēmu ar šīm sakarībām.",
        "Uzzīmē pusloku ar diametru 10 cm un pārbaudi h^2 = a · b ar lineālu.",
    ]),
]
