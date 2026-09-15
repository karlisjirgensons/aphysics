# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.2. Kā skaidro un lieto pakāpi ar veselu kāpinātāju?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.2. temats): bāze, kāpinātājs
un pakāpe, pakāpju īpašības ar vienādām bāzēm, pakāpes, reizinājuma un daļas
kāpināšana, pakāpe ar nulles un negatīvu kāpinātāju un skaitļa normālforma.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.2."
NOSAUKUMS = "Kā skaidro un lieto pakāpi ar veselu kāpinātāju?"

KAPES = "⁰¹²³⁴⁵⁶⁷⁸⁹"          # kāpinātāju zīmes 0..9

ATGADNE = [
    "Pakāpju īpašības:   aᵐ · aⁿ = aᵐ⁺ⁿ   ·   aᵐ : aⁿ = aᵐ⁻ⁿ   ·   "
    "(aᵐ)ⁿ = aᵐ·ⁿ   ·   (ab)ⁿ = aⁿbⁿ   ·   ({a|b})ⁿ = {aⁿ|bⁿ}",
    "a⁰ = 1   (a ≠ 0)   ·   a⁻ⁿ = {1|aⁿ}   ·   pakāpes aⁿ un a⁻ⁿ ir "
    "savstarpēji apgriezti skaitļi.",
    "Normālforma:   a · 10ⁿ,   kur 1 ≤ a < 10   ·   piemēram   "
    "3200 = 3,2 · 10³   ·   0,004 = 4 · 10⁻³",
]


def kap(n):
    """Kāpinātāja zīme ar augšējiem cipariem; negatīvam - ar mīnusu."""
    if n < 0:
        return "⁻" + "".join(KAPES[int(c)] for c in str(-n))
    return "".join(KAPES[int(c)] for c in str(n))


# ---------------------------------------------------------------- veidnes
def vertiba(a, n):
    """Pakāpes skaitliskā vērtība."""
    return ("Cik ir %d%s?" % (a, kap(n)),
            V.izvele(a ** n, a * n, a + n, n ** a, a ** n + 1,
                     a ** (n + 1)), 0)


def reizina(a, m, n):
    """Pakāpju reizinājums ar vienādām bāzēm."""
    return ("Vienkāršo:  a%s · a%s." % (kap(m), kap(n)),
            V.izvele("a%s" % kap(m + n), "a%s" % kap(m * n),
                     "a%s" % kap(abs(m - n)), "a%s" % kap(m + n + 1),
                     "2a%s" % kap(m + n), "a%s" % kap(m)), 0)


def dala(a, m, n):
    """Pakāpju dalījums ar vienādām bāzēm."""
    return ("Vienkāršo:  a%s : a%s." % (kap(m), kap(n)),
            V.izvele("a%s" % kap(m - n), "a%s" % kap(m + n),
                     "a%s" % kap(n - m), "a%s" % kap(m * n),
                     "a%s" % kap(m - n + 1), "a%s" % kap(m)), 0)


def kapina(m, n):
    """Pakāpes kāpināšana."""
    return ("Vienkāršo:  (a%s)%s." % (kap(m), kap(n)),
            V.izvele("a%s" % kap(m * n), "a%s" % kap(m + n),
                     "a%s" % kap(abs(m - n)), "a%s" % kap(m * n + 1),
                     "%da%s" % (n, kap(m)), "a%s" % kap(n)), 0)


def negativs(a, n):
    """Pakāpe ar negatīvu kāpinātāju."""
    return ("Cik ir %d%s?" % (a, kap(-n)),
            V.izvele(V.dalu(1, a ** n), a ** n, -(a ** n),
                     V.dalu(1, a * n), V.dalu(-1, a ** n),
                     V.dalu(1, a ** n + 1)), 0)


