# -*- coding: utf-8 -*-
"""Matemātika, 7. klase. 7.8. Kādi ir paņēmieni nezināmā noteikšanai?

Saturs abiem temata darbiem. Sasniedzamie rezultāti un jēdzieni no oficiālās
programmas (PD_generate/mat_p.pdf, 7. klase, 7.8. temats): vienādojums un tā
sakne, ekvivalenti vienādojumi un ekvivalentie pārveidojumi, lineāra
vienādojuma atrisināšana (spriežot, pārveidojot, grafiski), proporcija un tās
nezināmā locekļa aprēķināšana, situāciju uzdevumi un rezultāta atbilstība
dzīves situācijai.

Rēķinu jautājumi nāk no veidnēm (mat_varianti.py): viena veidne un skaitļu
saraksts dod daudz līdzvērtīgu jautājumu, tāpēc izlozētie darbi patiešām
atšķiras.
"""

import mat_varianti as V

PRIEKSMETS = "Matemātika  |  7. klase"
TEMATS = "7.8."
NOSAUKUMS = "Kādi ir paņēmieni nezināmā noteikšanai?"

ATGADNE = [
    "Vienādojuma abām pusēm drīkst pieskaitīt vai atņemt vienu un to pašu "
    "lielumu, kā arī reizināt vai dalīt abas puses ar vienu un to pašu "
    "skaitli (ne ar nulli) — sakne nemainās.",
    "Lineārs vienādojums:   ax + b = c   ⟹   ax = c − b   ⟹   x = "
    "{c − b|a}",
    "Proporcija ir divu attiecību vienādība:   {a|b} = {c|d}   ·   malējo "
    "locekļu reizinājums ir vienāds ar vidējo:   a · d = b · c",
]


# ---------------------------------------------------------------- veidnes
def vienadojums(a, b, x):
    """Lineārs vienādojums  ax + b = c  ar veselu sakni."""
    c = a * x + b
    zime = "+" if b >= 0 else "−"
    return ("Atrisini vienādojumu  %dx %s %d = %d." % (a, zime, abs(b), c),
            V.izvele("x = %s" % V.sk(x), "x = %s" % V.sk(-x),
                     "x = %s" % V.sk(c), "x = %s" % V.sk(c - b),
                     "x = %s" % V.sk(x + 1), "x = %s" % V.sk(c + b),
                     "x = %s" % V.sk(x - 1)), 0)


def vienkarss(b, x):
    """Vienādojums  x + b = c - risina, spriežot par darbības locekļiem."""
    c = x + b
    zime = "+" if b >= 0 else "−"
    return ("Atrisini vienādojumu  x %s %d = %d." % (zime, abs(b), c),
            V.izvele("x = %s" % V.sk(x), "x = %s" % V.sk(-x),
                     "x = %s" % V.sk(c + b), "x = %s" % V.sk(c),
                     "x = %s" % V.sk(b), "x = %s" % V.sk(x + 2)), 0)


def reizinajums(a, x):
    """Vienādojums  ax = c."""
    c = a * x
    return ("Atrisini vienādojumu  %dx = %d." % (a, c),
            V.izvele("x = %s" % V.sk(x), "x = %s" % V.sk(c),
                     "x = %s" % V.sk(c * a), "x = %s" % V.sk(a),
                     "x = %s" % V.sk(c - a), "x = %s" % V.sk(x + 1)), 0)


