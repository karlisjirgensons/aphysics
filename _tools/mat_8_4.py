# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.4. Kā aprēķina laukumu jebkuram trijstūrim, riņķim?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.4. temats): trijstūra laukums
un tā saistība ar taisnstūra laukumu, trijstūra augstumi, riņķa laukums un
riņķa sektora laukums, figūras sadalīšana zināmās figūrās, taisnas prizmas un
cilindra zīmēšana, virsmas laukums un tilpums.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.4."
NOSAUKUMS = "Kā aprēķina laukumu jebkuram trijstūrim, riņķim?"

ATGADNE = [
    "Trijstūris:   S = {a · h|2}   ·   riņķis:   S = πR²,   riņķa līnija:   "
    "C = 2πR   ·   sektors ar leņķi α:   S = πR² · {α|360°}",
    "Taisnai prizmai un cilindram tilpumu aprēķina vienādi:   V = S · h,  "
    " kur S ir pamata laukums.",
    "Cilindrs:   V = πR²h   ·   sānu virsma:   S = 2πRh   ·   pilna virsma: "
    "  S = 2πR² + 2πRh   ·   aprēķinos π ≈ 3,14.",
]


# ---------------------------------------------------------------- veidnes
def trijsturis(a, h):
    """Trijstūra laukums pēc malas un pret to novilktā augstuma."""
    return ("Trijstūra mala ir %d cm, pret to novilktais augstums — %d cm. "
            "Cik liels ir laukums?" % (a, h),
            V.izvele("%s cm²" % V.dalu(a * h, 2), "%d cm²" % (a * h),
                     "%d cm²" % (a + h), "%s cm²" % V.dalu(a + h, 2),
                     "%d cm²" % (2 * a * h), "%d cm²" % (a * h + 2)), 0)


def trijsturis_mala(s, h):
    """Trijstūra mala, ja zināms laukums un augstums."""
    return ("Trijstūra laukums ir %d cm², augstums — %d cm. Cik gara ir "
            "mala, pret kuru novilkts augstums?" % (s, h),
            V.izvele("%s cm" % V.dalu(2 * s, h), "%s cm" % V.dalu(s, h),
                     "%d cm" % (s * h), "%d cm" % (s - h),
                     "%s cm" % V.dalu(s, 2 * h), "%d cm" % (s + h)), 0)


def rinkis(r):
    """Riņķa laukums ar π ≈ 3,14."""
    s = 3.14 * r * r
    return ("Riņķa rādiuss ir %d cm. Cik liels ir laukums (π ≈ 3,14)?" % r,
            V.izvele("%s cm²" % V.sk(round(s, 2)),
                     "%s cm²" % V.sk(round(2 * 3.14 * r, 2)),
                     "%s cm²" % V.sk(round(3.14 * r, 2)),
                     "%s cm²" % V.sk(round(s * 2, 2)),
                     "%s cm²" % V.sk(r * r),
                     "%s cm²" % V.sk(round(s + 1, 2))), 0)


def rinka_linija(r):
    """Riņķa līnijas garums ar π ≈ 3,14."""
    c = 2 * 3.14 * r
    return ("Riņķa līnijas rādiuss ir %d cm. Cik garš ir riņķa līnija "
            "(π ≈ 3,14)?" % r,
            V.izvele("%s cm" % V.sk(round(c, 2)),
                     "%s cm" % V.sk(round(3.14 * r * r, 2)),
                     "%s cm" % V.sk(round(3.14 * r, 2)),
                     "%s cm" % V.sk(round(c * 2, 2)),
                     "%s cm" % V.sk(2 * r),
                     "%s cm" % V.sk(round(c + 1, 2))), 0)


def sektors(r, alfa):
    """Riņķa sektora laukums."""
    s = 3.14 * r * r * alfa / 360.0
    return ("Riņķa rādiuss ir %d cm; sektora leņķis — %d°. Cik liels ir "
            "sektora laukums (π ≈ 3,14)?" % (r, alfa),
            V.izvele("%s cm²" % V.sk(round(s, 2)),
                     "%s cm²" % V.sk(round(3.14 * r * r, 2)),
                     "%s cm²" % V.sk(round(s * 2, 2)),
                     "%s cm²" % V.sk(round(s / 2.0, 2)),
                     "%s cm²" % V.sk(round(2 * 3.14 * r * alfa / 360.0, 2)),
                     "%s cm²" % V.sk(round(s + 1, 2))), 0)


