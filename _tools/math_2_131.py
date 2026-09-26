# -*- coding: utf-8 -*-
"""2. klase, 131. stunda: «Kas rodas, saskaitot divus pāra skaitļus?»

Pētījums un likumsakarība: pāra + pāra = pāra, nepāra + nepāra = pāra,
pāra + nepāra = nepāra. Ar ripiņām pa pāriem redz, kāpēc: divi «lieki»
vieninieki kopā izveido pāri.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kas rodas, saskaitot divus pāra skaitļus?"

MERKIS = ("Šodien pētīsim un formulēsim likumsakarību par pāra un nepāra "
          "skaitļu summu.")

_LIKUMS = restis([["+", "pāra", "nepāra"],
                  ["pāra", "pāra", "nepāra"],
                  ["nepāra", "nepāra", "pāra"]])

_PARA = ["pāra", "nepāra"]

SATURS = [
    Sakums("Vai 7 + 9 var būt nepāra?",
           zimejums=_LIKUMS,
           paraksts="Summa atkarīga tikai no tā, vai saskaitāmie ir pāra.",
           fakti=["7 + 9 = 16 - pāra!",
                  "Divi nepāra kopā vienmēr dod pāra.",
                  "To var pārbaudīt ar ripiņām pa pāriem."]),

    Doma("Likumsakarība",
         "Pāra + pāra = pāra, nepāra + nepāra = pāra, pāra + nepāra = "
         "nepāra.",
         soli=[
             "Pāra skaitli var salikt pa pāriem bez atlikuma.",
             "Nepāra skaitlim paliek viens lieks.",
             "Divi lieki kopā - vēl viens pāris.",
             "Tāpēc nepāra + nepāra = pāra.",
         ]),

    Petijums("Pētī", [
        "Uzraksti 3 summas: pāra + pāra.",
        "Uzraksti 3 summas: nepāra + nepāra.",
        "Uzraksti 3 summas: pāra + nepāra.",
        "Kāda ir katra summa? Vai redzi likumu?",
    ], vajag="burtnīca", secinajums="Summa ir nepāra tikai tad, ja viens "
                                    "saskaitāmais ir pāra, otrs - nepāra."),

    Varianti("Nerēķinot - pāra vai nepāra?", [
        {"jaut": "24 + 36", "zim": _LIKUMS, "opcijas": _PARA,
         "jaukt": False, "pareizi": 0, "padoms": "Pāra + pāra."},
        {"jaut": "15 + 23", "zim": _LIKUMS, "opcijas": _PARA,
         "jaukt": False, "pareizi": 0, "padoms": "Nepāra + nepāra."},
        {"jaut": "42 + 17", "zim": _LIKUMS, "opcijas": _PARA,
         "jaukt": False, "pareizi": 1, "padoms": "Pāra + nepāra."},
        {"jaut": "39 + 40", "zim": _LIKUMS, "opcijas": _PARA,
         "jaukt": False, "pareizi": 1, "padoms": "Nepāra + pāra."},
    ]),

    Ievadi("Pārbaudi", [
        {"jaut": "15 + 23 = ?", "atb": ["38"], "padoms": "38 - pāra."},
        {"jaut": "42 + 17 = ?", "atb": ["59"], "padoms": "59 - nepāra."},
        {"jaut": "Kāds pāra skaitlis jāpieskaita 25, lai būtu 31?",
         "atb": ["6"], "padoms": "31 − 25."},
        {"jaut": "Kāds nepāra skaitlis jāpieskaita 27, lai būtu 40?",
         "atb": ["13"], "padoms": "40 − 27."},
    ]),

    Pasaule("Komandas pa pāriem",
            Varianti("", [
                {"jaut": "2.a klasē 13 bērni, 2.b - 11. Vai visi var "
                         "sadalīties pāros?",
                 "opcijas": ["Jā - 24 ir pāra", "Nē"], "jaukt": False,
                 "pareizi": 0, "padoms": "Nepāra + nepāra = pāra."},
                {"jaut": "Pievienojās vēl 1 bērns. Vai tagad var?",
                 "opcijas": ["Nē - 25 ir nepāra", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "Pāra + nepāra."},
            ]),
            pavediens="sports",
            konteksts="Dejās visi jāsadala pa pāriem.",
            kapec="Likumsakarība pasaka atbildi bez skaitīšanas."),

    Kopsavilkums([
        "Zinu, kad summa ir pāra un kad nepāra.",
        "Paskaidroju to ar pāriem.",
        "Pārbaudu likumu ar piemēriem.",
    ]),

    Majas([
        "Pārbaudi likumu ar 5 jauniem piemēriem.",
        "Vai kāds piemērs to lauza?",
        "Paskaidro mājiniekam, kāpēc nepāra + nepāra = pāra.",
    ]),
]
