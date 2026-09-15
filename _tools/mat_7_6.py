# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.6. Kādas ir sakarības starp lielumiem trijstūrī?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.6. temats): īpašība un pazīme,
trijstūra leņķu summa 180°, sakarības starp malām un leņķiem trijstūrī,
šaurleņķa, taisnleņķa un platleņķa trijstūris, kā arī kāpšļu leņķi, iekšējie
šķērsleņķi un iekšējie vienpusleņķi pie paralēlām taisnēm.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.6."
NOSAUKUMS = "Kādas ir sakarības starp lielumiem trijstūrī?"

ATGADNE = [
    "Trijstūra leņķu summa ir 180°   ·   pret vienādām malām atrodas "
    "vienādi leņķi   ·   pret garāko malu atrodas lielākais leņķis.",
    "Divām paralēlām taisnēm krustojoties ar trešo:   kāpšļu leņķi ir "
    "vienādi   ·   iekšējie šķērsleņķi ir vienādi   ·   iekšējo vienpusleņķu "
    "summa ir 180°.",
    "Pēc lielākā leņķa izšķir šaurleņķa (visi < 90°), taisnleņķa (viens "
    "= 90°) un platleņķa (viens > 90°) trijstūrus.",
]


# ---------------------------------------------------------------- veidnes
def tresais_lenkis(a, b):
    """Trešais trijstūra leņķis, ja zināmi divi."""
    return ("Trijstūra divi leņķi ir %d° un %d°. Cik liels ir trešais?"
            % (a, b),
            V.izvele("%d°" % (180 - a - b), "%d°" % (a + b),
                     "%d°" % (90 - a), "%d°" % (360 - a - b),
                     "%d°" % (180 - a), "%d°" % (180 - a - b + 10)), 0)


def trijstura_veids(a, b):
    """Trijstūra veids pēc lielākā leņķa."""
    c = 180 - a - b
    liel = max(a, b, c)
    veids = ("taisnleņķa" if liel == 90 else
             ("platleņķa" if liel > 90 else "šaurleņķa"))
    citi = [v for v in ("šaurleņķa", "taisnleņķa", "platleņķa")
            if v != veids]
    return ("Trijstūra divi leņķi ir %d° un %d°. Kāds ir šis trijstūris?"
            % (a, b),
            V.izvele(veids, citi[0], citi[1], "tāda trijstūra nav"), 0)


def taisnlenka(a):
    """Otrs šaurais leņķis taisnleņķa trijstūrī."""
    return ("Taisnleņķa trijstūra viens šaurais leņķis ir %d°. Cik liels ir "
            "otrs?" % a,
            V.izvele("%d°" % (90 - a), "%d°" % (180 - a), "%d°" % a,
                     "%d°" % (90 + a), "%d°" % (90 - a + 10),
                     "%d°" % (2 * a)), 0)


def skerslenki(a):
    """Iekšējie šķērsleņķi pie paralēlām taisnēm ir vienādi."""
    return ("Divas paralēlas taisnes krusto trešā; viens iekšējais "
            "šķērsleņķis ir %d°. Cik liels ir otrs?" % a,
            V.izvele("%d°" % a, "%d°" % (180 - a), "%d°" % (90 - a),
                     "%d°" % (360 - a), "%d°" % (2 * a),
                     "%d°" % (a + 10)), 0)


def vienpuslenki(a):
    """Iekšējo vienpusleņķu summa ir 180°."""
    return ("Divas paralēlas taisnes krusto trešā; viens iekšējais "
            "vienpusleņķis ir %d°. Cik liels ir otrs?" % a,
            V.izvele("%d°" % (180 - a), "%d°" % a, "%d°" % (90 - a),
                     "%d°" % (360 - a), "%d°" % (2 * a),
                     "%d°" % (180 - a + 10)), 0)