def tilpums(s, h):
    """Taisnas prizmas vai cilindra tilpums:  V = S · h."""
    return ("Taisnas prizmas pamata laukums ir %d cm², augstums — %d cm. "
            "Cik liels ir tilpums?" % (s, h),
            V.izvele("%d cm³" % (s * h), "%d cm³" % (s + h),
                     "%s cm³" % V.dalu(s * h, 2), "%d cm³" % (2 * s * h),
                     "%d cm³" % (s - h), "%d cm³" % (s * h + 2)), 0)


def cilindrs(r, h):
    """Cilindra tilpums ar π ≈ 3,14."""
    v = 3.14 * r * r * h
    return ("Cilindra rādiuss ir %d cm, augstums — %d cm. Cik liels ir "
            "tilpums (π ≈ 3,14)?" % (r, h),
            V.izvele("%s cm³" % V.sk(round(v, 2)),
                     "%s cm³" % V.sk(round(3.14 * r * h, 2)),
                     "%s cm³" % V.sk(round(2 * 3.14 * r * h, 2)),
                     "%s cm³" % V.sk(round(v * 2, 2)),
                     "%s cm³" % V.sk(r * r * h),
                     "%s cm³" % V.sk(round(v + 1, 2))), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.4. temata beigās. Pārbauda trijstūra "
                "un riņķa laukuma formulas, sektora laukumu, kombinētas "
                "figūras laukumu un taisnas prizmas un cilindra virsmas "
                "laukumu un tilpumu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina trijstūra laukuma formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina trijstūra laukumu?",
              ["S = {a · h|2}", "S = a · h", "S = a + h",
               "S = 2 · (a + h)"], 0),
             ("No kuras formulas iegūst trijstūra laukuma formulu?",
              ["no taisnstūra laukuma", "no riņķa laukuma",
               "no perimetra", "no tilpuma"], 0),
             ("Cik augstumu ir trijstūrim?", ["trīs", "viens", "divi",
                                              "seši"], 0),
             ("Kas jāievēro, lietojot formulu S = {a · h|2}?",
              ["augstums novilkts pret malu a", "malas ir vienādas",
               "leņķis ir taisns", "trijstūris ir vienādsānu"], 0),
             ("Kā aprēķina taisnleņķa trijstūra laukumu?",
              ["katešu reizinājumu dala ar 2", "malas saskaita",
               "hipotenūzu dala ar 2", "katetes saskaita"], 0),
             ("Kā mainās laukums, ja augstumu dubulto?",
              ["aug 2 reizes", "sarūk 2 reizes", "nemainās",
               "aug 4 reizes"], 0),
             ("Kā mainās laukums, ja abus lielumus dubulto?",
              ["aug 4 reizes", "aug 2 reizes", "nemainās",
               "aug 8 reizes"], 0),
             ("Vai diviem trijstūriem ar vienādu laukumu jābūt vienādiem?",
              ["nē", "jā", "tikai taisnleņķa", "tikai vienādsānu"], 0),
         ]},
        {"sr": "Aprēķina trijstūra laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(trijsturis, [
             (6, 4), (8, 5), (10, 3), (12, 7), (9, 6), (14, 5), (7, 8),
             (16, 9), (11, 4), (18, 6), (13, 10), (20, 7), (15, 8),
             (22, 5), (24, 9)]),
         },
        {"sr": "Nosaka trijstūra malu pēc laukuma",
         "stunda": TEMATS,
         "jautajumi": V.kopa(trijsturis_mala, [
             (24, 6), (30, 5), (40, 8), (18, 3), (54, 9), (28, 7),
             (36, 4), (60, 10), (48, 6), (44, 11), (32, 8), (70, 14),
             (42, 7), (90, 15), (56, 8)]),
         },
        {"sr": "Zina riņķa lielumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina riņķa laukumu?",
              ["S = πR²", "S = 2πR", "S = πR", "S = πD"], 0),
             ("Ar kuru formulu aprēķina riņķa līnijas garumu?",
              ["C = 2πR", "C = πR²", "C = πR", "C = R²"], 0),
             ("Cik aptuveni ir π?", ["3,14", "3,41", "2,14", "31,4"], 0),
             ("Kāds skaitlis ir π?", ["iracionāls", "vesels", "racionāls",
                                      "negatīvs"], 0),
             ("Kā rādiusu izsaka ar diametru?",
              ["R = {D|2}", "R = 2D", "R = D + 2", "R = D²"], 0),
             ("Kā mainās riņķa laukums, ja rādiusu dubulto?",
              ["aug 4 reizes", "aug 2 reizes", "nemainās",
               "aug 8 reizes"], 0),
             ("Kā mainās riņķa līnijas garums, ja rādiusu dubulto?",
              ["aug 2 reizes", "aug 4 reizes", "nemainās",
               "sarūk 2 reizes"], 0),
             ("Kāpēc ar π ≈ 3,14 iegūst tuvinājumu?",
              ["π ir bezgalīga neperiodiska decimāldaļa",
               "formula ir neprecīza", "rādiuss ir aptuvens",
               "tā ir kļūda"], 0),
         ]},
        {"sr": "Aprēķina riņķa laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(rinkis, [
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 11, 13]),
         },
        {"sr": "Aprēķina riņķa līnijas garumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(rinka_linija, [
             1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 11, 13]),
         },
        {"sr": "Aprēķina riņķa sektora laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sektors, [
             (6, 90), (10, 180), (4, 90), (6, 60), (12, 30), (8, 45),
             (10, 36), (6, 120), (5, 72), (9, 40), (12, 90), (15, 24),
             (20, 18), (3, 120), (18, 20)]),
         },
        {"sr": "Aprēķina kombinētas figūras laukumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Figūru veido taisnstūris 20 cm² un trijstūris 6 cm². Cik "
              "liels ir laukums?", ["26 cm²", "14 cm²", "120 cm²",
                                    "13 cm²"], 0),
             ("No taisnstūra 40 cm² izgriež trijstūri 12 cm². Cik liels ir "
              "atlikums?", ["28 cm²", "52 cm²", "480 cm²", "14 cm²"], 0),
             ("Kā aprēķina kombinētas figūras laukumu?",
              ["sadala to zināmās figūrās", "saskaita malas",
               "mēra garāko malu", "dala perimetru ar 2"], 0),
             ("Taisnstūris 8 cm un 5 cm; tajā ierakstīts trijstūris ar "
              "pamatu 8 cm un augstumu 5 cm. Kāda daļa ir trijstūris?",
              ["puse", "trešdaļa", "ceturtdaļa", "viss"], 0),
             ("Kvadrāts ar malu 10 cm; tajā ierakstīts riņķis ar rādiusu "
              "5 cm. Cik liels ir riņķa laukums?",
              ["78,5 cm²", "100 cm²", "31,4 cm²", "50 cm²"], 0),
             ("Tajā pašā figūrā — cik liels ir laukums ārpus riņķa?",
              ["21,5 cm²", "78,5 cm²", "50 cm²", "31,4 cm²"], 0),
             ("Kāpēc figūru sadala daļās?",
              ["lai lietotu zināmas formulas", "lai būtu skaistāk",
               "lai samazinātu laukumu", "tas nav vajadzīgs"], 0),
             ("Ko dara, ja figūru nevar sadalīt?",
              ["papildina līdz zināmai figūrai un atņem lieko",
               "atstāj neatrisinātu", "mēra ar lineālu",
               "noapaļo laukumu"], 0),
         ]},
        {"sr": "Zina telpisku ķermeņu attēlošanu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas saglabājas, attēlojot telpisku ķermeni plaknē?",
              ["paralelitāte", "visi leņķi", "visi garumi",
               "visi laukumi"], 0),
             ("Kas nesaglabājas telpiska ķermeņa attēlā?",
              ["leņķu lielumi", "paralelitāte",
               "nogriežņu garumu attiecība uz vienas taisnes",
               "virsotņu skaits"], 0),
             ("Kāda figūra ir taisnas prizmas pamats?",
              ["daudzstūris", "riņķis", "lode", "taisne"], 0),
             ("Kāda figūra ir cilindra pamats?",
              ["riņķis", "kvadrāts", "trijstūris", "daudzstūris"], 0),
             ("Kāda figūra ir cilindra sānu virsmas izklājums?",
              ["taisnstūris", "riņķis", "trijstūris", "kvadrāts"], 0),
             ("Cik pamatu ir cilindram?", ["divi", "viens", "trīs",
                                           "neviens"], 0),
             ("Kā zīmē prizmas neredzamās šķautnes?",
              ["ar pārtrauktu līniju", "ar biezu līniju",
               "tās nezīmē", "ar sarkanu krāsu"], 0),
             ("Kas ir taisna prizma?",
              ["prizma, kuras sānu šķautnes ir perpendikulāras pamatam",
               "prizma ar kvadrāta pamatu", "prizma bez pamata",
               "cilindrs"], 0),
         ]},
        {"sr": "Aprēķina prizmas tilpumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(tilpums, [
             (12, 5), (20, 6), (15, 8), (24, 4), (30, 7), (18, 9),
             (36, 3), (40, 5), (25, 10), (48, 6), (50, 4), (60, 8),
             (35, 12), (45, 7), (54, 9)]),
         },
        {"sr": "Aprēķina cilindra tilpumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(cilindrs, [
             (1, 5), (2, 3), (3, 4), (4, 2), (5, 6), (2, 10), (6, 3),
             (3, 8), (7, 2), (10, 5), (4, 7), (8, 3), (5, 12), (9, 4),
             (12, 2)]),
         },
        {"sr": "Lieto sakarības starp lielumiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina taisnas prizmas tilpumu?",
              ["V = S · h", "V = S + h", "V = {S|h}", "V = 2S · h"], 0),
             ("Cilindra tilpums ir 100 cm³, pamata laukums — 20 cm². Cik "
              "liels ir augstums?", ["5 cm", "2000 cm", "80 cm",
                                     "120 cm"], 0),
             ("Prizmas tilpums ir 120 cm³, augstums — 10 cm. Cik liels ir "
              "pamata laukums?", ["12 cm²", "1200 cm²", "110 cm²",
                                  "130 cm²"], 0),
             ("Ar kuru formulu aprēķina cilindra sānu virsmas laukumu?",
              ["S = 2πRh", "S = πR²", "S = πRh", "S = 2πR²"], 0),
             ("Kā mainās cilindra tilpums, ja rādiusu dubulto?",
              ["aug 4 reizes", "aug 2 reizes", "nemainās",
               "aug 8 reizes"], 0),
             ("Kā mainās cilindra tilpums, ja augstumu dubulto?",
              ["aug 2 reizes", "aug 4 reizes", "nemainās",
               "aug 8 reizes"], 0),
             ("Cik litru ir 1000 cm³?", ["1 l", "10 l", "100 l",
                                         "0,1 l"], 0),
             ("Kāpēc prizmai un cilindram ir viena tilpuma formula?",
              ["abiem tilpums ir pamata laukums reiz augstums",
               "abiem pamats ir riņķis", "abi ir taisni",
               "tā ir sagadīšanās"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.4. temata noslēgumā. "
                "Pārbauda trijstūra un riņķa laukumu, sektora laukumu, "
                "kombinētas figūras laukumu un prizmas un cilindra tilpumu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Aprēķina trijstūra laukumu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(trijsturis, [
             (8, 6), (10, 5), (12, 4), (14, 7), (9, 8), (16, 5), (7, 6)])
             + V.kopa(trijsturis_mala, [
                 (36, 6), (40, 5), (50, 10), (24, 4), (63, 9), (30, 6),
                 (44, 8), (72, 12)])),
         },
        {"sr": "Zina laukuma formulas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru formulu aprēķina trijstūra laukumu?",
              ["S = {a · h|2}", "S = a · h", "S = a + h",
               "S = 2 · (a + h)"], 0),
             ("Ar kuru formulu aprēķina riņķa laukumu?",
              ["S = πR²", "S = 2πR", "S = πR", "S = πD"], 0),
             ("Ar kuru formulu aprēķina riņķa līnijas garumu?",
              ["C = 2πR", "C = πR²", "C = πR", "C = R²"], 0),
             ("Kāds skaitlis ir π?", ["iracionāls", "vesels", "racionāls",
                                      "negatīvs"], 0),
             ("Cik augstumu ir trijstūrim?", ["trīs", "viens", "divi",
                                              "seši"], 0),
             ("Kā mainās riņķa laukums, ja rādiusu dubulto?",
              ["aug 4 reizes", "aug 2 reizes", "nemainās",
               "aug 8 reizes"], 0),
             ("Ar kuru formulu aprēķina taisnas prizmas tilpumu?",
              ["V = S · h", "V = S + h", "V = {S|h}", "V = 2S · h"], 0),
             ("Ar kuru formulu aprēķina cilindra sānu virsmas laukumu?",
              ["S = 2πRh", "S = πR²", "S = πRh", "S = 2πR²"], 0),
         ]},
        {"sr": "Aprēķina riņķa lielumus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(rinkis, [
             2, 3, 4, 5, 6, 8, 10])
             + V.kopa(rinka_linija, [
                 1, 7, 9, 11, 12, 13, 15, 20])),
         },
        {"sr": "Aprēķina sektora laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sektors, [
             (6, 90), (10, 180), (4, 90), (6, 60), (12, 30), (8, 45),
             (10, 36), (6, 120), (5, 72), (9, 40), (12, 90), (15, 24),
             (20, 18), (3, 120), (18, 20)]),
         },
        {"sr": "Aprēķina prizmas un cilindra tilpumu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(tilpums, [
             (14, 5), (22, 6), (16, 8), (26, 4), (32, 7), (19, 9),
             (38, 3)])
             + V.kopa(cilindrs, [
                 (1, 4), (2, 5), (3, 3), (4, 6), (5, 2), (6, 4), (10, 3),
                 (7, 5)])),
         },
        {"sr": "Lieto sakarības starp lielumiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cilindra tilpums ir 100 cm³, pamata laukums — 20 cm². Cik "
              "liels ir augstums?", ["5 cm", "2000 cm", "80 cm",
                                     "120 cm"], 0),
             ("Prizmas tilpums ir 120 cm³, augstums — 10 cm. Cik liels ir "
              "pamata laukums?", ["12 cm²", "1200 cm²", "110 cm²",
                                  "130 cm²"], 0),
             ("Kā mainās cilindra tilpums, ja rādiusu dubulto?",
              ["aug 4 reizes", "aug 2 reizes", "nemainās",
               "aug 8 reizes"], 0),
             ("Cik litru ir 1000 cm³?", ["1 l", "10 l", "100 l",
                                         "0,1 l"], 0),
             ("Kāda figūra ir cilindra sānu virsmas izklājums?",
              ["taisnstūris", "riņķis", "trijstūris", "kvadrāts"], 0),
             ("Kā aprēķina kombinētas figūras laukumu?",
              ["sadala to zināmās figūrās", "saskaita malas",
               "mēra garāko malu", "dala perimetru ar 2"], 0),
             ("Kas saglabājas, attēlojot telpisku ķermeni plaknē?",
              ["paralelitāte", "visi leņķi", "visi garumi",
               "visi laukumi"], 0),
             ("Kāpēc prizmai un cilindram ir viena tilpuma formula?",
              ["abiem tilpums ir pamata laukums reiz augstums",
               "abiem pamats ir riņķis", "abi ir taisni",
               "tā ir sagadīšanās"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina laukumus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Laukumi",
             lambda a, h, r, alfa: [
                 ("Trijstūris  a = %d cm,  h = %d cm;  S = …… cm²"
                  % (a, h), V.dalu(a * h, 2)),
                 ("Trijstūris  S = %d cm²,  h = %d cm;  a = …… cm"
                  % (a * h, h), V.sk(2 * a)),
                 ("Riņķis  R = %d cm;  S = …… cm²  (π ≈ 3,14)" % r,
                  V.sk(round(3.14 * r * r, 2))),
                 ("Sektors  R = %d cm,  α = %d°;  S = …… cm²" % (r, alfa),
                  V.sk(round(3.14 * r * r * alfa / 360.0, 2)))],
             [(6, 4, 2, 90), (8, 5, 3, 180), (10, 3, 4, 90), (12, 7, 5, 60),
              (9, 6, 6, 30), (14, 5, 2, 45), (7, 8, 10, 36),
              (16, 9, 3, 120), (11, 4, 5, 72), (18, 6, 9, 40),
              (13, 10, 12, 90), (20, 7, 15, 24), (15, 8, 20, 18),
              (22, 5, 3, 120), (24, 9, 18, 20)]),
         },
        {"sr": "Aprēķina tilpumus",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Tilpumi",
             lambda s, h, r: [
                 ("Prizma  S = %d cm²,  h = %d cm;  V = …… cm³" % (s, h),
                  V.sk(s * h)),
                 ("Prizma  V = %d cm³,  h = %d cm;  S = …… cm²"
                  % (s * h, h), V.sk(s)),
                 ("Cilindrs  R = %d cm,  h = %d cm;  V = …… cm³" % (r, h),
                  V.sk(round(3.14 * r * r * h, 2)))],
             [(12, 5, 2), (20, 6, 3), (15, 8, 1), (24, 4, 4), (30, 7, 2),
              (18, 9, 3), (36, 3, 5), (40, 5, 2), (25, 10, 6),
              (48, 6, 4), (50, 4, 7), (60, 8, 3), (35, 12, 5),
              (45, 7, 8), (54, 9, 10)]),
         },
        {"sr": "Risina uzdevumu par kombinētu figūru",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Kombinēta figūra",
             lambda a, b, h, r: {
                 "teksts": "Figūru veido taisnstūris ar malām %d cm un "
                           "%d cm un trijstūris ar pamatu %d cm un "
                           "augstumu %d cm.   a) Aprēķini taisnstūra "
                           "laukumu!   b) Aprēķini trijstūra laukumu!   "
                           "c) Cik liels ir visas figūras laukums?   "
                           "d) Cik liels būtu riņķa laukums ar rādiusu "
                           "%d cm (π ≈ 3,14)?" % (a, b, a, h, r),
                 "kriteriji": [
                     "a) %d · %d = %d cm².   (1 p.)" % (a, b, a * b),
                     "b) %d · %d : 2 = %s cm².   (1 p.)"
                     % (a, h, V.dalu(a * h, 2)),
                     "c) %d + %s = %s cm².   (1 p.)"
                     % (a * b, V.dalu(a * h, 2),
                        V.sk(a * b + a * h / 2.0)),
                     "d) 3,14 · %d² = %s cm².   (1 p.)"
                     % (r, V.sk(round(3.14 * r * r, 2)))]},
             [(8, 5, 4, 2), (10, 6, 6, 3), (12, 4, 8, 4), (6, 7, 10, 5),
              (14, 5, 4, 6), (9, 8, 6, 2), (16, 3, 12, 7), (11, 6, 8, 3),
              (18, 4, 10, 8), (13, 7, 6, 4), (20, 5, 14, 9),
              (15, 8, 12, 5), (22, 6, 8, 10), (17, 4, 16, 6),
              (24, 7, 10, 12)]),
         },
        {"sr": "Pamato laukuma un tilpuma aprēķinus",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Cilindrs",
             lambda r, h: {
                 "ievads": "Cilindra rādiuss ir %d cm, augstums — %d cm "
                           "(π ≈ 3,14)." % (r, h),
                 "jaut": [("Aprēķini pamata laukumu!", 1),
                          ("Aprēķini tilpumu!", 1),
                          ("Cik litru tas ir?", 1)],
                 "atbildes": [
                     "1) 3,14 · %d² = %s cm².   (1 p.)"
                     % (r, V.sk(round(3.14 * r * r, 2))),
                     "2) %s · %d = %s cm³.   (1 p.)"
                     % (V.sk(round(3.14 * r * r, 2)), h,
                        V.sk(round(3.14 * r * r * h, 2))),
                     "3) %s l.   (1 p.)"
                     % V.sk(round(3.14 * r * r * h / 1000.0, 3))]},
             [(5, 10), (10, 20), (4, 15), (6, 12), (8, 10), (3, 20),
              (7, 14), (9, 10), (12, 5), (15, 4), (2, 25), (11, 8),
              (13, 6), (14, 10), (20, 3)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
