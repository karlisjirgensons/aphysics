# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.3. Kā skaidro un lieto daļas pamatīpašību?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.3. temats): daļas pamatīpašība,
daļas paplašināšana un saīsināšana, nesaīsināma daļa, kopīgs saucējs, daļu
salīdzināšana, saskaitīšana un atņemšana ar dažādiem saucējiem un daļas
dalīšana.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.3."
NOSAUKUMS = "Kā skaidro un lieto daļas pamatīpašību?"

ATGADNE = [
    "Daļas pamatīpašība: skaitītāju un saucēju reizinot vai dalot ar vienu "
    "un to pašu skaitli, daļas lielums nemainās:   {2|3} = {4|6} = {6|9}",
    "Paplašina, reizinot:   {2|3} = {8|12}      ·      saīsina, dalot:   "
    "{6|9} = {2|3}",
    "Lai salīdzinātu, saskaitītu vai atņemtu daļas ar dažādiem saucējiem, "
    "tās vispirms pārveido līdz vienādiem saucējiem.",
]


def lkd(a, b):
    while b:
        a, b = b, a % b
    return a


# ---------------------------------------------------------------- veidnes
def paplasina(a, b, k):
    """Daļas paplašināšana ar reizinātāju k."""
    return ("Paplašini daļu {%d|%d} ar %d!" % (a, b, k),
            V.izvele("{%d|%d}" % (a * k, b * k), "{%d|%d}" % (a, b * k),
                     "{%d|%d}" % (a * k, b), "{%d|%d}" % (a + k, b + k),
                     "{%d|%d}" % (b * k, a * k),
                     "{%d|%d}" % (a * k, b * k + 1)), 0)


def saisina(a, b, k):
    """Daļas saīsināšana; {a·k|b·k} saīsinās līdz {a|b}."""
    return ("Saīsini daļu {%d|%d}!" % (a * k, b * k),
            V.izvele(V.dalu(a, b), "{%d|%d}" % (b, a),
                     "{%d|%d}" % (a * k, b), "{%d|%d}" % (a, b * k),
                     "{%d|%d}" % (a + 1, b), "{%d|%d}" % (a, b + 1)), 0)


def kopigais(a, b):
    """Mazākais kopīgais saucējs."""
    m = a * b // lkd(a, b)
    return ("Kāds ir mazākais kopīgais saucējs daļām ar saucējiem %d un %d?"
            % (a, b),
            V.izvele(m, a * b, a + b, lkd(a, b), m + a, m * 2), 0)


def salidzina(a, b, c, d):
    """Divu daļu salīdzināšana."""
    lielaka = "{%d|%d}" % ((a, b) if a * d > c * b else (c, d))
    mazaka = "{%d|%d}" % ((c, d) if a * d > c * b else (a, b))
    return ("Kura daļa ir lielāka: {%d|%d} vai {%d|%d}?" % (a, b, c, d),
            V.izvele(lielaka, mazaka, "tās ir vienādas",
                     "nevar salīdzināt"), 0)


