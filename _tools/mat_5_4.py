# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.4. Kā vienu skaitli izsaka kā otra skaitļa daļu?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.4. temats): daļas pieraksta
veidi (a pret b; a : b; {a|b}), viena skaitļa izteikšana kā otra skaitļa daļu,
daļas skaitliskās vērtības un veselā aprēķināšana, daļas pārveidošana lieluma
mazākajās mērvienībās un secinājums, ka dalījums ar lielāku skaitli ir mazāks
nekā 1.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.4."
NOSAUKUMS = "Kā vienu skaitli izsaka kā otra skaitļa daļu?"

ATGADNE = [
    "Skaitli a kā skaitļa b daļu pieraksta dažādi:   a pret b   ·   a : b  "
    " ·   {a|b}",
    "Daļas vērtība:   {3|4} no 20 = 20 : 4 · 3 = 15      ·      veselais: "
    "ja {1|5} ir 6, tad veselais ir 6 · 5 = 30",
    "Ja skaitli dala ar lielāku skaitli, dalījums ir mazāks nekā 1; "
    "rezultātu cenšas saīsināt līdz nesaīsināmai daļai.",
]


# ---------------------------------------------------------------- veidnes
def izsaka(a, b):
    """Kādu daļu no b veido a."""
    return ("Kādu daļu no %d veido %d?" % (b, a),
            V.izvele("{%d|%d}" % (a, b), "{%d|%d}" % (b, a),
                     "{%d|%d}" % (a, b - a), "{%d|%d}" % (b - a, b),
                     "{%d|%d}" % (a, b + a), "{%d|%d}" % (a + 1, b)), 0)


def dalijums(a, b):
    """Daļa kā dalījums."""
    return ("Kā daļu {%d|%d} pieraksta kā dalījumu?" % (a, b),
            V.izvele("%d : %d" % (a, b), "%d : %d" % (b, a),
                     "%d · %d" % (a, b), "%d + %d" % (a, b),
                     "%d − %d" % (a, b), "%d : %d" % (a, b + 1)), 0)