def decimals(mantisa, n):
    """«3,2» un 3  ->  «3200»: komatu pārceļ, nevis rēķina ar peldošo punktu.

    Peldošā punkta aritmētika šeit mēdz noapaļot (0,00025 -> 0,0003), tāpēc
    pierakstu veido no pašiem cipariem.
    """
    cipari = mantisa.replace(",", "")
    vieta = mantisa.index(",") if "," in mantisa else len(mantisa)
    vieta += n
    if vieta >= len(cipari):
        return V.sk(int(cipari + "0" * (vieta - len(cipari))))
    if vieta <= 0:
        return "0," + "0" * (-vieta) + cipari
    return cipari[:vieta] + "," + cipari[vieta:]


def normalforma(mantisa, n):
    """Skaitļa pieraksts normālformā:  a · 10ⁿ,  kur 1 ≤ a < 10."""
    a = mantisa
    return ("Kā normālformā pieraksta %s?" % decimals(mantisa, n),
            V.izvele("%s · 10%s" % (a, kap(n)),
                     "%s · 10%s" % (a, kap(-n)),
                     "%s · 10%s" % (a, kap(n + 1)),
                     "%s · 10%s" % (decimals(a, 1), kap(n)),
                     "%s · 10%s" % (a, kap(n - 1)),
                     "%s" % a), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.2. temata beigās. Pārbauda pakāpes "
                "vērtību, pakāpju īpašības, kāpināšanu, pakāpi ar negatīvu "
                "kāpinātāju un skaitļa normālformu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina pakāpes jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc skaitli, ko kāpina?", ["bāze", "kāpinātājs",
                                              "pakāpe", "koeficients"], 0),
             ("Kā sauc skaitli, kas rāda reizinātāju skaitu?",
              ["kāpinātājs", "bāze", "pakāpe", "koeficients"], 0),
             ("Ko nozīmē a⁵?", ["a · a · a · a · a", "a · 5", "a + 5",
                                "5 · 5 · 5 · 5 · 5"], 0),
             ("Cik ir a⁰, ja a ≠ 0?", ["1", "0", "a", "nav noteikts"], 0),
             ("Cik ir a¹?", ["a", "1", "0", "a²"], 0),
             ("Ar ko vienāds a⁻ⁿ?", ["{1|aⁿ}", "−aⁿ", "aⁿ", "{aⁿ|1}"], 0),
             ("Kādi skaitļi ir aⁿ un a⁻ⁿ?",
              ["savstarpēji apgriezti", "pretēji", "vienādi",
               "nesalīdzināmi"], 0),
             ("Kāda zīme ir pakāpei (−3)⁴?",
              ["pozitīva", "negatīva", "nulle", "nevar noteikt"], 0),
         ]},
        {"sr": "Aprēķina pakāpes vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vertiba, [
             (2, 3), (3, 2), (5, 2), (2, 4), (4, 3), (10, 3), (3, 3),
             (6, 2), (2, 5), (7, 2), (8, 2), (9, 2), (2, 6), (5, 3),
             (10, 4)]),
         },
        {"sr": "Reizina pakāpes ar vienādām bāzēm",
         "stunda": TEMATS,
         "jautajumi": V.kopa(reizina, [
             (0, 2, 3), (0, 4, 5), (0, 3, 7), (0, 6, 2), (0, 5, 8),
             (0, 7, 4), (0, 9, 3), (0, 2, 10), (0, 8, 6), (0, 11, 2),
             (0, 4, 9), (0, 12, 3), (0, 5, 11), (0, 13, 4), (0, 6, 7)]),
         },
        {"sr": "Dala pakāpes ar vienādām bāzēm",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dala, [
             (0, 7, 3), (0, 9, 4), (0, 8, 2), (0, 12, 5), (0, 10, 6),
             (0, 11, 3), (0, 15, 7), (0, 13, 8), (0, 14, 9), (0, 16, 4),
             (0, 17, 11), (0, 18, 6), (0, 19, 12), (0, 20, 13),
             (0, 21, 15)]),
         },
        {"sr": "Kāpina pakāpi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kapina, [
             (2, 3), (3, 4), (4, 2), (5, 3), (2, 6), (6, 2), (3, 5),
             (7, 2), (4, 4), (2, 8), (8, 2), (3, 6), (9, 2), (5, 4),
             (2, 9)]),
         },
        {"sr": "Kāpina reizinājumu un daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienkāršo:  (ab)³.", ["a³b³", "ab³", "a³b", "3ab"], 0),
             ("Vienkāršo:  (2a)³.", ["8a³", "2a³", "6a³", "8a"], 0),
             ("Vienkāršo:  (3a)².", ["9a²", "3a²", "6a²", "9a"], 0),
             ("Vienkāršo:  ({a|b})⁴.", ["{a⁴|b⁴}", "{a⁴|b}", "{a|b⁴}",
                                        "{4a|4b}"], 0),
             ("Vienkāršo:  (5a)².", ["25a²", "5a²", "10a²", "25a"], 0),
             ("Vienkāršo:  (a²b)³.", ["a⁶b³", "a⁵b³", "a⁶b", "a²b³"], 0),
             ("Vienkāršo:  (−2a)⁴.", ["16a⁴", "−16a⁴", "8a⁴", "16a"], 0),
             ("Vienkāršo:  (4a)³.", ["64a³", "12a³", "4a³", "64a"], 0),
         ]},
        {"sr": "Lieto pakāpi ar negatīvu kāpinātāju",
         "stunda": TEMATS,
         "jautajumi": V.kopa(negativs, [
             (2, 3), (3, 2), (5, 2), (2, 4), (4, 2), (10, 3), (3, 3),
             (6, 2), (2, 5), (7, 2), (8, 2), (9, 2), (2, 6), (5, 3),
             (10, 2)]),
         },
        {"sr": "Pārveido negatīvu kāpinātāju par pozitīvu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pārveido:  a⁻³.", ["{1|a³}", "−a³", "a³", "{a³|1}"], 0),
             ("Pārveido:  {1|a⁻²}.", ["a²", "{1|a²}", "−a²", "a⁻²"], 0),
             ("Pārveido:  2a⁻¹.", ["{2|a}", "{1|2a}", "−2a", "2a"], 0),
             ("Pārveido:  (2a)⁻².", ["{1|4a²}", "{1|2a²}", "4a²",
                                     "−4a²"], 0),
             ("Pārveido:  ({a|b})⁻¹.", ["{b|a}", "{a|b}", "−{a|b}",
                                        "{1|ab}"], 0),
             ("Ar ko vienāds 10⁻²?", ["0,01", "0,1", "−100", "100"], 0),
             ("Ar ko vienāds 10⁻³?", ["0,001", "0,01", "−1000", "1000"], 0),
             ("Ar ko vienāds ({1|2})⁻¹?", ["2", "{1|2}", "−2", "{1|4}"], 0),
         ]},
        {"sr": "Pieraksta skaitli normālformā",
         "stunda": TEMATS,
         "jautajumi": V.kopa(normalforma, [
             ("3,2", 3), ("5", 4), ("1,5", 6), ("2,4", 5), ("7", 3),
             ("9,8", 4), ("6,1", 7), ("4", 6), ("8,5", 5), ("2", 8),
             ("3", 9), ("1,2", 10), ("4", -3), ("2,5", -4), ("7", -5)]),
         },
        {"sr": "Pārveido normālformu par decimālu pierakstu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 3 · 10³?", ["3000", "300", "30 000", "3,3"], 0),
             ("Cik ir 2,5 · 10⁴?", ["25 000", "2500", "250 000", "2,54"], 0),
             ("Cik ir 4 · 10⁻²?", ["0,04", "0,4", "400", "−400"], 0),
             ("Cik ir 6 · 10⁻³?", ["0,006", "0,06", "6000", "−6000"], 0),
             ("Cik ir 1,2 · 10⁵?", ["120 000", "12 000", "1 200 000",
                                    "1,25"], 0),
             ("Cik ir 9 · 10⁻¹?", ["0,9", "0,09", "90", "−9"], 0),
             ("Kurš skaitlis ir pierakstīts normālformā?",
              ["4,7 · 10⁵", "47 · 10⁴", "0,47 · 10⁶", "4,7"], 0),
             ("Kāds nosacījums ir skaitlim a normālformā a · 10ⁿ?",
              ["1 ≤ a < 10", "0 < a < 1", "a ir vesels", "a > 10"], 0),
         ]},
        {"sr": "Lieto normālformu situācijās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Gaismas ātrums ir 300 000 km/s. Kā to pieraksta "
              "normālformā?", ["3 · 10⁵ km/s", "30 · 10⁴ km/s",
                               "3 · 10⁶ km/s", "0,3 · 10⁶ km/s"], 0),
             ("Baktērijas izmērs ir 0,000002 m. Kā to pieraksta?",
              ["2 · 10⁻⁶ m", "2 · 10⁶ m", "20 · 10⁻⁷ m", "0,2 · 10⁻⁵ m"], 0),
             ("Kāpēc lieto normālformu?",
              ["ļoti lielus un mazus skaitļus ir ērtāk pierakstīt",
               "tā ir īsāka vienmēr", "tā ir skaistāka",
               "tā prasa noteikumi"], 0),
             ("Cik ir (2 · 10³) · (3 · 10²)?",
              ["6 · 10⁵", "5 · 10⁵", "6 · 10⁶", "6 · 10¹"], 0),
             ("Cik ir (8 · 10⁵) : (2 · 10²)?",
              ["4 · 10³", "4 · 10⁷", "6 · 10³", "4 · 10²"], 0),
             ("Kurš skaitlis ir lielāks?",
              ["5 · 10⁴", "9 · 10³", "7 · 10²", "8 · 10¹"], 0),
             ("Kurš skaitlis ir mazāks?",
              ["3 · 10⁻⁵", "3 · 10⁻³", "3 · 10⁻¹", "3 · 10⁰"], 0),
             ("Cik nullu ir skaitlī 10⁶?", ["6", "5", "7", "10"], 0),
         ]},
        {"sr": "Vienkāršo izteiksmes ar pakāpēm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienkāršo:  a³ · a² : a⁴.", ["a", "a⁹", "a⁵", "a²"], 0),
             ("Vienkāršo:  (a²)³ : a⁵.", ["a", "a⁶", "a¹¹", "a⁰"], 0),
             ("Vienkāršo:  2a³ · 3a².", ["6a⁵", "5a⁵", "6a⁶", "6a"], 0),
             ("Vienkāršo:  8a⁵ : 2a³.", ["4a²", "4a⁸", "6a²", "4a"], 0),
             ("Vienkāršo:  a⁴ · a⁻²."  , ["a²", "a⁶", "a⁻⁸", "a⁻²"], 0),
             ("Vienkāršo:  (3a²)².", ["9a⁴", "3a⁴", "6a⁴", "9a²"], 0),
             ("Vienkāršo:  a⁵ : a⁵.", ["1", "a", "0", "a¹⁰"], 0),
             ("Vai a² + a³ = a⁵?", ["nē", "jā", "tikai ja a = 1",
                                    "vienmēr"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.2. temata noslēgumā. "
                "Pārbauda pakāpes vērtību, pakāpju īpašības, kāpināšanu, "
                "pakāpi ar negatīvu kāpinātāju un normālformu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Aprēķina pakāpes vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vertiba, [
             (3, 3), (4, 2), (6, 2), (2, 5), (5, 3), (10, 2), (7, 2),
             (8, 2), (2, 7), (9, 2), (3, 4), (11, 2), (2, 8), (12, 2),
             (10, 5)]),
         },
        {"sr": "Lieto pakāpju īpašības",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(reizina, [
             (0, 3, 4), (0, 5, 6), (0, 2, 9), (0, 7, 3), (0, 6, 8),
             (0, 8, 5), (0, 10, 2)])
             + V.kopa(dala, [
                 (0, 8, 3), (0, 10, 4), (0, 9, 2), (0, 13, 6), (0, 11, 7),
                 (0, 12, 8), (0, 16, 9), (0, 14, 5)])),
         },
        {"sr": "Kāpina pakāpi un reizinājumu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(kapina, [
             (3, 3), (4, 3), (5, 2), (2, 7), (6, 3), (3, 7), (7, 3)])
             + [("Vienkāršo:  (2a)³.", ["8a³", "2a³", "6a³", "8a"], 0),
                ("Vienkāršo:  (3a)².", ["9a²", "3a²", "6a²", "9a"], 0),
                ("Vienkāršo:  (ab)⁴.", ["a⁴b⁴", "ab⁴", "a⁴b", "4ab"], 0),
                ("Vienkāršo:  ({a|b})³.", ["{a³|b³}", "{a³|b}", "{a|b³}",
                                           "{3a|3b}"], 0),
                ("Vienkāršo:  (5a)².", ["25a²", "5a²", "10a²", "25a"], 0),
                ("Vienkāršo:  (a³b)².", ["a⁶b²", "a⁵b²", "a⁶b", "a³b²"], 0),
                ("Vienkāršo:  (−3a)².", ["9a²", "−9a²", "6a²", "9a"], 0),
                ("Vienkāršo:  (4a)³.", ["64a³", "12a³", "4a³", "64a"], 0)]),
         },
        {"sr": "Lieto negatīvu kāpinātāju",
         "stunda": TEMATS,
         "jautajumi": V.kopa(negativs, [
             (2, 2), (3, 3), (4, 2), (5, 3), (2, 6), (6, 2), (7, 2),
             (10, 4), (8, 2), (9, 2), (2, 7), (3, 4), (11, 2), (12, 2),
             (10, 5)]),
         },
        {"sr": "Pieraksta skaitli normālformā",
         "stunda": TEMATS,
         "jautajumi": V.kopa(normalforma, [
             ("2,4", 3), ("6", 4), ("1,8", 6), ("3,5", 5), ("8", 3),
             ("9,2", 4), ("5,1", 7), ("7", 6), ("4,5", 5), ("3", 8),
             ("2", 9), ("1,6", 10), ("5", -3), ("3,5", -4), ("8", -5)]),
         },
        {"sr": "Pārveido normālformu un vienkāršo izteiksmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir 4 · 10³?", ["4000", "400", "40 000", "4,3"], 0),
             ("Cik ir 3,5 · 10⁴?", ["35 000", "3500", "350 000",
                                    "3,54"], 0),
             ("Cik ir 5 · 10⁻²?", ["0,05", "0,5", "500", "−500"], 0),
             ("Kurš skaitlis ir pierakstīts normālformā?",
              ["6,3 · 10⁵", "63 · 10⁴", "0,63 · 10⁶", "6,3"], 0),
             ("Vienkāršo:  a⁴ · a³ : a⁵.", ["a²", "a¹²", "a⁷", "a"], 0),
             ("Vienkāršo:  2a⁴ · 4a².", ["8a⁶", "6a⁶", "8a⁸", "8a"], 0),
             ("Vienkāršo:  9a⁶ : 3a².", ["3a⁴", "3a³", "6a⁴", "3a⁸"], 0),
             ("Vai a³ + a² = a⁵?", ["nē", "jā", "tikai ja a = 1",
                                    "vienmēr"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina pakāpes un lieto īpašības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Aprēķini un vienkāršo",
             lambda a, n, m, k: [
                 ("%d%s = ……" % (a, kap(n)), V.sk(a ** n)),
                 ("%d%s = ……" % (a, kap(-2)), V.dalu(1, a * a)),
                 ("a%s · a%s = ……" % (kap(m), kap(k)),
                  "a%s" % kap(m + k)),
                 ("(a%s)%s = ……" % (kap(m), kap(k)), "a%s" % kap(m * k))],
             [(2, 3, 4, 5), (3, 2, 5, 3), (5, 2, 2, 6), (2, 4, 7, 2),
              (4, 3, 3, 4), (10, 3, 6, 3), (3, 3, 8, 2), (6, 2, 4, 4),
              (2, 5, 9, 2), (7, 2, 5, 5), (8, 2, 3, 6), (9, 2, 10, 2),
              (2, 6, 7, 3), (5, 3, 6, 4), (10, 4, 4, 7)]),
         },
        {"sr": "Lieto normālformu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Normālforma",
             lambda a, n, b, m: [
                 ("%s · 10%s = ……" % (a, kap(n)), decimals(a, n)),
                 ("%s = …… (normālformā)" % decimals(b, m),
                  "%s · 10%s" % (b, kap(m))),
                 ("10%s = ……" % kap(-2), "0,01")],
             [("3", 3, "2,4", 4), ("5", 4, "1,5", 3), ("2", 5, "6,2", 5),
              ("4", 3, "3,1", 6), ("6", 4, "8,4", 3), ("7", 3, "2,5", 7),
              ("8", 5, "9,3", 4), ("9", 3, "1,2", 8), ("1,5", 4, "4,6", 5),
              ("2,5", 5, "7,8", 3), ("3,5", 3, "5,4", 6),
              ("4,5", 4, "6,7", 4), ("5,5", 5, "3,9", 7),
              ("6,5", 3, "8,1", 5), ("7,5", 4, "2,2", 9)]),
         },
        {"sr": "Lieto pakāpes situāciju uzdevumā",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Pakāpes situācijā",
             lambda a, n, b, m: {
                 "teksts": "Doti skaitļi  A = %s · 10%s  un  B = %s · 10%s. "
                           "  a) Pieraksti A decimālā pierakstā!   "
                           "b) Aprēķini A · B un pieraksti normālformā!   "
                           "c) Aprēķini A : B!   d) Kurš skaitlis ir "
                           "lielāks?" % (V.sk(a), kap(n), V.sk(b), kap(m)),
                 "kriteriji": [
                     "a) %s.   (1 p.)" % V.sk(int(a * 10 ** n)),
                     "b) %s · 10%s.   (1 p.)"
                     % (V.sk(a * b), kap(n + m)),
                     "c) %s · 10%s.   (1 p.)"
                     % (V.sk(round(a / float(b), 4)), kap(n - m)),
                     "d) %s.   (1 p.)"
                     % ("A" if a * 10 ** n > b * 10 ** m else "B")]},
             [(2, 3, 3, 2), (4, 4, 2, 3), (5, 5, 2, 2), (3, 6, 3, 4),
              (6, 3, 2, 5), (8, 4, 4, 2), (9, 5, 3, 3), (2, 7, 5, 4),
              (7, 3, 7, 2), (4, 6, 8, 3), (6, 5, 3, 5), (8, 6, 2, 4),
              (9, 4, 3, 6), (5, 7, 5, 3), (3, 8, 6, 2)]),
         },
        {"sr": "Pamato pakāpju īpašības",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Pakāpju īpašības",
             lambda m, n: {
                 "ievads": "Dotas pakāpes  a%s  un  a%s." % (kap(m), kap(n)),
                 "jaut": [("Uzraksti to reizinājumu!", 1),
                          ("Uzraksti to dalījumu!", 1),
                          ("Paskaidro, kāpēc kāpinātājus saskaita!", 1)],
                 "atbildes": [
                     "1) a%s.   (1 p.)" % kap(m + n),
                     "2) a%s.   (1 p.)" % kap(m - n),
                     "3) Abās pakāpēs reizinātāju skaits saskaitās.   "
                     "(1 p.)"]},
             [(5, 3), (7, 4), (6, 2), (9, 5), (8, 3), (10, 6), (4, 2),
              (11, 7), (12, 4), (13, 8), (14, 5), (15, 9), (16, 6),
              (17, 3), (18, 10)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
