# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.4. Funkcijas, kuru grafiks ir taisne.

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.4. temats): funkcija,
arguments un funkcijas vērtība, funkcijas uzdošana ar formulu un grafiku,
lineāra funkcija y = kx + b, koeficientu k un b nozīme, augoša un dilstoša
funkcija, krustpunkti ar asīm, funkcijas vērtības zīme un punkta piederība
grafikam.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.4."
NOSAUKUMS = "Kā pieraksta un pēta funkcijas, kuru grafiks ir taisne?"

ATGADNE = [
    "Lineāra funkcija:   y = kx + b   ·   grafiks ir taisne   ·   k > 0 — "
    "funkcija augoša, k < 0 — dilstoša   ·   b ir krustpunkta ordināta ar "
    "y asi.",
    "Krustpunkts ar y asi:   x = 0,   y = b   ·   krustpunkts ar x asi:   "
    "y = 0,   x = −{b|k}",
    "Punkts pieder grafikam, ja, ievietojot tā koordinātas formulā, iegūst "
    "patiesu vienādību.",
]


# ---------------------------------------------------------------- veidnes
def vertiba(k, b, x):
    zime = "+" if b >= 0 else "−"
    return ("y = %sx %s %d. Cik liels ir y, ja x = %d?"
            % (V.iek(k), zime, abs(b), x),
            V.izvele(k * x + b, k * x - b, k + x + b, k * x,
                     (k + b) * x, k * x + b + 1, k * (x + b)), 0)


