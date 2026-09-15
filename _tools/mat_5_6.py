# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.6. Kā nosaka figūru nezināmos lielumus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.6. temats): leņķa veidi un
izstiepta, pilna un atvērta leņķa lielums, leņķa lieluma aprēķināšana kā citu
leņķu summa vai starpība, riņķa līnija, tās rādiuss, diametrs un garums,
cirkuļa lietojums, taisnstūra laukums un nezināmās malas garums, mērvienību
pārveidošana aprēķinos un kombinētas figūras laukums.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.6."
NOSAUKUMS = "Kā nosaka figūru nezināmos lielumus?"

ATGADNE = [
    "Leņķi:   šaurs < 90°   ·   taisns = 90°   ·   plats no 90° līdz 180° "
    "  ·   izstiepts = 180°   ·   atvērts no 180° līdz 360°   ·   pilns "
    "= 360°",
    "Riņķa līnija:   d = 2 · r   ·   garums C ≈ 6 · r      ·      "
    "taisnstūris:   S = a · b,   a = S : b,   P = 2 · (a + b)",
    "Kombinētas figūras laukumu aprēķina, sadalot to taisnstūros un "
    "taisnleņķa trijstūros; garumus vispirms pārveido vienādās mērvienībās.",
]


# ---------------------------------------------------------------- veidnes
def lenka_veids(a):
    """Leņķa veids pēc tā lieluma."""
    veids = ("šaurs" if a < 90 else
             ("taisns" if a == 90 else
              ("plats" if a < 180 else
               ("izstiepts" if a == 180 else "atvērts"))))
    citi = [v for v in ("šaurs", "taisns", "plats", "izstiepts", "atvērts")
            if v != veids]
    return ("Kāds leņķis ir %d°?" % a, V.izvele(veids, *citi), 0)


def summa(a, b):
    """Leņķis kā divu blakus leņķu summa."""
    return ("Diviem blakus leņķiem ir %d° un %d°. Cik liels ir kopējais "
            "leņķis?" % (a, b),
            V.izvele("%d°" % (a + b), "%d°" % abs(a - b),
                     "%d°" % (180 - a - b), "%d°" % (a + b + 10),
                     "%d°" % (360 - a - b), "%d°" % (a * 2)), 0)


def starpiba(viss, a, nos):
    """Otrs leņķis, ja stars sadala izstieptu vai pilnu leņķi."""
    return ("%s leņķi stars sadala divos leņķos; viens ir %d°. Cik liels "
            "ir otrs?" % (nos, a),
            V.izvele("%d°" % (viss - a), "%d°" % a, "%d°" % (viss + a),
                     "%d°" % (viss - a + 10), "%d°" % (90 - a if a < 90
                                                       else 2 * a),
                     "%d°" % (viss - a - 10)), 0)


