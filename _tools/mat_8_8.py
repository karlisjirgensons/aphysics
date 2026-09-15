# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.8. Taisnleņķa trijstūra nezināmā mala.

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.8. temats): katete un
hipotenūza, Pitagora teorēma un tās lietojums nezināmās malas aprēķināšanai,
teorēmas izmantošana citu plaknes figūru nezināmo lielumu noteikšanai,
taisnleņķa trijstūra konstruēšana un vienādības pierādīšana.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.8."
NOSAUKUMS = "Kā nosaka taisnleņķa trijstūra nezināmās malas garumu?"

ATGADNE = [
    "Pitagora teorēma:   a² + b² = c²,   kur a un b ir katetes, c — "
    "hipotenūza (garākā mala pret taisno leņķi).",
    "Hipotenūza:   c = √(a² + b²)   ·   katete:   a = √(c² − b²)",
    "Bieži sastopami veseli trijnieki:   3; 4; 5   ·   6; 8; 10   ·   "
    "5; 12; 13   ·   8; 15; 17   ·   9; 12; 15   ·   7; 24; 25",
]


# ---------------------------------------------------------------- veidnes
def hipotenuza(a, b):
    """Hipotenūza no divām katetēm (Pitagora trijnieki)."""
    c = int(round((a * a + b * b) ** 0.5))
    return ("Taisnleņķa trijstūra katetes ir %d cm un %d cm. Cik gara ir "
            "hipotenūza?" % (a, b),
            V.izvele("%d cm" % c, "%d cm" % (a + b), "%d cm" % (a * b),
                     "%d cm" % (c + 1), "%d cm" % abs(a - b),
                     "%d cm" % (c - 1)), 0)


def katete(c, b):
    """Katete, ja zināma hipotenūza un otra katete."""
    a = int(round((c * c - b * b) ** 0.5))
    return ("Taisnleņķa trijstūra hipotenūza ir %d cm, viena katete — "
            "%d cm. Cik gara ir otra katete?" % (c, b),
            V.izvele("%d cm" % a, "%d cm" % (c - b), "%d cm" % (c + b),
                     "%d cm" % (a + 1), "%d cm" % (c * b),
                     "%d cm" % (a - 1)), 0)


def kvadrati(a, b):
    """Katešu kvadrātu summa ir hipotenūzas kvadrāts."""
    return ("Katetes ir %d cm un %d cm. Cik liels ir hipotenūzas kvadrāts?"
            % (a, b),
            V.izvele("%d cm²" % (a * a + b * b), "%d cm²" % ((a + b) ** 2),
                     "%d cm²" % (a * b), "%d cm²" % (a + b),
                     "%d cm²" % (a * a - b * b),
                     "%d cm²" % (a * a + b * b + 1)), 0)


def diagonale(a, b):
    """Taisnstūra diagonāle - Pitagora teorēma citā figūrā."""
    d = int(round((a * a + b * b) ** 0.5))
    return ("Taisnstūra malas ir %d cm un %d cm. Cik gara ir diagonāle?"
            % (a, b),
            V.izvele("%d cm" % d, "%d cm" % (a + b), "%d cm" % (a * b),
                     "%d cm" % (d + 1), "%d cm" % (2 * (a + b)),
                     "%d cm" % (d - 1)), 0)


def vai_taisnlenka(a, b, c):
    """Vai trijstūris ar dotajām malām ir taisnleņķa."""
    ir = a * a + b * b == c * c
    return ("Vai trijstūris ar malām %d cm, %d cm un %d cm ir taisnleņķa?"
            % (a, b, c),
            V.izvele("jā" if ir else "nē", "nē" if ir else "jā",
                     "tikai vienādsānu", "nevar noteikt"), 0)


