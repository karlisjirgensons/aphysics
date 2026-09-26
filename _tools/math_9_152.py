# -*- coding: utf-8 -*-
"""9. klase, 152. stunda: «Kā aprēķināt leņķus riņķa līnijā?»

Jaukti uzdevumi: centra un ievilktie leņķi, leņķis uz diametra, vienādsānu
trijstūri ar rādiusiem, ievilkts četrstūris. Katram leņķim - pamatojums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija, uz_rinka)

TEMA = "Kā aprēķināt leņķus riņķa līnijā?"

MERKIS = ("Aprēķināsim nezināmos leņķus, lietojot ievilktā leņķa "
          "īpašības.")

_ZIM = geometrija([("O", 0, 0, -90), uz_rinka("A", 200), uz_rinka("B", 340),
                   uz_rinka("C", 100)],
                  nogriezni=["CA", "CB", "AB", "OA", "OB"],
                  lenki=[("AOB", "140°"), ("ACB", "?"), ("OAB", "?")],
                  rinki=[("O", 5)])

SATURS = [
    Sakums("Trīs leņķi no viena skaitļa",
           zimejums=_ZIM,
           paraksts="∠AOB = 140°. Atrodi ∠ACB un ∠OAB.",
           fakti=["∠ACB = {140°|2} = 70° (ievilktais).",
                  "△AOB vienādsānu: ∠OAB = {180° − 140°|2} = 20°.",
                  "Katram solim - sava īpašība."]),

    Doma("Rīki leņķu aprēķinam",
         "Centra = loks; ievilktais = puse loka; uz diametra = 90°; rādiusi "
         "veido vienādsānu trijstūrus; ievilktā četrstūrī pretējie kopā 180°.",
         soli=[
             "Iezīmē rādiusus - meklē vienādsānu trijstūrus.",
             "Nosaki lokus un to grādu mērus.",
             "Lieto trijstūra leņķu summu 180°.",
             "Pie katra rezultāta pieraksti īpašību.",
         ]),

    Paraugs("Ievilkts četrstūris",
            uzd="Četrstūris ABCD ir ievilkts riņķa līnijā, ∠A = 85°, "
                "∠B = 70°. Atrodi ∠C un ∠D.",
            soli=[
                ("∠C = 180° − 85° = 95°", "Pretējie leņķi."),
                ("∠D = 180° − 70° = 110°", "Pretējie leņķi."),
            ],
            atbilde="∠C = 95°, ∠D = 110°"),

    Ievadi("Aprēķini", [
        {"jaut": "∠AOB = 80°. ∠OAB = ?°", "atb": ["50"],
         "padoms": "(180 − 80) : 2."},
        {"jaut": "AB - diametrs, ∠ABC = 28°. ∠BAC = ?°", "atb": ["62"],
         "padoms": "∠C = 90°."},
        {"jaut": "Ievilktais ∠ACB = 35°. △AOB leņķis pie A = ?°",
         "atb": ["55"], "padoms": "∠AOB = 70°; (180 − 70) : 2."},
        {"jaut": "Ievilktā četrstūrī ∠A = 3∠C. ∠A = ?°", "atb": ["135"],
         "padoms": "4∠C = 180."},
    ]),

    Varianti("Pamatojums", [
        {"jaut": "∠OAB = ∠OBA, jo...",
         "opcijas": ["OA = OB - rādiusi", "AB - diametrs",
                     "ievilktie leņķi", "dots"],
         "pareizi": 0, "padoms": "Vienādsānu."},
        {"jaut": "∠A + ∠C = 180° ievilktā četrstūrī, jo...",
         "opcijas": ["loki kopā 360°, ievilktie - puse", "tā ir pazīme",
                     "trijstūra summa", "vienmēr visiem četrstūriem"],
         "pareizi": 0, "padoms": "Divi ievilkti uz papildu lokiem."},
    ]),

    Pasaule("Ratu spieķi",
            Ievadi("", [
                {"jaut": "Velosipēda ratā 36 spieķi vienādos leņķos. Leņķis "
                         "starp blakus spieķiem (°)?", "atb": ["10"],
                 "padoms": "360 : 36."},
                {"jaut": "Ievilktais leņķis uz loka starp 2 blakus spieķiem "
                         "(°)?", "atb": ["5"], "padoms": "Puse."},
            ]),
            pavediens="sports",
            konteksts="Spieķi ir rādiusi - starp tiem ir centra leņķi.",
            kapec="Centra un ievilktie leņķi ir riteņa ģeometrija."),

    Kopsavilkums([
        "Aprēķinu leņķus ar centra un ievilktā leņķa īpašībām.",
        "Izmantoju vienādsānu trijstūrus ar rādiusiem.",
        "Lietoju ievilktā četrstūra īpašību.",
    ]),

    Majas([
        "∠AOB = 124°. Atrodi ∠OAB un ievilkto ∠ACB.",
        "Ievilktā četrstūrī ∠B = 2∠D. Atrodi ∠B.",
        "Izveido savu uzdevumu ar 3 soļiem.",
    ]),
]
