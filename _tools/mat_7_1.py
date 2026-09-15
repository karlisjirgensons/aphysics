# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.1. Kopas elementi un notikuma varbūtība.

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.1. temats): kopa, apakškopa,
kopu apvienojums un šķēlums, izlase un tās secības nozīme, reizināšanas
likums komplektu skaitīšanai, pilnā pārlase, droši un neiespējami notikumi un
notikuma varbūtības aprēķināšana.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.1."
NOSAUKUMS = "Kā nosaka kopas visus elementus, aprēķina notikuma varbūtību?"

ATGADNE = [
    "Kopu apraksta ar elementu sarakstu vai ar īpašību:   A = {2; 4; 6}   ·  "
    " apvienojumā A ∪ B ir visi elementi, šķēlumā A ∩ B — tikai kopīgie.",
    "Reizināšanas likums: ja vienu izvēlas a veidos, otru — b veidos, tad "
    "pāri var izvēlēties a · b veidos.",
    "Varbūtība:   P = {labvēlīgo iznākumu skaits|visu iznākumu skaits}   ·  "
    " drošam notikumam P = 1, neiespējamam P = 0, pārējiem 0 < P < 1.",
]


# ---------------------------------------------------------------- veidnes
def varbutiba(a, b, krasa1, krasa2):
    """Varbūtība izvilkt vienu no divām krāsām - pamata varbūtības uzdevums."""
    return ("Somā ir %d %s un %d %s bumbiņas. Kāda ir varbūtība izvilkt "
            "%s bumbiņu?" % (a, krasa1, b, krasa2, krasa1[:-1] + "u"),
            V.izvele(V.dalu(a, a + b), V.dalu(b, a + b), V.dalu(a, b),
                     V.dalu(a + b, a), V.dalu(1, a + b),
                     V.dalu(a, a + b + 1)), 0)


def kaulins(n, nosac, labv):
    """Varbūtība, metot kauliņu ar n skaldnēm."""
    return ("Met kauliņu ar %d skaldnēm. Kāda ir varbūtība, ka uzkrīt %s?"
            % (n, nosac),
            V.izvele(V.dalu(labv, n), V.dalu(n - labv, n), V.dalu(n, labv),
                     V.dalu(1, n), V.dalu(labv, n + 1),
                     V.dalu(labv + 1, n)), 0)


def komplekti(a, b, ko1, ko2):
    """Reizināšanas likums diviem objektiem."""
    return ("Ir %d %s un %d %s. Cik dažādus komplektus var izveidot?"
            % (a, ko1, b, ko2),
            V.izvele(a * b, a + b, a * b + 1, abs(a - b), a * b * 2), 0)


def komplekti3(a, b, c):
    """Reizināšanas likums trim objektiem."""
    return ("Ēdienkartē ir %d zupas, %d otrie ēdieni un %d deserti. Cik "
            "dažādas pusdienas var izvēlēties?" % (a, b, c),
            V.izvele(a * b * c, a + b + c, a * b + c, a * (b + c),
                     a * b * c + 1), 0)


def apvienojums(a, b):
    """Cik elementu ir apvienojumā, ja daži elementi ir kopīgi."""
    kopigie = min(a, b) // 2 or 1
    return ("Kopā A ir %d elementi, kopā B — %d; kopīgi tiem ir %d "
            "elementi. Cik elementu ir apvienojumā A ∪ B?"
            % (a, b, kopigie),
            V.izvele(a + b - kopigie, a + b, a + b + kopigie, abs(a - b),
                     kopigie), 0)


