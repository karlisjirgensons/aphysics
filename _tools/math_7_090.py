# -*- coding: utf-8 -*-
"""7. klase, 90. stunda: «Kā izmērīt attālumu no punkta līdz taisnei?»

Attālums no punkta līdz taisnei ir perpendikula garums - īsākais no visiem
nogriežņiem, ko var novilkt no punkta līdz taisnei. Stunda konstruē
perpendikulu ar cirkuli un skaidro, kāpēc tas ir īsākais.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         geometrija)

TEMA = "Kā izmērīt attālumu no punkta līdz taisnei?"

MERKIS = ("Konstruēsim perpendikulu no punkta pret taisni un skaidrosim "
          "attāluma jēdzienu.")

_ATT = geometrija([("P", 3, 4), ("H", 3, 0, -90), ("_a", -1, 0),
                   ("_b", 9, 0), ("K", 7, 0, -90), ("L", 0, 0, -90)],
                  taisnes=[("_a", "_b")], izcelti=["PH"],
                  nogriezni=["PK", "PL"], taisni=["PHK"],
                  malas=[("PH", "4 cm")])

SATURS = [
    Sakums("Īsākais ceļš līdz krastam",
           zimejums=_ATT,
           paraksts="PH ⊥ a: īsākais no visiem nogriežņiem.",
           fakti=["Peldētājs uz krastu peld taisni «pretī» krastam.",
                  "Jebkurš slīps ceļš (PK, PL) ir garāks.",
                  "Attālums līdz taisnei ir perpendikula garums."]),

    Doma("Attālums = perpendikula garums",
         "Attālums no punkta līdz taisnei ir perpendikula garums, kas "
         "novilkts no šī punkta pret taisni. Tas ir īsākais no visiem "
         "nogriežņiem, kas savieno punktu ar taisni.",
         soli=[
             "Konstrukcija: no P novelc loku, kas krusto taisni divos "
             "punktos A un B.",
             "No A un B novelc vienādus lokus otrpus taisnei - krustpunkts C.",
             "Taisne PC ir perpendikuls; H - krustpunkts ar a.",
             "Izmēri PH.",
         ],
         pieze="Slīpais nogrieznis PK ir garāks par PH: trijstūrī PHK pretī "
               "taisnajam leņķim ir garākā mala (to pierādīsim 102. stundā)."),

    Paraugs("Attālums un slīpnes",
            uzd="Punkts P ir 4 cm no taisnes a. Vai no P līdz a var novilkt "
                "nogriezni 3 cm? Bet 5 cm?",
            soli=[
                ("Īsākais - perpendikuls, 4 cm", "Attālums."),
                ("3 cm < 4 cm - nevar", "Īsāka par perpendikulu nav."),
                ("5 cm > 4 cm - var, un pat divus (abās pusēs)",
                 "Slīpnes."),
            ],
            atbilde="3 cm - nevar; 5 cm - var (divus)."),

    Varianti("Attālums", [
        {"jaut": "Kā mēra attālumu no punkta līdz taisnei?",
         "opcijas": ["Pa perpendikulu", "Pa jebkuru nogriezni",
                     "Pa garāko nogriezni", "Pa 45° leņķi"],
         "pareizi": 0, "padoms": "Īsākais."},
        {"jaut": "Punkts atrodas uz taisnes. Kāds ir attālums?",
         "opcijas": ["0", "1", "Nav definēts", "Bezgalīgs"],
         "pareizi": 0, "padoms": "Nav jāiet nekur."},
        {"jaut": "Attālums starp paralēlām taisnēm ir...",
         "opcijas": ["perpendikula garums starp tām",
                     "jebkurš nogrieznis", "0", "nav definēts"],
         "pareizi": 0, "padoms": "Tas visur vienāds."},
    ]),

    Petijums("Konstruē perpendikulu",
             ["Uzzīmē taisni a un punktu P virs tās.",
              "Ar cirkuli no P novelc loku, kas krusto a punktos A un B.",
              "No A un B ar vienu rādiusu novelc lokus zem a - punkts C.",
              "Novelc PC. Izmēri leņķi pie H un attālumu PH.",
              "Izmēri vēl 2 slīpus nogriežņus no P uz a un salīdzini."],
             vajag="cirkulis, lineāls, stūrenis",
             secinajums="Leņķis pie H ir 90°, un PH ir īsāks par jebkuru "
                         "slīpu nogriezni."),

    Ievadi("Aprēķini", [
        {"jaut": "Attālums starp paralēlām taisnēm 6 cm. Punkts pa vidu. "
                 "Attālums līdz katrai (cm)?",
         "atb": ["3"], "padoms": "6 : 2."},
        {"jaut": "Taisnstūra malas 5 cm un 8 cm. Attālums no virsotnes līdz "
                 "pretējai garākajai malai (cm)?",
         "atb": ["5"], "padoms": "Blakus mala ir perpendikuls."},
        {"jaut": "Punkts (3; 7). Attālums līdz x asij?",
         "atb": ["7"], "padoms": "Perpendikuls - vertikāli."},
        {"jaut": "Punkts (−4; 2). Attālums līdz y asij?",
         "atb": ["4"], "padoms": "Horizontāli līdz x = 0."},
    ]),

    Pasaule("Glābšana no ledus",
            Ievadi("", [
                {"jaut": "Makšķernieks uz ledus 120 m no taisna krasta. "
                         "Cik m īsākais ceļš līdz krastam?",
                 "atb": ["120"], "padoms": "Perpendikuls."},
                {"jaut": "Tuvākā laipa ir 50 m pa krastu no perpendikula "
                         "pamata. Ceļš līdz laipai ir 130 m. Par cik m "
                         "garāks nekā īsākais?",
                 "atb": ["10"], "padoms": "130 − 120."},
                {"jaut": "Ejot 1 m/s, cik s aizņem īsākais ceļš?",
                 "atb": ["120"], "padoms": "120 : 1."},
            ]),
            pavediens="planeta",
            konteksts="Plāns ledus - svarīgs katrs metrs; īsākais ceļš ir "
                      "perpendikuls krastam.",
            kapec="Attālums līdz taisnei - drošības jautājums."),

    Zimejums("Punkta attālums līdz asīm",
             geometrija([("P", 3, 2), ("_x", 3, 0), ("_y", 0, 2),
                         ("O", 0, 0, 225), ("_x2", 5, 0), ("_y2", 0, 4)],
                        stari=[("O", "_x2"), ("O", "_y2")],
                        izcelti=[("P", "_x"), ("P", "_y")],
                        taisni=[("P", "_x", "_x2"), ("P", "_y", "_y2")],
                        malas=[(("P", "_x"), "2"), (("P", "_y"), "3")]),
             paskaidro="Punktam (3; 2): līdz x asij 2, līdz y asij 3."),

    Kopsavilkums([
        "Zinu, ka attālums līdz taisnei ir perpendikula garums.",
        "Konstruēju perpendikulu ar cirkuli un lineālu.",
        "Zinu, ka perpendikuls ir īsāks par slīpnēm.",
        "Nosaku attālumu starp paralēlām taisnēm un līdz asīm.",
    ]),

    Majas([
        "Konstruē perpendikulu no punkta pret taisni.",
        "Izmēri attālumu no loga līdz sienai pretī (perpendikulāri).",
        "Paskaidro, kāpēc gājēju pāreja iet perpendikulāri ielai.",
    ]),
]
