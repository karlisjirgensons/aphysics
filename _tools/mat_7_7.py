# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.7. Ko nozīmē pārveidot izteiksmi ar mainīgo?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.7. temats): algebriska
izteiksme un tās vērtība, situāciju apraksts ar izteiksmi («par tik
vairāk/mazāk», «tik reižu vairāk/mazāk», «tik procentu no»), līdzīgu
saskaitāmo savilkšana, summas reizināšana un dalīšana ar skaitli, iekavu
atvēršana un identiski vienādas izteiksmes.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.7."
NOSAUKUMS = "Ko nozīmē pārveidot izteiksmi ar mainīgo lielumu?"

ATGADNE = [
    "Līdzīgus saskaitāmos savelk, saskaitot koeficientus:   3a + 7a = 10a  "
    " ·   5x − 2x = 3x   ·   a + a + a = 3a",
    "Summu reizina ar skaitli, reizinot katru saskaitāmo:   k(a + b) = "
    "ka + kb   ·   summu dala tāpat:   {a + b|k} = {a|k} + {b|k}",
    "Atņemot summu, maina visu tās locekļu zīmes:   a − (b + c) = a − b − c "
    "  ·   a − (b − c) = a − b + c",
]


# ---------------------------------------------------------------- veidnes
def savelk(a, b):
    """Līdzīgu saskaitāmo savilkšana."""
    return ("Savelc līdzīgos saskaitāmos:  %da + %da." % (a, b),
            V.izvele("%da" % (a + b), "%da" % (a * b), "%da" % abs(a - b),
                     "%da²" % (a + b), "%d + a" % (a + b),
                     "%da" % (a + b + 1)), 0)


def savelk_starpiba(a, b):
    """Līdzīgu saskaitāmo savilkšana ar atņemšanu."""
    return ("Savelc līdzīgos saskaitāmos:  %dx − %dx." % (a, b),
            V.izvele("%dx" % (a - b), "%dx" % (a + b), "%dx" % (b - a),
                     "%dx²" % (a - b), "%d − x" % (a - b),
                     "%dx" % (a - b + 1)), 0)


def iekavas(k, a, b):
    """Summas reizināšana ar skaitli."""
    return ("Atver iekavas:  %d(%sa + %d)." % (k, "" if a == 1 else a, b),
            V.izvele("%da + %d" % (k * a, k * b),
                     "%da + %d" % (k * a, b),
                     "%da + %d" % (a, k * b),
                     "%da + %d" % (k + a, k + b),
                     "%da" % (k * a + k * b),
                     "%da + %d" % (k * a, k * b + 1)), 0)


def atnem_summu(a, b, c):
    """Summas atņemšana - zīmju maiņa iekavās."""
    return ("Atver iekavas:  %da − (%da + %d)." % (a + b, b, c),
            V.izvele("%da − %d" % (a, c), "%da + %d" % (a, c),
                     "%da − %d" % (a + 2 * b, c),
                     "%da − %d" % (a, c + b),
                     "%da − %d" % (a - b, c), "%da" % a), 0)


