# -*- coding: utf-8 -*-
"""7. klase, 109. stunda: «Kā uzbūvēt pierādījumu?»

Garākā pierādījumā apvieno visu, kas apgūts: leņķus pie paralēlām, leņķu
summu un trijstūru vienādību. Stunda pierāda figūras īpašību - ka
paralelograma pretējās malas un leņķi ir vienādi.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, geometrija, restis)

TEMA = "Kā uzbūvēt pierādījumu?"

MERKIS = ("Pierādīsim figūras īpašību, lietojot leņķu sakarības un "
          "trijstūru vienādību.")

_PAR = geometrija([("A", 0, 0), ("B", 6, 0), ("C", 8, 3), ("D", 2, 3)],
                  nogriezni=["AB", "BC", "CD", "DA"], izcelti=["AC"],
                  lenki=[("BAC", "", 1), ("DCA", "", 1), ("CAD", "", 2),
                         ("ACB", "", 2)])

SATURS = [
    Sakums("Paralelograms - no divām paralēlu pāriem",
           zimejums=_PAR,
           paraksts="AB ∥ CD, AD ∥ BC. Diagonāle AC dala to divos trijstūros.",
           fakti=["Diagonāle ir krustotājs abiem paralēlu pāriem.",
                  "Iegūst divus šķērsleņķu pārus.",
                  "Un kopīgu malu - pazīme lml."]),

    Doma("Pierādījums no gabaliem",
         "Garāku pierādījumu būvē no zināmiem gabaliem: palīgkonstrukcija "
         "(diagonāle), leņķu vienādība (šķērsleņķi), trijstūru vienādība "
         "(pazīme) un secinājums (atbilstošie elementi).",
         soli=[
             "Novelc diagonāli AC.",
             "AB ∥ CD: ∠BAC = ∠DCA (šķērsleņķi).",
             "AD ∥ BC: ∠DAC = ∠BCA (šķērsleņķi).",
             "AC kopīga: △ABC = △CDA (lml).",
             "Tātad AB = CD, BC = DA, ∠B = ∠D.",
         ]),

    Paraugs("Paralelograma īpašība",
            uzd="Dots: ABCD - paralelograms (AB ∥ CD, AD ∥ BC). Pierādi, "
                "ka AB = CD un AD = BC.",
            soli=[
                ("∠BAC = ∠DCA", "(iekšējie šķērsleņķi, AB ∥ CD)"),
                ("∠BCA = ∠DAC", "(iekšējie šķērsleņķi, AD ∥ BC)"),
                ("AC = CA", "(kopīga mala)"),
                ("△ABC = △CDA", "(lml)"),
                ("AB = CD, BC = DA", "(atbilstošās malas)"),
            ],
            atbilde="Paralelograma pretējās malas ir vienādas."),

    Zimejums("Pierādījuma karte",
             restis([["gabals", "kas tas ir"],
                     ["diagonāle", "palīgkonstrukcija"],
                     ["šķērsleņķi", "paralēlu taišņu īpašība"],
                     ["lml", "trijstūru vienādības pazīme"],
                     ["AB = CD", "atbilstošie elementi"]]),
             paskaidro="Katrs gabals ir no citas stundas."),

    Varianti("Pierādījuma loģika", [
        {"jaut": "Kāpēc novelk diagonāli?",
         "opcijas": ["Lai iegūtu trijstūrus, kuriem var lietot pazīmes",
                     "Lai zīmējums būtu skaistāks",
                     "Diagonāle vienmēr jāvelk", "Lai izmērītu"],
         "pareizi": 0, "padoms": "Pazīmes ir trijstūriem."},
        {"jaut": "No △ABC = △CDA secina arī...",
         "opcijas": ["∠B = ∠D", "∠A = ∠B", "AC = BD", "AB = BC"],
         "pareizi": 0, "padoms": "Atbilstošie leņķi."},
        {"jaut": "Kura pazīme šeit lietota?",
         "opcijas": ["lml", "mmm", "mlm", "Neviena"],
         "pareizi": 0, "padoms": "Mala AC un divi leņķi pie tās."},
    ]),

    Pasaule("Paralelograms mehānismos",
            Varianti("", [
                {"jaut": "Galda lampas plecs ir paralelograms. Kāpēc lampa "
                         "paliek vērsta vienā virzienā, kad to pārvieto?",
                 "opcijas": ["Pretējās malas paliek paralēlas",
                             "Lampa ir smaga", "Tā ir magnētiska",
                             "Tā nepaliek"],
                 "pareizi": 0, "padoms": "Paralelograma īpašība."},
                {"jaut": "Kas notiek ar malu garumiem, kustinot plecu?",
                 "opcijas": ["Paliek vienādi - pretējās vienādas",
                             "Mainās", "Kļūst 0", "Dubultojas"],
                 "pareizi": 0, "padoms": "Stieņi ir cieti."},
                {"jaut": "Kas mainās?",
                 "opcijas": ["Leņķi", "Malas", "Nekas", "Krāsa"],
                 "pareizi": 0, "padoms": "Paralelograms «sagāžas»."},
            ]),
            pavediens="tehnika",
            konteksts="Lampas, logu vērtnes un pacēlāji izmanto "
                      "paralelogramu - tā malas paliek paralēlas.",
            kapec="Pierādītā īpašība strādā mehānismā."),

    Kopsavilkums([
        "Būvēju pierādījumu no zināmiem gabaliem.",
        "Lietoju palīgkonstrukciju.",
        "Apvienoju paralēlu taišņu īpašības un pazīmi lml.",
        "Pierādu paralelograma pretējo malu vienādību.",
    ]),

    Majas([
        "Pierādi, ka paralelograma pretējie leņķi ir vienādi.",
        "Pierādi, ka paralelograma diagonāles krustpunktā dalās uz pusēm.",
        "Atrodi mājās paralelograma mehānismu.",
    ]),
]