def dala_lenka(a, b, viss, nos):
    """Daļa no izstiepta vai pilna leņķa."""
    return ("Cik grādu ir {%d|%d} no %s leņķa?" % (a, b, nos),
            V.izvele("%d°" % (viss // b * a), "%d°" % (viss // b),
                     "%d°" % (viss - viss // b * a),
                     "%d°" % (viss // b * a + 10),
                     "%d°" % (viss // a * b), "%d°" % viss), 0)


def diametrs(r):
    """Diametrs pēc rādiusa."""
    return ("Riņķa līnijas rādiuss ir %d cm. Cik garš ir diametrs?" % r,
            V.izvele("%d cm" % (2 * r), "%s cm" % V.dalu(r, 2),
                     "%d cm" % r, "%d cm" % (4 * r), "%d cm" % (r + 2),
                     "%d cm" % (2 * r + 2)), 0)


def linijas_garums(r):
    """Riņķa līnijas garums pēc sakarības C ≈ 6r."""
    return ("Rādiuss ir %d cm. Cik aptuveni garš ir riņķa līnija?" % r,
            V.izvele("aptuveni %d cm" % (6 * r), "aptuveni %d cm" % (2 * r),
                     "aptuveni %d cm" % (3 * r), "aptuveni %d cm" % (12 * r),
                     "aptuveni %d cm" % (6 * r + 6),
                     "aptuveni %d cm" % (r * r)), 0)


def laukums(a, b):
    """Taisnstūra laukums."""
    return ("Taisnstūra malas ir %d cm un %d cm. Cik liels ir laukums?"
            % (a, b),
            V.izvele("%d cm²" % (a * b), "%d cm²" % (a + b),
                     "%d cm²" % (2 * (a + b)), "%d cm²" % (a * b + 2),
                     "%d cm²" % abs(a - b), "%d cm²" % (a * b * 2)), 0)


def nezinama_mala(s, a):
    """Taisnstūra nezināmā mala, ja zināms laukums."""
    return ("Taisnstūra laukums ir %d cm², viena mala — %d cm. Cik gara ir "
            "otra mala?" % (s, a),
            V.izvele("%d cm" % (s // a), "%d cm" % (s - a),
                     "%d cm" % (s + a), "%d cm" % (s * a),
                     "%d cm" % (s // a + 1), "%d cm" % (s // a - 1)), 0)


def kombineta(s1, s2):
    """Kombinētas figūras laukums kā divu laukumu summa."""
    return ("Figūru veido divi taisnstūri — %d cm² un %d cm². Cik liels ir "
            "figūras laukums?" % (s1, s2),
            V.izvele("%d cm²" % (s1 + s2), "%d cm²" % abs(s1 - s2),
                     "%d cm²" % (s1 * s2), "%d cm²" % (s1 + s2 + 2),
                     "%d cm²" % ((s1 + s2) // 2), "%d cm²" % s1), 0)


FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.6. temata beigās. Pārbauda leņķu "
                "veidus un lielumus, leņķa aprēķināšanu kā summu vai "
                "starpību, riņķa līnijas lielumus, taisnstūra laukumu un "
                "nezināmo malu, mērvienību pārveidošanu un kombinētas "
                "figūras laukumu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Nosaka leņķa veidu pēc tā lieluma",
         "stunda": TEMATS,
         "jautajumi": V.kopa(lenka_veids, [
             65, 120, 90, 180, 250, 45, 135, 30, 160, 200, 75, 110,
             300, 15, 170]),
         },
        {"sr": "Zina izstiepta, pilna un atvērta leņķa lielumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik grādu ir izstieptam leņķim?",
              ["180°", "90°", "360°", "270°"], 0),
             ("Cik grādu ir pilnam leņķim?",
              ["360°", "180°", "90°", "300°"], 0),
             ("Kurš leņķis ir atvērts?", ["250°", "150°", "90°", "45°"], 0),
             ("Par cik grādiem stars pagriežas pusapgriezienā?",
              ["180°", "90°", "360°", "45°"], 0),
             ("Par cik grādiem stars pagriežas pilnā apgriezienā?",
              ["360°", "180°", "90°", "270°"], 0),
             ("Kāds leņķis rodas ceturtdaļapgriezienā?",
              ["taisns", "izstiepts", "pilns", "atvērts"], 0),
             ("Kādās robežās ir atvērts leņķis?",
              ["no 180° līdz 360°", "no 90° līdz 180°", "līdz 90°",
               "vairāk nekā 360°"], 0),
             ("Ar ko mēra leņķus?",
              ["ar transportieri", "ar lineālu", "ar cirkuli",
               "ar svariem"], 0),
         ]},
        {"sr": "Aprēķina leņķi kā divu leņķu summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(summa, [
             (35, 40), (90, 45), (25, 60), (50, 30), (18, 62), (55, 35),
             (48, 52), (70, 20), (15, 75), (80, 40), (12, 38), (65, 25),
             (42, 28), (33, 57), (27, 63)]),
         },
        {"sr": "Aprēķina leņķi kā divu leņķu starpību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(starpiba, [
             (180, 60, "Izstieptu"), (90, 25, "Taisnu"),
             (360, 100, "Pilnu"), (180, 75, "Izstieptu"),
             (90, 40, "Taisnu"), (360, 135, "Pilnu"),
             (180, 45, "Izstieptu"), (90, 55, "Taisnu"),
             (360, 200, "Pilnu"), (180, 120, "Izstieptu"),
             (90, 15, "Taisnu"), (360, 90, "Pilnu"),
             (180, 30, "Izstieptu"), (90, 70, "Taisnu"),
             (360, 270, "Pilnu")]),
         },
        {"sr": "Nosaka daļu no izstiepta un pilna leņķa",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dala_lenka, [
             (1, 2, 180, "izstiepta"), (1, 4, 360, "pilna"),
             (1, 3, 180, "izstiepta"), (1, 2, 360, "pilna"),
             (2, 3, 180, "izstiepta"), (1, 6, 360, "pilna"),
             (1, 6, 180, "izstiepta"), (3, 4, 360, "pilna"),
             (1, 9, 180, "izstiepta"), (1, 8, 360, "pilna"),
             (5, 6, 180, "izstiepta"), (2, 3, 360, "pilna"),
             (1, 4, 180, "izstiepta"), (5, 8, 360, "pilna"),
             (1, 5, 180, "izstiepta")]),
         },
        {"sr": "Saista riņķa līnijas rādiusu un diametru",
         "stunda": TEMATS,
         "jautajumi": V.kopa(diametrs, [
             4, 5, 7, 8, 10, 12, 3, 6, 9, 11, 14, 15, 20, 25, 18]),
         },
        {"sr": "Aprēķina riņķa līnijas garumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(linijas_garums, [
             5, 10, 3, 7, 8, 12, 4, 6, 9, 15, 11, 20, 13, 25, 2]),
         },
        {"sr": "Zina cirkuļa lietojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko zīmē ar cirkuli?",
              ["riņķa līniju", "taisnu leņķi", "kvadrātu",
               "skaitļu taisni"], 0),
             ("Kā ar cirkuli atliek nogriezni, kas vienāds ar doto?",
              ["cirkuļa atvērumu ņem vienādu ar doto nogriezni",
               "nogriezni izmēra ar transportieri", "nogriezni pārloka",
               "nogriezni uzzīmē no acs"], 0),
             ("Kā ar cirkuli iegūst 3 reizes garāku nogriezni?",
              ["atliek doto nogriezni 3 reizes pēc kārtas",
               "sareizina cirkuļa atvērumu ar 3", "uzzīmē 3 riņķa līnijas",
               "izmēra ar transportieri"], 0),
             ("Ko nosaka cirkuļa atvērums?",
              ["rādiusa garumu", "leņķa lielumu", "laukumu",
               "perimetru"], 0),
             ("Kas ir riņķa līnijas centrs?",
              ["punkts, no kura visi līnijas punkti ir vienādā attālumā",
               "līnijas viduspunkts", "diametra gals",
               "jebkurš punkts iekšpusē"], 0),
             ("Cik rādiusu var novilkt vienā riņķa līnijā?",
              ["bezgalīgi daudz", "vienu", "divus", "četrus"], 0),
             ("Kas ir riņķa diametrs?",
              ["horda caur centru", "jebkura horda", "rādiusa puse",
               "riņķa līnijas garums"], 0),
             ("Kā zīmē divas riņķa līnijas ar vienu centru?",
              ["maina tikai cirkuļa atvērumu", "pārvieto adatu",
               "zīmē no acs", "lieto lineālu"], 0),
         ]},
        {"sr": "Aprēķina taisnstūra laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(laukums, [
             (6, 4), (8, 5), (7, 7), (9, 6), (12, 3), (10, 8), (5, 11),
             (14, 4), (13, 6), (15, 5), (16, 7), (18, 9), (20, 6),
             (11, 12), (17, 8)]),
         },
        {"sr": "Nosaka nezināmo malu, ja zināms laukums",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nezinama_mala, [
             (24, 6), (45, 9), (56, 7), (36, 4), (72, 8), (64, 16),
             (81, 9), (48, 12), (100, 10), (90, 15), (54, 6), (42, 14),
             (63, 7), (120, 8), (144, 12)]),
         },
        {"sr": "Aprēķina kombinētas figūras laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kombineta, [
             (12, 8), (18, 14), (20, 15), (24, 6), (30, 12), (16, 9),
             (36, 18), (25, 11), (40, 22), (28, 17), (45, 15), (32, 13),
             (50, 24), (21, 19), (60, 27)]),
         },
        {"sr": "Aprēķina perimetru un risina uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Taisnstūra malas ir 8 cm un 5 cm. Cik garš ir perimetrs?",
              ["26 cm", "40 cm", "13 cm", "18 cm"], 0),
             ("Kvadrāta mala ir 9 cm. Cik garš ir perimetrs?",
              ["36 cm", "81 cm", "18 cm", "27 cm"], 0),
             ("Taisnstūra perimetrs ir 20 cm, viena mala — 6 cm. Cik gara "
              "ir otra?", ["4 cm", "14 cm", "10 cm", "3 cm"], 0),
             ("Ar kuru formulu aprēķina taisnstūra perimetru?",
              ["P = 2 · (a + b)", "P = a · b", "P = a + b", "P = 4 · a"], 0),
             ("Istabas grīda 4 m un 3 m; 1 m² segums maksā 12 eiro. Cik "
              "maksās?", ["144 eiro", "84 eiro", "12 eiro", "168 eiro"], 0),
             ("Dārza dobe 8 m un 5 m. Cik liels ir laukums?",
              ["40 m²", "26 m²", "13 m²", "45 m²"], 0),
             ("No kvadrāta ar laukumu 25 cm² izgriež 6 cm². Cik paliek?",
              ["19 cm²", "31 cm²", "150 cm²", "21 cm²"], 0),
             ("Kā aprēķina kombinētas figūras laukumu?",
              ["sadala to daļās un saskaita laukumus",
               "izmēra tikai vienu malu", "saskaita visas malas",
               "sareizina visas malas"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.6. temata noslēgumā. "
                "Pārbauda leņķu veidus un aprēķinus ar leņķiem, riņķa "
                "līnijas lielumus, taisnstūra laukumu un nezināmo malu, "
                "mērvienību pārveidošanu un kombinētas figūras laukumu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Nosaka leņķa veidu un lielumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(lenka_veids, [
             145, 80, 90, 180, 300, 55, 125, 25, 165, 220, 70, 100,
             350, 10, 175]),
         },
        {"sr": "Aprēķina leņķa lielumu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(starpiba, [
             (180, 75, "Izstieptu"), (90, 35, "Taisnu"),
             (360, 150, "Pilnu"), (180, 95, "Izstieptu"),
             (90, 20, "Taisnu"), (360, 240, "Pilnu"),
             (180, 110, "Izstieptu")])
             + V.kopa(summa, [
                 (48, 52), (25, 40), (60, 30), (35, 55), (18, 72),
                 (45, 45), (12, 78), (65, 15)])),
         },
        {"sr": "Lieto riņķa līnijas lielumus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(diametrs, [
             7, 9, 11, 13, 16, 17, 19])
             + V.kopa(linijas_garums, [
                 3, 5, 6, 8, 10, 14, 18, 22])),
         },
        {"sr": "Aprēķina taisnstūra laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(laukums, [
             (8, 5), (9, 9), (12, 4), (7, 6), (14, 3), (11, 8), (6, 13),
             (15, 4), (10, 7), (16, 5), (18, 6), (20, 9), (22, 4),
             (13, 11), (19, 7)]),
         },
        {"sr": "Nosaka nezināmo malu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nezinama_mala, [
             (56, 7), (36, 4), (63, 9), (80, 8), (96, 12), (49, 7),
             (108, 9), (64, 4), (110, 10), (75, 15), (66, 6), (56, 14),
             (77, 7), (128, 8), (156, 12)]),
         },
        {"sr": "Aprēķina kombinētas figūras laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kombineta, [
             (18, 14), (22, 16), (25, 18), (28, 7), (34, 14), (19, 11),
             (40, 20), (27, 13), (44, 24), (31, 19), (48, 17), (35, 15),
             (55, 26), (23, 21), (66, 29)]),
         },
    ],
    "uzdevumi": [
        {"sr": "Aprēķina leņķu lielumus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Aprēķini leņķi",
             lambda a, b, c, d: [
                 ("Izstiepts leņķis sadalīts %d° un ……" % a,
                  "%d°" % (180 - a)),
                 ("Blakus leņķi %d° un %d° veido ……" % (b, c),
                  "%d°" % (b + c)),
                 ("{1|%d} no izstiepta leņķa ir ……" % d,
                  "%d°" % (180 // d)),
                 ("Pilns leņķis bez %d° ir ……" % a, "%d°" % (360 - a))],
             [(70, 25, 40, 2), (45, 55, 35, 3), (120, 18, 62, 4),
              (60, 48, 52, 2), (135, 15, 75, 3), (90, 30, 60, 4),
              (30, 80, 40, 2), (150, 12, 38, 3), (100, 65, 25, 4),
              (110, 42, 28, 2), (25, 33, 57, 3), (160, 27, 63, 4),
              (75, 70, 20, 2), (50, 22, 68, 3), (140, 36, 54, 4)]),
         },
        {"sr": "Pārveido mērvienības un lieto laukuma formulu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Garumi un laukumi",
             lambda dm, a, b, s, c: [
                 ("%d dm = …… cm" % dm, V.sk(dm * 10)),
                 ("Taisnstūris %d cm un %d cm:  S = …… cm²" % (a, b),
                  V.sk(a * b)),
                 ("S = %d cm², a = %d cm, tad b = …… cm" % (s, c),
                  V.sk(s // c))],
             [(3, 30, 20, 42, 6), (2, 50, 40, 72, 8), (5, 50, 12, 64, 4),
              (4, 25, 16, 90, 9), (6, 35, 14, 55, 5), (7, 45, 18, 84, 7),
              (8, 60, 15, 96, 12), (9, 22, 11, 100, 10), (10, 18, 13, 33, 3),
              (12, 24, 17, 121, 11), (15, 36, 19, 169, 13),
              (11, 40, 21, 196, 14), (13, 28, 23, 225, 15),
              (14, 32, 25, 256, 16), (20, 44, 27, 289, 17)]),
         },
        {"sr": "Aprēķina kombinētas figūras laukumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Kombinēta figūra",
             lambda a, b, c, cena: {
                 "teksts": "Istabas grīdu veido divi taisnstūri: pirmais "
                           "%d m un %d m, otrs %d m un %d m.   a) Aprēķini "
                           "pirmā laukumu!   b) Aprēķini otrā laukumu!   "
                           "c) Cik liels ir visas grīdas laukums?   d) Cik "
                           "maksās grīdas segums, ja 1 m² maksā %d eiro?"
                           % (a, b, c, b, cena),
                 "kriteriji": [
                     "a) %d · %d = %d m².   (1 p.)" % (a, b, a * b),
                     "b) %d · %d = %d m².   (1 p.)" % (c, b, c * b),
                     "c) %d + %d = %d m².   (1 p.)"
                     % (a * b, c * b, a * b + c * b),
                     "d) %d · %d = %d eiro.   (1 p.)"
                     % (a * b + c * b, cena, (a * b + c * b) * cena)]},
             [(4, 3, 2, 12), (5, 4, 3, 10), (6, 2, 4, 15), (3, 5, 2, 20),
              (7, 3, 5, 9), (8, 2, 6, 11), (4, 6, 3, 14), (9, 4, 2, 13),
              (5, 7, 4, 8), (10, 3, 5, 16), (6, 5, 7, 7), (11, 2, 8, 18),
              (7, 6, 3, 6), (12, 4, 9, 5), (8, 7, 5, 17)]),
         },
        {"sr": "Spriež par riņķa līniju, leņķiem un taisnstūri",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Riņķa līnija",
             lambda r: {
                 "ievads": "Riņķa līnijas rādiuss ir %d cm." % r,
                 "jaut": [("Cik garš ir diametrs?", 1),
                          ("Cik aptuveni garš ir riņķa līnija?", 1),
                          ("Paskaidro, kā ieguvi riņķa līnijas garumu!",
                           1)],
                 "atbildes": [
                     "1) d = 2 · %d = %d cm.   (1 p.)" % (r, 2 * r),
                     "2) C ≈ 6 · %d = %d cm.   (1 p.)" % (r, 6 * r),
                     "3) Rādiusu reizina ar 6, jo riņķa līnijas garums ir "
                     "aptuveni 6 rādiusi.   (1 p.)"]},
             [6, 5, 4, 7, 8, 3, 9, 10, 12, 15, 11, 20, 13, 25, 2]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
