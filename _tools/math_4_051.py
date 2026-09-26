# -*- coding: utf-8 -*-
"""4. klase, 51. stunda: «Kā pārbaudīt, vai malas ir perpendikulāras?»

Uzstūris ir taisnā leņķa paraugs. To pieliek daudzstūra virsotnei: ja abas
malas sakrīt ar uzstūra malām, tās ir perpendikulāras. Stundā pārbauda
daudzstūrus rūtiņās un saskaita taisnos leņķus.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         figura)

TEMA = "Kā pārbaudīt, vai malas ir perpendikulāras?"

MERKIS = ("Ar uzstūri pārbaudīsim, vai daudzstūra malas ir "
          "perpendikulāras.")

SATURS = [
    Sakums("Vai durvis ir taisnas?",
           zimejums=figura([(0, 0), (6, 0), (6, 10), (0, 10)],
                           uzraksti=[(0.8, 0.8, "90°"), (5.2, 0.8, "90°"),
                                     (5.2, 9.2, "90°"), (0.8, 9.2, "90°")],
                           platums=7, augstums=11),
           paraksts="Ja visi stūri ir taisni, durvis aizveras cieši.",
           fakti=["Galdnieks pārbauda stūrus ar uzstūri.",
                  "Ja stūris nav taisns, durvīs paliek sprauga."]),

    Doma("Uzstūris ir taisnā leņķa paraugs",
         "Ja uzstūra divas malas pilnīgi sakrīt ar daudzstūra divām malām, "
         "malas ir perpendikulāras.",
         soli=[
             "Pieliec uzstūra taisno stūri daudzstūra virsotnei.",
             "Vienu uzstūra malu savieto ar vienu malu.",
             "Paskaties uz otru malu: vai tā sakrīt ar uzstūri?",
             "Ja sakrīt - malas ir perpendikulāras; ja nē - nav.",
         ],
         pieze="Rūtiņās perpendikularitāti bieži redz: mala pa rūtiņu līniju "
               "horizontāli un otra - vertikāli."),

    Zimejums("Kuri stūri ir taisni?",
             figura([(0, 0), (8, 0), (8, 4), (3, 6), (0, 4)],
                    uzraksti=[(0.7, 0.7, "A"), (7.3, 0.7, "B"),
                              (7.3, 4.2, "C"), (3, 5.2, "D"),
                              (0.7, 4.2, "E")],
                    platums=9, augstums=7),
             paskaidro="A un B ir taisni leņķi. Pie C, D un E malas nav "
                       "perpendikulāras.",
             ievads="Piecstūris rūtiņās - pārbaudi katru virsotni."),

    Paraugs("Pārbaudi piecstūri",
            uzd="Cik taisnu leņķu ir piecstūrim ABCDE?",
            soli=[
                ("A: horizontāla un vertikāla mala", "Taisns."),
                ("B: horizontāla un vertikāla mala", "Taisns."),
                ("C, D, E: viena mala slīpa", "Nav taisni."),
            ],
            atbilde="2 taisni leņķi"),

    Varianti("Taisns vai nav?", [
        {"jaut": "Kvadrātam ir cik taisnu leņķu?",
         "opcijas": ["4", "2", "0", "3"], "pareizi": 0,
         "padoms": "Visi stūri taisni."},
        {"jaut": "Uzstūra mala sakrīt ar vienu malu, bet otra mala atkāpjas. "
                 "Malas ir...",
         "opcijas": ["nav perpendikulāras", "perpendikulāras", "paralēlas"],
         "pareizi": 0, "padoms": "Abām jāsakrīt."},
        {"jaut": "Vai trijstūrim var būt divi taisni leņķi?",
         "opcijas": ["nē", "jā"], "pareizi": 0,
         "padoms": "Pamēģini uzzīmēt - malas neaizvērsies."},
        {"jaut": "Ko izmanto taisna leņķa pārbaudei?",
         "opcijas": ["uzstūri", "cirkuli", "svarus", "termometru"],
         "pareizi": 0, "padoms": "Tam ir taisns stūris."},
    ], pamats=4),

    Ievadi("Saskaiti taisnos leņķus", [
        {"jaut": "Cik taisnu leņķu ir taisnstūrim?", "atb": ["4"],
         "padoms": "Visi četri."},
        {"jaut": "Cik taisnu leņķu ir burtam «L»?", "atb": ["1"],
         "padoms": "Viens stūris."},
        {"jaut": "Cik taisnu leņķu ir burtam «T» (ap krustpunktu)?",
         "atb": ["2"], "padoms": "Pa kreisi un pa labi no kājas."},
        {"jaut": "Cik taisnu leņķu ir zīmei «+»?", "atb": ["4"],
         "padoms": "Četri ap centru."},
    ]),

    Pasaule("Galdnieka darbnīca",
            Ievadi("", [
                {"jaut": "Plauktam 4 stūri, katrā jāpārbauda taisnais leņķis. "
                         "Cik pārbaužu 6 plauktiem?",
                 "atb": ["24"], "padoms": "6 · 4."},
                {"jaut": "No 24 stūriem 3 nebija taisni. Cik bija taisni?",
                 "atb": ["21"], "padoms": "24 − 3."},
                {"jaut": "Katra labošana aizņem 15 min. Cik minūšu 3 "
                         "labošanām?",
                 "atb": ["45"], "padoms": "3 · 15."},
                {"jaut": "Kastei ir 6 skaldnes pa 4 stūriem. Cik stūru "
                         "jāpārbauda visām skaldnēm?",
                 "atb": ["24"], "padoms": "6 · 4."},
            ]),
            pavediens="maja",
            konteksts="Mēbeles ar šķībiem stūriem ļodzās - tāpēc galdnieks "
                      "pārbauda katru stūri.",
            kapec="Taisns leņķis padara mēbeli stabilu."),

    Petijums("Uzstūra pārbaude",
             soli=[
                 "Uzzīmē rūtiņās 3 dažādus četrstūrus.",
                 "Ar uzstūri pārbaudi katru virsotni.",
                 "Taisnos leņķus atzīmē ar kvadrātiņu.",
                 "Pieraksti, cik taisnu leņķu katram četrstūrim.",
             ],
             vajag="uzstūris, rūtiņu lapa",
             secinajums="Četrstūrim var būt 0, 1, 2 vai 4 taisni leņķi - bet "
                        "ne tieši 3."),

    Kopsavilkums([
        "Pārbaudu perpendikularitāti ar uzstūri.",
        "Atzīmēju taisnu leņķi ar kvadrātiņu.",
        "Saskaitu taisnos leņķus daudzstūrī.",
    ]),

    Majas([
        "Pārbaudi ar burtnīcas stūri 5 priekšmetu stūrus mājās.",
        "Uzzīmē četrstūri ar tieši 2 taisniem leņķiem.",
        "Padomā: kāpēc četrstūrim nevar būt tieši 3 taisni leņķi?",
    ]),
]
