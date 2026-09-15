# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.1. Kā dažādi pieraksta naturālos skaitļus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.1. temats): naturālo skaitļu
šķiras un lasīšana, lielās šķiras (miljons, miljards), romiešu cipari,
noapaļošana līdz desmitiem, simtiem un tūkstošiem, daudzciparu skaitļu
saskaitīšana un atņemšana, nezināmā noteikšana un darbību secība.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.1."
NOSAUKUMS = "Kā dažādi pieraksta naturālos skaitļus?"

ATGADNE = [
    "Šķiras:  vieni · desmiti · simti · tūkstoši · desmiti tūkstošu · simti "
    "tūkstošu · miljoni      ·      1 000 000 — miljons, 1 000 000 000 — "
    "miljards",
    "Romiešu cipari:   I = 1   ·   V = 5   ·   X = 10   ·   L = 50   ·   "
    "C = 100   ·   D = 500   ·   M = 1000",
    "Noapaļojot līdz simtiem, skatās desmitus: ja 5 vai vairāk — uz augšu, "
    "ja mazāk — uz leju.",
]

ROMIESU = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
           (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
           (5, "V"), (4, "IV"), (1, "I")]


def romiesu(n):
    """Skaitlis romiešu ciparos - lai pierakstu nevajag rakstīt ar roku."""
    out = ""
    for vertiba, zime in ROMIESU:
        while n >= vertiba:
            out += zime
            n -= vertiba
    return out


