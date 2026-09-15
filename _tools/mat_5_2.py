# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.2. Kā lieto skaitļa sadalīšanu reizinātājos?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.2. temats): darbību secība un
sadalāmības īpašība, skaitļa sadalīšana reizinātājos un pirmreizinātājos,
dalītāji un dalāmie, pirmskaitļi un salikti skaitļi, dalāmības pazīmes,
mazākais kopīgais dalāmais un pakāpes pieraksts.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.2."
NOSAUKUMS = "Kā lieto skaitļa sadalīšanu reizinātājos?"

ATGADNE = [
    "Pirmskaitlis dalās tikai ar 1 un ar sevi; skaitlis 1 nav ne "
    "pirmskaitlis, ne salikts skaitlis.",
    "Vienādu reizinātāju reizinājumu pieraksta kā pakāpi:   5 · 5 · 5 · 5 = "
    "5⁴      (5 — bāze, 4 — kāpinātājs)",
    "Darbību sadalāmība:   b · a + c · a = (b + c) · a      ·      "
    "b : a + c : a = (b + c) : a",
]

KAPES = "²³⁴⁵⁶⁷"          # kāpinātāju zīmes 2..7

PIRMIE = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def pirmreizinataji(n):
    """Skaitļa sadalījums pirmreizinātājos kā teksts:  «2 · 2 · 3»."""
    out, d = [], 2
    while n > 1:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    return " · ".join(str(x) for x in out)


def lkd(a, b):
    while b:
        a, b = b, a % b
    return a


# ---------------------------------------------------------------- veidnes
def seciba(a, b, c):
    """Darbību secība: reizināšana pirms saskaitīšanas."""
    return ("Cik ir %d + %d · %d?" % (a, b, c),
            V.izvele(a + b * c, (a + b) * c, a + b + c, a * b + c,
                     a * (b + c), a + b * c + 1), 0)


def sadala(n):
    """Sadalīšana pirmreizinātājos."""
    return ("Sadali %d pirmreizinātājos!" % n,
            V.izvele(pirmreizinataji(n), pirmreizinataji(n + 1),
                     pirmreizinataji(n * 2), pirmreizinataji(n - 1),
                     "%d · 1" % n, pirmreizinataji(n + 2)), 0)


def dalitaji(n):
    """Cik dalītāju ir skaitlim."""
    d = [x for x in range(1, n + 1) if n % x == 0]
    return ("Cik dalītāju ir skaitlim %d?" % n,
            V.izvele(len(d), len(d) + 1, len(d) - 1, n, len(d) + 2,
                     len(d) * 2), 0)


def dalams(n, d):
    """Vai skaitlis dalās ar doto dalītāju."""
    ir = n % d == 0
    return ("Vai %d dalās ar %d?" % (n, d),
            V.izvele("jā" if ir else "nē", "nē" if ir else "jā",
                     "tikai ar atlikumu", "nevar noteikt"), 0)


def pirmskaitlis(n):
    """Vai skaitlis ir pirmskaitlis."""
    ir = n in PIRMIE
    return ("Vai %d ir pirmskaitlis?" % n,
            V.izvele("jā" if ir else "nē", "nē" if ir else "jā",
                     "tas ir 1", "nevar noteikt"), 0)


def mkd(a, b):
    """Mazākais kopīgais dalāmais."""
    m = a * b // lkd(a, b)
    return ("Kāds ir skaitļu %d un %d mazākais kopīgais dalāmais?" % (a, b),
            V.izvele(m, a * b, a + b, lkd(a, b), m + a, m * 2), 0)


def pakape(a, n):
    """Pakāpes skaitliskā vērtība."""
    return ("Cik ir %d%s?" % (a, KAPES[n - 2]),
            V.izvele(a ** n, a * n, a + n, n ** a, a ** n + 1,
                     a ** n - 1, 2 * a ** n), 0)


def nezinamais(a, x):
    """Nezināmais reizinājuma vienādībā."""
    return ("Atrisini:  %d · x = %d." % (a, a * x),
            V.izvele(x, a * x, a, a * x * a, x + 1, a + x), 0)


FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.2. temata beigās. Pārbauda darbību "
                "secību, sadalīšanu reizinātājos, dalītājus un dalāmos, "
                "pirmskaitļus, dalāmības pazīmes, mazāko kopīgo dalāmo un "
                "pakāpes pierakstu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Ievēro darbību secību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(seciba, [
             (12, 3, 4), (25, 5, 6), (18, 7, 2), (30, 4, 8), (45, 6, 3),
             (50, 9, 2), (16, 8, 5), (72, 3, 7), (64, 2, 9), (80, 5, 4),
             (36, 6, 6), (90, 4, 5), (28, 7, 3), (100, 8, 2),
             (55, 9, 4)]),
         },
        {"sr": "Lieto darbību sadalāmības īpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko vienāds  b · a + c · a?",
              ["(b + c) · a", "b · c · a", "(b + c) + a", "b + c · a"], 0),
             ("Ar ko vienāds  7 · 4 + 3 · 4?",
              ["10 · 4", "7 · 3 · 4", "10 + 4", "7 · 7"], 0),
             ("Ar ko vienāds  9 · 5 − 4 · 5?",
              ["5 · 5", "13 · 5", "9 · 4", "5 + 5"], 0),
             ("Ar ko vienāds  b : a + c : a?",
              ["(b + c) : a", "b : c : a", "(b + c) + a", "b + c : a"], 0),
             ("Cik ir  12 : 3 + 9 : 3?", ["7", "21", "4", "3"], 0),
             ("Kā ātrāk aprēķināt  25 · 8 + 25 · 2?",
              ["25 · 10", "25 · 16", "50 · 10", "25 + 10"], 0),
             ("Kāpēc lieto sadalāmības īpašību?",
              ["lai aprēķinu vienkāršotu", "lai skaitļi augtu",
               "tā prasa noteikumi", "tas nav vajadzīgs"], 0),
             ("Ar ko vienāds  6 · (10 + 3)?",
              ["6 · 10 + 6 · 3", "6 · 10 + 3", "6 + 10 · 3",
               "6 · 13 · 3"], 0),
         ]},
        {"sr": "Sadala skaitli pirmreizinātājos",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sadala, [
             12, 18, 20, 24, 28, 30, 36, 40, 42, 45, 50, 54, 60, 63, 72]),
         },
        {"sr": "Nosaka skaitļa dalītājus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dalitaji, [
             6, 8, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30]),
         },
        {"sr": "Nosaka, vai skaitlis dalās",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dalams, [
             (48, 6), (51, 4), (72, 9), (85, 3), (96, 8), (77, 6),
             (105, 5), (91, 4), (144, 12), (118, 7), (150, 6), (133, 9),
             (168, 8), (125, 4), (180, 15)]),
         },
        {"sr": "Atšķir pirmskaitļus no saliktiem skaitļiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(pirmskaitlis, [
             7, 9, 13, 15, 17, 21, 23, 25, 29, 33, 31, 35, 37, 39, 41]),
         },
        {"sr": "Lieto dalāmības pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko dalās skaitlis, kas beidzas ar 0?",
              ["ar 2, 5 un 10", "tikai ar 2", "tikai ar 5",
               "ne ar ko"], 0),
             ("Kā pazīst skaitli, kas dalās ar 2?",
              ["tas beidzas ar pāra ciparu", "tas beidzas ar 5",
               "ciparu summa dalās ar 2", "tas ir liels"], 0),
             ("Kā pazīst skaitli, kas dalās ar 5?",
              ["tas beidzas ar 0 vai 5", "tas beidzas ar pāra ciparu",
               "ciparu summa dalās ar 5", "tas ir nepāra"], 0),
             ("Kā pazīst skaitli, kas dalās ar 3?",
              ["ciparu summa dalās ar 3", "tas beidzas ar 3",
               "tas ir nepāra", "tas beidzas ar 0"], 0),
             ("Kā pazīst skaitli, kas dalās ar 9?",
              ["ciparu summa dalās ar 9", "tas beidzas ar 9",
               "tas ir nepāra", "tas beidzas ar 0"], 0),
             ("Vai 234 dalās ar 3?", ["jā", "nē", "tikai ar atlikumu",
                                      "nevar noteikt"], 0),
             ("Vai 4725 dalās ar 5?", ["jā", "nē", "tikai ar atlikumu",
                                       "nevar noteikt"], 0),
             ("Vai 1287 dalās ar 9?", ["jā", "nē", "tikai ar atlikumu",
                                       "nevar noteikt"], 0),
         ]},
        {"sr": "Nosaka mazāko kopīgo dalāmo",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mkd, [
             (4, 6), (6, 8), (3, 5), (9, 12), (10, 15), (8, 12), (5, 7),
             (14, 21), (6, 10), (12, 18), (9, 15), (16, 24), (7, 11),
             (20, 30), (18, 27)]),
         },
        {"sr": "Zina pakāpes pierakstu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta  5 · 5 · 5 · 5?", ["5⁴", "4⁵", "5 · 4",
                                               "20"], 0),
             ("Kā sauc skaitli, ko reizina?", ["bāze", "kāpinātājs",
                                               "pakāpe", "dalītājs"], 0),
             ("Kā sauc skaitli, kas rāda reizinātāju skaitu?",
              ["kāpinātājs", "bāze", "pakāpe", "dalītājs"], 0),
             ("Ko nozīmē 2⁵?", ["2 · 2 · 2 · 2 · 2", "2 · 5", "5 · 5",
                                "2 + 5"], 0),
             ("Kā lasa pierakstu 3²?", ["trīs kvadrātā", "trīs reiz divi",
                                        "divi kvadrātā", "trīs plus divi"],
              0),
             ("Kā lasa pierakstu 4³?", ["četri kubā", "trīs kubā",
                                        "četri reiz trīs", "divpadsmit"], 0),
             ("Cik ir 1 jebkurā pakāpē?", ["1", "0", "pakāpes skaitlis",
                                           "tas ir dažādi"], 0),
             ("Kā pieraksta  a · a · a?", ["a³", "3a", "a · 3", "3³"], 0),
         ]},
        {"sr": "Aprēķina pakāpes vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(pakape, [
             (2, 3), (3, 2), (5, 2), (2, 4), (4, 3), (10, 3), (3, 3),
             (6, 2), (2, 5), (7, 2), (8, 2), (9, 2), (10, 2), (5, 3),
             (4, 2)]),
         },
        {"sr": "Aprēķina nezināmo reizinājuma vienādībā",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nezinamais, [
             (3, 7), (4, 6), (5, 8), (6, 9), (7, 4), (8, 5), (9, 3),
             (12, 6), (11, 7), (2, 15), (15, 4), (13, 5), (14, 3),
             (16, 2), (20, 6)]),
         },
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("24 ābolus sadala vienādi 6 grozos. Cik katrā?",
              ["4", "18", "30", "144"], 0),
             ("Konfektes pa 5 kastītēs; kopā 45. Cik kastīšu?",
              ["9", "40", "50", "225"], 0),
             ("Divi autobusi brauc ik pēc 4 un 6 minūtēm. Pēc cik minūtēm "
              "tie sakrīt?", ["12", "10", "24", "2"], 0),
             ("Skolēnus var sadalīt gan 3, gan 4 vienādās grupās. Cik "
              "mazākais skolēnu skaits?", ["12", "7", "24", "1"], 0),
             ("36 burtnīcas sadala vienādās pakās. Cik dažādos veidos to "
              "var izdarīt?", ["9", "6", "36", "4"], 0),
             ("Kastē 48 olas pa 6 rindās. Cik olu rindā?",
              ["8", "42", "54", "288"], 0),
             ("Divas lampiņas mirgo ik pēc 6 un 8 sekundēm. Pēc cik "
              "sekundēm kopā?", ["24", "14", "48", "2"], 0),
             ("Cik ir 2³ · 5?", ["40", "30", "16", "13"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.2. temata noslēgumā. "
                "Pārbauda darbību secību, sadalīšanu pirmreizinātājos, "
                "dalītājus, pirmskaitļus, dalāmības pazīmes, mazāko kopīgo "
                "dalāmo un pakāpes.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Ievēro darbību secību un sadalāmības īpašību",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(seciba, [
             (15, 4, 5), (28, 6, 3), (40, 7, 2), (55, 3, 8), (66, 5, 4),
             (24, 9, 3), (81, 2, 7)])
             + [("Ar ko vienāds  b · a + c · a?",
                 ["(b + c) · a", "b · c · a", "(b + c) + a",
                  "b + c · a"], 0),
                ("Ar ko vienāds  7 · 4 + 3 · 4?",
                 ["10 · 4", "7 · 3 · 4", "10 + 4", "7 · 7"], 0),
                ("Ar ko vienāds  9 · 5 − 4 · 5?",
                 ["5 · 5", "13 · 5", "9 · 4", "5 + 5"], 0),
                ("Cik ir  12 : 3 + 9 : 3?", ["7", "21", "4", "3"], 0),
                ("Kā ātrāk aprēķināt  25 · 8 + 25 · 2?",
                 ["25 · 10", "25 · 16", "50 · 10", "25 + 10"], 0),
                ("Ar ko vienāds  6 · (10 + 3)?",
                 ["6 · 10 + 6 · 3", "6 · 10 + 3", "6 + 10 · 3",
                  "6 · 13 · 3"], 0),
                ("Ar ko vienāds  b : a + c : a?",
                 ["(b + c) : a", "b : c : a", "(b + c) + a",
                  "b + c : a"], 0),
                ("Kāpēc lieto sadalāmības īpašību?",
                 ["lai aprēķinu vienkāršotu", "lai skaitļi augtu",
                  "tā prasa noteikumi", "tas nav vajadzīgs"], 0)]),
         },
        {"sr": "Sadala skaitli reizinātājos un nosaka dalītājus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(sadala, [
             16, 22, 26, 32, 33, 44, 48])
             + V.kopa(dalitaji, [
                 9, 11, 22, 26, 32, 33, 35, 36])),
         },
        {"sr": "Atšķir pirmskaitļus un lieto dalāmības pazīmes",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(pirmskaitlis, [
             11, 19, 27, 43, 45, 47, 49])
             + V.kopa(dalams, [
                 (54, 6), (63, 4), (81, 9), (95, 3), (108, 8), (87, 6),
                 (115, 5), (99, 4)])),
         },
        {"sr": "Nosaka mazāko kopīgo dalāmo",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mkd, [
             (4, 10), (6, 9), (3, 7), (8, 10), (12, 15), (5, 6), (9, 21),
             (10, 12), (14, 35), (15, 20), (16, 20), (11, 22), (18, 24),
             (21, 28), (25, 30)]),
         },
        {"sr": "Lieto kāpināšanu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(pakape, [
             (2, 2), (3, 4), (6, 3), (7, 3), (11, 2), (12, 2), (2, 6)])
             + [("Kā pieraksta  5 · 5 · 5 · 5?", ["5⁴", "4⁵", "5 · 4",
                                                  "20"], 0),
                ("Kā sauc skaitli, ko reizina?", ["bāze", "kāpinātājs",
                                                  "pakāpe", "dalītājs"], 0),
                ("Ko nozīmē 2⁵?", ["2 · 2 · 2 · 2 · 2", "2 · 5", "5 · 5",
                                   "2 + 5"], 0),
                ("Kā lasa pierakstu 3²?", ["trīs kvadrātā",
                                           "trīs reiz divi",
                                           "divi kvadrātā",
                                           "trīs plus divi"], 0),
                ("Kā lasa pierakstu 4³?", ["četri kubā", "trīs kubā",
                                           "četri reiz trīs",
                                           "divpadsmit"], 0),
                ("Cik ir 1 jebkurā pakāpē?", ["1", "0",
                                              "pakāpes skaitlis",
                                              "tas ir dažādi"], 0),
                ("Kā pieraksta  a · a · a?", ["a³", "3a", "a · 3",
                                              "3³"], 0),
                ("Kā sauc skaitli, kas rāda reizinātāju skaitu?",
                 ["kāpinātājs", "bāze", "pakāpe", "dalītājs"], 0)]),
         },
        {"sr": "Aprēķina nezināmo un risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(nezinamais, [
             (3, 9), (4, 8), (5, 6), (6, 7), (7, 5), (8, 4), (9, 6)])
             + [("24 ābolus sadala vienādi 6 grozos. Cik katrā?",
                 ["4", "18", "30", "144"], 0),
                ("Konfektes pa 5 kastītēs; kopā 45. Cik kastīšu?",
                 ["9", "40", "50", "225"], 0),
                ("Divi autobusi brauc ik pēc 4 un 6 minūtēm. Pēc cik "
                 "minūtēm tie sakrīt?", ["12", "10", "24", "2"], 0),
                ("Skolēnus var sadalīt gan 3, gan 4 vienādās grupās. Cik "
                 "mazākais skolēnu skaits?", ["12", "7", "24", "1"], 0),
                ("Kastē 48 olas pa 6 rindās. Cik olu rindā?",
                 ["8", "42", "54", "288"], 0),
                ("Divas lampiņas mirgo ik pēc 6 un 8 sekundēm. Pēc cik "
                 "sekundēm kopā?", ["24", "14", "48", "2"], 0),
                ("Cik ir 2³ · 5?", ["40", "30", "16", "13"], 0),
                ("36 burtnīcas sadala vienādās pakās. Cik dažādos veidos "
                 "to var izdarīt?", ["9", "6", "36", "4"], 0)]),
         },
    ],
    "uzdevumi": [
        {"sr": "Kāpina, nosaka dalītājus un mazāko kopīgo dalāmo",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, n, x, y: [
                 ("%d%s = ……" % (a, KAPES[n - 2]), V.sk(a ** n)),
                 ("%d = …… (pirmreizinātājos)" % (x * y),
                  pirmreizinataji(x * y)),
                 ("Skaitļa %d dalītāju skaits:   ……" % (x * y),
                  V.sk(len([d for d in range(1, x * y + 1)
                            if (x * y) % d == 0]))),
                 ("%d un %d mazākais kopīgais dalāmais:   ……" % (x, y),
                  V.sk(x * y // lkd(x, y)))],
             [(2, 3, 4, 6), (3, 2, 6, 8), (5, 2, 3, 5), (2, 4, 9, 12),
              (4, 3, 10, 15), (10, 3, 8, 12), (3, 3, 5, 7), (6, 2, 14, 21),
              (2, 5, 6, 10), (7, 2, 12, 18), (8, 2, 9, 15), (9, 2, 16, 24),
              (10, 2, 7, 11), (5, 3, 20, 30), (4, 2, 18, 27)]),
         },
        {"sr": "Sadala pirmreizinātājos un aprēķina nezināmo",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Reizinātāji un nezināmais",
             lambda n, a, x: [
                 ("%d = …… (pirmreizinātājos)" % n, pirmreizinataji(n)),
                 ("%d · x = %d;   x = ……" % (a, a * x), V.sk(x)),
                 ("Vai %d ir pirmskaitlis?   ……" % n,
                  "jā" if n in PIRMIE else "nē")],
             [(12, 3, 7), (18, 4, 6), (20, 5, 8), (24, 6, 9), (28, 7, 4),
              (30, 8, 5), (36, 9, 3), (40, 12, 6), (42, 11, 7), (45, 2, 15),
              (50, 15, 4), (54, 13, 5), (60, 14, 3), (63, 16, 2),
              (72, 20, 6)]),
         },
        {"sr": "Lieto sadalīšanu reizinātājos situāciju uzdevumā",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda a, b: {
                 "teksts": "Viens autobuss no pieturas atiet ik pēc "
                           "%d minūtēm, otrs — ik pēc %d minūtēm; plkst. "
                           "8.00 abi atiet reizē.   a) Sadali abus skaitļus "
                           "pirmreizinātājos!   b) Aprēķini mazāko kopīgo "
                           "dalāmo!   c) Pēc cik minūtēm tie atkal atiet "
                           "reizē?   d) Cikos tas notiks?" % (a, b),
                 "kriteriji": [
                     "a) %d = %s;  %d = %s.   (1 p.)"
                     % (a, pirmreizinataji(a), b, pirmreizinataji(b)),
                     "b) MKD = %d.   (1 p.)" % (a * b // lkd(a, b)),
                     "c) Pēc %d minūtēm.   (1 p.)" % (a * b // lkd(a, b)),
                     "d) Plkst. 8.%02d.   (1 p.)" % (a * b // lkd(a, b))]},
             [(4, 6), (6, 8), (3, 5), (9, 12), (10, 15), (8, 12), (5, 7),
              (6, 10), (12, 18), (9, 15), (4, 10), (6, 9), (3, 7),
              (8, 10), (5, 6)]),
         },
        {"sr": "Skaidro sadalīšanu reizinātājos un pakāpes pierakstu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Skaitļa reizinātāji",
             lambda n: {
                 "ievads": "Dots skaitlis %d." % n,
                 "jaut": [("Sadali to pirmreizinātājos!", 1),
                          ("Uzskaiti visus tā dalītājus!", 1),
                          ("Vai tas ir pirmskaitlis? Pamato!", 1)],
                 "atbildes": [
                     "1) %d = %s.   (1 p.)" % (n, pirmreizinataji(n)),
                     "2) %s.   (1 p.)"
                     % "; ".join(str(d) for d in range(1, n + 1)
                                 if n % d == 0),
                     "3) Nē — tam ir vairāk nekā divi dalītāji.   (1 p.)"]},
             [12, 18, 20, 24, 28, 30, 36, 40, 42, 45, 50, 54, 60, 63, 72]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
