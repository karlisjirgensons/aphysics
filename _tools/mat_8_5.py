# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.5. Četrstūri ar pa pāriem paralēlām malām.

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.5. temats): taišņu
paralelitātes pazīmes, četrstūra leņķu summa, četrstūru klasifikācija
(paralelograms, trapece, rombs, taisnstūris, kvadrāts), paralelograma un
romba īpašības, diagonāles un laukuma formulas.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.5."
NOSAUKUMS = "Kas kopīgs četrstūriem, kuru pretējās malas ir pa pāriem " \
            "paralēlas?"

ATGADNE = [
    "Četrstūra iekšējo leņķu summa ir 360°   ·   paralelogramā pretējie "
    "leņķi ir vienādi, blakus leņķu summa ir 180°.",
    "Paralelogramā pretējās malas ir vienādas, diagonāles krustpunktā dalās "
    "uz pusēm   ·   rombā diagonāles ir perpendikulāras un dala leņķus uz "
    "pusēm.",
    "Laukumi:   paralelograms   S = a · h   ·   rombs   S = {d₁ · d₂|2}   ·  "
    " taisnstūris   S = a · b   ·   kvadrāts   S = a².",
]


# ---------------------------------------------------------------- veidnes
def ceturtais_lenkis(a, b, c):
    """Ceturtais četrstūra leņķis, ja zināmi trīs."""
    return ("Četrstūra trīs leņķi ir %d°, %d° un %d°. Cik liels ir "
            "ceturtais?" % (a, b, c),
            V.izvele("%d°" % (360 - a - b - c), "%d°" % (180 - a - b - c
                                                         if a + b + c < 180
                                                         else a + b + c),
                     "%d°" % (a + b + c), "%d°" % (360 - a - b),
                     "%d°" % (360 - a - b - c + 10),
                     "%d°" % (180 - a)), 0)


def paralelograms_lenkis(a):
    """Paralelograma blakus leņķis."""
    return ("Paralelograma viens leņķis ir %d°. Cik liels ir tam blakus "
            "esošais leņķis?" % a,
            V.izvele("%d°" % (180 - a), "%d°" % a, "%d°" % (360 - a),
                     "%d°" % (90 - a), "%d°" % (2 * a),
                     "%d°" % (180 - a + 10)), 0)


def paralelograms_pretejs(a):
    """Paralelograma pretējais leņķis."""
    return ("Paralelograma viens leņķis ir %d°. Cik liels ir tam pretējais "
            "leņķis?" % a,
            V.izvele("%d°" % a, "%d°" % (180 - a), "%d°" % (360 - a),
                     "%d°" % (90 - a), "%d°" % (2 * a),
                     "%d°" % (a + 10)), 0)


def perimetrs(a, b):
    """Paralelograma perimetrs."""
    return ("Paralelograma malas ir %d cm un %d cm. Cik garš ir perimetrs?"
            % (a, b),
            V.izvele("%d cm" % (2 * (a + b)), "%d cm" % (a + b),
                     "%d cm" % (a * b), "%d cm" % (4 * a),
                     "%d cm" % (2 * a + b), "%d cm" % (2 * (a + b) + 2)), 0)


def laukums(a, h):
    """Paralelograma laukums."""
    return ("Paralelograma mala ir %d cm, pret to novilktais augstums — "
            "%d cm. Cik liels ir laukums?" % (a, h),
            V.izvele("%d cm²" % (a * h), "%s cm²" % V.dalu(a * h, 2),
                     "%d cm²" % (a + h), "%d cm²" % (2 * (a + h)),
                     "%d cm²" % (2 * a * h), "%d cm²" % (a * h + 2)), 0)


