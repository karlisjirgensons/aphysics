# -*- coding: utf-8 -*-
"""Matemātika, 8. klase. 8.1. Kā matemātiski raksturo un analizē datus?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 8. klase, 8.1. temats): datu kopas
statistiskie rādītāji — amplitūda, mediāna, moda, aritmētiskais vidējais,
absolūtais un relatīvais biežums —, datu attēlošana un analīze, divu objektu
kopu salīdzināšana un vienkārša pētījuma plānošana.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  8. klase"
TEMATS = "8.1."
NOSAUKUMS = "Kā matemātiski raksturo un analizē datus?"

ATGADNE = [
    "Aritmētiskais vidējais = summa : skaits   ·   amplitūda = lielākā "
    "vērtība − mazākā vērtība   ·   moda ir biežāk sastopamā vērtība.",
    "Mediāna ir sakārtotas datu kopas vidējais elements; ja elementu skaits "
    "ir pāra skaitlis, tā ir divu vidējo aritmētiskais vidējais.",
    "Absolūtais biežums ir, cik reižu vērtība sastopama; relatīvais biežums "
    "= {absolūtais biežums|visu datu skaits}, to bieži izsaka procentos.",
]


# ---------------------------------------------------------------- veidnes
def _rinda(dati):
    return "; ".join(str(x) for x in dati)


def videjais(*dati):
    """Aritmētiskais vidējais datu kopai, kuras summa dalās ar skaitu."""
    s, n = sum(dati), len(dati)
    return ("Kāds ir aritmētiskais vidējais datiem  %s?" % _rinda(dati),
            V.izvele(V.dalu(s, n), s, n, max(dati), min(dati),
                     V.dalu(s, n) + 1 if isinstance(V.dalu(s, n), int)
                     else s - n), 0)


def amplituda(*dati):
    """Amplitūda ir lielākās un mazākās vērtības starpība."""
    return ("Kāda ir amplitūda datiem  %s?" % _rinda(dati),
            V.izvele(max(dati) - min(dati), max(dati), min(dati),
                     max(dati) + min(dati), sum(dati),
                     max(dati) - min(dati) + 1), 0)


def moda(*dati):
    """Moda ir biežāk sastopamā vērtība."""
    biez = max(set(dati), key=lambda x: dati.count(x))
    return ("Kāda ir moda datiem  %s?" % _rinda(dati),
            V.izvele(biez, max(dati), min(dati), len(dati),
                     sum(dati), biez + 1), 0)


def mediana(*dati):
    """Mediāna sakārtotai datu kopai ar nepāra elementu skaitu."""
    kart = sorted(dati)
    vid = kart[len(kart) // 2]
    return ("Kāda ir mediāna datiem  %s?" % _rinda(dati),
            V.izvele(vid, sum(dati) // len(dati), max(dati), min(dati),
                     len(dati), vid + 1), 0)


def relativais(biezums, kopa_):
    """Relatīvais biežums procentos."""
    return ("Vērtība sastopama %d reizes no %d datiem. Kāds ir relatīvais "
            "biežums?" % (biezums, kopa_),
            V.izvele("%d %%" % (biezums * 100 // kopa_),
                     "%d %%" % biezums, "%d %%" % kopa_,
                     "%d %%" % (kopa_ * 100 // biezums),
                     "%d %%" % (kopa_ - biezums),
                     "%d %%" % (biezums * 100 // kopa_ + 5)), 0)


FD = {
    "veids": "fd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 8.1. temata beigās. Pārbauda "
                "aritmētisko vidējo, amplitūdu, modu, mediānu, absolūto un "
                "relatīvo biežumu un datu analīzi.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina statistisko rādītāju nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir moda?",
              ["biežāk sastopamā vērtība", "vidējā vērtība",
               "lielākā vērtība", "vērtību skaits"], 0),
             ("Kas ir mediāna?",
              ["sakārtotas kopas vidējais elements",
               "biežāk sastopamā vērtība", "lielākā vērtība",
               "vērtību summa"], 0),
             ("Kas ir amplitūda?",
              ["lielākās un mazākās vērtības starpība", "vidējā vērtība",
               "vērtību skaits", "vērtību summa"], 0),
             ("Kas ir aritmētiskais vidējais?",
              ["summa, dalīta ar skaitu", "biežākā vērtība",
               "vidējais elements", "lielākā vērtība"], 0),
             ("Kas ir absolūtais biežums?",
              ["cik reižu vērtība sastopama", "vērtību summa",
               "vērtību daļa procentos", "lielākā vērtība"], 0),
             ("Kas ir relatīvais biežums?",
              ["biežuma attiecība pret visu datu skaitu",
               "cik reižu vērtība sastopama", "vērtību summa",
               "amplitūda"], 0),
             ("Kāpēc datus sakārto, meklējot mediānu?",
              ["lai atrastu vidējo elementu", "lai tie būtu skaisti",
               "lai saskaitītu ātrāk", "tas nav vajadzīgs"], 0),
             ("Vai datu kopai var būt vairākas modas?",
              ["jā", "nē", "tikai ar 10 datiem", "tikai ar veseliem"], 0),
         ]},
        {"sr": "Aprēķina aritmētisko vidējo",
         "stunda": TEMATS,
         "jautajumi": V.kopa(videjais, [
             (4, 6, 8), (2, 5, 8), (3, 7, 11), (5, 10, 15), (6, 9, 12),
             (1, 4, 7), (10, 20, 30), (8, 12, 16), (2, 4, 6, 8),
             (5, 7, 9, 11), (3, 6, 9, 12), (1, 3, 5, 7), (10, 14, 18, 22),
             (4, 8, 12, 16), (6, 12, 18, 24)]),
         },
        {"sr": "Aprēķina amplitūdu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(amplituda, [
             (3, 8, 5), (12, 4, 9), (7, 15, 10), (2, 11, 6), (20, 8, 14),
             (5, 17, 9), (25, 13, 19), (1, 9, 4), (30, 12, 21),
             (6, 22, 15), (18, 3, 11), (14, 28, 20), (9, 35, 24),
             (11, 26, 17), (40, 16, 29)]),
         },
        {"sr": "Nosaka modu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(moda, [
             (3, 5, 5, 7), (2, 4, 4, 9), (6, 8, 8, 11), (1, 3, 3, 10),
             (7, 9, 9, 12), (5, 5, 5, 8, 13), (4, 6, 6, 6, 15),
             (2, 2, 2, 7, 16), (10, 10, 12, 14), (8, 8, 11, 17),
             (9, 9, 13, 18), (3, 7, 7, 7, 19), (12, 12, 15, 20),
             (6, 11, 11, 21), (5, 14, 14, 22)]),
         },
        {"sr": "Nosaka mediānu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mediana, [
             (3, 7, 5), (2, 9, 4), (8, 1, 6), (12, 5, 10), (15, 7, 11),
             (4, 20, 13), (6, 18, 9), (2, 14, 8), (21, 3, 12),
             (5, 25, 17), (30, 7, 19), (11, 2, 6), (16, 24, 20),
             (9, 33, 22), (13, 27, 18)]),
         },
        {"sr": "Aprēķina relatīvo biežumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(relativais, [
             (5, 20), (3, 12), (7, 28), (4, 25), (9, 30), (6, 24),
             (8, 40), (12, 50), (2, 10), (15, 60), (11, 44), (14, 70),
             (18, 90), (16, 80), (10, 25)]),
         },
        {"sr": "Salīdzina statistiskos rādītājus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad aritmētiskais vidējais slikti raksturo datus?",
              ["ja ir dažas ļoti atšķirīgas vērtības",
               "ja visi dati ir vienādi", "ja datu ir daudz",
               "ja dati ir veseli skaitļi"], 0),
             ("Kurš rādītājs nav atkarīgs no ļoti lielas atsevišķas "
              "vērtības?", ["mediāna", "aritmētiskais vidējais",
                            "amplitūda", "summa"], 0),
             ("Algas: 500; 600; 700 un 5000 eiro. Kurš rādītājs raksturo "
              "labāk?", ["mediāna", "aritmētiskais vidējais", "amplitūda",
                         "moda"], 0),
             ("Ko rāda liela amplitūda?",
              ["datu izkliedi", "datu vidējo vērtību", "datu skaitu",
               "biežāko vērtību"], 0),
             ("Divām kopām vienāds vidējais, bet dažāda amplitūda. Ko tas "
              "nozīmē?", ["viena kopa ir izkliedētāka", "kopas ir vienādas",
                          "vienā ir vairāk datu", "tas nav iespējams"], 0),
             ("Kurš rādītājs der arī nečiparu datiem, piemēram, krāsām?",
              ["moda", "aritmētiskais vidējais", "mediāna", "amplitūda"], 0),
             ("Cik ir visu relatīvo biežumu summa?",
              ["100 %", "50 %", "vienmēr dažāda", "0 %"], 0),
             ("Kāpēc datus attēlo diagrammā?",
              ["lai tos būtu vieglāk salīdzināt", "lai būtu skaisti",
               "lai nerēķinātu", "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Lasa datus no tabulas",
         "stunda": TEMATS,
         "jautajumi": [
             ("Tabulā: 5 skolēni ieguva 6 balles, 8 — 7 balles, 7 — "
              "8 balles. Cik skolēnu kopā?", ["20", "21", "15", "18"], 0),
             ("Tajā pašā tabulā — kāda ir moda?",
              ["7 balles", "6 balles", "8 balles", "8 skolēni"], 0),
             ("Tajā pašā tabulā — kāds ir 7 baļļu absolūtais biežums?",
              ["8", "7", "5", "20"], 0),
             ("Tajā pašā tabulā — kāds ir 7 baļļu relatīvais biežums?",
              ["40 %", "35 %", "25 %", "8 %"], 0),
             ("Tajā pašā tabulā — kāda ir amplitūda?",
              ["2", "8", "6", "20"], 0),
             ("Tajā pašā tabulā — cik skolēnu ieguva vismaz 7 balles?",
              ["15", "8", "7", "20"], 0),
             ("Kā tabulā pārbauda, vai visi dati ievadīti?",
              ["saskaita biežumus", "saskaita vērtības",
               "salīdzina ar vidējo", "nekā"], 0),
             ("Ko rāda tabulas aile «biežums»?",
              ["cik reižu vērtība sastopama", "vērtību lielumu",
               "vērtību summu", "datu skaitu kopā"], 0),
         ]},
        {"sr": "Aprēķina vidējo no biežumu tabulas",
         "stunda": TEMATS,
         "jautajumi": [
             ("2 skolēni ieguva 5 balles, 3 — 10 balles. Kāds ir vidējais?",
              ["8", "7,5", "5", "15"], 0),
             ("4 skolēni ieguva 6 balles, 6 — 8 balles. Kāds ir vidējais?",
              ["7,2", "7", "14", "6"], 0),
             ("3 skolēni ieguva 4 balles, 2 — 9 balles. Kāds ir vidējais?",
              ["6", "6,5", "13", "5"], 0),
             ("5 skolēni ieguva 7 balles, 5 — 9 balles. Kāds ir vidējais?",
              ["8", "7", "16", "9"], 0),
             ("Kā aprēķina vidējo no biežumu tabulas?",
              ["reizina vērtības ar biežumiem", "saskaita vērtības",
               "ņem biežāko vērtību", "ņem vidējo vērtību"], 0),
             ("6 preces maksā 2 eiro, 4 — 7 eiro. Kāda ir vidējā cena?",
              ["4 eiro", "4,5 eiro", "9 eiro", "3 eiro"], 0),
             ("Vai vidējais var būt lielāks nekā lielākā vērtība?",
              ["nē", "jā", "tikai ar procentiem", "vienmēr"], 0),
             ("Vai vidējais var nesakrist ne ar vienu datu vērtību?",
              ["jā", "nē", "tikai ar daļām", "nekad"], 0),
         ]},
        {"sr": "Prognozē pēc datiem",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko ļauj darīt datu analīze?",
              ["prognozēt lieluma izmaiņas", "mainīt datus",
               "izvairīties no mērījumiem", "noteikt precīzu nākotni"], 0),
             ("Kāpēc prognoze var neīstenoties?",
              ["to ietekmē arī citi lielumi", "dati vienmēr ir kļūdaini",
               "matemātika ir neprecīza", "prognozes neveido"], 0),
             ("Kā prognozē tendenci no grafika?",
              ["skatās, vai vērtības aug vai sarūk",
               "skatās tikai pēdējo punktu", "saskaita punktus",
               "mēra grafika garumu"], 0),
             ("Kāpēc pētījumā vajag pietiekami daudz datu?",
              ["lai secinājumi būtu ticami", "lai būtu vairāk darba",
               "lai vidējais būtu lielāks", "tas nav vajadzīgs"], 0),
             ("Kas ir pētījuma pirmais solis?",
              ["mērķa formulēšana", "datu apstrāde", "secinājumi",
               "diagrammas zīmēšana"], 0),
             ("Kas ir pētījuma pēdējais solis?",
              ["secinājumu formulēšana", "datu vākšana",
               "mērķa formulēšana", "tabulas veidošana"], 0),
             ("Kā salīdzina divas objektu kopas?",
              ["salīdzina to vidējos lielumus un izkliedi",
               "salīdzina datu skaitu", "salīdzina tabulu izmērus",
               "salīdzina krāsas"], 0),
             ("Ko nozīmē, ja vienai kopai vidējais ir lielāks?",
              ["kopumā tās vērtības ir lielākas",
               "visas tās vērtības ir lielākas", "tajā ir vairāk datu",
               "tā ir precīzāka"], 0),
         ]},
        {"sr": "Zina datu attēlošanas veidus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad lieto sektoru diagrammu?",
              ["kad daļas kopā veido 100 %", "kad datu ir ļoti daudz",
               "kad dati ir negatīvi", "kad dati ir decimāldaļas"], 0),
             ("Kad lieto stabiņu diagrammu?",
              ["kad salīdzina atsevišķas vērtības",
               "kad daļas veido veselu", "kad dati mainās nepārtraukti",
               "nekad"], 0),
             ("Kad lieto līniju diagrammu?",
              ["kad rāda izmaiņas laikā", "kad daļas veido veselu",
               "kad dati nav skaitliski", "nekad"], 0),
             ("Ko obligāti norāda diagrammā?",
              ["asu nozīmi un mērvienības", "autora vārdu", "datumu",
               "krāsu skaitu"], 0),
             ("Kāpēc diagrammas ass jāsāk ar nulli?",
              ["citādi atšķirības izskatās lielākas", "tā ir tradīcija",
               "lai taupītu vietu", "tas nav svarīgi"], 0),
             ("Ko rāda sektora lielums sektoru diagrammā?",
              ["daļu no veselā", "absolūto vērtību", "amplitūdu",
               "mediānu"], 0),
             ("Kā sektoru diagrammā aprēķina sektora leņķi?",
              ["360° reizina ar daļu", "100 reizina ar daļu",
               "180° reizina ar daļu", "daļu dala ar 360°"], 0),
             ("Cik grādu ir sektoram, kas atbilst 25 %?",
              ["90°", "25°", "180°", "120°"], 0),
         ]},
        {"sr": "Izvērtē datu ticamību",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāpēc aptaujā svarīgs respondentu skaits?",
              ["mazā izlasē secinājumi ir nedroši", "lai būtu vairāk darba",
               "lai vidējais būtu lielāks", "tas nav svarīgs"], 0),
             ("Ko nozīmē, ja aptaujāti tikai draugi?",
              ["izlase nav objektīva", "izlase ir labāka",
               "rezultāts ir precīzāks", "tas nemaina neko"], 0),
             ("Vai viens mērījums pietiek secinājumam?",
              ["nē", "jā", "tikai fizikā", "tikai matemātikā"], 0),
             ("Kāpēc mērījumus atkārto?",
              ["lai samazinātu nejaušu kļūdu ietekmi", "lai būtu ilgāk",
               "lai dati būtu lielāki", "tas nav vajadzīgs"], 0),
             ("Ko dara ar acīmredzami kļūdainu vērtību?",
              ["pārbauda mērījumu", "vienkārši izdzēš",
               "aizvieto ar vidējo", "atstāj bez ievērības"], 0),
             ("Ko nozīmē «vidēji 2,3 bērni ģimenē»?",
              ["tas ir aprēķināts rādītājs, ne konkrēts skaits",
               "ģimenēs ir 2,3 bērni", "dati ir kļūdaini",
               "nav nozīmes"], 0),
             ("Kas ir izlase?",
              ["daļa no visas kopas", "visa kopa", "viens objekts",
               "vidējais lielums"], 0),
             ("Kāpēc pēta izlasi, nevis visu kopu?",
              ["visu kopu bieži nav iespējams aptaujāt", "tas ir precīzāk",
               "tā prasa noteikumi", "izlase ir lielāka"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 8,
    "temats": TEMATS,
    "nr": 1,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "1. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 8.1. temata noslēgumā. "
                "Pārbauda statistiskos rādītājus, datu lasīšanu no tabulas "
                "un diagrammas un datu analīzi.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina statistisko rādītāju nozīmi",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir moda?",
              ["biežāk sastopamā vērtība", "vidējā vērtība",
               "lielākā vērtība", "vērtību skaits"], 0),
             ("Kas ir mediāna?",
              ["sakārtotas kopas vidējais elements",
               "biežāk sastopamā vērtība", "lielākā vērtība",
               "vērtību summa"], 0),
             ("Kas ir amplitūda?",
              ["lielākās un mazākās vērtības starpība", "vidējā vērtība",
               "vērtību skaits", "vērtību summa"], 0),
             ("Kas ir relatīvais biežums?",
              ["biežuma attiecība pret visu datu skaitu",
               "cik reižu vērtība sastopama", "vērtību summa",
               "amplitūda"], 0),
             ("Kurš rādītājs der arī nečiparu datiem?",
              ["moda", "aritmētiskais vidējais", "mediāna", "amplitūda"], 0),
             ("Cik ir visu relatīvo biežumu summa?",
              ["100 %", "50 %", "vienmēr dažāda", "0 %"], 0),
             ("Ko rāda liela amplitūda?",
              ["datu izkliedi", "datu vidējo vērtību", "datu skaitu",
               "biežāko vērtību"], 0),
             ("Kāpēc datus sakārto, meklējot mediānu?",
              ["lai atrastu vidējo elementu", "lai tie būtu skaisti",
               "lai saskaitītu ātrāk", "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Aprēķina aritmētisko vidējo",
         "stunda": TEMATS,
         "jautajumi": V.kopa(videjais, [
             (5, 7, 9), (3, 6, 9), (4, 8, 12), (6, 10, 14), (2, 7, 12),
             (8, 11, 14), (10, 15, 20), (9, 13, 17), (3, 5, 7, 9),
             (6, 8, 10, 12), (4, 7, 10, 13), (2, 6, 10, 14),
             (11, 15, 19, 23), (5, 10, 15, 20), (7, 14, 21, 28)]),
         },
        {"sr": "Aprēķina amplitūdu un modu",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(amplituda, [
             (4, 9, 6), (13, 5, 10), (8, 16, 11), (3, 12, 7), (21, 9, 15),
             (7, 19, 12), (27, 14, 20)])
             + V.kopa(moda, [
                 (4, 6, 6, 8), (3, 5, 5, 10), (7, 9, 9, 12),
                 (2, 4, 4, 11), (8, 10, 10, 13), (6, 6, 6, 9, 14),
                 (5, 7, 7, 7, 16), (3, 3, 3, 8, 17)])),
         },
        {"sr": "Nosaka mediānu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(mediana, [
             (4, 8, 6), (3, 10, 5), (9, 2, 7), (13, 6, 11), (16, 8, 12),
             (5, 21, 14), (7, 19, 10), (3, 15, 9), (22, 4, 13),
             (6, 26, 18), (31, 8, 20), (12, 3, 7), (17, 25, 21),
             (10, 34, 23), (14, 28, 19)]),
         },
        {"sr": "Aprēķina relatīvo biežumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(relativais, [
             (6, 20), (4, 16), (9, 36), (5, 25), (12, 40), (7, 35),
             (10, 50), (14, 56), (3, 15), (18, 72), (13, 52), (16, 64),
             (20, 80), (11, 55), (8, 32)]),
         },
        {"sr": "Analizē un izvērtē datus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kad aritmētiskais vidējais slikti raksturo datus?",
              ["ja ir dažas ļoti atšķirīgas vērtības",
               "ja visi dati ir vienādi", "ja datu ir daudz",
               "ja dati ir veseli skaitļi"], 0),
             ("Kurš rādītājs nav jutīgs pret vienu ļoti lielu vērtību?",
              ["mediāna", "aritmētiskais vidējais", "amplitūda",
               "summa"], 0),
             ("Kā salīdzina divas objektu kopas?",
              ["salīdzina to vidējos lielumus un izkliedi",
               "salīdzina datu skaitu", "salīdzina tabulu izmērus",
               "salīdzina krāsas"], 0),
             ("Kāpēc aptaujā svarīgs respondentu skaits?",
              ["mazā izlasē secinājumi ir nedroši",
               "lai būtu vairāk darba", "lai vidējais būtu lielāks",
               "tas nav svarīgs"], 0),
             ("Kas ir izlase?",
              ["daļa no visas kopas", "visa kopa", "viens objekts",
               "vidējais lielums"], 0),
             ("Cik grādu ir sektoram, kas atbilst 25 %?",
              ["90°", "25°", "180°", "120°"], 0),
             ("Kad lieto līniju diagrammu?",
              ["kad rāda izmaiņas laikā", "kad daļas veido veselu",
               "kad dati nav skaitliski", "nekad"], 0),
             ("Kāpēc mērījumus atkārto?",
              ["lai samazinātu nejaušu kļūdu ietekmi", "lai būtu ilgāk",
               "lai dati būtu lielāki", "tas nav vajadzīgs"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Aprēķina statistiskos rādītājus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Datu kopa",
             lambda a, b, c, d, e: [
                 ("Dati %d; %d; %d; %d; %d;  vidējais = ……"
                  % (a, b, c, d, e), V.dalu(a + b + c + d + e, 5)),
                 ("Tie paši dati;  amplitūda = ……",
                  V.sk(max(a, b, c, d, e) - min(a, b, c, d, e))),
                 ("Tie paši dati;  mediāna = ……",
                  V.sk(sorted([a, b, c, d, e])[2])),
                 ("Tie paši dati;  moda = ……",
                  V.sk(max({a, b, c, d, e},
                           key=[a, b, c, d, e].count)))],
             [(3, 5, 5, 7, 10), (2, 4, 4, 8, 12), (6, 8, 8, 10, 13),
              (1, 3, 3, 6, 12), (7, 9, 9, 11, 14), (5, 5, 8, 10, 12),
              (4, 6, 6, 9, 15), (2, 2, 7, 9, 15), (10, 10, 12, 14, 19),
              (8, 8, 11, 13, 20), (9, 9, 13, 15, 19), (3, 7, 7, 11, 17),
              (12, 12, 15, 18, 23), (6, 11, 11, 14, 18),
              (5, 14, 14, 16, 21)]),
         },
        {"sr": "Aprēķina biežumus",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Biežumi",
             lambda b, n: [
                 ("Vērtība sastopama %d reizes no %d;  absolūtais biežums "
                  "= ……" % (b, n), V.sk(b)),
                 ("Tā pati vērtība;  relatīvais biežums = …… %%",
                  V.sk(b * 100 // n)),
                 ("Pārējo vērtību relatīvais biežums = …… %%",
                  V.sk(100 - b * 100 // n))],
             [(5, 20), (3, 12), (7, 28), (4, 25), (9, 30), (6, 24),
              (8, 40), (12, 50), (2, 10), (15, 60), (11, 44), (14, 70),
              (18, 90), (16, 80), (10, 25)]),
         },
        {"sr": "Analizē datu kopu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Datu analīze",
             lambda a, b, c, d, e: {
                 "teksts": "Kontroldarbā skolēni ieguva punktus:  %d; %d; "
                           "%d; %d; %d.   a) Aprēķini aritmētisko vidējo!   "
                           "b) Nosaki mediānu!   c) Nosaki amplitūdu!   "
                           "d) Kurš rādītājs labāk raksturo šos datus? "
                           "Pamato!" % (a, b, c, d, e),
                 "kriteriji": [
                     "a) (%d + %d + %d + %d + %d) : 5 = %s.   (1 p.)"
                     % (a, b, c, d, e, V.dalu(a + b + c + d + e, 5)),
                     "b) %s.   (1 p.)" % V.sk(sorted([a, b, c, d, e])[2]),
                     "c) %d − %d = %d.   (1 p.)"
                     % (max(a, b, c, d, e), min(a, b, c, d, e),
                        max(a, b, c, d, e) - min(a, b, c, d, e)),
                     "d) Ja viena vērtība stipri atšķiras, labāk raksturo "
                     "mediāna.   (1 p.)"]},
             [(3, 5, 5, 7, 10), (2, 4, 4, 8, 12), (6, 8, 8, 10, 13),
              (1, 3, 3, 6, 12), (7, 9, 9, 11, 14), (5, 5, 8, 10, 12),
              (4, 6, 6, 9, 15), (2, 2, 7, 9, 15), (10, 10, 12, 14, 19),
              (8, 8, 11, 13, 20), (9, 9, 13, 15, 19), (3, 7, 7, 11, 17),
              (12, 12, 15, 18, 23), (6, 11, 11, 14, 18),
              (5, 14, 14, 16, 21)]),
         },
        {"sr": "Salīdzina divas datu kopas",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Divas klases",
             lambda a1, a2, a3, b1, b2, b3: {
                 "ievads": "A klasē punkti:  %d; %d; %d.   B klasē:  "
                           "%d; %d; %d." % (a1, a2, a3, b1, b2, b3),
                 "jaut": [("Aprēķini abu klašu vidējos!", 1),
                          ("Aprēķini abu klašu amplitūdas!", 1),
                          ("Kurā klasē rezultāti ir vienmērīgāki?", 1)],
                 "atbildes": [
                     "1) A: %s;  B: %s.   (1 p.)"
                     % (V.dalu(a1 + a2 + a3, 3), V.dalu(b1 + b2 + b3, 3)),
                     "2) A: %d;  B: %d.   (1 p.)"
                     % (max(a1, a2, a3) - min(a1, a2, a3),
                        max(b1, b2, b3) - min(b1, b2, b3)),
                     "3) Tajā, kurai amplitūda ir mazāka.   (1 p.)"]},
             [(4, 6, 8, 2, 6, 10), (5, 7, 9, 3, 7, 11),
              (6, 9, 12, 4, 9, 14), (3, 6, 9, 1, 6, 11),
              (8, 10, 12, 5, 10, 15), (7, 11, 15, 9, 11, 13),
              (2, 5, 8, 4, 5, 6), (10, 14, 18, 12, 14, 16),
              (9, 12, 15, 6, 12, 18), (11, 13, 15, 8, 13, 18),
              (12, 16, 20, 14, 16, 18), (5, 10, 15, 8, 10, 12),
              (6, 12, 18, 10, 12, 14), (13, 17, 21, 15, 17, 19),
              (7, 13, 19, 11, 13, 15)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
