# -*- coding: utf-8 -*-
"""2. klase, 42. stunda: «Kā pierakstīt stabiņā?» (atņemšana)

Atņemšana stabiņā: ja augšējais vienu cipars ir mazāks, «aizņemas» vienu
desmitu - virs vieniem pieraksta 10 un desmitu ciparu samazina par 1. Tas ir
tas pats sadalītais desmits, ko iepriekšējā stundā darīja ar kubiņiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, stabins)

TEMA = "Kā pierakstīt stabiņā?"

MERKIS = ("Šodien atņemsim divciparu skaitļus stabiņā un aprēķināsim "
          "starpību.")

SATURS = [
    Sakums("Kā atņemt stabiņā, ja augšā ir mazāk vienu?",
           zimejums=stabins(63, 28, "-", virs="10"),
           paraksts="Virs desmitiem - atzīme par sadalīto desmitu.",
           fakti=["No 3 nevar atņemt 8 - sadala desmitu.",
                  "13 − 8 = 5.",
                  "Desmiti: 5 − 2 = 3. Atbilde 35."]),

    Doma("Atņemšana stabiņā",
         "Sāk ar vieniem; ja augšā ir mazāk, aizņemas vienu desmitu.",
         soli=[
             "Uzraksti: vieni zem vieniem.",
             "Ja augšējais vienu cipars ir mazāks, pieliec tam 10.",
             "Desmitu ciparu samazini par 1 (atzīmē ar punktu).",
             "Atņem vienus, tad desmitus.",
         ]),

    Slidnis("72 − 45 soli pa solim", [
        {"v": "72 − 45", "teksts": "No 2 nevar atņemt 5.",
         "zim": stabins(72, 45, "-", rezultats=False)},
        {"v": "12 − 5 = 7", "teksts": "Aizņemas desmitu.",
         "zim": stabins(72, 45, "-", rezultats=False, virs="10")},
        {"v": "6 − 4 = 2", "teksts": "Desmitu palika 6. Atbilde 27.",
         "zim": stabins(72, 45, "-", virs="10")},
    ]),

    Ievadi("Rēķini stabiņā", [
        {"jaut": "Cik ir?", "zim": stabins(54, 27, "-", rezultats=False),
         "atb": ["27"], "padoms": "14 − 7, 4 − 2."},
        {"jaut": "Cik ir?", "zim": stabins(81, 36, "-", rezultats=False),
         "atb": ["45"], "padoms": "11 − 6, 7 − 3."},
        {"jaut": "Cik ir?", "zim": stabins(90, 42, "-", rezultats=False),
         "atb": ["48"], "padoms": "10 − 2, 8 − 4."},
        {"jaut": "Cik ir?", "zim": stabins(65, 38, "-", rezultats=False),
         "atb": ["27"], "padoms": "15 − 8, 5 − 3."},
        {"jaut": "Cik ir?", "zim": stabins(43, 19, "-", rezultats=False),
         "atb": ["24"], "padoms": "13 − 9, 3 − 1."},
        {"jaut": "Cik ir?", "zim": stabins(76, 58, "-", rezultats=False),
         "atb": ["18"], "padoms": "16 − 8, 6 − 5."},
    ], pamats=4),

    Varianti("Atrodi kļūdu", [
        {"jaut": "Ilze: 52 − 18 = 44. Kas aizmirsts?",
         "opcijas": ["samazināt desmitus par 1", "pārnest desmitu",
                     "nekas"], "pareizi": 0, "padoms": "Jābūt 34."},
        {"jaut": "Kas ir 40 − 17 vienu vietā?",
         "opcijas": ["3", "7", "0"], "pareizi": 0, "padoms": "10 − 7 = 3."},
    ]),

    Pasaule("Cik līdz virsotnei?",
            Ievadi("", [
                {"jaut": "Tūristi jau uzkāpuši 47 m. Kalns ir 82 m augsts. "
                         "Cik m vēl jākāpj?", "atb": ["35"], "mers": "m",
                 "padoms": "82 − 47 stabiņā."},
                {"jaut": "Pēc atpūtas uzkāpa vēl 18 m. Cik vēl atlicis?",
                 "atb": ["17"], "mers": "m", "padoms": "35 − 18."},
            ]),
            pavediens="celojums",
            konteksts="Tūristi kāpj Latvijas kalnos un skatu torņos.",
            kapec="Starpība pasaka, cik vēl palicis."),

    Kopsavilkums([
        "Atņemu divciparu skaitļus stabiņā.",
        "Aizņemos desmitu, ja augšā vienu ir mazāk.",
        "Neaizmirstu samazināt desmitus.",
    ]),

    Majas([
        "Izrēķini stabiņā: 71 − 38, 60 − 24, 93 − 47.",
        "Atzīmē aizņemtos desmitus.",
        "Pārbaudi ar saskaitīšanu.",
    ]),
]
