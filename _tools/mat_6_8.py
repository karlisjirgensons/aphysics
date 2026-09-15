# -*- coding: utf-8 -*-
"""Matemātika, 6. klase. 6.8. Kā plāno darbību izpildi ar visu veidu skaitļiem?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 6. klase, 6.8. temats): pozitīvu un
negatīvu skaitļu reizināšana un dalīšana, reizinājuma un dalījuma zīme,
kāpināšana, racionāls skaitlis kā {m|n}, darbību secība izteiksmēs ar
iekavām (līdz četrām darbībām), pāreja uz viena veida daļskaitļiem un
racionālu skaitļu šķirošana pēc pazīmes.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  6. klase"
TEMATS = "6.8."
NOSAUKUMS = "Kā plāno darbību izpildi ar visu veidu skaitļiem?"

ATGADNE = [
    "Zīmes:   ja abiem skaitļiem zīmes ir vienādas, reizinājums un dalījums "
    "ir pozitīvs; ja dažādas — negatīvs.   (−3) · (−4) = 12",
    "Kāpināšana:   (−2)² = 4   ·   (−2)³ = −8   ·   pāra kāpinātājs dod "
    "pozitīvu, nepāra — negatīvu rezultātu.",
    "Racionāls skaitlis ir katrs skaitlis, ko var pierakstīt kā {m|n}, kur "
    "m ir vesels un n — naturāls skaitlis. Darbību secība: iekavas, "
    "kāpināšana, reizināšana un dalīšana, tad saskaitīšana un atņemšana.",
]


# ---------------------------------------------------------------- veidnes
def zime(a, b):
    """Kāda zīme ir reizinājumam - pārbauda likumu, nevis rēķināšanu."""
    poz = (a < 0) == (b < 0)
    return ("Kāda zīme ir reizinājumam %s · %s?" % (V.iek(a), V.iek(b)),
            V.izvele("pozitīva" if poz else "negatīva",
                     "negatīva" if poz else "pozitīva",
                     "nulle", "nevar noteikt"), 0)


def reizina(a, b):
    return ("Cik ir %s · %s?" % (V.iek(a), V.iek(b)),
            V.izvele(a * b, -a * b, a + b, a - b, b - a, a * b + b), 0)


def dala(a, b):
    return ("Cik ir %s : %s?" % (V.iek(a), V.iek(b)),
            V.izvele(a // b, -(a // b), a - b, a + b, a // b + b,
                     2 * (a // b)), 0)


KAPES = "²³⁴⁵⁶⁷"          # kāpinātāju zīmes 2..7


def kapina(a, n):
    return ("Cik ir %s%s?" % (V.iek(a), KAPES[n - 2]),
            V.izvele(a ** n, -(a ** n), a * n, -a * n, a + n,
                     abs(a) * n, a ** n + n), 0)


def reiz_sask(a, b, c):
    """a + b · c - pārbauda, vai skolēns sāk ar reizināšanu."""
    return ("Cik ir %s + %s · %s?" % (V.sk(a), V.iek(b), V.iek(c)),
            V.izvele(a + b * c, (a + b) * c, a - b * c, a + b + c,
                     b * c, a + b * c + b), 0)


def iekavas(a, b, c):
    """a · (b − c) - pārbauda darbību secību ar iekavām."""
    return ("Cik ir %s · (%s − %s)?" % (V.iek(a), V.sk(b), V.sk(c)),
            V.izvele(a * (b - c), a * b - c, a * (b + c), a - b + c,
                     b - c, a * (c - b)), 0)


def kapina_izteiksme(a, b, c):
    """a² + b · c - kāpināšana izteiksmē ar vairākām darbībām."""
    return ("Cik ir %s² + %s · %s?" % (V.iek(a), V.iek(b), V.sk(c)),
            V.izvele(a * a + b * c, -a * a + b * c, a * 2 + b * c,
                     (a + b) * c, a * a - b * c, a * a + b + c), 0)


FD = {
    "veids": "fd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 6.8. temata beigās. Pārbauda pozitīvu un "
                "negatīvu skaitļu reizināšanu un dalīšanu, rezultāta zīmi, "
                "kāpināšanu, darbību secību izteiksmēs un racionāla skaitļa "
                "jēdzienu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosaka reizinājuma un dalījuma zīmi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(zime, [
             (-3, 5), (-4, -6), (7, -2), (-8, 3), (-5, -9), (6, -4),
             (-2, 11), (-7, -3), (9, -5), (-6, 8), (-9, -2), (4, -7),
             (-11, 3), (-5, -4), (8, -6)]),
         },
        {"sr": "Reizina pozitīvus un negatīvus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(reizina, [
             (-4, 7), (-5, -6), (8, -3), (-9, 4), (-7, -2), (6, -5),
             (-3, 12), (-8, -4), (11, -3), (-6, 9), (-12, -2), (5, -8),
             (-7, 6), (-2, -13), (9, -4)]),
         },
        {"sr": "Dala pozitīvus un negatīvus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dala, [
             (-24, 6), (-36, -9), (45, -5), (-56, 7), (-63, -9), (72, -8),
             (-42, 6), (-80, -10), (54, -6), (-64, 8), (-99, -11), (48, -4),
             (-35, 5), (-77, -7), (60, -12)]),
         },
        {"sr": "Kāpina racionālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kapina, [
             (-2, 2), (-2, 3), (-3, 2), (-3, 3), (-4, 2), (-5, 2),
             (-1, 4), (-1, 5), (-6, 2), (-2, 4), (-7, 2), (-10, 2),
             (-8, 2), (-2, 5), (-9, 2)]),
         },
        {"sr": "Zina, kad pakāpe ir pozitīva",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad pakāpe ar negatīvu bāzi ir pozitīva?",
              ["ja kāpinātājs ir pāra skaitlis",
               "ja kāpinātājs ir nepāra skaitlis", "vienmēr", "nekad"], 0),
             ("Kad pakāpe ar negatīvu bāzi ir negatīva?",
              ["ja kāpinātājs ir nepāra skaitlis",
               "ja kāpinātājs ir pāra skaitlis", "vienmēr", "nekad"], 0),
             ("Ar ko atšķiras (−3)² un −3²?",
              ["(−3)² = 9, bet −3² = −9", "tie ir vienādi",
               "(−3)² = −9, bet −3² = 9", "abi ir negatīvi"], 0),
             ("Kāda zīme ir pakāpei (−5)⁴?",
              ["pozitīva", "negatīva", "nulle", "nevar noteikt"], 0),
             ("Kāda zīme ir pakāpei (−5)⁷?",
              ["negatīva", "pozitīva", "nulle", "nevar noteikt"], 0),
             ("Cik ir (−1)¹⁰⁰?", ["1", "−1", "100", "−100"], 0),
             ("Cik ir (−1)⁹⁹?", ["−1", "1", "99", "−99"], 0),
             ("Cik ir 0² − 5?", ["−5", "5", "0", "25"], 0),
         ]},
        {"sr": "Reizina un dala daļas un decimāldaļas ar zīmēm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {1|2} · (−{2|3})?",
              ["−{1|3}", "{1|3}", "−{2|5}", "{2|5}"], 0),
             ("Cik ir (−{3|4}) : (−{1|4})?", ["3", "−3", "{3|16}", "1"], 0),
             ("Cik ir (−{2|5}) · 10?", ["−4", "4", "−20", "20"], 0),
             ("Cik ir (−{5|6}) : 5?", ["−{1|6}", "{1|6}", "−6", "6"], 0),
             ("Cik ir (−0,5) · 4?", ["−2", "2", "−20", "20"], 0),
             ("Cik ir (−0,2) · (−6)?", ["1,2", "−1,2", "12", "−12"], 0),
             ("Cik ir (−4,8) : 4?", ["−1,2", "1,2", "−12", "12"], 0),
             ("Cik ir (−2,4) : (−0,8)?", ["3", "−3", "0,3", "−0,3"], 0),
             ("Cik ir {3|4} · (−8)?", ["−6", "6", "−24", "24"], 0),
             ("Cik ir (−1,5) · (−2)?", ["3", "−3", "0,75", "−0,75"], 0),
         ]},
        {"sr": "Zina, kas ir racionāls skaitlis",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir racionāls skaitlis?",
              ["skaitlis, ko var pierakstīt kā {m|n}",
               "tikai vesels skaitlis", "tikai pozitīvs skaitlis",
               "tikai decimāldaļa"], 0),
             ("Kurš skaitlis nav vesels, bet ir racionāls?",
              ["0,75", "−3", "0", "12"], 0),
             ("Vai −5 ir racionāls skaitlis?",
              ["jā, jo −5 = {−5|1}", "nē", "tikai ar moduli",
               "tikai ar iekavām"], 0),
             ("Vai 0 ir racionāls skaitlis?",
              ["jā, jo 0 = {0|1}", "nē", "tikai pozitīvs", "tikai vesels"], 0),
             ("Kurš skaitlis nav negatīvs?", ["0", "−1", "−0,5", "−7"], 0),
             ("Kurš pieraksts nav racionāls skaitlis?",
              ["dalījums ar nulli", "{3|7}", "−2,5", "8"], 0),
             ("Kā racionālu skaitli pieraksta 0,25?",
              ["{1|4}", "{1|25}", "{25|1}", "{4|1}"], 0),
             ("Kā racionālu skaitli pieraksta −1,5?",
              ["−{3|2}", "{3|2}", "−{2|3}", "{15|1}"], 0),
         ]},
        {"sr": "Ievēro darbību secību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(reiz_sask, [
             (-5, 3, -4), (12, -2, -5), (20, -6, 2), (-8, 4, -3),
             (15, -3, 4), (-10, 5, -2), (7, -4, 3), (-6, -2, 5),
             (25, -5, 3), (-9, 6, -2), (18, -3, -4), (-12, 2, 7),
             (30, -4, 5), (-15, 3, 6), (11, -5, -3)]),
         },
        {"sr": "Aprēķina izteiksmi ar iekavām",
         "stunda": TEMATS,
         "jautajumi": V.kopa(iekavas, [
             (-3, 5, 8), (-5, 3, 7), (4, 2, 9), (-2, 10, 4), (6, 1, 5),
             (-4, 6, 11), (3, -2, 5), (-6, 8, 2), (5, 4, 9), (-7, 2, 6),
             (2, -5, 3), (-8, 7, 4), (9, 3, 8), (-2, -4, 6), (7, 5, 12)]),
         },
        {"sr": "Aprēķina izteiksmi ar kāpināšanu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kapina_izteiksme, [
             (-3, 2, 5), (-2, -4, 3), (-4, 3, 2), (-5, -2, 6), (-1, 7, 4),
             (-6, 2, 3), (-3, -5, 2), (-2, 6, 5), (-7, 3, 4), (-4, -3, 7),
             (-5, 4, 2), (-2, -7, 3), (-6, 5, 4), (-3, 8, 6), (-8, -2, 5)]),
         },
        {"sr": "Šķiro racionālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir negatīvs vesels skaitlis?",
              ["−4", "−0,4", "{1|4}", "4"], 0),
             ("Kurš skaitlis nav vesels?", ["−2,5", "−2", "0", "25"], 0),
             ("Kurš skaitlis ir gan vesels, gan pozitīvs?",
              ["7", "−7", "0,7", "−0,7"], 0),
             ("Kurš skaitlis ir lielākais?", ["2", "−2", "−5", "−10"], 0),
             ("Kurš skaitlis ir mazākais?", ["−6", "−3", "0", "3"], 0),
             ("Kurš skaitlis ir tuvāk nullei?", ["−1", "−4", "5", "−9"], 0),
             ("Kurus skaitļus sauc par pretējiem?",
              ["−3 un 3", "−3 un −3", "3 un 6", "0 un 3"], 0),
             ("Kurš skaitlis ir gan negatīvs, gan daļa?",
              ["−{2|3}", "{2|3}", "−3", "3"], 0),
         ]},
        {"sr": "Plāno un pārbauda aprēķinu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nosaka vispirms, reizinot divus skaitļus ar zīmēm?",
              ["rezultāta zīmi", "moduli", "kāpinātāju", "iekavas"], 0),
             ("Kas jādara, ja izteiksmē ir gan daļas, gan decimāldaļas?",
              ["jāpāriet uz viena veida daļskaitļiem",
               "jāsāk no kreisās puses", "jānoapaļo", "jāizlaiž iekavas"], 0),
             ("Kāpēc rezultātu novērtē pirms aprēķina?",
              ["lai pamanītu rupju kļūdu", "lai nerēķinātu",
               "lai zustu zīme", "lai būtu īsāk"], 0),
             ("Kura darbība izpildāma pirmā?",
              ["darbības iekavās", "saskaitīšana", "atņemšana",
               "no kreisās uz labo"], 0),
             ("Kāda ir darbību secība?",
              ["iekavas, kāpināšana, reizināšana, saskaitīšana",
               "no kreisās uz labo", "saskaitīšana vispirms",
               "kāpināšana pēdējā"], 0),
             ("Vai saskaitāmos var mainīt vietām?",
              ["jā, summa nemainās", "nē", "tikai pozitīvus",
               "tikai negatīvus"], 0),
             ("Kā pārbauda dalīšanas rezultātu?",
              ["reizina dalījumu ar dalītāju", "saskaita skaitļus",
               "maina zīmi", "dala vēlreiz"], 0),
             ("Cik ir jebkura skaitļa reizinājums ar nulli?",
              ["0", "1", "pats skaitlis", "pretējais skaitlis"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 6,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 6.8. temata noslēgumā. "
                "Pārbauda pozitīvu un negatīvu skaitļu reizināšanu un "
                "dalīšanu, kāpināšanu, darbību secību izteiksmēs ar "
                "iekavām un racionāla skaitļa jēdzienu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Nosaka reizinājuma un dalījuma zīmi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(zime, [
             (-7, -2), (6, -5), (-3, 8), (-9, -4), (5, -11), (-2, 6),
             (-8, -7), (12, -3), (-4, 9), (-6, -8), (10, -2), (-5, 7),
             (-11, -3), (4, -9), (-10, 5)]),
         },
        {"sr": "Reizina un dala racionālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(reizina, [
             (-6, 9), (-8, -5), (7, -6), (-11, 4), (-9, -3), (12, -5),
             (-4, 13)])
             + V.kopa(dala, [
                 (-48, -8), (-75, 5), (84, -7), (-90, -9), (66, -6),
                 (-52, 4), (-96, -12), (100, -5)])),
         },
        {"sr": "Kāpina racionālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kapina, [
             (-4, 2), (-3, 3), (-6, 2), (-2, 4), (-7, 2), (-1, 5),
             (-5, 3), (-8, 2), (-2, 5), (-9, 2), (-10, 2), (-1, 6),
             (-11, 2), (-4, 3), (-12, 2)]),
         },
        {"sr": "Ievēro darbību secību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(reiz_sask, [
             (-4, 2, -5), (15, -3, 4), (22, -4, 3), (-7, 5, -2),
             (19, -2, 6), (-11, 4, -3), (8, -6, 2), (-5, -3, 7),
             (27, -4, 5), (-13, 2, 8), (16, -5, -2), (-9, 7, 3),
             (24, -3, 6), (-14, 5, 2), (13, -2, -7)]),
         },
        {"sr": "Aprēķina izteiksmes ar iekavām",
         "stunda": TEMATS,
         "jautajumi": V.kopa(iekavas, [
             (-5, 3, 7), (-4, 6, 14), (3, 2, 11), (-6, 9, 3), (5, 1, 8),
             (-2, 12, 5), (4, -3, 6), (-7, 5, 2), (6, 4, 13), (-3, 8, 1),
             (2, -6, 4), (-9, 7, 3), (8, 2, 9), (-4, -5, 7), (7, 6, 15)]),
         },
        {"sr": "Šķiro racionālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir racionāls skaitlis?",
              ["skaitlis, ko var pierakstīt kā {m|n}",
               "tikai vesels skaitlis", "tikai pozitīvs skaitlis",
               "tikai decimāldaļa"], 0),
             ("Kurš skaitlis ir negatīvs vesels skaitlis?",
              ["−9", "−0,9", "{1|9}", "9"], 0),
             ("Vai −7 ir racionāls skaitlis?",
              ["jā, jo −7 = {−7|1}", "nē", "tikai ar moduli",
               "tikai ar iekavām"], 0),
             ("Kurš skaitlis nav vesels?", ["−3,5", "−3", "0", "35"], 0),
             ("Kurš skaitlis ir tuvāk nullei?", ["−2", "−5", "6", "−8"], 0),
             ("Kā racionālu skaitli pieraksta 0,4?",
              ["{2|5}", "{4|1}", "{1|4}", "{5|2}"], 0),
             ("Kā racionālu skaitli pieraksta −2,5?",
              ["−{5|2}", "{5|2}", "−{2|5}", "{25|1}"], 0),
             ("Kurus skaitļus sauc par pretējiem?",
              ["−6 un 6", "−6 un −6", "6 un 12", "0 un 6"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Reizina, dala un kāpina racionālus skaitļus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Aprēķini",
             lambda a, b, c, d, e, n: [
                 ("%s · %s = ……" % (V.iek(a), V.iek(b)), V.sk(a * b)),
                 ("%s : %s = ……" % (V.iek(c), V.iek(d)), V.sk(c // d)),
                 ("%s² = ……" % V.iek(e), V.sk(e * e)),
                 ("%s%s = ……" % (V.iek(-2), KAPES[n - 2]),
                  V.sk((-2) ** n))],
             [(-7, 6, -54, -9, -3, 4), (-8, -5, 36, -6, -5, 3),
              (9, -4, -72, 8, -6, 5), (-6, 7, -63, -7, -4, 2),
              (-9, -3, 48, -6, -7, 3), (5, -8, -55, 5, -2, 4),
              (-4, 11, -84, -12, -8, 2), (-12, -2, 90, -9, -3, 5),
              (7, -7, -64, 8, -9, 2), (-5, 9, -56, -8, -10, 3),
              (-11, -4, 75, -5, -6, 4), (6, -9, -96, 12, -4, 5),
              (-3, 13, -42, -6, -11, 2), (-10, -6, 88, -8, -5, 4),
              (8, -5, -78, 6, -7, 3)]),
         },
        {"sr": "Aprēķina izteiksmes, ievērojot darbību secību",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Izteiksmes",
             lambda a, b, c, d, e, f, g: [
                 ("%s + %s · %s = ……" % (V.sk(a), V.sk(b), V.iek(c)),
                  V.sk(a + b * c)),
                 ("%s · (%s − %s) = ……" % (V.iek(d), V.sk(e), V.sk(f)),
                  V.sk(d * (e - f))),
                 ("%s² − 3 · 4 = ……" % V.iek(g), V.sk(g * g - 12))],
             [(-6, 4, -3, -4, 2, 9, -5), (-8, 5, -2, -3, 6, 11, -4),
              (-10, 3, -4, -6, 4, 9, -6), (-5, 6, -3, -2, 7, 12, -3),
              (-7, 2, -8, -5, 3, 8, -7), (-9, 4, -2, -4, 5, 10, -2),
              (-12, 3, -5, -7, 2, 6, -8), (-4, 7, -3, -3, 9, 14, -5),
              (-11, 5, -2, -6, 3, 7, -4), (-6, 8, -2, -2, 11, 15, -6),
              (-13, 4, -3, -5, 6, 10, -3), (-3, 9, -4, -8, 2, 5, -7),
              (-14, 2, -6, -4, 8, 13, -2), (-15, 6, -2, -9, 3, 4, -9),
              (-2, 11, -3, -7, 5, 9, -10)]),
         },
        {"sr": "Risina uzdevumu ar racionāliem skaitļiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda sak, solis, n, m: {
                 "teksts": "Naktī temperatūra ik stundu pazeminājās par "
                           "%s °C; sākumā tā bija %s °C.   a) Uzraksti "
                           "izteiksmi temperatūrai pēc %d stundām!   "
                           "b) Aprēķini to!   c) Kāda temperatūra bija pēc "
                           "%d stundām?   d) Par cik grādiem temperatūra "
                           "pazeminājās %d stundās?"
                           % (V.sk(solis), V.sk(sak), n, m, n),
                 "kriteriji": [
                     "a) %s + %d · (−%s).   (1 p.)"
                     % (V.sk(sak), n, V.sk(solis)),
                     "b) %s − %s = %s °C.   (1 p.)"
                     % (V.sk(sak), V.sk(n * solis), V.sk(sak - n * solis)),
                     "c) %s + %d · (−%s) = %s °C.   (1 p.)"
                     % (V.sk(sak), m, V.sk(solis), V.sk(sak - m * solis)),
                     "d) %s °C.   (1 p.)" % V.sk(n * solis)]},
             [(4, 3, 5, 2), (2, 4, 4, 1), (6, 2, 7, 3), (1, 5, 3, 2),
              (8, 3, 6, 2), (3, 6, 2, 1), (5, 4, 5, 3), (0, 3, 8, 4),
              (7, 5, 4, 2), (9, 2, 9, 5), (2, 7, 3, 1), (10, 4, 6, 3),
              (4, 6, 4, 2), (6, 5, 5, 3), (1, 8, 2, 1)]),
         },
        {"sr": "Skaidro zīmju likumus un darbību secību",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Zīmju likums",
             lambda a, b: {
                 "ievads": "Dotas izteiksmes  %s · %s  un  %s · %s."
                           % (V.iek(-a), V.sk(b), V.iek(-a), V.iek(-b)),
                 "jaut": [("Aprēķini abas izteiksmes!", 1),
                          ("Kāpēc rezultātu zīmes ir dažādas?", 1),
                          ("Uzraksti savu piemēru ar pozitīvu "
                           "reizinājumu!", 1)],
                 "atbildes": [
                     "1) %s un %s.   (1 p.)" % (V.sk(-a * b), V.sk(a * b)),
                     "2) Ja zīmes ir dažādas, reizinājums ir negatīvs; ja "
                     "vienādas — pozitīvs.   (1 p.)",
                     "3) Piemēram, %s · %s = %s.   (1 p.)"
                     % (V.iek(-a), V.iek(-b), V.sk(a * b))]},
             [(4, 3), (5, 2), (6, 4), (3, 7), (8, 2), (7, 5), (9, 3),
              (2, 11), (6, 6), (10, 4), (5, 9), (12, 2), (4, 8), (11, 3),
              (7, 7)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
