# -*- coding: utf-8 -*-
"""1. klase, 35. stunda: «Cik ātri vari?»

Veiklības stunda: summas un starpības 10 apjomā. Ātrums nāk no zināmām
summām un gudra paņēmiena, nevis no skriešanas; tāpēc pēc katras sērijas
skolēns pastāsta, kā vienu no tām izrēķināja.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, ramis)

TEMA = "Cik ātri vari?"

MERKIS = ("Šodien veikli saskaitīsim un atņemsim 10 apjomā un "
          "pastāstīsim, kā to izdarījām.")

SATURS = [
    Sakums("Ātri un pareizi - kā?",
           zimejums=ramis(8, otra=3),
           paraksts="5 + 3 = 8: pilna rinda un vēl 3.",
           fakti=["Sāc ar lielāko.",
                  "Izmanto summas, ko zini.",
                  "Pārbaudi ar pretējo darbību."]),

    Doma("Ātrums no gudrības",
         "Ātrs ir tas, kurš izvēlas īsāko ceļu - nevis tas, kurš steidzas.",
         soli=[
             "Ja zini no galvas - saki uzreiz.",
             "Ja nē - skaiti no lielākā vai lieto dubulto.",
             "Pārbaudi: 8 − 3 = 5, jo 5 + 3 = 8.",
         ]),

    Ievadi("1. sērija: saskaiti", [
        {"jaut": "5 + 3", "atb": ["8"], "padoms": "No 5 trīs uz priekšu."},
        {"jaut": "2 + 7", "atb": ["9"], "padoms": "7 un 2."},
        {"jaut": "4 + 6", "atb": ["10"], "padoms": "Desmita draugi."},
        {"jaut": "3 + 4", "atb": ["7"], "padoms": "3 + 3 un vēl 1."},
        {"jaut": "6 + 2", "atb": ["8"], "padoms": "No 6: 7, 8."},
        {"jaut": "1 + 9", "atb": ["10"], "padoms": "9 un 1."},
    ], pamats=4),

    Ievadi("2. sērija: atņem", [
        {"jaut": "9 − 4", "atb": ["5"], "padoms": "4 + ? = 9."},
        {"jaut": "7 − 2", "atb": ["5"], "padoms": "Atpakaļ 2."},
        {"jaut": "10 − 7", "atb": ["3"], "padoms": "Desmita draugi."},
        {"jaut": "8 − 4", "atb": ["4"], "padoms": "4 + 4 = 8."},
        {"jaut": "6 − 5", "atb": ["1"], "padoms": "5 + 1 = 6."},
        {"jaut": "5 − 0", "atb": ["5"], "padoms": "Neko neatņem."},
    ], pamats=4),

    Varianti("Kā tu to izdarīji?", [
        {"jaut": "Kā ātri izrēķināt 9 − 8?",
         "opcijas": ["8 + 1 = 9, tātad 1", "skaitīt atpakaļ 8 soļus"],
         "jaukt": False, "pareizi": 0, "padoms": "Skaitļi ir blakus."},
        {"jaut": "Kā ātri izrēķināt 4 + 5?",
         "opcijas": ["4 + 4 un vēl 1", "skaitīt visus no 1"],
         "jaukt": False, "pareizi": 0, "padoms": "Dubultais palīdz."},
    ]),

    Pasaule("Kurš ātrāk?",
            Ievadi("", [
                {"jaut": "Sacensībās tu atrisināji 8 piemērus, 2 bija "
                         "nepareizi. Cik pareizi?", "atb": ["6"],
                 "padoms": "8 − 2."},
                {"jaut": "Draugam 7 pareizi. Par cik vairāk nekā tev?",
                 "atb": ["1"], "padoms": "7 − 6."},
            ]),
            pavediens="sports",
            konteksts="Klasē notiek piemēru sacensības pārī.",
            kapec="Svarīgi ir pareizi, ne tikai ātri."),

    Kopsavilkums([
        "Veikli saskaitu un atņemu 10 apjomā.",
        "Izvēlos ātrāko paņēmienu.",
        "Pastāstu, kā izrēķināju.",
    ]),

    Majas([
        "Katru dienu izrēķini 10 piemērus un pārbaudi.",
        "Izaicini mājinieku: kurš ātrāk?",
        "Pieraksti, kurš piemērs bija visgrūtākais.",
    ]),
]
