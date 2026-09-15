# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.5. Kā raksturo trijstūri, izmantojot tā elementus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.5. temats): trijstūra
nevienādība un trijstūra eksistence, trijstūru veidi pēc malām, vienādsānu
trijstūra elementi un īpašības, bisektrise, mediāna un augstums, trijstūru
vienādības pazīmes (mmm, mlm, lml) un konstruēšana ar cirkuli un lineālu.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.5."
NOSAUKUMS = "Kā raksturo trijstūri, izmantojot tā elementus?"

ATGADNE = [
    "Trijstūra nevienādība: katras malas garums ir mazāks nekā abu pārējo "
    "malu garumu summa.",
    "Vienādsānu trijstūrim sānu malas ir vienādas un pamata pieleņķi ir "
    "vienādi; vienādmalu trijstūrim visas malas vienādas un visi leņķi 60°.",
    "Bisektrise dala leņķi uz pusēm   ·   mediāna savieno virsotni ar "
    "pretējās malas viduspunktu   ·   augstums ir perpendikuls no virsotnes "
    "pret pretējo malu.",
]


# ---------------------------------------------------------------- veidnes
def nevienadiba(a, b, c):
    """Vai no trim nogriežņiem var izveidot trijstūri."""
    var = a + b > c and a + c > b and b + c > a
    return ("Vai no nogriežņiem %d cm, %d cm un %d cm var izveidot "
            "trijstūri?" % (a, b, c),
            V.izvele("jā" if var else "nē", "nē" if var else "jā",
                     "tikai taisnleņķa", "nevar noteikt"), 0)


def perimetrs_sanu(sanu, pamats):
    """Vienādsānu trijstūra perimetrs."""
    return ("Vienādsānu trijstūra sānu mala ir %d cm, pamats — %d cm. Cik "
            "garš ir perimetrs?" % (sanu, pamats),
            V.izvele("%d cm" % (2 * sanu + pamats),
                     "%d cm" % (sanu + 2 * pamats),
                     "%d cm" % (sanu + pamats),
                     "%d cm" % (3 * sanu),
                     "%d cm" % (2 * sanu),
                     "%d cm" % (2 * sanu + pamats + 2)), 0)


