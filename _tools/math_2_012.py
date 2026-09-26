# -*- coding: utf-8 -*-
"""2. klase, 12. stunda: «Kas ir milimetrs?»

Uz lineāla starp centimetru iedaļām ir sīkas iedaļas - milimetri. Vienā
centimetrā ir 10 milimetri, tāpēc garumu, kas neiznāk vesels centimetros,
var pierakstīt precīzi: 4 cm 5 mm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, lineals)

TEMA = "Kas ir milimetrs?"

MERKIS = ("Šodien mērīsim ar lineālu centimetros un milimetros un "
          "pierakstīsim rezultātu ar mērvienību.")

SATURS = [
    Sakums("Cik garš ir šis zīmulis, ja tas neiznāk vesels centimetros?",
           zimejums=lineals(10, [(0, 7.4, "zīmulis")], mm=True),
           paraksts="7 cm un vēl 4 sīkas iedaļas.",
           fakti=["Sīkās iedaļas ir milimetri.",
                  "1 cm = 10 mm.",
                  "Skudra ir apmēram 5 mm gara."]),

    Doma("Milimetrs ir desmitā daļa no centimetra",
         "Vienā centimetrā ir 10 milimetru: 1 cm = 10 mm.",
         soli=[
             "Noliec lineāla nulli pie priekšmeta sākuma.",
             "Nolasi, cik veselu centimetru ir līdz galam.",
             "Saskaiti sīkās iedaļas pēc pēdējā centimetra - tie ir mm.",
             "Pieraksti: 7 cm 4 mm.",
         ],
         pieze="Garākā sīkā iedaļa ir centimetra vidū - tur ir 5 mm."),

    Slidnis("Aug par milimetru", [
        {"v": "3 cm", "teksts": "Tieši 3 veseli centimetri.",
         "zim": lineals(6, [(0, 3, "")], mm=True)},
        {"v": "3 cm 2 mm", "teksts": "Vēl 2 sīkas iedaļas.",
         "zim": lineals(6, [(0, 3.2, "")], mm=True)},
        {"v": "3 cm 5 mm", "teksts": "Līdz garākajai sīkajai iedaļai.",
         "zim": lineals(6, [(0, 3.5, "")], mm=True)},
        {"v": "4 cm", "teksts": "10 mm - atkal vesels centimetrs.",
         "zim": lineals(6, [(0, 4, "")], mm=True)},
    ]),

    Ievadi("Nolasi garumu", [
        {"jaut": "Cik veselu centimetru garš ir nogrieznis?",
         "zim": lineals(8, [(0, 5.3, "")], mm=True), "atb": ["5"],
         "padoms": "Skaiti lielās iedaļas."},
        {"jaut": "Cik milimetru vēl ir pēc 5 cm?",
         "zim": lineals(8, [(0, 5.3, "")], mm=True), "atb": ["3"],
         "padoms": "Sīkās iedaļas aiz 5."},
        {"jaut": "Cik veselu centimetru?",
         "zim": lineals(8, [(0, 6.5, "")], mm=True), "atb": ["6"],
         "padoms": "Pēdējā lielā iedaļa pirms gala."},
        {"jaut": "Cik milimetru pēc veselajiem centimetriem?",
         "zim": lineals(8, [(0, 6.5, "")], mm=True), "atb": ["5"],
         "padoms": "Beidzas pie garākās sīkās iedaļas."},
        {"jaut": "Cik centimetru garš ir nogrieznis?",
         "zim": lineals(8, [(2, 6, "")], mm=True), "atb": ["4"],
         "padoms": "Tas nesākas pie 0: 6 − 2."},
        {"jaut": "Cik milimetru ir 2 cm?", "atb": ["20"],
         "padoms": "Katrā cm - 10 mm."},
    ], pamats=4),

    Varianti("Kurš pieraksts pareizs?", [
        {"jaut": "Nogrieznis ir 4 veseli cm un vēl 7 sīkas iedaļas.",
         "opcijas": ["4 cm 7 mm", "7 cm 4 mm", "47 cm"], "pareizi": 0,
         "padoms": "Vispirms cm, tad mm."},
        {"jaut": "Kas ir garāks?",
         "opcijas": ["1 cm", "9 mm"], "jaukt": False, "pareizi": 0,
         "padoms": "1 cm = 10 mm."},
    ]),

    Pasaule("Cik gara ir vabole?",
            Ievadi("", [
                {"jaut": "Mārīte ir 7 mm gara. Cik mm pietrūkst līdz 1 cm?",
                 "atb": ["3"], "padoms": "1 cm = 10 mm."},
                {"jaut": "Skudra ir 5 mm, mārīte 7 mm. Par cik mm mārīte ir "
                         "garāka?", "atb": ["2"], "padoms": "7 − 5."},
            ]),
            pavediens="daba",
            konteksts="Kukaiņi ir tik mazi, ka tos mēra milimetros.",
            kapec="Bez milimetriem visi kukaiņi būtu «apmēram 1 cm»."),

    Kopsavilkums([
        "Zinu, ka 1 cm = 10 mm.",
        "Mēru ar lineālu centimetros un milimetros.",
        "Pierakstu garumu: 7 cm 4 mm.",
    ]),

    Majas([
        "Izmēri ar lineālu 3 mazas lietas: dzēšgumiju, pogu, monētu.",
        "Pieraksti katru garumu cm un mm.",
        "Kura ir garākā?",
    ]),
]
