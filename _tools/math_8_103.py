# -*- coding: utf-8 -*-
"""8. klase, 103. stunda: «Kādas ir taisnstūra īpašības?»

Taisnstūra diagonāles ir vienādas: △ABD = △BAC pēc divām malām un leņķim
starp tām (AB kopīga, AD = BC, ∠A = ∠B = 90°). Tāpēc AO = BO = CO = DO,
un △AOB ir vienādsānu. Pazīme: paralelograms ar vienādām diagonālēm ir
taisnstūris - tā būvnieki pārbauda stūrus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, geometrija)

TEMA = "Kādas ir taisnstūra īpašības?"

MERKIS = "Formulēsim un pierādīsim taisnstūra īpašības par diagonālēm."

SATURS = [
    Sakums("Vai taisnstūra diagonāles ir vienādas?",
           zimejums=geometrija([("A", 0, 0), ("B", 7, 0), ("C", 7, 4),
                                ("D", 0, 4), ("O", 3.5, 2, 270)],
                               nogriezni=["AB", "BC", "CD", "DA", "AC",
                                          "BD"],
                               svitras=[("AO", 1), ("BO", 1), ("CO", 1),
                                        ("DO", 1)],
                               taisni=["BAD"], iekrasot=[("ABCD", 0)]),
           paraksts="AO = BO = CO = DO.",
           fakti=["Taisnstūris - paralelograms ar taisnu leņķi.",
                  "Taisnstūra diagonāles ir vienādas.",
                  "Krustpunkts O ir vienādā attālumā no visām virsotnēm."]),

    Doma("Taisnstūra īpašības",
         "Taisnstūrim ir visas paralelograma īpašības un vienādas "
         "diagonāles.",
         soli=[
             "Visi leņķi ir 90°.",
             "Diagonāles ir vienādas un dalās uz pusēm.",
             "Tātad AO = BO = CO = DO - trijstūri AOB, BOC ir vienādsānu.",
             "Pazīme: paralelograms ar vienādām diagonālēm ir taisnstūris.",
         ]),

    Paraugs("Pierādījums",
            uzd="Pierādi, ka taisnstūra ABCD diagonāles ir vienādas.",
            soli=[
                ("AB - kopīga", "△ABD un △BAC."),
                ("AD = BC", "Pretējās malas."),
                ("∠DAB = ∠CBA = 90°", "Taisnstūra leņķi."),
                ("△ABD = △BAC", "Pēc divām malām un leņķa starp tām."),
                ("BD = AC", "Atbilstošās malas."),
            ],
            atbilde="AC = BD"),

    Ievadi("Aprēķini", [
        {"jaut": "AC = 10 cm. BO (cm)?", "atb": ["5"],
         "padoms": "BD = AC, puse."},
        {"jaut": "∠AOB = 60°, AB = 4 cm. AC (cm)?", "atb": ["8"],
         "padoms": "△AOB vienādmalu: AO = 4."},
        {"jaut": "∠CAB = 25°. ∠ABD?", "atb": ["25"],
         "padoms": "AO = BO - vienādsānu."},
        {"jaut": "∠AOB = 110°. ∠AOD?", "atb": ["70"],
         "padoms": "Blakusleņķi."},
        {"jaut": "BD = 3x − 2, AC = x + 6. x?", "atb": ["4"],
         "padoms": "3x − 2 = x + 6."},
    ]),

    Varianti("Spried", [
        {"jaut": "Rāmim pretējās malas vienādas. Kā pārbaudīt, vai stūri "
                 "taisni?",
         "opcijas": ["Izmērīt abas diagonāles", "Izmērīt vienu malu",
                     "Saskaitīt stūrus", "Izmērīt perimetru"],
         "pareizi": 0, "padoms": "Vienādas diagonāles ⇒ taisnstūris."},
        {"jaut": "Vai taisnstūra diagonāles ir perpendikulāras?",
         "opcijas": ["Tikai kvadrātam", "Vienmēr", "Nekad",
                     "Tikai garam"],
         "pareizi": 0, "padoms": "Tā ir romba īpašība."},
        {"jaut": "Trijstūris AOB taisnstūrī ir...",
         "opcijas": ["vienādsānu", "vienmēr vienādmalu", "taisnleņķa",
                     "vienmēr platleņķa"],
         "pareizi": 0, "padoms": "AO = BO."},
    ]),

    Pasaule("Pamatu nospraušana",
            Ievadi("", [
                {"jaut": "Mājas pamati 10 m × 6 m, pretējās malas vienādas. "
                         "Diagonāles 11,6 m un 11,8 m. Vai stūri taisni? "
                         "(1 - jā, 0 - nē)",
                 "atb": ["0"], "padoms": "Diagonāles nav vienādas."},
                {"jaut": "Pēc labošanas abas diagonāles ir 11,7 m. Cik m no "
                         "krustpunkta līdz stūrim?",
                 "atb": ["5,85"], "padoms": "11,7 : 2."},
                {"jaut": "Pamatu perimetrs (m)?", "atb": ["32"],
                 "padoms": "2 · (10 + 6)."},
            ]),
            pavediens="maja",
            konteksts="Būvnieki pārbauda taisnos stūrus, mērot diagonāles.",
            kapec="Paralelograms ar vienādām diagonālēm ir taisnstūris."),

    Kopsavilkums([
        "Pierādu, ka taisnstūra diagonāles ir vienādas.",
        "Lietoju vienādsānu trijstūrus pie diagonāļu krustpunkta.",
        "Pārbaudu taisnos leņķus ar diagonālēm.",
    ]),

    Majas([
        "Izmēri durvju vai loga rāmja diagonāles - vai tās vienādas?",
        "Uzzīmē taisnstūri un izmēri leņķi starp diagonālēm.",
        "Paskaidro, kāpēc paralelogramam diagonāles parasti nav vienādas.",
    ]),
]