def noapalot(n, lidz):
    """Noapaļošana līdz dotajai šķirai."""
    return (n + lidz // 2) // lidz * lidz


# ---------------------------------------------------------------- veidnes
def skira(n, viet, nos):
    """Kurš cipars stāv dotajā šķirā."""
    cipari = str(n)[::-1]
    d = int(cipari[viet])
    # Maldi vispirms no paša skaitļa cipariem; ja tie atkārtojas, noder
    # citi cipari, lai atbilžu variantu vienmēr ir četri.
    maldi = [c for c in cipari if c != cipari[viet]]
    maldi += [str((d + solis) % 10) for solis in (1, 3, 7)]
    return ("Kurš cipars skaitlī %s ir %s šķirā?" % (V.sk(n), nos),
            V.izvele(cipari[viet], *maldi), 0)


def lasa_romiesu(n):
    """Romiešu pieraksts -> skaitlis."""
    return ("Kāds skaitlis pierakstīts ar romiešu cipariem %s?" % romiesu(n),
            V.izvele(n, n + 1, n - 1, n + 10, n * 2, n - 10), 0)


def raksta_romiesu(n):
    """Skaitlis -> romiešu pieraksts."""
    return ("Kā ar romiešu cipariem pieraksta %s?" % V.sk(n),
            V.izvele(romiesu(n), romiesu(n + 1), romiesu(n - 1),
                     romiesu(n + 10), romiesu(n * 2), romiesu(n + 5)), 0)


def noapalo(n, lidz, nos):
    """Noapaļošana līdz desmitiem, simtiem vai tūkstošiem."""
    r = noapalot(n, lidz)
    return ("Noapaļo %s līdz %s!" % (V.sk(n), nos),
            V.izvele(r, r + lidz, r - lidz, n, r + lidz // 2,
                     noapalot(n, lidz * 10)), 0)


def saskaita(a, b):
    return ("Cik ir %s + %s?" % (V.sk(a), V.sk(b)),
            V.izvele(a + b, a - b, b - a, a + b + 10, a + b - 10,
                     a + b + 100), 0)


def atnem(a, b):
    return ("Cik ir %s − %s?" % (V.sk(a), V.sk(b)),
            V.izvele(a - b, a + b, b - a, a - b + 10, a - b - 10,
                     a - b + 100), 0)


def nezinamais(a, b):
    """Nezināmais saskaitīšanas vai atņemšanas vienādībā."""
    return ("Atrisini:  x + %s = %s." % (V.sk(a), V.sk(a + b)),
            V.izvele(b, a, a + b, a + 2 * b, b + 10, b - 10), 0)


def izteiksme(a, b, c):
    """Darbību secība skaitliskā izteiksmē."""
    return ("Cik ir %d + %d · %d?" % (a, b, c),
            V.izvele(a + b * c, (a + b) * c, a + b + c, a * b + c,
                     a + b * c + 1, a * (b + c)), 0)


FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.1. temata beigās. Pārbauda naturālo "
                "skaitļu šķiras, romiešu ciparus, noapaļošanu, daudzciparu "
                "skaitļu saskaitīšanu un atņemšanu un darbību secību.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina naturālo skaitļu īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš ir mazākais naturālais skaitlis?",
              ["1", "0", "−1", "10"], 0),
             ("Vai 0 ir naturāls skaitlis?",
              ["nē", "jā", "tikai skaitīšanā", "nevar noteikt"], 0),
             ("Vai naturālo skaitļu ir bezgalīgi daudz?",
              ["jā", "nē", "tikai līdz miljonam", "nevar noteikt"], 0),
             ("Kāds ir skaitlim 99 sekojošais naturālais skaitlis?",
              ["100", "98", "990", "109"], 0),
             ("Kāds skaitlis ir pirms 1000?",
              ["999", "1001", "900", "100"], 0),
             ("Kam lieto naturālos skaitļus?",
              ["priekšmetu skaitīšanai", "daļu pierakstam",
               "temperatūrai zem nulles", "mērvienībām"], 0),
             ("Cik ciparu ir skaitlī 10 000?", ["5", "4", "6", "10"], 0),
             ("Kurš skaitlis ir lielākais?",
              ["90 909", "9909", "90 099", "9990"], 0),
         ]},
        {"sr": "Nosaka šķiras un lasa skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(skira, [
             (3475, 0, "vienu"), (3475, 1, "desmitu"),
             (3475, 2, "simtu"), (3475, 3, "tūkstošu"),
             (52816, 0, "vienu"), (52816, 2, "simtu"),
             (52816, 4, "desmitu tūkstošu"), (91423, 1, "desmitu"),
             (91423, 3, "tūkstošu"), (60734, 2, "simtu"),
             (60734, 4, "desmitu tūkstošu"), (18592, 0, "vienu"),
             (18592, 3, "tūkstošu"), (47061, 1, "desmitu"),
             (47061, 2, "simtu")]),
         },
        {"sr": "Zina lielās šķiras",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik nullu ir miljonā?", ["6", "3", "9", "12"], 0),
             ("Cik nullu ir miljardā?", ["9", "6", "12", "3"], 0),
             ("Kā pieraksta vienu miljonu?",
              ["1 000 000", "100 000", "10 000 000", "1000"], 0),
             ("Cik tūkstoši ir vienā miljonā?",
              ["1000", "100", "10", "1 000 000"], 0),
             ("Cik miljoni ir vienā miljardā?",
              ["1000", "100", "10", "1 000 000"], 0),
             ("Kā sauc šķiru aiz simtiem tūkstošu?",
              ["miljoni", "miljardi", "desmiti tūkstošu", "simti"], 0),
             ("Cik ciparu ir mazākajam miljonam?", ["7", "6", "8", "9"], 0),
             ("Kurš skaitlis ir lielāks: 999 999 vai 1 000 000?",
              ["1 000 000", "999 999", "tie ir vienādi",
               "nevar salīdzināt"], 0),
         ]},
        {"sr": "Lasa romiešu ciparus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(lasa_romiesu, [
             4, 9, 14, 19, 24, 40, 44, 59, 90, 99, 104, 150, 400, 900,
             1200]),
         },
        {"sr": "Pieraksta skaitļus ar romiešu cipariem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(raksta_romiesu, [
             6, 12, 17, 23, 29, 34, 45, 56, 68, 74, 85, 96, 110, 250,
             1500]),
         },
        {"sr": "Noapaļo līdz simtiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(noapalo, [
             (347, 100, "simtiem"), (682, 100, "simtiem"),
             (1250, 100, "simtiem"), (2649, 100, "simtiem"),
             (3561, 100, "simtiem"), (4928, 100, "simtiem"),
             (5183, 100, "simtiem"), (6714, 100, "simtiem"),
             (7352, 100, "simtiem"), (8496, 100, "simtiem"),
             (9635, 100, "simtiem"), (10748, 100, "simtiem"),
             (21863, 100, "simtiem"), (32974, 100, "simtiem"),
             (45082, 100, "simtiem")]),
         },
        {"sr": "Noapaļo līdz tūkstošiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(noapalo, [
             (3475, 1000, "tūkstošiem"), (6821, 1000, "tūkstošiem"),
             (12503, 1000, "tūkstošiem"), (26491, 1000, "tūkstošiem"),
             (35617, 1000, "tūkstošiem"), (49283, 1000, "tūkstošiem"),
             (51834, 1000, "tūkstošiem"), (67145, 1000, "tūkstošiem"),
             (73526, 1000, "tūkstošiem"), (84962, 1000, "tūkstošiem"),
             (96358, 1000, "tūkstošiem"), (107482, 1000, "tūkstošiem"),
             (218637, 1000, "tūkstošiem"), (329741, 1000, "tūkstošiem"),
             (450829, 1000, "tūkstošiem")]),
         },
        {"sr": "Saskaita daudzciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saskaita, [
             (3475, 2816), (5219, 3684), (7342, 1958), (4506, 2794),
             (6128, 3875), (8241, 1659), (9073, 2847), (1584, 6329),
             (2706, 5194), (3918, 4082), (5437, 2663), (6852, 3148),
             (7195, 2805), (8364, 1736), (9528, 4472)]),
         },
        {"sr": "Atņem daudzciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem, [
             (6291, 3475), (8903, 5219), (9300, 7342), (7500, 4506),
             (10004, 6128), (9182, 8241), (12000, 9073), (8010, 1584),
             (7900, 2706), (11000, 3918), (9605, 5437), (10200, 6852),
             (8451, 7195), (13000, 8364), (14502, 9528)]),
         },
        {"sr": "Aprēķina nezināmo vienādībā",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nezinamais, [
             (35, 47), (62, 18), (124, 76), (205, 95), (318, 82),
             (426, 174), (537, 63), (648, 252), (759, 141), (860, 240),
             (971, 129), (1082, 418), (1263, 237), (1394, 106),
             (1475, 525)]),
         },
        {"sr": "Aprēķina skaitliskas izteiksmes vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(izteiksme, [
             (12, 3, 4), (25, 5, 6), (18, 7, 2), (30, 4, 8), (45, 6, 3),
             (50, 9, 2), (16, 8, 5), (72, 3, 7), (64, 2, 9), (80, 5, 4),
             (36, 6, 6), (90, 4, 5), (28, 7, 3), (100, 8, 2),
             (55, 9, 4)]),
         },
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skolā ir 1245 grāmatas, iegādājas vēl 378. Cik ir kopā?",
              ["1623", "867", "1523", "1613"], 0),
             ("Bibliotēkā bija 2500 grāmatas, izsniedza 847. Cik palika?",
              ["1653", "3347", "1753", "1643"], 0),
             ("Stadionā 5000 vietas, aizņemtas 3675. Cik brīvas?",
              ["1325", "8675", "1425", "1335"], 0),
             ("Pilsētā 12 480 iedzīvotāju; noapaļo līdz tūkstošiem!",
              ["12 000", "13 000", "12 500", "12 400"], 0),
             ("Veikalā pārdeva 1860 un 2140 preces. Cik kopā?",
              ["4000", "3900", "4100", "280"], 0),
             ("Ceļojumā 3400 km; nobraukti 1875 km. Cik atlicis?",
              ["1525", "5275", "1625", "1515"], 0),
             ("Fabrika saražoja 9500 detaļas, 1250 bija ar defektu. Cik "
              "derīgo?", ["8250", "10 750", "8350", "8150"], 0),
             ("Cik ir 4500 + 2700 − 1200?", ["6000", "8400", "5000",
                                             "3000"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.1. temata noslēgumā. "
                "Pārbauda skaitļa šķiras, romiešu ciparus, noapaļošanu, "
                "daudzciparu skaitļu saskaitīšanu un atņemšanu un nezināmā "
                "noteikšanu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Nosaka šķiras un lasa skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(skira, [
             (4286, 0, "vienu"), (4286, 1, "desmitu"), (4286, 2, "simtu"),
             (4286, 3, "tūkstošu"), (63927, 0, "vienu"),
             (63927, 2, "simtu"), (63927, 4, "desmitu tūkstošu"),
             (82534, 1, "desmitu"), (82534, 3, "tūkstošu"),
             (70815, 2, "simtu"), (70815, 4, "desmitu tūkstošu"),
             (29603, 0, "vienu"), (29603, 3, "tūkstošu"),
             (58172, 1, "desmitu"), (58172, 2, "simtu")]),
         },
        {"sr": "Lieto romiešu ciparus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(lasa_romiesu, [
             7, 13, 18, 26, 39, 49, 64])
             + V.kopa(raksta_romiesu, [
                 8, 15, 21, 37, 48, 62, 79, 95])),
         },
        {"sr": "Noapaļo skaitļus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(noapalo, [
             (58, 10, "desmitiem"), (94, 10, "desmitiem"),
             (137, 10, "desmitiem"), (275, 10, "desmitiem"),
             (462, 100, "simtiem")])
             + V.kopa(noapalo, [
                 (749, 100, "simtiem"), (1358, 100, "simtiem"),
                 (2641, 100, "simtiem"), (4283, 1000, "tūkstošiem"),
                 (7519, 1000, "tūkstošiem"), (13628, 1000, "tūkstošiem"),
                 (27394, 1000, "tūkstošiem"), (36815, 1000, "tūkstošiem"),
                 (48260, 1000, "tūkstošiem"),
                 (59473, 1000, "tūkstošiem")])),
         },
        {"sr": "Saskaita un atņem daudzciparu skaitļus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(saskaita, [
             (4286, 3175), (6328, 2794), (8451, 1639), (5073, 3927),
             (7264, 2836), (9185, 1715), (3492, 6508)])
             + V.kopa(atnem, [
                 (7413, 4286), (9204, 6328), (10500, 8451), (8300, 5073),
                 (11000, 7264), (12480, 9185), (9060, 3492),
                 (15000, 6749)])),
         },
        {"sr": "Aprēķina nezināmo un izteiksmes vērtību",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(nezinamais, [
             (48, 36), (75, 25), (136, 64), (247, 153), (358, 142),
             (469, 231), (572, 128)])
             + V.kopa(izteiksme, [
                 (14, 4, 5), (27, 6, 3), (35, 8, 2), (48, 5, 7),
                 (60, 3, 9), (75, 7, 4), (88, 2, 6), (96, 9, 3)])),
         },
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Skolā ir 1245 grāmatas, iegādājas vēl 378. Cik ir kopā?",
              ["1623", "867", "1523", "1613"], 0),
             ("Bibliotēkā bija 2500 grāmatas, izsniedza 847. Cik palika?",
              ["1653", "3347", "1753", "1643"], 0),
             ("Stadionā 5000 vietas, aizņemtas 3675. Cik brīvas?",
              ["1325", "8675", "1425", "1335"], 0),
             ("Pilsētā 12 480 iedzīvotāju; noapaļo līdz tūkstošiem!",
              ["12 000", "13 000", "12 500", "12 400"], 0),
             ("Ceļojumā 3400 km; nobraukti 1875 km. Cik atlicis?",
              ["1525", "5275", "1625", "1515"], 0),
             ("Fabrika saražoja 9500 detaļas, 1250 bija ar defektu. Cik "
              "derīgo?", ["8250", "10 750", "8350", "8150"], 0),
             ("Cik ir 4500 + 2700 − 1200?", ["6000", "8400", "5000",
                                             "3000"], 0),
             ("Veikalā pārdeva 1860 un 2140 preces. Cik kopā?",
              ["4000", "3900", "4100", "280"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Saskaita, atņem, noapaļo un lasa romiešu ciparus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, b, n, r: [
                 ("%s + %s = ……" % (V.sk(a), V.sk(b)), V.sk(a + b)),
                 ("%s − %s = ……" % (V.sk(a), V.sk(b)), V.sk(a - b)),
                 ("Noapaļo %s līdz simtiem:   ……" % V.sk(n),
                  V.sk(noapalot(n, 100))),
                 ("%s = …… (ar cipariem)" % romiesu(r), V.sk(r))],
             [(3475, 2816, 347, 14), (5219, 3684, 682, 19),
              (7342, 1958, 1250, 24), (4506, 2794, 2649, 40),
              (6128, 3875, 3561, 44), (8241, 1659, 4928, 59),
              (9073, 2847, 5183, 90), (1584, 629, 6714, 99),
              (2706, 1194, 7352, 104), (3918, 2082, 8496, 150),
              (5437, 2663, 9635, 400), (6852, 3148, 10748, 900),
              (7195, 2805, 21863, 1200), (8364, 1736, 32974, 49),
              (9528, 4472, 45082, 64)]),
         },
        {"sr": "Aprēķina nezināmo un pieraksta ar romiešu cipariem",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Nezināmais un romiešu cipari",
             lambda a, b, r: [
                 ("x + %s = %s;   x = ……" % (V.sk(a), V.sk(a + b)),
                  V.sk(b)),
                 ("x − %s = %s;   x = ……" % (V.sk(a), V.sk(b)),
                  V.sk(a + b)),
                 ("%s = …… (ar romiešu cipariem)" % V.sk(r), romiesu(r))],
             [(35, 47, 6), (62, 18, 12), (124, 76, 17), (205, 95, 23),
              (318, 82, 29), (426, 174, 34), (537, 63, 45), (648, 252, 56),
              (759, 141, 68), (860, 240, 74), (971, 129, 85),
              (1082, 418, 96), (1263, 237, 110), (1394, 106, 250),
              (1475, 525, 1500)]),
         },
        {"sr": "Risina situāciju uzdevumu un noapaļo rezultātu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda bija, pienaca, izlietoja: {
                 "teksts": "Noliktavā bija %s preces, atveda vēl %s, bet "
                           "izsniedza %s.   a) Cik preču bija pēc "
                           "piegādes?   b) Cik preču palika?   "
                           "c) Noapaļo atlikumu līdz simtiem!   "
                           "d) Noapaļo atlikumu līdz tūkstošiem!"
                           % (V.sk(bija), V.sk(pienaca), V.sk(izlietoja)),
                 "kriteriji": [
                     "a) %s + %s = %s.   (1 p.)"
                     % (V.sk(bija), V.sk(pienaca), V.sk(bija + pienaca)),
                     "b) %s − %s = %s.   (1 p.)"
                     % (V.sk(bija + pienaca), V.sk(izlietoja),
                        V.sk(bija + pienaca - izlietoja)),
                     "c) %s.   (1 p.)"
                     % V.sk(noapalot(bija + pienaca - izlietoja, 100)),
                     "d) %s.   (1 p.)"
                     % V.sk(noapalot(bija + pienaca - izlietoja, 1000))]},
             [(3475, 2816, 1958), (5219, 3684, 2794), (7342, 1958, 3875),
              (4506, 2794, 1659), (6128, 3875, 2847), (8241, 1659, 6329),
              (9073, 2847, 5194), (1584, 6329, 4082), (2706, 5194, 2663),
              (3918, 4082, 3148), (5437, 2663, 2805), (6852, 3148, 1736),
              (7195, 2805, 4472), (8364, 1736, 3475), (9528, 4472, 5219)]),
         },
        {"sr": "Skaidro skaitļa uzbūvi un darbību secību",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Skaitļa uzbūve",
             lambda n: {
                 "ievads": "Dots skaitlis %s." % V.sk(n),
                 "jaut": [("Cik ciparu ir šim skaitlim?", 1),
                          ("Kurš cipars ir simtu šķirā?", 1),
                          ("Noapaļo to līdz tūkstošiem!", 1)],
                 "atbildes": [
                     "1) %d cipari.   (1 p.)" % len(str(n)),
                     "2) %s.   (1 p.)" % str(n)[::-1][2],
                     "3) %s.   (1 p.)" % V.sk(noapalot(n, 1000))]},
             [3475, 6821, 12503, 26491, 35617, 49283, 51834, 67145,
              73526, 84962, 96358, 107482, 218637, 329741, 450829]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
