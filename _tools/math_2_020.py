# -*- coding: utf-8 -*-
"""2. klase, 20. stunda: «Cik tālu aizlēci?»

Tāllēkšanā garumu mēra no atspēriena līnijas līdz tuvākajai pēdai smiltīs,
un rezultātu raksta metros un centimetros. Salīdzināšana - par cik viens
lēciens garāks - ir atņemšana tajā pašā mērvienībā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Cik tālu aizlēci?"

MERKIS = ("Šodien mērīsim un pierakstīsim tāllēkšanas rezultātus un "
          "noskaidrosim, par cik viens rezultāts lielāks nekā otrs.")

_REZ = restis([["vārds", "1. lēciens", "2. lēciens"],
               ["Elza", "1 m 12 cm", "1 m 20 cm"],
               ["Jānis", "1 m 25 cm", "1 m 19 cm"],
               ["Rūta", "98 cm", "1 m 5 cm"]])

SATURS = [
    Sakums("Pasaules rekords tāllēkšanā ir gandrīz 9 metri. Cik tālu vari "
           "tu?",
           zimejums=_REZ,
           paraksts="Katram ir divi mēģinājumi, skaitās labākais.",
           fakti=["Mēra no līnijas līdz tuvākajai pēdai smiltīs.",
                  "Rezultātu raksta metros un centimetros.",
                  "1 m 20 cm ir 1 metrs un vēl 20 centimetri."]),

    Doma("Salīdzina vienādās vienībās",
         "Ja abiem lēcieniem ir 1 m, salīdzina tikai centimetrus.",
         soli=[
             "Pieraksti abus rezultātus: 1 m 25 cm un 1 m 19 cm.",
             "Metri sakrīt - salīdzini centimetrus: 25 un 19.",
             "Starpība: 25 − 19 = 6.",
             "Pirmais lēciens ir par 6 cm garāks.",
         ],
         pieze="1 m 5 cm ir 105 cm - tas ir vairāk nekā 98 cm."),

    Kustiba("Aizlec līdz karodziņam", [
        {"jaut": "Elzas lēciens: 1 m 20 cm. Cik cm aiz metra atzīmes ir "
                 "pēda?", "atb": 20, "beigas": 50, "iedala": 10, "mers": "cm",
         "objekts": "pēda", "merkis": "Elza", "padoms": "Nolasi cm daļu."},
        {"jaut": "Jānis lēca par 5 cm tālāk nekā Elza. Cik cm aiz metra "
                 "atzīmes?", "atb": 25, "beigas": 50, "iedala": 10,
         "mers": "cm", "objekts": "pēda", "merkis": "Jānis",
         "padoms": "20 + 5."},
        {"jaut": "Rūtas lēciens ir 1 m 5 cm. Cik cm aiz metra?", "atb": 5,
         "beigas": 50, "iedala": 10, "mers": "cm", "objekts": "pēda",
         "merkis": "Rūta", "padoms": "5 cm pēc metra."},
    ], ievads="Trase sākas pie 1 m atzīmes. Ieraksti centimetrus un spied "
              "«Palaist»."),

    Ievadi("Par cik?", [
        {"jaut": "Par cik cm Elzas 2. lēciens bija garāks nekā 1.?",
         "zim": _REZ, "atb": ["8"], "mers": "cm", "padoms": "20 − 12."},
        {"jaut": "Par cik cm Jāņa 1. lēciens bija garāks nekā 2.?",
         "zim": _REZ, "atb": ["6"], "mers": "cm", "padoms": "25 − 19."},
        {"jaut": "Rūtas 2. lēciens ir 1 m 5 cm. Cik tas ir cm?",
         "zim": _REZ, "atb": ["105"], "mers": "cm", "padoms": "100 + 5."},
        {"jaut": "Par cik cm Rūtas 2. lēciens garāks nekā 1.?",
         "zim": _REZ, "atb": ["7"], "mers": "cm",
         "padoms": "No 98 līdz 100 ir 2, vēl 5."},
    ]),

    Varianti("Kurš uzvar?", [
        {"jaut": "Kuram ir labākais rezultāts?", "zim": _REZ,
         "opcijas": ["Jānim", "Elzai", "Rūtai"], "pareizi": 0,
         "padoms": "1 m 25 cm ir vairāk nekā 1 m 20 cm."},
        {"jaut": "Kas ieņem 2. vietu?", "zim": _REZ,
         "opcijas": ["Elza", "Rūta", "Jānis"], "pareizi": 0,
         "padoms": "Salīdzini katra labāko lēcienu."},
    ]),

    Pasaule("Klases sacensības",
            Ievadi("", [
                {"jaut": "Tavs lēciens 1 m 16 cm, rekords 1 m 30 cm. Cik cm "
                         "pietrūka līdz rekordam?", "atb": ["14"],
                 "mers": "cm", "padoms": "30 − 16."},
                {"jaut": "Nākamgad tu lēksi par 10 cm tālāk. Cik cm aiz 1 m "
                         "būs pēda?", "atb": ["26"], "mers": "cm",
                 "padoms": "16 + 10."},
            ]),
            pavediens="sports",
            konteksts="Klases rekords tāllēkšanā ir 1 m 30 cm.",
            kapec="Sportisti uzvar un zaudē par dažiem centimetriem."),

    Kopsavilkums([
        "Pierakstu rezultātu metros un centimetros.",
        "Salīdzinu lēcienus un atrodu starpību.",
        "Nosaku labāko rezultātu.",
    ]),

    Majas([
        "Pagalmā atzīmē līniju un aizlec no tās.",
        "Ar mērlenti izmēri lēcienu.",
        "Aizlec vēlreiz. Par cik cm otrs lēciens atšķīrās?",
    ]),
]