def parlase(cipari, vietas):
    """Cik skaitļu var izveidot, ja ciparus drīkst atkārtot."""
    return ("No %d dažādiem cipariem veido %d ciparu skaitli; ciparus drīkst "
            "atkārtot. Cik tādu skaitļu ir?" % (cipari, vietas),
            V.izvele(cipari ** vietas, cipari * vietas, cipari + vietas,
                     vietas ** cipari, cipari ** vietas - 1), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.1. temata beigās. Pārbauda kopas "
                "jēdzienu, apakškopas, apvienojumu un šķēlumu, reizināšanas "
                "likumu, pilno pārlasi un notikuma varbūtības aprēķināšanu.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, kas ir kopa un kā to apraksta",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā var aprakstīt kopu?",
              ["ar elementu sarakstu vai ar īpašību", "tikai ar zīmējumu",
               "tikai ar skaitli", "tikai ar burtu"], 0),
             ("Kā pieraksta kopu ar elementiem 2; 4 un 6?",
              ["A = {2; 4; 6}", "A = (2; 4; 6)", "A = 2 + 4 + 6",
               "A = 2 · 4 · 6"], 0),
             ("Cik elementu ir kopā {1; 3; 5; 7}?", ["4", "7", "16", "3"], 0),
             ("Kura kopa ir pāra skaitļu kopa no 1 līdz 10?",
              ["{2; 4; 6; 8; 10}", "{1; 3; 5; 7; 9}", "{1; 2; 3}",
               "{10}"], 0),
             ("Kas ir tukša kopa?",
              ["kopa bez elementiem", "kopa ar vienu elementu",
               "kopa ar nulli", "kopa ar visiem skaitļiem"], 0),
             ("Kā apzīmē, ka 3 pieder kopai A?",
              ["3 ∈ A", "3 ∉ A", "3 ∪ A", "3 ∩ A"], 0),
             ("Kas ir apakškopa?",
              ["kopa, kuras visi elementi pieder citai kopai",
               "kopa ar mazāk nekā 3 elementiem", "tukša kopa",
               "kopu apvienojums"], 0),
             ("Vai {2; 4} ir kopas {2; 4; 6} apakškopa?",
              ["jā", "nē", "tikai ar 6", "nevar noteikt"], 0),
         ]},
        {"sr": "Nosaka kopu apvienojumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(apvienojums, [
             (8, 6), (10, 7), (12, 9), (5, 4), (14, 8), (9, 6), (11, 5),
             (16, 10), (7, 6), (13, 8), (15, 9), (6, 4), (18, 12),
             (20, 14), (17, 11)]),
         },
        {"sr": "Nosaka kopu šķēlumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir kopu šķēlums A ∩ B?",
              ["tikai kopīgie elementi", "visi elementi",
               "tikai A elementi", "tikai B elementi"], 0),
             ("Kāds ir kopu {1; 2; 3} un {2; 3; 4} šķēlums?",
              ["{2; 3}", "{1; 4}", "{1; 2; 3; 4}", "tukša kopa"], 0),
             ("Kāds ir kopu {1; 2} un {5; 6} šķēlums?",
              ["tukša kopa", "{1; 2}", "{5; 6}", "{1; 2; 5; 6}"], 0),
             ("Kāds ir kopu {2; 4; 6} un {4; 6; 8} šķēlums?",
              ["{4; 6}", "{2; 8}", "{2; 4; 6; 8}", "tukša kopa"], 0),
             ("Kāds ir kopu {1; 2; 3} un {1; 2; 3} šķēlums?",
              ["{1; 2; 3}", "tukša kopa", "{1}", "{3}"], 0),
             ("Klasē 12 skolēni spēlē futbolu, 9 — basketbolu, 5 — abus. "
              "Cik spēlē tikai futbolu?", ["7", "12", "16", "5"], 0),
             ("Tajā pašā klasē cik spēlē tikai basketbolu?",
              ["4", "9", "5", "14"], 0),
             ("Tajā pašā klasē cik spēlē vismaz vienu spēli?",
              ["16", "21", "26", "5"], 0),
         ]},
        {"sr": "Lieto reizināšanas likumu diviem objektiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(komplekti, [
             (3, 4, "kreklu", "bikses"), (5, 3, "cepures", "šalles"),
             (4, 6, "krūzes", "karotītes"), (2, 7, "jakas", "cimdu pāri"),
             (6, 5, "burtnīcas", "pildspalvas"),
             (3, 8, "somas", "atslēgu piekariņi"),
             (7, 2, "grāmatas", "grāmatzīmes"),
             (4, 4, "šķīvji", "glāzes"), (5, 6, "zeķu pāri", "kurpes"),
             (8, 3, "krāsas", "otas"), (2, 9, "galdi", "krēsli"),
             (6, 7, "aploksnes", "pastmarkas"),
             (9, 2, "kartes", "aploksnes"), (3, 9, "krūzes", "tējas maisiņi"),
             (10, 4, "burtnīcas", "vāciņi")]),
         },
        {"sr": "Lieto reizināšanas likumu trim objektiem",
         "stunda": TEMATS,
         "jautajumi": V.kopa(komplekti3, [
             (3, 4, 2), (2, 5, 3), (4, 3, 5), (5, 2, 4), (3, 6, 2),
             (2, 4, 6), (6, 3, 2), (4, 5, 3), (3, 3, 7), (5, 4, 2),
             (2, 8, 3), (7, 2, 4), (4, 4, 4), (6, 5, 2), (3, 5, 6)]),
         },
        {"sr": "Lieto pilno pārlasi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(parlase, [
             (3, 2), (4, 2), (5, 2), (2, 3), (3, 3), (6, 2), (2, 4),
             (7, 2), (4, 3), (8, 2), (2, 5), (5, 3), (9, 2), (3, 4),
             (10, 2)]),
         },
        {"sr": "Spriež par izlases secību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad izlasē secībai ir nozīme?",
              ["kad objektiem ir dažādas lomas", "vienmēr", "nekad",
               "kad objektu ir vairāk nekā 3"], 0),
             ("Vai secībai ir nozīme, izvēloties komandas kapteini un "
              "vietnieku?", ["jā", "nē", "tikai lielā komandā",
                             "nevar noteikt"], 0),
             ("Vai secībai ir nozīme, izvēloties divus dežurantus?",
              ["nē", "jā", "tikai klasē", "nevar noteikt"], 0),
             ("Cik veidos no 5 skolēniem var izvēlēties kapteini un "
              "vietnieku?", ["20", "25", "10", "5"], 0),
             ("Cik veidos no 4 skolēniem var izvēlēties divus dežurantus?",
              ["6", "12", "8", "4"], 0),
             ("Kā sauc visu objektu uzskaitījumu?",
              ["pilnā pārlase", "izlase", "apakškopa", "šķēlums"], 0),
             ("Kāpēc pārlasi organizē pēc kārtas?",
              ["lai neko neizlaistu un neatkārtotu", "lai būtu ātrāk",
               "lai skaitļi būtu mazāki", "tas nav vajadzīgs"], 0),
             ("Ar ko pārlasi ir ērti attēlot?",
              ["ar tabulu vai grafu", "ar skaitļu taisni",
               "ar sektoru diagrammu", "ar formulu"], 0),
         ]},
        {"sr": "Zina, kas ir varbūtība",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko rāda notikuma varbūtība?",
              ["cik iespējams ir notikums", "cik reižu notikums notika",
               "cik objektu ir kopā", "cik ilgi notikums turpinās"], 0),
             ("Kāda ir droša notikuma varbūtība?", ["1", "0", "0,5",
                                                    "100"], 0),
             ("Kāda ir neiespējama notikuma varbūtība?",
              ["0", "1", "0,5", "−1"], 0),
             ("Kādās robežās ir jebkura varbūtība?",
              ["no 0 līdz 1", "no 0 līdz 100", "no −1 līdz 1",
               "no 1 līdz 10"], 0),
             ("Kurš notikums ir drošs?",
              ["metot kauliņu, uzkrīt mazāk nekā 7",
               "metot kauliņu, uzkrīt 7", "metot monētu, uzkrīt mala",
               "rīt snigs"], 0),
             ("Kurš notikums ir neiespējams?",
              ["metot kauliņu, uzkrīt 8", "metot kauliņu, uzkrīt 6",
               "metot monētu, uzkrīt cipars", "rīt līs"], 0),
             ("Kā varbūtību var noteikt eksperimentāli?",
              ["daudzkārt atkārtojot mēģinājumu", "aprēķinot ar formulu",
               "uzminot", "jautājot skolotājam"], 0),
             ("Ar ko aizvieto vārdu «varbūtība» sadzīvē?",
              ["«iespēja», «izredzes»", "«skaits»", "«laiks»",
               "«mērvienība»"], 0),
         ]},
        {"sr": "Aprēķina varbūtību, velkot bumbiņu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(varbutiba, [
             (3, 5, "sarkanas", "zilas"), (4, 6, "zaļas", "dzeltenas"),
             (2, 8, "baltas", "melnas"), (5, 7, "sarkanas", "zaļas"),
             (6, 4, "zilas", "baltas"), (7, 3, "dzeltenas", "melnas"),
             (3, 9, "zaļas", "sarkanas"), (8, 4, "melnas", "baltas"),
             (5, 10, "sarkanas", "dzeltenas"), (9, 6, "zilas", "zaļas"),
             (4, 12, "baltas", "sarkanas"), (6, 9, "dzeltenas", "zilas"),
             (2, 6, "melnas", "zaļas"), (10, 5, "sarkanas", "baltas"),
             (7, 8, "zaļas", "melnas")]),
         },
        {"sr": "Aprēķina varbūtību, metot kauliņu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(kaulins, [
             (6, "pāra skaitlis", 3), (6, "skaitlis 5", 1),
             (6, "skaitlis, lielāks nekā 4", 2),
             (6, "skaitlis, mazāks nekā 3", 2), (6, "nepāra skaitlis", 3),
             (6, "skaitlis, dalāms ar 3", 2), (8, "pāra skaitlis", 4),
             (8, "skaitlis 7", 1), (8, "skaitlis, lielāks nekā 6", 2),
             (10, "pāra skaitlis", 5), (10, "skaitlis, mazāks nekā 4", 3),
             (12, "skaitlis, dalāms ar 4", 3), (12, "pāra skaitlis", 6),
             (20, "skaitlis, dalāms ar 5", 4),
             (20, "skaitlis, lielāks nekā 15", 5)]),
         },
        {"sr": "Aprēķina varbūtību citās situācijās",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda ir varbūtība, ka, metot monētu, uzkrīt cipars?",
              ["{1|2}", "{1|4}", "1", "0"], 0),
             ("Klasē ir 25 skolēni, 10 no tiem meitenes. Kāda ir varbūtība "
              "izvēlēties meiteni?", ["{2|5}", "{3|5}", "{5|2}",
                                      "{10|15}"], 0),
             ("Somā ir 12 burtnīcas, 4 no tām rūtiņu. Kāda ir varbūtība "
              "izvilkt rūtiņu burtnīcu?", ["{1|3}", "{2|3}", "{1|4}",
                                           "{3|1}"], 0),
             ("Kastē ir 20 kartītes ar skaitļiem 1–20. Kāda ir varbūtība "
              "izvilkt pāra skaitli?", ["{1|2}", "{1|4}", "{1|10}",
                                        "{1|20}"], 0),
             ("Tajā pašā kastē — varbūtība izvilkt skaitli, dalāmu ar 5?",
              ["{1|5}", "{1|4}", "{1|10}", "{4|5}"], 0),
             ("Kāda ir varbūtība, ka, metot divas monētas, abām uzkrīt "
              "cipars?", ["{1|4}", "{1|2}", "{1|3}", "{3|4}"], 0),
             ("Ratā ir 8 vienādi sektori, 2 no tiem sarkani. Kāda ir "
              "varbūtība apstāties sarkanajā?", ["{1|4}", "{1|8}", "{3|4}",
                                                 "{1|2}"], 0),
             ("Varbūtība uzvarēt ir {1|5}. Kāda ir varbūtība neuzvarēt?",
              ["{4|5}", "{1|5}", "{5|1}", "0"], 0),
         ]},
        {"sr": "Spriež par varbūtību sadzīvē",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko nozīmē varbūtība 0,5?",
              ["notikums ir tikpat iespējams kā nenotikšana",
               "notikums noteikti notiks", "notikums nekad nenotiks",
               "notikums notiks 5 reizes"], 0),
             ("Kurš notikums ir iespējamāks: varbūtība 0,7 vai 0,3?",
              ["ar varbūtību 0,7", "ar varbūtību 0,3", "abi vienādi",
               "nevar salīdzināt"], 0),
             ("Vai varbūtība var būt 1,5?",
              ["nē", "jā", "tikai eksperimentā", "tikai teorētiski"], 0),
             ("Vai varbūtība var būt negatīva?",
              ["nē", "jā", "tikai sadzīvē", "tikai aprēķinos"], 0),
             ("Ko nozīmē «lietus varbūtība 80 %»?",
              ["lietus ir ļoti iespējams", "lietus noteikti būs",
               "lietus nebūs", "lietus ilgs 80 minūtes"], 0),
             ("Cik ir visu iespējamo iznākumu varbūtību summa?",
              ["1", "0", "100", "tas ir dažādi"], 0),
             ("Kā mainās varbūtība, ja labvēlīgo iznākumu kļūst vairāk?",
              ["tā pieaug", "tā sarūk", "tā nemainās", "tā kļūst 0"], 0),
             ("Kā mainās varbūtība, ja visu iznākumu kļūst vairāk?",
              ["tā sarūk", "tā pieaug", "tā nemainās", "tā kļūst 1"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.1. temata noslēgumā. "
                "Pārbauda darbības ar kopām, reizināšanas likumu, pilno "
                "pārlasi un notikuma varbūtības aprēķināšanu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina kopu jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā var aprakstīt kopu?",
              ["ar elementu sarakstu vai ar īpašību", "tikai ar zīmējumu",
               "tikai ar skaitli", "tikai ar burtu"], 0),
             ("Kas ir apakškopa?",
              ["kopa, kuras visi elementi pieder citai kopai",
               "kopa ar mazāk nekā 3 elementiem", "tukša kopa",
               "kopu apvienojums"], 0),
             ("Kas ir kopu šķēlums A ∩ B?",
              ["tikai kopīgie elementi", "visi elementi",
               "tikai A elementi", "tikai B elementi"], 0),
             ("Kāds ir kopu {3; 5; 7} un {5; 7; 9} šķēlums?",
              ["{5; 7}", "{3; 9}", "{3; 5; 7; 9}", "tukša kopa"], 0),
             ("Cik elementu ir kopā {2; 4; 6; 8; 10}?",
              ["5", "10", "25", "2"], 0),
             ("Kā apzīmē kopu apvienojumu?",
              ["A ∪ B", "A ∩ B", "A · B", "A + B"], 0),
             ("Vai {1; 3} ir kopas {1; 2; 3} apakškopa?",
              ["jā", "nē", "tikai ar 2", "nevar noteikt"], 0),
             ("Kas ir tukša kopa?",
              ["kopa bez elementiem", "kopa ar vienu elementu",
               "kopa ar nulli", "kopa ar visiem skaitļiem"], 0),
         ]},
        {"sr": "Nosaka kopu apvienojumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(apvienojums, [
             (9, 7), (11, 8), (13, 10), (6, 5), (15, 9), (10, 7), (12, 6),
             (17, 11), (8, 7), (14, 9), (16, 10), (7, 5), (19, 13),
             (21, 15), (18, 12)]),
         },
        {"sr": "Lieto reizināšanas likumu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(komplekti, [
             (4, 5, "kreklu", "bikses"), (6, 3, "cepures", "šalles"),
             (5, 6, "krūzes", "karotītes"), (3, 7, "jakas", "cimdu pāri"),
             (7, 4, "burtnīcas", "pildspalvas"),
             (2, 8, "somas", "piekariņi"), (9, 3, "grāmatas", "grāmatzīmes")])
             + V.kopa(komplekti3, [
                 (2, 3, 4), (3, 4, 5), (4, 2, 6), (5, 3, 2), (2, 6, 3),
                 (3, 3, 4), (6, 2, 5), (4, 4, 2)])),
         },
        {"sr": "Lieto pilno pārlasi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(parlase, [
             (3, 2), (4, 2), (5, 2), (2, 3), (3, 3), (6, 2), (2, 4),
             (7, 2), (4, 3), (8, 2), (2, 5), (5, 3), (9, 2), (3, 4),
             (10, 2)]),
         },
        {"sr": "Aprēķina varbūtību",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(varbutiba, [
             (4, 5, "sarkanas", "zilas"), (3, 7, "zaļas", "dzeltenas"),
             (5, 9, "baltas", "melnas"), (6, 11, "sarkanas", "zaļas"),
             (2, 10, "zilas", "baltas"), (8, 2, "dzeltenas", "melnas"),
             (9, 3, "zaļas", "sarkanas")])
             + V.kopa(kaulins, [
                 (6, "pāra skaitlis", 3), (6, "skaitlis 2", 1),
                 (6, "skaitlis, lielāks nekā 3", 3),
                 (8, "nepāra skaitlis", 4), (10, "skaitlis 10", 1),
                 (12, "skaitlis, dalāms ar 3", 4),
                 (20, "skaitlis, dalāms ar 10", 2),
                 (6, "skaitlis, mazāks nekā 5", 4)])),
         },
        {"sr": "Spriež par varbūtības vērtību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāda ir droša notikuma varbūtība?", ["1", "0", "0,5",
                                                    "100"], 0),
             ("Kāda ir neiespējama notikuma varbūtība?",
              ["0", "1", "0,5", "−1"], 0),
             ("Kādās robežās ir jebkura varbūtība?",
              ["no 0 līdz 1", "no 0 līdz 100", "no −1 līdz 1",
               "no 1 līdz 10"], 0),
             ("Varbūtība uzvarēt ir {2|7}. Kāda ir varbūtība neuzvarēt?",
              ["{5|7}", "{2|7}", "{7|2}", "0"], 0),
             ("Vai varbūtība var būt 1,2?",
              ["nē", "jā", "tikai eksperimentā", "tikai teorētiski"], 0),
             ("Cik ir visu iespējamo iznākumu varbūtību summa?",
              ["1", "0", "100", "tas ir dažādi"], 0),
             ("Kā mainās varbūtība, ja labvēlīgo iznākumu kļūst vairāk?",
              ["tā pieaug", "tā sarūk", "tā nemainās", "tā kļūst 0"], 0),
             ("Kā varbūtību var noteikt eksperimentāli?",
              ["daudzkārt atkārtojot mēģinājumu", "aprēķinot ar formulu",
               "uzminot", "jautājot skolotājam"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Nosaka kopu elementus un komplektu skaitu",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, b, kop, x, y: [
                 ("Kopā {%s} ir …… elementi" % kop, V.sk(len(kop.split(";")))),
                 ("%d krekli un %d bikses dod …… komplektus" % (a, b),
                  V.sk(a * b)),
                 ("No %d cipariem %d ciparu skaitļi:  ……" % (x, y),
                  V.sk(x ** y)),
                 ("Kopām ar %d un %d elementiem, %d kopīgiem, apvienojumā "
                  "ir ……" % (a + 4, b + 3, 2), V.sk(a + b + 5))],
             [(3, 4, "2; 4; 6", 3, 2), (5, 3, "1; 3; 5; 7", 4, 2),
              (4, 6, "2; 5; 8", 5, 2), (2, 7, "1; 2; 3; 4; 5", 2, 3),
              (6, 5, "10; 20", 3, 3), (3, 8, "1; 4; 9; 16", 6, 2),
              (7, 2, "5; 10; 15", 2, 4), (4, 4, "3; 6; 9; 12", 7, 2),
              (5, 6, "1; 2", 4, 3), (8, 3, "2; 3; 5; 7; 11", 8, 2),
              (2, 9, "0; 1; 2", 2, 5), (6, 7, "4; 8; 12; 16", 5, 3),
              (9, 2, "1; 10; 100", 9, 2), (3, 9, "6; 12; 18", 3, 4),
              (10, 4, "1; 2; 3; 4; 5; 6", 10, 2)]),
         },
        {"sr": "Aprēķina varbūtību",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Varbūtība",
             lambda a, b, n, labv: [
                 ("Somā %d sarkanas un %d zilas; P(sarkana) = ……" % (a, b),
                  V.dalu(a, a + b)),
                 ("Tajā pašā somā  P(zila) = ……", V.dalu(b, a + b)),
                 ("Kauliņam ar %d skaldnēm  P(dalās ar %d) = ……"
                  % (n, labv), V.dalu(n // labv, n))],
             [(3, 5, 6, 2), (4, 6, 6, 3), (2, 8, 8, 2), (5, 7, 10, 5),
              (6, 4, 12, 3), (7, 3, 6, 6), (3, 9, 8, 4), (8, 4, 10, 2),
              (5, 10, 12, 4), (9, 6, 20, 5), (4, 12, 6, 1), (6, 9, 12, 6),
              (2, 6, 20, 10), (10, 5, 8, 8), (7, 8, 10, 10)]),
         },
        {"sr": "Risina uzdevumu ar pilno pārlasi un varbūtību",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda a, b, c: {
                 "teksts": "Kafejnīcā piedāvā %d zupas, %d otros ēdienus un "
                           "%d desertus.   a) Cik dažādas pusdienas var "
                           "izvēlēties?   b) Cik dažādas pusdienas var "
                           "izvēlēties bez deserta?   c) Kāda ir varbūtība, "
                           "ka nejauši izvēlētās pusdienās ir konkrētā "
                           "zupa?   d) Cik pusdienu variantu ir ar vienu "
                           "konkrētu desertu?" % (a, b, c),
                 "kriteriji": [
                     "a) %d · %d · %d = %d.   (1 p.)" % (a, b, c, a * b * c),
                     "b) %d · %d = %d.   (1 p.)" % (a, b, a * b),
                     "c) P = %s.   (1 p.)" % V.dalu(1, a),
                     "d) %d · %d = %d.   (1 p.)" % (a, b, a * b)]},
             [(3, 4, 2), (2, 5, 3), (4, 3, 5), (5, 2, 4), (3, 6, 2),
              (2, 4, 6), (6, 3, 2), (4, 5, 3), (3, 3, 7), (5, 4, 2),
              (2, 8, 3), (7, 2, 4), (4, 4, 4), (6, 5, 2), (3, 5, 6)]),
         },
        {"sr": "Skaidro darbības ar kopām",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Divas pulciņu grupas",
             lambda a, b, abi: {
                 "ievads": "Klasē %d skolēni apmeklē sporta pulciņu, %d — "
                           "mūzikas pulciņu, %d apmeklē abus."
                           % (a, b, abi),
                 "jaut": [("Cik skolēnu apmeklē tikai sporta pulciņu?", 1),
                          ("Cik skolēnu apmeklē vismaz vienu pulciņu?", 1),
                          ("Kā šo skaitu sauc matemātikā?", 1)],
                 "atbildes": [
                     "1) %d − %d = %d skolēni.   (1 p.)" % (a, abi, a - abi),
                     "2) %d + %d − %d = %d skolēni.   (1 p.)"
                     % (a, b, abi, a + b - abi),
                     "3) Kopu apvienojums A ∪ B.   (1 p.)"]},
             [(12, 9, 5), (14, 10, 6), (11, 8, 4), (15, 12, 7), (10, 7, 3),
              (16, 11, 6), (13, 9, 5), (18, 14, 8), (9, 6, 2), (17, 13, 7),
              (20, 15, 9), (8, 5, 2), (19, 12, 6), (22, 16, 10),
              (21, 14, 8)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