def sakne_atbilde(a, b):
    """Hipotenūza, kas nav vesels skaitlis - atbilde ar sakni."""
    s = a * a + b * b
    return ("Katetes ir %d cm un %d cm. Cik gara ir hipotenūza?" % (a, b),
            V.izvele("√%d cm" % s, "%d cm" % (a + b), "√%d cm" % (a + b),
                     "%d cm" % (a * b), "√%d cm" % (a * a - b * b),
                     "√%d cm" % (s + 1)), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.8. temata beigās. Pārbauda katetes un "
                "hipotenūzas jēdzienus, Pitagora teorēmu un tās lietojumu "
                "taisnleņķa trijstūrī un citās plaknes figūrās.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina taisnleņķa trijstūra malu nosaukumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc taisnā leņķa pretmalu?",
              ["hipotenūza", "katete", "pamats", "augstums"], 0),
             ("Kā sauc malas, kas veido taisno leņķi?",
              ["katetes", "hipotenūzas", "pamati", "mediānas"], 0),
             ("Kura ir taisnleņķa trijstūra garākā mala?",
              ["hipotenūza", "katete", "abas katetes", "tas ir dažādi"], 0),
             ("Cik kašetu ir taisnleņķa trijstūrim?",
              ["divas", "viena", "trīs", "neviena"], 0),
             ("Cik liela ir taisnleņķa trijstūra šauro leņķu summa?",
              ["90°", "180°", "45°", "120°"], 0),
             ("Vai taisnleņķa trijstūrim var būt plats leņķis?",
              ["nē", "jā", "tikai vienādsānu", "vienmēr"], 0),
             ("Vai taisnleņķa trijstūris var būt vienādsānu?",
              ["jā, ar leņķiem 90°, 45° un 45°", "nē",
               "tikai ar 60°", "nevar noteikt"], 0),
             ("Ar ko taisnleņķa trijstūrī sakrīt divi augstumi?",
              ["ar katetēm", "ar hipotenūzu", "ar mediānām",
               "ar bisektrisēm"], 0),
         ]},
        {"sr": "Zina Pitagora teorēmu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā skan Pitagora teorēma?",
              ["katešu kvadrātu summa ir hipotenūzas kvadrāts",
               "katešu summa ir hipotenūza",
               "malu kvadrātu summa ir nulle",
               "hipotenūza ir divas katetes"], 0),
             ("Ar kuru formulu to pieraksta?",
              ["a² + b² = c²", "a + b = c", "a² − b² = c²",
               "a · b = c"], 0),
             ("Kā aprēķina hipotenūzu?",
              ["c = √(a² + b²)", "c = a + b", "c = √(a² − b²)",
               "c = a · b"], 0),
             ("Kā aprēķina kateti?",
              ["a = √(c² − b²)", "a = c − b", "a = √(c² + b²)",
               "a = c · b"], 0),
             ("Kuram trijstūrim var lietot Pitagora teorēmu?",
              ["tikai taisnleņķa", "jebkuram", "tikai vienādsānu",
               "tikai vienādmalu"], 0),
             ("Ko izmanto Pitagora teorēmas vizuālajā pierādījumā?",
              ["kvadrātu laukumus", "leņķu summu", "perimetru",
               "tilpumu"], 0),
             ("Kurš malu trijnieks veido taisnleņķa trijstūri?",
              ["3; 4; 5", "2; 3; 4", "4; 5; 6", "5; 6; 7"], 0),
             ("Kāpēc hipotenūza ir garākā mala?",
              ["tās kvadrāts ir abu katešu kvadrātu summa",
               "tā ir definīcija", "tā atrodas apakšā",
               "tas nav tiesa"], 0),
         ]},
        {"sr": "Aprēķina hipotenūzu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(hipotenuza, [
             (3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24), (12, 16),
             (20, 21), (10, 24), (15, 20), (9, 40), (12, 35), (16, 30),
             (18, 24), (14, 48)]),
         },
        {"sr": "Aprēķina kateti",
         "stunda": TEMATS,
         "jautajumi": V.kopa(katete, [
             (5, 3), (10, 6), (13, 5), (17, 8), (15, 9), (25, 7),
             (20, 12), (29, 20), (26, 10), (25, 15), (41, 9), (37, 12),
             (34, 16), (30, 18), (50, 14)]),
         },
        {"sr": "Lieto katešu kvadrātu summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kvadrati, [
             (3, 4), (6, 8), (5, 12), (2, 3), (4, 5), (7, 24), (1, 2),
             (9, 12), (5, 6), (8, 15), (2, 5), (10, 24), (3, 7),
             (12, 16), (4, 9)]),
         },
        {"sr": "Aprēķina taisnstūra diagonāli",
         "stunda": TEMATS,
         "jautajumi": V.kopa(diagonale, [
             (3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24), (12, 16),
             (20, 21), (10, 24), (15, 20), (9, 40), (12, 35), (16, 30),
             (18, 24), (14, 48)]),
         },
        {"sr": "Nosaka, vai trijstūris ir taisnleņķa",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vai_taisnlenka, [
             (3, 4, 5), (2, 3, 4), (6, 8, 10), (4, 5, 6), (5, 12, 13),
             (7, 8, 9), (8, 15, 17), (5, 6, 8), (9, 12, 15), (6, 7, 10),
             (7, 24, 25), (10, 11, 14), (20, 21, 29), (8, 9, 12),
             (12, 16, 20)]),
         },
        {"sr": "Pieraksta atbildi ar kvadrātsakni",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sakne_atbilde, [
             (1, 2), (2, 3), (1, 3), (2, 5), (3, 5), (1, 4), (4, 5),
             (2, 6), (3, 7), (5, 6), (4, 7), (1, 5), (6, 7), (3, 8),
             (2, 7)]),
         },
        {"sr": "Lieto teorēmu citās figūrās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kvadrāta mala ir 5 cm. Cik gara ir diagonāle?",
              ["√50 cm", "10 cm", "25 cm", "5 cm"], 0),
             ("Vienādsānu trijstūra pamats ir 6 cm, sānu mala — 5 cm. Cik "
              "garš ir augstums pret pamatu?", ["4 cm", "3 cm", "8 cm",
                                                "11 cm"], 0),
             ("Kā Pitagora teorēmu lieto citā figūrā?",
              ["figūrā izdala taisnleņķa trijstūri", "mēra visas malas",
               "saskaita leņķus", "aprēķina laukumu"], 0),
             ("Romba diagonāles ir 6 cm un 8 cm. Cik gara ir mala?",
              ["5 cm", "7 cm", "10 cm", "14 cm"], 0),
             ("Kāpņu garums ir 5 m, apakšgals 3 m no sienas. Cik augstu "
              "tās sniedzas?", ["4 m", "2 m", "8 m", "6 m"], 0),
             ("Trapeces augstums ir 4 cm, sānu malas projekcija — 3 cm. "
              "Cik gara ir sānu mala?", ["5 cm", "7 cm", "1 cm", "12 cm"],
              0),
             ("Punkti A(0; 0) un B(3; 4). Cik garš ir nogrieznis AB?",
              ["5", "7", "12", "25"], 0),
             ("Ko zīmē, lai lietotu teorēmu sarežģītākā figūrā?",
              ["palīglīnijas", "krāsainas malas", "leņķu lokus",
               "papildu punktus uz asīm"], 0),
         ]},
        {"sr": "Konstruē taisnleņķa trijstūri",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko konstruē taisnleņķa trijstūri?",
              ["ar cirkuli un lineālu bez skalas", "ar transportieri",
               "ar lineālu ar skalu", "no acs"], 0),
             ("Kas jāuzkonstruē vispirms?",
              ["taisns leņķis", "hipotenūza", "augstums", "mediāna"], 0),
             ("Kā konstruē perpendikulu?",
              ["ar cirkuli no punkta pret taisni", "ar transportieri",
               "ar lineālu", "no acs"], 0),
             ("Cik elementi jāzina, lai konstruētu taisnleņķa trijstūri?",
              ["divi (bez taisnā leņķa)", "viens", "visi seši",
               "neviens"], 0),
             ("Kā pierāda divu taisnleņķa trijstūru vienādību?",
              ["lietojot trijstūru vienādības pazīmes",
               "izmērot tos", "salīdzinot laukumus",
               "salīdzinot perimetru"], 0),
             ("Ar ko zīmējumā apzīmē taisno leņķi?",
              ["ar kvadrātiņu", "ar lociņu", "ar punktu", "ar bultiņu"], 0),
             ("Kāpēc risinājumā zīmē skici?",
              ["lai saprastu, kas dots un kas meklēts", "lai būtu skaisti",
               "lai aizpildītu lapu", "tas nav vajadzīgs"], 0),
             ("Kā ar Pitagora teorēmu konstruē nogriezni ar garumu √2?",
              ["kā taisnleņķa trijstūra ar katetēm 1 un 1 hipotenūzu",
               "izmērot ar lineālu", "dalot nogriezni uz pusēm",
               "ar transportieri"], 0),
         ]},
        {"sr": "Pārbauda rezultāta ticamību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Aprēķinā hipotenūza sanāca īsāka nekā katete. Ko tas nozīmē?",
              ["risinājumā ir kļūda", "tā mēdz būt",
               "trijstūris ir vienādsānu", "katete ir hipotenūza"], 0),
             ("Vai hipotenūza var būt vienāda ar kateti?",
              ["nē", "jā", "tikai vienādsānu", "vienmēr"], 0),
             ("Katetes ir 3 cm un 4 cm; aprēķināja hipotenūzu 7 cm. Vai "
              "pareizi?", ["nē, jābūt 5 cm", "jā", "nē, jābūt 12 cm",
                           "nevar noteikt"], 0),
             ("Kā ātri pārbaudīt atbildi?",
              ["hipotenūzai jābūt garākajai malai", "jāsaskaita leņķi",
               "jāizmēra ar lineālu", "jānoapaļo"], 0),
             ("Vai malu garums var būt negatīvs?",
              ["nē", "jā", "tikai aprēķinos", "tikai koordinātās"], 0),
             ("Ko dara, ja atbilde nav vesels skaitlis?",
              ["atstāj to kā kvadrātsakni vai noapaļo", "maina uzdevumu",
               "noapaļo līdz veselam vienmēr", "atmet atbildi"], 0),
             ("Kāpēc atbildē norāda mērvienību?",
              ["bez tās rezultāts nav pilnīgs", "lai būtu garāk",
               "tā prasa skolotājs", "tas nav vajadzīgs"], 0),
             ("Katetes 5 cm un 12 cm. Vai hipotenūza var būt 13 cm?",
              ["jā", "nē", "tikai aptuveni", "nevar noteikt"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Masts ir 12 m augsts; troses apakšgals 9 m no pamatnes. Cik "
              "gara ir trose?", ["15 m", "21 m", "3 m", "108 m"], 0),
             ("Futbola laukums 30 m un 40 m. Cik gara ir diagonāle?",
              ["50 m", "70 m", "10 m", "1200 m"], 0),
             ("Kāpnes 13 m; augšgals 12 m augstumā. Cik tālu no sienas ir "
              "apakšgals?", ["5 m", "1 m", "25 m", "156 m"], 0),
             ("Ceļš 3 km uz ziemeļiem un 4 km uz austrumiem. Cik tālu no "
              "sākuma?", ["5 km", "7 km", "1 km", "12 km"], 0),
             ("Ekrāna malas 16 cm un 12 cm. Cik gara ir diagonāle?",
              ["20 cm", "28 cm", "4 cm", "192 cm"], 0),
             ("Dārza stūris: malas 6 m un 8 m. Cik garš ir taisnais ceļš?",
              ["10 m", "14 m", "2 m", "48 m"], 0),
             ("Vārti 24 dm plati, 7 dm augsti. Cik gara ir diagonāle?",
              ["25 dm", "31 dm", "17 dm", "168 dm"], 0),
             ("Kāds ir pirmais solis situāciju uzdevumā?",
              ["uzzīmēt skici ar taisnleņķa trijstūri", "noapaļot skaitļus",
               "aprēķināt laukumu", "izmērīt leņķi"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.8. temata noslēgumā. "
                "Pārbauda Pitagora teorēmu, nezināmās malas aprēķināšanu, "
                "teorēmas lietojumu citās figūrās un situāciju uzdevumus.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina Pitagora teorēmu un malu nosaukumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc taisnā leņķa pretmalu?",
              ["hipotenūza", "katete", "pamats", "augstums"], 0),
             ("Kā skan Pitagora teorēma?",
              ["katešu kvadrātu summa ir hipotenūzas kvadrāts",
               "katešu summa ir hipotenūza",
               "malu kvadrātu summa ir nulle",
               "hipotenūza ir divas katetes"], 0),
             ("Kā aprēķina hipotenūzu?",
              ["c = √(a² + b²)", "c = a + b", "c = √(a² − b²)",
               "c = a · b"], 0),
             ("Kā aprēķina kateti?",
              ["a = √(c² − b²)", "a = c − b", "a = √(c² + b²)",
               "a = c · b"], 0),
             ("Kuram trijstūrim var lietot Pitagora teorēmu?",
              ["tikai taisnleņķa", "jebkuram", "tikai vienādsānu",
               "tikai vienādmalu"], 0),
             ("Kurš malu trijnieks veido taisnleņķa trijstūri?",
              ["3; 4; 5", "2; 3; 4", "4; 5; 6", "5; 6; 7"], 0),
             ("Vai hipotenūza var būt īsāka nekā katete?",
              ["nē", "jā", "tikai vienādsānu", "nevar noteikt"], 0),
             ("Cik liela ir taisnleņķa trijstūra šauro leņķu summa?",
              ["90°", "180°", "45°", "120°"], 0),
         ]},
        {"sr": "Aprēķina hipotenūzu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(hipotenuza, [
             (3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24), (12, 16),
             (20, 21), (10, 24), (15, 20), (9, 40), (12, 35), (16, 30),
             (18, 24), (14, 48)]),
         },
        {"sr": "Aprēķina kateti",
         "stunda": TEMATS,
         "jautajumi": V.kopa(katete, [
             (5, 4), (10, 8), (13, 12), (17, 15), (15, 12), (25, 24),
             (20, 16), (29, 21), (26, 24), (25, 20), (41, 40), (37, 35),
             (34, 30), (30, 24), (50, 48)]),
         },
        {"sr": "Aprēķina diagonāli un kvadrātu summu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(diagonale, [
             (3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24), (12, 16)])
             + V.kopa(kvadrati, [
                 (2, 3), (4, 5), (1, 2), (5, 6), (2, 5), (3, 7), (4, 9),
                 (1, 4)])),
         },
        {"sr": "Nosaka, vai trijstūris ir taisnleņķa",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vai_taisnlenka, [
             (3, 4, 5), (2, 3, 4), (6, 8, 10), (4, 5, 6), (5, 12, 13),
             (7, 8, 9), (8, 15, 17), (5, 6, 8), (9, 12, 15), (6, 7, 10),
             (7, 24, 25), (10, 11, 14), (20, 21, 29), (8, 9, 12),
             (12, 16, 20)]),
         },
        {"sr": "Lieto teorēmu situācijās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Masts ir 12 m augsts; troses apakšgals 9 m no pamatnes. Cik "
              "gara ir trose?", ["15 m", "21 m", "3 m", "108 m"], 0),
             ("Futbola laukums 30 m un 40 m. Cik gara ir diagonāle?",
              ["50 m", "70 m", "10 m", "1200 m"], 0),
             ("Kāpnes 13 m; augšgals 12 m augstumā. Cik tālu no sienas ir "
              "apakšgals?", ["5 m", "1 m", "25 m", "156 m"], 0),
             ("Ekrāna malas 16 cm un 12 cm. Cik gara ir diagonāle?",
              ["20 cm", "28 cm", "4 cm", "192 cm"], 0),
             ("Kvadrāta mala ir 5 cm. Cik gara ir diagonāle?",
              ["√50 cm", "10 cm", "25 cm", "5 cm"], 0),
             ("Romba diagonāles ir 6 cm un 8 cm. Cik gara ir mala?",
              ["5 cm", "7 cm", "10 cm", "14 cm"], 0),
             ("Punkti A(0; 0) un B(3; 4). Cik garš ir nogrieznis AB?",
              ["5", "7", "12", "25"], 0),
             ("Kāds ir pirmais solis situāciju uzdevumā?",
              ["uzzīmēt skici ar taisnleņķa trijstūri",
               "noapaļot skaitļus", "aprēķināt laukumu",
               "izmērīt leņķi"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina taisnleņķa trijstūra malas",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Pitagora teorēma",
             lambda a, b, c: [
                 ("Katetes %d cm un %d cm;  c = …… cm" % (a, b), V.sk(c)),
                 ("Hipotenūza %d cm, katete %d cm;  otra katete …… cm"
                  % (c, a), V.sk(b)),
                 ("Katetes %d cm un %d cm;  c² = …… cm²" % (a, b),
                  V.sk(c * c)),
                 ("Taisnstūris %d cm un %d cm;  diagonāle …… cm" % (a, b),
                  V.sk(c))],
             [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15),
              (7, 24, 25), (12, 16, 20), (20, 21, 29), (10, 24, 26),
              (15, 20, 25), (9, 40, 41), (12, 35, 37), (16, 30, 34),
              (18, 24, 30), (14, 48, 50)]),
         },
        {"sr": "Nosaka trijstūra veidu pēc malām",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Vai taisnleņķa?",
             lambda a, b, c, d: [
                 ("Malas %d; %d; %d cm — taisnleņķa?   ……" % (a, b, c),
                  "jā"),
                 ("Malas %d; %d; %d cm — taisnleņķa?   ……"
                  % (a, b, c + d), "nē"),
                 ("Katetes %d un %d cm;  hipotenūzas kvadrāts …… cm²"
                  % (a, b), V.sk(c * c))],
             [(3, 4, 5, 1), (6, 8, 10, 2), (5, 12, 13, 1), (8, 15, 17, 2),
              (9, 12, 15, 1), (7, 24, 25, 2), (12, 16, 20, 1),
              (20, 21, 29, 2), (10, 24, 26, 1), (15, 20, 25, 2),
              (9, 40, 41, 1), (12, 35, 37, 2), (16, 30, 34, 1),
              (18, 24, 30, 2), (14, 48, 50, 1)]),
         },
        {"sr": "Risina situāciju uzdevumu ar Pitagora teorēmu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda a, b, c: {
                 "teksts": "Taisnstūrveida laukuma malas ir %d m un %d m.  "
                           " a) Uzzīmē skici un atzīmē diagonāli!   "
                           "b) Aprēķini diagonāles garumu!   c) Cik garš ir "
                           "laukuma perimetrs?   d) Par cik metriem ceļš pa "
                           "diagonāli ir īsāks nekā pa divām malām?"
                           % (a, b),
                 "kriteriji": [
                     "a) Skice ar taisnleņķa trijstūri.   (1 p.)",
                     "b) d = √(%d² + %d²) = %d m.   (1 p.)" % (a, b, c),
                     "c) 2 · (%d + %d) = %d m.   (1 p.)"
                     % (a, b, 2 * (a + b)),
                     "d) %d + %d − %d = %d m.   (1 p.)"
                     % (a, b, c, a + b - c)]},
             [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15),
              (7, 24, 25), (12, 16, 20), (20, 21, 29), (10, 24, 26),
              (15, 20, 25), (9, 40, 41), (12, 35, 37), (16, 30, 34),
              (18, 24, 30), (14, 48, 50)]),
         },
        {"sr": "Pamato risinājuma gaitu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Vienādsānu trijstūris",
             lambda pamats, sanu, h: {
                 "ievads": "Vienādsānu trijstūra pamats ir %d cm, sānu "
                           "mala — %d cm." % (pamats, sanu),
                 "jaut": [("Cik gara ir pamata puse?", 1),
                          ("Aprēķini augstumu pret pamatu!", 1),
                          ("Aprēķini trijstūra laukumu!", 1)],
                 "atbildes": [
                     "1) %d : 2 = %s cm.   (1 p.)"
                     % (pamats, V.dalu(pamats, 2)),
                     "2) √(%d² − %s²) = %d cm.   (1 p.)"
                     % (sanu, V.dalu(pamats, 2), h),
                     "3) %d · %d : 2 = %s cm².   (1 p.)"
                     % (pamats, h, V.dalu(pamats * h, 2))]},
             [(6, 5, 4), (16, 10, 6), (10, 13, 12), (30, 17, 8),
              (24, 15, 9), (14, 25, 24), (24, 20, 16), (42, 29, 20),
              (20, 26, 24), (30, 25, 20), (18, 41, 40), (24, 37, 35),
              (32, 34, 30), (36, 30, 24), (28, 50, 48)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
