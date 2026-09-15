# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.3. Kā rīkojas, ja skaitli nevar pierakstīt kā daļu?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.3. temats): racionāls un
iracionāls skaitlis, galīga un bezgalīga periodiska decimāldaļa, noapaļošana
un mērījuma kļūda, skaitlis π, aritmētiskā kvadrātsakne un tās īpašības,
reizinātāja iznešana pirms saknes un ienešana zem saknes un līdzīgas
kvadrātsaknes.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.3."
NOSAUKUMS = "Kā rīkojas, ja skaitli nevar pierakstīt kā daļu?"

ATGADNE = [
    "√a ir tas nenegatīvais skaitlis, kura kvadrāts ir a:   √25 = 5   ·   "
    "(√a)² = a   ·   √(a²) = a,  ja a ≥ 0",
    "Saknes īpašības:   √(a · b) = √a · √b   ·   √({a|b}) = {√a|√b}   ·   "
    "reizinātāju iznes:   √12 = √(4 · 3) = 2√3",
    "Racionāls skaitlis ir katrs, ko var pierakstīt kā {m|n}; iracionāls — "
    "tāds, ko nevar (piemēram, √2 un π). Līdzīgas kvadrātsaknes savelk kā "
    "līdzīgus saskaitāmos:   3√2 + 5√2 = 8√2",
]


