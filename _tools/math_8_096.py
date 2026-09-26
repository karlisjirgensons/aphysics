# -*- coding: utf-8 -*-
"""8. klase, 96. stunda: «Kādas ir paralelograma īpašības?»

Pretējās malas un pretējie leņķi ir vienādi, blakus leņķu summa 180°.
Pierādījums: diagonāle AC sadala paralelogramu divos vienādos trijstūros
pēc pazīmes leņķis-mala-leņķis (šķērsleņķi pie abiem paralēlo malu
pāriem un kopīgā mala AC).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kādas ir paralelograma īpašības?"

MERKIS = ("Formulēsim un pierādīsim paralelograma īpašības par malām un "
          "leņķiem.")

_PUNKTI = [("A", 0, 0), ("B", 5, 0), ("C", 6.5, 3), ("D", 1.5, 3)]

SATURS = [
    Sakums("Kas paralelogramā ir vienāds?",
           zimejums=geometrija(_PUNKTI, nogriezni=["AB", "BC", "CD", "DA"],
                               svitras=[("AB", 1), ("CD", 1), ("BC", 2),
                                        ("DA", 2)],
                               lenki=[("BAD", "", 1), ("DCB", "", 1),
                                      ("CBA", "", 2), ("ADC", "", 2)],
                               iekrasot=[("ABCD", 0)]),
           paraksts="Vienādas svītriņas - vienādas malas, vienādi loki - "
                    "vienādi leņķi.",
           fakti=["Pretējās malas ir vienādas.",
                  "Pretējie leņķi ir vienādi.",
                  "Blakus leņķu summa ir 180°."]),

    Doma("Īpašības",
         "Diagonāle sadala paralelogramu divos vienādos trijstūros.",
         soli=[
             "AB = CD un AD = BC.",
             "∠A = ∠C un ∠B = ∠D.",
             "∠A + ∠B = 180° - tie ir vienpusleņķi pie AD ∥ BC.",
         ]),

    Paraugs("Pierādījums",
            uzd="Pierādi, ka paralelogramā ABCD AB = CD un ∠B = ∠D.",
            soli=[
                ("∠BAC = ∠DCA", "Šķērsleņķi, jo AB ∥ CD."),
                ("∠BCA = ∠DAC", "Šķērsleņķi, jo AD ∥ BC."),
                ("AC - kopīga mala", "Abiem trijstūriem."),
                ("△ABC = △CDA", "Pēc pazīmes leņķis-mala-leņķis."),
                ("AB = CD, ∠B = ∠D", "Atbilstošie elementi vienādos "
                                     "trijstūros."),
            ],
            atbilde="AB = CD un ∠B = ∠D"),

    Ievadi("Aprēķini", [
        {"jaut": "AB = 7 cm, BC = 4 cm. CD (cm)?", "atb": ["7"],
         "padoms": "Pretējā mala."},
        {"jaut": "∠A = 65°. ∠C?", "atb": ["65"], "padoms": "Pretējais."},
        {"jaut": "∠A = 65°. ∠B?", "atb": ["115"], "padoms": "180 − 65."},
        {"jaut": "Perimetrs 30 cm, AB = 9 cm. BC (cm)?", "atb": ["6"],
         "padoms": "AB + BC = 15."},
        {"jaut": "∠A : ∠B = 1 : 2. ∠A?", "atb": ["60"],
         "padoms": "3 daļas = 180°."},
    ]),

    Varianti("Spried", [
        {"jaut": "Kāpēc △ABC = △CDA?",
         "opcijas": ["Pēc pazīmes leņķis-mala-leņķis", "Tie ir līdzīgi",
                     "Tie ir taisnleņķa", "Tā izskatās"],
         "pareizi": 0, "padoms": "Divi šķērsleņķi un kopīga mala."},
        {"jaut": "Paralelogramā ∠A = 100°. Vai ∠B = 100°?",
         "opcijas": ["Nē - ∠B = 80°", "Jā", "Nevar noteikt",
                     "Tikai rombā"],
         "pareizi": 0, "padoms": "Blakus leņķi dod 180°."},
        {"jaut": "Kuri leņķi ir šķērsleņķi pie diagonāles AC?",
         "opcijas": ["∠BAC un ∠DCA", "∠BAC un ∠BCA", "∠A un ∠B",
                     "∠B un ∠D"],
         "pareizi": 0, "padoms": "AB ∥ CD, AC - krustotājs."},
    ]),

    Pasaule("Vārti",
            Ievadi("", [
                {"jaut": "Sašķiebušies vārti ir paralelograms: augšējā mala "
                         "2 m, slīpā mala 1,2 m. Cik m koka rāmī?",
                 "atb": ["6,4"], "padoms": "2 · (2 + 1,2)."},
                {"jaut": "Leņķis apakšējā kreisajā stūrī 75°. Apakšējā "
                         "labajā?",
                 "atb": ["105"], "padoms": "180 − 75."},
                {"jaut": "Augšējā labajā stūrī?", "atb": ["75"],
                 "padoms": "Pretējais leņķis."},
            ]),
            pavediens="maja",
            konteksts="Kad vārti sašķiebjas, taisnstūris kļūst par "
                      "paralelogramu, bet malas paliek tās pašas.",
            kapec="Paralelograma pretējās malas un leņķi ir vienādi."),

    Kopsavilkums([
        "Formulēju paralelograma īpašības par malām un leņķiem.",
        "Pierādu tās ar vienādiem trijstūriem.",
        "Lietoju īpašības aprēķinos.",
    ]),

    Majas([
        "Uzzīmē paralelogramu, izmēri malas un leņķus un pārbaudi īpašības.",
        "Pieraksti pierādījumu, ka ∠A = ∠C.",
        "Aprēķini paralelograma leņķus, ja viens ir par 40° lielāks.",
    ]),
]
