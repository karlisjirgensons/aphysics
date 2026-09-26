# -*- coding: utf-8 -*-
"""1. klase, 54. stunda: «Kā saskaitīt daudz priekšmetu, nesajaucoties?»

Daudzus priekšmetus grupē pa 10: pilnos desmitus saskaita ātri, pārējos -
pa vienam. 3 pilni desmiti un vēl 4 ir 34. Tā nesajūk, un var pārbaudīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, bildes, desmiti)

TEMA = "Kā saskaitīt daudz priekšmetu, nesajaucoties?"

MERKIS = ("Šodien grupēsim priekšmetus pa 10 un pateiksim, cik ir pilnu "
          "desmitu un cik vēl vienu.")

SATURS = [
    Sakums("Kā ātri saskaitīt 34 zīmuļus?",
           zimejums=desmiti(3, 4),
           paraksts="3 pilni desmiti un vēl 4 vieni - 34.",
           fakti=["Liec pa 10 kopā - tas ir viens desmits.",
                  "Saskaiti desmitus: 10, 20, 30.",
                  "Pieskaiti atlikušos vienus."]),

    Slidnis("Grupējam pa 10", [
        {"v": "10", "teksts": "Viens pilns desmits", "zim": desmiti(1, 0)},
        {"v": "20", "teksts": "Divi desmiti", "zim": desmiti(2, 0)},
        {"v": "23", "teksts": "Divi desmiti un 3 vieni",
         "zim": desmiti(2, 3)},
        {"v": "34", "teksts": "Trīs desmiti un 4 vieni",
         "zim": desmiti(3, 4)},
    ]),

    Doma("Desmiti un vieni",
         "Pilnos desmitus skaita pa 10, atlikušos - pa vienam.",
         soli=[
             "Saliec priekšmetus kaudzītēs pa 10.",
             "Skaiti kaudzītes: 10, 20, 30...",
             "Pieskaiti tos, kas nav kaudzītē.",
         ]),

    Ievadi("Cik ir?", [
        {"jaut": "Cik kubiņu?", "zim": desmiti(2, 5), "atb": ["25"],
         "padoms": "2 desmiti un 5."},
        {"jaut": "Cik kubiņu?", "zim": desmiti(4, 1), "atb": ["41"],
         "padoms": "4 desmiti un 1."},
        {"jaut": "Cik kubiņu?", "zim": desmiti(1, 7), "atb": ["17"],
         "padoms": "1 desmits un 7."},
        {"jaut": "Cik pilnu desmitu ir 38 kubiņos?", "zim": desmiti(3, 8),
         "atb": ["3"], "padoms": "Saskaiti stieņus."},
        {"jaut": "Cik kubiņu?", "zim": desmiti(5, 0), "atb": ["50"],
         "padoms": "5 desmiti."},
        {"jaut": "Cik vienu nav desmitā 26 kubiņos?", "zim": desmiti(2, 6),
         "atb": ["6"], "padoms": "Atsevišķie kubiņi."},
    ], pamats=4),

    Petijums("Saskaiti klasē", [
        "Paņem kasti ar kociņiem vai makaroniem.",
        "Sasien vai saliec tos pa 10.",
        "Saskaiti desmitus un vienus.",
        "Pieraksti skaitli.",
    ], vajag="kociņi vai makaroni, gumijas"),

    Pasaule("Olas fermā",
            Ievadi("", [
                {"jaut": "Fermā olas liek kastēs pa 10. Ir 4 pilnas kastes un "
                         "vēl 3 olas. Cik olu?", "atb": ["43"],
                 "padoms": "40 un 3."},
                {"jaut": "Cik pilnas kastes var piepildīt ar 27 olām?",
                 "atb": ["2"], "padoms": "20 olas - 2 kastes."},
            ]),
            pavediens="daba",
            konteksts="Fermā olas skaita pa kastēm, nevis pa vienai.",
            kapec="Pa 10 ir ātrāk un nesajūk."),

    Kopsavilkums([
        "Grupēju priekšmetus pa 10.",
        "Nosaku, cik ir desmitu un cik vienu.",
        "Saskaitu daudz priekšmetu, nesajaucoties.",
    ]),

    Majas([
        "Saskaiti pogas, grupējot pa 10.",
        "Saskaiti grāmatas plauktā pa 10.",
        "Pieraksti: cik desmitu, cik vienu.",
    ]),
]