def romba_laukums(d1, d2):
    """Romba laukums pēc diagonālēm."""
    return ("Romba diagonāles ir %d cm un %d cm. Cik liels ir laukums?"
            % (d1, d2),
            V.izvele("%s cm²" % V.dalu(d1 * d2, 2), "%d cm²" % (d1 * d2),
                     "%d cm²" % (d1 + d2), "%s cm²" % V.dalu(d1 + d2, 2),
                     "%d cm²" % (2 * d1 * d2), "%d cm²" % (d1 * d2 + 2)), 0)


def mala_no_laukuma(s, h):
    """Paralelograma mala, ja zināms laukums un augstums."""
    return ("Paralelograma laukums ir %d cm², augstums — %d cm. Cik gara ir "
            "mala?" % (s, h),
            V.izvele("%s cm" % V.dalu(s, h), "%s cm" % V.dalu(2 * s, h),
                     "%d cm" % (s * h), "%d cm" % (s - h),
                     "%s cm" % V.dalu(s, 2 * h), "%d cm" % (s + h)), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.5. temata beigās. Pārbauda četrstūru "
                "klasifikāciju, četrstūra leņķu summu, paralelograma un "
                "romba īpašības, diagonāles un laukuma formulas.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Šķiro četrstūrus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc četrstūri, kuram pretējās malas ir pa pāriem "
              "paralēlas?", ["paralelograms", "trapece", "deltoīds",
                             "daudzstūris"], 0),
             ("Kā sauc četrstūri, kuram tieši divas malas ir paralēlas?",
              ["trapece", "paralelograms", "rombs", "kvadrāts"], 0),
             ("Kā sauc paralelogramu ar visām vienādām malām?",
              ["rombs", "taisnstūris", "trapece", "deltoīds"], 0),
             ("Kā sauc paralelogramu ar taisniem leņķiem?",
              ["taisnstūris", "rombs", "trapece", "deltoīds"], 0),
             ("Kas ir kvadrāts?",
              ["rombs un taisnstūris vienlaikus", "tikai rombs",
               "tikai taisnstūris", "trapece"], 0),
             ("Vai katrs taisnstūris ir paralelograms?",
              ["jā", "nē", "tikai kvadrāts", "nevar noteikt"], 0),
             ("Vai katrs paralelograms ir taisnstūris?",
              ["nē", "jā", "tikai rombs", "vienmēr"], 0),
             ("Kā sauc nogriezni, kas savieno pretējās virsotnes?",
              ["diagonāle", "augstums", "mediāna", "bisektrise"], 0),
         ]},
        {"sr": "Zina četrstūra leņķu summu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir četrstūra leņķu summa?",
              ["360°", "180°", "540°", "270°"], 0),
             ("Kā to iegūst?",
              ["četrstūri sadala divos trijstūros", "izmēra ar transportieri",
               "saskaita malas", "dala 180° ar 2"], 0),
             ("Cik liela ir taisnstūra leņķu summa?",
              ["360°", "180°", "90°", "270°"], 0),
             ("Ja visi četrstūra leņķi ir vienādi, cik liels ir katrs?",
              ["90°", "60°", "120°", "45°"], 0),
             ("Vai četrstūrim var būt trīs taisni leņķi?",
              ["jā, tad arī ceturtais ir taisns", "nē",
               "tikai rombā", "tikai trapecē"], 0),
             ("Vai četrstūrim var būt četri plati leņķi?",
              ["nē", "jā", "tikai rombā", "tikai trapecē"], 0),
             ("Cik liela ir paralelograma blakus leņķu summa?",
              ["180°", "360°", "90°", "270°"], 0),
             ("Kāds ir ieliekts četrstūris?",
              ["tam viens leņķis ir lielāks nekā 180°",
               "tam visas malas vienādas", "tam nav diagonāļu",
               "tas ir kvadrāts"], 0),
         ]},
        {"sr": "Aprēķina ceturto četrstūra leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(ceturtais_lenkis, [
             (90, 90, 80), (70, 110, 60), (85, 95, 100), (60, 120, 90),
             (100, 80, 75), (45, 135, 110), (65, 115, 95), (50, 130, 85),
             (105, 75, 60), (40, 140, 120), (55, 125, 100), (95, 85, 70),
             (110, 70, 65), (35, 145, 115), (80, 100, 55)]),
         },
        {"sr": "Aprēķina paralelograma blakus leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(paralelograms_lenkis, [
             40, 55, 65, 70, 80, 95, 100, 110, 115, 125, 130, 140, 145,
             35, 50]),
         },
        {"sr": "Aprēķina paralelograma pretējo leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(paralelograms_pretejs, [
             45, 60, 75, 85, 90, 105, 120, 135, 150, 30, 25, 155, 160,
             20, 165]),
         },
        {"sr": "Zina paralelograma īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir paralelograma pretējās malas?",
              ["vienādas un paralēlas", "vienādas, bet nav paralēlas",
               "paralēlas, bet nav vienādas", "perpendikulāras"], 0),
             ("Kādi ir paralelograma pretējie leņķi?",
              ["vienādi", "papildinoši līdz 180°", "taisni", "dažādi"], 0),
             ("Kā paralelogramā dalās diagonāles?",
              ["krustpunktā uz pusēm", "tās nekrustojas",
               "attiecībā 1 : 2", "tās ir vienādas"], 0),
             ("Vai paralelograma diagonāles vienmēr ir vienādas?",
              ["nē, tikai taisnstūrī", "jā", "tikai rombā", "nekad"], 0),
             ("Vai paralelograma diagonāles vienmēr ir perpendikulāras?",
              ["nē, tikai rombā", "jā", "tikai taisnstūrī", "nekad"], 0),
             ("Kā paralelogramu sadala diagonāle?",
              ["divos vienādos trijstūros", "divos dažādos trijstūros",
               "četros trijstūros", "tā nesadala"], 0),
             ("Kas ir paralelograma augstums?",
              ["perpendikuls starp paralēlām malām", "diagonāle",
               "garākā mala", "malu summa"], 0),
             ("Kas ir attālums starp paralēlām taisnēm?",
              ["perpendikula garums starp tām", "jebkurš nogrieznis",
               "taisnes garums", "krustpunkts"], 0),
         ]},
        {"sr": "Aprēķina paralelograma perimetru",
         "stunda": TEMATS,
         "jautajumi": V.kopa(perimetrs, [
             (5, 8), (6, 9), (4, 7), (10, 12), (3, 11), (7, 13),
             (8, 15), (9, 14), (11, 16), (12, 20), (13, 17), (14, 18),
             (15, 25), (16, 19), (20, 30)]),
         },
        {"sr": "Aprēķina paralelograma laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(laukums, [
             (6, 4), (8, 5), (10, 3), (12, 7), (9, 6), (14, 5), (7, 8),
             (16, 9), (11, 4), (18, 6), (13, 10), (20, 7), (15, 8),
             (22, 5), (24, 9)]),
         },
        {"sr": "Nosaka malu pēc laukuma",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mala_no_laukuma, [
             (24, 6), (30, 5), (40, 8), (18, 3), (54, 9), (28, 7),
             (36, 4), (60, 10), (48, 6), (44, 11), (32, 8), (70, 14),
             (42, 7), (90, 15), (56, 8)]),
         },
        {"sr": "Aprēķina romba laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(romba_laukums, [
             (6, 8), (10, 4), (12, 5), (8, 14), (16, 6), (20, 3),
             (9, 10), (18, 7), (24, 5), (15, 12), (22, 8), (30, 4),
             (26, 9), (11, 16), (28, 6)]),
         },
        {"sr": "Zina romba un taisnstūra īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir romba diagonāles?",
              ["perpendikulāras un dalās uz pusēm", "vienādas",
               "paralēlas", "nekrustojas"], 0),
             ("Ko rombā dara diagonāle ar leņķi?",
              ["dala to uz pusēm", "dala to attiecībā 1 : 2",
               "nemaina to", "palielina to"], 0),
             ("Kādas ir taisnstūra diagonāles?",
              ["vienādas un dalās uz pusēm", "perpendikulāras",
               "dažāda garuma", "paralēlas"], 0),
             ("Kādas ir kvadrāta diagonāles?",
              ["vienādas un perpendikulāras", "tikai vienādas",
               "tikai perpendikulāras", "dažāda garuma"], 0),
             ("Ar kuru formulu aprēķina romba laukumu?",
              ["S = {d₁ · d₂|2}", "S = d₁ · d₂", "S = a²",
               "S = 2 · (a + b)"], 0),
             ("Vai rombam var lietot formulu S = a · h?",
              ["jā", "nē", "tikai kvadrātam", "tikai taisnstūrim"], 0),
             ("Cik simetrijas asu ir kvadrātam?",
              ["četras", "divas", "viena", "neviena"], 0),
             ("Cik simetrijas asu ir rombam?",
              ["divas", "četras", "viena", "neviena"], 0),
         ]},
        {"sr": "Lieto taišņu paralelitātes pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad divas taisnes ir paralēlas?",
              ["ja iekšējie šķērsleņķi ir vienādi", "ja tās krustojas",
               "ja leņķi ir taisni", "ja tās ir vienāda garuma"], 0),
             ("Ko var secināt, ja kāpšļu leņķi ir vienādi?",
              ["taisnes ir paralēlas", "taisnes krustojas",
               "taisnes sakrīt", "neko"], 0),
             ("Ko var secināt, ja iekšējo vienpusleņķu summa ir 180°?",
              ["taisnes ir paralēlas", "taisnes krustojas",
               "taisnes sakrīt", "neko"], 0),
             ("Ja abas taisnes ir perpendikulāras trešajai, tad tās ir...",
              ["paralēlas", "perpendikulāras", "krustiskas", "vienādas"], 0),
             ("Cik kopīgu punktu ir divām paralēlām taisnēm?",
              ["0", "1", "2", "bezgalīgi daudz"], 0),
             ("Kā apzīmē paralēlas taisnes?",
              ["a ∥ b", "a ⊥ b", "a = b", "a ∈ b"], 0),
             ("Kāpēc paralelogramā pretējās malas ir paralēlas?",
              ["tā ir tā definīcija", "tā ir sagadīšanās",
               "to nosaka laukums", "tas nav tiesa"], 0),
             ("Kā pierāda četrstūra malu vienādību?",
              ["parāda divu trijstūru vienādību", "izmēra tās",
               "saskaita leņķus", "aprēķina laukumu"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.5. temata noslēgumā. "
                "Pārbauda četrstūru klasifikāciju, leņķu aprēķinus, "
                "paralelograma un romba īpašības un laukuma formulas.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Šķiro četrstūrus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc četrstūri, kuram pretējās malas ir pa pāriem "
              "paralēlas?", ["paralelograms", "trapece", "deltoīds",
                             "daudzstūris"], 0),
             ("Kā sauc četrstūri, kuram tieši divas malas ir paralēlas?",
              ["trapece", "paralelograms", "rombs", "kvadrāts"], 0),
             ("Kā sauc paralelogramu ar visām vienādām malām?",
              ["rombs", "taisnstūris", "trapece", "deltoīds"], 0),
             ("Kas ir kvadrāts?",
              ["rombs un taisnstūris vienlaikus", "tikai rombs",
               "tikai taisnstūris", "trapece"], 0),
             ("Vai katrs taisnstūris ir paralelograms?",
              ["jā", "nē", "tikai kvadrāts", "nevar noteikt"], 0),
             ("Cik liela ir četrstūra leņķu summa?",
              ["360°", "180°", "540°", "270°"], 0),
             ("Kā sauc nogriezni, kas savieno pretējās virsotnes?",
              ["diagonāle", "augstums", "mediāna", "bisektrise"], 0),
             ("Kāds ir ieliekts četrstūris?",
              ["tam viens leņķis ir lielāks nekā 180°",
               "tam visas malas vienādas", "tam nav diagonāļu",
               "tas ir kvadrāts"], 0),
         ]},
        {"sr": "Aprēķina četrstūra leņķus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(ceturtais_lenkis, [
             (90, 90, 70), (75, 105, 60), (80, 100, 95), (65, 115, 90),
             (105, 75, 80), (50, 130, 105), (70, 110, 90), (55, 125, 80),
             (100, 80, 65), (45, 135, 115), (60, 120, 95), (90, 85, 75),
             (115, 65, 70), (40, 140, 110), (85, 95, 60)]),
         },
        {"sr": "Aprēķina paralelograma leņķus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(paralelograms_lenkis, [
             45, 60, 75, 85, 105, 120, 135])
             + V.kopa(paralelograms_pretejs, [
                 40, 55, 65, 70, 80, 95, 110, 125])),
         },
        {"sr": "Aprēķina perimetru un laukumu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(perimetrs, [
             (6, 9), (7, 10), (5, 8), (11, 13), (4, 12), (8, 14),
             (9, 16)])
             + V.kopa(laukums, [
                 (7, 5), (9, 6), (11, 4), (13, 8), (10, 7), (15, 6),
                 (8, 9), (17, 10)])),
         },
        {"sr": "Aprēķina romba laukumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(romba_laukums, [
             (8, 6), (12, 4), (14, 5), (10, 16), (18, 6), (22, 3),
             (11, 10), (20, 7), (26, 5), (17, 12), (24, 8), (32, 4),
             (28, 9), (13, 18), (30, 6)]),
         },
        {"sr": "Zina paralelograma un romba īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādas ir paralelograma pretējās malas?",
              ["vienādas un paralēlas", "vienādas, bet nav paralēlas",
               "paralēlas, bet nav vienādas", "perpendikulāras"], 0),
             ("Kā paralelogramā dalās diagonāles?",
              ["krustpunktā uz pusēm", "tās nekrustojas",
               "attiecībā 1 : 2", "tās ir vienādas"], 0),
             ("Kādas ir romba diagonāles?",
              ["perpendikulāras un dalās uz pusēm", "vienādas",
               "paralēlas", "nekrustojas"], 0),
             ("Kādas ir taisnstūra diagonāles?",
              ["vienādas un dalās uz pusēm", "perpendikulāras",
               "dažāda garuma", "paralēlas"], 0),
             ("Ar kuru formulu aprēķina romba laukumu?",
              ["S = {d₁ · d₂|2}", "S = d₁ · d₂", "S = a²",
               "S = 2 · (a + b)"], 0),
             ("Kad divas taisnes ir paralēlas?",
              ["ja iekšējie šķērsleņķi ir vienādi", "ja tās krustojas",
               "ja leņķi ir taisni", "ja tās ir vienāda garuma"], 0),
             ("Kā paralelogramu sadala diagonāle?",
              ["divos vienādos trijstūros", "divos dažādos trijstūros",
               "četros trijstūros", "tā nesadala"], 0),
             ("Cik simetrijas asu ir kvadrātam?",
              ["četras", "divas", "viena", "neviena"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina četrstūra lielumus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, b, h, lenk: [
                 ("Paralelograms  a = %d cm,  b = %d cm;  P = …… cm"
                  % (a, b), V.sk(2 * (a + b))),
                 ("Paralelograms  a = %d cm,  h = %d cm;  S = …… cm²"
                  % (a, h), V.sk(a * h)),
                 ("Paralelograma leņķis %d°;  blakus leņķis ……°" % lenk,
                  V.sk(180 - lenk)),
                 ("Rombs  d₁ = %d cm,  d₂ = %d cm;  S = …… cm²" % (a, h),
                  V.dalu(a * h, 2))],
             [(6, 8, 4, 40), (8, 10, 5, 55), (10, 12, 3, 65),
              (12, 14, 7, 70), (9, 11, 6, 80), (14, 16, 5, 95),
              (7, 9, 8, 100), (16, 18, 9, 110), (11, 13, 4, 115),
              (18, 20, 6, 125), (13, 15, 10, 130), (20, 22, 7, 140),
              (15, 17, 8, 145), (22, 24, 5, 35), (24, 26, 9, 50)]),
         },
        {"sr": "Aprēķina leņķus četrstūrī",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Leņķi četrstūrī",
             lambda a, b, c: [
                 ("Četrstūra leņķi %d°, %d°, %d°;  ceturtais ……°"
                  % (a, b, c), V.sk(360 - a - b - c)),
                 ("Paralelograma leņķis %d°;  pretējais ……°" % a,
                  V.sk(a)),
                 ("Paralelograma leņķis %d°;  blakus ……°" % a,
                  V.sk(180 - a))],
             [(90, 90, 80), (70, 110, 60), (85, 95, 100), (60, 120, 90),
              (100, 80, 75), (45, 135, 110), (65, 115, 95), (50, 130, 85),
              (105, 75, 60), (40, 140, 120), (55, 125, 100), (95, 85, 70),
              (110, 70, 65), (35, 145, 115), (80, 100, 55)]),
         },
        {"sr": "Risina uzdevumu par paralelogramu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Paralelograms",
             lambda a, b, h, lenk: {
                 "teksts": "Paralelograma malas ir %d cm un %d cm, "
                           "augstums pret %d cm malu — %d cm, viens leņķis "
                           "— %d°.   a) Aprēķini perimetru!   b) Aprēķini "
                           "laukumu!   c) Cik liels ir blakus leņķis?   "
                           "d) Cik liels ir pretējais leņķis?"
                           % (a, b, a, h, lenk),
                 "kriteriji": [
                     "a) 2 · (%d + %d) = %d cm.   (1 p.)"
                     % (a, b, 2 * (a + b)),
                     "b) %d · %d = %d cm².   (1 p.)" % (a, h, a * h),
                     "c) 180° − %d° = %d°.   (1 p.)" % (lenk, 180 - lenk),
                     "d) %d°.   (1 p.)" % lenk]},
             [(6, 8, 4, 40), (8, 10, 5, 55), (10, 12, 3, 65),
              (12, 14, 7, 70), (9, 11, 6, 80), (14, 16, 5, 95),
              (7, 9, 8, 100), (16, 18, 9, 110), (11, 13, 4, 115),
              (18, 20, 6, 125), (13, 15, 10, 130), (20, 22, 7, 140),
              (15, 17, 8, 145), (22, 24, 5, 35), (24, 26, 9, 50)]),
         },
        {"sr": "Pamato četrstūra īpašības",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Rombs",
             lambda d1, d2: {
                 "ievads": "Romba diagonāles ir %d cm un %d cm."
                           % (d1, d2),
                 "jaut": [("Aprēķini romba laukumu!", 1),
                          ("Kādā leņķī krustojas diagonāles?", 1),
                          ("Cik garas ir diagonāļu puses?", 1)],
                 "atbildes": [
                     "1) %d · %d : 2 = %s cm².   (1 p.)"
                     % (d1, d2, V.dalu(d1 * d2, 2)),
                     "2) 90° — rombā diagonāles ir perpendikulāras.   "
                     "(1 p.)",
                     "3) %s cm un %s cm.   (1 p.)"
                     % (V.dalu(d1, 2), V.dalu(d2, 2))]},
             [(6, 8), (10, 4), (12, 5), (8, 14), (16, 6), (20, 3),
              (9, 10), (18, 7), (24, 5), (15, 12), (22, 8), (30, 4),
              (26, 9), (11, 16), (28, 6)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
