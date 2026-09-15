# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.7. Kā dažādas funkcijas izmanto modelēšanai?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.7. temats): kvadrātfunkcija un
parabola, funkcija y = {k|x} un hiperbola, grafiku forma un simetrija,
parabolas virsotne, funkcijas vērtību apgabals, lielākā un mazākā vērtība,
augšanas un dilšanas intervāli, krustpunkti ar asīm un vienādojuma x² = t
atrisināšana.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.7."
NOSAUKUMS = "Kā dažādas funkcijas izmanto matemātiskai modelēšanai?"

ATGADNE = [
    "Kvadrātfunkcijas y = ax² + c grafiks ir parabola: ja a > 0, zari vērsti "
    "uz augšu un funkcijai ir mazākā vērtība; ja a < 0 — uz leju.",
    "Funkcijas y = ax² virsotne ir (0; 0), funkcijai y = ax² + c — (0; c); "
    "parabola ir simetriska pret ordinātu asi.",
    "Funkcijas y = {k|x} grafiks ir hiperbola; x ≠ 0. Vienādojumam x² = t "
    "ir divas saknes  x = ±√t,  ja t > 0, viena sakne, ja t = 0, un nav "
    "sakņu, ja t < 0.",
]


# ---------------------------------------------------------------- veidnes
def kvadrat_vertiba(a, c, x):
    """Kvadrātfunkcijas y = ax² + c vērtība."""
    zime = "+" if c >= 0 else "−"
    return ("y = %sx² %s %d. Cik liels ir y, ja x = %d?"
            % (V.iek(a), zime, abs(c), x),
            V.izvele(a * x * x + c, a * x + c, (a * x) ** 2 + c,
                     a * x * x - c, a * x * x, a * x * x + c + 1), 0)


def hiperbola_vertiba(k, x):
    """Funkcijas y = {k|x} vērtība."""
    return ("y = {%d|x}. Cik liels ir y, ja x = %d?" % (k, x),
            V.izvele(V.dalu(k, x), V.dalu(x, k), k * x, k - x,
                     V.dalu(k, x) if k % x else k // x + 1,
                     V.dalu(k, x + 1)), 0)


def virsotne(a, c):
    """Parabolas y = ax² + c virsotne."""
    zime = "+" if c >= 0 else "−"
    return ("Kur atrodas funkcijas  y = %sx² %s %d  grafika virsotne?"
            % (V.iek(a), zime, abs(c)),
            V.izvele("(0; %s)" % V.sk(c), "(%s; 0)" % V.sk(c),
                     "(0; %s)" % V.sk(a), "(%s; 0)" % V.sk(a),
                     "(0; 0)", "(%s; %s)" % (V.sk(a), V.sk(c))), 0)


def zari(a, c):
    """Uz kuru pusi vērsti parabolas zari."""
    zime = "+" if c >= 0 else "−"
    return ("Uz kuru pusi vērsti funkcijas  y = %sx² %s %d  grafika zari?"
            % (V.iek(a), zime, abs(c)),
            V.izvele("uz augšu" if a > 0 else "uz leju",
                     "uz leju" if a > 0 else "uz augšu",
                     "pa labi", "pa kreisi"), 0)


def x_kvadrata(t):
    """Vienādojums x² = t: divas saknes, viena vai neviena."""
    n = int(round(abs(t) ** 0.5))
    divas = "x = %d  vai  x = −%d" % (n, n)
    if t > 0:
        atbildes = (divas, "x = %d" % n, "x = −%d" % n, "sakņu nav",
                    "x = %s" % V.sk(t))
    elif t == 0:
        atbildes = ("x = 0", "x = 0  vai  x = 1", "sakņu nav",
                    "bezgalīgi daudz sakņu")
    else:
        atbildes = ("sakņu nav", divas, "x = %d" % n, "x = 0",
                    "x = %s" % V.sk(t))
    return ("Atrisini vienādojumu  x² = %s." % V.sk(t),
            V.izvele(*atbildes), 0)


