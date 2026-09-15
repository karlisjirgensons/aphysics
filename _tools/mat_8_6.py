# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.6. Kā skaidro un izpilda darbības ar izteiksmēm?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.6. temats): monoms un
polinoms, to pakāpe un normālforma, binoms un trinoms, monomu saskaitīšana,
reizināšana, dalīšana un kāpināšana, polinomu saskaitīšana un atņemšana,
monoma reizināšana ar polinomu un binoma reizināšana ar binomu.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.6."
NOSAUKUMS = "Kā skaidro un izpilda darbības ar izteiksmēm?"

KAPES = "⁰¹²³⁴⁵⁶⁷⁸⁹"


def kap(n):
    """Kāpinātāja zīme; pirmā pakāpe paliek bez zīmes, negatīvai - mīnuss."""
    if n == 1:
        return ""
    zime, n = ("⁻", -n) if n < 0 else ("", n)
    return zime + "".join(KAPES[int(c)] for c in str(n))


def monoms(k, n):
    """Monoms ka·aⁿ tekstā:  3a²,  a,  −5a³."""
    if n == 0:
        return V.sk(k)
    koef = "" if k == 1 else ("−" if k == -1 else V.sk(k))
    return "%sa%s" % (koef, kap(n))


ATGADNE = [
    "Monomu reizina ar monomu: koeficientus sareizina, pakāpēm ar vienādām "
    "bāzēm kāpinātājus saskaita.   3a² · 4a³ = 12a⁵",
    "Līdzīgus monomus savelk:   3a² + 5a² = 8a²   ·   nelīdzīgus monomus "
    "savilkt nevar:   3a² + 5a³ paliek kā ir.",
    "Monomu ar polinomu reizina pa locekļiem:   k(a + b) = ka + kb   ·   "
    "binomu ar binomu:   (a + b)(c + d) = ac + ad + bc + bd",
]


# ---------------------------------------------------------------- veidnes
def savelk(k1, k2, n):
    """Līdzīgu monomu savilkšana."""
    return ("Savelc:  %s + %s." % (monoms(k1, n), monoms(k2, n)),
            V.izvele(monoms(k1 + k2, n), monoms(k1 * k2, n),
                     monoms(k1 + k2, 2 * n), monoms(k1 + k2, n + 1),
                     monoms(abs(k1 - k2), n), monoms(k1 + k2 + 1, n)), 0)


def reizina(k1, n1, k2, n2):
    """Monomu reizinājums."""
    return ("Vienkāršo:  %s · %s." % (monoms(k1, n1), monoms(k2, n2)),
            V.izvele(monoms(k1 * k2, n1 + n2), monoms(k1 + k2, n1 + n2),
                     monoms(k1 * k2, n1 * n2), monoms(k1 * k2, n1),
                     monoms(k1 * k2, abs(n1 - n2)),
                     monoms(k1 * k2 + 1, n1 + n2)), 0)