# ---------------------------------------------------------------- veidnes
def sakne(a):
    """Precīza kvadrātsakne no pilna kvadrāta."""
    n = int(round(a ** 0.5))
    return ("Cik ir √%d?" % a,
            V.izvele(n, a // 2, n + 1, n * 2, a, n - 1), 0)


def kvadrats(n):
    """Kvadrāta vērtība - saknes pretējā darbība."""
    return ("Cik ir (√%d)²?" % n,
            V.izvele(n, int(round(n ** 0.5)) if n > 0 else 0, n * n,
                     n + 1, n * 2, n - 1), 0)


def iznes(k, r):
    """Reizinātāja iznešana pirms saknes:  √(k²·r) = k√r."""
    a = k * k * r
    return ("Iznes reizinātāju pirms saknes:  √%d." % a,
            V.izvele("%d√%d" % (k, r), "%d√%d" % (r, k),
                     "%d√%d" % (k * r, r), "√%d" % (k * r),
                     "%d√%d" % (k, r * r), "%d√%d" % (k + 1, r)), 0)


def ienes(k, r):
    """Reizinātāja ienešana zem saknes:  k√r = √(k²·r)."""
    return ("Ienes reizinātāju zem saknes:  %d√%d." % (k, r),
            V.izvele("√%d" % (k * k * r), "√%d" % (k * r),
                     "√%d" % (k * r * r), "√%d" % (k + r),
                     "√%d" % (k * k + r), "√%d" % (k * k * r + 1)), 0)


def reizina(a, b):
    """Sakņu reizinājums:  √a · √b = √(a·b)."""
    rez = int(round((a * b) ** 0.5))
    return ("Cik ir √%d · √%d?" % (a, b),
            V.izvele(rez, a * b, a + b, rez + 1, rez * 2,
                     abs(a - b)), 0)


def lidzigas(m, n, r):
    """Līdzīgu kvadrātsakņu savilkšana:  m√r + n√r = (m+n)√r."""
    return ("Savelc:  %d√%d + %d√%d." % (m, r, n, r),
            V.izvele("%d√%d" % (m + n, r), "%d√%d" % (m * n, r),
                     "%d√%d" % (m + n, 2 * r), "%d√%d" % (m + n, r * r),
                     "√%d" % (m + n), "%d√%d" % (m + n + 1, r)), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.3. temata beigās. Pārbauda racionālus "
                "un iracionālus skaitļus, noapaļošanu, aritmētisko "
                "kvadrātsakni un tās īpašības, reizinātāja iznešanu un "
                "ienešanu un līdzīgas kvadrātsaknes.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Atšķir racionālus un iracionālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir racionāls skaitlis?",
              ["skaitlis, ko var pierakstīt kā {m|n}",
               "tikai vesels skaitlis", "tikai decimāldaļa",
               "tikai pozitīvs skaitlis"], 0),
             ("Kas ir iracionāls skaitlis?",
              ["skaitlis, ko nevar pierakstīt kā daļu",
               "negatīvs skaitlis", "ļoti liels skaitlis",
               "skaitlis ar komatu"], 0),
             ("Kurš skaitlis ir iracionāls?", ["√2", "0,5", "{3|4}",
                                               "−7"], 0),
             ("Kurš skaitlis ir racionāls?", ["0,25", "√3", "√5", "π"], 0),
             ("Vai π ir racionāls skaitlis?",
              ["nē", "jā", "tikai noapaļots", "nevar noteikt"], 0),
             ("Vai √9 ir iracionāls skaitlis?",
              ["nē, tas ir 3", "jā", "tikai aptuveni", "nevar noteikt"], 0),
             ("Kāda decimāldaļa iznāk, pārveidojot parasto daļu?",
              ["galīga vai bezgalīga periodiska", "vienmēr galīga",
               "vienmēr bezgalīga", "vienmēr neperiodiska"], 0),
             ("Kāda ir iracionāla skaitļa decimāldaļa?",
              ["bezgalīga un neperiodiska", "galīga",
               "bezgalīga periodiska", "vienmēr nulle"], 0),
         ]},
        {"sr": "Zina aritmētiskās kvadrātsaknes jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir √a?",
              ["nenegatīvs skaitlis, kura kvadrāts ir a",
               "skaitlis, kas reizināts ar 2 dod a", "skaitļa a puse",
               "skaitlis a, dalīts ar 2"], 0),
             ("Cik ir (√12)²?", ["12", "√12", "144", "24"], 0),
             ("Cik ir √(5²)?", ["5", "25", "√5", "10"], 0),
             ("Vai √a var būt negatīvs?",
              ["nē", "jā", "tikai ja a < 0", "vienmēr"], 0),
             ("Kādam a nav definēta √a?", ["a < 0", "a > 0", "a = 0",
                                           "a = 1"], 0),
             ("Cik ir √0?", ["0", "1", "nav definēta", "−1"], 0),
             ("Cik ir √1?", ["1", "0", "−1", "2"], 0),
             ("Starp kuriem veseliem skaitļiem atrodas √10?",
              ["starp 3 un 4", "starp 2 un 3", "starp 4 un 5",
               "starp 9 un 11"], 0),
         ]},
        {"sr": "Aprēķina precīzu kvadrātsakni",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sakne, [
             4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196,
             225, 400]),
         },
        {"sr": "Lieto saknes un kvadrāta saistību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kvadrats, [
             3, 5, 7, 11, 13, 2, 6, 10, 15, 17, 19, 23, 29, 31, 37]),
         },
        {"sr": "Reizina kvadrātsaknes",
         "stunda": TEMATS,
         "jautajumi": V.kopa(reizina, [
             (2, 8), (3, 12), (5, 20), (2, 18), (6, 24), (3, 27),
             (7, 28), (2, 32), (5, 45), (8, 50), (2, 50), (3, 48),
             (10, 40), (6, 54), (11, 44)]),
         },
        {"sr": "Iznes reizinātāju pirms saknes",
         "stunda": TEMATS,
         "jautajumi": V.kopa(iznes, [
             (2, 3), (3, 2), (2, 5), (4, 3), (5, 2), (3, 5), (2, 7),
             (6, 2), (4, 5), (7, 3), (2, 11), (5, 3), (8, 2), (3, 7),
             (10, 3)]),
         },
        {"sr": "Ienes reizinātāju zem saknes",
         "stunda": TEMATS,
         "jautajumi": V.kopa(ienes, [
             (2, 3), (3, 2), (2, 5), (4, 3), (5, 2), (3, 5), (2, 7),
             (6, 2), (4, 5), (7, 3), (2, 11), (5, 3), (8, 2), (3, 7),
             (10, 3)]),
         },
        {"sr": "Savelk līdzīgas kvadrātsaknes",
         "stunda": TEMATS,
         "jautajumi": V.kopa(lidzigas, [
             (3, 5, 2), (4, 2, 3), (6, 1, 5), (2, 7, 3), (5, 4, 2),
             (8, 3, 7), (1, 9, 5), (7, 6, 2), (3, 8, 11), (9, 2, 3),
             (4, 6, 13), (10, 5, 2), (2, 12, 7), (11, 4, 3), (6, 9, 5)]),
         },
        {"sr": "Noapaļo un novērtē vērtības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Noapaļo 3,146 līdz simtdaļām!", ["3,15", "3,14", "3,1",
                                                "3"], 0),
             ("Noapaļo 2,718 līdz desmitdaļām!", ["2,7", "2,8", "2,72",
                                                  "3"], 0),
             ("Noapaļo 1,4142 līdz simtdaļām!", ["1,41", "1,42", "1,4",
                                                 "1"], 0),
             ("Cik aptuveni ir √2?", ["1,41", "2,41", "0,41", "4"], 0),
             ("Cik aptuveni ir √3?", ["1,73", "2,73", "0,73", "9"], 0),
             ("Cik aptuveni ir π?", ["3,14", "3,41", "2,14", "31,4"], 0),
             ("Starp kuriem veseliem skaitļiem atrodas √50?",
              ["starp 7 un 8", "starp 6 un 7", "starp 8 un 9",
               "starp 24 un 26"], 0),
             ("Starp kuriem veseliem skaitļiem atrodas √30?",
              ["starp 5 un 6", "starp 4 un 5", "starp 6 un 7",
               "starp 14 un 16"], 0),
         ]},
        {"sr": "Salīdzina reālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kurš skaitlis ir lielākais?", ["√17", "4", "3,9", "{15|4}"],
              0),
             ("Kurš skaitlis ir mazākais?", ["√2", "1,5", "{3|2}", "2"], 0),
             ("Kurš apgalvojums par sakni ir patiess?",
              ["√9 = 3", "√9 = 4,5", "√9 = 81", "√9 = 18"], 0),
             ("Kurš apgalvojums ir patiess?",
              ["√16 < √25", "√16 > √25", "√16 = √25", "√16 = 25"], 0),
             ("Kurš skaitlis ir starp 2 un 3?", ["√5", "√2", "√10",
                                                 "√16"], 0),
             ("Sakārto augošā secībā:  √4;  √9;  √1.",
              ["√1; √4; √9", "√9; √4; √1", "√4; √1; √9", "√1; √9; √4"], 0),
             ("Kurš skaitlis ir tuvāk 5?", ["√26", "√20", "√30", "√36"], 0),
             ("Vai √a aug, ja a aug?",
              ["jā", "nē", "tikai veseliem", "tikai līdz 100"], 0),
         ]},
        {"sr": "Zina mērījuma precizitāti",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir mērījuma kļūda?",
              ["novirze no precīzās vērtības", "aprēķina kļūda",
               "nepareizs mērinstruments", "noapaļošana"], 0),
             ("Kā pieraksta mērījumu ar kļūdu?",
              ["12,5 ± 0,1 cm", "12,5 cm", "±12,5 cm", "12,5 : 0,1 cm"], 0),
             ("Kāpēc mērījumu rezultāts ir tuvinājums?",
              ["katram instrumentam ir ierobežota precizitāte",
               "matemātika ir neprecīza", "skaitļi ir iracionāli",
               "mērīt nevajag"], 0),
             ("Ar kādu precizitāti mēra ar lineālu, kura iedaļa ir 1 mm?",
              ["līdz 1 mm", "līdz 1 cm", "līdz 0,1 mm", "līdz 1 m"], 0),
             ("Kā rīkojas ar π praktiskos aprēķinos?",
              ["lieto tuvinājumu 3,14", "lieto 3", "lieto 22",
               "neizmanto"], 0),
             ("Kurš pieraksts ir precīzā vērtība?",
              ["√2", "1,41", "1,414", "1,4142"], 0),
             ("Kāpēc starprezultātus nenoapaļo pārāk agri?",
              ["kļūda uzkrājas", "aprēķins kļūst garāks",
               "tas nav atļauts", "tas nemaina neko"], 0),
             ("Cik zīmju aiz komata atstāj, ja prasa simtdaļas?",
              ["divas", "vienu", "trīs", "nevienu"], 0),
         ]},
        {"sr": "Vienkāršo izteiksmes ar saknēm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vienkāršo:  √8.", ["2√2", "4√2", "2√4", "8√2"], 0),
             ("Vienkāršo:  √18.", ["3√2", "2√3", "9√2", "3√6"], 0),
             ("Vienkāršo:  √50.", ["5√2", "2√5", "25√2", "5√10"], 0),
             ("Vienkāršo:  √(4 · 9).", ["6", "13", "36", "√13"], 0),
             ("Vienkāršo:  √({16|25}).", ["{4|5}", "{16|5}", "{4|25}",
                                          "{8|10}"], 0),
             ("Vienkāršo:  2√3 · √3.", ["6", "2√3", "2√9", "9"], 0),
             ("Vienkāršo:  √20 : √5.", ["2", "4", "√15", "15"], 0),
             ("Vienkāršo:  3√5 − √5.", ["2√5", "3", "2", "3√5"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 3,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "3. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.3. temata noslēgumā. "
                "Pārbauda racionālus un iracionālus skaitļus, kvadrātsaknes "
                "aprēķināšanu, sakņu īpašības, reizinātāja iznešanu un "
                "ienešanu un noapaļošanu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Atšķir racionālus un iracionālus skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir iracionāls skaitlis?",
              ["skaitlis, ko nevar pierakstīt kā daļu",
               "negatīvs skaitlis", "ļoti liels skaitlis",
               "skaitlis ar komatu"], 0),
             ("Kurš skaitlis ir iracionāls?", ["√5", "0,25", "{2|3}",
                                               "−4"], 0),
             ("Kurš skaitlis ir racionāls?", ["0,75", "√7", "√11", "π"], 0),
             ("Vai π ir racionāls skaitlis?",
              ["nē", "jā", "tikai noapaļots", "nevar noteikt"], 0),
             ("Vai √16 ir iracionāls skaitlis?",
              ["nē, tas ir 4", "jā", "tikai aptuveni", "nevar noteikt"], 0),
             ("Kāda ir iracionāla skaitļa decimāldaļa?",
              ["bezgalīga un neperiodiska", "galīga",
               "bezgalīga periodiska", "vienmēr nulle"], 0),
             ("Kurš pieraksts ir precīzā vērtība?",
              ["√3", "1,73", "1,732", "1,7321"], 0),
             ("Kāda decimāldaļa iznāk, pārveidojot parasto daļu?",
              ["galīga vai bezgalīga periodiska", "vienmēr galīga",
               "vienmēr bezgalīga", "vienmēr neperiodiska"], 0),
         ]},
        {"sr": "Aprēķina kvadrātsakni",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sakne, [
             9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225,
             256, 900]),
         },
        {"sr": "Lieto saknes īpašības",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(kvadrats, [
             3, 5, 7, 11, 13, 6, 10])
             + V.kopa(reizina, [
                 (2, 8), (3, 12), (5, 20), (2, 18), (6, 24), (3, 27),
                 (7, 28), (2, 32)])),
         },
        {"sr": "Iznes un ienes reizinātāju",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(iznes, [
             (2, 3), (3, 2), (2, 5), (4, 3), (5, 2), (3, 5), (2, 7)])
             + V.kopa(ienes, [
                 (6, 2), (4, 5), (7, 3), (2, 11), (5, 3), (8, 2), (3, 7),
                 (10, 3)])),
         },
        {"sr": "Savelk līdzīgas kvadrātsaknes",
         "stunda": TEMATS,
         "jautajumi": V.kopa(lidzigas, [
             (4, 6, 2), (5, 3, 3), (7, 2, 5), (3, 8, 3), (6, 5, 2),
             (9, 4, 7), (2, 10, 5), (8, 7, 2), (4, 9, 11), (10, 3, 3),
             (5, 7, 13), (11, 6, 2), (3, 13, 7), (12, 5, 3), (7, 10, 5)]),
         },
        {"sr": "Noapaļo un salīdzina skaitļus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Noapaļo 3,146 līdz simtdaļām!", ["3,15", "3,14", "3,1",
                                                "3"], 0),
             ("Noapaļo 2,718 līdz desmitdaļām!", ["2,7", "2,8", "2,72",
                                                  "3"], 0),
             ("Cik aptuveni ir √2?", ["1,41", "2,41", "0,41", "4"], 0),
             ("Starp kuriem veseliem skaitļiem atrodas √50?",
              ["starp 7 un 8", "starp 6 un 7", "starp 8 un 9",
               "starp 24 un 26"], 0),
             ("Kurš skaitlis ir lielākais?", ["√17", "4", "3,9",
                                              "{15|4}"], 0),
             ("Kurš apgalvojums ir patiess?",
              ["√16 < √25", "√16 > √25", "√16 = √25", "√16 = 25"], 0),
             ("Kas ir mērījuma kļūda?",
              ["novirze no precīzās vērtības", "aprēķina kļūda",
               "nepareizs mērinstruments", "noapaļošana"], 0),
             ("Kāpēc starprezultātus nenoapaļo pārāk agri?",
              ["kļūda uzkrājas", "aprēķins kļūst garāks",
               "tas nav atļauts", "tas nemaina neko"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina un pārveido kvadrātsaknes",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Kvadrātsaknes",
             lambda a, k, r: [
                 ("√%d = ……" % a, V.sk(int(round(a ** 0.5)))),
                 ("(√%d)² = ……" % r, V.sk(r)),
                 ("√%d = …… (iznes reizinātāju)" % (k * k * r),
                  "%d√%d" % (k, r)),
                 ("%d√%d = …… (ienes zem saknes)" % (k, r),
                  "√%d" % (k * k * r))],
             [(16, 2, 3), (25, 3, 2), (36, 2, 5), (49, 4, 3), (64, 5, 2),
              (81, 3, 5), (100, 2, 7), (121, 6, 2), (144, 4, 5),
              (169, 7, 3), (196, 2, 11), (225, 5, 3), (256, 8, 2),
              (400, 3, 7), (900, 10, 3)]),
         },
        {"sr": "Lieto sakņu īpašības",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Darbības ar saknēm",
             lambda a, b, m, n, r: [
                 ("√%d · √%d = ……" % (a, b),
                  V.sk(int(round((a * b) ** 0.5)))),
                 ("√%d : √%d = ……" % (a * b, b),
                  V.sk(int(round(a ** 0.5))) if int(a ** 0.5) ** 2 == a
                  else "√%d" % a),
                 ("%d√%d + %d√%d = ……" % (m, r, n, r),
                  "%d√%d" % (m + n, r))],
             [(4, 9, 3, 5, 2), (9, 16, 4, 2, 3), (16, 25, 6, 1, 5),
              (25, 4, 2, 7, 3), (36, 9, 5, 4, 2), (49, 16, 8, 3, 7),
              (64, 25, 1, 9, 5), (81, 4, 7, 6, 2), (100, 9, 3, 8, 11),
              (121, 16, 9, 2, 3), (144, 25, 4, 6, 13), (4, 36, 10, 5, 2),
              (9, 49, 2, 12, 7), (16, 64, 11, 4, 3), (25, 81, 6, 9, 5)]),
         },
        {"sr": "Risina uzdevumu ar kvadrātsakni",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Kvadrāts un sakne",
             lambda s, a: {
                 "teksts": "Kvadrāta laukums ir %d cm².   a) Cik gara ir "
                           "kvadrāta mala?   b) Cik garš ir perimetrs?   "
                           "c) Kāds būtu malas garums, ja laukums būtu "
                           "%d cm²?   d) Vai šis malas garums ir racionāls "
                           "skaitlis? Pamato!" % (s, a),
                 "kriteriji": [
                     "a) √%d = %d cm.   (1 p.)"
                     % (s, int(round(s ** 0.5))),
                     "b) 4 · %d = %d cm.   (1 p.)"
                     % (int(round(s ** 0.5)), 4 * int(round(s ** 0.5))),
                     "c) √%d cm.   (1 p.)" % a,
                     "d) Nē — %d nav pilns kvadrāts, tāpēc √%d ir "
                     "iracionāls.   (1 p.)" % (a, a)]},
             [(16, 2), (25, 3), (36, 5), (49, 7), (64, 10), (81, 11),
              (100, 13), (121, 15), (144, 17), (169, 19), (196, 21),
              (225, 23), (256, 26), (400, 29), (900, 31)]),
         },
        {"sr": "Pamato spriedumus par skaitļiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Racionāli un iracionāli skaitļi",
             lambda a, b: {
                 "ievads": "Doti skaitļi  √%d  un  √%d." % (a, b),
                 "jaut": [("Kurš no tiem ir racionāls? Aprēķini to!", 1),
                          ("Kurš ir iracionāls? Pamato!", 1),
                          ("Starp kuriem veseliem skaitļiem tas atrodas?",
                           1)],
                 "atbildes": [
                     "1) √%d = %d.   (1 p.)" % (a, int(round(a ** 0.5))),
                     "2) √%d — %d nav pilns kvadrāts.   (1 p.)" % (b, b),
                     "3) Starp %d un %d.   (1 p.)"
                     % (int(b ** 0.5), int(b ** 0.5) + 1)]},
             [(16, 2), (25, 3), (36, 5), (49, 7), (64, 10), (81, 11),
              (100, 13), (121, 15), (144, 17), (169, 19), (196, 21),
              (225, 23), (256, 26), (400, 29), (900, 31)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
