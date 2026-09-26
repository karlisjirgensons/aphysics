# -*- coding: utf-8 -*-
"""9. klase, 101. stunda: «Kur meklēt lielāko vērtību?»

Optimizācija ar parabolas virsotni: 40 m žoga gar kūts sienu - kāds
taisnstūris dod lielāko laukumu? S(x) = x(40 − 2x) ir parabola ar zariem
lejup; virsotne x = 10 dod 200 m². Temata noslēgums pirms PD.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, geometrija,
                         parabola, restis)

TEMA = "Kur meklēt lielāko vērtību?"

MERKIS = ("Risināsim praktisku uzdevumu par lielāko laukumu vai mazākajām "
          "izmaksām.")


def _aploks(x):
    """Taisnstūris x × (40 − 2x) pie sienas (augšējā mala - siena)."""
    y = 40 - 2 * x
    return geometrija([("_1", 0, 0), ("_2", y, 0), ("_3", y, x),
                       ("_4", 0, x)],
                      nogriezni=[("_1", "_2"), ("_2", "_3"), ("_4", "_1")],
                      izcelti=[("_3", "_4")],
                      iekrasot=[(("_1", "_2", "_3", "_4"), 0)],
                      malas=[(("_4", "_1"), "%g m" % x),
                             (("_1", "_2"), "%g m" % y)],
                      uzraksti=[(y / 2.0, x / 2.0, "%g m²" % (x * y))])


SATURS = [
    Sakums("40 m žoga - cik lielu aploku var uzbūvēt?",
           zimejums=parabola(-2, 40, 0, 0, 20, 0, 220, uzraksts="S(x)",
                             solis=2, solis_y=40, asis=("x", "S"),
                             punkti=[(10, 200, "(10; 200)")]),
           paraksts="S(x) = x(40 − 2x): lielākais laukums pie x = 10 m.",
           fakti=["Ceturtā mala - kūts siena, tai žogs nav vajadzīgs.",
                  "Divas malas x, viena 40 − 2x.",
                  "Virsotne: x = 10, S = 200 m²."]),

    Slidnis("Izmēģini dažādus x", [
        {"v": "x = 5", "teksts": "5 × 30 = 150 m²", "zim": _aploks(5)},
        {"v": "x = 10", "teksts": "10 × 20 = 200 m² - lielākais",
         "zim": _aploks(10)},
        {"v": "x = 15", "teksts": "15 × 10 = 150 m²", "zim": _aploks(15)},
    ], ievads="Siena ir augšā (izcelta); žogs - pārējās trīs malas."),

    Doma("Optimizācija ar virsotni",
         "Ja lielums ir kvadrātfunkcija ar a < 0, tā lielākā vērtība ir "
         "virsotnē; ja a > 0 - mazākā.",
         soli=[
             "Apzīmē mainīgo x un izsaki lielumu kā funkciju.",
             "Atver iekavas: S = ax^2 + bx + c.",
             "x_v = −{b|2a}; aprēķini S(x_v).",
             "Pārbaudi, vai x_v der situācijā (garumi > 0).",
         ]),

    Paraugs("Aploks pie sienas",
            uzd="Ar 40 m žoga pie sienas norobežo taisnstūri. Kādi izmēri "
                "dod lielāko laukumu?",
            soli=[
                ("S = x(40 − 2x) = −2x^2 + 40x", "Funkcija."),
                ("x_v = −{40|−4} = 10", "Virsotne."),
                ("S(10) = 10 · 20 = 200", "Lielākais laukums."),
            ],
            atbilde="10 m × 20 m, 200 m²"),

    Ievadi("Aprēķini", [
        {"jaut": "Bez sienas: 40 m žoga ap taisnstūri. S = x(20 − x). "
                 "Lielākais laukums (m²)?", "atb": ["100"],
         "padoms": "x_v = 10: kvadrāts 10 × 10."},
        {"jaut": "Divu skaitļu summa 16. Lielākais reizinājums?",
         "atb": ["64"], "padoms": "x(16 − x), x_v = 8."},
        {"jaut": "Peļņa P = −x^2 + 60x − 500 (€), x - pārdotās preces. "
                 "Pie kāda x peļņa lielākā?", "atb": ["30"],
         "padoms": "−{60|−2}."},
        {"jaut": "Lielākā peļņa (€)?", "atb": ["400"],
         "padoms": "−900 + 1800 − 500."},
    ]),

    Varianti("Kur ir optimums?", [
        {"jaut": "Izmaksas C = 2x^2 − 40x + 300. Mazākās izmaksas pie x = ?",
         "opcijas": ["10", "20", "−10", "300"],
         "pareizi": 0, "padoms": "a > 0, virsotne - minimums."},
        {"jaut": "S = −x^2 + 8x. Vai 20 m² var sasniegt?",
         "opcijas": ["Nē - max ir 16", "Jā, pie x = 4", "Jā, pie x = 2",
                     "Jā, pie x = 10"],
         "pareizi": 0, "padoms": "S(4) = 16."},
    ]),

    Pasaule("Biļešu cena koncertam",
            Kustiba("", [
                {"jaut": "Pie 10 € biļetes nāk 600 cilvēku; katrs +1 € atbaida "
                         "30 cilvēkus. Ieņēmumi (10 + x)(600 − 30x). Kāda cena "
                         "(€) dod lielākos ieņēmumus?",
                 "atb": 15, "sakums": 10, "beigas": 20, "iedala": 1,
                 "mers": "€", "merkis": "labākā cena", "objekts": "Cena",
                 "padoms": "−30x^2 + 300x + 6000; x_v = 5."},
                {"jaut": "Cik cilvēku tad nāks?",
                 "atb": 450, "sakums": 300, "beigas": 600, "iedala": 50,
                 "mers": "", "merkis": "apmeklētāji", "objekts": "Zāle",
                 "padoms": "600 − 150."},
            ]),
            pavediens="veikals",
            konteksts="Organizatori meklē cenu: dārgāk - mazāk cilvēku, "
                      "lētāk - mazāk naudas no katra.",
            kapec="Ieņēmumu parabolas virsotne ir labākā cena.",
            zimejums=restis([["cena, €", "10", "15", "20"],
                             ["ieņēmumi, €", "6000", "6750", "6000"]])),

    Kopsavilkums([
        "Izsaku lielumu kā kvadrātfunkciju.",
        "Atrodu lielāko vai mazāko vērtību virsotnē.",
        "Pārbaudu, vai atbilde der situācijā.",
    ]),

    Majas([
        "Atkārto 9.5. tematu - nākamajā stundā pārbaudes darbs.",
        "Ar 60 m žoga pie sienas: kāds ir lielākais laukums?",
        "Atrodi reālu situāciju, kur jāmeklē «labākā» vērtība.",
    ]),
]
