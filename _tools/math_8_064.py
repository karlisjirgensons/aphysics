# -*- coding: utf-8 -*-
"""8. klase, 64. stunda: «Kā no taisnstūra iegūt trijstūra laukumu?»

Temata 8.4. sākums. Augstums sadala taisnstūri a × h divās daļās, un
trijstūris aizņem tieši pusi no katras - tātad S = {a · h|2}. Slīdnis
iekrāso abas puses pēc kārtas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kā no taisnstūra iegūt trijstūra laukumu?"

MERKIS = ("Iegūsim trijstūra laukuma formulu, izmantojot taisnstūra "
          "laukumu.")

_PUNKTI = [("A", 0, 0), ("B", 6, 0), ("C", 6, 4), ("D", 0, 4), ("E", 2, 4),
           ("H", 2, 0, 270)]


def _zim(iekrasot, augstums=True):
    nogr = ["AB", "BC", "CD", "DA", "AE", "BE"]
    if augstums:
        nogr.append("EH")
    return geometrija(_PUNKTI, nogriezni=nogr, taisni=["EHB"] if augstums
                      else [], iekrasot=iekrasot, malas=[("AB", "a")],
                      uzraksti=[(2.4, 2, "h")] if augstums else [])


SATURS = [
    Sakums("Kāpēc trijstūris ir puse no taisnstūra?",
           zimejums=_zim([("ABE", 0)]),
           paraksts="Augstums EH sadala taisnstūri divās daļās.",
           fakti=["S = {a · h|2} - mala reiz tai novilktais augstums, "
                  "dalīts ar 2.",
                  "Augstums ir perpendikuls no virsotnes pret malu.",
                  "Laukumu mēra kvadrātvienībās: cm², m²."]),

    Slidnis("Divas puses", [
        {"v": "a · h", "teksts": "Taisnstūris ap trijstūri",
         "zim": _zim([("ABCD", 0)], augstums=False)},
        {"v": "Augstums EH", "teksts": "Sadala taisnstūri divos",
         "zim": _zim([("ABE", 0)])},
        {"v": "AHE = {1|2} AHED", "teksts": "Kreisā daļa - tieši uz pusi",
         "zim": _zim([("AHE", 0), ("AHED", 1)])},
        {"v": "HBE = {1|2} HBCE", "teksts": "Labā daļa - arī uz pusi",
         "zim": _zim([("HBE", 0), ("HBCE", 1)])},
    ]),

    Doma("Trijstūra laukums",
         "Trijstūris ir puse no taisnstūra ar tādu pašu malu un augstumu.",
         soli=[
             "Novelc augstumu h pret malu a.",
             "Iedomājies taisnstūri a × h ap trijstūri.",
             "Augstums sadala taisnstūri divās daļās; katru trijstūris "
             "aizņem uz pusi.",
             "Tātad S = {a · h|2}.",
         ]),

    Paraugs("Aprēķini laukumu",
            uzd="Trijstūra mala ir 12 cm, augstums pret to - 7 cm. Aprēķini "
                "laukumu.",
            soli=[
                ("S = {a · h|2}", "Formula."),
                ("S = {12 · 7|2} = {84|2}", "Ievieto."),
                ("S = 42 cm²", "Mērvienība - kvadrātā."),
            ],
            atbilde="42 cm²"),

    Ievadi("Aprēķini laukumu", [
        {"jaut": "a = 10 cm, h = 6 cm. S (cm²)?", "atb": ["30"],
         "padoms": "{10 · 6|2}."},
        {"jaut": "a = 9 m, h = 4 m. S (m²)?", "atb": ["18"],
         "padoms": "{36|2}."},
        {"jaut": "a = 7 dm, h = 5 dm. S (dm²)?", "atb": ["17,5"],
         "padoms": "{35|2}."},
        {"jaut": "a = 2,4 cm, h = 1,5 cm. S (cm²)?", "atb": ["1,8"],
         "padoms": "{3,6|2}."},
        {"jaut": "Taisnstūris 8 cm × 5 cm. Trijstūrim ir tā pati mala un "
                 "augstums. S (cm²)?", "atb": ["20"], "padoms": "{40|2}."},
    ]),

    Varianti("Spried", [
        {"jaut": "Kā mainās laukums, ja augstumu divkāršo?",
         "opcijas": ["Divkāršojas", "Četrkāršojas", "Nemainās",
                     "Samazinās"],
         "pareizi": 0, "padoms": "h ir reizinātājs."},
        {"jaut": "Trijstūrim un taisnstūrim ir vienāda mala un augstums. "
                 "Trijstūra laukums ir...",
         "opcijas": ["puse no taisnstūra", "vienāds", "divreiz lielāks",
                     "trešdaļa"],
         "pareizi": 0, "padoms": "Skaties slīdni."},
        {"jaut": "Ko nozīmē h formulā S = {a · h|2}?",
         "opcijas": ["Augstumu pret malu a", "Jebkuru malu", "Perimetru",
                     "Diagonāli"],
         "pareizi": 0, "padoms": "Augstums un mala iet pārī."},
    ]),

    Pasaule("Jahtas bura",
            Ievadi("", [
                {"jaut": "Trijstūrveida buras pamats ir 3 m, augstums - 6 m. "
                         "Laukums (m²)?",
                 "atb": ["9"], "padoms": "{3 · 6|2}."},
                {"jaut": "Audums maksā 12 € par m². Cik € maksā buras "
                         "audums?",
                 "atb": ["108"], "padoms": "9 · 12."},
                {"jaut": "Šuvēm pieliek 10 % auduma. Cik m² jāpērk?",
                 "atb": ["9,9"], "padoms": "9 · 1,1."},
            ]),
            pavediens="sports",
            konteksts="Buras laukums nosaka, cik daudz vēja tā noķer un cik "
                      "auduma vajag.",
            kapec="Bura ir puse no taisnstūra ar tādu pašu pamatu un "
                  "augstumu."),

    Kopsavilkums([
        "Pamatoju trijstūra laukuma formulu ar taisnstūri.",
        "Aprēķinu laukumu pēc malas un tai novilktā augstuma.",
        "Lietoju kvadrātvienības.",
    ]),

    Majas([
        "Uzzīmē trīs dažādus trijstūrus ar malu 6 cm un augstumu 4 cm. "
        "Salīdzini laukumus.",
        "Izgriez trijstūri no papīra un saliec no diviem tādiem taisnstūri "
        "vai paralelogramu.",
        "Atrodi mājās trijstūrveida priekšmetu un aprēķini tā laukumu.",
    ]),
]
