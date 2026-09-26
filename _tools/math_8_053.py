# -*- coding: utf-8 -*-
"""8. klase, 53. stunda: «Kur uz skaitļu taisnes atrodas šī sakne?»

Iracionālu skaitli uz taisnes var atlikt divējādi: aptuveni (pēc
tuvinājuma) vai precīzi - ar cirkuli no kvadrāta diagonāles. Slīdnis
parāda, kā riņķa loks «pārnes» diagonāli √2 uz taisni.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, geometrija, taisne)

TEMA = "Kur uz skaitļu taisnes atrodas šī sakne?"

MERKIS = ("Atliksim uz skaitļu taisnes iracionālu skaitli ar norādīto "
          "precizitāti.")


def _diagonale(ar_loku):
    punkti = [("O", 0, 0, 270), ("A", 3, 0, 270), ("B", 3, 3),
              ("_x", 5, 0)]
    if ar_loku:
        punkti.append(("P", 4.24, 0, 270))
    return geometrija(punkti, nogriezni=["OA", "AB", "OB"],
                      stari=[("O", "_x")], taisni=["OAB"],
                      malas=[("OA", "1"), ("AB", "1"), ("OB", "√2")],
                      izcelti=["OP"] if ar_loku else [])


SATURS = [
    Sakums("Kur ir √2 uz taisnes?",
           zimejums=taisne(0, 3, 1, [(1.414, "√2"), (1.732, "√3")], sikas=10),
           paraksts="√2 ≈ 1,41 un √3 ≈ 1,73 - starp 1 un 2.",
           fakti=["Aptuveni: atliek tuvinājumu.",
                  "Precīzi: ar cirkuli no kvadrāta diagonāles.",
                  "Punkts uz taisnes ir precīzs, tuvinājums - nē."]),

    Slidnis("√2 ar cirkuli", [
        {"v": "1. solis", "teksts": "Kvadrāts ar malu 1 uz taisnes",
         "zim": _diagonale(False)},
        {"v": "2. solis", "teksts": "Diagonāle OB = √2 (laukums 2)",
         "zim": _diagonale(False)},
        {"v": "3. solis", "teksts": "Cirkulis O centrā, rādiuss OB - loks "
                                    "krusto taisni punktā P",
         "zim": _diagonale(True)},
        {"v": "OP = √2", "teksts": "Precīzs punkts, bez tuvinājuma",
         "zim": _diagonale(True)},
    ]),

    Doma("Divi veidi",
         "Iracionālu skaitli uz taisnes var atlikt aptuveni vai precīzi.",
         soli=[
             "Aptuveni: atrodi tuvinājumu ar vajadzīgo precizitāti.",
             "Izvēlies vienības nogriezni tā, lai precizitāte būtu redzama "
             "(piem., 10 cm, ja vajag desmitdaļas).",
             "Precīzi: sakni uzbūvē kā taisnleņķa trijstūra malu un pārnes ar "
             "cirkuli.",
         ],
         pieze="√5 iegūst no taisnleņķa trijstūra ar katetēm 1 un 2 - to "
               "pamatos Pitagora teorēma gada beigās."),

    Ievadi("Atliec un novērtē", [
        {"jaut": "Starp kurām desmitdaļām ir √5? Ieraksti mazāko.",
         "atb": ["2,2", "2.2"], "padoms": "2,2^2 = 4,84; 2,3^2 = 5,29."},
        {"jaut": "Starp kurām desmitdaļām ir √8? Ieraksti mazāko.",
         "atb": ["2,8", "2.8"], "padoms": "2,8^2 = 7,84; 2,9^2 = 8,41."},
        {"jaut": "Vienības nogrieznis 10 cm. Cik cm no 0 ir √2 (līdz mm)?",
         "atb": ["14,1", "14.1"], "padoms": "1,414 · 10."},
        {"jaut": "Cik veselu skaitļu ir starp −√10 un √10?",
         "atb": ["7"], "padoms": "−3 ... 3."},
    ]),

    Varianti("Kurš punkts?", [
        {"jaut": "Kurš skaitlis ir tuvāk 3?",
         "opcijas": ["√10", "√7", "√5", "√3"],
         "pareizi": 0, "padoms": "√9 = 3."},
        {"jaut": "Kurš no skaitļiem atrodas starp 4 un 5?",
         "opcijas": ["√23", "√15", "√26", "√35"],
         "pareizi": 0, "padoms": "16 < 23 < 25."},
        {"jaut": "Ar cirkuli no kvadrāta ar malu 1 iegūst...",
         "opcijas": ["√2", "2", "√3", "1,4"],
         "pareizi": 0, "padoms": "Diagonāle."},
    ]),

    Pasaule("Kartes mērogs",
            Ievadi("", [
                {"jaut": "Kvadrātveida parks kartē 1 cm × 1 cm, mērogs 1 : 1000. "
                         "Cik metru ir parka diagonāle (līdz m)?",
                 "atb": ["14"], "padoms": "√2 · 10 m ≈ 14,1 m."},
                {"jaut": "Parka mala dabā (m)?",
                 "atb": ["10"], "padoms": "1 cm · 1000."},
                {"jaut": "Cik metru ietaupa, ejot pa diagonāli, nevis gar "
                         "divām malām (līdz m)?",
                 "atb": ["6"], "padoms": "20 − 14,1."},
            ]),
            pavediens="celojums",
            konteksts="Taka pa kvadrāta diagonāli ir √2 reizes garāka par "
                      "malu - vienmēr, jebkurā mērogā.",
            kapec="Tāpēc parkos cilvēki izmin takas pa diagonāli."),

    Kopsavilkums([
        "Atlieku sakni uz taisnes aptuveni ar vajadzīgo precizitāti.",
        "Uzbūvēju √2 ar cirkuli no kvadrāta diagonāles.",
        "Salīdzinu saknes pēc to vietas uz taisnes.",
    ]),

    Majas([
        "Uz rūtiņu lapas (vienība 10 rūtiņas) atliec √2 ar cirkuli.",
        "Atliec √3 un √5 aptuveni.",
        "Nomēri, cik tuvu tavs √2 punkts ir 1,41.",
    ]),
]