def vertiba(k, b, x):
    """Algebriskas izteiksmes vērtība pie dotas mainīgā vērtības."""
    zime = "+" if b >= 0 else "−"
    return ("Cik liela ir izteiksmes  %dx %s %d  vērtība, ja x = %d?"
            % (k, zime, abs(b), x),
            V.izvele(k * x + b, k * x - b, k + x + b, k * x,
                     (k + b) * x, k * x + b + 1, k * (x + b)), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.7. temata beigās. Pārbauda algebriskas "
                "izteiksmes vērtību, līdzīgu saskaitāmo savilkšanu, iekavu "
                "atvēršanu un situāciju pierakstu ar izteiksmi.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kas ir algebriska izteiksme",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir algebriska izteiksme?",
              ["izteiksme, kurā ir mainīgais", "tikai skaitļu virkne",
               "vienādojums", "nevienādība"], 0),
             ("Ko nozīmē pieraksts 4a?",
              ["skaitļu 4 un a reizinājums", "skaitļu 4 un a summa",
               "skaitļu 4 un a starpība", "skaitli 4a"], 0),
             ("Kāpēc izteiksmei var būt dažādas vērtības?",
              ["mainīgā vietā var likt dažādus skaitļus",
               "tā ir kļūda", "tā ir definīcija", "tas nav tiesa"], 0),
             ("Kā pieraksta skaitļa x un 5 summu?",
              ["x + 5", "5x", "x − 5", "{x|5}"], 0),
             ("Kā pieraksta skaitli, kas par 3 lielāks nekā x?",
              ["x + 3", "3x", "x − 3", "{x|3}"], 0),
             ("Kā pieraksta skaitli, kas 3 reizes lielāks nekā x?",
              ["3x", "x + 3", "x − 3", "{x|3}"], 0),
             ("Kā pieraksta skaitli, kas 4 reizes mazāks nekā x?",
              ["{x|4}", "4x", "x − 4", "x + 4"], 0),
             ("Kā pieraksta skaitli, kas par 6 mazāks nekā x?",
              ["x − 6", "6x", "x + 6", "{x|6}"], 0),
         ]},
        {"sr": "Aprēķina izteiksmes vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vertiba, [
             (2, 3, 4), (3, -1, 5), (4, 2, 3), (5, -3, 6), (2, 7, 8),
             (6, 1, 2), (3, 5, 7), (7, -2, 4), (4, -5, 9), (8, 3, 2),
             (5, 4, 6), (9, -1, 3), (6, -4, 5), (10, 2, 7), (3, 8, 11)]),
         },
        {"sr": "Savelk līdzīgus saskaitāmos ar saskaitīšanu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(savelk, [
             (3, 7), (5, 4), (2, 9), (6, 8), (4, 11), (7, 3), (9, 6),
             (8, 12), (10, 5), (11, 4), (12, 7), (13, 9), (14, 6),
             (15, 8), (16, 3)]),
         },
        {"sr": "Savelk līdzīgus saskaitāmos ar atņemšanu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(savelk_starpiba, [
             (9, 4), (12, 5), (15, 7), (8, 3), (11, 6), (14, 9), (10, 2),
             (17, 8), (13, 4), (16, 11), (18, 5), (19, 12), (20, 7),
             (21, 13), (22, 9)]),
         },
        {"sr": "Atver iekavas, reizinot summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(iekavas, [
             (3, 1, 4), (2, 5, 3), (4, 2, 7), (5, 3, 2), (6, 1, 9),
             (7, 4, 5), (2, 8, 11), (8, 3, 6), (9, 2, 4), (3, 7, 8),
             (10, 5, 3), (4, 6, 12), (11, 2, 7), (5, 9, 4), (12, 3, 5)]),
         },
        {"sr": "Atver iekavas, atņemot summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem_summu, [
             (3, 2, 5), (4, 3, 7), (5, 1, 9), (6, 4, 2), (7, 2, 11),
             (2, 5, 6), (8, 3, 4), (9, 6, 13), (10, 2, 8), (11, 4, 3),
             (12, 5, 15), (13, 3, 7), (14, 6, 9), (15, 2, 12), (16, 7, 5)]),
         },
        {"sr": "Zina identiski vienādas izteiksmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir identiski vienādas izteiksmes?",
              ["izteiksmes ar vienādām vērtībām pie visiem x",
               "izteiksmes ar vienādu garumu", "vienādojumi",
               "nevienādības"], 0),
             ("Vai a + a + a = 3a?", ["jā", "nē", "tikai ja a = 1",
                                      "tikai ja a > 0"], 0),
             ("Vai 2a + 3a = 5a²?", ["nē, ir 5a", "jā", "tikai ja a = 0",
                                     "nevar noteikt"], 0),
             ("Vai 3(a + 2) = 3a + 6?", ["jā", "nē", "tikai ja a = 2",
                                         "tikai ja a = 0"], 0),
             ("Vai 3(a + 2) = 3a + 2?", ["nē", "jā", "tikai ja a = 0",
                                         "vienmēr"], 0),
             ("Kā pārbauda, vai izteiksmes ir identiski vienādas?",
              ["pārveido vienu par otru", "ievieto vienu skaitli",
               "salīdzina garumu", "salīdzina burtus"], 0),
             ("Kas ir līdzīgi saskaitāmie?",
              ["saskaitāmie ar vienādu burtu daļu",
               "saskaitāmie ar vienādiem koeficientiem",
               "visi saskaitāmie", "tikai skaitļi"], 0),
             ("Vai 5x un 5y ir līdzīgi saskaitāmie?",
              ["nē", "jā", "tikai ja x = y", "vienmēr"], 0),
         ]},
        {"sr": "Apraksta situāciju ar izteiksmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Burtnīca maksā x eiro. Cik maksā 5 burtnīcas?",
              ["5x eiro", "x + 5 eiro", "x − 5 eiro", "{x|5} eiro"], 0),
             ("Ievai ir x eiro, Jānim — par 4 eiro vairāk. Cik ir Jānim?",
              ["x + 4", "4x", "x − 4", "{x|4}"], 0),
             ("Ievai ir x eiro, Jānim — 4 reizes vairāk. Cik ir Jānim?",
              ["4x", "x + 4", "x − 4", "{x|4}"], 0),
             ("Klasē ir x skolēni; puse no tiem ir meitenes. Cik ir "
              "meiteņu?", ["{x|2}", "2x", "x − 2", "x + 2"], 0),
             ("Taisnstūra malas ir x un x + 3. Kāds ir perimetrs?",
              ["4x + 6", "2x + 3", "x² + 3x", "2x + 6"], 0),
             ("Kvadrāta mala ir a. Kāds ir perimetrs?",
              ["4a", "a²", "2a", "a + 4"], 0),
             ("Divu skaitļu attiecība ir 2 : 3. Kā pieraksta skaitļus?",
              ["2x un 3x", "x + 2 un x + 3", "2 un 3", "{x|2} un {x|3}"], 0),
             ("Trīs skaitļu attiecība ir 1 : 2 : 4. Kāda ir to summa?",
              ["7x", "x + 7", "8x", "6x"], 0),
         ]},
        {"sr": "Lieto procentus izteiksmēs",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cena ir x eiro. Kā pieraksta 20 % no cenas?",
              ["0,2x", "20x", "x + 20", "x − 20"], 0),
             ("Cena ir x eiro, tā pieaug par 10 %. Kāda ir jaunā cena?",
              ["1,1x", "0,1x", "x + 10", "10x"], 0),
             ("Cena ir x eiro, tai atlaide 25 %. Kāda ir jaunā cena?",
              ["0,75x", "0,25x", "x − 25", "25x"], 0),
             ("Skaitlis x palielināts par 50 %. Kāds tas ir?",
              ["1,5x", "0,5x", "x + 50", "50x"], 0),
             ("Skaitlis x samazināts par 40 %. Kāds tas ir?",
              ["0,6x", "0,4x", "x − 40", "40x"], 0),
             ("Kā pieraksta 5 % no skaitļa a?",
              ["0,05a", "5a", "a + 5", "{a|5}"], 0),
             ("Ko nozīmē 1,2x?",
              ["x, palielināts par 20 %", "x, samazināts par 20 %",
               "20 % no x", "x plus 1,2"], 0),
             ("Ko nozīmē 0,8x?",
              ["x, samazināts par 20 %", "x, palielināts par 20 %",
               "80 % pieaugums", "x mīnus 0,8"], 0),
         ]},
        {"sr": "Dala summu ar skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {6a + 9|3}?", ["2a + 3", "6a + 3", "2a + 9",
                                     "18a + 27"], 0),
             ("Cik ir {10x − 5|5}?", ["2x − 1", "10x − 1", "2x − 5",
                                      "50x − 25"], 0),
             ("Cik ir {8a + 12|4}?", ["2a + 3", "8a + 3", "2a + 12",
                                      "32a + 48"], 0),
             ("Cik ir {15x + 20|5}?", ["3x + 4", "15x + 4", "3x + 20",
                                       "75x + 100"], 0),
             ("Cik ir {4a|2}?", ["2a", "4a", "8a", "2a²"], 0),
             ("Kā dala summu ar skaitli?",
              ["dala katru saskaitāmo", "dala tikai pirmo",
               "dala tikai pēdējo", "reizina saskaitāmos"], 0),
             ("Cik ir {9x + 3|3}?", ["3x + 1", "9x + 1", "3x + 3",
                                     "27x + 9"], 0),
             ("Cik ir {2a + 6|2}?", ["a + 3", "2a + 3", "a + 6",
                                     "4a + 12"], 0),
         ]},
        {"sr": "Vienkāršo izteiksmes ar vairākām darbībām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienkāršo:  2(a + 3) + 4a.", ["6a + 6", "2a + 6", "6a + 3",
                                             "8a + 6"], 0),
             ("Vienkāršo:  3(x − 2) + 5.", ["3x − 1", "3x − 6", "3x + 3",
                                            "8x − 1"], 0),
             ("Vienkāršo:  5a − 2(a + 1).", ["3a − 2", "3a + 2", "7a − 2",
                                             "3a − 1"], 0),
             ("Vienkāršo:  4(x + 1) − x.", ["3x + 4", "5x + 4", "3x + 1",
                                            "4x + 4"], 0),
             ("Vienkāršo:  a + a + 2a.", ["4a", "3a", "2a²", "a³"], 0),
             ("Vienkāršo:  2(a + b) − 2b.", ["2a", "2a + 4b", "2a − 4b",
                                             "4a"], 0),
             ("Vienkāršo:  6x − (2x + 3).", ["4x − 3", "4x + 3", "8x − 3",
                                             "4x"], 0),
             ("Vienkāršo:  7a − (3a − 5).", ["4a + 5", "4a − 5", "10a − 5",
                                             "4a"], 0),
         ]},
        {"sr": "Zina darbību īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Uz kuru īpašību balstās iekavu atvēršana?",
              ["reizināšanas sadalāmības īpašību",
               "saskaitīšanas secību", "dalīšanas likumu",
               "kāpināšanas likumu"], 0),
             ("Vai a + b = b + a?", ["jā", "nē", "tikai ja a = b",
                                     "tikai pozitīviem"], 0),
             ("Vai a − b = b − a?", ["nē", "jā", "vienmēr",
                                     "tikai pozitīviem"], 0),
             ("Ar ko vienāds a · 1?", ["a", "1", "0", "2a"], 0),
             ("Ar ko vienāds a · 0?", ["0", "a", "1", "−a"], 0),
             ("Ar ko vienāds a + 0?", ["a", "0", "1", "2a"], 0),
             ("Ar ko vienāds a − a?", ["0", "a", "2a", "1"], 0),
             ("Ar ko vienāds −(a + b)?", ["−a − b", "−a + b", "a − b",
                                          "a + b"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.7. temata noslēgumā. "
                "Pārbauda izteiksmes vērtību, līdzīgu saskaitāmo "
                "savilkšanu, iekavu atvēršanu, summas dalīšanu un situāciju "
                "pierakstu ar izteiksmi.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Aprēķina izteiksmes vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vertiba, [
             (3, 2, 5), (4, -3, 6), (5, 1, 4), (6, -2, 7), (2, 9, 3),
             (7, 4, 2), (8, -5, 3), (9, 2, 4), (10, -1, 5), (11, 3, 2),
             (12, -4, 3), (2, 11, 6), (13, 1, 4), (3, 12, 5), (14, -2, 3)]),
         },
        {"sr": "Savelk līdzīgus saskaitāmos",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(savelk, [
             (4, 8), (6, 5), (3, 10), (7, 9), (5, 12), (8, 4), (11, 7)])
             + V.kopa(savelk_starpiba, [
                 (10, 3), (13, 6), (16, 8), (9, 2), (12, 7), (15, 10),
                 (11, 5), (18, 9)])),
         },
        {"sr": "Atver iekavas, reizinot summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(iekavas, [
             (2, 3, 5), (3, 4, 6), (5, 2, 8), (4, 5, 3), (7, 1, 10),
             (6, 3, 4), (8, 2, 9), (9, 4, 2), (10, 3, 7), (11, 1, 5),
             (12, 2, 6), (2, 9, 13), (13, 3, 4), (3, 8, 11), (14, 2, 5)]),
         },
        {"sr": "Atver iekavas, atņemot summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem_summu, [
             (4, 3, 6), (5, 2, 8), (6, 5, 10), (7, 3, 4), (8, 4, 12),
             (3, 6, 7), (9, 2, 5), (10, 7, 14), (11, 3, 9), (12, 5, 4),
             (13, 6, 16), (14, 4, 8), (15, 7, 10), (16, 3, 13), (17, 8, 6)]),
         },
        {"sr": "Dala summu ar skaitli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {6a + 9|3}?", ["2a + 3", "6a + 3", "2a + 9",
                                     "18a + 27"], 0),
             ("Cik ir {10x − 5|5}?", ["2x − 1", "10x − 1", "2x − 5",
                                      "50x − 25"], 0),
             ("Cik ir {8a + 12|4}?", ["2a + 3", "8a + 3", "2a + 12",
                                      "32a + 48"], 0),
             ("Cik ir {15x + 20|5}?", ["3x + 4", "15x + 4", "3x + 20",
                                       "75x + 100"], 0),
             ("Cik ir {12a − 18|6}?", ["2a − 3", "12a − 3", "2a − 18",
                                       "72a − 108"], 0),
             ("Cik ir {14x + 7|7}?", ["2x + 1", "14x + 1", "2x + 7",
                                      "98x + 49"], 0),
             ("Kā dala summu ar skaitli?",
              ["dala katru saskaitāmo", "dala tikai pirmo",
               "dala tikai pēdējo", "reizina saskaitāmos"], 0),
             ("Cik ir {20a + 30|10}?", ["2a + 3", "20a + 3", "2a + 30",
                                        "200a + 300"], 0),
         ]},
        {"sr": "Apraksta situāciju ar izteiksmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Burtnīca maksā x eiro. Cik maksā 7 burtnīcas?",
              ["7x eiro", "x + 7 eiro", "x − 7 eiro", "{x|7} eiro"], 0),
             ("Ievai ir x eiro, Jānim — par 6 eiro vairāk. Cik ir Jānim?",
              ["x + 6", "6x", "x − 6", "{x|6}"], 0),
             ("Cena ir x eiro, tai atlaide 25 %. Kāda ir jaunā cena?",
              ["0,75x", "0,25x", "x − 25", "25x"], 0),
             ("Cena ir x eiro, tā pieaug par 10 %. Kāda ir jaunā cena?",
              ["1,1x", "0,1x", "x + 10", "10x"], 0),
             ("Taisnstūra malas ir x un x + 5. Kāds ir perimetrs?",
              ["4x + 10", "2x + 5", "x² + 5x", "2x + 10"], 0),
             ("Divu skaitļu attiecība ir 3 : 4. Kā pieraksta skaitļus?",
              ["3x un 4x", "x + 3 un x + 4", "3 un 4", "{x|3} un {x|4}"], 0),
             ("Ko nozīmē 0,9x?",
              ["x, samazināts par 10 %", "x, palielināts par 10 %",
               "90 % pieaugums", "x mīnus 0,9"], 0),
             ("Klasē ir x skolēni; trešdaļa ir zēni. Cik ir zēnu?",
              ["{x|3}", "3x", "x − 3", "x + 3"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārveido algebriskas izteiksmes",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Vienkāršo izteiksmi",
             lambda a, b, k, c: [
                 ("%da + %da = ……" % (a, b), "%da" % (a + b)),
                 ("%dx − %dx = ……" % (a + b, b), "%dx" % a),
                 ("%d(a + %d) = ……" % (k, c), "%da + %d" % (k, k * c)),
                 ("%da − (%da + %d) = ……" % (a + b, b, c),
                  "%da − %d" % (a, c))],
             [(3, 7, 2, 5), (5, 4, 3, 6), (2, 9, 4, 3), (6, 8, 5, 2),
              (4, 11, 6, 7), (7, 3, 2, 9), (9, 6, 3, 4), (8, 12, 7, 5),
              (10, 5, 4, 8), (11, 4, 5, 6), (12, 7, 8, 3), (13, 9, 2, 11),
              (14, 6, 9, 4), (15, 8, 3, 7), (16, 3, 10, 5)]),
         },
        {"sr": "Aprēķina izteiksmes vērtību",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Izteiksmes vērtība",
             lambda k, b, x1, x2: [
                 ("%dx + %d,  ja x = %d:   ……" % (k, b, x1),
                  V.sk(k * x1 + b)),
                 ("%dx + %d,  ja x = %d:   ……" % (k, b, x2),
                  V.sk(k * x2 + b)),
                 ("%d(x + %d),  ja x = %d:   ……" % (k, b, x1),
                  V.sk(k * (x1 + b)))],
             [(2, 3, 4, 7), (3, 5, 2, 6), (4, 1, 5, 8), (5, 2, 3, 9),
              (6, 4, 2, 7), (7, 3, 4, 5), (8, 1, 6, 3), (9, 2, 5, 4),
              (10, 5, 3, 8), (11, 4, 2, 6), (12, 3, 4, 7), (13, 2, 5, 3),
              (14, 1, 6, 9), (15, 4, 2, 5), (16, 3, 3, 8)]),
         },
        {"sr": "Apraksta situāciju ar izteiksmi",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situācija un izteiksme",
             lambda cena, n, p: {
                 "teksts": "Burtnīca maksā x eiro, bet grāmata — par "
                           "%d eiro vairāk.   a) Pieraksti grāmatas cenu "
                           "ar izteiksmi!   b) Pieraksti ar izteiksmi, cik "
                           "maksā %d burtnīcas un viena grāmata!   "
                           "c) Vienkāršo šo izteiksmi!   d) Cik jāmaksā, ja "
                           "x = %d?" % (cena, n, p),
                 "kriteriji": [
                     "a) x + %d.   (1 p.)" % cena,
                     "b) %dx + (x + %d).   (1 p.)" % (n, cena),
                     "c) %dx + %d.   (1 p.)" % (n + 1, cena),
                     "d) %d · %d + %d = %d eiro.   (1 p.)"
                     % (n + 1, p, cena, (n + 1) * p + cena)]},
             [(2, 3, 4), (3, 4, 5), (4, 2, 6), (5, 5, 3), (6, 3, 7),
              (7, 4, 2), (8, 6, 5), (9, 2, 8), (10, 5, 4), (11, 3, 9),
              (12, 4, 6), (13, 6, 3), (14, 2, 7), (15, 5, 5), (16, 3, 8)]),
         },
        {"sr": "Pamato izteiksmju vienādību",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Identiski vienādas izteiksmes",
             lambda k, c: {
                 "ievads": "Dotas izteiksmes  %d(x + %d)  un  %dx + %d."
                           % (k, c, k, k * c),
                 "jaut": [("Atver iekavas pirmajā izteiksmē!", 1),
                          ("Vai izteiksmes ir identiski vienādas?", 1),
                          ("Pārbaudi, ievietojot x = 2!", 1)],
                 "atbildes": [
                     "1) %dx + %d.   (1 p.)" % (k, k * c),
                     "2) Jā — pēc iekavu atvēršanas tās sakrīt.   (1 p.)",
                     "3) %d · (2 + %d) = %d  un  %d · 2 + %d = %d.   (1 p.)"
                     % (k, c, k * (2 + c), k, k * c, 2 * k + k * c)]},
             [(2, 3), (3, 4), (4, 2), (5, 6), (6, 1), (7, 5), (8, 3),
              (9, 2), (10, 7), (11, 4), (12, 5), (13, 2), (14, 6),
              (15, 3), (16, 4)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
