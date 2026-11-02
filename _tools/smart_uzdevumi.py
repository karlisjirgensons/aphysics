# -*- coding: utf-8 -*-
"""«Cik labi zini bērna matemātiku» (smart/) - 5 uzdevumi katrai klasei 1-9.

Uzdevumi ir tādi, ar kādiem bērns tajā klasē sastopas skolā; vecāks tos
risina pats. Katram uzdevumam: (angliski, latviski vai None - tas pats
teksts, [pareizā, nepareizā, nepareizā, nepareizā]). Pareizā ir pirmā -
pārlūks atbildes sajauc.

Iezīmes (tās pašas kā stundās): {3|4} - stāvā daļa, x^2 / a^{m+n} -
kāpinātājs. Rakstām angliski - decimālpunkts, ×, ÷; latviskajai lapai
latvisks() pārvērš par decimālkomatu, «·» un «:».
1. klasē nav reizināšanas un daļu.

Šis modulis zina tikai uzdevumus un to noformējumu (SRP).
"""

import html
import json
import re

import valoda

KLASES = {
    1: [
        ("8 + 7 = ?", None, ["15", "14", "16", "13"]),
        ("15 − 9 = ?", None, ["6", "5", "7", "8"]),
        ("Which number is missing? 12, 14, __, 18",
         "Kurš skaitlis trūkst? 12, 14, __, 18", ["16", "15", "17", "20"]),
        ("Anna has 9 apples and gives away 4. How many are left?",
         "Annai ir 9 āboli, 4 viņa atdod. Cik palika?",
         ["5", "4", "13", "6"]),
        ("How many tens are in 17?", "Cik desmitu ir skaitlī 17?",
         ["1", "7", "17", "10"]),
    ],
    2: [
        ("47 + 36 = ?", None, ["83", "73", "713", "81"]),
        ("5 × 6 = ?", None, ["30", "11", "25", "36"]),
        ("20 ÷ 4 = ?", None, ["5", "4", "6", "16"]),
        ("How many minutes are in 1 hour?", "Cik minūšu ir 1 stundā?",
         ["60", "100", "30", "24"]),
        ("1 m = ? cm", None, ["100", "10", "1000", "60"]),
    ],
    3: [
        ("8 × 7 = ?", None, ["56", "54", "49", "63"]),
        ("72 ÷ 9 = ?", None, ["8", "7", "9", "6"]),
        ("345 + 278 = ?", None, ["623", "613", "523", "633"]),
        ("A square has a side of 6 cm. Its perimeter?",
         "Kvadrāta mala ir 6 cm. Tā perimetrs?",
         ["24 cm", "36 cm", "12 cm", "18 cm"]),
        ("What is {1|2} of 18?", "Cik ir {1|2} no 18?",
         ["9", "6", "12", "36"]),
    ],
    4: [
        ("24 × 15 = ?", None, ["360", "340", "300", "390"]),
        ("What is the remainder of 50 ÷ 7?",
         "Kāds ir atlikums, dalot 50 ar 7?", ["1", "7", "3", "0"]),
        ("A rectangle has sides 8 cm and 5 cm. Its area?",
         "Taisnstūra malas ir 8 cm un 5 cm. Tā laukums?",
         ["40 cm^2", "26 cm^2", "13 cm^2", "45 cm^2"]),
        ("{3|4} of 20 = ?", "{3|4} no 20 = ?", ["15", "5", "12", "16"]),
        ("2 kg 300 g = ? g", None, ["2300", "230", "2030", "2003"]),
    ],
    5: [
        ("0.6 + 0.25 = ?", None, ["0.85", "0.31", "0.625", "0.8"]),
        ("{2|5} + {1|5} = ?", None, ["{3|5}", "{3|10}", "{2|25}", "{1|5}"]),
        ("6 + 4 × 3 = ?", None, ["18", "30", "22", "13"]),
        ("Round 3.47 to tenths", "Noapaļo 3.47 līdz desmitdaļām",
         ["3.5", "3.4", "3.47", "4"]),
        ("3.2 × 10 = ?", None, ["32", "3.20", "320", "0.32"]),
    ],
    6: [
        ("−5 + 8 = ?", None, ["3", "−3", "13", "−13"]),
        ("20% of 150 = ?", "20% no 150 = ?", ["30", "20", "15", "75"]),
        ("{2|3} × {3|4} = ?", None, ["{1|2}", "{5|7}", "{6|7}", "{8|9}"]),
        ("Solve: x + 7 = 12", "Atrisini: x + 7 = 12",
         ["x = 5", "x = 19", "x = 7", "x = −5"]),
        ("Simplify the ratio 12 : 18", "Saīsini attiecību 12 : 18",
         ["2 : 3", "3 : 2", "6 : 9", "4 : 5"]),
    ],
    7: [
        ("Solve: 3x − 4 = 11", "Atrisini: 3x − 4 = 11",
         ["x = 5", "x = 15", "x = 3", "x = {7|3}"]),
        ("2^5 = ?", None, ["32", "10", "25", "16"]),
        ("Two angles of a triangle are 40° and 75°. The third angle?",
         "Divi trijstūra leņķi ir 40° un 75°. Trešais leņķis?",
         ["65°", "75°", "55°", "245°"]),
        ("A jacket costs 80 €, discount 25%. New price?",
         "Jaka maksā 80 €, atlaide 25%. Jaunā cena?",
         ["60 €", "55 €", "20 €", "64 €"]),
        ("(−3) × (−4) = ?", None, ["12", "−12", "−7", "7"]),
    ],
    8: [
        ("A right triangle has legs 6 and 8. The hypotenuse?",
         "Taisnleņķa trijstūra katetes ir 6 un 8. Hipotenūza?",
         ["10", "14", "48", "12"]),
        ("(a + 3)^2 = ?", None,
         ["a^2 + 6a + 9", "a^2 + 9", "a^2 + 3a + 9", "2a + 6"]),
        ("y = 2x − 1. What is y when x = 4?",
         "y = 2x − 1. Cik ir y, ja x = 4?", ["7", "9", "8", "3"]),
        ("Solve: 2x > 10", "Atrisini: 2x > 10",
         ["x > 5", "x < 5", "x > 20", "x > 8"]),
        ("3^2 × 3^3 = ?", None, ["3^5", "3^6", "9^5", "6^5"]),
    ],
    9: [
        ("Solve: x^2 = 49", "Atrisini: x^2 = 49",
         ["x = ±7", "x = 7", "x = 24.5", "x = ±49"]),
        ("Roots of x^2 − 5x + 6 = 0?", "Vienādojuma x^2 − 5x + 6 = 0 saknes?",
         ["2; 3", "−2; −3", "1; 6", "−1; 6"]),
        ("x + y = 10 and x − y = 4. x = ?", "x + y = 10 un x − y = 4. x = ?",
         ["7", "3", "6", "14"]),
        ("A coin is tossed twice. Probability of heads both times?",
         "Monētu met divreiz. Varbūtība, ka abas reizes ģerbonis?",
         ["{1|4}", "{1|2}", "{1|3}", "{3|4}"]),
        ("Right triangle: opposite side 3, hypotenuse 5. sin α = ?",
         "Taisnleņķa trijstūrī pretkatete 3, hipotenūza 5. sin α = ?",
         ["{3|5}", "{4|5}", "{3|4}", "{5|3}"]),
    ],
}

