# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.2. Kā definē ģeometriskas figūras?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.2. temats): definīcija un tās
veidošanas veidi, punkts, taisne un plakne kā nedefinējamas figūras,
nogriežņa garums kā citu nogriežņu summa vai starpība, nogriežņa viduspunkts,
teorēma un pierādījums, kā arī blakusleņķu un krustleņķu īpašības.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.2."
NOSAUKUMS = "Kā definē ģeometriskas figūras?"

ATGADNE = [
    "Blakusleņķu summa ir 180°, krustleņķi ir vienādi. Ja viens no četriem "
    "leņķiem ir α, tad pārējie ir 180° − α, α un 180° − α.",
    "Trīs punkti uz vienas taisnes:   AC = AB + BC   ·   BC = AC − AB   ·  "
    " viduspunkts M dala nogriezni uz pusēm:   AM = MB = {AB|2}",
    "Definē, 1) izmantojot iepriekš definēto; 2) aprakstot tikai šai figūrai "
    "raksturīgās īpašības; 3) aprakstot konstruēšanas gaitu. Punktu, taisni "
    "un plakni nedefinē.",
]


# ---------------------------------------------------------------- veidnes
def blakuslenkis(a):
    return ("Viens blakusleņķis ir %d°. Cik liels ir otrs?" % a,
            V.izvele("%d°" % (180 - a), "%d°" % a, "%d°" % (90 - a),
                     "%d°" % (360 - a), "%d°" % (180 + a)), 0)


def krustlenkis(a):
    return ("Viens no krustleņķiem ir %d°. Cik liels ir tam vienādais "
            "leņķis?" % a,
            V.izvele("%d°" % a, "%d°" % (180 - a), "%d°" % (90 - a),
                     "%d°" % (360 - a), "%d°" % (2 * a)), 0)


