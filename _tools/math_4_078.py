# -*- coding: utf-8 -*-
"""4. klase, 78. stunda: «Kurš paņēmiens man ērtāks?»

Trīs ceļi vienam reizinājumam - pa daļām, logs, stabiņš - un vēl «triki»
(25 · 48 = 100 · 12, 99 · 34 = 3400 − 34). Skolēns izvēlas un pamato:
ne katram reizinājumam vajag stabiņu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kurš paņēmiens man ērtāks?"

MERKIS = ("Izvēlēsimies piemērotāko reizināšanas paņēmienu un pierakstu un "
          "pamatosim izvēli.")

SATURS = [
    Sakums("Kā ātrāk: 25 · 48?",
           zimejums=restis([["paņēmiens", "25 · 48"],
                            ["stabiņš", "200 + 1000 = 1200"],
                            ["logs", "800 + 200 + 160 + 40"],
                            ["triks", "25 · 4 · 12 = 1200"]],
                           "trīs ceļi"),
           paraksts="Triks: 48 = 4 · 12, un 25 · 4 = 100.",
           fakti=["Stabiņš der vienmēr, bet ne vienmēr ir ātrākais.",
                  "Paskaties uz skaitļiem, pirms sāc."]),

    Doma("Vispirms paskaties, tad izvēlies",
         "Izvēlies paņēmienu pēc skaitļiem: apaļi un «draudzīgi» - triks; "
         "neērti - stabiņš vai logs.",
         soli=[
             "Tuvu apaļam (99, 101)? - (100 − 1) · a.",
             "Ir 25 vai 5 un pāra skaitlis? - draudzīgais pāris.",
             "Mazi desmiti (12, 21)? - pa daļām galvā.",
             "Citādi - stabiņš ar novērtējumu.",
         ],
         pieze="Labs matemātiķis nav tas, kurš rēķina ātri, bet kurš izvēlas "
               "gudri."),

    Varianti("Kurš paņēmiens ērtākais?", [
        {"jaut": "99 · 34",
         "opcijas": ["3400 − 34", "stabiņš", "logs"], "pareizi": 0,
         "padoms": "99 = 100 − 1."},
        {"jaut": "25 · 36",
         "opcijas": ["25 · 4 · 9", "stabiņš", "logs"], "pareizi": 0,
         "padoms": "36 = 4 · 9."},
        {"jaut": "67 · 83",
         "opcijas": ["stabiņš", "triks ar 100", "draudzīgais pāris"],
         "pareizi": 0, "padoms": "Nekas «draudzīgs» te nav."},
        {"jaut": "12 · 11",
         "opcijas": ["120 + 12 galvā", "stabiņš", "kalkulators"],
         "pareizi": 0, "padoms": "12 · 10 + 12."},
    ], pamats=4),

    Ievadi("Izvēlies un izrēķini", [
        {"jaut": "99 · 34 = ?", "atb": ["3366"], "padoms": "3400 − 34."},
        {"jaut": "25 · 36 = ?", "atb": ["900"], "padoms": "100 · 9."},
        {"jaut": "67 · 83 = ?", "atb": ["5561"], "padoms": "201 + 5360."},
        {"jaut": "12 · 11 = ?", "atb": ["132"], "padoms": "120 + 12."},
        {"jaut": "50 · 86 = ?", "atb": ["4300"], "padoms": "8600 : 2."},
        {"jaut": "101 · 45 = ?", "atb": ["4545"], "padoms": "4500 + 45."},
    ], pamats=4),

    Pasaule("Ātrrēķinu turnīrs",
            Ievadi("", [
                {"jaut": "1. kārta: 25 · 44 = ?", "atb": ["1100"],
                 "padoms": "25 · 4 · 11."},
                {"jaut": "2. kārta: 98 · 15 = ?", "atb": ["1470"],
                 "padoms": "1500 − 30."},
                {"jaut": "3. kārta: 21 · 31 = ?", "atb": ["651"],
                 "padoms": "620 + 31."},
                {"jaut": "Fināls: 48 · 52 = ?", "atb": ["2496"],
                 "padoms": "2400 + 96."},
            ]),
            pavediens="skola",
            konteksts="Galvas rēķinu sacensībās uzvar tas, kurš izvēlas "
                      "īsāko ceļu, nevis rēķina visātrāk.",
            kapec="Gudra izvēle ietaupa vairāk laika nekā ātri pirksti."),

    Kopsavilkums([
        "Zinu vairākus reizināšanas paņēmienus.",
        "Izvēlos paņēmienu pēc skaitļiem.",
        "Pamatoju savu izvēli.",
    ]),

    Majas([
        "Sarīko mājās ātrrēķinu turnīru ar 5 reizinājumiem.",
        "Atrodi reizinājumu, kuram der triks ar 100.",
        "Pastāsti, kurš paņēmiens tev patīk visvairāk un kāpēc.",
    ]),
]
