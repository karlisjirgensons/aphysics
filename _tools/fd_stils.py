# -*- coding: utf-8 -*-
"""Formatīvā darba lapas noformējuma vērtības - viena vieta abiem skatiem.

Ekrāna lapa un lejupielādētais Word fails ir viens un tas pats dokuments
divās vidēs, tāpēc krāsas, fonts, lapas izmērs un burtu lielumi dzīvo te
(SRP), un abas puses tos lasa no viena avota (DRY).

Vērtības nāk no pd_common.py - tā, lai ģenerētā lapa izskatītos tieši tāpat
kā ar Python uzbūvētie pārbaudes darbi un ātrie testi.
"""

import json

import mathfmt as MF
import pd_common as C

TEKSTA_PLATUMS = C.TEKSTA_PLATUMS      # cm
AILES = 6                              # cik jautājumu vienā atbilžu blokā

# Word puses noformējums. Piemales: augša, labā, apakša, kreisā (cm).
DOCX = {
    "font": "Calibri",
    "size": 11,
    "page": [21.0, 29.7],
    "margin": [1.2, 1.5, 1.2, 1.5],
}

KRASAS = {
    "navy": str(C.NAVY),               # virsraksti un tabulu galvenes
    "grey": str(C.GREY),               # palīgteksts
    "white": str(C.WHITE),
    "box": "EEF2F8",                   # ATGĀDNE kastes fons
}

# Burtu lielumi (pt) - tie paši, kas at_common.py darba lapā.
IZMERI = {
    "meta": 9.0, "h1": 16.0, "h2": 13.0, "note": 9.5, "jaut": 10.0,
    "sec": 12.0, "mazs": 9.0, "vid": 10.5,
}

# Kvadrātsaknes zīme. To zīmē pati lapa (mathfmt.root_pts), nevis ņem no
# fonta, tāpēc vinkuls turpinās tieši no zīmes stūra un pāri paliek VISA
# izteiksme (rules_pd.txt). Tā pati zīme ir prezentācijās (html_deck.py).
ROOT_EM = MF.root_em([("t", "")])
SAKNE = {"w": MF.root_pts(ROOT_EM)[0], "svg": MF.root_svg(ROOT_EM)}

PLATUMI = {
    "veidlapa": [5.5, 5.5, 3.5, 3.5],  # Vārds, Uzvārds, Klase, Datums
    "struktura": [2.2, 13.2, 2.6],     # Jaut. | Sasniedzamais rezultāts | St.
}


def js():
    """Vērtības kā JavaScript objekts - to ielasa DOCX un PAPER moduļi."""
    return "window.FD_STILS=%s;" % json.dumps({
        "docx": DOCX, "krasas": KRASAS, "izmeri": IZMERI,
        "platumi": PLATUMI, "platums": TEKSTA_PLATUMS, "ailes": AILES,
        "sakne": SAKNE,
        "burti": C.BURTI, "skola": C.SKOLA, "gads": C.GADS,
    }, ensure_ascii=False)
