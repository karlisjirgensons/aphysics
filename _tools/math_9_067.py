# -*- coding: utf-8 -*-
"""9. klase, 67. stunda: «Kā atcerēties formulas?»

Trīs formulas vienā atgādnē un «atpazīšanas spēle»: pēc izteiksmes formas
nosaki, kura formula der. Tā ir tieši prasme, kas vajadzīga, lietojot
formulas otrā virzienā (sadalīšanai).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, binoma_kvadrats, restis)

TEMA = "Kā atcerēties formulas?"

MERKIS = ("Veidosim atgādni par formulām un pārbaudīsim tās ar piemēriem.")

_T = "text"

_ATGADNE = restis([["formula", "pazīme"],
                   ["(a + b)² = a² + 2ab + b²", "3 locekļi, visi +"],
                   ["(a − b)² = a² − 2ab + b²", "vidū −"],
                   ["a² − b² = (a − b)(a + b)", "2 kvadrāti ar −"]])

SATURS = [
    Sakums("Trīs formulas - viena lapa",
           zimejums=_ATGADNE,
           paraksts="Eksāmena formulu lapā tās ir - bet jāprot atpazīt.",
           fakti=["Binoma kvadrātā vienmēr 3 locekļi.",
                  "Kvadrātu starpībā - 2 locekļi un mīnuss.",
                  "Pārbaude: ievieto a = 2, b = 1."]),

    Slidnis("Laukuma atgādnes", [
        {"v": "(a + b)²", "teksts": "Liels kvadrāts no četrām daļām",
         "zim": binoma_kvadrats(izcelt="ab")},
        {"v": "(a − b)²", "teksts": "No a^2 atņem divas joslas un pieskaita "
                                    "b^2, ko atņēma divreiz",
         "zim": binoma_kvadrats(izcelt="a2")},
    ]),

    Doma("Atpazīšanas plāns",
         "Pirms atver vai sadali, pajautā: cik locekļu, kādas zīmes, vai ir "
         "kvadrāti?",
         soli=[
             "2 locekļi, abi kvadrāti, starp tiem − → kvadrātu starpība.",
             "3 locekļi, divi no tiem kvadrāti → varbūt binoma kvadrāts.",
             "Pārbaudi vidējo: vai tas ir 2 · a · b?",
             "Ja nekas neder - iznes kopīgo reizinātāju vai grupē.",
         ]),

    Varianti("Kura formula der?", [
        {"jaut": "x^2 − 81",
         "opcijas": ["Kvadrātu starpība", "Summas kvadrāts",
                     "Starpības kvadrāts", "Neviena"],
         "pareizi": 0, "padoms": "Divi kvadrāti ar −."},
        {"jaut": "x^2 + 10x + 25",
         "opcijas": ["Summas kvadrāts (x + 5)^2", "Kvadrātu starpība",
                     "Starpības kvadrāts", "Neviena"],
         "pareizi": 0, "padoms": "2 · x · 5 = 10x."},
        {"jaut": "a^2 − 6a + 9",
         "opcijas": ["Starpības kvadrāts (a − 3)^2", "Kvadrātu starpība",
                     "Summas kvadrāts", "Neviena"],
         "pareizi": 0, "padoms": "Vidū −6a = −2 · a · 3."},
        {"jaut": "x^2 + 5x + 25",
         "opcijas": ["Neviena - vidējam jābūt 10x", "Summas kvadrāts",
                     "Kvadrātu starpība", "Starpības kvadrāts"],
         "pareizi": 0, "padoms": "2 · x · 5 ≠ 5x."},
        {"jaut": "4m^2 − 9n^2",
         "opcijas": ["Kvadrātu starpība", "Starpības kvadrāts",
                     "Summas kvadrāts", "Neviena"],
         "pareizi": 0, "padoms": "(2m)^2 − (3n)^2."},
    ], pamats=3),

    Ievadi("Pārbaudi ar a = 2, b = 1", [
        {"jaut": "(a + b)^2 = ?", "atb": ["9"], "padoms": "3^2."},
        {"jaut": "a^2 + 2ab + b^2 = ?", "atb": ["9"], "padoms": "4 + 4 + 1."},
        {"jaut": "(a − b)^2 = ?", "atb": ["1"], "padoms": "1^2."},
        {"jaut": "a^2 − b^2 = ?", "atb": ["3"], "padoms": "4 − 1 = 1 · 3."},
    ]),

    Pasaule("Formulu kārtis",
            Varianti("", [
                {"jaut": "Kārts: «(m − 7)^2». Kura otrā kārts ir tās pāris?",
                 "opcijas": ["m^2 − 14m + 49", "m^2 − 49", "m^2 + 49",
                             "m^2 − 7m + 49"],
                 "pareizi": 0, "padoms": "2 · 7m = 14m."},
                {"jaut": "Kārts: «x^2 − 1». Pāris?",
                 "opcijas": ["(x − 1)(x + 1)", "(x − 1)^2", "(x + 1)^2",
                             "x(x − 1)"],
                 "pareizi": 0, "padoms": "Kvadrātu starpība."},
            ]),
            pavediens="speles",
            konteksts="Spēle «Atrodi pāri»: uz kārtīm izteiksmes, jāsaliek "
                      "vienādās pa pāriem.",
            kapec="Atpazīšana spēlē kļūst automātiska."),

    Kopsavilkums([
        "Zinu trīs saīsinātās reizināšanas formulas.",
        "Atpazīstu formulu pēc locekļu skaita un zīmēm.",
        "Pārbaudu formulu ar skaitļiem.",
    ]),

    Majas([
        "Izgatavo 10 pāru kārtis «Atrodi pāri» un izspēlē.",
        "Uzraksti atgādni no atmiņas.",
        "Atrodi, kurām izteiksmēm formula neder: x^2 + 4; x^2 − 4x + 4.",
    ]),
]
