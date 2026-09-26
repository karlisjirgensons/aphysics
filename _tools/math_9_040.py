# -*- coding: utf-8 -*-
"""9. klase, 40. stunda: «Kāpēc visi trijstūri ar vienādu leņķi ir līdzīgi?»

Trigonometrijas pamats ir 9.1. temata līdzība: diviem taisnleņķa
trijstūriem ar vienādu šauro leņķi ir divi vienādi leņķi (90° un α), tātad
tie ir līdzīgi, un malu attiecības ir vienādas neatkarīgi no izmēra.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, taisnlenka)

TEMA = "Kāpēc visi trijstūri ar vienādu leņķi ir līdzīgi?"

MERKIS = ("Secināsim un pamatosim, ka taisnleņķa trijstūri ar vienādu šauro "
          "leņķi ir līdzīgi.")

# Stars no A ar slīpumu 3 : 4 un trīs perpendikuli - trīs līdzīgi trijstūri.
_KAPNES = geometrija([("A", 0, 0), ("C_1", 4, 0), ("B_1", 4, 3),
                      ("C_2", 8, 0), ("B_2", 8, 6), ("C_3", 12, 0),
                      ("B_3", 12, 9)],
                     nogriezni=[("A", "C_3"), ("A", "B_3"),
                                ("C_1", "B_1"), ("C_2", "B_2"),
                                ("C_3", "B_3")],
                     taisni=[("A", "C_1", "B_1"), ("A", "C_2", "B_2"),
                             ("A", "C_3", "B_3")],
                     lenki=[(("C_3", "A", "B_3"), "α")])

SATURS = [
    Sakums("Kāpēc visām rampām ar vienu slīpumu ir viena «forma»?",
           zimejums=_KAPNES,
           paraksts="Trīs balsti zem vienas rampas - trīs līdzīgi trijstūri.",
           fakti=["Visiem ir taisns leņķis un kopīgais leņķis α.",
                  "Divi vienādi leņķi - trijstūri ir līdzīgi.",
                  "Tātad {B_1C_1|AB_1} = {B_2C_2|AB_2} = {B_3C_3|AB_3}."]),

    Doma("Viens leņķis nosaka formu",
         "Taisnleņķa trijstūri ar vienādu šauro leņķi ir līdzīgi, jo tiem ir "
         "divi vienādi leņķi: 90° un α.",
         soli=[
             "Trešais leņķis abiem: 90° − α.",
             "Līdzīgiem trijstūriem atbilstošo malu attiecības vienādas.",
             "Tātad jebkuras divu malu attiecība atkarīga TIKAI no α.",
         ],
         pieze="Tas ir trigonometrijas pamats: leņķis → skaitlis."),

    Slidnis("Maini izmēru, ne leņķi", [
        {"v": "mazs", "teksts": "Katetes 4 un 3, hipotenūza 5: 3 : 5 = 0,6",
         "zim": taisnlenka(4, 3, ("3", "4", "5"))},
        {"v": "vidējs", "teksts": "Katetes 8 un 6, hipotenūza 10: 6 : 10 = 0,6",
         "zim": taisnlenka(8, 6, ("6", "8", "10"))},
        {"v": "liels", "teksts": "Katetes 20 un 15, hipotenūza 25: "
                                 "15 : 25 = 0,6",
         "zim": taisnlenka(20, 15, ("15", "20", "25"))},
    ], ievads="Leņķis α visos vienāds. Kas notiek ar attiecību?"),

    Varianti("Līdzīgi vai nē?", [
        {"jaut": "Divi taisnleņķa trijstūri, katram viens leņķis 40°.",
         "opcijas": ["Līdzīgi", "Nelīdzīgi", "Vienādi", "Nevar zināt"],
         "pareizi": 0, "padoms": "90° un 40° abiem."},
        {"jaut": "Taisnleņķa trijstūri ar leņķiem 30° un 60°.",
         "opcijas": ["Līdzīgi - otram arī ir 30°", "Nelīdzīgi",
                     "Nevar zināt", "Tikai ja hipotenūzas vienādas"],
         "pareizi": 0, "padoms": "90 − 60 = 30."},
        {"jaut": "Divi taisnleņķa trijstūri ar vienādām hipotenūzām.",
         "opcijas": ["Ne obligāti līdzīgi", "Vienmēr līdzīgi",
                     "Vienmēr vienādi", "Nekad"],
         "pareizi": 0, "padoms": "Leņķi var atšķirties."},
    ]),

    Ievadi("Attiecības līdzīgos trijstūros", [
        {"jaut": "Trijstūrī katetes 6 un 8, hipotenūza 10. Līdzīgā trijstūrī "
                 "hipotenūza 25. Mazākā katete?", "atb": ["15"],
         "padoms": "k = 2,5."},
        {"jaut": "Pretkatetes un hipotenūzas attiecība pirmajam ir 0,6. "
                 "Otrajam (līdzīgam)?", "atb": ["0,6"],
         "padoms": "Attiecība nemainās."},
        {"jaut": "Rampas balstam 1 m horizontāli atbilst 0,25 m augstums. "
                 "Cik augsts balsts pie 3 m?", "atb": ["0,75"],
         "padoms": "0,25 · 3."},
    ]),

    Pasaule("Rampa skolas ieejai",
            Ievadi("", [
                {"jaut": "Rampas slīpums: 1 m pacēlums uz 12 m horizontāli. "
                         "Durvis ir 0,5 m augstumā. Cik m gara (horizontāli) "
                         "jābūt rampai?", "atb": ["6"],
                 "padoms": "{0,5|x} = {1|12}."},
                {"jaut": "Ja durvis 0,75 m augstumā?", "atb": ["9"],
                 "padoms": "0,75 · 12."},
            ]),
            pavediens="skola",
            konteksts="Ratiņkrēslam rampa nedrīkst būt stāva - projektā nosaka "
                      "slīpumu, tātad leņķi, nevis garumu.",
            kapec="Vienāds slīpums nozīmē līdzīgus trijstūrus."),

    Kopsavilkums([
        "Pamatoju, ka taisnleņķa trijstūri ar vienādu šauro leņķi ir līdzīgi.",
        "Secinu, ka malu attiecība atkarīga tikai no leņķa.",
        "Lietoju to rampas un kāpņu aprēķinos.",
    ]),

    Majas([
        "Uzzīmē trīs dažāda izmēra taisnleņķa trijstūrus ar leņķi 35°.",
        "Katrā izmēri pretkateti un hipotenūzu, aprēķini attiecību.",
        "Salīdzini rezultātus ar klasesbiedriem.",
    ]),
]