def vertiba(a, b, n):
    """Daļas {a|b} vērtība no skaitļa n."""
    return ("Cik ir {%d|%d} no %d?" % (a, b, n),
            V.izvele(n // b * a, n // b, n * b // a, n - a,
                     n // b * a + 1, n * a), 0)


def veselais(a, b, dala):
    """Veselais, ja zināma daļas {a|b} vērtība."""
    return ("{%d|%d} no skaitļa ir %d. Kāds ir skaitlis?" % (a, b, dala),
            V.izvele(dala // a * b, dala * a, dala + b, dala // a,
                     dala * b, dala // a * b + 1), 0)


def saisina(a, b, k):
    """Daļas saīsināšana."""
    return ("Saīsini daļu {%d|%d}!" % (a * k, b * k),
            V.izvele(V.dalu(a, b), "{%d|%d}" % (b, a),
                     "{%d|%d}" % (a * k, b), "{%d|%d}" % (a, b * k),
                     "{%d|%d}" % (a + 1, b), "{%d|%d}" % (a, b + 1)), 0)


def mervienibas(a, b, viss, liela, maza):
    """Daļa no lieluma mazākās mērvienībās."""
    return ("Cik %s ir {%d|%d} %s?" % (maza, a, b, liela),
            V.izvele("%s %s" % (V.sk(viss // b * a), maza),
                     "%s %s" % (V.sk(viss // b), maza),
                     "%s %s" % (V.sk(viss // a * b), maza),
                     "%s %s" % (V.sk(viss - a), maza),
                     "%s %s" % (V.sk(viss // b * a + 10), maza),
                     "%s %s" % (V.sk(viss), maza)), 0)


def izteiksme(a, b, n):
    """Ar kuru izteiksmi aprēķina daļu no skaitļa."""
    return ("Ar kuru izteiksmi aprēķina {%d|%d} no %d?" % (a, b, n),
            V.izvele("%d : %d · %d" % (n, b, a), "%d · %d : %d" % (n, b, a),
                     "%d : %d · %d" % (n, a, b), "%d + %d · %d" % (n, b, a),
                     "%d · %d · %d" % (n, a, b),
                     "%d : %d : %d" % (n, a, b)), 0)


FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.4. temata beigās. Pārbauda daļas "
                "pieraksta veidus, viena skaitļa izteikšanu kā otra daļu, "
                "daļas vērtības un veselā aprēķināšanu, daļu no "
                "mērvienībām un rezultāta saīsināšanu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina daļas pieraksta veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā pieraksta, ka 3 ir skaitļa 4 daļa?",
              ["{3|4}", "{4|3}", "3 − 4", "3 · 4"], 0),
             ("Kuri pieraksti nozīmē vienu un to pašu?",
              ["3 pret 4,  3 : 4  un  {3|4}", "3 + 4 un {3|4}",
               "3 · 4 un {4|3}", "3 − 4 un {3|4}"], 0),
             ("Kā daļu var pierakstīt citādi?",
              ["kā dalījumu", "kā summu", "kā starpību", "kā pakāpi"], 0),
             ("Kā vārdiem izlasa pierakstu 5 : 8?",
              ["5 pret 8", "5 un 8", "5 mīnus 8", "5 reiz 8"], 0),
             ("Kas ir daļas skaitītājs?",
              ["skaitlis virs daļsvītras", "skaitlis zem daļsvītras",
               "vesela daļa", "dalījums"], 0),
             ("Kas ir daļas saucējs?",
              ["skaitlis zem daļsvītras", "skaitlis virs daļsvītras",
               "vesela daļa", "reizinājums"], 0),
             ("Ko rāda saucējs?",
              ["cik vienādās daļās sadalīts veselais",
               "cik daļas paņemtas", "cik ir veselais", "cik ir summa"], 0),
             ("Ko rāda skaitītājs?",
              ["cik daļas paņemtas", "cik vienādās daļās sadalīts veselais",
               "cik ir veselais", "cik ir starpība"], 0),
         ]},
        {"sr": "Izsaka vienu skaitli kā otra skaitļa daļu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(izsaka, [
             (5, 20), (3, 12), (6, 30), (4, 16), (7, 21), (8, 40),
             (9, 27), (10, 25), (12, 36), (15, 45), (6, 18), (14, 42),
             (11, 33), (16, 48), (18, 54)]),
         },
        {"sr": "Saista daļu ar dalījumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dalijums, [
             (3, 4), (5, 8), (7, 10), (2, 9), (4, 7), (6, 11), (9, 13),
             (1, 6), (8, 15), (5, 12), (3, 14), (7, 16), (11, 20),
             (2, 17), (13, 25)]),
         },
        {"sr": "Aprēķina daļas vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vertiba, [
             (3, 4, 20), (2, 5, 45), (3, 5, 40), (2, 3, 36), (5, 6, 42),
             (3, 8, 64), (4, 7, 49), (5, 9, 27), (7, 10, 50), (2, 7, 63),
             (3, 10, 80), (5, 8, 32), (4, 9, 54), (7, 12, 48),
             (5, 11, 44)]),
         },
        {"sr": "Nosaka veselo",
         "stunda": TEMATS,
         "jautajumi": V.kopa(veselais, [
             (1, 6, 4), (3, 4, 18), (2, 3, 10), (1, 5, 7), (2, 5, 14),
             (3, 7, 12), (1, 4, 9), (4, 5, 16), (2, 9, 8), (5, 6, 25),
             (1, 8, 6), (3, 10, 15), (2, 11, 10), (4, 7, 20),
             (5, 12, 30)]),
         },
        {"sr": "Pieraksta aprēķinu kā divu darbību izteiksmi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(izteiksme, [
             (3, 5, 40), (2, 3, 24), (4, 5, 35), (3, 4, 28), (5, 6, 54),
             (2, 7, 42), (3, 8, 56), (4, 9, 45), (5, 7, 63), (2, 5, 30),
             (7, 10, 60), (3, 11, 44), (4, 13, 39), (5, 9, 36),
             (6, 7, 49)]),
         },
        {"sr": "Pārveido daļu mazākās mērvienībās",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mervienibas, [
             (3, 4, 1000, "kg", "gramu"), (4, 5, 1000, "km", "metru"),
             (2, 3, 60, "stundas", "minūšu"), (1, 2, 1000, "kg", "gramu"),
             (3, 5, 1000, "km", "metru"), (1, 4, 60, "stundas", "minūšu"),
             (1, 4, 1000, "kg", "gramu"), (7, 10, 1000, "km", "metru"),
             (5, 6, 60, "stundas", "minūšu"), (2, 5, 1000, "kg", "gramu"),
             (9, 10, 1000, "km", "metru"), (1, 3, 60, "stundas", "minūšu"),
             (3, 8, 1000, "kg", "gramu"), (1, 5, 1000, "km", "metru"),
             (3, 4, 60, "stundas", "minūšu")]),
         },
        {"sr": "Saīsina rezultātu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saisina, [
             (1, 5, 6), (1, 3, 8), (2, 5, 5), (1, 4, 10), (3, 5, 4),
             (2, 3, 9), (1, 2, 12), (3, 4, 7), (2, 7, 6), (4, 5, 3),
             (1, 6, 11), (5, 7, 2), (3, 8, 5), (2, 9, 4), (5, 6, 8)]),
         },
        {"sr": "Spriež par dalījumu, kas mazāks nekā 1",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir dalījums, ja skaitli dala ar lielāku skaitli?",
              ["mazāks nekā 1", "lielāks nekā 1", "vienāds ar 1",
               "vienāds ar 0"], 0),
             ("Vai {3|7} ir lielāka nekā 1?",
              ["nē", "jā", "vienāda ar 1", "nevar noteikt"], 0),
             ("Kura daļa ir lielāka nekā 1?",
              ["{9|4}", "{3|4}", "{4|9}", "{1|4}"], 0),
             ("Kura daļa ir mazāka nekā 1?",
              ["{2|7}", "{7|2}", "{9|5}", "{8|3}"], 0),
             ("Kad daļa ir vienāda ar 1?",
              ["kad skaitītājs un saucējs ir vienādi",
               "kad skaitītājs ir 1", "kad saucējs ir 1", "nekad"], 0),
             ("Kā sauc daļu, kuras skaitītājs ir mazāks nekā saucējs?",
              ["īsta daļa", "neīsta daļa", "jaukts skaitlis",
               "vesels skaitlis"], 0),
             ("Kā sauc daļu, kuras skaitītājs ir lielāks nekā saucējs?",
              ["neīsta daļa", "īsta daļa", "jaukts skaitlis",
               "pamatdaļa"], 0),
             ("Kura daļa ir vislielākā?",
              ["{5|4}", "{3|4}", "{1|4}", "{2|4}"], 0),
         ]},
        {"sr": "Salīdzina daļas dažādos veselos",
         "stunda": TEMATS,
         "jautajumi": [
             ("No 20 skolēniem šahu spēlē 5, no 30 — 6. Kur daļa ir "
              "lielāka?", ["pirmajā grupā", "otrajā grupā", "vienāda",
                           "nevar salīdzināt"], 0),
             ("No 12 ābolu 3 ir sarkani, no 20 — 4. Kur daļa lielāka?",
              ["pirmajā grozā", "otrajā grozā", "vienāda",
               "nevar salīdzināt"], 0),
             ("No 25 burtnīcām 5 ir rūtiņu, no 30 — 6. Kur daļa lielāka?",
              ["abās vienāda", "pirmajā", "otrajā", "nevar salīdzināt"], 0),
             ("Kāpēc daļas saīsina, lai tās salīdzinātu?",
              ["lai varētu salīdzināt dažādus veselos",
               "lai skaitļi būtu lielāki", "lai būtu ātrāk",
               "tas nav vajadzīgs"], 0),
             ("Saīsini {6|30}.", ["{1|5}", "{5|1}", "{6|5}", "{1|6}"], 0),
             ("Saīsini {8|24}.", ["{1|3}", "{3|1}", "{8|3}", "{1|8}"], 0),
             ("Saīsini {10|25}.", ["{2|5}", "{5|2}", "{10|5}", "{1|5}"], 0),
             ("Kura daļa ir lielāka: {1|4} vai {1|5}?",
              ["{1|4}", "{1|5}", "tās ir vienādas", "nevar salīdzināt"], 0),
         ]},
        {"sr": "Modelē situāciju ar daļu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Klasē ir 25 skolēni, 10 brauc ar autobusu. Kādu daļu tie "
              "veido?", ["{10|25}", "{25|10}", "{10|15}", "{15|25}"], 0),
             ("Kas šajā uzdevumā ir veselais?",
              ["25 skolēni", "10 skolēnu", "15 skolēnu", "1 skolēns"], 0),
             ("Grāmatā ir 120 lappuses; izlasītas 30. Kāda daļa izlasīta?",
              ["{1|4}", "{1|3}", "{3|4}", "{1|12}"], 0),
             ("Cik lappušu ir {2|3} no 120?", ["80", "40", "180", "60"], 0),
             ("{1|4} no ceļa ir 12 km. Cik garš ir viss ceļš?",
              ["48 km", "3 km", "16 km", "36 km"], 0),
             ("Skolā 240 skolēni; 60 dzied korī. Kādu daļu tie veido?",
              ["{1|4}", "{1|3}", "{1|6}", "{3|4}"], 0),
             ("Somā 15 burtnīcas, 5 ir rūtiņu. Kādu daļu tās veido?",
              ["{1|3}", "{1|5}", "{2|3}", "{3|1}"], 0),
             ("Kas jāzina, lai izteiktu skaitli kā otra daļu?",
              ["abi skaitļi — daļa un veselais", "tikai veselais",
               "tikai daļa", "tikai saucējs"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik ir {3|4} no 60 eiro?", ["45 eiro", "15 eiro", "80 eiro",
                                           "20 eiro"], 0),
             ("Cik ir {2|5} no 100 m?", ["40 m", "20 m", "250 m",
                                         "60 m"], 0),
             ("{1|6} no skaitļa ir 5. Kāds ir skaitlis?",
              ["30", "11", "5", "6"], 0),
             ("{3|5} no skaitļa ir 21. Kāds ir skaitlis?",
              ["35", "26", "63", "7"], 0),
             ("Cik minūtes ir trīs ceturtdaļstundā?",
              ["45", "30", "34", "15"], 0),
             ("Cik gramu ir pusotra kilograma?",
              ["1500 g", "150 g", "1050 g", "500 g"], 0),
             ("Cik centimetru ir {1|2} metra?",
              ["50 cm", "5 cm", "500 cm", "25 cm"], 0),
             ("Cik ir 40 : 5 · 3?", ["24", "8", "120", "15"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.4. temata noslēgumā. "
                "Pārbauda viena skaitļa izteikšanu kā otra daļu, rezultāta "
                "saīsināšanu, daļas vērtības un veselā aprēķināšanu, daļu "
                "no mērvienībām un situāciju uzdevumus.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina daļas pieraksta veidus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dalijums, [
             (7, 9), (5, 8), (4, 5), (3, 11), (6, 13), (2, 15), (8, 17),
             (9, 20), (1, 12), (10, 21), (11, 24), (5, 19), (7, 18),
             (12, 23), (4, 27)]),
         },
        {"sr": "Izsaka vienu skaitli kā otra skaitļa daļu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(izsaka, [
             (8, 40), (6, 24), (9, 36), (5, 35), (7, 28), (12, 60),
             (10, 50), (4, 32), (14, 56), (15, 60), (11, 44), (13, 52),
             (16, 64), (18, 72), (20, 80)]),
         },
        {"sr": "Aprēķina daļas vērtību",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(vertiba, [
             (2, 3, 36), (3, 5, 40), (5, 8, 64), (3, 7, 56), (4, 9, 63),
             (7, 12, 60), (2, 11, 55)])
             + V.kopa(izteiksme, [
                 (3, 5, 40), (2, 3, 24), (4, 5, 35), (3, 4, 28),
                 (5, 6, 54), (2, 7, 42), (3, 8, 56), (4, 9, 45)])),
         },
        {"sr": "Nosaka veselo",
         "stunda": TEMATS,
         "jautajumi": V.kopa(veselais, [
             (1, 5, 7), (2, 3, 10), (3, 4, 15), (1, 7, 8), (2, 5, 12),
             (4, 5, 20), (1, 9, 6), (3, 8, 18), (5, 7, 25), (2, 13, 14),
             (1, 10, 11), (3, 11, 21), (4, 9, 24), (5, 8, 30),
             (6, 7, 36)]),
         },
        {"sr": "Pārveido daļu mazākās mērvienībās",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mervienibas, [
             (1, 2, 1000, "kg", "gramu"), (3, 5, 1000, "km", "metru"),
             (1, 4, 60, "stundas", "minūšu"), (3, 4, 1000, "kg", "gramu"),
             (4, 5, 1000, "km", "metru"), (2, 3, 60, "stundas", "minūšu"),
             (7, 10, 1000, "kg", "gramu"), (1, 5, 1000, "km", "metru"),
             (5, 12, 60, "stundas", "minūšu"),
             (2, 5, 1000, "kg", "gramu"), (9, 10, 1000, "km", "metru"),
             (5, 6, 60, "stundas", "minūšu"), (3, 8, 1000, "kg", "gramu"),
             (1, 4, 1000, "km", "metru"), (1, 3, 60, "stundas", "minūšu")]),
         },
        {"sr": "Spriež par daļas lielumu un risina uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura daļa ir lielāka nekā 1?",
              ["{7|3}", "{3|7}", "{1|3}", "{2|7}"], 0),
             ("Grāmatā 120 lappuses; izlasītas 30. Kāda daļa izlasīta?",
              ["{1|4}", "{1|3}", "{3|4}", "{1|12}"], 0),
             ("{1|4} no ceļa ir 12 km. Cik garš ir viss ceļš?",
              ["48 km", "3 km", "16 km", "36 km"], 0),
             ("Kāds ir dalījums, ja skaitli dala ar lielāku skaitli?",
              ["mazāks nekā 1", "lielāks nekā 1", "vienāds ar 1",
               "vienāds ar 0"], 0),
             ("Kā sauc daļu, kuras skaitītājs ir lielāks nekā saucējs?",
              ["neīsta daļa", "īsta daļa", "jaukts skaitlis",
               "pamatdaļa"], 0),
             ("Kura daļa ir lielāka: {1|3} vai {1|6}?",
              ["{1|3}", "{1|6}", "tās ir vienādas", "nevar salīdzināt"], 0),
             ("Saīsini {12|30}.", ["{2|5}", "{5|2}", "{6|15}", "{1|5}"], 0),
             ("Kāpēc rezultātu cenšas saīsināt?",
              ["lai daļa būtu vienkāršākajā formā", "lai tā būtu lielāka",
               "lai tā būtu mazāka", "tas nav vajadzīgs"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Izsaka daļu, saīsina to un aprēķina vērtību",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, b, c, d, n, dala: [
                 ("Kādu daļu no %d veido %d?   ……" % (b, a),
                  "{%d|%d}" % (a, b)),
                 ("Saīsini to:   ……", V.dalu(a, b)),
                 ("{%d|%d} no %d = ……" % (c, d, n), V.sk(n // d * c)),
                 ("{1|%d} no skaitļa ir %d; skaitlis ir ……" % (d, dala),
                  V.sk(dala * d))],
             [(5, 20, 3, 4, 20, 4), (3, 12, 2, 5, 45, 6), (6, 30, 3, 5, 40, 3),
              (4, 16, 2, 3, 36, 5), (7, 21, 5, 6, 42, 7),
              (8, 40, 3, 8, 64, 2), (9, 27, 4, 7, 49, 8),
              (10, 25, 5, 9, 27, 9), (12, 36, 7, 10, 50, 4),
              (15, 45, 2, 7, 63, 5), (6, 18, 3, 10, 80, 6),
              (14, 42, 5, 8, 32, 3), (11, 33, 4, 9, 54, 7),
              (16, 48, 7, 12, 48, 2), (18, 54, 5, 11, 44, 8)]),
         },
        {"sr": "Pārveido daļu mazākās mērvienībās",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Pārveido mērvienības",
             lambda a, b, c, d, e, f: [
                 ("{%d|%d} kg = …… g" % (a, b), V.sk(1000 // b * a)),
                 ("{%d|%d} km = …… m" % (c, d), V.sk(1000 // d * c)),
                 ("{%d|%d} stundas = …… min" % (e, f), V.sk(60 // f * e))],
             [(3, 4, 4, 5, 2, 3), (1, 2, 3, 5, 1, 4), (1, 4, 7, 10, 5, 6),
              (2, 5, 9, 10, 1, 3), (3, 8, 1, 5, 3, 4), (5, 8, 2, 5, 1, 2),
              (7, 10, 1, 4, 5, 12), (1, 5, 3, 4, 7, 12), (9, 10, 1, 2, 1, 6),
              (3, 5, 4, 25, 11, 12), (1, 8, 3, 8, 2, 5), (7, 8, 7, 20, 3, 5),
              (1, 10, 9, 20, 4, 5), (3, 10, 11, 20, 1, 5),
              (9, 20, 13, 20, 7, 10)]),
         },
        {"sr": "Risina situāciju uzdevumu ar daļām",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda kopa_, dala, b: {
                 "teksts": "Klasē ir %d skolēni; %d no tiem brauc uz skolu "
                           "ar autobusu.   a) Kādu daļu klases viņi "
                           "veido?   b) Saīsini to!   c) Kādu daļu veido "
                           "pārējie?   d) Cik skolēnu ir {1|%d} no klases?"
                           % (kopa_, dala, b),
                 "kriteriji": [
                     "a) {%d|%d}.   (1 p.)" % (dala, kopa_),
                     "b) {%d|%d} = %s.   (1 p.)"
                     % (dala, kopa_, V.dalu(dala, kopa_)),
                     "c) Pārējie veido %s.   (1 p.)"
                     % V.dalu(kopa_ - dala, kopa_),
                     "d) %d : %d = %d skolēni.   (1 p.)"
                     % (kopa_, b, kopa_ // b)]},
             [(25, 10, 5), (30, 12, 6), (24, 8, 4), (20, 5, 4), (36, 12, 6),
              (40, 16, 8), (28, 7, 7), (32, 8, 8), (45, 15, 9),
              (50, 20, 10), (27, 9, 3), (33, 11, 11), (21, 6, 7),
              (48, 12, 12), (60, 24, 10)]),
         },
        {"sr": "Skaidro daļas nozīmi un salīdzina daļas",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Divas grupas",
             lambda a, b, c, d: {
                 "ievads": "Klasē A no %d skolēniem šahu spēlē %d, klasē B "
                           "no %d skolēniem — %d." % (b, a, d, c),
                 "jaut": [("Izsaki abas daļas!", 1), ("Saīsini tās!", 1),
                          ("Kurā klasē šahistu daļa ir lielāka?", 1)],
                 "atbildes": [
                     "1) {%d|%d} un {%d|%d}.   (1 p.)" % (a, b, c, d),
                     "2) %s un %s.   (1 p.)"
                     % (V.dalu(a, b), V.dalu(c, d)),
                     "3) %s.   (1 p.)"
                     % ("Klasē A" if a * d > c * b else
                        ("Klasē B" if a * d < c * b else
                         "Abās vienāda"))]},
             [(5, 20, 6, 30), (4, 12, 6, 24), (3, 15, 4, 16),
              (6, 18, 5, 20), (8, 24, 7, 28), (9, 27, 10, 40),
              (5, 25, 6, 24), (7, 21, 8, 32), (10, 30, 9, 36),
              (4, 16, 5, 25), (6, 30, 7, 35), (8, 32, 9, 27),
              (3, 12, 5, 15), (11, 33, 12, 48), (12, 36, 10, 50)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