_DALA = re.compile(r"\{([^|{}]+)\|([^|{}]+)\}")
_KAP = re.compile(r"\^(\{[^{}]+\}|\S)")


def latvisks(s):
    """Decimālkomats, reizināšana «·», dalīšana «:»."""
    s = re.sub(r"(\d)\.(\d)", r"\1,\2", s)
    return s.replace("×", "·").replace("÷", ":")


def formula(s):
    """Iezīmes -> HTML: {3|4} stāvā daļa, x^2 / a^{m+n} kāpinātājs."""
    s = html.escape(latvisks(s) if valoda.tagad() == "lv" else s)
    s = _DALA.sub(r'<span class="fr"><span>\1</span><span>\2</span></span>',
                  s)
    return _KAP.sub(lambda m: "<sup>%s</sup>" % m.group(1).strip("{}"), s)


def klases():
    """{klase: [{q: HTML, o: [HTML, ...]}]} tagadējā valodā; o[0] ir
    pareizā atbilde."""
    return {k: [{"q": formula(lv if valoda.tagad() == "lv" and lv else en),
                 "o": [formula(x) for x in o]} for en, lv, o in uzd]
            for k, uzd in KLASES.items()}


def js():
    return "var SU=%s;" % json.dumps(klases(), ensure_ascii=False)
