# -*- coding: utf-8 -*-
"""9. klase, 7. stunda: «Ko nozīmē «līdzīgi»?»

Ikdienā «līdzīgs» nozīmē «mazliet kā»; matemātikā - tieši tāda pati forma
citā mērogā. Divi nosacījumi: vienādi leņķi un proporcionālas malas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, lidzigi)

TEMA = "Ko nozīmē «līdzīgi»?"

MERKIS = ("Definēsim līdzīgus trijstūrus un nosauksim to atbilstošos "
          "elementus.")

# Trijstūris ar malām AB = 6, AC = 4, BC = 5.
_ABC = [(0, 0), (6, 0), (2.25, 3.31)]


def _pari(k, m):
    return lidzigi(_ABC, k, malas=[(0, 1, "6"), (0, 2, "4"), (1, 2, "5")],
                   malas2=[(0, 1, m[0]), (0, 2, m[1]), (1, 2, m[2])],
                   lenki=[(0, "", 1), (1, "", 2), (2, "", 3)])


SATURS = [
    Sakums("Vai rotaļu auto ir līdzīgs īstajam?",
           zimejums=_pari(1.5, ("9", "6", "7,5")),
           paraksts="Modelis 1 : 43 - katrs izmērs 43 reizes mazāks.",
           fakti=["Līdzīgām figūrām forma vienāda, izmērs - citāds.",
                  "Leņķi paliek tie paši.",
                  "Visas malas mainās vienādu reižu skaitu."]),

    Doma("Līdzīgi trijstūri",
         "△ABC ∼ △A_1B_1C_1, ja ∠A = ∠A_1, ∠B = ∠B_1, ∠C = ∠C_1 un "
         "{A_1B_1|AB} = {B_1C_1|BC} = {A_1C_1|AC}.",
         soli=[
             "Zīme ∼ nozīmē «līdzīgs».",
             "Burtu secība pieraksta, kura virsotne atbilst kurai.",
             "Atbilstošās malas atrodas pretī vienādiem leņķiem.",
             "Vienādi trijstūri ir līdzīgi ar attiecību 1.",
         ]),

    Slidnis("Palielini trijstūri", [
        {"v": "× 1", "teksts": "Vienādi trijstūri: malas 6, 4, 5",
         "zim": _pari(1, ("6", "4", "5"))},
        {"v": "× 1,5", "teksts": "Malas 9, 6, 7,5 - leņķi nemainās",
         "zim": _pari(1.5, ("9", "6", "7,5"))},
        {"v": "× 2", "teksts": "Malas 12, 8, 10 - leņķi nemainās",
         "zim": _pari(2, ("12", "8", "10"))},
    ], ievads="Loki rāda vienādos leņķus. Kas mainās un kas ne?"),

    Varianti("Atbilstošie elementi", [
        {"jaut": "△ABC ∼ △KLM. Kurš leņķis atbilst ∠B?",
         "opcijas": ["∠L", "∠K", "∠M", "Nevar zināt"],
         "pareizi": 0, "padoms": "Otrā vieta nosaukumā."},
        {"jaut": "△ABC ∼ △KLM. Kura mala atbilst AC?",
         "opcijas": ["KM", "KL", "LM", "AC"],
         "pareizi": 0, "padoms": "1. un 3. burts."},
        {"jaut": "△PQR ∼ △XYZ. Kura attiecība ir pareiza?",
         "opcijas": ["{XY|PQ} = {YZ|QR}", "{XY|QR} = {YZ|PQ}",
                     "{XZ|PQ} = {YZ|QR}", "{PQ|YZ} = {QR|XY}"],
         "pareizi": 0, "padoms": "Atbilstošās malas."},
        {"jaut": "Vai divi jebkuri vienādmalu trijstūri ir līdzīgi?",
         "opcijas": ["Jā, vienmēr", "Nē", "Tikai vienādi", "Tikai lieli"],
         "pareizi": 0, "padoms": "Visi leņķi 60°, malas proporcionālas."},
    ]),

    Ievadi("Līdzīgo trijstūru malas", [
        {"jaut": "△ABC ∼ △A_1B_1C_1, AB = 4, A_1B_1 = 12. Cik reizes lielāks "
                 "ir otrais?", "atb": ["3"], "padoms": "12 : 4."},
        {"jaut": "Tie paši trijstūri, BC = 5. B_1C_1 = ?", "atb": ["15"],
         "padoms": "5 · 3."},
        {"jaut": "∠A = 40°, ∠B = 75°. ∠C_1 = ?°", "atb": ["65"],
         "padoms": "180 − 40 − 75."},
        {"jaut": "A_1C_1 = 21. AC = ?", "atb": ["7"], "padoms": "21 : 3."},
    ]),

    Pasaule("Modelis vitrīnā",
            Ievadi("", [
                {"jaut": "Auto garums 4,3 m, modelis 1 : 43. Modeļa garums "
                         "(cm)?", "atb": ["10"],
                 "padoms": "430 cm : 43."},
                {"jaut": "Modeļa riteņa diametrs 1,5 cm. Īstā riteņa "
                         "diametrs (cm)?", "atb": ["64,5"],
                 "padoms": "1,5 · 43."},
                {"jaut": "Vējstikla slīpums īstajam auto ir 30°. Modelim "
                         "(grādos)?", "atb": ["30"],
                 "padoms": "Leņķi nemainās."},
            ]),
            pavediens="tehnika",
            konteksts="Kolekcionāru modeļi ir precīzas līdzīgas kopijas: "
                      "katrs izmērs samazināts vienādi.",
            kapec="Leņķi paliek, garumi dalās ar vienu skaitli."),

    Kopsavilkums([
        "Definēju līdzīgus trijstūrus.",
        "No pieraksta nosaku atbilstošās virsotnes un malas.",
        "Zinu: leņķi vienādi, malas proporcionālas.",
    ]),

    Majas([
        "Atrodi mājās divus līdzīgus priekšmetus un izmēri tos.",
        "△DEF ∼ △PQR. Pieraksti visas vienādības un attiecības.",
        "Vai divi jebkuri taisnleņķa trijstūri ir līdzīgi? Pamato.",
    ]),
]