def proporcija(a, b, c):
    """Proporcijas nezināmais loceklis:  {a|b} = {x|c}."""
    x = a * c // b
    return ("Atrisini proporciju  {%d|%d} = {x|%d}." % (a, b, c),
            V.izvele("x = %s" % V.sk(x), "x = %s" % V.sk(b * c // a),
                     "x = %s" % V.sk(a * b // c if c else 0),
                     "x = %s" % V.sk(a + c - b), "x = %s" % V.sk(x + 1),
                     "x = %s" % V.sk(a * c)), 0)


def sakne(a, b, x, parbaude):
    """Vai dotais skaitlis ir vienādojuma sakne - gan jā, gan nē."""
    c = a * x + b
    zime = "+" if b >= 0 else "−"
    ir = (parbaude == x)
    return ("Vai %d ir vienādojuma  %dx %s %d = %d  sakne?"
            % (parbaude, a, zime, abs(b), c),
            V.izvele("jā" if ir else "nē", "nē" if ir else "jā",
                     "tikai ja a = 1", "nevar noteikt"), 0)


def situacija(n, kop):
    """Situāciju uzdevums, ko apraksta ar lineāru vienādojumu."""
    return ("Par %d vienādām biļetēm samaksāja %d eiro. Cik maksā viena "
            "biļete?" % (n, kop),
            V.izvele("%d eiro" % (kop // n), "%d eiro" % (kop * n),
                     "%d eiro" % (kop - n), "%d eiro" % (kop + n),
                     "%d eiro" % (kop // n + 1), "%d eiro" % n), 0)


FD = {
    "veids": "fd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 12 jautājumi · 15 minūtes",
    "laiks": 15,
    "apraksts": "Formatīvais darbs 7.8. temata beigās. Pārbauda vienādojuma "
                "un saknes jēdzienu, ekvivalentos pārveidojumus, lineāra "
                "vienādojuma atrisināšanu, proporciju un situāciju "
                "uzdevumus.",
    "atgadne": ATGADNE,
    "grupas": [
        {"sr": "Zina vienādojuma un saknes jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir vienādojums?",
              ["vienādība, kas satur nezināmo", "jebkura vienādība",
               "izteiksme ar mainīgo", "nevienādība"], 0),
             ("Kas ir vienādojuma sakne?",
              ["skaitlis, ar kuru vienādība ir patiesa",
               "jebkurš skaitlis", "koeficients", "nezināmais"], 0),
             ("Ko nozīmē atrisināt vienādojumu?",
              ["noteikt visas saknes un pamatot, ka citu nav",
               "atrast vienu sakni", "pārrakstīt vienādojumu",
               "uzzīmēt grafiku"], 0),
             ("Kad vienādojumi ir ekvivalenti?",
              ["ja tiem ir vienas un tās pašas saknes",
               "ja tie izskatās vienādi", "ja tiem ir viens nezināmais",
               "ja saknes ir veselas"], 0),
             ("Vai x = 3 ir vienādojuma  2x = 6  sakne?",
              ["jā", "nē", "tikai ja x > 0", "nevar noteikt"], 0),
             ("Vai x = 2 ir vienādojuma  3x + 1 = 10  sakne?",
              ["nē", "jā", "tikai aptuveni", "nevar noteikt"], 0),
             ("Cik sakņu ir vienādojumam  x + 1 = x + 2?",
              ["neviena", "viena", "divas", "bezgalīgi daudz"], 0),
             ("Cik sakņu ir vienādojumam  2x = 2x?",
              ["bezgalīgi daudz", "viena", "neviena", "divas"], 0),
         ]},
        {"sr": "Zina ekvivalentos pārveidojumus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Ko drīkst darīt ar vienādojuma abām pusēm?",
              ["pieskaitīt vienu un to pašu lielumu",
               "pieskaitīt dažādus lielumus", "izsvītrot nezināmo",
               "mainīt zīmi tikai vienā pusē"], 0),
             ("Vai drīkst abas puses reizināt ar 3?",
              ["jā", "nē", "tikai ar 1", "tikai ar 0"], 0),
             ("Vai drīkst abas puses dalīt ar 0?",
              ["nē", "jā", "tikai ja sakne ir 0", "vienmēr"], 0),
             ("Kas notiek ar saknēm pēc ekvivalenta pārveidojuma?",
              ["tās nemainās", "tās mainās", "tās pazūd",
               "tās kļūst negatīvas"], 0),
             ("Ko nozīmē pārnest locekli uz otru pusi?",
              ["atņemt to abām pusēm un mainīt zīmi",
               "vienkārši pārrakstīt", "reizināt ar −1",
               "izsvītrot to"], 0),
             ("Kā no  x + 5 = 12  iegūst x?",
              ["abām pusēm atņem 5", "abām pusēm pieskaita 5",
               "abas puses dala ar 5", "abas puses reizina ar 5"], 0),
             ("Kā no  4x = 20  iegūst x?",
              ["abas puses dala ar 4", "abas puses reizina ar 4",
               "abām pusēm atņem 4", "abām pusēm pieskaita 4"], 0),
             ("Kāpēc risinājumu pārbauda?",
              ["lai pārliecinātos, ka vienādība ir patiesa",
               "lai būtu garāks risinājums", "tā prasa skolotājs",
               "tas nav vajadzīgs"], 0),
         ]},
        {"sr": "Atrisina vienkāršu vienādojumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vienkarss, [
             (5, 7), (3, 9), (-4, 12), (8, 6), (-6, 15), (11, 4),
             (-9, 20), (7, 13), (-2, 18), (14, 5), (-11, 25), (6, 21),
             (-7, 30), (12, 8), (-13, 16)]),
         },
        {"sr": "Atrisina vienādojumu ar reizinājumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(reizinajums, [
             (3, 5), (4, 7), (5, 6), (6, 4), (7, 8), (2, 13), (8, 5),
             (9, 3), (10, 7), (11, 4), (12, 6), (13, 2), (14, 5),
             (15, 3), (16, 4)]),
         },
        {"sr": "Atrisina lineāru vienādojumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vienadojums, [
             (2, 3, 4), (3, -1, 5), (4, 2, 3), (5, -3, 6), (2, 7, 8),
             (6, 1, 2), (3, 5, 7), (7, -2, 4), (4, -5, 9), (8, 3, 2),
             (5, 4, 6), (9, -1, 3), (6, -4, 5), (10, 2, 7), (3, 8, 11)]),
         },
        {"sr": "Pārbauda, vai skaitlis ir sakne",
         "stunda": TEMATS,
         "jautajumi": V.kopa(sakne, [
             (2, 3, 4, 4), (3, -1, 5, 6), (4, 2, 3, 3), (5, -3, 6, 5),
             (2, 7, 8, 8), (6, 1, 2, 3), (3, 5, 7, 7), (7, -2, 4, 5),
             (4, -5, 9, 9), (8, 3, 2, 1), (5, 4, 6, 6), (9, -1, 3, 4),
             (6, -4, 5, 5), (10, 2, 7, 6), (3, 8, 11, 11)]),
         },
        {"sr": "Zina proporcijas jēdzienu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir proporcija?",
              ["divu attiecību vienādība", "divu skaitļu summa",
               "divu skaitļu reizinājums", "nevienādība"], 0),
             ("Kā sauc a un d proporcijā  {a|b} = {c|d}?",
              ["malējie locekļi", "vidējie locekļi", "koeficienti",
               "saknes"], 0),
             ("Kā sauc b un c proporcijā  {a|b} = {c|d}?",
              ["vidējie locekļi", "malējie locekļi", "koeficienti",
               "saknes"], 0),
             ("Kāda ir proporcijas pamatīpašība?",
              ["a · d = b · c", "a + d = b + c", "a − d = b − c",
               "a : d = b : c"], 0),
             ("Vai {2|3} = {4|6} ir proporcija?",
              ["jā", "nē", "tikai saīsinot", "nevar noteikt"], 0),
             ("Vai {2|3} = {3|4} ir proporcija?",
              ["nē", "jā", "tikai aptuveni", "nevar noteikt"], 0),
             ("Kā no proporcijas iegūst nezināmo?",
              ["lieto pamatīpašību un atrisina vienādojumu",
               "saskaita locekļus", "atņem locekļus", "saīsina daļas"], 0),
             ("Kur proporciju lieto?",
              ["mērogā, procentos, recepšu pārrēķinos",
               "tikai ģeometrijā", "tikai fizikā", "tikai kartēs"], 0),
         ]},
        {"sr": "Aprēķina proporcijas nezināmo locekli",
         "stunda": TEMATS,
         "jautajumi": V.kopa(proporcija, [
             (2, 3, 12), (3, 4, 20), (5, 2, 8), (4, 5, 15), (6, 3, 9),
             (7, 2, 10), (2, 5, 25), (8, 4, 12), (9, 3, 6), (3, 7, 14),
             (10, 5, 20), (4, 6, 18), (11, 2, 4), (5, 8, 24), (12, 3, 15)]),
         },
        {"sr": "Atrisina vienādojumu, spriežot",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kāds skaitlis, reizināts ar 6, dod 42?",
              ["7", "36", "48", "252"], 0),
             ("Kāds skaitlis, pieskaitot 9, dod 23?",
              ["14", "32", "9", "23"], 0),
             ("No kāda skaitļa atņemot 15, iegūst 27?",
              ["42", "12", "15", "27"], 0),
             ("Kāds skaitlis, dalīts ar 4, dod 9?",
              ["36", "13", "5", "2,25"], 0),
             ("Kāds skaitlis ir par 8 mazāks nekā 31?",
              ["23", "39", "8", "31"], 0),
             ("Kāds skaitlis ir 5 reizes lielāks nekā 12?",
              ["60", "17", "7", "2,4"], 0),
             ("Divu skaitļu summa ir 20, viens no tiem 8. Kāds ir otrs?",
              ["12", "28", "8", "160"], 0),
             ("Divu skaitļu reizinājums ir 36, viens no tiem 4. Kāds ir "
              "otrs?", ["9", "32", "40", "144"], 0),
         ]},
        {"sr": "Atrisina vienādojumu grafiski",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kā vienādojumu atrisina grafiski?",
              ["abas puses pieraksta kā funkcijas un zīmē grafikus",
               "zīmē tikai vienu grafiku", "mēra grafika garumu",
               "saskaita koordinātas"], 0),
             ("Ko rāda grafiku krustpunkta abscisa?",
              ["vienādojuma sakni", "funkcijas vērtību",
               "koeficientu k", "grafika garumu"], 0),
             ("Cik sakņu ir, ja grafiki krustojas vienā punktā?",
              ["viena", "neviena", "divas", "bezgalīgi daudz"], 0),
             ("Cik sakņu ir, ja grafiki ir paralēli?",
              ["neviena", "viena", "divas", "bezgalīgi daudz"], 0),
             ("Cik sakņu ir, ja grafiki sakrīt?",
              ["bezgalīgi daudz", "viena", "neviena", "divas"], 0),
             ("Vienādojumam  2x = x + 3  atbilst grafiki...",
              ["y = 2x un y = x + 3", "tikai y = 2x", "tikai y = x + 3",
               "y = 2x + 3"], 0),
             ("Tā paša vienādojuma sakne ir...",
              ["x = 3", "x = 1", "x = 6", "x = 0"], 0),
             ("Kāpēc grafisko paņēmienu lieto retāk?",
              ["tas dod tikai aptuvenu sakni", "tas ir aizliegts",
               "tas ir ātrāks", "tas ir precīzāks"], 0),
         ]},
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(situacija, [
             (4, 20), (5, 35), (3, 27), (6, 48), (7, 42),
             (8, 64), (2, 18), (9, 54), (10, 70), (12, 96),
             (11, 55), (13, 91), (14, 84), (15, 75),
             (16, 112)]),
         },
        {"sr": "Izvērtē atrisinājuma atbilstību situācijai",
         "stunda": TEMATS,
         "jautajumi": [
             ("Uzdevumā meklē skolēnu skaitu; sanāk x = 7,5. Ko darīt?",
              ["pārbaudīt aprēķinu — skaits ir vesels skaitlis",
               "noapaļot uz augšu", "noapaļot uz leju",
               "pieņemt 7,5 skolēnus"], 0),
             ("Uzdevumā meklē cenu; sanāk x = −20. Ko tas nozīmē?",
              ["risinājumā ir kļūda", "prece ir bez maksas",
               "cena ir 20 eiro", "veikals piemaksā"], 0),
             ("Kāpēc atbildi salīdzina ar situāciju?",
              ["lai pamanītu neiespējamu rezultātu", "lai būtu garāks "
               "risinājums", "tā prasa skolotājs", "tas nav vajadzīgs"], 0),
             ("Kas ir matemātiskā modeļa pirmais solis?",
              ["situāciju aprakstīt matemātiski", "atrisināt vienādojumu",
               "uzrakstīt atbildi", "uzzīmēt grafiku"], 0),
             ("Kas ir pēdējais solis?",
              ["atbildes izvērtēšana situācijā", "vienādojuma sastādīšana",
               "vienādojuma atrisināšana", "skices zīmēšana"], 0),
             ("Ar ko apzīmē meklēto lielumu?",
              ["ar burtu", "ar skaitli", "ar krāsu", "ar zīmējumu"], 0),
             ("Uzdevumā meklē laiku; sanāk x = 0. Ko tas nozīmē?",
              ["notikums sākas uzreiz", "risinājumā vienmēr ir kļūda",
               "laika nav", "uzdevums ir aplams"], 0),
             ("Kāpēc uzdevumā pieraksta, ko apzīmē x?",
              ["lai risinājums būtu saprotams", "lai būtu garāk",
               "lai atbilde būtu lielāka", "tas nav vajadzīgs"], 0),
         ]},
    ],
}

