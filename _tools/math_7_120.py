# -*- coding: utf-8 -*-
"""7. klase, 120. stunda: «Kā atvērt iekavas?»

Reizināšanas sadalāmības īpašība: a(b + c) = ab + ac. Reizinātājs pirms
iekavām jāpareizina ar katru saskaitāmo iekavās. Ģeometriski - lielā
taisnstūra laukums ir divu mazāko summa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, geometrija)

TEMA = "Kā atvērt iekavas?"

MERKIS = ("Atvērsim iekavas, lietojot reizināšanas sadalāmības īpašību.")

SATURS = [
    Sakums("3(x + 2): viens taisnstūris vai divi?",
           zimejums=geometrija([("_A", 0, 0), ("_E", 5, 0), ("_B", 8, 0),
                                ("_C", 8, 3), ("_F", 5, 3), ("_D", 0, 3)],
                               nogriezni=[("_A", "_B"), ("_B", "_C"),
                                          ("_C", "_D"), ("_D", "_A"),
                                          ("_E", "_F")],
                               iekrasot=[(("_A", "_E", "_F", "_D"), 0),
                                         (("_E", "_B", "_C", "_F"), 1)],
                               uzraksti=[(2.5, 1.3, "3x"), (6.5, 1.3, "6")],
                               malas=[(("_A", "_E"), "x"),
                                      (("_E", "_B"), "2"),
                                      (("_D", "_A"), "3")]),
           paraksts="Laukums 3(x + 2) = 3x + 6.",
           fakti=["Lielais taisnstūris: augstums 3, platums x + 2.",
                  "Sadalīts divos: 3x un 3 · 2.",
                  "Tātad 3(x + 2) = 3x + 6."]),

    Doma("Katram saskaitāmajam",
         "Atverot iekavas, reizinātāju pirms iekavām pareizina ar katru "
         "saskaitāmo iekavās: a(b + c) = ab + ac, a(b − c) = ab − ac.",
         soli=[
             "Novelc «bultiņas» no reizinātāja uz katru saskaitāmo.",
             "Sareizini katru pāri, ievērojot zīmes.",
             "Pieraksti rezultātu bez iekavām.",
             "Ja vajag, savelc līdzīgos.",
         ],
         pieze="Biežākā kļūda: 3(x + 2) = 3x + 2 - aizmirst pareizināt "
               "otro saskaitāmo."),

    Paraugs("Atver iekavas un savelc",
            uzd="Vienkāršo: 4(2a − 3) + 5a.",
            soli=[
                ("4 · 2a − 4 · 3 + 5a", "Bultiņas."),
                ("8a − 12 + 5a", "Sareizina."),
                ("13a − 12", "Savelk."),
            ],
            atbilde="13a − 12"),

    Ievadi("Atver iekavas", [
        {"jaut": "5(x + 4) = ?",
         "atb": ["5x + 20", "5x+20", "20+5x"], "padoms": "5x un 20.",
         "tastatura": "text"},
        {"jaut": "3(2y − 7) = ?",
         "atb": ["6y − 21", "6y-21"], "padoms": "6y un 21.",
         "tastatura": "text"},
        {"jaut": "a(b + 3) = ?",
         "atb": ["ab + 3a", "ab+3a", "3a+ab"], "padoms": "ab un 3a.",
         "tastatura": "text"},
        {"jaut": "2(x + 1) + 3(x + 2) = ?",
         "atb": ["5x + 8", "5x+8"], "padoms": "2x + 2 + 3x + 6.",
         "tastatura": "text"},
        {"jaut": "0,5(4m + 6) = ?",
         "atb": ["2m + 3", "2m+3"], "padoms": "Puse no katra.",
         "tastatura": "text"},
        {"jaut": "x(x + 5) = ?",
         "atb": ["x² + 5x", "x^2+5x", "x²+5x"], "padoms": "x · x = x².",
         "tastatura": "text"},
    ], pamats=4),

    Varianti("Kur kļūda?", [
        {"jaut": "6(a + 2) = 6a + 2",
         "opcijas": ["Jābūt 6a + 12", "Pareizi", "Jābūt 8a",
                     "Jābūt 6a + 8"],
         "pareizi": 0, "padoms": "Arī 2 jāreizina."},
        {"jaut": "3(x − 4) = 3x − 7",
         "opcijas": ["Jābūt 3x − 12", "Pareizi", "Jābūt 3x + 12",
                     "Jābūt x − 12"],
         "pareizi": 0, "padoms": "3 · 4 = 12."},
    ]),

    Pasaule("Grupas biļetes",
            Ievadi("", [
                {"jaut": "4 draugi pērk biļeti b € un popkornu 3 € katrs: "
                         "4(b + 3). Cik €, ja b = 8?",
                 "atb": ["44"], "padoms": "4 · 11 vai 32 + 12."},
                {"jaut": "Atverot iekavas: 4b + ? Kāds skaitlis?",
                 "atb": ["12"], "padoms": "4 · 3."},
                {"jaut": "Cik € par popkornu visiem kopā?",
                 "atb": ["12"], "padoms": "4 · 3."},
            ]),
            pavediens="skola",
            konteksts="Grupas rēķins: vai nu katrs reizi pa (b + 3), vai "
                      "atsevišķi biļetes un popkorns - summa tā pati.",
            kapec="Iekavas atverot, aprēķins sadalās daļās."),

    Kopsavilkums([
        "Lietoju a(b + c) = ab + ac.",
        "Reizinu ar katru saskaitāmo iekavās.",
        "Pēc iekavu atvēršanas savelku līdzīgos.",
        "Modelēju ar taisnstūra laukumu.",
    ]),

    Majas([
        "Atver iekavas: 7(2x − 3) − 5x.",
        "Uzzīmē laukuma modeli izteiksmei 4(a + 5).",
        "Izdomā situāciju izteiksmei 3(x + 10).",
    ]),
]