def arguments(k, b, y):
    """No funkcijas vērtības nosaka argumentu, ja y = kx + b."""
    zime = "+" if b >= 0 else "−"
    x = (y - b) // k
    return ("y = %sx %s %d. Cik liels ir x, ja y = %d?"
            % (V.iek(k), zime, abs(b), y),
            V.izvele(x, -x, y - b, (y + b) // k if k else 0, x + 1,
                     y // k, x - 1), 0)


def augosa(k, b):
    zime = "+" if b >= 0 else "−"
    return ("Vai funkcija  y = %sx %s %d  ir augoša vai dilstoša?"
            % (V.iek(k), zime, abs(b)),
            V.izvele("augoša" if k > 0 else "dilstoša",
                     "dilstoša" if k > 0 else "augoša",
                     "ne augoša, ne dilstoša", "nevar noteikt"), 0)


def y_ass(k, b):
    zime = "+" if b >= 0 else "−"
    return ("Kurā punktā funkcijas  y = %sx %s %d  grafiks krusto y asi?"
            % (V.iek(k), zime, abs(b)),
            V.izvele("(0; %s)" % V.sk(b), "(%s; 0)" % V.sk(b),
                     "(0; %s)" % V.sk(k), "(%s; 0)" % V.sk(k),
                     "(0; 0)", "(%s; %s)" % (V.sk(k), V.sk(b))), 0)


def x_ass(k, b):
    """Krustpunkts ar x asi; b izvēlēts tā, lai dalījums būtu vesels."""
    zime = "+" if b >= 0 else "−"
    x = -b // k
    return ("Kurā punktā funkcijas  y = %sx %s %d  grafiks krusto x asi?"
            % (V.iek(k), zime, abs(b)),
            V.izvele("(%s; 0)" % V.sk(x), "(0; %s)" % V.sk(x),
                     "(%s; 0)" % V.sk(-x), "(%s; 0)" % V.sk(b),
                     "(0; %s)" % V.sk(b), "(0; 0)"), 0)


def pieder(k, b, x, y):
    """Vai punkts pieder grafikam - pārbauda, ievietojot koordinātas."""
    zime = "+" if b >= 0 else "−"
    ir = (k * x + b == y)
    return ("Vai punkts (%d; %d) pieder funkcijas  y = %sx %s %d  grafikam?"
            % (x, y, V.iek(k), zime, abs(b)),
            V.izvele("jā" if ir else "nē", "nē" if ir else "jā",
                     "tikai ja x = 0", "nevar noteikt"), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.4. temata beigās. Pārbauda funkcijas "
                "jēdzienu, lineāras funkcijas formulu un grafiku, "
                "koeficientu nozīmi, krustpunktus ar asīm un punkta "
                "piederību grafikam.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina funkcijas jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad sakarību sauc par funkciju?",
              ["ja katram argumentam atbilst tieši viena vērtība",
               "ja grafiks ir taisne", "ja formulā ir x",
               "ja vērtības ir pozitīvas"], 0),
             ("Kā vēl sauc neatkarīgo mainīgo?",
              ["arguments", "funkcijas vērtība", "koeficients",
               "krustpunkts"], 0),
             ("Kā vēl sauc atkarīgo mainīgo?",
              ["funkcijas vērtība", "arguments", "koeficients",
               "krustpunkts"], 0),
             ("Kas veido funkcijas grafiku?",
              ["visi punkti (arguments; funkcijas vērtība)",
               "tikai divi punkti", "asis", "formulas burti"], 0),
             ("Kad saka, ka funkcija ir uzdota?",
              ["kad zināms, kā aprēķina vērtību", "kad uzzīmēts grafiks",
               "kad ir tabula", "kad ir divi punkti"], 0),
             ("Vai taisne x = 3 attēlo funkciju?",
              ["nē", "jā", "tikai ar tabulu", "tikai ar grafiku"], 0),
             ("Vai taisne y = 3 attēlo funkciju?",
              ["jā", "nē", "tikai ar tabulu", "tikai ar grafiku"], 0),
             ("Ar ko apzīmē funkcijas vērtību?",
              ["y", "x", "k", "b"], 0),
         ]},
        {"sr": "Zina lineāras funkcijas formulu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda ir lineāras funkcijas formula?",
              ["y = kx + b", "y = x²", "y = {k|x}", "y = √x"], 0),
             ("Kāds ir lineāras funkcijas grafiks?",
              ["taisne", "parabola", "riņķa līnija", "hiperbola"], 0),
             ("Kā sauc skaitļus k un b?",
              ["koeficienti", "argumenti", "vērtības", "krustpunkti"], 0),
             ("Kura funkcija ir lineāra?",
              ["y = 3x − 5", "y = x²", "y = {6|x}", "y = √x"], 0),
             ("Kura funkcija nav lineāra?",
              ["y = x²", "y = 2x", "y = −x + 1", "y = 4"], 0),
             ("Kāda funkcija apraksta tieši proporcionālus lielumus?",
              ["y = kx", "y = kx + b, b ≠ 0", "y = {k|x}", "y = x²"], 0),
             ("Cik punktu pietiek, lai uzzīmētu taisni?",
              ["divi", "viens", "trīs", "bezgalīgi daudz"], 0),
             ("Ko rāda koeficients b?",
              ["kur grafiks krusto y asi", "grafika slīpumu",
               "grafika garumu", "argumenta vērtību"], 0),
         ]},
        {"sr": "Aprēķina funkcijas vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vertiba, [
             (2, 3, 4), (3, -1, 5), (-2, 7, 3), (4, 2, 6), (-3, 5, 2),
             (5, -4, 3), (2, -6, 8), (-4, 1, 5), (6, 3, 2), (-5, 9, 4),
             (7, -2, 3), (3, 8, 7), (-6, 4, 5), (8, -3, 2), (-7, 6, 3)]),
         },
        {"sr": "Nosaka argumentu pēc funkcijas vērtības",
         "stunda": TEMATS,
         "jautajumi": V.kopa(arguments, [
             (2, 3, 11), (3, -1, 14), (4, 2, 22), (5, -3, 22), (2, 7, 17),
             (6, 1, 25), (3, 5, 20), (7, -2, 33), (4, -5, 23), (8, 3, 35),
             (5, 4, 29), (9, -1, 35), (6, -4, 32), (10, 2, 42), (3, 8, 26)]),
         },
        {"sr": "Nosaka, vai funkcija ir augoša vai dilstoša",
         "stunda": TEMATS,
         "jautajumi": V.kopa(augosa, [
             (2, 3), (-3, 1), (4, -2), (-5, 4), (6, 0), (-2, 7), (3, -6),
             (-4, 2), (7, 5), (-6, 3), (5, -1), (-7, 8), (8, 4), (-8, 6),
             (9, -3)]),
         },
        {"sr": "Nosaka krustpunktu ar ordinātu asi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(y_ass, [
             (2, 3), (3, -4), (-2, 5), (4, 6), (-3, -7), (5, 2), (6, -1),
             (-4, 8), (7, 9), (-5, -2), (8, 4), (9, -6), (-6, 3), (10, 7),
             (-7, -5)]),
         },
        {"sr": "Nosaka krustpunktu ar abscisu asi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(x_ass, [
             (2, -6), (3, 9), (4, -8), (5, 10), (-2, 8), (6, -12),
             (-3, 9), (7, 14), (8, -16), (-4, 12), (9, 18), (10, -20),
             (-5, 15), (11, 22), (12, -24)]),
         },
        {"sr": "Pārbauda punkta piederību grafikam",
         "stunda": TEMATS,
         "jautajumi": V.kopa(pieder, [
             (2, 3, 4, 11), (3, -1, 5, 14), (2, 1, 3, 8), (4, 2, 3, 15),
             (5, -2, 4, 18), (2, 5, 6, 17), (3, 4, 2, 10), (6, -3, 2, 9),
             (7, 1, 3, 22), (4, -5, 5, 15), (8, 2, 2, 18), (9, -4, 3, 22),
             (5, 6, 4, 26), (10, 1, 2, 20), (3, 7, 5, 22)]),
         },
        {"sr": "Saista koeficientus ar grafika novietojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē k > 0?",
              ["funkcija ir augoša", "funkcija ir dilstoša",
               "grafiks ir horizontāls", "grafiks iet caur sākumpunktu"], 0),
             ("Ko nozīmē k < 0?",
              ["funkcija ir dilstoša", "funkcija ir augoša",
               "grafiks ir horizontāls", "grafiks iet caur sākumpunktu"], 0),
             ("Ko nozīmē b = 0?",
              ["grafiks iet caur sākumpunktu", "grafiks ir horizontāls",
               "funkcija ir dilstoša", "funkcijas nav"], 0),
             ("Ko nozīmē k = 0?",
              ["grafiks ir horizontāla taisne", "grafiks ir vertikāls",
               "funkcija ir augoša", "funkcijas nav"], 0),
             ("Kurš grafiks ir stāvāks?",
              ["y = 5x", "y = 2x", "y = x", "y = 0,5x"], 0),
             ("Kuras funkcijas grafiks iet caur sākumpunktu?",
              ["y = 3x", "y = 3x + 1", "y = 3", "y = x − 2"], 0),
             ("Divām paralēlām taisnēm ir vienāds...",
              ["koeficients k", "koeficients b", "krustpunkts",
               "garums"], 0),
             ("Ko rāda koeficients k?",
              ["cik strauji mainās funkcijas vērtība", "grafika garumu",
               "krustpunktu ar y asi", "argumenta vērtību"], 0),
         ]},
        {"sr": "Nosaka funkcijas vērtības zīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("y = 2x − 6. Kāda ir y zīme, ja x = 5?",
              ["pozitīva", "negatīva", "nulle", "nevar noteikt"], 0),
             ("y = 2x − 6. Kāda ir y zīme, ja x = 1?",
              ["negatīva", "pozitīva", "nulle", "nevar noteikt"], 0),
             ("y = 2x − 6. Ar kuru x vērtību y = 0?",
              ["x = 3", "x = 6", "x = −3", "x = 2"], 0),
             ("y = −3x + 9. Kāda ir y zīme, ja x = 4?",
              ["negatīva", "pozitīva", "nulle", "nevar noteikt"], 0),
             ("y = −3x + 9. Ar kuru x vērtību y = 0?",
              ["x = 3", "x = 9", "x = −3", "x = −9"], 0),
             ("y = x + 4. Ar kurām x vērtībām y > 0?",
              ["x > −4", "x < −4", "x > 4", "x < 4"], 0),
             ("Kur grafiks atrodas virs x ass?",
              ["kur funkcijas vērtība ir pozitīva",
               "kur vērtība ir negatīva", "kur x ir pozitīvs",
               "kur x ir negatīvs"], 0),
             ("Kur grafiks atrodas zem x ass?",
              ["kur funkcijas vērtība ir negatīva",
               "kur vērtība ir pozitīva", "kur x ir pozitīvs",
               "kur x ir negatīvs"], 0),
         ]},
        {"sr": "Lasa grafiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā no grafika nolasa funkcijas vērtību, ja zināms x?",
              ["no x iet uz augšu līdz grafikam", "no x iet pa labi",
               "mēra grafika garumu", "saskaita koordinātas"], 0),
             ("Kā no grafika nolasa argumentu, ja zināms y?",
              ["no y iet pa labi līdz grafikam", "no y iet uz augšu",
               "mēra grafika garumu", "saskaita koordinātas"], 0),
             ("Ko rāda grafika krustpunkts ar x asi?",
              ["argumentu, ar kuru y = 0", "funkcijas lielāko vērtību",
               "koeficientu k", "grafika garumu"], 0),
             ("Ko rāda grafika krustpunkts ar y asi?",
              ["funkcijas vērtību, ja x = 0", "argumentu, ar kuru y = 0",
               "koeficientu k", "grafika slīpumu"], 0),
             ("Divu taišņu krustpunkts rāda, ka...",
              ["abām funkcijām ir vienāda vērtība", "viena taisne beidzas",
               "koeficienti ir vienādi", "grafiks ir nepareizs"], 0),
             ("Kurš grafiks ir dilstošai funkcijai?",
              ["taisne, kas krīt pa labi", "taisne, kas kāpj pa labi",
               "horizontāla taisne", "vertikāla taisne"], 0),
             ("Cik punktus pietiek atlikt, zīmējot taisni?",
              ["divus", "vienu", "piecus", "desmit"], 0),
             ("Kāpēc grafiku zīmē precīzi?",
              ["neprecizitāte dod aplamus secinājumus", "lai būtu skaisti",
               "lai aizpildītu lapu", "tas nav svarīgi"], 0),
         ]},
        {"sr": "Lieto lineāru funkciju kā modeli",
         "stunda": TEMATS,
         "jautajumi": [
             ("Telpas īre 100 eiro un 20 eiro par dalībnieku. Ar kuru "
              "formulu aprēķina izmaksas?",
              ["y = 20x + 100", "y = 100x + 20", "y = 120x",
               "y = 20x − 100"], 0),
             ("Tajā pašā situācijā — cik maksās 10 dalībnieki?",
              ["300 eiro", "200 eiro", "1020 eiro", "120 eiro"], 0),
             ("Taksometrs: 3 eiro un 1 eiro par km. Formula?",
              ["y = x + 3", "y = 3x + 1", "y = 4x", "y = 3x"], 0),
             ("Tajā pašā situācijā — cik maksās 12 km?",
              ["15 eiro", "37 eiro", "48 eiro", "36 eiro"], 0),
             ("Ko šajās formulās rāda koeficients b?",
              ["pastāvīgo daļu", "maksu par vienību", "kopējo summu",
               "vienību skaitu"], 0),
             ("Ko šajās formulās rāda koeficients k?",
              ["maksu par vienu vienību", "pastāvīgo daļu",
               "kopējo summu", "vienību skaitu"], 0),
             ("Krājumā 500 eiro; katru mēnesi pieliek 50 eiro. Formula?",
              ["y = 50x + 500", "y = 500x + 50", "y = 550x",
               "y = 500 − 50x"], 0),
             ("Tajā pašā situācijā — cik būs pēc 6 mēnešiem?",
              ["800 eiro", "550 eiro", "3300 eiro", "3000 eiro"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 4,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "4. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.4. temata noslēgumā. "
                "Pārbauda lineāras funkcijas formulu un grafiku, vērtību un "
                "argumenta noteikšanu, krustpunktus ar asīm un koeficientu "
                "nozīmi.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina funkcijas un lineāras funkcijas jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad sakarību sauc par funkciju?",
              ["ja katram argumentam atbilst tieši viena vērtība",
               "ja grafiks ir taisne", "ja formulā ir x",
               "ja vērtības ir pozitīvas"], 0),
             ("Kāda ir lineāras funkcijas formula?",
              ["y = kx + b", "y = x²", "y = {k|x}", "y = √x"], 0),
             ("Kāds ir lineāras funkcijas grafiks?",
              ["taisne", "parabola", "riņķa līnija", "hiperbola"], 0),
             ("Kā vēl sauc neatkarīgo mainīgo?",
              ["arguments", "funkcijas vērtība", "koeficients",
               "krustpunkts"], 0),
             ("Kura funkcija nav lineāra?",
              ["y = x²", "y = 2x", "y = −x + 1", "y = 4"], 0),
             ("Cik punktu pietiek, lai uzzīmētu taisni?",
              ["divi", "viens", "trīs", "bezgalīgi daudz"], 0),
             ("Vai taisne x = 5 attēlo funkciju?",
              ["nē", "jā", "tikai ar tabulu", "tikai ar grafiku"], 0),
             ("Kāda funkcija apraksta tieši proporcionālus lielumus?",
              ["y = kx", "y = kx + b, b ≠ 0", "y = {k|x}", "y = x²"], 0),
         ]},
        {"sr": "Aprēķina funkcijas vērtību un argumentu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(vertiba, [
             (3, 2, 5), (-4, 6, 3), (5, -3, 4), (2, 9, 7), (-6, 1, 2),
             (7, -5, 3), (-3, 8, 6)])
             + V.kopa(arguments, [
                 (2, 5, 17), (3, -2, 19), (4, 3, 27), (5, 1, 26),
                 (6, -4, 32), (7, 2, 37), (8, -1, 39), (9, 5, 50)])),
         },
        {"sr": "Nosaka, vai funkcija ir augoša vai dilstoša",
         "stunda": TEMATS,
         "jautajumi": V.kopa(augosa, [
             (3, 2), (-2, 5), (5, -3), (-6, 1), (7, 4), (-3, 8), (4, -7),
             (-5, 2), (8, 6), (-7, 3), (6, -2), (-8, 9), (9, 5), (-9, 7),
             (10, -4)]),
         },
        {"sr": "Nosaka krustpunktus ar asīm",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(y_ass, [
             (3, 4), (-2, 6), (5, -3), (4, 7), (-6, -2), (7, 1), (8, -5)])
             + V.kopa(x_ass, [
                 (2, -10), (3, 12), (4, -12), (5, 15), (-2, 10), (6, -18),
                 (7, 21), (8, -24)])),
         },
        {"sr": "Pārbauda punkta piederību grafikam",
         "stunda": TEMATS,
         "jautajumi": V.kopa(pieder, [
             (2, 1, 3, 7), (3, 2, 4, 14), (4, -1, 2, 8), (5, 3, 2, 13),
             (2, -4, 5, 6), (6, 1, 3, 20), (3, 5, 4, 17), (7, -2, 2, 12),
             (8, 3, 1, 11), (4, 6, 3, 18), (9, -1, 2, 17), (5, 2, 5, 27),
             (10, 4, 1, 14), (6, -5, 4, 19), (3, 9, 2, 15)]),
         },
        {"sr": "Saista koeficientus ar grafiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē k > 0?",
              ["funkcija ir augoša", "funkcija ir dilstoša",
               "grafiks ir horizontāls", "grafiks iet caur sākumpunktu"], 0),
             ("Ko nozīmē b = 0?",
              ["grafiks iet caur sākumpunktu", "grafiks ir horizontāls",
               "funkcija ir dilstoša", "funkcijas nav"], 0),
             ("Kurš grafiks ir stāvāks?",
              ["y = 6x", "y = 3x", "y = x", "y = 0,5x"], 0),
             ("Divām paralēlām taisnēm ir vienāds...",
              ["koeficients k", "koeficients b", "krustpunkts",
               "garums"], 0),
             ("Ko rāda grafika krustpunkts ar x asi?",
              ["argumentu, ar kuru y = 0", "funkcijas lielāko vērtību",
               "koeficientu k", "grafika garumu"], 0),
             ("y = 2x − 8. Ar kuru x vērtību y = 0?",
              ["x = 4", "x = 8", "x = −4", "x = 2"], 0),
             ("y = x + 5. Ar kurām x vērtībām y > 0?",
              ["x > −5", "x < −5", "x > 5", "x < 5"], 0),
             ("Kurš grafiks ir dilstošai funkcijai?",
              ["taisne, kas krīt pa labi", "taisne, kas kāpj pa labi",
               "horizontāla taisne", "vertikāla taisne"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina vērtības un krustpunktus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Lineāra funkcija  y = kx + b",
             lambda k, b, x1, x2: [
                 ("k = %d,  b = %d;  ja x = %d, tad y = ……" % (k, b, x1),
                  V.sk(k * x1 + b)),
                 ("k = %d,  b = %d;  ja x = %d, tad y = ……" % (k, b, x2),
                  V.sk(k * x2 + b)),
                 ("Krustpunkts ar y asi:   ……", "(0; %s)" % V.sk(b)),
                 ("Krustpunkts ar x asi:   ……",
                  "(%s; 0)" % V.dalu(-b, k))],
             [(2, -6, 3, 5), (3, 9, 2, 4), (4, -8, 1, 6), (5, 10, 3, 7),
              (-2, 8, 2, 5), (6, -12, 4, 3), (-3, 9, 1, 4), (7, 14, 2, 6),
              (8, -16, 3, 5), (-4, 12, 2, 7), (9, 18, 1, 3), (10, -20, 4, 2),
              (-5, 15, 3, 6), (11, 22, 2, 5), (12, -24, 3, 4)]),
         },
        {"sr": "Pēta funkcijas īpašības",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Funkcijas īpašības",
             lambda k, b, x, y: [
                 ("y = %sx + %s  ir ……  (augoša vai dilstoša)"
                  % (V.iek(k), V.sk(b)),
                  "augoša" if k > 0 else "dilstoša"),
                 ("Vai punkts (%d; %d) pieder grafikam?   ……" % (x, y),
                  "jā" if k * x + b == y else "nē"),
                 ("Funkcijas vērtība, ja x = 0:   y = ……", V.sk(b))],
             [(2, 3, 4, 11), (-3, 5, 2, 1), (4, -1, 3, 11), (5, 2, 2, 12),
              (-2, 7, 3, 1), (6, -4, 2, 8), (3, 6, 4, 18), (-5, 9, 1, 4),
              (7, 1, 2, 15), (8, -3, 3, 21), (-4, 8, 2, 0), (9, 4, 1, 13),
              (10, -5, 2, 15), (-6, 11, 1, 5), (11, 2, 3, 35)]),
         },
        {"sr": "Lieto lineāru funkciju kā situācijas modeli",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situācijas matemātiskais modelis",
             lambda b, k, n, summa: {
                 "teksts": "Par telpas īri jāmaksā %d eiro un vēl %d eiro "
                           "par katru dalībnieku.   a) Pieraksti izmaksas "
                           "y ar formulu, ja dalībnieku ir x!   b) Cik "
                           "maksās pasākums ar %d dalībniekiem?   c) Cik "
                           "dalībnieku var uzaicināt par %d eiro?   d) Ko "
                           "šajā formulā rāda koeficients k?"
                           % (b, k, n, summa),
                 "kriteriji": [
                     "a) y = %dx + %d.   (1 p.)" % (k, b),
                     "b) %d · %d + %d = %d eiro.   (1 p.)"
                     % (k, n, b, k * n + b),
                     "c) (%d − %d) : %d = %d dalībnieki.   (1 p.)"
                     % (summa, b, k, (summa - b) // k),
                     "d) Maksu par vienu dalībnieku — %d eiro.   (1 p.)"
                     % k]},
             [(100, 20, 10, 500), (150, 25, 8, 650), (200, 30, 12, 800),
              (120, 15, 20, 600), (180, 40, 6, 700), (90, 10, 25, 390),
              (250, 50, 9, 950), (160, 20, 15, 560), (140, 35, 7, 630),
              (220, 45, 11, 985), (110, 30, 14, 620), (300, 60, 5, 1080),
              (130, 25, 18, 730), (170, 55, 8, 720), (240, 80, 6, 960)]),
         },
        {"sr": "Skaidro grafika novietojumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Funkcijas grafiks",
             lambda k, b: {
                 "ievads": "Dota funkcija  y = %sx + %s."
                           % (V.iek(k), V.sk(b)),
                 "jaut": [("Uzraksti divus punktus, kas pieder grafikam!",
                           1),
                          ("Vai funkcija ir augoša vai dilstoša? Pamato!",
                           1),
                          ("Kurā punktā grafiks krusto y asi?", 1)],
                 "atbildes": [
                     "1) Piemēram, (0; %s) un (1; %s).   (1 p.)"
                     % (V.sk(b), V.sk(k + b)),
                     "2) %s, jo k %s 0.   (1 p.)"
                     % ("Augoša" if k > 0 else "Dilstoša",
                        ">" if k > 0 else "<"),
                     "3) (0; %s).   (1 p.)" % V.sk(b)]},
             [(2, 3), (-3, 5), (4, -2), (5, 1), (-2, 7), (6, -4), (3, 8),
              (-5, 9), (7, 2), (8, -6), (-4, 11), (9, 4), (10, -3),
              (-6, 13), (11, 5)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
