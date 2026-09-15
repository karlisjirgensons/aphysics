# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.9. Kā salīdzina izteiksmes, kurās ir mainīgais?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.9. temats): nevienādība un tās
atrisinājums, atrisinājumu kopa un skaitļu intervāls, ekvivalentas
nevienādības un ekvivalentie pārveidojumi, lineāras nevienādības
atrisināšana, divkārša nevienādība un nevienādību sistēma, kā arī situāciju
apraksts ar nevienādību.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.9."
NOSAUKUMS = "Kā salīdzina izteiksmes, kurās ir mainīgais lielums?"

ATGADNE = [
    "Nevienādības abām pusēm drīkst pieskaitīt vai atņemt vienu un to pašu "
    "lielumu. Reizinot vai dalot ar negatīvu skaitli, nevienādības zīmi "
    "maina uz pretējo.",
    "Atrisinājumu kopu pieraksta kā intervālu:   x > 3   ⟹   (3; +∞)   ·  "
    " x ≤ 5   ⟹   (−∞; 5]   ·   2 < x < 7   ⟹   (2; 7)",
    "Divkāršu nevienādību var pierakstīt kā sistēmu; sistēmas atrisinājums "
    "ir abu atrisinājumu kopu šķēlums.",
]


# ---------------------------------------------------------------- veidnes
def nevienadiba(a, b, x):
    """Nevienādība  ax + b > c  ar veselu robežu."""
    c = a * x + b
    zime = "+" if b >= 0 else "−"
    return ("Atrisini nevienādību  %dx %s %d > %d." % (a, zime, abs(b), c),
            V.izvele("x > %s" % V.sk(x), "x < %s" % V.sk(x),
                     "x > %s" % V.sk(c), "x > %s" % V.sk(-x),
                     "x ≥ %s" % V.sk(x), "x > %s" % V.sk(x + 1)), 0)


def vienkarsa(b, x):
    """Nevienādība  x + b < c."""
    c = x + b
    zime = "+" if b >= 0 else "−"
    return ("Atrisini nevienādību  x %s %d < %d." % (zime, abs(b), c),
            V.izvele("x < %s" % V.sk(x), "x > %s" % V.sk(x),
                     "x < %s" % V.sk(c), "x < %s" % V.sk(-x),
                     "x ≤ %s" % V.sk(x), "x < %s" % V.sk(c + b)), 0)


def intervals(a, b):
    """Divkāršas nevienādības atrisinājums kā intervāls."""
    return ("Kā ar intervālu pieraksta atrisinājumu  %d < x < %d?" % (a, b),
            V.izvele("(%d; %d)" % (a, b), "[%d; %d]" % (a, b),
                     "(%d; %d)" % (b, a), "(−∞; %d)" % b,
                     "(%d; +∞)" % a, "(%d; %d]" % (a, b)), 0)


def sistema(a, b):
    """Nevienādību sistēmas atrisinājums kā kopu šķēlums."""
    return ("Kāds ir sistēmas  x > %d  un  x < %d  atrisinājums?" % (a, b),
            V.izvele("%d < x < %d" % (a, b), "x > %d" % b,
                     "x < %d" % a, "%d < x < %d" % (b, a),
                     "atrisinājumu nav", "x > %d" % a), 0)


def parbaude(a, b, x):
    """Vai skaitlis pieder nevienādības atrisinājumu kopai."""
    ir = a * x > b
    return ("Vai x = %d ir nevienādības  %dx > %d  atrisinājums?"
            % (x, a, b),
            V.izvele("jā" if ir else "nē", "nē" if ir else "jā",
                     "tikai ja x > 0", "nevar noteikt"), 0)