def saskaita(a, b, c, d):
    """Daļu saskaitīšana ar dažādiem saucējiem."""
    sauc = b * d // lkd(b, d)
    sk = a * (sauc // b) + c * (sauc // d)
    return ("Cik ir {%d|%d} + {%d|%d}?" % (a, b, c, d),
            V.izvele(V.dalu(sk, sauc), "{%d|%d}" % (a + c, b + d),
                     "{%d|%d}" % (a + c, sauc), V.dalu(sk, sauc * 2),
                     "{%d|%d}" % (a * c, b * d),
                     V.dalu(sk + 1, sauc)), 0)


def atnem(a, b, c, d):
    """Daļu atņemšana ar dažādiem saucējiem."""
    sauc = b * d // lkd(b, d)
    sk = a * (sauc // b) - c * (sauc // d)
    return ("Cik ir {%d|%d} − {%d|%d}?" % (a, b, c, d),
            V.izvele(V.dalu(sk, sauc), "{%d|%d}" % (a - c, b - d)
                     if b != d else "{%d|%d}" % (a - c, b + d),
                     "{%d|%d}" % (a - c, sauc), V.dalu(sk, sauc * 2),
                     "{%d|%d}" % (a * c, b * d), V.dalu(sk + 1, sauc)), 0)


def dala_ar_veselu(a, b, n):
    """Daļas dalīšana ar veselu skaitli."""
    return ("Cik ir {%d|%d} : %d?" % (a, b, n),
            V.izvele(V.dalu(a, b * n), V.dalu(a * n, b), V.dalu(a, b + n),
                     V.dalu(a - n, b), V.dalu(b, a * n),
                     V.dalu(a, b * n + 1)), 0)


def veselu_ar_dalu(n, a, b):
    """Vesela skaitļa dalīšana ar daļu."""
    return ("Cik ir %d : {%d|%d}?" % (n, a, b),
            V.izvele(V.dalu(n * b, a), V.dalu(n * a, b), V.dalu(a, n * b),
                     V.dalu(n, a * b), V.dalu(b, n * a),
                     V.dalu(n * b + 1, a)), 0)


FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.3. temata beigās. Pārbauda daļas "
                "pamatīpašību, paplašināšanu un saīsināšanu, kopīgo saucēju, "
                "daļu salīdzināšanu, saskaitīšanu, atņemšanu un dalīšanu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina daļas pamatīpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā skan daļas pamatīpašība?",
              ["skaitītāju un saucēju var reizināt vai dalīt ar vienu "
               "skaitli", "skaitītāju var mainīt brīvi",
               "saucēju var mainīt brīvi", "daļu nedrīkst mainīt"], 0),
             ("Kas notiek ar daļas lielumu, to paplašinot?",
              ["nemainās", "aug", "sarūk", "kļūst 0"], 0),
             ("Kas notiek ar daļas lielumu, to saīsinot?",
              ["nemainās", "aug", "sarūk", "kļūst 0"], 0),
             ("Vai {2|3} un {4|6} ir vienādas daļas?",
              ["jā", "nē", "tikai aptuveni", "nevar noteikt"], 0),
             ("Vai {2|3} un {3|4} ir vienādas daļas?",
              ["nē", "jā", "tikai saīsinot", "nevar noteikt"], 0),
             ("Ar kuru skaitli daļu nedrīkst paplašināt?",
              ["ar 0", "ar 1", "ar 2", "ar 10"], 0),
             ("Kas ir nesaīsināma daļa?",
              ["daļa, kuru vairs nevar saīsināt", "daļa ar lielu saucēju",
               "daļa ar skaitītāju 1", "neīsta daļa"], 0),
             ("Kāpēc daļas saīsina?",
              ["lai tās būtu vienkāršākajā formā", "lai tās augtu",
               "lai tās sarūktu", "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Paplašina daļu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(paplasina, [
             (2, 3, 4), (1, 2, 5), (3, 5, 2), (2, 7, 3), (4, 9, 2),
             (5, 6, 3), (1, 4, 6), (3, 8, 4), (2, 11, 5), (7, 10, 2),
             (5, 12, 3), (4, 15, 2), (3, 7, 5), (6, 13, 2), (8, 9, 3)]),
         },
        {"sr": "Saīsina daļu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saisina, [
             (1, 3, 4), (2, 5, 3), (3, 4, 5), (1, 2, 7), (4, 7, 2),
             (2, 3, 6), (5, 8, 3), (3, 10, 4), (1, 5, 9), (7, 9, 2),
             (2, 9, 5), (4, 11, 3), (5, 6, 4), (3, 13, 2), (6, 7, 5)]),
         },
        {"sr": "Atpazīst nesaīsināmu daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir nesaīsināma?", ["{3|5}", "{4|6}", "{6|9}",
                                            "{8|12}"], 0),
             ("Kurai daļai vairs nav kopīga dalītāja?",
              ["{5|7}", "{6|8}", "{9|12}", "{10|15}"], 0),
             ("Kura no daļām jau ir vienkāršākajā formā?",
              ["{7|9}", "{6|10}", "{8|14}", "{12|18}"], 0),
             ("Kura daļa ir saīsināma?", ["{6|8}", "{3|7}", "{5|9}",
                                          "{7|11}"], 0),
             ("Kurai daļai ir kopīgs dalītājs?",
              ["{10|25}", "{4|9}", "{7|8}", "{11|13}"], 0),
             ("Kā pārbauda, vai daļu var saīsināt?",
              ["meklē kopīgu dalītāju", "salīdzina ar 1",
               "saskaita skaitītāju un saucēju", "reizina tos"], 0),
             ("Saīsini {12|18}.", ["{2|3}", "{3|2}", "{6|9}", "{1|3}"], 0),
             ("Saīsini {20|30}.", ["{2|3}", "{3|2}", "{10|15}",
                                   "{1|3}"], 0),
         ]},
        {"sr": "Atrod kopīgo saucēju",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kopigais, [
             (2, 3), (3, 4), (4, 6), (5, 10), (6, 8), (3, 5), (8, 12),
             (9, 12), (10, 15), (4, 5), (6, 9), (7, 14), (5, 6), (8, 10),
             (12, 18)]),
         },
        {"sr": "Salīdzina daļas ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(salidzina, [
             (1, 2, 1, 3), (2, 3, 3, 4), (3, 5, 1, 2), (4, 7, 2, 3),
             (5, 6, 7, 9), (1, 4, 2, 9), (3, 8, 2, 5), (5, 12, 1, 3),
             (7, 10, 2, 3), (4, 9, 3, 7), (5, 8, 7, 12), (2, 7, 3, 10),
             (9, 10, 8, 9), (1, 6, 2, 11), (11, 12, 7, 8)]),
         },
        {"sr": "Saskaita daļas ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saskaita, [
             (1, 2, 1, 3), (1, 4, 1, 6), (2, 3, 1, 6), (1, 5, 3, 10),
             (3, 4, 1, 8), (2, 5, 3, 10), (1, 3, 1, 4), (5, 6, 1, 12),
             (1, 2, 1, 5), (2, 7, 3, 14), (1, 6, 1, 9), (3, 8, 1, 4),
             (2, 9, 1, 3), (4, 5, 1, 10), (1, 8, 5, 12)]),
         },
        {"sr": "Atņem daļas ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem, [
             (1, 2, 1, 3), (3, 4, 1, 6), (2, 3, 1, 6), (4, 5, 3, 10),
             (7, 8, 1, 4), (3, 5, 3, 10), (1, 2, 1, 5), (5, 6, 1, 12),
             (2, 3, 1, 4), (5, 7, 3, 14), (5, 6, 1, 9), (3, 4, 1, 8),
             (2, 3, 1, 9), (4, 5, 1, 10), (7, 12, 1, 8)]),
         },
        {"sr": "Dala daļu ar veselu skaitli",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dala_ar_veselu, [
             (1, 2, 3), (2, 3, 4), (3, 5, 2), (4, 7, 3), (5, 6, 5),
             (1, 4, 2), (3, 8, 3), (2, 9, 4), (5, 12, 5), (7, 10, 7),
             (4, 9, 2), (5, 8, 5), (3, 7, 3), (6, 11, 2), (8, 15, 4)]),
         },
        {"sr": "Dala veselu skaitli ar daļu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(veselu_ar_dalu, [
             (2, 1, 3), (3, 1, 2), (4, 1, 5), (6, 2, 3), (5, 1, 4),
             (8, 2, 5), (10, 1, 2), (9, 3, 4), (12, 3, 5), (7, 1, 3),
             (15, 5, 6), (14, 2, 7), (20, 4, 5), (18, 3, 8), (16, 2, 9)]),
         },
        {"sr": "Atpazīst vienādas daļas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir vienāda ar {1|2}?", ["{3|6}", "{2|5}", "{3|5}",
                                                 "{1|3}"], 0),
             ("Kura daļa ir vienāda ar {2|3}?", ["{8|12}", "{3|4}",
                                                 "{2|6}", "{4|5}"], 0),
             ("Kura daļa ir vienāda ar {3|4}?", ["{9|12}", "{4|3}",
                                                 "{3|8}", "{6|9}"], 0),
             ("Kura daļa ir vienāda ar {1|5}?", ["{4|20}", "{5|1}",
                                                 "{2|5}", "{1|10}"], 0),
             ("Kura daļa nav vienāda ar {2|5}?", ["{5|2}", "{4|10}",
                                                  "{6|15}", "{8|20}"], 0),
             ("Kā pārbauda, vai divas daļas ir vienādas?",
              ["saīsina abas līdz nesaīsināmām", "salīdzina skaitītājus",
               "salīdzina saucējus", "saskaita tās"], 0),
             ("Cik daļu ir vienādas ar {1|2}?",
              ["bezgalīgi daudz", "viena", "divas", "neviena"], 0),
             ("Ar ko vienāda daļa {5|5}?", ["1", "0", "5", "{1|5}"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ievai ir {1|2} torte, Jānim — {1|4}. Cik kopā?",
              ["{3|4}", "{2|6}", "{1|6}", "{1|8}"], 0),
             ("No {3|4} m auduma nogrieza {1|4} m. Cik palika?",
              ["{1|2} m", "{2|8} m", "1 m", "{3|16} m"], 0),
             ("Divas lentes: {2|3} m un {1|6} m. Cik kopā?",
              ["{5|6} m", "{3|9} m", "{1|2} m", "{2|18} m"], 0),
             ("{5|6} l sulas sadala 5 glāzēs. Cik katrā?",
              ["{1|6} l", "{5|30} l", "{25|6} l", "{6|5} l"], 0),
             ("Cik {1|4} l glāzes var piepildīt no 3 l?",
              ["12", "3", "{3|4}", "7"], 0),
             ("Uzdevumam veltīja {1|3} h un vēl {1|6} h. Cik kopā?",
              ["{1|2} h", "{2|9} h", "{1|9} h", "{1|18} h"], 0),
             ("Grāmatas {2|5} izlasītas. Kāda daļa palikusi?",
              ["{3|5}", "{2|5}", "{5|2}", "{1|5}"], 0),
             ("{3|8} kūkas apēda, {1|4} atdeva. Cik palika?",
              ["{3|8}", "{1|8}", "{5|8}", "{2|12}"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.3. temata noslēgumā. "
                "Pārbauda daļas pamatīpašību, paplašināšanu un saīsināšanu, "
                "salīdzināšanu, saskaitīšanu, atņemšanu un dalīšanu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina daļas pamatīpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā skan daļas pamatīpašība?",
              ["skaitītāju un saucēju var reizināt vai dalīt ar vienu "
               "skaitli", "skaitītāju var mainīt brīvi",
               "saucēju var mainīt brīvi", "daļu nedrīkst mainīt"], 0),
             ("Kas notiek ar daļas lielumu, to paplašinot?",
              ["nemainās", "aug", "sarūk", "kļūst 0"], 0),
             ("Vai {2|3} un {4|6} ir vienādas daļas?",
              ["jā", "nē", "tikai aptuveni", "nevar noteikt"], 0),
             ("Ar kuru skaitli daļu nedrīkst paplašināt?",
              ["ar 0", "ar 1", "ar 2", "ar 10"], 0),
             ("Kas ir nesaīsināma daļa?",
              ["daļa, kuru vairs nevar saīsināt", "daļa ar lielu saucēju",
               "daļa ar skaitītāju 1", "neīsta daļa"], 0),
             ("Kura daļa ir nesaīsināma?", ["{3|5}", "{4|6}", "{6|9}",
                                            "{8|12}"], 0),
             ("Ar ko vienāda daļa {5|5}?", ["1", "0", "5", "{1|5}"], 0),
             ("Cik daļu ir vienādas ar {1|2}?",
              ["bezgalīgi daudz", "viena", "divas", "neviena"], 0),
         ]},
        {"sr": "Paplašina un saīsina daļu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(paplasina, [
             (3, 4, 3), (2, 5, 4), (1, 3, 7), (4, 7, 3), (5, 9, 2),
             (2, 9, 4), (7, 8, 3)])
             + V.kopa(saisina, [
                 (2, 7, 4), (3, 8, 3), (1, 4, 8), (5, 9, 3), (4, 5, 6),
                 (3, 11, 4), (2, 13, 3), (7, 10, 2)])),
         },
        {"sr": "Salīdzina daļas ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(salidzina, [
             (1, 3, 1, 4), (3, 4, 2, 3), (2, 5, 1, 2), (5, 7, 2, 3),
             (3, 6, 5, 9), (1, 5, 2, 11), (5, 8, 3, 5)])
             + V.kopa(kopigais, [
                 (2, 5), (3, 7), (4, 9), (6, 10), (8, 14), (9, 15),
                 (10, 12), (5, 12)])),
         },
        {"sr": "Saskaita daļas ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saskaita, [
             (1, 3, 1, 6), (1, 2, 1, 4), (2, 5, 1, 10), (3, 4, 1, 12),
             (1, 6, 1, 3), (2, 7, 1, 2), (5, 8, 1, 6), (1, 9, 2, 3),
             (3, 10, 1, 5), (1, 4, 2, 5), (4, 7, 1, 3), (5, 9, 1, 6),
             (1, 12, 3, 4), (2, 11, 1, 2), (7, 15, 1, 5)]),
         },
        {"sr": "Atņem daļas ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem, [
             (2, 3, 1, 6), (3, 4, 1, 2), (4, 5, 1, 10), (11, 12, 3, 4),
             (5, 6, 1, 3), (6, 7, 1, 2), (7, 8, 1, 6), (8, 9, 1, 3),
             (9, 10, 1, 5), (3, 4, 2, 5), (5, 7, 1, 3), (7, 9, 1, 6),
             (11, 12, 1, 4), (9, 11, 1, 2), (13, 15, 1, 5)]),
         },
        {"sr": "Dala daļas",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(dala_ar_veselu, [
             (1, 3, 2), (2, 5, 3), (3, 4, 5), (4, 9, 2), (5, 7, 4)])
             + V.kopa(veselu_ar_dalu, [
                 (2, 1, 5), (3, 1, 4), (5, 1, 3), (6, 1, 2), (4, 2, 3),
                 (8, 3, 4), (9, 1, 6), (12, 2, 5), (10, 3, 7),
                 (15, 4, 9)])),
         },
    ],
    "uzdevumi": [
        {"sr": "Saīsina, paplašina, saskaita un atņem daļas",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, b, k, c, d: [
                 ("Paplašini {%d|%d} ar %d:   ……" % (a, b, k),
                  "{%d|%d}" % (a * k, b * k)),
                 ("Saīsini {%d|%d}:   ……" % (a * k, b * k), V.dalu(a, b)),
                 ("{%d|%d} + {%d|%d} = ……" % (a, b, c, d),
                  V.dalu(a * (b * d // lkd(b, d) // b)
                         + c * (b * d // lkd(b, d) // d),
                         b * d // lkd(b, d))),
                 ("{%d|%d} − {%d|%d} = ……" % (c, d, a, b),
                  V.dalu(c * (b * d // lkd(b, d) // d)
                         - a * (b * d // lkd(b, d) // b),
                         b * d // lkd(b, d)))],
             [(1, 3, 4, 1, 2), (1, 4, 3, 2, 3), (1, 6, 2, 3, 4),
              (2, 5, 3, 7, 10), (1, 8, 4, 3, 4), (3, 10, 2, 4, 5),
              (1, 5, 6, 1, 2), (2, 9, 3, 2, 3), (1, 12, 2, 5, 6),
              (3, 8, 2, 7, 8), (1, 10, 3, 3, 5), (2, 7, 4, 5, 7),
              (1, 9, 5, 2, 3), (3, 14, 2, 5, 7), (1, 15, 3, 4, 5)]),
         },
        {"sr": "Salīdzina daļas",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Salīdzini daļas",
             lambda a, b, c, d: [
                 ("Kopīgais saucējs daļām {%d|%d} un {%d|%d}:   ……"
                  % (a, b, c, d), V.sk(b * d // lkd(b, d))),
                 ("Lielākā no daļām {%d|%d} un {%d|%d}:   ……"
                  % (a, b, c, d),
                  "{%d|%d}" % ((a, b) if a * d > c * b else (c, d))),
                 ("Daļa {%d|%d} nesaīsināmā veidā:   ……" % (a * 2, b * 2),
                  V.dalu(a, b))],
             [(1, 2, 1, 3), (2, 3, 3, 4), (3, 5, 1, 2), (4, 7, 2, 3),
              (5, 6, 7, 9), (1, 4, 2, 9), (3, 8, 2, 5), (5, 12, 1, 3),
              (7, 10, 2, 3), (4, 9, 3, 7), (5, 8, 7, 12), (2, 7, 3, 10),
              (9, 10, 8, 9), (1, 6, 2, 11), (11, 12, 7, 8)]),
         },
        {"sr": "Risina situāciju uzdevumu ar daļām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda a, b, c, d: {
                 "teksts": "Pirmajā dienā izlasīja {%d|%d} grāmatas, otrajā "
                           "— {%d|%d}.   a) Cik liela daļa izlasīta abās "
                           "dienās?   b) Kāda daļa palikusi?   c) Par cik "
                           "otrajā dienā izlasīts vairāk vai mazāk nekā "
                           "pirmajā?   d) Kura diena bija ražīgāka?"
                           % (a, b, c, d),
                 "kriteriji": [
                     "a) {%d|%d} + {%d|%d} = %s.   (1 p.)"
                     % (a, b, c, d,
                        V.dalu(a * (b * d // lkd(b, d) // b)
                               + c * (b * d // lkd(b, d) // d),
                               b * d // lkd(b, d))),
                     "b) 1 − %s = %s.   (1 p.)"
                     % (V.dalu(a * (b * d // lkd(b, d) // b)
                               + c * (b * d // lkd(b, d) // d),
                               b * d // lkd(b, d)),
                        V.dalu(b * d // lkd(b, d)
                               - a * (b * d // lkd(b, d) // b)
                               - c * (b * d // lkd(b, d) // d),
                               b * d // lkd(b, d))),
                     "c) Starpība %s.   (1 p.)"
                     % V.dalu(abs(a * (b * d // lkd(b, d) // b)
                                  - c * (b * d // lkd(b, d) // d)),
                              b * d // lkd(b, d)),
                     "d) %s diena.   (1 p.)"
                     % ("Pirmā" if a * d > c * b else "Otrā")]},
             [(1, 3, 1, 6), (1, 2, 1, 4), (2, 5, 1, 10), (1, 4, 1, 12),
              (1, 6, 1, 3), (2, 7, 1, 2), (1, 8, 1, 6), (1, 9, 2, 3),
              (3, 10, 1, 5), (1, 4, 2, 5), (1, 7, 1, 3), (5, 9, 1, 6),
              (1, 12, 1, 4), (2, 11, 1, 2), (7, 15, 1, 5)]),
         },
        {"sr": "Skaidro daļas pamatīpašības lietojumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Daļas pamatīpašība",
             lambda a, b, k: {
                 "ievads": "Dota daļa  {%d|%d}." % (a * k, b * k),
                 "jaut": [("Saīsini to!", 1),
                          ("Paplašini nesaīsināmo daļu ar 3!", 1),
                          ("Paskaidro, kāpēc daļas lielums nemainās!", 1)],
                 "atbildes": [
                     "1) %s.   (1 p.)" % V.dalu(a, b),
                     "2) {%d|%d}.   (1 p.)" % (a * 3, b * 3),
                     "3) Skaitītāju un saucēju reizina vai dala ar vienu un "
                     "to pašu skaitli.   (1 p.)"]},
             [(1, 3, 4), (2, 5, 3), (3, 4, 5), (1, 2, 7), (4, 7, 2),
              (2, 3, 6), (5, 8, 3), (3, 10, 4), (1, 5, 9), (7, 9, 2),
              (2, 9, 5), (4, 11, 3), (5, 6, 4), (3, 13, 2), (6, 7, 5)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
