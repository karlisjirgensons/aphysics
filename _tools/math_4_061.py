# -*- coding: utf-8 -*-
"""4. klase, 61. stunda: «Cik leņķu ir zīmējumā?»

Mikrotemata noslēgums un mazs kombinatorikas uzdevums: no vienas virsotnes
3 stari veido 3 leņķus, 4 stari - 6 leņķus. Lai neviens nepaliek
nepamanīts, leņķus uzskaita sistemātiski - no katra stara pa kārtai.
Tā pati uzskaites prasme vajadzīga vēlāk kombinatorikā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, lenkis, restis)

TEMA = "Cik leņķu ir zīmējumā?"

MERKIS = ("Saskatīsim visus leņķus figūrā ar trim vai četriem stariem un "
          "pārliecināsimies, ka apskatīti visi.")

SATURS = [
    Sakums("Cik leņķu te ir? Trīs vai vairāk?",
           zimejums=lenkis([(0, "A"), (50, "B"), (120, "C")],
                           loki=[(0, 50, ""), (50, 120, "")]),
           paraksts="Stari OA, OB, OC no viena punkta O.",
           fakti=["Pirmajā mirklī redz divus leņķus.",
                  "Bet ir arī trešais - ∠AOC, kas aptver abus."]),

    Doma("Skaiti sistemātiski - pa pāriem",
         "Katrs staru pāris veido vienu leņķi; uzskaiti visus pārus kārtībā, "
         "lai neviens nepazūd.",
         soli=[
             "Nosauc starus pēc kārtas: A, B, C, D.",
             "Pāri ar A: AB, AC, AD.",
             "Pāri ar B (bez A): BC, BD.",
             "Pāri ar C (bez A, B): CD. Pavisam 3 + 2 + 1 = 6.",
         ],
         pieze="3 stari: 2 + 1 = 3 leņķi. 5 stari: 4 + 3 + 2 + 1 = 10."),

    Paraugs("Trīs stari",
            uzd="No punkta O iziet stari OA, OB, OC. Cik leņķu?",
            soli=[
                ("∠AOB, ∠AOC", "Pāri ar A."),
                ("∠BOC", "Pāri ar B."),
                ("2 + 1 = 3", None),
            ],
            atbilde="3 leņķi"),

    Slidnis("Kā aug leņķu skaits",
            soli=[
                {"v": "2 stari → 1 leņķis",
                 "zim": lenkis([(0, ""), (60, "")]), "teksts": "1"},
                {"v": "3 stari → 3 leņķi",
                 "zim": lenkis([(0, ""), (60, ""), (120, "")]),
                 "teksts": "2 + 1"},
                {"v": "4 stari → 6 leņķi",
                 "zim": lenkis([(0, ""), (45, ""), (90, ""), (150, "")]),
                 "teksts": "3 + 2 + 1"},
                {"v": "5 stari → 10 leņķu",
                 "zim": lenkis([(0, ""), (35, ""), (70, ""), (110, ""),
                                (160, "")]),
                 "teksts": "4 + 3 + 2 + 1"},
            ],
            ievads="Katrs jauns stars pievieno tik leņķu, cik staru jau bija."),

    Ievadi("Saskaiti leņķus", [
        {"jaut": "Cik leņķu veido 3 stari no vienas virsotnes?",
         "atb": ["3"], "padoms": "2 + 1."},
        {"jaut": "Cik leņķu veido 4 stari?", "atb": ["6"],
         "padoms": "3 + 2 + 1."},
        {"jaut": "Cik leņķu veido 5 stari?", "atb": ["10"],
         "padoms": "4 + 3 + 2 + 1."},
        {"jaut": "Cik leņķu veido 6 stari?", "atb": ["15"],
         "padoms": "5 + 4 + 3 + 2 + 1."},
    ]),

    Varianti("Vai visi uzskaitīti?", [
        {"jaut": "Stari OA, OB, OC, OD. Kurš leņķis *nav* sarakstā: ∠AOB, "
                 "∠AOC, ∠AOD, ∠BOC, ∠COD?",
         "opcijas": ["∠BOD", "∠AOB", "∠COD", "∠DOA"], "pareizi": 0,
         "padoms": "Pāri ar B: BC un BD."},
        {"jaut": "Kāpēc ∠AOB un ∠BOA skaita kā vienu?",
         "opcijas": ["tas ir tas pats leņķis", "tie ir dažādi",
                     "tā nevajag"], "pareizi": 0,
         "padoms": "Tie paši stari."},
        {"jaut": "Ja ∠AOB = 30° un ∠BOC = 40°, cik ir ∠AOC?",
         "opcijas": ["70°", "10°", "30°", "40°"], "pareizi": 0,
         "padoms": "Lielais leņķis = abu summa."},
    ]),

    Pasaule("Velosipēda ritenis",
            Ievadi("", [
                {"jaut": "Riteņa centrā satiekas 4 spieķi. Cik leņķu starp "
                         "tiem var saskaitīt (pa pāriem)?",
                 "atb": ["6"], "padoms": "3 + 2 + 1."},
                {"jaut": "Ja 4 spieķi sadala apli vienādi, cik grādu starp "
                         "blakus spieķiem?",
                 "atb": ["90"], "padoms": "360 : 4."},
                {"jaut": "Ja spieķu ir 6 un tie vienādi, cik grādu starp "
                         "blakus spieķiem?",
                 "atb": ["60"], "padoms": "360 : 6."},
                {"jaut": "Picu sagriež 8 vienādos gabalos. Cik grādu katram "
                         "gabalam?",
                 "atb": ["45"], "padoms": "360 : 8."},
            ]),
            pavediens="tehnika",
            konteksts="Riteņa spieķi, picas griezumi un pulksteņa rādītāji - "
                      "visi ir stari no viena centra.",
            kapec="Sistemātiska skaitīšana neļauj neko palaist garām."),

    Kopsavilkums([
        "Saskatu visus leņķus figūrā ar vairākiem stariem.",
        "Skaitu sistemātiski pa pāriem.",
        "Zinu: 3 stari - 3 leņķi, 4 stari - 6 leņķi.",
    ]),

    Majas([
        "Uzzīmē 5 starus no viena punkta un uzraksti visus 10 leņķus.",
        "Saskaiti leņķus starp velosipēda riteņa spieķiem.",
        "Izdomā, cik rokasspiedienu būs, ja sasveicinās 4 cilvēki.",
    ], ievads="Tā pati skaitīšana der rokasspiedieniem: pāri, nevis leņķi."),
]
