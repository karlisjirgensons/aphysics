# -*- coding: utf-8 -*-
"""7. klase, 82. stunda: «Kā no trijstūriem secināt par malām?»

Trijstūru vienādība ir rīks: kad tā pierādīta, visi atbilstošie elementi
ir vienādi. Tā pierāda, ka divi nogriežņi vai leņķi ir vienādi, - atrod
trijstūrus, kuros tie ir, un pierāda to vienādību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā no trijstūriem secināt par malām?"

MERKIS = ("No trijstūru vienādības secināsim par to elementu vienādību.")

_X = geometrija([("A", 0, 3), ("B", 6, -3), ("C", 0, -1.5),
                 ("D", 6, 1.5), ("O", 3, 0, 90)],
                nogriezni=["AB", "CD", "AC", "BD"],
                svitras=[("AO", 1), ("OB", 1), ("CO", 2), ("OD", 2)])

SATURS = [
    Sakums("Vienādi trijstūri - vienādas visas daļas",
           zimejums=_X,
           paraksts="Vai AC = BD? Atbilde slēpjas trijstūros AOC un BOD.",
           fakti=["Tieši izmērīt AC un BD nevar - tas nav pierādījums.",
                  "Bet AC un BD ir vienādu trijstūru atbilstošās malas.",
                  "Pierāda trijstūrus - iegūst malas."]),

    Doma("Vienādi trijstūri → vienādi elementi",
         "Lai pierādītu divu nogriežņu (vai leņķu) vienādību, atrod divus "
         "trijstūrus, kuros tie ir atbilstošie elementi, pierāda šo "
         "trijstūru vienādību un secina.",
         soli=[
             "Atrodi trijstūrus, kuros ir meklētie nogriežņi.",
             "Pierādi trijstūru vienādību pēc pazīmes.",
             "Pārbaudi, ka nogriežņi ir atbilstošie (vienādā vietā).",
             "Secini: (atbilstošie elementi vienādos trijstūros).",
         ],
         pieze="Pieraksta secība palīdz: △AOC = △BOD nozīmē A→B, O→O, "
               "C→D, tātad AC atbilst BD."),

    Paraugs("Pierādi, ka AC = BD",
            uzd="AB un CD krustojas punktā O, AO = OB, CO = OD. Pierādi, ka "
                "AC = BD.",
            soli=[
                ("AO = OB, CO = OD", "(dots)"),
                ("∠AOC = ∠BOD", "(krustleņķi)"),
                ("△AOC = △BOD", "(mlm)"),
                ("AC = BD", "(atbilstošās malas vienādos trijstūros)"),
            ],
            atbilde="AC = BD - pierādīts."),

    Varianti("Kas vienāds pēc △KLM = △PQR?", [
        {"jaut": "Kas atbilst malai KM?",
         "opcijas": ["PR", "PQ", "QR", "KL"],
         "pareizi": 0, "padoms": "1. un 3. burts."},
        {"jaut": "Kas atbilst ∠L?",
         "opcijas": ["∠Q", "∠P", "∠R", "∠M"],
         "pareizi": 0, "padoms": "2. burts."},
        {"jaut": "Kurš secinājums ir aplams?",
         "opcijas": ["KL = QR", "KL = PQ", "LM = QR", "∠M = ∠R"],
         "pareizi": 0, "padoms": "KL atbilst PQ."},
    ]),

    Ievadi("Aprēķini, izmantojot vienādību", [
        {"jaut": "△AOC = △BOD, AC = 4,5 cm. Cik cm ir BD?",
         "atb": ["4,5"], "padoms": "Atbilstošās malas."},
        {"jaut": "△AOC = △BOD, ∠OAC = 38°. Cik grādu ir ∠OBD?",
         "atb": ["38"], "padoms": "Atbilstošie leņķi."},
        {"jaut": "△ABC = △DEF, perimetrs P(ABC) = 19 cm, DE = 5 cm, "
                 "EF = 6 cm. Cik cm ir AC?",
         "atb": ["8"], "padoms": "19 − 5 − 6."},
    ]),

    Zimejums("Pierādītās malas",
             geometrija([("A", 0, 3), ("B", 6, -3), ("C", 0, -1.5),
                         ("D", 6, 1.5), ("O", 3, 0, 90)],
                        nogriezni=["AB", "CD"], izcelti=["AC", "BD"],
                        svitras=[("AC", 3), ("BD", 3)]),
             paskaidro="AC = BD - tas izrietēja no trijstūru vienādības."),

    Pasaule("Tilta balsti",
            Varianti("", [
                {"jaut": "Divi krustoti tērauda stieņi ir savienoti vidū. "
                         "Kāpēc attālumi starp to augšējiem un apakšējiem "
                         "galiem ir vienādi?",
                 "opcijas": ["Vienādi trijstūri pēc mlm",
                             "Stieņi ir no viena tērauda",
                             "Tā gadās", "Nav vienādi"],
                 "pareizi": 0, "padoms": "Puses vienādas, krustleņķi."},
                {"jaut": "Ko inženieris var nemērīt, ja pierādījis "
                         "vienādību?",
                 "opcijas": ["Otru attālumu - tas ir vienāds",
                             "Neko", "Stieņu garumu", "Leņķus pie O"],
                 "pareizi": 0, "padoms": "Atbilstošās malas."},
                {"jaut": "Šāda konstrukcija ir...",
                 "opcijas": ["šķēru lifts", "pakāpiens", "virve",
                             "ritenis"],
                 "pareizi": 0, "padoms": "Krustoti stieņi."},
            ]),
            pavediens="tehnika",
            konteksts="Šķēru pacēlājs strādā, jo krustoto stieņu trijstūri "
                      "vienmēr ir vienādi.",
            kapec="Vienādība dod vienādus attālumus bez mērīšanas."),

    Kopsavilkums([
        "No trijstūru vienādības secinu par malām un leņķiem.",
        "Atrodu atbilstošos elementus pēc burtu secības.",
        "Pierakstu pamatojumu «atbilstošie elementi».",
        "Izmantoju vienādību aprēķinos.",
    ]),

    Majas([
        "Pierādi, ka paralelogramā pretējās malas ir vienādas (ar "
        "diagonāli).",
        "Izdomā zīmējumu, kur divi nogriežņi ir vienādi un pierādi to.",
        "Uzraksti, kāpēc svarīga ir burtu secība pierakstā.",
    ]),
]
