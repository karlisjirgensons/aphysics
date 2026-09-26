# -*- coding: utf-8 -*-
"""7. klase, 37. stunda: «Kā pierādīt krustleņķu īpašību?»

Krustleņķi ir vienādi. Pierādījums lieto tikai blakusleņķu īpašību: abi
krustleņķi ir viena un tā paša leņķa blakusleņķi, tāpēc katrs ir 180°
mīnus tas pats. Tas ir pirmais pilnais pierādījums ar strukturētu pierakstu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā pierādīt krustleņķu īpašību?"

MERKIS = ("Pierādīsim, ka krustleņķi ir vienādi, un iemācīsimies pierakstīt "
          "pierādījumu.")


def _krusts(slipums):
    """Divas taisnes, kas krustojas; slīpums maina leņķu lielumu."""
    return geometrija(
        [("A", -4, 0), ("B", 4, 0), ("C", 2, 2 * slipums),
         ("D", -2, -2 * slipums), ("O", 0, 0, -90)],
        nogriezni=["AB", "CD"],
        lenki=[("BOC", "1"), ("COA", "2"), ("AOD", "3")])


SATURS = [
    Sakums("Pagriez taisni - kas paliek vienāds?",
           zimejums=_krusts(1.5),
           paraksts="∠1 un ∠3 ir krustleņķi.",
           fakti=["Mēri ar transportieri: ∠1 = ∠3 vienmēr.",
                  "Bet mērījums nav pierādījums - varbūt tā gadījās.",
                  "Pierādījums parāda, ka citādi nevar būt."]),

    Slidnis("Maini slīpumu", [
        {"v": "∠1 = 45°", "teksts": "∠2 = 135°, ∠3 = 45°",
         "zim": _krusts(1.0)},
        {"v": "∠1 = 60°", "teksts": "∠2 = 120°, ∠3 = 60°",
         "zim": _krusts(1.73)},
        {"v": "∠1 = 90°", "teksts": "∠2 = 90°, ∠3 = 90°",
         "zim": geometrija([("A", -4, 0), ("B", 4, 0), ("C", 0, 3),
                            ("D", 0, -3), ("O", 0, 0, -135)],
                           nogriezni=["AB", "CD"],
                           taisni=["BOC", "COA", "AOD"])},
    ], ievads="Katrā stāvoklī ∠1 un ∠3 ir vienādi."),

    Doma("Krustleņķi ir vienādi",
         "Teorēma: krustleņķi ir vienādi. Pierādījums: ∠1 un ∠3 abi ir ∠2 "
         "blakusleņķi, tāpēc ∠1 = 180° − ∠2 un ∠3 = 180° − ∠2. Labās puses "
         "ir vienādas, tātad ∠1 = ∠3.",
         soli=[
             "Dots: ∠1 un ∠3 - krustleņķi.",
             "Jāpierāda: ∠1 = ∠3.",
             "Atrodi leņķi, kas ir blakusleņķis abiem - ∠2.",
             "Izsaki abus ar ∠2 un salīdzini.",
         ]),

    Paraugs("Pierādījuma pieraksts",
            uzd="Pierādi, ka krustleņķi ∠1 un ∠3 ir vienādi.",
            soli=[
                ("∠1 + ∠2 = 180°", "(blakusleņķi)"),
                ("∠3 + ∠2 = 180°", "(blakusleņķi)"),
                ("∠1 = 180° − ∠2 un ∠3 = 180° − ∠2", "(no 1. un 2. rindas)"),
                ("∠1 = ∠3", "(vienādas labās puses)"),
            ],
            atbilde="Krustleņķi ir vienādi. Pierādīts."),

    Varianti("Pierādījuma soļi", [
        {"jaut": "Kāpēc pierādījumā izmanto ∠2?",
         "opcijas": ["Tas ir blakusleņķis gan ∠1, gan ∠3",
                     "Tas ir vislielākais", "Tas ir taisns",
                     "Tas ir krustleņķis ∠1"],
         "pareizi": 0,
         "padoms": "Tas savieno abus."},
        {"jaut": "Kura īpašība ir pierādījuma pamatā?",
         "opcijas": ["Blakusleņķu summa ir 180°",
                     "Trijstūra leņķu summa", "Paralēlu taišņu īpašība",
                     "Leņķa bisektrise"],
         "pareizi": 0,
         "padoms": "Tā ir vienīgā, ko līdz šim zinām."},
        {"jaut": "Vai pietiek izmērīt 10 krustleņķu pārus, lai pierādītu?",
         "opcijas": ["Nē - mērījumi neaptver visus gadījumus",
                     "Jā, 10 ir pietiekami", "Jā, ja visi vienādi",
                     "Pietiek ar vienu"],
         "pareizi": 0,
         "padoms": "Pierādījums der visiem gadījumiem."},
    ]),

    Ievadi("Lieto īpašību", [
        {"jaut": "∠1 = 48°. Cik grādu ir tā krustleņķis?",
         "atb": ["48"], "padoms": "Krustleņķi vienādi."},
        {"jaut": "∠1 = 48°. Cik grādu ir ∠2 (blakusleņķis)?",
         "atb": ["132"], "padoms": "180 − 48."},
        {"jaut": "Divu krustleņķu summa ir 100°. Cik grādu ir katrs?",
         "atb": ["50"], "padoms": "Tie ir vienādi."},
        {"jaut": "Trīs no četriem leņķiem kopā ir 250°. Cik grādu ir "
                 "ceturtais?",
         "atb": ["110"], "padoms": "Visi četri kopā 360°."},
    ]),

    Pasaule("Dzelzceļa pārbrauktuve",
            Ievadi("", [
                {"jaut": "Ceļš krusto sliedes 65° leņķī. Cik grādu ir "
                         "krustleņķis pretējā pusē?",
                 "atb": ["65"], "padoms": "Krustleņķi vienādi."},
                {"jaut": "Cik grādu ir blakusleņķis?",
                 "atb": ["115"], "padoms": "180 − 65."},
                {"jaut": "Cik no četriem leņķiem ir 65°?",
                 "atb": ["2"], "padoms": "Viens pāris krustleņķu."},
            ]),
            pavediens="celojums",
            konteksts="Ceļa inženieri norāda tikai vienu leņķi - pārējie "
                      "trīs izriet no krustleņķu un blakusleņķu īpašībām.",
            kapec="Viens leņķis nosaka visus četrus."),

    Kopsavilkums([
        "Zinu teorēmu: krustleņķi ir vienādi.",
        "Pierādu to ar blakusleņķu īpašību.",
        "Pierakstu pierādījumu ar pamatojumiem.",
        "Zinu, ka mērījums nav pierādījums.",
    ]),

    Majas([
        "Uzraksti pierādījumu no atmiņas.",
        "Izskaidro pierādījumu kādam, kas nemācās 7. klasē.",
        "Uzzīmē divas krustojošas taisnes un izmēri visus 4 leņķus.",
    ]),
]
