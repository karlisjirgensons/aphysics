# -*- coding: utf-8 -*-
"""7. klase, 98. stunda: «Kā pierāda leņķu summas teorēmu?»

Pierādījums: caur trijstūra virsotni novelk taisni, paralēlu pretējai
malai. Tad abi pārējie leņķi «pārceļas» uz virsotni kā iekšējie šķērsleņķi,
un visi trīs kopā veido izstieptu leņķi 180°.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā pierāda leņķu summas teorēmu?"

MERKIS = ("Pierādīsim trijstūra leņķu summas teorēmu, izmantojot "
          "paralēlas taisnes.")

_P = [("A", 0, 0), ("C", 7, 0), ("B", 2.5, 3.5, 90), ("_k", -1.5, 3.5),
      ("_l", 6.5, 3.5)]


def _pier(n):
    lenki = [("CAB", "∠1", 1), ("BCA", "∠3", 2), ("ABC", "∠2", 3)]
    taisnes, izc = [], []
    if n >= 2:
        taisnes = [("_k", "_l")]
    if n >= 3:
        lenki += [(("_k", "B", "A"), "∠1", 1)]
    if n >= 4:
        lenki += [(("C", "B", "_l"), "∠3", 2)]
    return geometrija(_P, nogriezni=["AB", "BC", "CA"], taisnes=taisnes,
                      lenki=lenki, izcelti=izc)


SATURS = [
    Sakums("Pārcel leņķus uz vienu virsotni",
           zimejums=_pier(4),
           paraksts="Taisne caur B ir paralēla AC.",
           fakti=["Pie B tagad ir trīs leņķi kopā.",
                  "Tie veido izstieptu leņķi - 180°.",
                  "Un tie ir tieši trijstūra trīs leņķi."]),

    Slidnis("Pierādījums soli pa solim", [
        {"v": "1. solis", "teksts": "Trijstūris ABC ar leņķiem 1, 2, 3.",
         "zim": _pier(1)},
        {"v": "2. solis", "teksts": "Caur B novelk taisni k ∥ AC.",
         "zim": _pier(2)},
        {"v": "3. solis",
         "teksts": "Pie B kreisajā pusē - leņķis, vienāds ar ∠1 "
                   "(šķērsleņķi).", "zim": _pier(3)},
        {"v": "4. solis",
         "teksts": "Labajā pusē - vienāds ar ∠3 (šķērsleņķi). Kopā 180°.",
         "zim": _pier(4)},
    ]),

    Doma("Pierādījuma ideja",
         "Caur virsotni B novelk taisni k, paralēlu AC. Pie B izveidojas "
         "izstiepts leņķis, ko sastāda trīs leņķi: viens ir ∠2, pārējie divi "
         "ir vienādi ar ∠1 un ∠3 kā iekšējie šķērsleņķi.",
         soli=[
             "Dots: △ABC. Jāpierāda: ∠1 + ∠2 + ∠3 = 180°.",
             "Konstrukcija: k ∥ AC caur B.",
             "Leņķi pie B uz taisnes k veido 180°.",
             "Aizstāj malējos ar ∠1 un ∠3.",
         ],
         pieze="Papildu līnija («palīgkonstrukcija») ir pierādījumu "
               "galvenais triks - tā pārvērš jaunu uzdevumu par zināmu."),

    Paraugs("Pieraksts",
            uzd="Pierādi, ka trijstūra ABC leņķu summa ir 180°.",
            soli=[
                ("Caur B novelkam k ∥ AC", "(konstrukcija)"),
                ("Leņķis starp k un BA = ∠1", "(iekšējie šķērsleņķi, k ∥ AC)"),
                ("Leņķis starp BC un k = ∠3", "(iekšējie šķērsleņķi, k ∥ AC)"),
                ("∠1 + ∠2 + ∠3 = 180°", "(veido izstieptu leņķi)"),
            ],
            atbilde="Teorēma pierādīta."),

    Varianti("Pierādījuma soļi", [
        {"jaut": "Kāpēc caur B velk tieši paralēlu taisni?",
         "opcijas": ["Lai izmantotu šķērsleņķu vienādību",
                     "Lai zīmējums būtu skaistāks",
                     "Tā vienmēr dara", "Lai iegūtu taisnu leņķi"],
         "pareizi": 0, "padoms": "Paralēlām - vienādi leņķi."},
        {"jaut": "Kura iepriekš pierādīta īpašība izmantota?",
         "opcijas": ["Iekšējie šķērsleņķi pie paralēlām ir vienādi",
                     "Krustleņķi vienādi", "Pazīme mmm",
                     "Trijstūra nevienādība"],
         "pareizi": 0, "padoms": "94. stunda."},
        {"jaut": "Kāpēc mērījums nav pierādījums?",
         "opcijas": ["Tas neaptver visus trijstūrus un ir neprecīzs",
                     "Mērījumi vienmēr kļūdaini",
                     "Transportieris ir aizliegts", "Tas ir pierādījums"],
         "pareizi": 0, "padoms": "Visi trijstūri."},
    ]),

    Pasaule("Uz sfēras - citādi!",
            Varianti("", [
                {"jaut": "Lidmašīna no Ziemeļpola lido uz ekvatoru, pa "
                         "ekvatoru ceturtdaļu apļa un atpakaļ uz polu. Visi "
                         "trīs leņķi ir 90°. Cik ir summa?",
                 "opcijas": ["270°", "180°", "90°", "360°"],
                 "pareizi": 0, "padoms": "3 · 90."},
                {"jaut": "Kāpēc uz sfēras teorēma nestrādā?",
                 "opcijas": ["Tur nav paralēlu taišņu kā plaknē",
                             "Tur nav trijstūru", "Leņķus nevar mērīt",
                             "Tā strādā"],
                 "pareizi": 0, "padoms": "Pierādījums lietoja paralēlas."},
                {"jaut": "Kur mūsu teorēma der?",
                 "opcijas": ["Plaknē (uz papīra, mazos laukos)",
                             "Uz visas Zemes", "Kosmosā visur",
                             "Nekur"],
                 "pareizi": 0, "padoms": "Plaknes ģeometrija."},
            ]),
            pavediens="kosmoss",
            konteksts="Lidmašīnu maršruti ir trijstūri uz sfēras, un tur "
                      "leņķu summa ir lielāka par 180°.",
            kapec="Teorēma balstās uz paralēlu taišņu aksiomu."),

    Kopsavilkums([
        "Pierādu leņķu summas teorēmu ar paralēlu taisni.",
        "Lietoju iekšējos šķērsleņķus.",
        "Zinu, kas ir palīgkonstrukcija.",
        "Zinu, ka teorēma der plaknē.",
    ]),

    Majas([
        "Uzraksti pierādījumu no atmiņas.",
        "Pierādi citādi: novelc paralēlu taisni caur C.",
        "Uzzīmē uz bumbas trijstūri ar trim taisniem leņķiem.",
    ]),
]
