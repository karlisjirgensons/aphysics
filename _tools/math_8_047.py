# -*- coding: utf-8 -*-
"""8. klase, 47. stunda: «Kas ir skaitlis pī?»

π atklāj ar mērījumu: jebkuram aplim apkārtmērs dalīts ar diametru ir
apmēram 3,14. Slīdnis «notin» riņķa līniju uz taisnes. Stundas beigās π
ir gatavs nākamajai stundai - pirmajam iracionālajam skaitlim.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, rinkis, restis,
                         taisne)

TEMA = "Kas ir skaitlis pī?"

MERKIS = ("Sapratīsim, ka riņķa līnijas garuma un diametra dalījums ir "
          "skaitlis π, un lietosim tā tuvinājumu.")

SATURS = [
    Sakums("Riņķa līnija ir nedaudz vairāk par 3 diametriem",
           zimejums=rinkis(diametrs="d", paraksts="C = π · d"),
           paraksts="Jebkuram aplim C : d ir viens un tas pats skaitlis.",
           fakti=["Šo skaitli sauc par pī un apzīmē ar π.",
                  "π ≈ 3,14.",
                  "Tas ir vienāds glāzei, ritenim un planētai."]),

    Slidnis("Notini riteni", [
        {"v": "d = 1", "teksts": "Ritenis ar diametru 1",
         "zim": taisne(0, 4, 1, [(0, "sākums")])},
        {"v": "Pusapgrieziens", "teksts": "Nobrauca ≈ 1,57",
         "zim": taisne(0, 4, 1, [(0, ""), (1.57, "1,57")])},
        {"v": "Pilns apgrieziens", "teksts": "Nobrauca π ≈ 3,14",
         "zim": taisne(0, 4, 1, [(0, ""), (3.14, "π")])},
    ], ievads="Viens apgrieziens - riņķa līnijas garums."),

    Doma("Skaitlis π",
         "π ir riņķa līnijas garuma C un diametra d dalījums: π = {C|d}. No "
         "tā: C = πd = 2πr.",
         soli=[
             "π ≈ 3,14 vai π ≈ {22|7} ikdienas aprēķiniem.",
             "π = 3,14159265... - cipari nebeidzas un neatkārtojas.",
             "Precīzā atbilde satur π: C = 10π cm.",
             "Aptuvenā: C ≈ 31,4 cm.",
         ],
         pieze="Ar datoriem aprēķināti vairāk nekā 100 triljoni π ciparu, un "
               "neviena perioda tajos nav."),

    Paraugs("Riteņa apkārtmērs",
            uzd="Velosipēda riteņa diametrs 70 cm. Cik tālu tas aizripo vienā "
                "apgriezienā?",
            soli=[
                ("C = πd", "Formula."),
                ("C = 70π cm", "Precīzi."),
                ("C ≈ 3,14 · 70 = 219,8 cm", "Aptuveni."),
            ],
            atbilde="C = 70π cm ≈ 2,2 m"),

    Ievadi("Aprēķini (π ≈ 3,14)", [
        {"jaut": "d = 10 cm. C ≈ ? cm", "atb": ["31,4", "31.4"],
         "padoms": "3,14 · 10."},
        {"jaut": "r = 5 m. C ≈ ? m", "atb": ["31,4", "31.4"],
         "padoms": "2 · 3,14 · 5."},
        {"jaut": "C = 12π cm. d = ? cm", "atb": ["12"], "padoms": "C = πd."},
        {"jaut": "C = 18,84 m. d ≈ ? m", "atb": ["6"],
         "padoms": "18,84 : 3,14."},
        {"jaut": "{22|7} līdz simtdaļām", "atb": ["3,14", "3.14"],
         "padoms": "3,142..."},
        {"jaut": "Par cik {22|7} lielāks par 3,1416? (līdz "
                 "desmittūkstošdaļām)",
         "atb": ["0,0013", "0.0013"], "padoms": "3,1429 − 3,1416."},
    ], pamats=4),

    Petijums("Nomēri π pats",
             vajag="3 apaļi priekšmeti, diegs, lineāls",
             soli=[
                 "Aptin diegu apkārt priekšmetam un nomēri C.",
                 "Nomēri diametru d.",
                 "Aprēķini C : d līdz simtdaļām.",
                 "Atkārto ar citiem priekšmetiem.",
                 "Atrodi rezultātu vidējo.",
             ],
             secinajums="Visi rezultāti būs tuvu 3,1 - atšķirības rada "
                        "mērījuma kļūda, nevis priekšmets."),

    Varianti("Kurš apgalvojums pareizs?", [
        {"jaut": "π ir...",
         "opcijas": ["C : d jebkuram aplim", "tieši 3,14",
                     "tieši {22|7}", "atkarīgs no apļa lieluma"],
         "pareizi": 0, "padoms": "3,14 ir tikai tuvinājums."},
        {"jaut": "Ja diametrs divkāršojas, C...",
         "opcijas": ["divkāršojas", "četrkāršojas", "nemainās",
                     "palielinās par π"],
         "pareizi": 0, "padoms": "C = πd."},
    ]),

    Pasaule("Velosipēda spidometrs",
            Ievadi("", [
                {"jaut": "Ritenis d = 0,7 m. Cik m vienā apgriezienā? "
                         "(π ≈ 3,14, līdz simtdaļām)",
                 "atb": ["2,2", "2.2", "2,20"], "padoms": "3,14 · 0,7 = 2,198."},
                {"jaut": "Cik apgriezienu 1 km ceļā? (veseli)",
                 "atb": ["455", "454"], "padoms": "1000 : 2,198 ≈ 455."},
                {"jaut": "Ritenis griežas 3 apgriezienus sekundē. Cik m/s?",
                 "atb": ["6,6", "6.6", "6,59", "6.59"],
                 "padoms": "3 · 2,198."},
            ]),
            pavediens="sports",
            konteksts="Velodatoram ievada riteņa apkārtmēru - no tā un "
                      "apgriezienu skaita tas rēķina ātrumu un attālumu.",
            kapec="Nepareizs diametrs - nepareizs ātrums visu braucienu."),

    Kopsavilkums([
        "Zinu, ka π = {C|d} jebkuram aplim.",
        "Aprēķinu riņķa līnijas garumu precīzi un aptuveni.",
        "No garuma atrodu diametru.",
    ]),

    Majas([
        "Nomēri π ar 3 priekšmetiem un salīdzini ar 3,14.",
        "Aprēķini, cik apgriezienu izdara tavs velosipēda ritenis 1 km.",
        "Uzzini, kas ir «π diena» un kad to svin.",
    ]),
]
