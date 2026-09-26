# -*- coding: utf-8 -*-
"""9. klase, 119. stunda: «Kā risināt uzdevumu par kustību?»

Kustības uzdevumi ar sistēmu: laiva pa straumi un pret straumi (v + u un
v − u), divi braucēji pretī viens otram, panākšana. Tabula «ātrums |
laiks | ceļš» katram braucienam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Kā risināt uzdevumu par kustību?"

MERKIS = "Risināsim uzdevumu par kustību, veidojot sistēmu."

SATURS = [
    Sakums("Laiva pa straumi - ātrāk, pret straumi - lēnāk",
           zimejums=restis([["", "ātrums", "laiks", "ceļš"],
                            ["pa straumi", "v + u", "2 h", "36 km"],
                            ["pret straumi", "v − u", "3 h", "36 km"]]),
           paraksts="v - laivas ātrums, u - straumes ātrums.",
           fakti=["2(v + u) = 36 ⇒ v + u = 18.",
                  "3(v − u) = 36 ⇒ v − u = 12.",
                  "v = 15 km/h, u = 3 km/h."]),

    Doma("Kustība sistēmā",
         "Katram braucienam: ceļš = ātrums · laiks; divi braucieni - divi "
         "vienādojumi.",
         soli=[
             "Nezināmie: parasti divi ātrumi (vai ātrums un laiks).",
             "Tabula ar rindu katram braucienam.",
             "s = v · t katrā rindā dod vienādojumu.",
             "Pretī - ātrumi saskaitās; vienā virzienā - atņemas.",
         ]),

    Paraugs("Divi velosipēdisti pretī",
            uzd="Starp ciemiem 60 km. Divi velosipēdisti izbrauc pretī viens "
                "otram un satiekas pēc 2 h. Ja pirmais brauktu 3 h, bet otrais "
                "1 h, kopā arī nobrauktu 60 km. Atrodi ātrumus.",
            soli=[
                ("2x + 2y = 60 ⇒ x + y = 30", "Pirmā situācija."),
                ("3x + y = 60", "Otrā situācija."),
                ("Atņem: 2x = 30 ⇒ x = 15; y = 15", "Atrisina."),
            ],
            atbilde="abi 15 km/h"),

    Kustiba("Laiva uz upes", [
        {"jaut": "Laiva pa straumi 24 km nobrauc 2 h, pret straumi - 3 h. "
                 "Laivas ātrums stāvošā ūdenī (km/h)?",
         "atb": 10, "beigas": 20, "iedala": 2, "mers": "km/h",
         "merkis": "v", "objekts": "Laiva",
         "padoms": "v + u = 12, v − u = 8."},
        {"jaut": "Straumes ātrums (km/h)?",
         "atb": 2, "beigas": 10, "iedala": 1, "mers": "km/h",
         "merkis": "u", "objekts": "Straume",
         "padoms": "12 − 10."},
    ]),

    Ievadi("Aprēķini", [
        {"jaut": "Divi auto no pilsētām 300 km attālumā satiekas pēc 2 h; "
                 "viens brauc par 10 km/h ātrāk. Ātrākā ātrums (km/h)?",
         "atb": ["80"], "padoms": "x + y = 150, x − y = 10."},
        {"jaut": "Lēnākā ātrums (km/h)?", "atb": ["70"], "padoms": "80 − 10."},
        {"jaut": "Motorlaiva pa straumi 20 km/h, pret straumi 14 km/h. "
                 "Straumes ātrums (km/h)?", "atb": ["3"],
         "padoms": "(20 − 14) : 2."},
    ]),

    Varianti("Pretī vai vienā virzienā?", [
        {"jaut": "Divi braucēji pretī viens otram ar 40 un 60 km/h. "
                 "Tuvošanās ātrums?",
         "opcijas": ["100 km/h", "20 km/h", "50 km/h", "2400 km/h"],
         "pareizi": 0, "padoms": "Saskaita."},
        {"jaut": "Viens panāk otru: 60 un 40 km/h vienā virzienā. "
                 "Tuvošanās ātrums?",
         "opcijas": ["20 km/h", "100 km/h", "50 km/h", "0"],
         "pareizi": 0, "padoms": "Atņem."},
    ]),

    Pasaule("Plostošana pa Gauju",
            Ievadi("", [
                {"jaut": "Laiva 18 km pa straumi nobrauc 3 h, bet atpakaļ - "
                         "6 h. Laivas ātrums (km/h)?", "atb": ["4,5"],
                 "padoms": "v + u = 6, v − u = 3."},
                {"jaut": "Gaujas straumes ātrums (km/h)?", "atb": ["1,5"],
                 "padoms": "6 − 4,5."},
            ]),
            pavediens="celojums",
            konteksts="Laivu nomas punkts iesaka maršrutu tikai pa straumi - "
                      "atpakaļ ceļš ir divreiz ilgāks.",
            kapec="Sistēma atdala laivas un upes ātrumu."),

    Kopsavilkums([
        "Sastādu tabulu ātrums - laiks - ceļš.",
        "Pierakstu sistēmu kustības uzdevumam.",
        "Lietoju v + u un v − u pa un pret straumi.",
    ]),

    Majas([
        "Laiva 30 km pa straumi 2 h, pret straumi 3 h. Atrodi ātrumus.",
        "Divi gājēji no 20 km attāluma satiekas pēc 2 h; viens iet par "
        "1 km/h ātrāk. Atrodi ātrumus.",
        "Izmēri savu iešanas ātrumu (km/h).",
    ]),
]