PD = {
    "veids": "pd",
    "klase": 7,
    "temats": TEMATS,
    "nr": 8,
    "nosaukums": NOSAUKUMS,
    "prieksmets": PRIEKSMETS,
    "kicker": "8. temats · 20 punkti · 40 minūtes",
    "laiks": 40,
    "apraksts": "Summatīvais pārbaudes darbs 7.8. temata noslēgumā. "
                "Pārbauda lineāra vienādojuma atrisināšanu, ekvivalentos "
                "pārveidojumus, proporciju un situāciju uzdevumus ar "
                "vienādojumu.",
    "atgadne": ATGADNE,
    "tests": [
        {"sr": "Zina vienādojuma jēdzienus",
         "stunda": TEMATS,
         "jautajumi": [
             ("Kas ir vienādojums?",
              ["vienādība, kas satur nezināmo", "jebkura vienādība",
               "izteiksme ar mainīgo", "nevienādība"], 0),
             ("Kas ir vienādojuma sakne?",
              ["skaitlis, ar kuru vienādība ir patiesa",
               "jebkurš skaitlis", "koeficients", "nezināmais"], 0),
             ("Kad vienādojumi ir ekvivalenti?",
              ["ja tiem ir vienas un tās pašas saknes",
               "ja tie izskatās vienādi", "ja tiem ir viens nezināmais",
               "ja saknes ir veselas"], 0),
             ("Vai drīkst abas puses dalīt ar 0?",
              ["nē", "jā", "tikai ja sakne ir 0", "vienmēr"], 0),
             ("Ko nozīmē pārnest locekli uz otru pusi?",
              ["atņemt to abām pusēm un mainīt zīmi",
               "vienkārši pārrakstīt", "reizināt ar −1",
               "izsvītrot to"], 0),
             ("Cik sakņu ir vienādojumam  x + 1 = x + 2?",
              ["neviena", "viena", "divas", "bezgalīgi daudz"], 0),
             ("Kāpēc risinājumu pārbauda?",
              ["lai pārliecinātos, ka vienādība ir patiesa",
               "lai būtu garāks risinājums", "tā prasa skolotājs",
               "tas nav vajadzīgs"], 0),
             ("Ko rāda grafiku krustpunkta abscisa?",
              ["vienādojuma sakni", "funkcijas vērtību",
               "koeficientu k", "grafika garumu"], 0),
         ]},
        {"sr": "Atrisina vienkāršus vienādojumus",
         "stunda": TEMATS,
         "jautajumi": (V.kopa(vienkarss, [
             (6, 8), (4, 11), (-5, 14), (9, 7), (-8, 17), (12, 5), (-10, 22)])
             + V.kopa(reizinajums, [
                 (4, 6), (5, 8), (6, 7), (7, 5), (8, 9), (9, 4), (11, 6),
                 (12, 3)])),
         },
        {"sr": "Atrisina lineāru vienādojumu",
         "stunda": TEMATS,
         "jautajumi": V.kopa(vienadojums, [
             (3, 4, 5), (4, -2, 6), (5, 3, 4), (6, -5, 7), (2, 9, 3),
             (7, 1, 5), (8, -3, 2), (9, 4, 6), (10, -1, 4), (11, 2, 3),
             (12, -6, 5), (13, 3, 2), (14, -2, 4), (15, 5, 3), (16, 1, 6)]),
         },
        {"sr": "Aprēķina proporcijas nezināmo locekli",
         "stunda": TEMATS,
         "jautajumi": V.kopa(proporcija, [
             (3, 2, 8), (4, 3, 15), (2, 7, 21), (5, 4, 16), (6, 5, 25),
             (7, 3, 12), (8, 2, 6), (9, 4, 20), (10, 3, 9), (11, 5, 10),
             (12, 4, 8), (2, 9, 27), (13, 2, 10), (14, 7, 21), (15, 5, 5)]),
         },
        {"sr": "Risina situāciju uzdevumus",
         "stunda": TEMATS,
         "jautajumi": V.kopa(situacija, [
             (5, 40), (6, 54), (4, 36), (7, 63), (8, 72),
             (9, 81), (3, 24), (10, 90), (11, 88), (12, 108),
             (13, 78), (14, 98), (15, 120), (16, 96),
             (2, 26)]),
         },
        {"sr": "Izvērtē atrisinājumu",
         "stunda": TEMATS,
         "jautajumi": [
             ("Uzdevumā meklē skolēnu skaitu; sanāk x = 7,5. Ko darīt?",
              ["pārbaudīt aprēķinu — skaits ir vesels skaitlis",
               "noapaļot uz augšu", "noapaļot uz leju",
               "pieņemt 7,5 skolēnus"], 0),
             ("Uzdevumā meklē cenu; sanāk x = −20. Ko tas nozīmē?",
              ["risinājumā ir kļūda", "prece ir bez maksas",
               "cena ir 20 eiro", "veikals piemaksā"], 0),
             ("Kas ir matemātiskā modeļa pirmais solis?",
              ["situāciju aprakstīt matemātiski", "atrisināt vienādojumu",
               "uzrakstīt atbildi", "uzzīmēt grafiku"], 0),
             ("Ar ko apzīmē meklēto lielumu?",
              ["ar burtu", "ar skaitli", "ar krāsu", "ar zīmējumu"], 0),
             ("Kāda ir proporcijas pamatīpašība?",
              ["a · d = b · c", "a + d = b + c", "a − d = b − c",
               "a : d = b : c"], 0),
             ("Vai {3|4} = {6|8} ir proporcija?",
              ["jā", "nē", "tikai saīsinot", "nevar noteikt"], 0),
             ("Kāpēc atbildi salīdzina ar situāciju?",
              ["lai pamanītu neiespējamu rezultātu",
               "lai būtu garāks risinājums", "tā prasa skolotājs",
               "tas nav vajadzīgs"], 0),
             ("Kāds skaitlis, reizināts ar 8, dod 56?",
              ["7", "48", "64", "448"], 0),
         ]},
    ],
    "uzdevumi": [
        {"sr": "Atrisina vienādojumus",
         "stunda": TEMATS, "punkti": 4, "lapa": 1,
         "varianti": V.parveide(
             "Atrisini vienādojumu",
             lambda a, b, x, p, q: [
                 ("x + %d = %d;   x = ……" % (b, x + b), V.sk(x)),
                 ("%dx = %d;   x = ……" % (a, a * x), V.sk(x)),
                 ("%dx + %d = %d;   x = ……" % (a, b, a * x + b), V.sk(x)),
                 ("{%d|%d} = {x|%d};   x = ……" % (p, q, q * 2),
                  V.sk(p * 2))],
             [(2, 3, 4, 5, 2), (3, 5, 6, 7, 3), (4, 2, 5, 3, 4),
              (5, 7, 3, 9, 5), (6, 4, 7, 11, 2), (7, 1, 8, 4, 3),
              (8, 6, 2, 13, 4), (9, 3, 5, 6, 5), (10, 8, 4, 15, 3),
              (11, 2, 6, 8, 2), (12, 5, 3, 17, 4), (13, 7, 2, 10, 5),
              (14, 4, 5, 19, 3), (15, 9, 4, 12, 2), (16, 3, 6, 21, 4)]),
         },
        {"sr": "Aprēķina proporcijas nezināmo",
         "stunda": TEMATS, "punkti": 3, "lapa": 1,
         "varianti": V.parveide(
             "Proporcija",
             lambda a, b, c: [
                 ("{%d|%d} = {x|%d};   x = ……" % (a, b, c),
                  V.sk(a * c // b)),
                 ("{x|%d} = {%d|%d};   x = ……" % (b, a, c),
                  V.sk(a * b // c)),
                 ("{%d|x} = {%d|%d};   x = ……" % (a, b, c),
                  V.sk(a * c // b))],
             [(2, 3, 12), (3, 4, 20), (5, 2, 8), (4, 5, 15), (6, 3, 9),
              (7, 2, 10), (2, 5, 25), (8, 4, 12), (9, 3, 6), (3, 7, 14),
              (10, 5, 20), (4, 6, 18), (11, 2, 4), (5, 8, 24),
              (12, 3, 15)]),
         },
        {"sr": "Risina situāciju uzdevumu ar vienādojumu",
         "stunda": TEMATS, "punkti": 4, "lapa": 2,
         "varianti": V.aprekins(
             "Situāciju uzdevums",
             lambda cena, n, papild: {
                 "teksts": "Par %d vienādām biļetēm un vienu programmiņu "
                           "par %d eiro samaksāja %d eiro.   a) Apzīmē "
                           "biļetes cenu ar x un uzraksti vienādojumu!   "
                           "b) Atrisini to!   c) Cik maksā viena biļete?   "
                           "d) Cik maksātu %d biļetes?"
                           % (n, papild, cena * n + papild, n + 2),
                 "kriteriji": [
                     "a) %dx + %d = %d.   (1 p.)"
                     % (n, papild, cena * n + papild),
                     "b) %dx = %d.   (1 p.)" % (n, cena * n),
                     "c) x = %d eiro.   (1 p.)" % cena,
                     "d) %d · %d = %d eiro.   (1 p.)"
                     % (n + 2, cena, (n + 2) * cena)]},
             [(5, 4, 3), (6, 5, 2), (4, 6, 7), (7, 3, 5), (8, 4, 6),
              (9, 5, 4), (3, 8, 9), (10, 6, 3), (11, 4, 8), (12, 3, 10),
              (13, 5, 5), (14, 4, 12), (15, 6, 7), (16, 3, 9), (20, 5, 6)]),
         },
        {"sr": "Pamato vienādojuma risinājumu",
         "stunda": TEMATS, "punkti": 3, "lapa": 2,
         "varianti": V.jautajumi(
             "Vienādojuma pārveidojumi",
             lambda a, b, x: {
                 "ievads": "Dots vienādojums  %dx + %d = %d."
                           % (a, b, a * x + b),
                 "jaut": [("Kādu pārveidojumu veiksi vispirms?", 1),
                          ("Atrisini vienādojumu!", 1),
                          ("Pārbaudi atrisinājumu!", 1)],
                 "atbildes": [
                     "1) Abām pusēm atņem %d.   (1 p.)" % b,
                     "2) %dx = %d,  x = %d.   (1 p.)"
                     % (a, a * x, x),
                     "3) %d · %d + %d = %d — pareizi.   (1 p.)"
                     % (a, x, b, a * x + b)]},
             [(2, 3, 4), (3, 5, 6), (4, 2, 5), (5, 7, 3), (6, 4, 7),
              (7, 1, 8), (8, 6, 2), (9, 3, 5), (10, 8, 4), (11, 2, 6),
              (12, 5, 3), (13, 7, 2), (14, 4, 5), (15, 9, 4), (16, 3, 6)]),
         },
    ],
}

DARBI = {"fd": FD, "pd": PD}