def mazaka(a, c):
    """Kvadrātfunkcijas lielākā vai mazākā vērtība."""
    zime = "+" if c >= 0 else "−"
    ir_maz = a > 0
    return ("Kāda ir funkcijas  y = %sx² %s %d  %s vērtība?"
            % (V.iek(a), zime, abs(c),
               "mazākā" if ir_maz else "lielākā"),
            V.izvele(V.sk(c), V.sk(-c), V.sk(a), "0",
                     V.sk(a + c), V.sk(c + 1)), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.7. temata beigās. Pārbauda "
                "kvadrātfunkciju un parabolu, funkciju y = {k|x} un "
                "hiperbolu, grafika īpašības un vienādojuma x² = t "
                "atrisināšanu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina funkciju veidus un to grafikus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir kvadrātfunkcijas grafiks?",
              ["parabola", "taisne", "hiperbola", "riņķa līnija"], 0),
             ("Kāds ir funkcijas y = {k|x} grafiks?",
              ["hiperbola", "parabola", "taisne", "riņķa līnija"], 0),
             ("Kāds ir lineāras funkcijas grafiks?",
              ["taisne", "parabola", "hiperbola", "riņķa līnija"], 0),
             ("Kura funkcija ir kvadrātfunkcija?",
              ["y = 2x² + 1", "y = 2x + 1", "y = {2|x}", "y = √x"], 0),
             ("Kura funkcija nav kvadrātfunkcija?",
              ["y = {3|x}", "y = x²", "y = −x² + 4", "y = 3x²"], 0),
             ("Pret kuru asi ir simetriska parabola y = ax²?",
              ["pret ordinātu asi", "pret abscisu asi",
               "pret abām asīm", "ne pret vienu"], 0),
             ("Kāda vērtība nav atļauta funkcijai y = {k|x}?",
              ["x = 0", "x = 1", "x = −1", "x = k"], 0),
             ("Vai katra liekta simetriska līnija ir parabola?",
              ["nē", "jā", "tikai ar virsotni", "vienmēr"], 0),
         ]},
        {"sr": "Nosaka parabolas zaru virzienu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(zari, [
             (2, 3), (-3, 1), (4, -2), (-5, 4), (1, 0), (-2, 7), (3, -6),
             (-4, 2), (5, 5), (-6, 3), (6, -1), (-7, 8), (7, 4), (-8, 6),
             (8, -3)]),
         },
        {"sr": "Nosaka parabolas virsotni",
         "stunda": TEMATS,
         "jautajumi": V.kopa(virsotne, [
             (1, 3), (2, -4), (-1, 5), (3, 6), (-2, -7), (4, 2), (5, -1),
             (-3, 8), (6, 9), (-4, -2), (7, 4), (8, -6), (-5, 3), (9, 7),
             (-6, -5)]),
         },
        {"sr": "Aprēķina kvadrātfunkcijas vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kvadrat_vertiba, [
             (1, 3, 2), (2, -1, 3), (-1, 5, 2), (3, 2, 1), (2, 4, 3),
             (-2, 6, 2), (1, -4, 5), (4, 1, 2), (-3, 2, 3), (5, -2, 1),
             (2, 7, 4), (-1, 9, 3), (6, 3, 2), (3, -5, 4), (-4, 1, 2)]),
         },
        {"sr": "Aprēķina funkcijas y = {k|x} vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(hiperbola_vertiba, [
             (12, 3), (24, 4), (36, 6), (18, 2), (30, 5), (48, 8),
             (60, 10), (20, 4), (45, 9), (56, 7), (72, 12), (100, 20),
             (16, 8), (54, 6), (81, 9)]),
         },
        {"sr": "Nosaka funkcijas lielāko vai mazāko vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mazaka, [
             (1, 3), (2, -4), (-1, 5), (3, 6), (-2, -7), (4, 2), (5, -1),
             (-3, 8), (6, 9), (-4, -2), (7, 4), (8, -6), (-5, 3), (9, 7),
             (-6, -5)]),
         },
        {"sr": "Atrisina vienādojumu x² = t",
         "stunda": TEMATS,
         "jautajumi": V.kopa(x_kvadrata, [
             4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 0, -4, -9,
             169]),
         },
        {"sr": "Lasa kvadrātfunkcijas grafiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda parabolas virsotne, ja zari vērsti uz augšu?",
              ["funkcijas mazāko vērtību", "funkcijas lielāko vērtību",
               "krustpunktu ar x asi", "grafika garumu"], 0),
             ("Ko rāda parabolas virsotne, ja zari vērsti uz leju?",
              ["funkcijas lielāko vērtību", "funkcijas mazāko vērtību",
               "krustpunktu ar x asi", "grafika garumu"], 0),
             ("Ko rāda parabolas krustpunkti ar x asi?",
              ["vienādojuma saknes", "funkcijas lielāko vērtību",
               "virsotni", "simetrijas asi"], 0),
             ("Cik krustpunktu ar x asi var būt parabolai?",
              ["divi, viens vai neviens", "vienmēr divi", "vienmēr viens",
               "vienmēr trīs"], 0),
             ("Kur funkcija y = x² ir augoša?",
              ["kad x > 0", "kad x < 0", "visur", "nekur"], 0),
             ("Kur funkcija y = x² ir dilstoša?",
              ["kad x < 0", "kad x > 0", "visur", "nekur"], 0),
             ("Kāds ir funkcijas y = x² vērtību apgabals?",
              ["y ≥ 0", "y > 0", "visi skaitļi", "y ≤ 0"], 0),
             ("Kāds ir funkcijas y = −x² vērtību apgabals?",
              ["y ≤ 0", "y ≥ 0", "visi skaitļi", "y > 0"], 0),
         ]},
        {"sr": "Lasa funkcijas y = {k|x} grafiku",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik zaru ir hiperbolai?", ["divi", "viens", "trīs",
                                          "četri"], 0),
             ("Kur atrodas hiperbolas zari, ja k > 0?",
              ["pirmajā un trešajā kvadrantā",
               "otrajā un ceturtajā kvadrantā", "tikai pirmajā",
               "uz asīm"], 0),
             ("Kur atrodas hiperbolas zari, ja k < 0?",
              ["otrajā un ceturtajā kvadrantā",
               "pirmajā un trešajā kvadrantā", "tikai otrajā",
               "uz asīm"], 0),
             ("Vai hiperbola krusto asis?",
              ["nē", "jā, abas", "tikai x asi", "tikai y asi"], 0),
             ("Kāds ir funkcijas y = {6|x} vērtību apgabals?",
              ["visi skaitļi, izņemot 0", "visi skaitļi", "y > 0",
               "y ≥ 0"], 0),
             ("Kā mainās y, ja x aug un k > 0?",
              ["y sarūk", "y aug", "y nemainās", "y kļūst 0"], 0),
             ("Kāpēc x nevar būt 0?",
              ["ar nulli nedala", "y kļūtu negatīvs", "grafiks pazustu",
               "tā ir vienošanās"], 0),
             ("Kurš punkts pieder funkcijas y = {12|x} grafikam?",
              ["(3; 4)", "(3; 9)", "(4; 8)", "(2; 10)"], 0),
         ]},
        {"sr": "Nosaka punkta piederību grafikam",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai punkts (2; 4) pieder funkcijas y = x² grafikam?",
              ["jā", "nē", "tikai ja x > 0", "nevar noteikt"], 0),
             ("Vai punkts (3; 6) pieder funkcijas y = x² grafikam?",
              ["nē", "jā", "tikai aptuveni", "nevar noteikt"], 0),
             ("Vai punkts (−2; 4) pieder funkcijas y = x² grafikam?",
              ["jā", "nē", "tikai ja x > 0", "nevar noteikt"], 0),
             ("Vai punkts (2; 5) pieder funkcijas y = x² + 1 grafikam?",
              ["jā", "nē", "tikai ja x > 0", "nevar noteikt"], 0),
             ("Vai punkts (4; 3) pieder funkcijas y = {12|x} grafikam?",
              ["jā", "nē", "tikai ja x > 0", "nevar noteikt"], 0),
             ("Vai punkts (5; 3) pieder funkcijas y = {12|x} grafikam?",
              ["nē", "jā", "tikai aptuveni", "nevar noteikt"], 0),
             ("Kā pārbauda punkta piederību grafikam?",
              ["ievieto koordinātas formulā", "mēra attālumu",
               "salīdzina ar virsotni", "uzzīmē taisni"], 0),
             ("Vai punkts (0; 0) pieder funkcijas y = {5|x} grafikam?",
              ["nē, jo x ≠ 0", "jā", "tikai aptuveni", "vienmēr"], 0),
         ]},
        {"sr": "Nosaka vienādojuma saknes no grafika",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā no grafika nosaka vienādojuma f(x) = 0 saknes?",
              ["nolasa krustpunktu ar x asi abscisas",
               "nolasa virsotni", "mēra grafika garumu",
               "nolasa krustpunktu ar y asi"], 0),
             ("Parabola krusto x asi punktos −3 un 3. Kādas ir saknes?",
              ["x = −3 un x = 3", "x = 0", "x = 9", "sakņu nav"], 0),
             ("Parabola pieskaras x asij punktā 2. Cik sakņu ir?",
              ["viena", "divas", "neviena", "bezgalīgi daudz"], 0),
             ("Parabola nekrusto x asi. Cik sakņu ir?",
              ["neviena", "viena", "divas", "bezgalīgi daudz"], 0),
             ("Kā no grafika nosaka, kur f(x) > 0?",
              ["kur grafiks ir virs x ass", "kur grafiks ir zem x ass",
               "kur x > 0", "virsotnē"], 0),
             ("Kā no grafika nosaka, kur f(x) < 0?",
              ["kur grafiks ir zem x ass", "kur grafiks ir virs x ass",
               "kur x < 0", "virsotnē"], 0),
             ("Ko rāda divu grafiku krustpunkts?",
              ["kur funkciju vērtības ir vienādas", "sakni",
               "virsotni", "vērtību apgabalu"], 0),
             ("Atrisini:  x² = 25.", ["x = 5 vai x = −5", "x = 5",
                                      "x = 12,5", "sakņu nav"], 0),
         ]},
        {"sr": "Lieto funkcijas modelēšanai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar kuru funkciju apraksta kvadrāta laukumu atkarībā no "
              "malas?", ["y = x²", "y = 4x", "y = {4|x}", "y = x + 4"], 0),
             ("Ar kuru funkciju apraksta kvadrāta perimetru atkarībā no "
              "malas?", ["y = 4x", "y = x²", "y = {4|x}", "y = x + 4"], 0),
             ("Ar kuru funkciju apraksta laiku atkarībā no ātruma, ja ceļš "
              "ir 120 km?", ["y = {120|x}", "y = 120x", "y = x + 120",
                             "y = x²"], 0),
             ("Ar kuru funkciju apraksta brīvi krītoša ķermeņa ceļu?",
              ["ar kvadrātfunkciju", "ar lineāru funkciju",
               "ar hiperbolu", "ar taisni"], 0),
             ("Kvadrāta mala aug 2 reizes. Cik reižu aug laukums?",
              ["4", "2", "8", "16"], 0),
             ("Ātrums aug 2 reizes. Kā mainās laiks noteiktā ceļā?",
              ["sarūk 2 reizes", "aug 2 reizes", "nemainās",
               "sarūk 4 reizes"], 0),
             ("Kāda ir sakarība starp apgriezti proporcionāliem lielumiem?",
              ["y = {k|x}", "y = kx", "y = x²", "y = x + k"], 0),
             ("Ar kuru funkciju apraksta lēciena trajektoriju?",
              ["ar kvadrātfunkciju", "ar lineāru funkciju",
               "ar hiperbolu", "ar taisni"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 7,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "7. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.7. temata noslēgumā. "
                "Pārbauda kvadrātfunkciju un hiperbolu, grafika īpašības, "
                "vērtību aprēķināšanu un vienādojuma x² = t atrisināšanu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina funkciju veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir kvadrātfunkcijas grafiks?",
              ["parabola", "taisne", "hiperbola", "riņķa līnija"], 0),
             ("Kāds ir funkcijas y = {k|x} grafiks?",
              ["hiperbola", "parabola", "taisne", "riņķa līnija"], 0),
             ("Kura funkcija ir kvadrātfunkcija?",
              ["y = 2x² + 1", "y = 2x + 1", "y = {2|x}", "y = √x"], 0),
             ("Pret kuru asi ir simetriska parabola y = ax²?",
              ["pret ordinātu asi", "pret abscisu asi",
               "pret abām asīm", "ne pret vienu"], 0),
             ("Kāda vērtība nav atļauta funkcijai y = {k|x}?",
              ["x = 0", "x = 1", "x = −1", "x = k"], 0),
             ("Cik zaru ir hiperbolai?", ["divi", "viens", "trīs",
                                          "četri"], 0),
             ("Kāds ir funkcijas y = x² vērtību apgabals?",
              ["y ≥ 0", "y > 0", "visi skaitļi", "y ≤ 0"], 0),
             ("Vai hiperbola krusto asis?",
              ["nē", "jā, abas", "tikai x asi", "tikai y asi"], 0),
         ]},
        {"sr": "Nosaka parabolas zarus un virsotni",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(zari, [
             (3, 2), (-2, 5), (5, -3), (-6, 1), (7, 4), (-3, 8), (4, -7)])
             + V.kopa(virsotne, [
                 (2, 4), (3, -5), (-2, 6), (4, 7), (-3, -8), (5, 3),
                 (6, -2), (-4, 9)])),
         },
        {"sr": "Aprēķina kvadrātfunkcijas vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kvadrat_vertiba, [
             (1, 4, 3), (2, -2, 2), (-1, 6, 3), (3, 1, 2), (2, 5, 4),
             (-2, 7, 3), (1, -3, 4), (4, 2, 3), (-3, 4, 2), (5, -1, 2),
             (2, 8, 5), (-1, 10, 4), (6, 2, 3), (3, -6, 5), (-4, 3, 3)]),
         },
        {"sr": "Aprēķina funkcijas y = {k|x} vērtību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(hiperbola_vertiba, [
             (24, 3), (36, 4), (48, 6), (20, 2), (40, 5), (64, 8),
             (80, 10), (28, 4), (54, 9), (63, 7), (84, 12), (120, 20),
             (32, 8), (66, 6), (90, 9)]),
         },
        {"sr": "Atrisina vienādojumu x² = t",
         "stunda": TEMATS,
         "jautajumi": V.kopa(x_kvadrata, [
             9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 0, -16, -25,
             196]),
         },
        {"sr": "Lasa grafiku un lieto funkcijas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda parabolas virsotne, ja zari vērsti uz augšu?",
              ["funkcijas mazāko vērtību", "funkcijas lielāko vērtību",
               "krustpunktu ar x asi", "grafika garumu"], 0),
             ("Ko rāda parabolas krustpunkti ar x asi?",
              ["vienādojuma saknes", "funkcijas lielāko vērtību",
               "virsotni", "simetrijas asi"], 0),
             ("Kur funkcija y = x² ir augoša?",
              ["kad x > 0", "kad x < 0", "visur", "nekur"], 0),
             ("Kā no grafika nosaka, kur f(x) > 0?",
              ["kur grafiks ir virs x ass", "kur grafiks ir zem x ass",
               "kur x > 0", "virsotnē"], 0),
             ("Ar kuru funkciju apraksta kvadrāta laukumu atkarībā no "
              "malas?", ["y = x²", "y = 4x", "y = {4|x}", "y = x + 4"], 0),
             ("Ar kuru funkciju apraksta laiku atkarībā no ātruma, ja ceļš "
              "ir 120 km?", ["y = {120|x}", "y = 120x", "y = x + 120",
                             "y = x²"], 0),
             ("Kvadrāta mala aug 2 reizes. Cik reižu aug laukums?",
              ["4", "2", "8", "16"], 0),
             ("Kā pārbauda punkta piederību grafikam?",
              ["ievieto koordinātas formulā", "mēra attālumu",
               "salīdzina ar virsotni", "uzzīmē taisni"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina funkciju vērtības",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Funkciju vērtības",
             lambda a, c, x, k: [
                 ("y = %dx² + %d;  ja x = %d, tad y = ……" % (a, c, x),
                  V.sk(a * x * x + c)),
                 ("y = %dx² + %d;  virsotne ……" % (a, c),
                  "(0; %s)" % V.sk(c)),
                 ("y = {%d|x};  ja x = %d, tad y = ……" % (k, x),
                  V.dalu(k, x)),
                 ("x² = %d;   x = ……" % (x * x),
                  "%d  vai  −%d" % (x, x))],
             [(1, 3, 2, 12), (2, 1, 3, 24), (3, 4, 2, 36), (1, 5, 4, 20),
              (2, 6, 3, 18), (4, 2, 2, 40), (1, 7, 5, 30), (3, 1, 3, 45),
              (5, 3, 2, 50), (2, 8, 4, 28), (6, 4, 3, 54), (1, 9, 6, 60),
              (7, 2, 2, 70), (4, 5, 4, 32), (8, 1, 3, 48)]),
         },
        {"sr": "Raksturo funkcijas grafiku",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Grafika īpašības",
             lambda a, c: [
                 ("y = %sx² + %d;  zari vērsti ……" % (V.iek(a), c),
                  "uz augšu" if a > 0 else "uz leju"),
                 ("y = %sx² + %d;  %s vērtība ……"
                  % (V.iek(a), c, "mazākā" if a > 0 else "lielākā"),
                  V.sk(c)),
                 ("y = %sx² + %d;  simetrijas ass ……" % (V.iek(a), c),
                  "ordinātu ass")],
             [(1, 3), (2, -4), (-1, 5), (3, 6), (-2, -7), (4, 2), (5, -1),
              (-3, 8), (6, 9), (-4, -2), (7, 4), (8, -6), (-5, 3), (9, 7),
              (-6, -5)]),
         },
        {"sr": "Lieto funkciju kā situācijas modeli",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Funkcija situācijā",
             lambda a, x, s: {
                 "teksts": "Kvadrāta mala ir x cm.   a) Pieraksti laukumu "
                           "ar formulu!   b) Cik liels ir laukums, ja "
                           "x = %d?   c) Cik gara ir mala, ja laukums ir "
                           "%d cm²?   d) Cik reižu aug laukums, ja malu "
                           "palielina %d reizes?" % (a, s, x),
                 "kriteriji": [
                     "a) y = x².   (1 p.)",
                     "b) %d² = %d cm².   (1 p.)" % (a, a * a),
                     "c) √%d = %d cm.   (1 p.)"
                     % (s, int(round(s ** 0.5))),
                     "d) %d reizes — %d².   (1 p.)" % (x * x, x)]},
             [(3, 2, 16), (4, 3, 25), (5, 2, 36), (6, 3, 49), (7, 2, 64),
              (8, 4, 81), (9, 2, 100), (10, 3, 121), (11, 2, 144),
              (12, 4, 169), (13, 3, 196), (14, 2, 225), (15, 5, 256),
              (16, 3, 400), (20, 2, 900)]),
         },
        {"sr": "Pamato spriedumus par grafiku",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Parabola",
             lambda a, c: {
                 "ievads": "Dota funkcija  y = %sx² + %s."
                           % (V.iek(a), V.sk(c)),
                 "jaut": [("Uz kuru pusi vērsti grafika zari? Pamato!", 1),
                          ("Kur atrodas grafika virsotne?", 1),
                          ("Kāda ir funkcijas %s vērtība?"
                           % ("mazākā" if a > 0 else "lielākā"), 1)],
                 "atbildes": [
                     "1) %s, jo a %s 0.   (1 p.)"
                     % ("Uz augšu" if a > 0 else "Uz leju",
                        ">" if a > 0 else "<"),
                     "2) (0; %s).   (1 p.)" % V.sk(c),
                     "3) %s.   (1 p.)" % V.sk(c)]},
             [(1, 3), (2, -4), (-1, 5), (3, 6), (-2, -7), (4, 2), (5, -1),
              (-3, 8), (6, 9), (-4, -2), (7, 4), (8, -6), (-5, 3), (9, 7),
              (-6, -5)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
