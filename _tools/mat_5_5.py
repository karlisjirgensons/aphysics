# -*- coding: utf-8 -*-
"""Matemātika, 5. klase. 5.5. Kā saskaita un atņem jauktus skaitļus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 5. klase, 5.5. temats): jaukts skaitlis un
neīsta daļa, to savstarpējā pārveidošana, jauktu skaitļu vieta uz skaitļu
taisnes un salīdzināšana, saskaitīšana un atņemšana ar vienādiem un dažādiem
saucējiem, pāreja pār veselo un aizņemšanās no veselā.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  5. klase"
TEMATS = "5.5."
NOSAUKUMS = "Kā saskaita un atņem jauktus skaitļus?"

ATGADNE = [
    "Jaukts skaitlis ir vesela skaitļa un īstas daļas summa:   2{1|4} = "
    "2 + {1|4}",
    "Neīstu daļu pārveido, dalot ar atlikumu:   {9|4} = 2{1|4}      ·      "
    "jauktu skaitli:   2{1|4} = {2 · 4 + 1|4} = {9|4}",
    "Saskaita un atņem atsevišķi veselos un atsevišķi daļas; ja daļa ir par "
    "mazu, no veselā aizņemas 1.",
]


def lkd(a, b):
    while b:
        a, b = b, a % b
    return a


def jaukts(vesels, a, b):
    """Jaukta skaitļa pieraksts:  2{1|4};  vesela daļa var arī iztrūkt."""
    a %= b
    if a == 0:
        return V.sk(vesels)
    if vesels == 0:
        return "{%d|%d}" % (a, b)
    return "%d{%d|%d}" % (vesels, a, b)


def no_neistas(sk, b):
    """Neīstu daļu {sk|b} pieraksta kā jauktu skaitli."""
    return jaukts(sk // b, sk % b, b)


# ---------------------------------------------------------------- veidnes
def parveido_jauktu(sk, b):
    """Neīsta daļa -> jaukts skaitlis."""
    return ("Pārveido neīsto daļu {%d|%d} par jauktu skaitli!" % (sk, b),
            V.izvele(no_neistas(sk, b), no_neistas(sk + b, b),
                     no_neistas(sk + 1, b), "%d{%d|%d}" % (sk % b, sk // b,
                                                           b),
                     no_neistas(sk - 1, b), "{%d|%d}" % (b, sk)), 0)


def parveido_neistu(vesels, a, b):
    """Jaukts skaitlis -> neīsta daļa."""
    sk = vesels * b + a
    return ("Pārveido jaukto skaitli %s par neīstu daļu!"
            % jaukts(vesels, a, b),
            V.izvele("{%d|%d}" % (sk, b), "{%d|%d}" % (vesels * b, b),
                     "{%d|%d}" % (vesels + a, b), "{%d|%d}" % (b, sk),
                     "{%d|%d}" % (sk + 1, b), "{%d|%d}" % (sk - b, b)), 0)


def salidzina(v1, a1, v2, a2, b):
    """Divu jauktu skaitļu salīdzināšana ar vienādu saucēju."""
    pirmais = v1 * b + a1 > v2 * b + a2
    return ("Kurš skaitlis ir lielāks: %s vai %s?"
            % (jaukts(v1, a1, b), jaukts(v2, a2, b)),
            V.izvele(jaukts(v1, a1, b) if pirmais else jaukts(v2, a2, b),
                     jaukts(v2, a2, b) if pirmais else jaukts(v1, a1, b),
                     "tie ir vienādi", "nevar salīdzināt"), 0)


def saskaita(v1, a1, v2, a2, b):
    """Jauktu skaitļu saskaitīšana ar vienādiem saucējiem."""
    sk = (v1 * b + a1) + (v2 * b + a2)
    return ("Cik ir %s + %s?" % (jaukts(v1, a1, b), jaukts(v2, a2, b)),
            V.izvele(no_neistas(sk, b), no_neistas(sk + b, b),
                     jaukts(v1 + v2, a1 + a2, b) if a1 + a2 < b
                     else no_neistas(sk - b, b),
                     no_neistas(sk + 1, b), no_neistas(sk - 1, b),
                     "{%d|%d}" % (sk, b * 2)), 0)


def atnem(v1, a1, v2, a2, b):
    """Jauktu skaitļu atņemšana ar vienādiem saucējiem."""
    sk = (v1 * b + a1) - (v2 * b + a2)
    return ("Cik ir %s − %s?" % (jaukts(v1, a1, b), jaukts(v2, a2, b)),
            V.izvele(no_neistas(sk, b), no_neistas(sk + b, b),
                     no_neistas(sk + 1, b), no_neistas(sk - 1, b),
                     "{%d|%d}" % (sk, b * 2),
                     jaukts(v1 - v2, abs(a1 - a2), b)), 0)


def dazadi_sauceji(v1, a1, b1, a2, b2):
    """Jaukta skaitļa un daļas saskaitīšana ar dažādiem saucējiem."""
    sauc = b1 * b2 // lkd(b1, b2)
    sk = (v1 * b1 + a1) * (sauc // b1) + a2 * (sauc // b2)
    return ("Cik ir %s + {%d|%d}?" % (jaukts(v1, a1, b1), a2, b2),
            V.izvele(no_neistas(sk, sauc), no_neistas(sk + sauc, sauc),
                     "%d{%d|%d}" % (v1, a1 + a2, b1 + b2),
                     no_neistas(sk + 1, sauc), no_neistas(sk - 1, sauc),
                     "{%d|%d}" % (sk, sauc * 2)), 0)


FD = {
    "veids": "fd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 5.5. temata beigās. Pārbauda jaukta "
                "skaitļa un neīstas daļas pārveidošanu, salīdzināšanu, "
                "saskaitīšanu un atņemšanu, arī ar pāreju pār veselo un "
                "aizņemoties no veselā.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina jaukta skaitļa jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir jaukts skaitlis?",
              ["vesela skaitļa un īstas daļas summa", "divu daļu summa",
               "neīsta daļa", "divu veselu skaitļu summa"], 0),
             ("Kas ir neīsta daļa?",
              ["daļa, kuras skaitītājs nav mazāks nekā saucējs",
               "daļa ar skaitītāju 1", "daļa ar lielu saucēju",
               "jaukts skaitlis"], 0),
             ("Ko nozīmē pieraksts 2{1|4}?",
              ["2 + {1|4}", "2 · {1|4}", "2 − {1|4}", "{2|4}"], 0),
             ("Kura daļa ir neīsta?", ["{7|4}", "{3|4}", "{1|4}",
                                       "{2|5}"], 0),
             ("Kura daļa ir īsta?", ["{3|8}", "{9|8}", "{8|8}",
                                     "{11|8}"], 0),
             ("Ar ko vienāda daļa {6|6}?", ["1", "0", "6", "{1|6}"], 0),
             ("Vai jauktu skaitli vienmēr var pierakstīt kā neīstu daļu?",
              ["jā", "nē", "tikai ar vienādiem saucējiem",
               "tikai veseliem"], 0),
             ("Kāda daļa paliek jauktā skaitlī aiz veselās daļas?",
              ["īsta daļa", "neīsta daļa", "vesels skaitlis",
               "nulle"], 0),
         ]},
        {"sr": "Pārveido neīstu daļu par jauktu skaitli",
         "stunda": TEMATS,
         "jautajumi": V.kopa(parveido_jauktu, [
             (9, 4), (7, 3), (11, 5), (13, 6), (17, 8), (23, 10), (5, 2),
             (19, 7), (25, 9), (14, 4), (29, 12), (33, 11), (16, 5),
             (27, 8), (41, 15)]),
         },
        {"sr": "Pārveido jauktu skaitli par neīstu daļu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(parveido_neistu, [
             (2, 1, 4), (1, 2, 3), (3, 1, 5), (2, 3, 7), (4, 2, 9),
             (1, 5, 6), (5, 1, 2), (3, 4, 11), (2, 7, 8), (6, 1, 3),
             (4, 5, 12), (7, 2, 5), (3, 8, 13), (5, 3, 10), (8, 4, 9)]),
         },
        {"sr": "Nosaka jaukta skaitļa vietu uz skaitļu taisnes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Starp kuriem veseliem skaitļiem atrodas 2{1|3}?",
              ["starp 2 un 3", "starp 1 un 2", "starp 3 un 4",
               "starp 0 un 1"], 0),
             ("Starp kuriem veseliem skaitļiem atrodas {7|2}?",
              ["starp 3 un 4", "starp 2 un 3", "starp 6 un 8",
               "starp 7 un 8"], 0),
             ("Starp kuriem veseliem skaitļiem atrodas {11|4}?",
              ["starp 2 un 3", "starp 3 un 4", "starp 10 un 12",
               "starp 1 un 2"], 0),
             ("Kurš skaitlis ir tuvāk 3?", ["2{7|8}", "2{1|8}", "3{5|8}",
                                            "2{1|2}"], 0),
             ("Kurš skaitlis atrodas pa kreisi no 4?",
              ["3{5|6}", "4{1|6}", "5", "4{5|6}"], 0),
             ("Cik vienādās daļās sadala nogriezni starp 2 un 3, lai "
              "atliktu 2{3|5}?", ["5", "3", "2", "10"], 0),
             ("Kurš skaitlis ir vistuvāk 5?", ["4{9|10}", "4{1|10}",
                                               "5{1|2}", "4{1|2}"], 0),
             ("Ar ko vienāds jaukts skaitlis 3{0|4}?",
              ["3", "4", "{3|4}", "12"], 0),
         ]},
        {"sr": "Salīdzina jauktus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(salidzina, [
             (2, 1, 2, 3, 4), (3, 2, 2, 5, 6), (1, 4, 1, 2, 5),
             (4, 1, 3, 6, 7), (2, 5, 2, 3, 8), (5, 2, 5, 7, 9),
             (3, 4, 4, 1, 5), (6, 1, 6, 5, 8), (2, 7, 3, 1, 10),
             (7, 3, 7, 8, 11), (4, 5, 4, 2, 6), (8, 1, 8, 9, 12),
             (5, 6, 6, 2, 7), (9, 4, 9, 11, 13), (3, 9, 4, 3, 10)]),
         },
        {"sr": "Saskaita jauktus skaitļus ar vienādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saskaita, [
             (2, 1, 1, 1, 4), (3, 2, 2, 1, 6), (1, 3, 2, 1, 7),
             (4, 1, 1, 2, 5), (2, 3, 3, 2, 8), (5, 2, 2, 3, 9),
             (1, 4, 3, 1, 10), (6, 3, 1, 4, 11), (2, 5, 4, 2, 12),
             (3, 1, 5, 1, 3), (7, 2, 2, 4, 13), (4, 3, 3, 5, 14),
             (8, 1, 1, 6, 15), (5, 4, 4, 3, 16), (9, 2, 2, 7, 17)]),
         },
        {"sr": "Saskaita ar pāreju pār veselo",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saskaita, [
             (2, 3, 1, 3, 4), (3, 4, 2, 4, 6), (1, 5, 2, 5, 7),
             (4, 3, 1, 4, 5), (2, 6, 3, 5, 8), (5, 7, 2, 5, 9),
             (1, 8, 3, 7, 10), (6, 9, 1, 8, 11), (2, 10, 4, 9, 12),
             (3, 2, 5, 2, 3), (7, 11, 2, 10, 13), (4, 12, 3, 11, 14),
             (8, 13, 1, 12, 15), (5, 14, 4, 13, 16), (9, 15, 2, 14, 17)]),
         },
        {"sr": "Atņem jauktus skaitļus ar vienādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem, [
             (3, 3, 1, 1, 4), (5, 4, 2, 1, 6), (4, 5, 1, 2, 7),
             (6, 3, 2, 1, 5), (5, 6, 3, 2, 8), (7, 7, 2, 3, 9),
             (4, 8, 1, 3, 10), (8, 9, 3, 4, 11), (6, 10, 2, 5, 12),
             (5, 2, 3, 1, 3), (9, 11, 4, 5, 13), (7, 12, 3, 6, 14),
             (10, 13, 2, 7, 15), (8, 14, 5, 8, 16), (11, 15, 4, 9, 17)]),
         },
        {"sr": "Atņem, aizņemoties no veselā",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem, [
             (3, 1, 1, 3, 4), (5, 1, 2, 4, 6), (4, 2, 1, 5, 7),
             (6, 1, 2, 3, 5), (5, 2, 3, 6, 8), (7, 3, 2, 7, 9),
             (4, 3, 1, 8, 10), (8, 4, 3, 9, 11), (6, 5, 2, 10, 12),
             (5, 1, 3, 2, 3), (9, 5, 4, 11, 13), (7, 6, 3, 12, 14),
             (10, 7, 2, 13, 15), (8, 8, 5, 14, 16), (11, 9, 4, 15, 17)]),
         },
        {"sr": "Rēķina ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dazadi_sauceji, [
             (2, 1, 2, 1, 4), (1, 1, 3, 1, 6), (3, 1, 4, 1, 8),
             (2, 2, 5, 1, 10), (1, 1, 2, 1, 6), (4, 3, 4, 1, 8),
             (2, 1, 3, 1, 9), (5, 1, 5, 3, 10), (3, 2, 3, 1, 12),
             (1, 3, 4, 1, 12), (6, 1, 6, 1, 3), (2, 5, 6, 1, 4),
             (4, 1, 4, 5, 12), (7, 2, 7, 1, 14), (3, 1, 5, 1, 15)]),
         },
        {"sr": "Aprēķina nezināmo vienādībā",
         "stunda": TEMATS,
         "jautajumi": [
             ("Atrisini:  x + 1{1|4} = 3{3|4}.",
              ["2{1|2}", "2{2|4}", "5", "2{1|4}"], 0),
             ("Atrisini:  x − 2{1|3} = 1{1|3}.",
              ["3{2|3}", "3{1|3}", "1", "4"], 0),
             ("Atrisini:  4{1|2} − x = 2{1|2}.",
              ["2", "7", "2{1|2}", "1"], 0),
             ("Atrisini:  x + {1|5} = 2{3|5}.",
              ["2{2|5}", "2{4|5}", "3", "2"], 0),
             ("Atrisini:  3 − x = 1{1|4}.",
              ["1{3|4}", "1{1|4}", "2{1|4}", "4{1|4}"], 0),
             ("Atrisini:  x − {2|7} = 1{3|7}.",
              ["1{5|7}", "1{1|7}", "2", "1"], 0),
             ("Kā atrod nezināmo saskaitāmo?",
              ["no summas atņem zināmo saskaitāmo", "saskaita abus",
               "reizina tos", "dala summu ar 2"], 0),
             ("Kā atrod nezināmo mazināmo?",
              ["starpībai pieskaita mazinātāju", "no starpības atņem",
               "reizina tos", "dala starpību"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ievai bija 2{1|2} m lentes; izlietoja 1{1|4} m. Cik palika?",
              ["1{1|4} m", "1{1|2} m", "3{3|4} m", "1 m"], 0),
             ("Divas kastes sver 1{1|3} kg un 2{1|3} kg. Cik kopā?",
              ["3{2|3} kg", "3{1|3} kg", "4 kg", "1 kg"], 0),
             ("Recepte prasa 1{1|2} l piena; ir 3 l. Cik paliks pāri?",
              ["1{1|2} l", "2{1|2} l", "4{1|2} l", "1 l"], 0),
             ("Skrējiens 5{1|4} km; noskrieti 2{3|4} km. Cik atlicis?",
              ["2{1|2} km", "3{1|2} km", "8 km", "2 km"], 0),
             ("Divi dēļi: 2{2|5} m un 1{4|5} m. Cik kopā?",
              ["4{1|5} m", "3{6|5} m", "4 m", "3{1|5} m"], 0),
             ("No 4 m auduma nogrieza 1{2|3} m. Cik palika?",
              ["2{1|3} m", "3{1|3} m", "2{2|3} m", "5{2|3} m"], 0),
             ("Uzdevumam veltīja 1{1|2} h un 2{1|4} h. Cik kopā?",
              ["3{3|4} h", "3{1|2} h", "4 h", "3{2|6} h"], 0),
             ("Kanna 3{1|2} l; izlēja 1{3|4} l. Cik palika?",
              ["1{3|4} l", "2{1|4} l", "5{1|4} l", "2 l"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 5,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 5.5. temata noslēgumā. "
                "Pārbauda jauktu skaitļu un neīstu daļu pārveidošanu, "
                "salīdzināšanu, saskaitīšanu un atņemšanu, arī ar dažādiem "
                "saucējiem.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Pārveido jauktus skaitļus un neīstas daļas",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(parveido_jauktu, [
             (11, 4), (8, 3), (13, 5), (17, 6), (19, 8), (27, 10), (7, 2)])
             + V.kopa(parveido_neistu, [
                 (3, 1, 4), (2, 2, 3), (4, 1, 5), (1, 3, 7), (5, 2, 9),
                 (2, 5, 6), (6, 1, 2), (4, 4, 11)])),
         },
        {"sr": "Salīdzina jauktus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(salidzina, [
             (3, 1, 3, 2, 4), (2, 3, 2, 1, 6), (4, 2, 4, 4, 5),
             (5, 1, 4, 6, 7), (3, 5, 3, 2, 8), (6, 2, 6, 7, 9),
             (2, 4, 3, 1, 5), (7, 1, 7, 5, 8), (4, 7, 5, 1, 10),
             (8, 3, 8, 8, 11), (5, 5, 5, 2, 6), (9, 1, 9, 9, 12),
             (6, 6, 7, 2, 7), (10, 4, 10, 11, 13), (4, 9, 5, 3, 10)]),
         },
        {"sr": "Saskaita jauktus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(saskaita, [
             (1, 1, 2, 1, 4), (2, 2, 3, 1, 6), (2, 3, 1, 1, 7),
             (3, 1, 2, 2, 5), (1, 3, 4, 2, 8), (4, 2, 3, 3, 9),
             (2, 4, 2, 1, 10), (5, 3, 2, 4, 11), (3, 5, 3, 2, 12),
             (2, 1, 6, 1, 3), (6, 2, 3, 4, 13), (3, 3, 4, 5, 14),
             (7, 1, 2, 6, 15), (4, 4, 5, 3, 16), (8, 2, 3, 7, 17)]),
         },
        {"sr": "Atņem jauktus skaitļus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(atnem, [
             (4, 3, 1, 1, 4), (6, 4, 2, 1, 6), (5, 5, 1, 2, 7),
             (7, 3, 2, 1, 5), (6, 6, 3, 2, 8), (8, 7, 2, 3, 9),
             (5, 1, 1, 3, 10), (9, 4, 3, 9, 11), (7, 5, 2, 10, 12),
             (6, 1, 3, 2, 3), (10, 5, 4, 11, 13), (8, 6, 3, 12, 14),
             (11, 7, 2, 13, 15), (9, 8, 5, 14, 16), (12, 9, 4, 15, 17)]),
         },
        {"sr": "Rēķina ar dažādiem saucējiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(dazadi_sauceji, [
             (3, 1, 2, 1, 4), (2, 1, 3, 1, 6), (4, 1, 4, 1, 8),
             (3, 2, 5, 1, 10), (2, 1, 2, 1, 6), (5, 3, 4, 1, 8),
             (3, 1, 3, 1, 9), (6, 1, 5, 3, 10), (4, 2, 3, 1, 12),
             (2, 3, 4, 1, 12), (7, 1, 6, 1, 3), (3, 5, 6, 1, 4),
             (5, 1, 4, 5, 12), (8, 2, 7, 1, 14), (4, 1, 5, 1, 15)]),
         },
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ievai bija 2{1|2} m lentes; izlietoja 1{1|4} m. Cik palika?",
              ["1{1|4} m", "1{1|2} m", "3{3|4} m", "1 m"], 0),
             ("Divas kastes sver 1{1|3} kg un 2{1|3} kg. Cik kopā?",
              ["3{2|3} kg", "3{1|3} kg", "4 kg", "1 kg"], 0),
             ("Recepte prasa 1{1|2} l piena; ir 3 l. Cik paliks pāri?",
              ["1{1|2} l", "2{1|2} l", "4{1|2} l", "1 l"], 0),
             ("Skrējiens 5{1|4} km; noskrieti 2{3|4} km. Cik atlicis?",
              ["2{1|2} km", "3{1|2} km", "8 km", "2 km"], 0),
             ("No 4 m auduma nogrieza 1{2|3} m. Cik palika?",
              ["2{1|3} m", "3{1|3} m", "2{2|3} m", "5{2|3} m"], 0),
             ("Uzdevumam veltīja 1{1|2} h un 2{1|4} h. Cik kopā?",
              ["3{3|4} h", "3{1|2} h", "4 h", "3{2|6} h"], 0),
             ("Kanna 3{1|2} l; izlēja 1{3|4} l. Cik palika?",
              ["1{3|4} l", "2{1|4} l", "5{1|4} l", "2 l"], 0),
             ("Divi dēļi: 2{2|5} m un 1{4|5} m. Cik kopā?",
              ["4{1|5} m", "3{6|5} m", "4 m", "3{1|5} m"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Pārveido, saskaita un atņem jauktus skaitļus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda sk, b, v, a: [
                 ("{%d|%d} = …… (jaukts skaitlis)" % (sk, b),
                  no_neistas(sk, b)),
                 ("%s = …… (neīsta daļa)" % jaukts(v, a, b),
                  "{%d|%d}" % (v * b + a, b)),
                 ("%s + %s = ……" % (jaukts(v, a, b), jaukts(1, 1, b)),
                  no_neistas(v * b + a + b + 1, b)),
                 ("%s − %s = ……" % (jaukts(v, a, b), jaukts(1, 1, b)),
                  no_neistas(v * b + a - b - 1, b))],
             [(9, 4, 2, 1), (7, 3, 3, 2), (11, 5, 4, 1), (13, 6, 2, 3),
              (17, 8, 5, 2), (23, 10, 3, 4), (5, 2, 6, 1), (19, 7, 4, 3),
              (25, 9, 7, 2), (14, 4, 5, 3), (29, 12, 8, 5), (33, 11, 6, 4),
              (16, 5, 9, 2), (27, 8, 7, 5), (41, 15, 10, 6)]),
         },
        {"sr": "Salīdzina jauktus skaitļus un neīstas daļas",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Salīdzini",
             lambda v1, a1, v2, a2, b: [
                 ("Lielākais no %s un %s:   ……"
                  % (jaukts(v1, a1, b), jaukts(v2, a2, b)),
                  jaukts(v1, a1, b) if v1 * b + a1 > v2 * b + a2
                  else jaukts(v2, a2, b)),
                 ("%s = …… (neīsta daļa)" % jaukts(v1, a1, b),
                  "{%d|%d}" % (v1 * b + a1, b)),
                 ("{%d|%d} = …… (jaukts skaitlis)" % (v2 * b + a2, b),
                  no_neistas(v2 * b + a2, b))],
             [(2, 1, 2, 3, 4), (3, 2, 2, 5, 6), (1, 4, 1, 2, 5),
              (4, 1, 3, 6, 7), (2, 5, 2, 3, 8), (5, 2, 5, 7, 9),
              (3, 4, 4, 1, 5), (6, 1, 6, 5, 8), (2, 7, 3, 1, 10),
              (7, 3, 7, 8, 11), (4, 5, 4, 2, 6), (8, 1, 8, 9, 12),
              (5, 6, 6, 2, 7), (9, 4, 9, 11, 13), (3, 9, 4, 3, 10)]),
         },
        {"sr": "Risina situāciju uzdevumu ar jauktiem skaitļiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda v1, a1, v2, a2, b: {
                 "teksts": "Pirmajā traukā ir %s l sulas, otrajā — %s l.   "
                           "a) Cik litru ir kopā?   b) Par cik litriem "
                           "pirmajā ir vairāk?   c) Pieraksti kopējo "
                           "daudzumu kā neīstu daļu!   d) Cik paliks, ja "
                           "izlies 1 l?"
                           % (jaukts(v1, a1, b), jaukts(v2, a2, b)),
                 "kriteriji": [
                     "a) %s.   (1 p.)"
                     % no_neistas((v1 * b + a1) + (v2 * b + a2), b),
                     "b) %s.   (1 p.)"
                     % no_neistas((v1 * b + a1) - (v2 * b + a2), b),
                     "c) {%d|%d}.   (1 p.)"
                     % ((v1 * b + a1) + (v2 * b + a2), b),
                     "d) %s.   (1 p.)"
                     % no_neistas((v1 * b + a1) + (v2 * b + a2) - b, b)]},
             [(3, 3, 1, 1, 4), (5, 4, 2, 1, 6), (4, 5, 1, 2, 7),
              (6, 3, 2, 1, 5), (5, 6, 3, 2, 8), (7, 7, 2, 3, 9),
              (4, 8, 1, 3, 10), (8, 9, 3, 4, 11), (6, 10, 2, 5, 12),
              (5, 2, 3, 1, 3), (9, 11, 4, 5, 13), (7, 12, 3, 6, 14),
              (10, 13, 2, 7, 15), (8, 14, 5, 8, 16), (11, 15, 4, 9, 17)]),
         },
        {"sr": "Skaidro darbības ar jauktiem skaitļiem",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Jaukti skaitļi",
             lambda v, a, b: {
                 "ievads": "Dots jaukts skaitlis  %s." % jaukts(v, a, b),
                 "jaut": [("Pieraksti to kā neīstu daļu!", 1),
                          ("Starp kuriem veseliem skaitļiem tas atrodas?",
                           1),
                          ("Cik ir šis skaitlis mīnus 1?", 1)],
                 "atbildes": [
                     "1) {%d|%d}.   (1 p.)" % (v * b + a, b),
                     "2) Starp %d un %d.   (1 p.)" % (v, v + 1),
                     "3) %s.   (1 p.)" % jaukts(v - 1, a, b)]},
             [(2, 1, 4), (3, 2, 3), (4, 1, 5), (2, 3, 7), (5, 2, 9),
              (1, 5, 6), (6, 1, 2), (3, 4, 11), (7, 7, 8), (4, 1, 3),
              (8, 5, 12), (5, 2, 5), (9, 8, 13), (6, 3, 10), (10, 4, 9)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