def nogrieznis_summa(ab, bc):
    return ("Punkts B atrodas starp A un C;  AB = %d cm,  BC = %d cm. Cik "
            "garš ir AC?" % (ab, bc),
            V.izvele("%d cm" % (ab + bc), "%d cm" % abs(ab - bc),
                     "%d cm" % (ab * bc), "%d cm" % ((ab + bc) // 2),
                     "%d cm" % (ab + bc + 2), "%d cm" % (2 * ab + bc)), 0)


def nogrieznis_starpiba(ac, ab):
    return ("Punkts B atrodas starp A un C;  AC = %d cm,  AB = %d cm. Cik "
            "garš ir BC?" % (ac, ab),
            V.izvele("%d cm" % (ac - ab), "%d cm" % (ac + ab),
                     "%d cm" % ab, "%d cm" % (ac // 2),
                     "%d cm" % (2 * ab), "%d cm" % (ac - ab + 2),
                     "%d cm" % (ac + 1)), 0)


def viduspunkts(ab):
    return ("M ir nogriežņa AB viduspunkts,  AB = %d cm. Cik garš ir AM?"
            % ab,
            V.izvele(V.dalu(ab, 2) + " cm", "%d cm" % ab,
                     "%d cm" % (2 * ab), "%d cm" % (ab - 2),
                     "%d cm" % (ab + 2), "%d cm" % (ab // 4)), 0)


def cetri_lenki(a):
    """Divas krustiskas taisnes: cik liela ir triju leņķu summa."""
    return ("Divas krustiskas taisnes veido leņķi %d°. Cik liela ir visu "
            "četru leņķu summa?" % a,
            V.izvele("360°", "180°", "%d°" % (4 * a), "90°",
                     "%d°" % (2 * a)), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.2. temata beigās. Pārbauda definīcijas "
                "jēdzienu, nogriežņa garuma aprēķināšanu, viduspunkta "
                "īpašību, teorēmas un pierādījuma nozīmi un blakusleņķu un "
                "krustleņķu īpašības.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina, ko nozīmē definēt figūru",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir ģeometriska figūra?",
              ["punktu kopa", "taisnes gabals", "skaitļu kopa",
               "leņķa lielums"], 0),
             ("Kāpēc figūras definē?",
              ["lai saziņā saprastos", "lai tās būtu skaistākas",
               "lai tās varētu izmērīt", "lai tās varētu uzzīmēt"], 0),
             ("Kuras figūras nedefinē?",
              ["punktu, taisni un plakni", "trijstūri un kvadrātu",
               "riņķi un lodi", "leņķi un nogriezni"], 0),
             ("Kāpēc punktu nevar definēt?",
              ["nav par to vienkāršākas figūras", "tas ir pārāk mazs",
               "to nevar uzzīmēt", "tam nav garuma"], 0),
             ("Kā var definēt figūru?",
              ["aprakstot tikai tai raksturīgās īpašības",
               "nosaucot tās krāsu", "izmērot tās laukumu",
               "uzzīmējot to"], 0),
             ("Kurš ir labs kvadrāta definējums?",
              ["taisnstūris, kuram visas malas vienādas",
               "figūra ar četrām malām", "figūra ar taisniem leņķiem",
               "liela figūra"], 0),
             ("Ko apraksta konstruēšanas definīcija?",
              ["kā figūru iegūst", "cik liela figūra ir",
               "kādā krāsā figūra ir", "kur figūra atrodas"], 0),
             ("Ar ko punktu, taisni un plakni raksturo?",
              ["ar reāliem objektiem un attēliem", "ar formulām",
               "ar mērvienībām", "ar skaitļiem"], 0),
         ]},
        {"sr": "Zina, kas ir teorēma un pierādījums",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir teorēma?",
              ["apgalvojums, kura patiesumu pierāda",
               "apgalvojums, ko nepierāda", "figūras definīcija",
               "figūras zīmējums"], 0),
             ("Kas ir pierādījums?",
              ["loģisku spriedumu kopums", "viens mērījums",
               "viens piemērs", "figūras zīmējums"], 0),
             ("Kas teorēmā jāsaprot vispirms?",
              ["kas dots un kas jāpierāda", "cik soļu būs",
               "kāda būs atbilde", "kurš to izdomāja"], 0),
             ("Vai viens piemērs pierāda vispārīgu apgalvojumu?",
              ["nē", "jā", "tikai ģeometrijā", "tikai ar zīmējumu"], 0),
             ("Ko nozīmē: ja pie vienādiem lielumiem pieskaita vienu un to "
              "pašu?", ["iegūst vienādus lielumus", "iegūst dažādus lielumus",
                        "iegūst nulli", "nekas nemainās"], 0),
             ("Ja a = c un b = c, ko var secināt?",
              ["a = b", "a > b", "a < b", "neko"], 0),
             ("Ar ko pierādījumā apzīmē vienādus nogriežņus?",
              ["ar vienādām svītriņām", "ar krāsu", "ar burtiem",
               "ar cipariem"], 0),
             ("Ar ko sākas pierādījums?",
              ["ar dotā pieraksti", "ar atbildi", "ar zīmējuma krāsošanu",
               "ar mērīšanu"], 0),
         ]},
        {"sr": "Aprēķina nogriežņa garumu kā summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nogrieznis_summa, [
             (3, 5), (4, 7), (6, 9), (5, 8), (2, 11), (7, 6), (8, 13),
             (9, 4), (10, 15), (12, 7), (11, 9), (14, 6), (13, 12),
             (15, 8), (16, 5)]),
         },
        {"sr": "Aprēķina nogriežņa garumu kā starpību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nogrieznis_starpiba, [
             (12, 5), (15, 7), (20, 8), (18, 6), (14, 9), (25, 11),
             (16, 7), (22, 13), (30, 12), (17, 8), (24, 15), (28, 9),
             (19, 6), (26, 14), (32, 17)]),
         },
        {"sr": "Lieto viduspunkta īpašību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(viduspunkts, [
             12, 16, 20, 8, 24, 14, 18, 22, 30, 26, 10, 28, 34, 36, 40]),
         },
        {"sr": "Zina blakusleņķu īpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik liela ir blakusleņķu summa?",
              ["180°", "90°", "360°", "270°"], 0),
             ("Kas ir blakusleņķi?",
              ["leņķi ar kopīgu malu, kuru otras malas veido taisni",
               "jebkuri divi leņķi", "vienādi leņķi", "taisni leņķi"], 0),
             ("Vai blakusleņķi var būt abi šauri?",
              ["nē", "jā", "tikai taisnstūrī", "vienmēr"], 0),
             ("Vai blakusleņķi var būt abi taisni?",
              ["jā", "nē", "tikai trijstūrī", "nekad"], 0),
             ("Kāds ir blakusleņķis taisnam leņķim?",
              ["taisns", "šaurs", "plats", "izstiepts"], 0),
             ("Kāds ir blakusleņķis šauram leņķim?",
              ["plats", "šaurs", "taisns", "izstiepts"], 0),
             ("Ja viens blakusleņķis ir divreiz lielāks nekā otrs, cik "
              "liels ir mazākais?", ["60°", "90°", "45°", "120°"], 0),
             ("Ja blakusleņķi ir vienādi, cik liels ir katrs?",
              ["90°", "45°", "180°", "60°"], 0),
         ]},
        {"sr": "Aprēķina blakusleņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(blakuslenkis, [
             35, 42, 55, 68, 73, 81, 95, 104, 117, 126, 138, 145, 152,
             163, 27]),
         },
        {"sr": "Zina krustleņķu īpašību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādi ir krustleņķi?",
              ["vienādi", "blakus", "taisni", "izstiepti"], 0),
             ("Kas ir krustleņķi?",
              ["leņķi, kuru malas ir pretējie stari",
               "leņķi ar kopīgu malu", "jebkuri divi leņķi",
               "leņķi trijstūrī"], 0),
             ("Cik leņķu veido divas krustiskas taisnes?",
              ["4", "2", "6", "8"], 0),
             ("Cik krustleņķu pāru veido divas krustiskas taisnes?",
              ["2", "1", "4", "3"], 0),
             ("Ja viens leņķis ir 90°, kādi ir pārējie?",
              ["visi 90°", "visi 45°", "divi 90° un divi 180°",
               "nevar noteikt"], 0),
             ("Vai krustleņķi var būt blakusleņķi?",
              ["tikai tad, ja abi ir 90°", "vienmēr", "nekad",
               "tikai šauri"], 0),
             ("Kāpēc krustleņķi ir vienādi?",
              ["abiem ir viens un tas pats blakusleņķis",
               "tie izskatās vienādi", "tā ir definīcija",
               "tos izmēra vienādi"], 0),
             ("Kā sauc apgalvojumu par krustleņķu vienādību?",
              ["teorēma", "definīcija", "aksioma", "piemērs"], 0),
         ]},
        {"sr": "Aprēķina krustleņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(krustlenkis, [
             38, 47, 52, 64, 71, 83, 97, 106, 112, 124, 133, 141, 155,
             29, 168]),
         },
        {"sr": "Nosaka visu četru leņķu summu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(cetri_lenki, [
             30, 40, 50, 55, 60, 65, 70, 75, 80, 85, 100, 110, 120,
             130, 140]),
         },
        {"sr": "Raksturo divu taišņu novietojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc taisnes, kurām nav kopīga punkta?",
              ["paralēlas", "krustiskas", "perpendikulāras", "vienādas"], 0),
             ("Kā sauc taisnes, kas krustojas taisnā leņķī?",
              ["perpendikulāras", "paralēlas", "vienādas", "šķeltas"], 0),
             ("Cik kopīgu punktu ir divām krustiskām taisnēm?",
              ["1", "0", "2", "bezgalīgi daudz"], 0),
             ("Cik kopīgu punktu ir divām paralēlām taisnēm?",
              ["0", "1", "2", "bezgalīgi daudz"], 0),
             ("Kā apzīmē paralēlas taisnes?",
              ["a ∥ b", "a ⊥ b", "a = b", "a ∈ b"], 0),
             ("Kā apzīmē perpendikulāras taisnes?",
              ["a ⊥ b", "a ∥ b", "a = b", "a ∈ b"], 0),
             ("Cik taisnes var novilkt caur diviem punktiem?",
              ["vienu", "divas", "nevienu", "bezgalīgi daudz"], 0),
             ("Cik taisnes var novilkt caur vienu punktu?",
              ["bezgalīgi daudz", "vienu", "divas", "nevienu"], 0),
         ]},
        {"sr": "Lieto apzīmējumus un skici",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ar ko apzīmē nogriezni ar galapunktiem A un B?",
              ["AB", "A + B", "A · B", "A : B"], 0),
             ("Ar ko apzīmē leņķi ar virsotni B?",
              ["∠ABC", "AB", "A + B", "ΔAB"], 0),
             ("Ko rāda skice?",
              ["figūru bez precīziem mērījumiem", "precīzu zīmējumu",
               "tikai burtus", "tikai skaitļus"], 0),
             ("Kāpēc risinājumā zīmē skici?",
              ["lai redzētu, kas dots un kas meklēts", "lai būtu skaisti",
               "lai aizpildītu lapu", "tas nav vajadzīgs"], 0),
             ("Ar cik burtiem parasti apzīmē trijstūri?",
              ["ar trim", "ar vienu", "ar diviem", "ar četriem"], 0),
             ("Kā apzīmē, ka nogriežņi ir vienāda garuma?",
              ["ar vienādām svītriņām", "ar vienādiem burtiem",
               "ar krāsu", "ar bultiņām"], 0),
             ("Kā zīmējumā apzīmē taisnu leņķi?",
              ["ar kvadrātiņu", "ar lociņu", "ar punktu", "ar bultiņu"], 0),
             ("Kas ir punktu ģeometriskā vieta?",
              ["visi punkti ar doto īpašību", "viens punkts",
               "divi punkti", "taisnes gabals"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 2,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "2. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.2. temata noslēgumā. "
                "Pārbauda definīcijas un pierādījuma jēdzienu, nogriežņa "
                "garuma un viduspunkta aprēķinus un leņķu aprēķināšanu ar "
                "blakusleņķu un krustleņķu īpašībām.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina definīcijas un pierādījuma jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir ģeometriska figūra?",
              ["punktu kopa", "taisnes gabals", "skaitļu kopa",
               "leņķa lielums"], 0),
             ("Kuras figūras nedefinē?",
              ["punktu, taisni un plakni", "trijstūri un kvadrātu",
               "riņķi un lodi", "leņķi un nogriezni"], 0),
             ("Kas ir teorēma?",
              ["apgalvojums, kura patiesumu pierāda",
               "apgalvojums, ko nepierāda", "figūras definīcija",
               "figūras zīmējums"], 0),
             ("Kas ir pierādījums?",
              ["loģisku spriedumu kopums", "viens mērījums",
               "viens piemērs", "figūras zīmējums"], 0),
             ("Vai viens piemērs pierāda vispārīgu apgalvojumu?",
              ["nē", "jā", "tikai ģeometrijā", "tikai ar zīmējumu"], 0),
             ("Ja a = c un b = c, ko var secināt?",
              ["a = b", "a > b", "a < b", "neko"], 0),
             ("Kurš ir labs kvadrāta definējums?",
              ["taisnstūris, kuram visas malas vienādas",
               "figūra ar četrām malām", "figūra ar taisniem leņķiem",
               "liela figūra"], 0),
             ("Kas teorēmā jāsaprot vispirms?",
              ["kas dots un kas jāpierāda", "cik soļu būs",
               "kāda būs atbilde", "kurš to izdomāja"], 0),
         ]},
        {"sr": "Aprēķina nogriežņa garumu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(nogrieznis_summa, [
             (4, 6), (5, 9), (7, 8), (3, 12), (6, 11), (9, 7), (10, 13)])
             + V.kopa(nogrieznis_starpiba, [
                 (14, 6), (18, 7), (21, 9), (26, 12), (16, 5), (23, 14),
                 (29, 11), (35, 18)])),
         },
        {"sr": "Lieto viduspunkta īpašību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(viduspunkts, [
             10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 12, 16, 20, 24]),
         },
        {"sr": "Aprēķina blakusleņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(blakuslenkis, [
             25, 37, 49, 58, 66, 77, 89, 101, 113, 122, 134, 147, 156,
             168, 43]),
         },
        {"sr": "Aprēķina krustleņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(krustlenkis, [
             33, 46, 57, 61, 74, 88, 92, 108, 119, 127, 136, 149, 158,
             31, 172]),
         },
        {"sr": "Raksturo taišņu novietojumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā sauc taisnes, kurām nav kopīga punkta?",
              ["paralēlas", "krustiskas", "perpendikulāras", "vienādas"], 0),
             ("Cik leņķu veido divas krustiskas taisnes?",
              ["4", "2", "6", "8"], 0),
             ("Kādi ir krustleņķi?",
              ["vienādi", "blakus", "taisni", "izstiepti"], 0),
             ("Cik liela ir blakusleņķu summa?",
              ["180°", "90°", "360°", "270°"], 0),
             ("Kā apzīmē perpendikulāras taisnes?",
              ["a ⊥ b", "a ∥ b", "a = b", "a ∈ b"], 0),
             ("Cik taisnes var novilkt caur diviem punktiem?",
              ["vienu", "divas", "nevienu", "bezgalīgi daudz"], 0),
             ("Ja blakusleņķi ir vienādi, cik liels ir katrs?",
              ["90°", "45°", "180°", "60°"], 0),
             ("Kāpēc krustleņķi ir vienādi?",
              ["abiem ir viens un tas pats blakusleņķis",
               "tie izskatās vienādi", "tā ir definīcija",
               "tos izmēra vienādi"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina leņķus un nogriežņus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda a, ab, bc, ac: [
                 ("Blakusleņķis leņķim %d° ir ……°" % a, V.sk(180 - a)),
                 ("Krustleņķis leņķim %d° ir ……°" % a, V.sk(a)),
                 ("AB = %d cm,  BC = %d cm,  AC = …… cm" % (ab, bc),
                  V.sk(ab + bc)),
                 ("AC = %d cm,  AB = %d cm,  BC = …… cm" % (ac, ab),
                  V.sk(ac - ab))],
             [(35, 4, 7, 15), (48, 5, 9, 18), (62, 6, 8, 20), (71, 3, 11, 16),
              (84, 7, 6, 22), (96, 9, 4, 25), (107, 8, 13, 30),
              (118, 10, 15, 28), (129, 12, 7, 32), (143, 11, 9, 24),
              (152, 14, 6, 35), (27, 13, 12, 26), (56, 15, 8, 40),
              (74, 16, 5, 38), (163, 9, 14, 21)]),
         },
        {"sr": "Lieto viduspunkta īpašību",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Nogriežņa viduspunkts",
             lambda ab, am: [
                 ("M ir AB viduspunkts,  AB = %d cm,  AM = …… cm" % ab,
                  V.dalu(ab, 2)),
                 ("M ir AB viduspunkts,  AM = %d cm,  AB = …… cm" % am,
                  V.sk(2 * am)),
                 ("M ir AB viduspunkts,  AB = %d cm,  MB = …… cm" % (2 * am),
                  V.sk(am))],
             [(12, 5), (16, 7), (20, 9), (24, 6), (18, 8), (30, 11),
              (14, 4), (26, 13), (34, 15), (22, 10), (28, 12), (36, 17),
              (40, 14), (10, 3), (32, 16)]),
         },
        {"sr": "Risina uzdevumu par krustiskām taisnēm",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Krustiskas taisnes",
             lambda a: {
                 "teksts": "Divas krustiskas taisnes veido četrus leņķus; "
                           "viens no tiem ir %d°.   a) Cik liels ir tā "
                           "blakusleņķis?   b) Cik liels ir tā "
                           "krustleņķis?   c) Cik liela ir visu četru leņķu "
                           "summa?   d) Kāda veida ir dotais leņķis?" % a,
                 "kriteriji": [
                     "a) 180° − %d° = %d°.   (1 p.)" % (a, 180 - a),
                     "b) %d°.   (1 p.)" % a,
                     "c) 360°.   (1 p.)",
                     "d) %s leņķis.   (1 p.)"
                     % ("Šaurs" if a < 90 else
                        ("Taisns" if a == 90 else "Plats"))]},
             [35, 42, 55, 68, 73, 81, 95, 104, 117, 126, 138, 145, 152,
              163, 27]),
         },
        {"sr": "Veido definīciju un pamato spriedumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Nogriežņi uz taisnes",
             lambda ac, ab: {
                 "ievads": "Punkts B atrodas starp punktiem A un C; "
                           "AC = %d cm un AB = %d cm." % (ac, ab),
                 "jaut": [("Cik garš ir nogrieznis BC?", 1),
                          ("Cik garš ir AM, ja M ir AC viduspunkts?", 1),
                          ("Pamato, kā ieguvi BC garumu!", 1)],
                 "atbildes": [
                     "1) BC = %d − %d = %d cm.   (1 p.)"
                     % (ac, ab, ac - ab),
                     "2) AM = %s cm.   (1 p.)" % V.dalu(ac, 2),
                     "3) AC = AB + BC, tāpēc BC = AC − AB.   (1 p.)"]},
             [(20, 8), (24, 9), (30, 12), (18, 7), (26, 11), (34, 15),
              (16, 6), (28, 13), (40, 17), (22, 10), (36, 14), (32, 19),
              (14, 5), (38, 16), (44, 21)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