def negativs(a, x):
    """Nevienādība  −ax > c - zīmi maina, dalot ar negatīvu skaitli."""
    c = -a * x
    return ("Atrisini nevienādību  %dx > %d." % (-a, c),
            V.izvele("x < %s" % V.sk(x), "x > %s" % V.sk(x),
                     "x < %s" % V.sk(-x), "x > %s" % V.sk(c),
                     "x ≤ %s" % V.sk(x), "x < %s" % V.sk(x + 1)), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 9,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "9. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.9. temata beigās. Pārbauda "
                "nevienādības un tās atrisinājuma jēdzienu, ekvivalentos "
                "pārveidojumus, intervāla pierakstu, nevienādību sistēmu un "
                "situāciju aprakstu ar nevienādību.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina nevienādības jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kam lieto nevienādības?",
              ["izteiksmju salīdzināšanai un novērtējumiem",
               "tikai skaitļu saskaitīšanai", "tikai ģeometrijā",
               "tikai procentiem"], 0),
             ("Kas ir nevienādības atrisinājums?",
              ["skaitlis, ar kuru nevienādība ir patiesa",
               "jebkurš skaitlis", "koeficients", "nezināmais"], 0),
             ("Ko nozīmē atrisināt nevienādību?",
              ["noteikt visu atrisinājumu kopu", "atrast vienu skaitli",
               "pārrakstīt nevienādību", "uzzīmēt grafiku"], 0),
             ("Kad nevienādības ir ekvivalentas?",
              ["ja atrisinājumu kopas sakrīt", "ja tās izskatās vienādi",
               "ja tām ir viens nezināmais", "ja robežas ir veselas"], 0),
             ("Vai nevienādība  x < x + 3  ir patiesa visiem x?",
              ["jā", "nē", "tikai pozitīviem", "tikai negatīviem"], 0),
             ("Vai nevienādība  x > x + 1  ir patiesa kādam x?",
              ["nē, nevienam", "jā, visiem", "tikai pozitīviem",
               "tikai negatīviem"], 0),
             ("Kas ir skaitļu intervāls?",
              ["skaitļu taisnes daļa", "viens skaitlis",
               "divu skaitļu summa", "kopu apvienojums"], 0),
             ("Ar kuru zīmi pieraksta «ne mazāk kā»?",
              ["≥", "≤", ">", "<"], 0),
         ]},
        {"sr": "Zina ekvivalentos pārveidojumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko drīkst darīt ar nevienādības abām pusēm?",
              ["pieskaitīt vienu un to pašu lielumu",
               "pieskaitīt dažādus lielumus", "izsvītrot nezināmo",
               "mainīt zīmi tikai vienā pusē"], 0),
             ("Kas notiek, ja abas puses reizina ar negatīvu skaitli?",
              ["zīmi maina uz pretējo", "zīme nemainās",
               "nevienādība kļūst aplama", "atrisinājums pazūd"], 0),
             ("Kas notiek, ja abas puses reizina ar pozitīvu skaitli?",
              ["zīme nemainās", "zīmi maina uz pretējo",
               "nevienādība kļūst aplama", "atrisinājums pazūd"], 0),
             ("Kā no  x + 4 < 9  iegūst x?",
              ["abām pusēm atņem 4", "abām pusēm pieskaita 4",
               "abas puses dala ar 4", "abas puses reizina ar 4"], 0),
             ("Kā no  3x > 12  iegūst x?",
              ["abas puses dala ar 3", "abas puses reizina ar 3",
               "abām pusēm atņem 3", "abām pusēm pieskaita 3"], 0),
             ("Kā no  −2x > 6  iegūst x?",
              ["dala ar −2 un maina zīmi", "dala ar −2, zīmi nemaina",
               "reizina ar 2", "atņem 2"], 0),
             ("Vai drīkst abas puses dalīt ar 0?",
              ["nē", "jā", "tikai ja x = 0", "vienmēr"], 0),
             ("Kāpēc nevienādību risinot jāspriež par zīmi?",
              ["darbība var mainīt, kurā pusē ir lielāks lielums",
               "lai būtu garāks risinājums", "tā prasa skolotājs",
               "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Atrisina vienkāršu nevienādību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vienkarsa, [
             (5, 7), (3, 9), (-4, 12), (8, 6), (-6, 15), (11, 4),
             (-9, 20), (7, 13), (-2, 18), (14, 5), (-11, 25), (6, 21),
             (-7, 30), (12, 8), (-13, 16)]),
         },
        {"sr": "Atrisina lineāru nevienādību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nevienadiba, [
             (2, 3, 4), (3, -1, 5), (4, 2, 3), (5, -3, 6), (2, 7, 8),
             (6, 1, 2), (3, 5, 7), (7, -2, 4), (4, -5, 9), (8, 3, 2),
             (5, 4, 6), (9, -1, 3), (6, -4, 5), (10, 2, 7), (3, 8, 11)]),
         },
        {"sr": "Atrisina nevienādību ar negatīvu koeficientu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(negativs, [
             (2, 3), (3, 4), (4, 2), (5, 6), (6, 1), (7, 5), (8, 3),
             (9, 2), (10, 7), (11, 4), (12, 5), (13, 2), (14, 6),
             (15, 3), (16, 4)]),
         },
        {"sr": "Pārbauda, vai skaitlis ir atrisinājums",
         "stunda": TEMATS,
         "jautajumi": V.kopa(parbaude, [
             (2, 6, 4), (3, 12, 3), (4, 8, 1), (5, 20, 5), (2, 10, 7),
             (6, 18, 2), (3, 9, 4), (7, 21, 3), (4, 16, 5), (8, 24, 2),
             (5, 15, 4), (9, 27, 3), (6, 12, 1), (10, 30, 4), (3, 21, 6)]),
         },
        {"sr": "Pieraksta atrisinājumu ar intervālu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(intervals, [
             (2, 7), (1, 5), (3, 8), (0, 6), (4, 9), (2, 10), (5, 11),
             (1, 8), (6, 12), (3, 13), (7, 14), (2, 15), (8, 16),
             (4, 17), (9, 18)]),
         },
        {"sr": "Atrisina nevienādību sistēmu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sistema, [
             (2, 7), (1, 5), (3, 8), (0, 6), (4, 9), (2, 10), (5, 11),
             (1, 8), (6, 12), (3, 13), (7, 14), (2, 15), (8, 16),
             (4, 17), (9, 18)]),
         },
        {"sr": "Lasa intervāla pierakstu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē intervāls (3; +∞)?", ["x > 3", "x ≥ 3", "x < 3",
                                               "x ≤ 3"], 0),
             ("Ko nozīmē intervāls (−∞; 5]?", ["x ≤ 5", "x < 5", "x ≥ 5",
                                               "x > 5"], 0),
             ("Ko nozīmē intervāls [2; 6]?", ["2 ≤ x ≤ 6", "2 < x < 6",
                                              "x < 2", "x > 6"], 0),
             ("Kā pieraksta  x ≥ 4  ar intervālu?",
              ["[4; +∞)", "(4; +∞)", "(−∞; 4]", "(−∞; 4)"], 0),
             ("Kā pieraksta  x < 7  ar intervālu?",
              ["(−∞; 7)", "(−∞; 7]", "(7; +∞)", "[7; +∞)"], 0),
             ("Ko nozīmē apaļa iekava intervālā?",
              ["robeža nepieder atrisinājumam",
               "robeža pieder atrisinājumam", "intervāls ir tukšs",
               "intervāls ir bezgalīgs"], 0),
             ("Ko nozīmē kvadrātiekava intervālā?",
              ["robeža pieder atrisinājumam",
               "robeža nepieder atrisinājumam", "intervāls ir tukšs",
               "intervāls ir bezgalīgs"], 0),
             ("Kā uz skaitļu taisnes attēlo  x > 2?",
              ["ar tukšu aplīti pie 2 un svītru pa labi",
               "ar aizkrāsotu aplīti pie 2", "ar svītru pa kreisi",
               "ar vienu punktu"], 0),
         ]},
        {"sr": "Salīdzina izteiksmes ar mainīgo",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kura izteiksme ir lielāka: x vai x + 3?",
              ["x + 3", "x", "tās ir vienādas", "atkarīgs no x"], 0),
             ("Kura izteiksme ir lielāka: 2x vai 3x, ja x > 0?",
              ["3x", "2x", "tās ir vienādas", "nevar noteikt"], 0),
             ("Kura izteiksme ir lielāka: 2x vai 3x, ja x < 0?",
              ["2x", "3x", "tās ir vienādas", "nevar noteikt"], 0),
             ("Kāda ir izteiksmju x un x − 5 starpība?",
              ["5", "−5", "0", "atkarīga no x"], 0),
             ("Vai x² ≥ 0 visiem x?", ["jā", "nē", "tikai pozitīviem",
                                       "tikai veseliem"], 0),
             ("Kura izteiksme ir lielāka, ja x = 0: 2x vai 3x?",
              ["tās ir vienādas", "2x", "3x", "nevar noteikt"], 0),
             ("Kāpēc, salīdzinot 2x un 3x, jāšķiro gadījumi?",
              ["rezultāts atkarīgs no x zīmes", "tā prasa noteikumi",
               "lai būtu garāk", "tas nav vajadzīgs"], 0),
             ("Kas ir pretpiemērs?",
              ["piemērs, kas atspēko apgalvojumu",
               "piemērs, kas apstiprina", "otrs risinājums",
               "otra nevienādība"], 0),
         ]},
        {"sr": "Apraksta situāciju ar nevienādību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru nevienādību pieraksta «x ir vismaz 10»?",
              ["x ≥ 10", "x > 10", "x ≤ 10", "x < 10"], 0),
             ("Ar kuru nevienādību pieraksta «x nepārsniedz 20»?",
              ["x ≤ 20", "x < 20", "x ≥ 20", "x > 20"], 0),
             ("Ar kuru nevienādību pieraksta «x ir lielāks nekā 5»?",
              ["x > 5", "x ≥ 5", "x < 5", "x ≤ 5"], 0),
             ("Somā drīkst būt ne vairāk kā 8 kg. Kā to pieraksta?",
              ["m ≤ 8", "m < 8", "m ≥ 8", "m > 8"], 0),
             ("Biļete maksā 5 eiro; ir 40 eiro. Cik biļešu var nopirkt?",
              ["ne vairāk kā 8", "vismaz 8", "tieši 40", "ne vairāk kā 5"],
              0),
             ("Ar kuru nevienādību pieraksta «x ir no 3 līdz 7»?",
              ["3 ≤ x ≤ 7", "3 < x < 7", "x > 3", "x < 7"], 0),
             ("Taisnstūra perimetrs nepārsniedz 30 cm. Kā to pieraksta?",
              ["P ≤ 30", "P < 30", "P ≥ 30", "P > 30"], 0),
             ("Kāpēc situācijās lieto nevienādības?",
              ["kad lielums var būt dažāds noteiktās robežās",
               "kad lielums ir precīzi zināms", "kad nav skaitļu",
               "kad ir tikai viens skaitlis"], 0),
         ]},
        {"sr": "Zina, kad nevienādība ir patiesa vai aplama",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad nevienādība ir patiesa visām x vērtībām?",
              ["ja pēc pārveidojumiem paliek patiesa skaitliska "
               "nevienādība", "nekad", "ja x ir pozitīvs",
               "ja x ir vesels"], 0),
             ("Vai  x + 1 > x  ir patiesa visiem x?",
              ["jā", "nē", "tikai pozitīviem", "tikai negatīviem"], 0),
             ("Vai  2x > x  ir patiesa visiem x?",
              ["nē, tikai ja x > 0", "jā", "nekad",
               "tikai ja x < 0"], 0),
             ("Cik atrisinājumu ir nevienādībai  x < x?",
              ["neviena", "viens", "bezgalīgi daudz", "divi"], 0),
             ("Cik atrisinājumu ir nevienādībai  0 · x < 5?",
              ["visi skaitļi", "neviens", "tikai 0", "tikai pozitīvi"], 0),
             ("Cik atrisinājumu ir nevienādībai  0 · x > 5?",
              ["neviens", "visi skaitļi", "tikai 0", "tikai pozitīvi"], 0),
             ("Kā pārbauda, vai skaitlis ir atrisinājums?",
              ["ievieto to nevienādībā", "salīdzina ar robežu",
               "uzzīmē grafiku", "saskaita puses"], 0),
             ("Ko nozīmē tukša atrisinājumu kopa?",
              ["nav neviena atrisinājuma", "visi skaitļi der",
               "ir viens atrisinājums", "kopa nav noteikta"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 9,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "9. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.9. temata noslēgumā. "
                "Pārbauda lineāras nevienādības atrisināšanu, intervāla "
                "pierakstu, nevienādību sistēmu un situāciju aprakstu ar "
                "nevienādību.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina nevienādības jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir nevienādības atrisinājums?",
              ["skaitlis, ar kuru nevienādība ir patiesa",
               "jebkurš skaitlis", "koeficients", "nezināmais"], 0),
             ("Ko nozīmē atrisināt nevienādību?",
              ["noteikt visu atrisinājumu kopu", "atrast vienu skaitli",
               "pārrakstīt nevienādību", "uzzīmēt grafiku"], 0),
             ("Kas notiek, ja abas puses reizina ar negatīvu skaitli?",
              ["zīmi maina uz pretējo", "zīme nemainās",
               "nevienādība kļūst aplama", "atrisinājums pazūd"], 0),
             ("Kas ir skaitļu intervāls?",
              ["skaitļu taisnes daļa", "viens skaitlis",
               "divu skaitļu summa", "kopu apvienojums"], 0),
             ("Kad nevienādības ir ekvivalentas?",
              ["ja atrisinājumu kopas sakrīt", "ja tās izskatās vienādi",
               "ja tām ir viens nezināmais", "ja robežas ir veselas"], 0),
             ("Ar kuru zīmi pieraksta «ne vairāk kā»?",
              ["≤", "≥", "<", ">"], 0),
             ("Ko nozīmē tukša atrisinājumu kopa?",
              ["nav neviena atrisinājuma", "visi skaitļi der",
               "ir viens atrisinājums", "kopa nav noteikta"], 0),
             ("Kāds ir sistēmas atrisinājums?",
              ["abu kopu šķēlums", "abu kopu apvienojums",
               "pirmās kopas daļa", "tukša kopa"], 0),
         ]},
        {"sr": "Atrisina vienkāršas nevienādības",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(vienkarsa, [
             (6, 8), (4, 11), (-5, 14), (9, 7), (-8, 17), (12, 5), (-10, 22)])
             + V.kopa(negativs, [
                 (3, 5), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4), (9, 6),
                 (10, 3)])),
         },
        {"sr": "Atrisina lineāru nevienādību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nevienadiba, [
             (3, 4, 5), (4, -2, 6), (5, 3, 4), (6, -5, 7), (2, 9, 3),
             (7, 1, 5), (8, -3, 2), (9, 4, 6), (10, -1, 4), (11, 2, 3),
             (12, -6, 5), (13, 3, 2), (14, -2, 4), (15, 5, 3), (16, 1, 6)]),
         },
        {"sr": "Pieraksta atrisinājumu ar intervālu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(intervals, [
             (1, 6), (2, 9), (3, 11), (0, 8), (4, 12), (5, 14), (6, 15),
             (1, 10), (7, 16), (2, 13), (8, 19), (3, 17), (9, 20),
             (4, 18), (10, 21)]),
         },
        {"sr": "Atrisina nevienādību sistēmu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sistema, [
             (1, 6), (2, 9), (3, 11), (0, 8), (4, 12), (5, 14), (6, 15),
             (1, 10), (7, 16), (2, 13), (8, 19), (3, 17), (9, 20),
             (4, 18), (10, 21)]),
         },
        {"sr": "Apraksta situāciju ar nevienādību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru nevienādību pieraksta «x ir vismaz 12»?",
              ["x ≥ 12", "x > 12", "x ≤ 12", "x < 12"], 0),
             ("Ar kuru nevienādību pieraksta «x nepārsniedz 25»?",
              ["x ≤ 25", "x < 25", "x ≥ 25", "x > 25"], 0),
             ("Somā drīkst būt ne vairāk kā 10 kg. Kā to pieraksta?",
              ["m ≤ 10", "m < 10", "m ≥ 10", "m > 10"], 0),
             ("Biļete maksā 6 eiro; ir 50 eiro. Cik biļešu var nopirkt?",
              ["ne vairāk kā 8", "vismaz 8", "tieši 50",
               "ne vairāk kā 6"], 0),
             ("Ar kuru nevienādību pieraksta «x ir no 2 līdz 9»?",
              ["2 ≤ x ≤ 9", "2 < x < 9", "x > 2", "x < 9"], 0),
             ("Kura izteiksme ir lielāka: x vai x + 4?",
              ["x + 4", "x", "tās ir vienādas", "atkarīgs no x"], 0),
             ("Kura izteiksme ir lielāka: 2x vai 5x, ja x > 0?",
              ["5x", "2x", "tās ir vienādas", "nevar noteikt"], 0),
             ("Ko nozīmē intervāls (−∞; 4]?",
              ["x ≤ 4", "x < 4", "x ≥ 4", "x > 4"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Atrisina nevienādības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Atrisini nevienādību",
             lambda a, b, x, c: [
                 ("x + %d < %d;   ……" % (b, x + b), "x < %s" % V.sk(x)),
                 ("%dx > %d;   ……" % (a, a * x), "x > %s" % V.sk(x)),
                 ("%dx + %d > %d;   ……" % (a, b, a * x + b),
                  "x > %s" % V.sk(x)),
                 ("−%dx > %d;   ……" % (a, -a * c), "x < %s" % V.sk(c))],
             [(2, 3, 4, 5), (3, 5, 6, 2), (4, 2, 5, 3), (5, 7, 3, 4),
              (6, 4, 7, 2), (7, 1, 8, 5), (8, 6, 2, 3), (9, 3, 5, 6),
              (10, 8, 4, 2), (11, 2, 6, 4), (12, 5, 3, 7), (13, 7, 2, 3),
              (14, 4, 5, 2), (15, 9, 4, 5), (16, 3, 6, 4)]),
         },
        {"sr": "Pieraksta atrisinājumu ar intervālu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Intervāli",
             lambda a, b: [
                 ("x > %d;   intervāls ……" % a, "(%d; +∞)" % a),
                 ("x ≤ %d;   intervāls ……" % b, "(−∞; %d]" % b),
                 ("%d < x < %d;   intervāls ……" % (a, b),
                  "(%d; %d)" % (a, b))],
             [(2, 7), (1, 5), (3, 8), (0, 6), (4, 9), (2, 10), (5, 11),
              (1, 8), (6, 12), (3, 13), (7, 14), (2, 15), (8, 16),
              (4, 17), (9, 18)]),
         },
        {"sr": "Risina situāciju uzdevumu ar nevienādību",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situācija un nevienādība",
             lambda cena, nauda, papild: {
                 "teksts": "Ieva grib nopirkt burtnīcas pa %d eiro un vienu "
                           "pildspalvu par %d eiro; viņai ir %d eiro.   "
                           "a) Apzīmē burtnīcu skaitu ar x un uzraksti "
                           "nevienādību!   b) Atrisini to!   c) Cik "
                           "burtnīcu viņa var nopirkt?   d) Cik naudas "
                           "atliks?" % (cena, papild, nauda),
                 "kriteriji": [
                     "a) %dx + %d ≤ %d.   (1 p.)" % (cena, papild, nauda),
                     "b) %dx ≤ %d,  x ≤ %s.   (1 p.)"
                     % (cena, nauda - papild,
                        V.dalu(nauda - papild, cena)),
                     "c) %d burtnīcas.   (1 p.)" % ((nauda - papild) // cena),
                     "d) %d − %d = %d eiro.   (1 p.)"
                     % (nauda, cena * ((nauda - papild) // cena) + papild,
                        nauda - cena * ((nauda - papild) // cena) - papild)]},
             [(3, 20, 2), (4, 30, 5), (5, 40, 3), (2, 25, 4), (6, 50, 7),
              (7, 45, 2), (8, 60, 6), (9, 70, 5), (3, 35, 8), (10, 80, 4),
              (11, 90, 3), (4, 55, 9), (12, 100, 7), (5, 65, 6),
              (13, 110, 5)]),
         },
        {"sr": "Pamato nevienādības risinājumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Nevienādības pārveidojumi",
             lambda a, x: {
                 "ievads": "Dota nevienādība  −%dx > %d." % (a, -a * x),
                 "jaut": [("Ar ko dalīsi abas puses?", 1),
                          ("Atrisini nevienādību!", 1),
                          ("Paskaidro, kāpēc zīme mainās!", 1)],
                 "atbildes": [
                     "1) Ar −%d.   (1 p.)" % a,
                     "2) x < %s.   (1 p.)" % V.sk(x),
                     "3) Dalot ar negatīvu skaitli, nevienādības zīmi maina "
                     "uz pretējo.   (1 p.)"]},
             [(2, 3), (3, 4), (4, 2), (5, 6), (6, 1), (7, 5), (8, 3),
              (9, 2), (10, 7), (11, 4), (12, 5), (13, 2), (14, 6),
              (15, 3), (16, 4)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