def dala(k1, n1, k2, n2):
    """Monomu dalījums (koeficienti un kāpinātāji dalās bez atlikuma)."""
    return ("Vienkāršo:  %s : %s." % (monoms(k1, n1), monoms(k2, n2)),
            V.izvele(monoms(k1 // k2, n1 - n2), monoms(k1 // k2, n1 + n2),
                     monoms(k1 * k2, n1 - n2), monoms(k1 - k2, n1 - n2),
                     monoms(k1 // k2, n2 - n1),
                     monoms(k1 // k2 + 1, n1 - n2)), 0)


def kapina(k, n, p):
    """Monoma kāpināšana."""
    return ("Vienkāršo:  (%s)%s." % (monoms(k, n), kap(p)),
            V.izvele(monoms(k ** p, n * p), monoms(k * p, n * p),
                     monoms(k ** p, n + p), monoms(k ** p, n),
                     monoms(k * p, n + p), monoms(k ** p + 1, n * p)), 0)


def monoms_polinoms(k, a, b):
    """Monoma reizināšana ar binomu:  k(ax + b)."""
    return ("Atver iekavas:  %da(%da + %d)." % (k, a, b),
            V.izvele("%da² + %da" % (k * a, k * b),
                     "%da² + %d" % (k * a, k * b),
                     "%da + %da" % (k * a, k * b),
                     "%da² + %da" % (k * a, b),
                     "%da² + %da" % (a, k * b),
                     "%da²" % (k * a + k * b)), 0)


def binomi(a, b):
    """Binoma reizināšana ar binomu:  (x + a)(x + b)."""
    return ("Atver iekavas:  (a + %d)(a + %d)." % (a, b),
            V.izvele("a² + %da + %d" % (a + b, a * b),
                     "a² + %da + %d" % (a * b, a + b),
                     "a² + %d" % (a * b),
                     "a² + %da + %d" % (a + b, a + b),
                     "a² + %da" % (a + b),
                     "a² + %da + %d" % (a + b, a * b + 1)), 0)


def polinomu_summa(a1, b1, a2, b2):
    """Polinomu saskaitīšana."""
    return ("Saskaiti:  (%da + %d) + (%da + %d)." % (a1, b1, a2, b2),
            V.izvele("%da + %d" % (a1 + a2, b1 + b2),
                     "%da + %d" % (a1 + a2, b1 * b2),
                     "%da + %d" % (a1 * a2, b1 + b2),
                     "%da² + %d" % (a1 + a2, b1 + b2),
                     "%da + %d" % (a1 - a2, b1 - b2),
                     "%da + %d" % (a1 + a2, b1 + b2 + 1)), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.6. temata beigās. Pārbauda monoma un "
                "polinoma jēdzienus, darbības ar monomiem, polinomu "
                "saskaitīšanu un atņemšanu un iekavu atvēršanu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina monoma un polinoma jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir monoms?",
              ["skaitļu un mainīgo pakāpju reizinājums",
               "divu monomu summa", "jebkura izteiksme",
               "tikai skaitlis"], 0),
             ("Kas ir polinoms?", ["monomu summa", "monomu reizinājums",
                                   "viens monoms", "daļa ar mainīgo"], 0),
             ("Kā sauc divu monomu summu?", ["binoms", "trinoms", "monoms",
                                             "koeficients"], 0),
             ("Kā sauc triju monomu summu?", ["trinoms", "binoms", "monoms",
                                              "koeficients"], 0),
             ("Kas ir monoma koeficients?",
              ["skaitliskais reizinātājs", "kāpinātājs", "bāze",
               "mainīgais"], 0),
             ("Kāda ir monoma 5a³ pakāpe?", ["3", "5", "8", "15"], 0),
             ("Kāda ir polinoma a³ + 2a pakāpe?", ["3", "1", "4", "2"], 0),
             ("Kad polinoms ir normālformā?",
              ["kad līdzīgie monomi savilkti", "kad tas ir garš",
               "kad koeficienti ir veseli", "kad tajā nav iekavu"], 0),
         ]},
        {"sr": "Savelk līdzīgus monomus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(savelk, [
             (3, 5, 2), (4, 2, 3), (6, 1, 1), (2, 7, 4), (5, 4, 2),
             (8, 3, 5), (1, 9, 3), (7, 6, 1), (3, 8, 2), (9, 2, 4),
             (4, 6, 3), (10, 5, 1), (2, 12, 5), (11, 4, 2), (6, 9, 3)]),
         },
        {"sr": "Reizina monomus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(reizina, [
             (3, 2, 4, 3), (2, 1, 5, 2), (6, 3, 2, 1), (4, 2, 3, 4),
             (5, 1, 7, 3), (2, 4, 8, 2), (9, 2, 2, 5), (3, 3, 6, 1),
             (7, 1, 4, 4), (8, 2, 5, 3), (2, 6, 3, 2), (10, 1, 2, 7),
             (4, 5, 6, 2), (11, 2, 3, 3), (5, 4, 7, 1)]),
         },
        {"sr": "Dala monomus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dala, [
             (12, 5, 3, 2), (20, 4, 4, 1), (18, 6, 2, 3), (24, 7, 6, 4),
             (30, 5, 5, 2), (16, 8, 4, 3), (36, 6, 9, 2), (28, 9, 7, 5),
             (40, 4, 8, 1), (45, 7, 5, 3), (48, 8, 6, 2), (54, 6, 9, 4),
             (60, 9, 10, 5), (35, 5, 7, 2), (64, 8, 8, 3)]),
         },
        {"sr": "Kāpina monomu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kapina, [
             (2, 1, 3), (3, 2, 2), (2, 3, 2), (4, 1, 2), (5, 2, 2),
             (2, 2, 3), (3, 1, 3), (6, 1, 2), (7, 2, 2), (2, 4, 2),
             (8, 1, 2), (3, 3, 2), (9, 2, 2), (10, 1, 2), (2, 5, 2)]),
         },
        {"sr": "Saskaita polinomus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(polinomu_summa, [
             (2, 3, 4, 5), (3, 1, 5, 2), (6, 4, 2, 7), (4, 2, 3, 6),
             (5, 8, 7, 1), (2, 9, 8, 3), (9, 5, 2, 4), (3, 7, 6, 2),
             (7, 3, 4, 8), (8, 6, 5, 9), (2, 11, 3, 4), (10, 2, 2, 5),
             (4, 12, 6, 3), (11, 4, 3, 7), (5, 10, 7, 6)]),
         },
        {"sr": "Atņem polinomus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atņem:  (5a + 7) − (2a + 3).", ["3a + 4", "3a + 10",
                                               "7a + 4", "3a − 4"], 0),
             ("Atņem:  (8a + 2) − (3a + 6).", ["5a − 4", "5a + 8",
                                               "11a − 4", "5a + 4"], 0),
             ("Atņem:  (6a − 1) − (2a − 5).", ["4a + 4", "4a − 6",
                                               "8a + 4", "4a − 4"], 0),
             ("Atņem:  (9a + 4) − (4a + 4).", ["5a", "5a + 8", "13a",
                                               "5a − 8"], 0),
             ("Atņem:  (7a² + 3) − (2a² + 1).", ["5a² + 2", "5a² + 4",
                                                 "9a² + 2", "5a² − 2"], 0),
             ("Kas jāievēro, atņemot polinomu?",
              ["jāmaina visu tā locekļu zīmes", "jāmaina tikai pirmā zīme",
               "zīmes nemainās", "jāizlaiž iekavas"], 0),
             ("Atņem:  (4a + 9) − (4a + 2).", ["7", "8a + 11", "7a",
                                               "−7"], 0),
             ("Atņem:  (10a − 3) − (6a + 2).", ["4a − 5", "4a − 1",
                                                "16a − 5", "4a + 5"], 0),
         ]},
        {"sr": "Reizina monomu ar polinomu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(monoms_polinoms, [
             (2, 3, 4), (3, 2, 5), (4, 1, 6), (5, 3, 2), (2, 6, 7),
             (6, 2, 3), (3, 5, 8), (7, 1, 4), (8, 3, 5), (4, 4, 9),
             (9, 2, 6), (5, 6, 3), (10, 1, 7), (2, 8, 11), (11, 3, 4)]),
         },
        {"sr": "Reizina binomu ar binomu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(binomi, [
             (2, 3), (1, 4), (3, 5), (2, 6), (4, 7), (1, 8), (5, 2),
             (3, 9), (6, 1), (4, 10), (7, 3), (2, 11), (8, 5), (9, 2),
             (6, 7)]),
         },
        {"sr": "Zina darbību pamatojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Uz kurām īpašībām balstās monomu reizināšana?",
              ["darbību un pakāpju īpašībām", "tikai saskaitīšanu",
               "tikai dalīšanu", "laukuma formulu"], 0),
             ("Kāpēc 3a² + 5a³ nevar savilkt?",
              ["monomi nav līdzīgi", "koeficienti ir dažādi",
               "abi ir pozitīvi", "tos var savilkt"], 0),
             ("Kad monomi ir līdzīgi?",
              ["kad burtu daļa ir vienāda", "kad koeficienti ir vienādi",
               "vienmēr", "kad pakāpes ir dažādas"], 0),
             ("Ar ko var modelēt reizinājumu 3a · 4a?",
              ["taisnstūra laukumu", "riņķa laukumu", "perimetru",
               "tilpumu"], 0),
             ("Kāds polinoms iznāk, reizinot divus binomus?",
              ["parasti trinoms", "vienmēr binoms", "vienmēr monoms",
               "vienmēr skaitlis"], 0),
             ("Cik locekļu iznāk, reizinot binomu ar binomu pirms "
              "savilkšanas?", ["četri", "divi", "trīs", "seši"], 0),
             ("Ar ko vienāds (a + b)²?",
              ["a² + 2ab + b²", "a² + b²", "a² − b²", "2a + 2b"], 0),
             ("Ar ko vienāds (a + b)(a − b)?",
              ["a² − b²", "a² + b²", "a² − 2ab + b²", "a² + 2ab"], 0),
         ]},
        {"sr": "Apraksta figūru lielumus ar izteiksmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas ir 3a un 4a. Kāds ir laukums?",
              ["12a²", "7a", "12a", "7a²"], 0),
             ("Kvadrāta mala ir 5a. Kāds ir laukums?",
              ["25a²", "20a", "10a", "5a²"], 0),
             ("Taisnstūra malas ir a un a + 3. Kāds ir laukums?",
              ["a² + 3a", "2a + 3", "a² + 3", "3a²"], 0),
             ("Kvadrāta mala ir a. Kāds ir perimetrs?",
              ["4a", "a²", "2a", "a + 4"], 0),
             ("Kuba šķautne ir 2a. Kāds ir tilpums?",
              ["8a³", "6a²", "2a³", "8a"], 0),
             ("Taisnstūra malas ir 2a un 5. Kāds ir perimetrs?",
              ["4a + 10", "10a", "2a + 5", "7a"], 0),
             ("Trijstūra pamats ir 4a, augstums — 6a. Kāds ir laukums?",
              ["12a²", "24a²", "10a", "12a"], 0),
             ("Kuba šķautne ir 3a. Kāds ir virsmas laukums?",
              ["54a²", "27a³", "18a²", "9a²"], 0),
         ]},
        {"sr": "Nosaka nezināmo vienādībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds monoms jāieraksta?   3a² · …… = 12a⁵",
              ["4a³", "4a²", "9a³", "4a⁷"], 0),
             ("Kāds monoms jāieraksta?   …… + 5a = 9a",
              ["4a", "14a", "4", "45a"], 0),
             ("Kāds monoms jāieraksta?   20a⁶ : …… = 4a²",
              ["5a⁴", "5a³", "16a⁴", "5a⁸"], 0),
             ("Kāds skaitlis jāieraksta?   (2a)…… = 8a³",
              ["3", "2", "4", "6"], 0),
             ("Kāds monoms jāieraksta?   …… · 3a = 15a⁴",
              ["5a³", "5a⁴", "12a³", "5a⁵"], 0),
             ("Kāds polinoms jāieraksta?   (3a + 2) + …… = 7a + 5",
              ["4a + 3", "4a + 7", "10a + 3", "4a − 3"], 0),
             ("Kāds polinoms jāieraksta?   (6a + 8) − …… = 2a + 3",
              ["4a + 5", "4a + 11", "8a + 5", "4a − 5"], 0),
             ("Kā pārbauda atrasto monomu?",
              ["ievieto to vienādībā", "salīdzina koeficientus",
               "saskaita pakāpes", "uzzīmē grafiku"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.6. temata noslēgumā. "
                "Pārbauda darbības ar monomiem, polinomu saskaitīšanu un "
                "atņemšanu, iekavu atvēršanu un figūru lielumu aprakstu ar "
                "izteiksmi.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina monoma un polinoma jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir monoms?",
              ["skaitļu un mainīgo pakāpju reizinājums",
               "divu monomu summa", "jebkura izteiksme",
               "tikai skaitlis"], 0),
             ("Kas ir polinoms?", ["monomu summa", "monomu reizinājums",
                                   "viens monoms", "daļa ar mainīgo"], 0),
             ("Kā sauc divu monomu summu?", ["binoms", "trinoms", "monoms",
                                             "koeficients"], 0),
             ("Kāda ir monoma 7a⁴ pakāpe?", ["4", "7", "11", "28"], 0),
             ("Kad monomi ir līdzīgi?",
              ["kad burtu daļa ir vienāda", "kad koeficienti ir vienādi",
               "vienmēr", "kad pakāpes ir dažādas"], 0),
             ("Kāpēc 3a² + 5a³ nevar savilkt?",
              ["monomi nav līdzīgi", "koeficienti ir dažādi",
               "abi ir pozitīvi", "tos var savilkt"], 0),
             ("Ar ko vienāds (a + b)²?",
              ["a² + 2ab + b²", "a² + b²", "a² − b²", "2a + 2b"], 0),
             ("Ar ko vienāds (a + b)(a − b)?",
              ["a² − b²", "a² + b²", "a² − 2ab + b²", "a² + 2ab"], 0),
         ]},
        {"sr": "Savelk un reizina monomus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(savelk, [
             (4, 6, 2), (5, 3, 3), (7, 2, 1), (3, 8, 4), (6, 5, 2),
             (9, 4, 5), (2, 10, 3)])
             + V.kopa(reizina, [
                 (2, 3, 5, 2), (3, 1, 6, 3), (4, 4, 2, 2), (5, 2, 4, 5),
                 (6, 1, 3, 4), (7, 3, 2, 6), (8, 2, 4, 1), (9, 1, 5, 5)])),
         },
        {"sr": "Dala un kāpina monomus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(dala, [
             (15, 6, 3, 2), (24, 5, 4, 1), (21, 7, 3, 3), (32, 8, 8, 4),
             (27, 6, 9, 2), (18, 9, 2, 5), (42, 5, 6, 1)])
             + V.kopa(kapina, [
                 (2, 2, 3), (3, 3, 2), (4, 2, 2), (5, 1, 3), (6, 2, 2),
                 (2, 6, 2), (7, 1, 2), (3, 4, 2)])),
         },
        {"sr": "Saskaita un atņem polinomus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(polinomu_summa, [
             (3, 4, 5, 6), (4, 2, 6, 3), (7, 5, 3, 8), (5, 3, 4, 7),
             (6, 9, 8, 2), (3, 10, 9, 4), (10, 6, 3, 5)])
             + [("Atņem:  (5a + 7) − (2a + 3).", ["3a + 4", "3a + 10",
                                                  "7a + 4", "3a − 4"], 0),
                ("Atņem:  (8a + 2) − (3a + 6).", ["5a − 4", "5a + 8",
                                                  "11a − 4", "5a + 4"], 0),
                ("Atņem:  (6a − 1) − (2a − 5).", ["4a + 4", "4a − 6",
                                                  "8a + 4", "4a − 4"], 0),
                ("Atņem:  (9a + 4) − (4a + 4).", ["5a", "5a + 8", "13a",
                                                  "5a − 8"], 0),
                ("Atņem:  (7a² + 3) − (2a² + 1).", ["5a² + 2", "5a² + 4",
                                                    "9a² + 2",
                                                    "5a² − 2"], 0),
                ("Atņem:  (4a + 9) − (4a + 2).", ["7", "8a + 11", "7a",
                                                  "−7"], 0),
                ("Atņem:  (10a − 3) − (6a + 2).", ["4a − 5", "4a − 1",
                                                   "16a − 5",
                                                   "4a + 5"], 0),
                ("Kas jāievēro, atņemot polinomu?",
                 ["jāmaina visu tā locekļu zīmes",
                  "jāmaina tikai pirmā zīme", "zīmes nemainās",
                  "jāizlaiž iekavas"], 0)]),
         },
        {"sr": "Atver iekavas",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(monoms_polinoms, [
             (3, 4, 5), (4, 2, 6), (5, 1, 7), (6, 3, 3), (2, 7, 8),
             (7, 2, 4), (4, 6, 9)])
             + V.kopa(binomi, [
                 (3, 4), (2, 5), (4, 6), (1, 7), (5, 3), (6, 2), (7, 4),
                 (8, 3)])),
         },
        {"sr": "Apraksta figūru lielumus ar izteiksmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas ir 3a un 4a. Kāds ir laukums?",
              ["12a²", "7a", "12a", "7a²"], 0),
             ("Kvadrāta mala ir 5a. Kāds ir laukums?",
              ["25a²", "20a", "10a", "5a²"], 0),
             ("Taisnstūra malas ir a un a + 3. Kāds ir laukums?",
              ["a² + 3a", "2a + 3", "a² + 3", "3a²"], 0),
             ("Kuba šķautne ir 2a. Kāds ir tilpums?",
              ["8a³", "6a²", "2a³", "8a"], 0),
             ("Taisnstūra malas ir 2a un 5. Kāds ir perimetrs?",
              ["4a + 10", "10a", "2a + 5", "7a"], 0),
             ("Trijstūra pamats ir 4a, augstums — 6a. Kāds ir laukums?",
              ["12a²", "24a²", "10a", "12a"], 0),
             ("Kuba šķautne ir 3a. Kāds ir virsmas laukums?",
              ["54a²", "27a³", "18a²", "9a²"], 0),
             ("Kvadrāta mala ir a. Kāds ir perimetrs?",
              ["4a", "a²", "2a", "a + 4"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Izpilda darbības ar monomiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Darbības ar monomiem",
             lambda k1, n1, k2, n2: [
                 ("%s + %s = ……" % (monoms(k1, n1), monoms(k2, n1)),
                  monoms(k1 + k2, n1)),
                 ("%s · %s = ……" % (monoms(k1, n1), monoms(k2, n2)),
                  monoms(k1 * k2, n1 + n2)),
                 ("%s : %s = ……" % (monoms(k1 * k2, n1 + n2),
                                    monoms(k2, n2)), monoms(k1, n1)),
                 ("(%s)² = ……" % monoms(k2, n2), monoms(k2 * k2, 2 * n2))],
             [(3, 2, 4, 3), (2, 1, 5, 2), (6, 3, 2, 1), (4, 2, 3, 4),
              (5, 1, 7, 3), (2, 4, 8, 2), (9, 2, 2, 5), (3, 3, 6, 1),
              (7, 1, 4, 4), (8, 2, 5, 3), (2, 6, 3, 2), (10, 1, 2, 7),
              (4, 5, 6, 2), (11, 2, 3, 3), (5, 4, 7, 1)]),
         },
        {"sr": "Atver iekavas",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Iekavu atvēršana",
             lambda k, a, b, c: [
                 ("%da(%da + %d) = ……" % (k, a, b),
                  "%da² + %da" % (k * a, k * b)),
                 ("(a + %d)(a + %d) = ……" % (b, c),
                  "a² + %da + %d" % (b + c, b * c)),
                 ("(%da + %d) + (%da + %d) = ……" % (a, b, k, c),
                  "%da + %d" % (a + k, b + c))],
             [(2, 3, 4, 5), (3, 2, 5, 6), (4, 1, 6, 7), (5, 3, 2, 8),
              (2, 6, 7, 3), (6, 2, 3, 9), (3, 5, 8, 2), (7, 1, 4, 10),
              (8, 3, 5, 4), (4, 4, 9, 6), (9, 2, 6, 5), (5, 6, 3, 7),
              (10, 1, 7, 8), (2, 8, 11, 3), (11, 3, 4, 9)]),
         },
        {"sr": "Apraksta figūras lielumus ar izteiksmi",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Figūra un izteiksme",
             lambda k, b, x: {
                 "teksts": "Taisnstūra viena mala ir %da, otra — par "
                           "%d garāka.   a) Pieraksti otro malu ar "
                           "izteiksmi!   b) Pieraksti perimetru un "
                           "vienkāršo to!   c) Pieraksti laukumu un atver "
                           "iekavas!   d) Aprēķini laukumu, ja a = %d!"
                           % (k, b, x),
                 "kriteriji": [
                     "a) %da + %d.   (1 p.)" % (k, b),
                     "b) 2(%da + %da + %d) = %da + %d.   (1 p.)"
                     % (k, k, b, 4 * k, 2 * b),
                     "c) %da(%da + %d) = %da² + %da.   (1 p.)"
                     % (k, k, b, k * k, k * b),
                     "d) %d · %d² + %d · %d = %d.   (1 p.)"
                     % (k * k, x, k * b, x, k * k * x * x + k * b * x)]},
             [(2, 3, 4), (3, 2, 5), (4, 1, 3), (5, 4, 2), (2, 6, 7),
              (6, 3, 2), (3, 5, 6), (7, 2, 3), (8, 4, 2), (4, 7, 5),
              (9, 1, 4), (5, 6, 3), (10, 3, 2), (2, 8, 6), (11, 2, 4)]),
         },
        {"sr": "Pamato darbības ar polinomiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Binomu reizinājums",
             lambda a, b: {
                 "ievads": "Dots reizinājums  (a + %d)(a + %d)." % (a, b),
                 "jaut": [("Atver iekavas!", 1),
                          ("Savelc līdzīgos locekļus!", 1),
                          ("Cik liela ir iegūtā polinoma pakāpe?", 1)],
                 "atbildes": [
                     "1) a² + %da + %da + %d.   (1 p.)" % (b, a, a * b),
                     "2) a² + %da + %d.   (1 p.)" % (a + b, a * b),
                     "3) Otrā pakāpe.   (1 p.)"]},
             [(2, 3), (1, 4), (3, 5), (2, 6), (4, 7), (1, 8), (5, 2),
              (3, 9), (6, 1), (4, 10), (7, 3), (2, 11), (8, 5), (9, 2),
              (6, 7)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
