# -*- coding: utf-8 -*-
"""9. klase, 9. stunda: «Kāda ir līdzības pirmā pazīme?»

Nav jāmēra sešas lietas: pietiek ar diviem vienādiem leņķiem. Trešais tad
ir vienāds pats no sevis (180°), un malas ir proporcionālas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija, lidzigi)

TEMA = "Kāda ir līdzības pirmā pazīme?"

MERKIS = ("Formulēsim un lietosim trijstūru līdzības pazīmi pēc diviem "
          "leņķiem.")

_ABC = [(0, 0), (6, 0), (2.25, 3.31)]

# Trijstūris ABC ar DE ∥ AC (D ∈ AB, E ∈ BC): △DBE ∼ △ABC.
_IEKSA = geometrija([("A", 0, 0), ("B", 9, 0), ("C", 3, 6), ("D", 4, 0),
                     ("E", 5.667, 3.333)],
                    nogriezni=["AB", "BC", "CA"], izcelti=["DE"],
                    lenki=[("BAC", "", 1), ("BDE", "", 1)])

SATURS = [
    Sakums("Kā Taless izmērīja piramīdu?",
           zimejums=lidzigi(_ABC, 1.6, lenki=[(0, "", 1), (1, "", 2)]),
           paraksts="Saules stari - vienāds leņķis; vertikāle - taisns leņķis.",
           fakti=["Divi vienādi leņķi - trijstūri jau ir līdzīgi.",
                  "Trešais leņķis vienāds pats: 180° − α − β.",
                  "Malas mērīt nevajag."]),

    Doma("Pirmā pazīme: divi leņķi",
         "Ja viena trijstūra divi leņķi ir attiecīgi vienādi ar otra "
         "trijstūra diviem leņķiem, tad trijstūri ir līdzīgi.",
         soli=[
             "Atrodi pirmo vienādo leņķu pāri un pamato (kopīgs, krustleņķi, "
             "paralēles...).",
             "Atrodi otro pāri un pamato.",
             "Pieraksti līdzību pareizā virsotņu secībā.",
             "Tad drīkst lietot malu proporcionalitāti.",
         ]),

    Slidnis("Paralēle trijstūrī", [
        {"v": "Figūra", "teksts": "Trijstūrī ABC novilkta DE ∥ AC.",
         "zim": _IEKSA},
        {"v": "1. leņķis", "teksts": "∠B - kopīgs abiem trijstūriem.",
         "zim": _IEKSA},
        {"v": "2. leņķis", "teksts": "∠BDE = ∠BAC - kāpšļu leņķi pie DE ∥ AC.",
         "zim": _IEKSA},
        {"v": "Secinājums", "teksts": "△DBE ∼ △ABC pēc divu leņķu pazīmes.",
         "zim": _IEKSA},
    ]),

    Paraugs("Pamato un aprēķini",
            uzd="Trijstūrī ABC DE ∥ AC, D ∈ AB, E ∈ BC. BD = 5, AB = 9, "
                "AC = 6. Atrodi DE.",
            soli=[
                ("△DBE ∼ △ABC", "∠B kopīgs, ∠BDE = ∠BAC (kāpšļu leņķi)."),
                ("{DE|AC} = {BD|BA}", "Atbilstošās malas."),
                ("{DE|6} = {5|9} ⇒ DE = {30|9} = {10|3}", "Krusteniski."),
            ],
            atbilde="DE = {10|3} = 3{1|3}"),

    Varianti("Vai trijstūri ir līdzīgi?", [
        {"jaut": "Leņķi 40° un 60° pret 60° un 80°.",
         "opcijas": ["Jā - trešais ir 80° un 40°", "Nē", "Nevar zināt",
                     "Tikai, ja malas vienādas"],
         "pareizi": 0, "padoms": "Aprēķini trešos leņķus."},
        {"jaut": "Leņķi 50° un 70° pret 50° un 50°.",
         "opcijas": ["Nē", "Jā", "Nevar zināt", "Tie ir vienādi"],
         "pareizi": 0, "padoms": "Otrajam trešais ir 80°."},
        {"jaut": "Divi taisnleņķa trijstūri ar vienu šauro leņķi 35°.",
         "opcijas": ["Līdzīgi", "Nelīdzīgi", "Vienādi", "Nevar zināt"],
         "pareizi": 0, "padoms": "90° un 35° abiem."},
        {"jaut": "Divi vienādsānu trijstūri ar virsotnes leņķi 30°.",
         "opcijas": ["Līdzīgi", "Nelīdzīgi", "Nevar zināt",
                     "Tikai ja pamati vienādi"],
         "pareizi": 0, "padoms": "Pamata leņķi abiem 75°."},
    ]),

    Ievadi("Aprēķini (DE ∥ AC)", [
        {"jaut": "BD = 4, BA = 12, AC = 9. DE = ?", "atb": ["3"],
         "padoms": "k = {4|12}."},
        {"jaut": "BE = 3, BC = 7,5, DE = 2. AC = ?", "atb": ["5"],
         "padoms": "{2|AC} = {3|7,5}."},
        {"jaut": "DE = 6, AC = 10, BD = 9. BA = ?", "atb": ["15"],
         "padoms": "{9|BA} = {6|10}."},
        {"jaut": "∠A = 55°, ∠C = 45°. ∠BED = ?°", "atb": ["45"],
         "padoms": "Atbilst ∠C."},
    ]),

    Pasaule("Piramīdas augstums",
            Ievadi("", [
                {"jaut": "Nūja 2 m, tās ēna 3 m. Piramīdas ēna (no centra) "
                         "210 m. Augstums (m)?", "atb": ["140"],
                 "padoms": "{h|210} = {2|3}."},
                {"jaut": "Cilvēks 1,8 m met 2,4 m ēnu. Tornis met 60 m ēnu. "
                         "Augstums (m)?", "atb": ["45"],
                 "padoms": "{h|60} = {1,8|2,4}."},
            ]),
            pavediens="kosmoss",
            konteksts="Saules stari krīt paralēli, tāpēc nūja un piramīda ar "
                      "savām ēnām veido līdzīgus trijstūrus.",
            kapec="Divi vienādi leņķi - un augstumu var izrēķināt."),

    Kopsavilkums([
        "Formulēju līdzības pazīmi pēc diviem leņķiem.",
        "Pamatoju vienādos leņķus (kopīgs, kāpšļu, krustleņķi).",
        "Lietoju līdzību malu aprēķinam.",
    ]),

    Majas([
        "Saulainā dienā izmēri savu ēnu un koka ēnu. Aprēķini koka augstumu.",
        "Uzzīmē trijstūri ar paralēli malai un pieraksti līdzību.",
        "Pamato: divi vienādmalu trijstūri vienmēr ir līdzīgi.",
    ]),
]