def vienadsanu_pamats(pamata):
    """Vienādsānu trijstūra virsotnes leņķis, ja zināms pamata pieleņķis."""
    return ("Vienādsānu trijstūra pamata pieleņķis ir %d°. Cik liels ir "
            "virsotnes leņķis?" % pamata,
            V.izvele("%d°" % (180 - 2 * pamata), "%d°" % pamata,
                     "%d°" % (180 - pamata), "%d°" % (90 - pamata),
                     "%d°" % (2 * pamata), "%d°" % (180 - 2 * pamata + 10)),
            0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.6. temata beigās. Pārbauda trijstūra "
                "leņķu summu, sakarības starp malām un leņķiem, trijstūru "
                "veidus pēc leņķiem un leņķus pie paralēlām taisnēm.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina trijstūra leņķu summu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir trijstūra leņķu summa?",
              ["180°", "360°", "90°", "270°"], 0),
             ("Vai trijstūrim var būt divi taisni leņķi?",
              ["nē", "jā", "tikai vienādsānu", "tikai vienādmalu"], 0),
             ("Vai trijstūrim var būt divi plati leņķi?",
              ["nē", "jā", "tikai dažādmalu", "tikai vienādsānu"], 0),
             ("Cik lieli ir vienādmalu trijstūra leņķi?",
              ["visi 60°", "visi 90°", "visi 45°", "visi 30°"], 0),
             ("Cik liela ir taisnleņķa trijstūra šauro leņķu summa?",
              ["90°", "180°", "45°", "120°"], 0),
             ("Vai eksistē trijstūris ar leņķiem 60°, 70° un 60°?",
              ["nē, summa nav 180°", "jā", "tikai vienādsānu",
               "nevar noteikt"], 0),
             ("Vai eksistē trijstūris ar leņķiem 30°, 60° un 90°?",
              ["jā", "nē", "tikai vienādmalu", "nevar noteikt"], 0),
             ("Cik mazākais var būt trijstūra lielākais leņķis?",
              ["60°", "45°", "90°", "30°"], 0),
         ]},
        {"sr": "Aprēķina trešo trijstūra leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(tresais_lenkis, [
             (40, 60), (50, 70), (30, 80), (45, 55), (25, 95), (65, 35),
             (20, 110), (75, 45), (85, 50), (15, 120), (55, 65), (90, 40),
             (100, 30), (70, 80), (35, 115)]),
         },
        {"sr": "Nosaka trijstūra veidu pēc leņķiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(trijstura_veids, [
             (40, 60), (50, 40), (30, 80), (100, 40), (25, 95), (60, 60),
             (20, 110), (45, 45), (85, 50), (15, 120), (55, 65), (70, 20),
             (35, 115), (75, 60), (10, 130)]),
         },
        {"sr": "Aprēķina taisnleņķa trijstūra šauro leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(taisnlenka, [
             30, 40, 25, 55, 20, 65, 15, 70, 35, 50, 45, 60, 10, 75, 80]),
         },
        {"sr": "Aprēķina vienādsānu trijstūra virsotnes leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vienadsanu_pamats, [
             40, 50, 30, 65, 25, 70, 20, 75, 35, 55, 45, 60, 15, 80, 85]),
         },
        {"sr": "Saista malas un leņķus trijstūrī",
         "stunda": TEMATS,
         "jautajumi": [
             ("Pret kādām malām atrodas vienādi leņķi?",
              ["pret vienādām malām", "pret garāko malu",
               "pret īsāko malu", "pret jebkuru malu"], 0),
             ("Pret kuru malu atrodas lielākais leņķis?",
              ["pret garāko malu", "pret īsāko malu",
               "pret vidējo malu", "tas nav noteikts"], 0),
             ("Pret kuru malu atrodas mazākais leņķis?",
              ["pret īsāko malu", "pret garāko malu",
               "pret vidējo malu", "tas nav noteikts"], 0),
             ("Trijstūra malas ir 5 cm, 7 cm un 9 cm. Pret kuru malu ir "
              "lielākais leņķis?", ["pret 9 cm malu", "pret 5 cm malu",
                                    "pret 7 cm malu", "visi vienādi"], 0),
             ("Trijstūra leņķi ir 40°, 60° un 80°. Kura mala ir garākā?",
              ["pret 80° leņķi", "pret 40° leņķi", "pret 60° leņķi",
               "visas vienādas"], 0),
             ("Vienādsānu trijstūrī — kādi ir pamata pieleņķi?",
              ["vienādi", "dažādi", "taisni", "plati"], 0),
             ("Ja trijstūrī divi leņķi ir vienādi, kāds tas ir?",
              ["vienādsānu", "dažādmalu", "taisnleņķa", "platleņķa"], 0),
             ("Kas ir figūras pazīme?",
              ["īpašība, kas ļauj to atšķirt no citām", "figūras nosaukums",
               "figūras laukums", "figūras krāsa"], 0),
         ]},
        {"sr": "Zina leņķu nosaukumus pie paralēlām taisnēm",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādi ir kāpšļu leņķi pie paralēlām taisnēm?",
              ["vienādi", "papildinoši līdz 180°", "taisni", "dažādi"], 0),
             ("Kādi ir iekšējie šķērsleņķi pie paralēlām taisnēm?",
              ["vienādi", "papildinoši līdz 180°", "taisni", "dažādi"], 0),
             ("Cik liela ir iekšējo vienpusleņķu summa?",
              ["180°", "90°", "360°", "270°"], 0),
             ("Cik leņķu veidojas, divām paralēlām taisnēm krustojoties ar "
              "trešo?", ["astoņi", "četri", "seši", "divi"], 0),
             ("Kad kāpšļu leņķi ir vienādi?",
              ["kad taisnes ir paralēlas", "vienmēr", "nekad",
               "kad taisnes ir perpendikulāras"], 0),
             ("Ko var secināt, ja iekšējie šķērsleņķi ir vienādi?",
              ["taisnes ir paralēlas", "taisnes krustojas",
               "taisnes sakrīt", "neko"], 0),
             ("Kā sauc taisni, kas krusto abas paralēlās taisnes?",
              ["šķēlēja", "bisektrise", "mediāna", "augstums"], 0),
             ("Cik dažādu leņķu lielumu ir, ja taisnes ir paralēlas?",
              ["divi", "viens", "četri", "astoņi"], 0),
         ]},
        {"sr": "Aprēķina iekšējos šķērsleņķus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(skerslenki, [
             35, 42, 55, 68, 73, 81, 95, 104, 117, 126, 138, 145, 152,
             28, 62]),
         },
        {"sr": "Aprēķina iekšējos vienpusleņķus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vienpuslenki, [
             38, 47, 52, 64, 71, 83, 97, 106, 112, 124, 133, 141, 155,
             29, 76]),
         },
        {"sr": "Lieto leņķu sakarības aprēķinos",
         "stunda": TEMATS,
         "jautajumi": [
             ("Trijstūra leņķi ir attiecībā 1 : 2 : 3. Cik liels ir "
              "mazākais?", ["30°", "60°", "90°", "45°"], 0),
             ("Tajā pašā trijstūrī — cik liels ir lielākais leņķis?",
              ["90°", "60°", "30°", "120°"], 0),
             ("Trijstūra leņķi ir attiecībā 1 : 1 : 2. Cik liels ir "
              "lielākais?", ["90°", "45°", "60°", "120°"], 0),
             ("Viens trijstūra leņķis ir 90°, otrs — divreiz lielāks nekā "
              "trešais. Cik liels ir trešais?", ["30°", "60°", "45°",
                                                 "90°"], 0),
             ("Vienādsānu trijstūra virsotnes leņķis ir 90°. Cik liels ir "
              "pamata pieleņķis?", ["45°", "90°", "60°", "30°"], 0),
             ("Trijstūra ārējais leņķis ir 120°. Cik liels ir tam blakus "
              "esošais iekšējais leņķis?", ["60°", "120°", "30°", "90°"], 0),
             ("Divi trijstūra leņķi ir vienādi, trešais — 80°. Cik liels ir "
              "katrs no pārējiem?", ["50°", "40°", "80°", "100°"], 0),
             ("Trijstūrī viens leņķis ir par 20° lielāks nekā otrs, trešais "
              "— 100°. Cik liels ir mazākais?", ["30°", "50°", "20°",
                                                 "40°"], 0),
         ]},
        {"sr": "Šķiro trijstūrus pēc leņķiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir trijstūris, kuram visi leņķi ir mazāki nekā 90°?",
              ["šaurleņķa", "taisnleņķa", "platleņķa", "vienādmalu"], 0),
             ("Kāds ir trijstūris ar vienu 90° leņķi?",
              ["taisnleņķa", "šaurleņķa", "platleņķa", "vienādmalu"], 0),
             ("Kāds ir trijstūris ar vienu leņķi, lielāku nekā 90°?",
              ["platleņķa", "šaurleņķa", "taisnleņķa", "vienādmalu"], 0),
             ("Kā sauc taisnleņķa trijstūra malas pie taisnā leņķa?",
              ["katetes", "hipotenūza", "pamati", "mediānas"], 0),
             ("Kā sauc taisnleņķa trijstūra garāko malu?",
              ["hipotenūza", "katete", "pamats", "augstums"], 0),
             ("Kāds ir vienādmalu trijstūris pēc leņķiem?",
              ["šaurleņķa", "taisnleņķa", "platleņķa", "dažādmalu"], 0),
             ("Vai platleņķa trijstūris var būt vienādsānu?",
              ["jā", "nē", "tikai ar 90°", "tikai ar 60°"], 0),
             ("Cik platu leņķu var būt vienā trijstūrī?",
              ["viens", "divi", "trīs", "neviens"], 0),
         ]},
        {"sr": "Pamato apgalvojumus par trijstūri",
         "stunda": TEMATS,
         "jautajumi": [
             ("Vai eksistē trijstūris ar diviem platiem leņķiem?",
              ["nē, summa pārsniegtu 180°", "jā", "tikai vienādsānu",
               "nevar noteikt"], 0),
             ("Vai eksistē vienādmalu taisnleņķa trijstūris?",
              ["nē, visi leņķi būtu 60°", "jā", "tikai liels",
               "nevar noteikt"], 0),
             ("Vai eksistē vienādsānu taisnleņķa trijstūris?",
              ["jā, leņķi 90°, 45° un 45°", "nē", "tikai vienādmalu",
               "nevar noteikt"], 0),
             ("Kāpēc trijstūra leņķu summa ir 180°?",
              ["to pierāda, izmantojot paralēlas taisnes",
               "tā ir definīcija", "tā ir sagadīšanās", "tas nav tiesa"], 0),
             ("Ko nozīmē pierādīt apgalvojumu?",
              ["parādīt, ka tas ir patiess visos gadījumos",
               "parādīt vienu piemēru", "to izmērīt", "to uzzīmēt"], 0),
             ("Kas ir pretpiemērs?",
              ["piemērs, kas atspēko apgalvojumu",
               "piemērs, kas apstiprina", "otrs pierādījums",
               "otra teorēma"], 0),
             ("Vai trijstūrī pret lielāko leņķi vienmēr ir garākā mala?",
              ["jā", "nē", "tikai vienādsānu", "tikai taisnleņķa"], 0),
             ("Kāds ir apgalvojums «trijstūrī visi leņķi ir vienādi»?",
              ["patiess tikai vienādmalu trijstūrim", "vienmēr patiess",
               "vienmēr aplams", "nevar noteikt"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 6,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "6. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.6. temata noslēgumā. "
                "Pārbauda trijstūra leņķu summu, trijstūru veidus, "
                "sakarības starp malām un leņķiem un leņķus pie paralēlām "
                "taisnēm.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Aprēķina trešo trijstūra leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(tresais_lenkis, [
             (35, 65), (55, 75), (25, 85), (40, 50), (30, 100), (60, 45),
             (15, 115), (70, 55), (80, 45), (20, 125), (50, 60), (95, 35),
             (105, 25), (75, 85), (45, 110)]),
         },
        {"sr": "Nosaka trijstūra veidu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(trijstura_veids, [
             (35, 65), (55, 35), (25, 85), (105, 35), (30, 100), (60, 50),
             (15, 115), (40, 50), (80, 55), (20, 125), (50, 60), (75, 25),
             (30, 120), (70, 65), (10, 140)]),
         },
        {"sr": "Aprēķina taisnleņķa un vienādsānu trijstūra leņķus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(taisnlenka, [
             35, 45, 20, 60, 25, 70, 15])
             + V.kopa(vienadsanu_pamats, [
                 45, 55, 35, 70, 30, 75, 25, 65])),
         },
        {"sr": "Aprēķina iekšējos šķērsleņķus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(skerslenki, [
             32, 44, 58, 66, 79, 88, 92, 108, 119, 127, 136, 149, 158,
             26, 71]),
         },
        {"sr": "Aprēķina iekšējos vienpusleņķus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vienpuslenki, [
             36, 49, 54, 61, 74, 87, 99, 103, 116, 121, 134, 147, 151,
             33, 69]),
         },
        {"sr": "Pamato apgalvojumus par trijstūri",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir trijstūra leņķu summa?",
              ["180°", "360°", "90°", "270°"], 0),
             ("Pret kuru malu atrodas lielākais leņķis?",
              ["pret garāko malu", "pret īsāko malu",
               "pret vidējo malu", "tas nav noteikts"], 0),
             ("Vai eksistē trijstūris ar diviem platiem leņķiem?",
              ["nē, summa pārsniegtu 180°", "jā", "tikai vienādsānu",
               "nevar noteikt"], 0),
             ("Kādi ir iekšējie šķērsleņķi pie paralēlām taisnēm?",
              ["vienādi", "papildinoši līdz 180°", "taisni", "dažādi"], 0),
             ("Cik liela ir iekšējo vienpusleņķu summa?",
              ["180°", "90°", "360°", "270°"], 0),
             ("Kāds ir trijstūris ar vienu leņķi, lielāku nekā 90°?",
              ["platleņķa", "šaurleņķa", "taisnleņķa", "vienādmalu"], 0),
             ("Trijstūra leņķi ir attiecībā 1 : 2 : 3. Cik liels ir "
              "lielākais?", ["90°", "60°", "30°", "120°"], 0),
             ("Kas ir figūras pazīme?",
              ["īpašība, kas ļauj to atšķirt no citām", "figūras nosaukums",
               "figūras laukums", "figūras krāsa"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina leņķus trijstūrī un pie paralēlām taisnēm",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, b, s, v: [
                 ("Trijstūrī leņķi %d° un %d°; trešais ……°" % (a, b),
                  V.sk(180 - a - b)),
                 ("Taisnleņķa trijstūrī šaurais leņķis %d°; otrs ……°" % a,
                  V.sk(90 - a)),
                 ("Iekšējais šķērsleņķis %d°; otrs ……°" % s, V.sk(s)),
                 ("Iekšējais vienpusleņķis %d°; otrs ……°" % v,
                  V.sk(180 - v))],
             [(40, 60, 55, 70), (50, 70, 62, 85), (30, 80, 48, 95),
              (45, 55, 71, 110), (25, 35, 84, 125), (65, 35, 39, 65),
              (20, 50, 96, 140), (75, 45, 57, 75), (85, 50, 43, 105),
              (15, 60, 108, 135), (55, 65, 66, 80), (35, 40, 74, 115),
              (10, 30, 88, 145), (70, 80, 52, 90), (60, 25, 119, 100)]),
         },
        {"sr": "Nosaka trijstūra veidu",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Trijstūra veids",
             lambda a, b, c, d: [
                 ("Leņķi %d° un %d°; trijstūris ir ……" % (a, b),
                  ("platleņķa" if 180 - a - b > 90 else
                   ("taisnleņķa" if 180 - a - b == 90 else "šaurleņķa"))),
                 ("Leņķi %d° un %d°; trijstūris ir ……" % (c, d),
                  ("platleņķa" if 180 - c - d > 90 else
                   ("taisnleņķa" if 180 - c - d == 90 else "šaurleņķa"))),
                 ("Vienādsānu trijstūra pamata pieleņķis %d°; virsotnes "
                  "leņķis ……°" % a, V.sk(180 - 2 * a))],
             [(40, 60, 30, 40), (50, 70, 25, 45), (35, 55, 20, 50),
              (45, 65, 15, 35), (55, 75, 10, 30), (60, 30, 40, 20),
              (65, 45, 35, 25), (70, 50, 45, 30), (30, 80, 50, 15),
              (75, 40, 55, 20), (25, 85, 60, 10), (80, 55, 65, 15),
              (20, 70, 70, 10), (85, 45, 75, 5), (15, 75, 80, 5)]),
         },
        {"sr": "Risina uzdevumu par trijstūra leņķiem",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Trijstūra leņķi",
             lambda a, b: {
                 "teksts": "Trijstūra divi leņķi ir %d° un %d°.   "
                           "a) Aprēķini trešo leņķi!   b) Kāds ir šis "
                           "trijstūris pēc leņķiem?   c) Pret kuru leņķi "
                           "atrodas garākā mala?   d) Cik liels ir ārējais "
                           "leņķis pie %d° leņķa?" % (a, b, a),
                 "kriteriji": [
                     "a) 180° − %d° − %d° = %d°.   (1 p.)"
                     % (a, b, 180 - a - b),
                     "b) %s trijstūris.   (1 p.)"
                     % ("Platleņķa" if max(a, b, 180 - a - b) > 90 else
                        ("Taisnleņķa" if max(a, b, 180 - a - b) == 90
                         else "Šaurleņķa")),
                     "c) Pret lielāko leņķi — %d°.   (1 p.)"
                     % max(a, b, 180 - a - b),
                     "d) 180° − %d° = %d°.   (1 p.)" % (a, 180 - a)]},
             [(40, 60), (50, 70), (30, 80), (45, 55), (25, 95), (65, 35),
              (20, 110), (75, 45), (85, 50), (15, 120), (55, 65), (90, 40),
              (100, 30), (70, 80), (35, 115)]),
         },
        {"sr": "Pamato leņķu sakarības pie paralēlām taisnēm",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Paralēlas taisnes",
             lambda a: {
                 "ievads": "Divas paralēlas taisnes krusto trešā taisne; "
                           "viens no leņķiem ir %d°." % a,
                 "jaut": [("Cik liels ir tam atbilstošais kāpšļu leņķis?",
                           1),
                          ("Cik liels ir iekšējais vienpusleņķis?", 1),
                          ("Pamato, kāpēc kāpšļu leņķi ir vienādi!", 1)],
                 "atbildes": [
                     "1) %d°.   (1 p.)" % a,
                     "2) 180° − %d° = %d°.   (1 p.)" % (a, 180 - a),
                     "3) Taisnes ir paralēlas, tāpēc kāpšļu leņķi ir "
                     "vienādi.   (1 p.)"]},
             [35, 42, 55, 68, 73, 81, 95, 104, 117, 126, 138, 145, 152,
              28, 62]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
