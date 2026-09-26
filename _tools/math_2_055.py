# -*- coding: utf-8 -*-
"""2. klase, 55. stunda: «Cik ir pulkstenis - līdz minūtei?»

1. klasē laiku lasīja pa stundām un pusstundām; tagad - līdz minūtei. Lielā
rādītāja katra lielā iedaļa ir 5 minūtes, starp tām - pa vienai minūtei.
Digitālajā pulkstenī tas pats laiks ir uzrakstīts: 8:23.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, laiks, pulkstenis)

TEMA = "Cik ir pulkstenis - līdz minūtei?"

MERKIS = ("Šodien nolasīsim un pierakstīsim laiku no analogā un digitālā "
          "pulksteņa ar precizitāti līdz minūtei.")

SATURS = [
    Sakums("Vilciens atiet 8:23. Vai paspēsi, ja pulkstenis rāda šo?",
           zimejums=pulkstenis(8, 20),
           paraksts="8:20 - vēl 3 minūtes!",
           fakti=["Vilcieni un autobusi kursē precīzi līdz minūtei.",
                  "Lielā iedaļa - 5 minūtes, mazā - 1 minūte.",
                  "Digitālais pulkstenis raksta 8:20."]),

    Doma("Laiks līdz minūtei",
         "Mazais rādītājs - stundas, lielais - minūtes.",
         soli=[
             "Nolasi stundu pēc mazā rādītāja.",
             "Lielajam rādītājam skaiti pa 5: pie 1 - 5 min, pie 2 - 10 min.",
             "Tad pieskaiti mazās iedaļas pa 1 minūtei.",
             "Pieraksti: 8:23 - stunda, kols, minūtes ar diviem cipariem.",
         ],
         pieze="8:05 raksta ar nulli: minūtēm vienmēr ir divi cipari."),

    Slidnis("Lielais rādītājs iet", [
        {"v": "3:05", "teksts": "Pie 1 - 5 minūtes.",
         "zim": pulkstenis(3, 5)},
        {"v": "3:15", "teksts": "Pie 3 - 15 minūtes.",
         "zim": pulkstenis(3, 15)},
        {"v": "3:17", "teksts": "Vēl 2 mazās iedaļas.",
         "zim": pulkstenis(3, 17)},
        {"v": "3:40", "teksts": "Pie 8 - 40 minūtes.",
         "zim": pulkstenis(3, 40)},
    ]),

    Ievadi("Cik ir pulkstenis?", [
        {"jaut": "Raksti laiku, piemēram 4:10.", "zim": pulkstenis(4, 10),
         "atb": laiks(4, 10), "padoms": "Lielais pie 2."},
        {"jaut": "Raksti laiku.", "zim": pulkstenis(7, 25),
         "atb": laiks(7, 25), "padoms": "Lielais pie 5."},
        {"jaut": "Raksti laiku.", "zim": pulkstenis(11, 50),
         "atb": laiks(11, 50), "padoms": "Lielais pie 10."},
        {"jaut": "Raksti laiku.", "zim": pulkstenis(2, 5),
         "atb": laiks(2, 5), "padoms": "Minūtes ar nulli: 05."},
        {"jaut": "Raksti laiku.", "zim": pulkstenis(9, 37),
         "atb": laiks(9, 37), "padoms": "35 un vēl 2."},
        {"jaut": "Raksti laiku.", "zim": pulkstenis(6, 13),
         "atb": laiks(6, 13), "padoms": "10 un vēl 3."},
    ], pamats=4),

    Varianti("Kurš pulkstenis?", [
        {"jaut": "Vai pulkstenis rāda 5:45?", "zim": pulkstenis(5, 45),
         "opcijas": ["Jā", "Nē"], "jaukt": False,
         "pareizi": 0, "padoms": "Lielais pie 9 - 45 minūtes."},
        {"jaut": "Kā pierakstīt «septiņas minūtes pāri desmitiem»?",
         "opcijas": ["10:07", "10:70", "7:10"], "pareizi": 0,
         "padoms": "Minūtēm divi cipari: 07."},
    ]),

    Pasaule("Vilciena saraksts",
            Ievadi("", [
                {"jaut": "Vilciens atiet 8:23. Pulkstenis rāda šo laiku. "
                         "Cik minūtes vēl?", "zim": pulkstenis(8, 16),
                 "atb": ["7"], "padoms": "No 16 līdz 23."},
                {"jaut": "Nākamais vilciens atiet pēc 30 minūtēm - 8:53. "
                         "Cik minūšu no 8:23?", "atb": ["30"],
                 "padoms": "53 − 23."},
            ]),
            pavediens="celojums",
            konteksts="Stacijā vilciens negaida - tas atiet precīzi.",
            kapec="Minūtes ir svarīgas, ja kaut kas notiek pēc saraksta."),

    Kopsavilkums([
        "Nolasu laiku līdz minūtei no pulksteņa ar rādītājiem.",
        "Pierakstu laiku ar kolu: 8:23.",
        "Minūtes rakstu ar diviem cipariem.",
    ]),

    Majas([
        "Piecas reizes dienā nolasi laiku no pulksteņa ar rādītājiem.",
        "Pieraksti katru laiku līdz minūtei.",
        "Pārbaudi ar telefona pulksteni.",
    ]),
]