def pamats_no_perimetra(sanu, perimetrs):
    """Vienādsānu trijstūra pamats, ja zināms perimetrs."""
    return ("Vienādsānu trijstūra perimetrs ir %d cm, sānu mala — %d cm. "
            "Cik garš ir pamats?" % (perimetrs, sanu),
            V.izvele("%d cm" % (perimetrs - 2 * sanu),
                     "%d cm" % (perimetrs - sanu),
                     "%d cm" % (perimetrs // 3),
                     "%d cm" % (perimetrs - 3 * sanu),
                     "%d cm" % sanu,
                     "%d cm" % (perimetrs - 2 * sanu + 2)), 0)


def bisektrise(a):
    """Bisektrise dala leņķi uz pusēm."""
    return ("Trijstūra leņķis ir %d°. Cik liels ir leņķis, ko no tā atdala "
            "bisektrise?" % a,
            V.izvele(V.dalu(a, 2) + "°", "%d°" % a, "%d°" % (2 * a),
                     "%d°" % (180 - a), "%d°" % (90 - a),
                     "%d°" % (a + 2)), 0)


def mediana(mala):
    """Mediāna savieno virsotni ar pretējās malas viduspunktu."""
    return ("Trijstūra mala ir %d cm. Cik garš ir nogrieznis no virsotnes "
            "līdz mediānas pamatam uz šīs malas?" % mala,
            V.izvele(V.dalu(mala, 2) + " cm", "%d cm" % mala,
                     "%d cm" % (2 * mala), "%d cm" % (mala - 2),
                     "%d cm" % (mala + 2), "%d cm" % (mala // 4)), 0)


def sanu_lenki(virsotne):
    """Vienādsānu trijstūra pamata pieleņķi, ja zināms virsotnes leņķis."""
    pielenkis = (180 - virsotne) // 2
    return ("Vienādsānu trijstūra virsotnes leņķis ir %d°. Cik liels ir "
            "katrs pamata pieleņķis?" % virsotne,
            V.izvele("%d°" % pielenkis, "%d°" % (180 - virsotne),
                     "%d°" % virsotne, "%d°" % (2 * pielenkis),
                     "%d°" % (pielenkis + 15), "%d°" % (pielenkis - 10),
                     "%d°" % (pielenkis + 25)), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.5. temata beigās. Pārbauda trijstūra "
                "nevienādību, trijstūru veidus, vienādsānu trijstūra "
                "īpašības, bisektrisi, mediānu un augstumu un trijstūru "
                "vienādības pazīmes.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Lieto trijstūra nevienādību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nevienadiba, [
             (3, 4, 5), (2, 3, 7), (5, 6, 10), (1, 2, 5), (7, 8, 9),
             (4, 4, 9), (6, 7, 12), (3, 3, 6), (8, 9, 15), (2, 9, 4),
             (10, 11, 20), (5, 5, 11), (12, 13, 14), (1, 8, 6),
             (9, 10, 18)]),
         },
        {"sr": "Zina trijstūra nevienādības nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā skan trijstūra nevienādība?",
              ["katra mala ir mazāka nekā pārējo divu summa",
               "katra mala ir lielāka nekā pārējo summa",
               "visas malas ir vienādas", "divas malas ir vienādas"], 0),
             ("Kāpēc lauztas līnijas garums ir lielāks nekā attālums starp "
              "galapunktiem?", ["taisnais ceļš ir īsākais",
                                "tā ir definīcija", "tas ir dažādi",
                                "tas nav tiesa"], 0),
             ("Divas malas ir 5 cm un 9 cm. Kāda var būt trešā?",
              ["6 cm", "3 cm", "14 cm", "20 cm"], 0),
             ("Divas malas ir 4 cm un 4 cm. Kāda nevar būt trešā?",
              ["8 cm", "5 cm", "3 cm", "7 cm"], 0),
             ("Kāds ir trešās malas lielākais veselais garums, ja malas ir "
              "6 cm un 8 cm?", ["13 cm", "14 cm", "15 cm", "2 cm"], 0),
             ("Kāds ir trešās malas mazākais veselais garums, ja malas ir "
              "6 cm un 8 cm?", ["3 cm", "2 cm", "1 cm", "14 cm"], 0),
             ("Vai no 2 cm, 3 cm un 5 cm var izveidot trijstūri?",
              ["nē, tie veido nogriezni", "jā", "tikai vienādsānu",
               "tikai taisnleņķa"], 0),
             ("Ko pārbauda vispirms, veidojot trijstūri no trim malām?",
              ["trijstūra nevienādību", "leņķu summu", "laukumu",
               "perimetru"], 0),
         ]},
        {"sr": "Šķiro trijstūrus pēc malām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir trijstūris ar malām 5 cm, 5 cm un 8 cm?",
              ["vienādsānu", "vienādmalu", "dažādmalu", "taisnleņķa"], 0),
             ("Kāds ir trijstūris ar malām 6 cm, 6 cm un 6 cm?",
              ["vienādmalu", "vienādsānu, bet ne vienādmalu", "dažādmalu",
               "platleņķa"], 0),
             ("Kāds ir trijstūris ar malām 4 cm, 7 cm un 9 cm?",
              ["dažādmalu", "vienādsānu", "vienādmalu", "taisnleņķa"], 0),
             ("Cik vienādu malu ir vienādsānu trijstūrim?",
              ["divas", "trīs", "viena", "neviena"], 0),
             ("Cik vienādu malu ir dažādmalu trijstūrim?",
              ["neviena", "divas", "trīs", "viena"], 0),
             ("Vai vienādmalu trijstūris ir arī vienādsānu?",
              ["jā", "nē", "tikai ar taisnu leņķi", "nevar noteikt"], 0),
             ("Kā sauc vienādsānu trijstūra trešo malu?",
              ["pamats", "sānu mala", "augstums", "mediāna"], 0),
             ("Cik lieli ir vienādmalu trijstūra leņķi?",
              ["visi 60°", "visi 90°", "visi 45°", "visi 30°"], 0),
         ]},
        {"sr": "Aprēķina vienādsānu trijstūra perimetru",
         "stunda": TEMATS,
         "jautajumi": V.kopa(perimetrs_sanu, [
             (5, 8), (7, 4), (6, 9), (9, 5), (8, 12), (10, 6), (4, 3),
             (11, 7), (12, 10), (13, 8), (15, 9), (14, 11), (16, 12),
             (9, 14), (20, 15)]),
         },
        {"sr": "Nosaka pamatu pēc perimetra",
         "stunda": TEMATS,
         "jautajumi": V.kopa(pamats_no_perimetra, [
             (5, 18), (7, 20), (6, 21), (9, 25), (8, 30), (10, 26),
             (4, 15), (11, 32), (12, 35), (13, 38), (15, 40), (14, 42),
             (16, 45), (9, 27), (20, 55)]),
         },
        {"sr": "Zina vienādsānu trijstūra īpašības",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kādi ir vienādsānu trijstūra pamata pieleņķi?",
              ["vienādi", "dažādi", "taisni", "plati"], 0),
             ("Kā sauc leņķi starp sānu malām?",
              ["virsotnes leņķis", "pamata pielenkis", "ārējais leņķis",
               "taisns leņķis"], 0),
             ("Ja pamata pielenkis ir 50°, cik liels ir otrs pielenkis?",
              ["50°", "80°", "130°", "40°"], 0),
             ("Vai vienādsānu trijstūrim var būt taisns virsotnes leņķis?",
              ["jā", "nē", "tikai vienādmalu", "nevar noteikt"], 0),
             ("Kas vienādsānu trijstūrī sakrīt ar pamata mediānu?",
              ["virsotnes leņķa bisektrise un augstums", "tikai perimetrs",
               "sānu mala", "pamats"], 0),
             ("Cik simetrijas asu ir vienādsānu trijstūrim?",
              ["viena", "divas", "trīs", "neviena"], 0),
             ("Cik simetrijas asu ir vienādmalu trijstūrim?",
              ["trīs", "viena", "divas", "neviena"], 0),
             ("Kā sauc vienādsānu trijstūra vienādās malas?",
              ["sānu malas", "pamats", "augstumi", "mediānas"], 0),
         ]},
        {"sr": "Aprēķina vienādsānu trijstūra leņķus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sanu_lenki, [
             40, 60, 80, 100, 30, 120, 20, 140, 50, 90, 70, 110, 10,
             130, 150]),
         },
        {"sr": "Zina bisektrises definīciju",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir trijstūra bisektrise?",
              ["nogrieznis, kas dala leņķi uz pusēm",
               "nogrieznis līdz malas viduspunktam",
               "perpendikuls pret malu", "trijstūra mala"], 0),
             ("Cik bisektrišu ir trijstūrim?", ["trīs", "viena", "divas",
                                                "četras"], 0),
             ("Ko dala bisektrise?", ["leņķi", "malu", "perimetru",
                                      "laukumu"], 0),
             ("Ar ko konstruē bisektrisi?",
              ["ar cirkuli un lineālu", "ar transportieri",
              "ar lineālu ar skalu", "no acs"], 0),
             ("Kur atrodas bisektrises sākumpunkts?",
              ["trijstūra virsotnē", "malas viduspunktā",
               "ārpus trijstūra", "riņķa centrā"], 0),
             ("Kur atrodas bisektrises galapunkts?",
              ["uz pretējās malas", "uz sānu malas", "virsotnē",
               "ārpus trijstūra"], 0),
             ("Vai bisektrise vienmēr dala malu uz pusēm?",
              ["nē", "jā", "tikai taisnleņķa trijstūrī", "vienmēr"], 0),
             ("Kad bisektrise sakrīt ar mediānu?",
              ["vienādsānu trijstūra virsotnē", "vienmēr", "nekad",
               "taisnleņķa trijstūrī"], 0),
         ]},
        {"sr": "Aprēķina bisektrises atdalīto leņķi",
         "stunda": TEMATS,
         "jautajumi": V.kopa(bisektrise, [
             40, 60, 80, 100, 30, 120, 50, 90, 70, 110, 20, 130, 140,
             150, 160]),
         },
        {"sr": "Zina mediānas un augstuma definīcijas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir trijstūra mediāna?",
              ["nogrieznis no virsotnes līdz pretējās malas viduspunktam",
               "nogrieznis, kas dala leņķi uz pusēm",
               "perpendikuls pret malu", "trijstūra mala"], 0),
             ("Kas ir trijstūra augstums?",
              ["perpendikuls no virsotnes pret pretējo malu",
               "nogrieznis līdz malas viduspunktam",
               "nogrieznis, kas dala leņķi", "garākā mala"], 0),
             ("Cik mediānu ir trijstūrim?", ["trīs", "viena", "divas",
                                             "četras"], 0),
             ("Cik augstumu ir trijstūrim?", ["trīs", "viena", "divas",
                                              "četras"], 0),
             ("Ko dala mediāna uz pusēm?", ["pretējo malu", "leņķi",
                                            "perimetru", "augstumu"], 0),
             ("Kādā leņķī augstums krusto malu?", ["90°", "60°", "45°",
                                                   "30°"], 0),
             ("Vai augstums vienmēr atrodas trijstūra iekšpusē?",
              ["nē, platleņķa trijstūrī tas ir ārpusē", "jā",
               "tikai vienādsānu", "tikai vienādmalu"], 0),
             ("Kur atrodas taisnleņķa trijstūra divi augstumi?",
              ["tie sakrīt ar katetēm", "tie sakrīt ar hipotenūzu",
               "ārpus trijstūra", "virsotnē"], 0),
         ]},
        {"sr": "Aprēķina mediānas atdalīto nogriezni",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mediana, [
             12, 16, 20, 8, 24, 14, 18, 22, 30, 26, 10, 28, 34, 36, 40]),
         },
        {"sr": "Lieto trijstūru vienādības pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik elementiem vismaz jābūt vienādiem, lai trijstūri būtu "
              "vienādi?", ["trim", "diviem", "vienam", "visiem sešiem"], 0),
             ("Ko nozīmē pazīme «mmm»?",
              ["trīs malas", "divas malas un leņķis",
               "leņķis, mala, leņķis", "trīs leņķi"], 0),
             ("Ko nozīmē pazīme «mlm»?",
              ["mala, leņķis starp tām, mala", "trīs malas", "trīs leņķi",
               "divas malas"], 0),
             ("Ko nozīmē pazīme «lml»?",
              ["leņķis, mala, leņķis", "trīs malas", "trīs leņķi",
               "divas malas"], 0),
             ("Vai trīs vienādi leņķi nodrošina trijstūru vienādību?",
              ["nē", "jā", "tikai vienādsānu", "tikai taisnleņķa"], 0),
             ("Kāpēc lieto trijstūru vienādību?",
              ["lai pierādītu citu figūru vienādību", "lai mērītu malas",
               "lai aprēķinātu laukumu", "lai zīmētu skici"], 0),
             ("Ar ko konstruē trijstūri pēc dotiem elementiem?",
              ["ar cirkuli un lineālu bez skalas", "ar transportieri",
               "ar lineālu ar skalu", "no acs"], 0),
             ("Kāpēc konstruē ar cirkuli un lineālu bez skalas?",
              ["precizitāti neietekmē mērījumu kļūda", "tas ir ātrāk",
               "tas ir skaistāk", "tā ir tradīcija"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 5,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "5. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.5. temata noslēgumā. "
                "Pārbauda trijstūra nevienādību, trijstūru veidus, "
                "vienādsānu trijstūra īpašības, bisektrisi, mediānu un "
                "augstumu un trijstūru vienādības pazīmes.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Lieto trijstūra nevienādību",
         "stunda": TEMATS,
         "jautajumi": V.kopa(nevienadiba, [
             (4, 5, 6), (3, 4, 8), (6, 7, 11), (2, 2, 5), (8, 9, 10),
             (5, 5, 12), (7, 8, 14), (4, 4, 7), (9, 10, 16), (3, 10, 5),
             (11, 12, 22), (6, 6, 13), (13, 14, 15), (2, 9, 6),
             (10, 11, 19)]),
         },
        {"sr": "Šķiro trijstūrus pēc malām",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds ir trijstūris ar malām 7 cm, 7 cm un 9 cm?",
              ["vienādsānu", "vienādmalu", "dažādmalu", "taisnleņķa"], 0),
             ("Kāds ir trijstūris ar malām 5 cm, 5 cm un 5 cm?",
              ["vienādmalu", "vienādsānu, bet ne vienādmalu", "dažādmalu",
               "platleņķa"], 0),
             ("Kāds ir trijstūris ar malām 3 cm, 6 cm un 8 cm?",
              ["dažādmalu", "vienādsānu", "vienādmalu", "taisnleņķa"], 0),
             ("Cik vienādu malu ir vienādsānu trijstūrim?",
              ["divas", "trīs", "viena", "neviena"], 0),
             ("Cik lieli ir vienādmalu trijstūra leņķi?",
              ["visi 60°", "visi 90°", "visi 45°", "visi 30°"], 0),
             ("Kā sauc vienādsānu trijstūra trešo malu?",
              ["pamats", "sānu mala", "augstums", "mediāna"], 0),
             ("Vai vienādmalu trijstūris ir arī vienādsānu?",
              ["jā", "nē", "tikai ar taisnu leņķi", "nevar noteikt"], 0),
             ("Cik simetrijas asu ir vienādmalu trijstūrim?",
              ["trīs", "viena", "divas", "neviena"], 0),
         ]},
        {"sr": "Aprēķina vienādsānu trijstūra perimetru",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(perimetrs_sanu, [
             (6, 5), (8, 7), (9, 4), (10, 8), (12, 7), (11, 9), (13, 6)])
             + V.kopa(pamats_no_perimetra, [
                 (6, 22), (8, 24), (9, 28), (10, 31), (12, 34), (11, 33),
                 (13, 36), (7, 23)])),
         },
        {"sr": "Aprēķina vienādsānu trijstūra leņķus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sanu_lenki, [
             30, 50, 70, 90, 110, 130, 20, 40, 60, 80, 100, 120, 140,
             10, 150]),
         },
        {"sr": "Lieto bisektrises un mediānas definīcijas",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(bisektrise, [
             50, 70, 90, 110, 130, 30, 150])
             + V.kopa(mediana, [
                 14, 18, 22, 26, 30, 34, 38, 42])),
         },
        {"sr": "Lieto trijstūru vienādības pazīmes",
         "stunda": TEMATS,
         "jautajumi": [
             ("Cik elementiem vismaz jābūt vienādiem, lai trijstūri būtu "
              "vienādi?", ["trim", "diviem", "vienam", "visiem sešiem"], 0),
             ("Ko nozīmē pazīme «mmm»?",
              ["trīs malas", "divas malas un leņķis",
               "leņķis, mala, leņķis", "trīs leņķi"], 0),
             ("Vai trīs vienādi leņķi nodrošina trijstūru vienādību?",
              ["nē", "jā", "tikai vienādsānu", "tikai taisnleņķa"], 0),
             ("Kas ir trijstūra augstums?",
              ["perpendikuls no virsotnes pret pretējo malu",
               "nogrieznis līdz malas viduspunktam",
               "nogrieznis, kas dala leņķi", "garākā mala"], 0),
             ("Cik mediānu ir trijstūrim?", ["trīs", "viena", "divas",
                                             "četras"], 0),
             ("Ar ko konstruē trijstūri pēc dotiem elementiem?",
              ["ar cirkuli un lineālu bez skalas", "ar transportieri",
               "ar lineālu ar skalu", "no acs"], 0),
             ("Kad bisektrise sakrīt ar mediānu?",
              ["vienādsānu trijstūra virsotnē", "vienmēr", "nekad",
               "taisnleņķa trijstūrī"], 0),
             ("Kāpēc lieto trijstūru vienādību?",
              ["lai pierādītu citu figūru vienādību", "lai mērītu malas",
               "lai aprēķinātu laukumu", "lai zīmētu skici"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina trijstūra elementus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Ieraksti trūkstošo",
             lambda s, p, virs, mala: [
                 ("Vienādsānu trijstūris:  sānu mala %d cm, pamats %d cm; "
                  "P = …… cm" % (s, p), V.sk(2 * s + p)),
                 ("Perimetrs %d cm, sānu mala %d cm; pamats = …… cm"
                  % (2 * s + p, s), V.sk(p)),
                 ("Virsotnes leņķis %d°; pamata pielenkis = ……°" % virs,
                  V.sk((180 - virs) // 2)),
                 ("Mala %d cm; mediānas pamats to dala pa …… cm" % mala,
                  V.dalu(mala, 2))],
             [(5, 8, 40, 12), (7, 4, 60, 16), (6, 9, 80, 20), (9, 5, 100, 8),
              (8, 12, 30, 24), (10, 6, 120, 14), (4, 3, 20, 18),
              (11, 7, 140, 22), (12, 10, 50, 30), (13, 8, 90, 26),
              (15, 9, 70, 10), (14, 11, 110, 28), (16, 12, 10, 34),
              (9, 14, 130, 36), (20, 15, 150, 40)]),
         },
        {"sr": "Pārbauda trijstūra eksistenci",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Trijstūra nevienādība",
             lambda a, b, c, d, e, f: [
                 ("Vai no %d; %d un %d cm var izveidot trijstūri?   ……"
                  % (a, b, c), "jā" if a + b > c else "nē"),
                 ("Vai no %d; %d un %d cm var izveidot trijstūri?   ……"
                  % (d, e, f), "jā" if d + e > f else "nē"),
                 ("Malas %d cm un %d cm; trešās malas lielākais veselais "
                  "garums ir …… cm" % (a, b), V.sk(a + b - 1))],
             [(3, 4, 5, 2, 3, 7), (5, 6, 10, 1, 2, 5), (7, 8, 9, 4, 4, 9),
              (6, 7, 12, 3, 3, 6), (8, 9, 15, 2, 9, 4), (10, 11, 20, 5, 5, 11),
              (12, 13, 14, 1, 8, 6), (9, 10, 18, 4, 5, 10),
              (4, 5, 8, 3, 5, 9), (11, 12, 15, 2, 6, 8),
              (13, 14, 20, 6, 7, 14), (5, 9, 11, 3, 7, 11),
              (6, 10, 13, 2, 4, 7), (14, 15, 25, 5, 8, 13),
              (7, 12, 16, 4, 6, 12)]),
         },
        {"sr": "Risina uzdevumu par vienādsānu trijstūri",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Vienādsānu trijstūris",
             lambda s, p, virs: {
                 "teksts": "Vienādsānu trijstūra sānu mala ir %d cm, "
                           "pamats — %d cm, virsotnes leņķis — %d°.   "
                           "a) Aprēķini perimetru!   b) Cik liels ir katrs "
                           "pamata pielenkis?   c) Cik liels ir leņķis, ko "
                           "no virsotnes leņķa atdala bisektrise?   d) Cik "
                           "garš ir pamata nogrieznis no viduspunkta līdz "
                           "virsotnei pa pamatu?" % (s, p, virs),
                 "kriteriji": [
                     "a) 2 · %d + %d = %d cm.   (1 p.)"
                     % (s, p, 2 * s + p),
                     "b) (180° − %d°) : 2 = %d°.   (1 p.)"
                     % (virs, (180 - virs) // 2),
                     "c) %d° : 2 = %s°.   (1 p.)" % (virs, V.dalu(virs, 2)),
                     "d) %d : 2 = %s cm.   (1 p.)" % (p, V.dalu(p, 2))]},
             [(5, 8, 40), (7, 6, 60), (6, 10, 80), (9, 4, 100), (8, 12, 30),
              (10, 6, 120), (4, 6, 20), (11, 8, 140), (12, 10, 50),
              (13, 8, 90), (15, 12, 70), (14, 10, 110), (16, 14, 100),
              (9, 12, 130), (20, 16, 150)]),
         },
        {"sr": "Pamato spriedumu par trijstūri",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Trijstūra malas",
             lambda a, b: {
                 "ievads": "Trijstūra divas malas ir %d cm un %d cm."
                           % (a, b),
                 "jaut": [("Kāds ir trešās malas lielākais veselais "
                           "garums?", 1),
                          ("Kāds ir trešās malas mazākais veselais "
                           "garums?", 1),
                          ("Pamato ar trijstūra nevienādību!", 1)],
                 "atbildes": [
                     "1) %d cm.   (1 p.)" % (a + b - 1),
                     "2) %d cm.   (1 p.)" % (abs(a - b) + 1),
                     "3) Trešā mala ir mazāka nekā %d cm un lielāka nekā "
                     "%d cm.   (1 p.)" % (a + b, abs(a - b))]},
             [(5, 9), (6, 8), (7, 11), (4, 10), (8, 13), (9, 12), (3, 7),
              (10, 15), (11, 14), (12, 18), (5, 12), (13, 16), (14, 20),
              (6, 15), (16, 21)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
