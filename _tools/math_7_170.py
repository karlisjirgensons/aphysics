# -*- coding: utf-8 -*-
"""7. klase, 170. stunda: «Ko protu ģeometrijā?»

Gada ģeometrija vienā stundā: trijstūra leņķu summa, leņķi pie paralēlām
taisnēm, trijstūru vienādības pazīmes un pierādījums divās kolonnās.
Pierādījumu būvē pa rindai slīdnī, lai redz, ka katram apgalvojumam ir
savs «kāpēc».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, Zimejums, geometrija, paralelas,
                         restis)

TEMA = "Ko protu ģeometrijā?"

MERKIS = ("Atkārtosim leņķu sakarības, trijstūru vienādības pazīmes un "
          "pierādījuma pierakstu.")

# Divi nogriežņi krustojas un dala viens otru uz pusēm.
_X = geometrija([("A", 0, 0), ("C", 7, 3), ("B", 2, 3), ("D", 5, 0),
                 ("O", 3.5, 1.5)],
                nogriezni=["AC", "BD", "AB", "CD"],
                svitras=[("AO", 1), ("OC", 1), ("BO", 2), ("OD", 2)],
                lenki=[("AOB", ""), ("COD", "")])

_PIERADIJUMS = [
    ["apgalvojums", "pamatojums"],
    ["AO = OC", "dots"],
    ["BO = OD", "dots"],
    ["∠AOB = ∠COD", "krustleņķi"],
    ["△AOB = △COD", "mlm"],
    ["AB = CD", "atbilstošās malas"],
]


def _lidz(n):
    """Pierādījuma tabula līdz n. rindai - lai slīdnī tā aug pa rindai."""
    return restis(_PIERADIJUMS[:n + 1])


SATURS = [
    Sakums("Trīs rīki visai gada ģeometrijai",
           zimejums=geometrija([("A", 0, 0), ("B", 6, 0), ("C", 2, 3.5)],
                               nogriezni=["AB", "BC", "CA"],
                               lenki=[("BAC", "60°"), ("CBA", "40°"),
                                      ("ACB", "?")]),
           paraksts="∠C = 180° − 60° − 40° = 80°.",
           fakti=["Trijstūra leņķu summa ir 180°.",
                  "Pie paralēlām taisnēm leņķi ir vienādi vai papildina "
                  "līdz 180°.",
                  "Vienādus trijstūrus pierāda ar mlm, lml vai mmm."]),

    Doma("Kā sākt ģeometrijas uzdevumu",
         "Ģeometrijā atbildi neuzmin no zīmējuma - katru skaitli un katru "
         "vienādību pamato ar likumu.",
         soli=[
             "Uzzīmē vai pārzīmē figūru un atzīmē doto.",
             "Meklē trijstūri (180°) vai paralēlas taisnes (leņķu pāri).",
             "Vienādus elementus atzīmē ar svītrām un lokiem.",
             "Pieraksti divās kolonnās: apgalvojums un pamatojums.",
         ],
         pieze="Astotajā klasē tie paši rīki pierādīs četrstūru īpašības un "
               "Pitagora teorēmu."),

    Ievadi("Aprēķini leņķi", [
        {"jaut": "Trijstūrī divi leņķi ir 48° un 67°. Cik grādu ir "
                 "trešais?",
         "atb": ["65", "65°"], "padoms": "180 − 48 − 67."},
        {"jaut": "Vienādsānu trijstūrī virsotnes leņķis ir 40°. Cik grādu "
                 "ir leņķis pie pamata?",
         "atb": ["70", "70°"], "padoms": "(180 − 40) : 2."},
        {"jaut": "a ∥ b, šķērsleņķis ∠3 = 65°. Cik grādu ir ∠5?",
         "atb": ["65", "65°"], "padoms": "Šķērsleņķi ir vienādi."},
        {"jaut": "a ∥ b, ∠5 = 70°. Cik grādu ir vienpusleņķis ∠4?",
         "atb": ["110", "110°"], "padoms": "180 − 70."},
        {"jaut": "Trijstūrī ∠A = 50°, ∠C = 60°. Cik grādu ir ārējais leņķis "
                 "pie B?",
         "atb": ["110", "110°"], "padoms": "Ārējais = ∠A + ∠C."},
    ], pamats=3),

    Zimejums("Atceries leņķu pārus",
             paralelas(radit=(3, 4, 5), uzraksti={3: "65°", 4: "115°",
                                                  5: "65°"},
                       loki={3: 2, 5: 2}, slipums=65),
             paskaidro="∠3 = ∠5 (šķērsleņķi), ∠4 + ∠5 = 180° "
                       "(vienpusleņķi)."),

    Varianti("Kura pazīme der?", [
        {"jaut": "AB = DE, BC = EF, ∠B = ∠E. △ABC = △DEF pēc...",
         "opcijas": ["mlm", "lml", "mmm", "nevar pierādīt"],
         "pareizi": 0, "padoms": "Leņķis starp abām malām."},
        {"jaut": "AB = DE, ∠A = ∠D, ∠B = ∠E. △ABC = △DEF pēc...",
         "opcijas": ["lml", "mlm", "mmm", "nevar pierādīt"],
         "pareizi": 0, "padoms": "Mala starp abiem leņķiem."},
        {"jaut": "AB = DE, BC = EF, CA = FD. △ABC = △DEF pēc...",
         "opcijas": ["mmm", "mlm", "lml", "nevar pierādīt"],
         "pareizi": 0, "padoms": "Trīs malas."},
        {"jaut": "Visi trīs leņķi vienādi. Vai trijstūri noteikti ir "
                 "vienādi?",
         "opcijas": ["Nē - viens var būt lielāks", "Jā, pēc lll",
                     "Jā, pēc lml", "Jā, pēc mmm"],
         "pareizi": 0, "padoms": "Vajag vismaz vienu malu."},
    ]),

    Zimejums("Pierādāmais", _X,
             paskaidro="Dots: AO = OC, BO = OD. Pierādīt: AB = CD."),

    Slidnis("Pierādījums pa rindai", [
        {"v": "Dots", "teksts": "Pirmās divas rindas nāk no nosacījuma",
         "zim": _lidz(2)},
        {"v": "Leņķis", "teksts": "Leņķis starp abām malām - krustleņķi",
         "zim": _lidz(3)},
        {"v": "Pazīme", "teksts": "Mala, leņķis, mala - mlm",
         "zim": _lidz(4)},
        {"v": "Secinājums", "teksts": "Vienādos trijstūros atbilstošās malas "
                                      "ir vienādas",
         "zim": _lidz(5)},
    ], ievads="Katrai rindai - apgalvojums un pamatojums."),

    Pasaule("Saliekamais krēsls",
            Ievadi("", [
                {"jaut": "Krēsla kājas krustojas to vidū. Apakšā kāju gali ir "
                         "40 cm viens no otra. Cik cm ir starp kāju galiem "
                         "augšā?",
                 "atb": ["40"], "padoms": "Tāpat kā AB = CD."},
                {"jaut": "Abas kājas ar grīdu veido 65° leņķi. Cik grādu ir "
                         "leņķis starp kājām apakšējā trijstūrī?",
                 "atb": ["50", "50°"], "padoms": "180 − 65 − 65."},
                {"jaut": "Cik grādu ir leņķis starp kājām augšējā "
                         "trijstūrī?",
                 "atb": ["50", "50°"], "padoms": "Krustleņķi."},
                {"jaut": "Cik grādu ir leņķis starp kāju un sēdekli, ja "
                         "sēdeklis ir paralēls grīdai?",
                 "atb": ["65", "65°"], "padoms": "Šķērsleņķi."},
            ]),
            pavediens="maja",
            konteksts="Saliekamā krēsla kājas ir tieši pierādītā figūra: "
                      "divi nogriežņi, kas dala viens otru uz pusēm.",
            kapec="Tāpēc sēdeklis ir tikpat plats kā kāju atstatums "
                  "apakšā un paliek līmenī."),

    Kopsavilkums([
        "Aprēķinu trijstūra leņķus un ārējo leņķi.",
        "Lietoju leņķu pārus pie paralēlām taisnēm.",
        "Izvēlos pareizo vienādības pazīmi.",
        "Pierakstu pierādījumu divās kolonnās.",
    ]),

    Majas([
        "Uzzīmē divas paralēlas taisnes ar krustotāju un atzīmē visus "
        "vienādos leņķus.",
        "Pierādi: ja AO = OC un BO = OD, tad ∠BAO = ∠DCO.",
        "Atrodi mājās vēl vienu priekšmetu ar vienādiem trijstūriem.",
    ]),
]
