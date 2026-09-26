# -*- coding: utf-8 -*-
"""8. klase, 65. stunda: «Kurš augstums der?»

Trijstūrim ir trīs augstumi, un katrs kopā ar savu malu dod to pašu
laukumu: 8 · 5 = 5√2 · 4√2 = 40. Platleņķa trijstūrī augstums var
krist ārpusē - uz malas pagarinājuma; slīdnis to parāda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Slidnis, Varianti, geometrija)

TEMA = "Kurš augstums der?"

MERKIS = ("Zīmēsim trijstūra augstumus un pamatosim, ka laukumu var "
          "aprēķināt ar katru malu un tās augstumu.")

_TRIS = geometrija(
    [("A", 0, 0), ("B", 8, 0), ("C", 3, 5), ("K", 3, 0, 270),
     ("L", 4, 4, 45), ("M", 2.1176, 3.5294, 150)],
    nogriezni=["AB", "BC", "CA", "CK", "AL", "BM"],
    taisni=["CKB", "ALB", "BMC"])


def _plats(solis):
    punkti = [("A", 0, 0), ("B", 4, 0), ("C", 7, 4), ("H", 7, 0, 270)]
    nogr = ["AB", "BC", "CA"]
    izc, tais = [], []
    if solis >= 2:
        izc.append("BH")
    if solis >= 3:
        nogr.append("CH")
        tais.append("CHA")
    return geometrija(punkti, nogriezni=nogr, izcelti=izc, taisni=tais,
                      iekrasot=[("ABC", 0)])


SATURS = [
    Sakums("Kurš augstums der?",
           zimejums=_TRIS,
           paraksts="Trīs augstumi CK, AL un BM - katrs pret savu malu.",
           fakti=["Trijstūrim ir trīs augstumi - pa vienam pret katru malu.",
                  "S = {a · h_a|2} = {b · h_b|2} = {c · h_c|2}.",
                  "Platleņķa trijstūrī augstums var būt ārpusē."]),

    Doma("Mala un tās augstums",
         "Laukumu var rēķināt ar jebkuru malu, ja ņem tieši tai novilkto "
         "augstumu.",
         soli=[
             "Augstums ir perpendikuls no virsotnes pret pretējo malu vai "
             "tās pagarinājumu.",
             "Šaurleņķa trijstūrī visi trīs augstumi ir iekšpusē.",
             "Platleņķa trijstūrī divi augstumi krīt ārpusē.",
             "Taisnleņķa trijstūrī divi augstumi ir pašas katetes.",
         ],
         pieze="Jo garāka mala, jo īsāks tai novilktais augstums - "
               "reizinājums a · h visām malām ir vienāds."),

    Slidnis("Augstums ārpusē", [
        {"v": "Plats leņķis B", "teksts": "Trijstūris ABC",
         "zim": _plats(1)},
        {"v": "Pagarina AB", "teksts": "Mala turpinās aiz B",
         "zim": _plats(2)},
        {"v": "Augstums CH", "teksts": "Perpendikuls krīt uz pagarinājuma",
         "zim": _plats(3)},
        {"v": "S = {AB · CH|2}", "teksts": "Formula tā pati: 4 · 4 : 2 = 8",
         "zim": _plats(3)},
    ]),

    Paraugs("Otrs augstums",
            uzd="Trijstūra malas a = 12 cm un b = 8 cm; augstums pret a ir "
                "6 cm. Atrodi augstumu pret b.",
            soli=[
                ("S = {12 · 6|2} = 36 cm²", "Laukums ar malu a."),
                ("{8 · h_b|2} = 36", "Tas pats laukums ar malu b."),
                ("h_b = {72|8} = 9 cm", "Atrisina."),
            ],
            atbilde="9 cm"),

    Ievadi("Aprēķini", [
        {"jaut": "Mala 10 cm, tās augstums 4 cm. S (cm²)?", "atb": ["20"],
         "padoms": "{40|2}."},
        {"jaut": "Tam pašam trijstūrim cita mala ir 5 cm. Augstums pret to "
                 "(cm)?", "atb": ["8"], "padoms": "{5 · h|2} = 20."},
        {"jaut": "Platleņķa trijstūrī mala 6 cm, augstums pret to (ārpusē) "
                 "5 cm. S (cm²)?", "atb": ["15"], "padoms": "{30|2}."},
        {"jaut": "Malas 15 cm un 10 cm; augstums pret 15 cm malu ir 4 cm. "
                 "Augstums pret 10 cm malu?", "atb": ["6"],
         "padoms": "S = 30 cm²."},
    ]),

    Varianti("Spried", [
        {"jaut": "Kur krīt platleņķa trijstūra augstums no šaurā leņķa "
                 "virsotnes?",
         "opcijas": ["Uz malas pagarinājuma", "Malas viduspunktā",
                     "Trijstūra iekšpusē", "Tāda augstuma nav"],
         "pareizi": 0, "padoms": "Skaties slīdni."},
        {"jaut": "Pret garāko malu novilktais augstums ir...",
         "opcijas": ["īsākais", "garākais", "vidējais",
                     "vienāds ar pārējiem"],
         "pareizi": 0, "padoms": "a · h ir vienāds visām malām."},
        {"jaut": "Taisnleņķa trijstūrī augstums pret kateti ir...",
         "opcijas": ["otra katete", "hipotenūza", "mediāna", "nulle"],
         "pareizi": 0, "padoms": "Katetes ir perpendikulāras."},
    ]),

    Pasaule("Zemes gabals",
            Ievadi("", [
                {"jaut": "Trijstūrveida zemes gabala mala gar ceļu ir 60 m. "
                         "Pretējais stūris ir 40 m no ceļa. Laukums (m²)?",
                 "atb": ["1200"], "padoms": "{60 · 40|2}."},
                {"jaut": "Cik aru tas ir? (1 ars = 100 m²)",
                 "atb": ["12"], "padoms": "1200 : 100."},
                {"jaut": "Mala gar upi ir 80 m. Cik m no upes ir pretējais "
                         "stūris?",
                 "atb": ["30"], "padoms": "{80 · h|2} = 1200."},
            ]),
            pavediens="maja",
            konteksts="Mērnieks mēra augstumu pret to malu, pie kuras ērtāk "
                      "piekļūt.",
            kapec="Katra mala ar savu augstumu dod vienu un to pašu "
                  "laukumu."),

    Kopsavilkums([
        "Novelku visus trīs trijstūra augstumus.",
        "Atrodu augstumu ārpus platleņķa trijstūra.",
        "Aprēķinu laukumu ar jebkuru malu un tās augstumu.",
    ]),

    Majas([
        "Uzzīmē platleņķa trijstūri un novelc visus trīs augstumus.",
        "Izmēri divas malas un to augstumus; pārbaudi, vai laukumi sakrīt.",
        "Paskaidro, kāpēc garākajai malai ir īsākais augstums.",
    ]),
]
