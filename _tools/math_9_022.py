# -*- coding: utf-8 -*-
"""9. klase, 22. stunda: «Kādi leņķi ir trapecē?»

Sānu mala ir krustotāja divām paralēlām taisnēm (pamatiem), tāpēc leņķi
pie vienas sānu malas ir iekšējie vienpusleņķi: to summa ir 180°. No šī
viena fakta izriet visi trapeces leņķu aprēķini.
"""

from math_saturs import (TRAPECES_MALAS, Doma, Ievadi, Kopsavilkums, Majas,
                         Paraugs, Pasaule, Sakums, Varianti, geometrija,
                         trapece)

TEMA = "Kādi leņķi ir trapecē?"

MERKIS = ("Aprēķināsim trapeces leņķus, lietojot paralēlu taišņu leņķu "
          "sakarības.")


def _zim(uzraksti):
    """Trapece ar leņķu uzrakstiem {virsotne: teksts}."""
    lenki = {"A": "BAD", "B": "CBA", "C": "DCB", "D": "ADC"}
    return geometrija(trapece(10, 5, 4, nobide=1.5),
                      nogriezni=TRAPECES_MALAS,
                      lenki=[(lenki[v], t) for v, t in uzraksti.items()])


SATURS = [
    Sakums("70° apakšā - cik augšā?",
           zimejums=_zim({"A": "70°", "D": "?"}),
           paraksts="AB ∥ DC, AD - krustotāja.",
           fakti=["Leņķi pie vienas sānu malas kopā ir 180°.",
                  "Tie ir iekšējie vienpusleņķi.",
                  "Visu četru leņķu summa - 360°."]),

    Doma("Leņķi pie sānu malas",
         "Trapecē ∠A + ∠D = 180° un ∠B + ∠C = 180°.",
         soli=[
             "Atrodi sānu malu, pie kuras ir zināmais leņķis.",
             "Otrs leņķis pie tās pašas sānu malas = 180° − zināmais.",
             "Vienādsānu trapecē vēl ∠A = ∠B, ∠C = ∠D.",
             "Pārbaude: visu leņķu summa 360°.",
         ],
         pieze="Leņķi pie viena pamata (∠A un ∠B) kopā NAV 180° - ja vien "
               "trapece nav īpaša."),

    Paraugs("Vienādsānu trapece",
            uzd="Vienādsānu trapecē ABCD (AB ∥ DC) ∠A = 64°. Atrodi pārējos "
                "leņķus.",
            soli=[
                ("∠B = ∠A = 64°", "Vienādsānu trapecē pamata leņķi vienādi."),
                ("∠D = 180° − 64° = 116°", "Vienpusleņķi pie AD."),
                ("∠C = ∠D = 116°", "Otra pamata leņķi."),
                ("64° + 64° + 116° + 116° = 360°", "Pārbaude."),
            ],
            atbilde="∠B = 64°, ∠C = ∠D = 116°"),

    Ievadi("Aprēķini leņķi", [
        {"jaut": "∠A = 50°. ∠D = ?°", "atb": ["130"],
         "padoms": "180 − 50."},
        {"jaut": "∠C = 105°. ∠B = ?°", "atb": ["75"],
         "padoms": "Pie sānu malas BC."},
        {"jaut": "Vienādsānu: ∠D = 125°. ∠A = ?°", "atb": ["55"],
         "padoms": "180 − 125."},
        {"jaut": "Taisnleņķa: ∠A = 90°, ∠B = 48°. ∠C = ?°", "atb": ["132"],
         "padoms": "180 − 48."},
        {"jaut": "∠A : ∠D = 2 : 3. ∠A = ?°", "atb": ["72"],
         "padoms": "180 : 5 · 2."},
        {"jaut": "Vienādsānu: ∠A ir par 40° mazāks nekā ∠D. ∠A = ?°",
         "atb": ["70"], "padoms": "x + x + 40 = 180."},
    ], pamats=4),

    Varianti("Vai tāda trapece ir iespējama?", [
        {"jaut": "Leņķi 60°, 120°, 60°, 120°, ejot pēc kārtas.",
         "opcijas": ["Nē - tas ir paralelograms", "Jā, vienādsānu",
                     "Jā, taisnleņķa", "Jā, jebkura"],
         "pareizi": 0, "padoms": "Pretējie leņķi vienādi."},
        {"jaut": "Leņķi pēc kārtas 70°, 70°, 110°, 110°.",
         "opcijas": ["Jā, vienādsānu trapece", "Nē", "Paralelograms",
                     "Taisnstūris"],
         "pareizi": 0, "padoms": "70 + 110 pie katras sānu malas."},
        {"jaut": "Trapecei trīs leņķi ir 90°.",
         "opcijas": ["Nē - ceturtais arī 90°, tas ir taisnstūris",
                     "Jā", "Tikai vienādsānu", "Tikai liela"],
         "pareizi": 0, "padoms": "Summa 360°."},
    ]),

    Pasaule("Jumta slīpums",
            Ievadi("", [
                {"jaut": "Mansarda jumta šķērsgriezums ir vienādsānu trapece. "
                         "Apakšā jumta slīpne ar grīdu veido 60°. Kāds leņķis "
                         "ir augšā pie griestiem (°)?", "atb": ["120"],
                 "padoms": "180 − 60."},
                {"jaut": "Ja slīpums būtu 45°, leņķis pie griestiem (°)?",
                 "atb": ["135"], "padoms": "180 − 45."},
            ]),
            pavediens="maja",
            konteksts="Mansarda istabas šķērsgriezums ir trapece: grīda, "
                      "griesti un slīpās sienas.",
            kapec="Galdnieks zāģē sijas pēc šiem leņķiem."),

    Kopsavilkums([
        "Lietoju: leņķi pie sānu malas kopā 180°.",
        "Lietoju vienādsānu trapeces leņķu īpašību.",
        "Pārbaudu ar leņķu summu 360°.",
    ]),

    Majas([
        "Vienādsānu trapecē viens leņķis ir 3 reizes lielāks par otru. "
        "Atrodi visus leņķus.",
        "Taisnleņķa trapecē šaurais leņķis 35°. Atrodi pārējos.",
        "Paskaidro, kāpēc trapecei nevar būt tieši trīs šauri leņķi.",
    ]),
]
