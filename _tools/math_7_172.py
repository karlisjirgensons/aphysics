# -*- coding: utf-8 -*-
"""7. klase, 172. stunda: «Ko gaida 8. klasē?»

Gada pēdējā stunda. Atskats uz 7. klasi un tilti uz 8. klasi: katram
nākamā gada tematam ir šī gada pamats. Stunda beidzas ar pašvērtējumu, ne ar
pārbaudi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, geometrija,
                         plakne, restis)

TEMA = "Ko gaida 8. klasē?"

MERKIS = ("Apkoposim 7. klasē apgūto un ieskatīsimies, kas gaida nākamajā "
          "klasē.")

_TAISNE_UN_PARABOLA = plakne(
    grafiki=[(1, 0, "y = x"),
             ([(x / 4.0, x * x / 16.0) for x in range(-8, 9)], "y = x²")],
    no_x=-3, lidz_x=3, no_y=-2, lidz_y=5, solis=1)

_PITAGORS = geometrija([("A", 0, 0), ("B", 4, 0), ("C", 0, 3)],
                       nogriezni=["AB", "BC", "CA"], taisni=["BAC"],
                       malas=[("AB", "4"), ("CA", "3"), ("BC", "?")])

SATURS = [
    Sakums("Katram jaunajam tematam jau ir pamats",
           zimejums=restis([["7. klasē", "8. klasē"],
                            ["y = kx + b", "y = x²"],
                            ["trijstūra leņķi", "Pitagora teorēma"],
                            ["2x + 3x", "(x + 2)(x + 3)"]]),
           paraksts="Pa kreisi - tas, ko jau proti; pa labi - kas no tā "
                    "izaugs.",
           fakti=["Iekavu atvēršana paliek tā pati.",
                  "Grafiku lasa tāpat - tikai tas kļūst liekts.",
                  "Pierādījums joprojām ir divās kolonnās."]),

    Doma("Kas paliek, kas nāk klāt",
         "Astotā klase neko neizmet - tā uz šī gada pamata būvē nākamo "
         "stāvu. Tāpēc tieši nedrošās vietas ir vērts atkārtot vasarā.",
         soli=[
             "Kopas un varbūtība - pamats statistikai.",
             "Izteiksmes ar mainīgo - pamats polinomiem.",
             "Lineārā funkcija - pamats kvadrātfunkcijai.",
             "Trijstūri - pamats četrstūriem un Pitagora teorēmai.",
             "Vienādojumi - rīks visiem tematiem.",
         ]),

    Slidnis("Tilti uz 8. klasi", [
        {"v": "Funkcijas", "teksts": "Taisne y = x un parabola y = x²",
         "zim": _TAISNE_UN_PARABOLA},
        {"v": "Pitagora teorēma",
         "teksts": "3² + 4² = 5², tāpēc BC = 5", "zim": _PITAGORS},
        {"v": "Polinomi",
         "teksts": "(x + 2)(x + 3) = x² + 5x + 6 - katrs ar katru"},
        {"v": "Pakāpes", "teksts": "2³ = 8, un 8. klasē arī 2⁻¹ = {1|2}"},
        {"v": "Statistika",
         "teksts": "No kopām un varbūtības - vidējais un mediāna"},
    ], ievads="Katrs solis - viens nākamā gada temats."),

    Ievadi("Pārbaudi visu gadu", [
        {"jaut": "A = {1; 2; 3; 4}, B = {3; 4; 5}. Cik elementu ir "
                 "A ∪ B?",
         "atb": ["5"], "padoms": "1; 2; 3; 4; 5."},
        {"jaut": "Met kauliņu. Kāda ir varbūtība uzmest pāra skaitli?",
         "atb": ["{1|2}", "1/2", "0,5", "0.5", "3/6"],
         "padoms": "2; 4; 6 no sešiem."},
        {"jaut": "Taisnleņķa trijstūrī viens šaurais leņķis ir 35°. Cik "
                 "grādu ir otrs?",
         "atb": ["55", "55°"], "padoms": "90 − 35."},
        {"jaut": "Vienkāršo 2(x + 3) − x",
         "atb": ["x + 6", "x+6", "6+x"], "padoms": "2x + 6 − x.",
         "tastatura": "text"},
        {"jaut": "5x − 3 = 2x + 9. x = ?",
         "atb": ["4"], "padoms": "3x = 12."},
        {"jaut": "2x − 1 < 7. Kāds ir lielākais veselais x?",
         "atb": ["3"], "padoms": "x < 4."},
        {"jaut": "y = 2x − 3. Kāds ir y, ja x = 5?",
         "atb": ["7"], "padoms": "10 − 3."},
    ], pamats=5,
        ievads="Septiņi uzdevumi no septiņiem gada tematiem."),

    Ievadi("Ieskats 8. klasē", [
        {"jaut": "Cik ir 3² + 4²?",
         "atb": ["25"], "padoms": "9 + 16."},
        {"jaut": "Kurš pozitīvs skaitlis kvadrātā ir 25?",
         "atb": ["5"], "padoms": "5 · 5."},
        {"jaut": "y = x². Kāds ir y, ja x = −3?",
         "atb": ["9"], "padoms": "(−3) · (−3)."},
        {"jaut": "Cik ir 2³?",
         "atb": ["8"], "padoms": "2 · 2 · 2."},
    ], ievads="Šos rēķinus jau proti - 8. klasē tie kļūs par jauniem "
              "likumiem."),

    Varianti("Kas nāks klāt?", [
        {"jaut": "Kura 7. klases prasme vajadzīga Pitagora teorēmai?",
         "opcijas": ["Taisnleņķa trijstūra malas", "Kopu šķēlums",
                     "Nevienādību sistēma", "Varbūtība"],
         "pareizi": 0, "padoms": "Teorēma ir par katetēm un hipotenūzu."},
        {"jaut": "Ar ko parabola y = x² atšķiras no taisnes?",
         "opcijas": ["Tā ir liekta", "Tā neiet caur (0; 0)",
                     "Tai nav grafika", "Tā vienmēr dilst"],
         "pareizi": 0, "padoms": "Salīdzini slīdnī."},
        {"jaut": "Kas paliks tas pats, reizinot polinomus?",
         "opcijas": ["Iekavu atvēršana", "Leņķu summa",
                     "Varbūtības formula", "Intervāla pieraksts"],
         "pareizi": 0, "padoms": "Katrs loceklis ar katru."},
    ]),

    Pasaule("Cik auksts ir lidmašīnas aiz loga?",
            Ievadi("", [
                {"jaut": "Pie zemes ir 13 °C, un katrā kilometrā uz augšu "
                         "gaiss atdziest par 6,5 °C. Cik grādu ir 4 km "
                         "augstumā?",
                 "atb": ["−13", "-13"], "padoms": "13 − 6,5 · 4."},
                {"jaut": "Kurā augstumā (km) ir 0 °C?",
                 "atb": ["2"], "padoms": "13 − 6,5h = 0."},
                {"jaut": "Lidmašīna lido 10 km augstumā. Cik grādu tur ir?",
                 "atb": ["−52", "-52"], "padoms": "13 − 65."},
            ]),
            pavediens="planeta",
            konteksts="Temperatūra atkarībā no augstuma ir lineāra funkcija "
                      "t = 13 − 6,5h: te satiekas funkcija, vienādojums un "
                      "negatīvi skaitļi.",
            kapec="Viss gads vienā uzdevumā - tā matemātika strādā arī "
                  "8. klasē."),

    Petijums("Uzraksti vēstuli sev",
             vajag="burtnīca",
             soli=[
                 "Pieraksti trīs lietas, ko šogad iemācījies vislabāk.",
                 "Pieraksti divas, kuras vēl ir nedrošas.",
                 "Katrai nedrošajai pieraksti vienu uzdevumu, ko atkārtot.",
                 "Pieraksti, kurš 8. klases temats tev šķiet "
                 "interesantākais.",
                 "Ieliec lapu burtnīcā un izlasi to septembrī.",
             ],
             secinajums="Vasarā pirmās aizmirstas tās vietas, kas jau maijā "
                        "bija nedrošas - tāpēc tās ir vērts pierakstīt."),

    Kopsavilkums([
        "Apkopoju, ko esmu iemācījies 7. klasē.",
        "Zinu, kuras vietas man vēl jāatkārto.",
        "Redzu, kā šī gada tēmas turpināsies 8. klasē.",
    ]),

    Majas([
        "Pieraksti trīs lietas, ko šogad iemācījies vislabāk.",
        "Vasarā atrisini pa vienam uzdevumam no katra nedrošā temata.",
        "Atrodi dzīvē vienu lineāru sakarību un uzzīmē tās grafiku.",
    ]),
]
