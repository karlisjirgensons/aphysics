# -*- coding: utf-8 -*-
"""8. klase, 57. stunda: «Kā izvilkt sakni no reizinājuma?»

√(ab) = √a · √b, ja a un b nav negatīvi. Īpašība strādā abos virzienos:
lielu zemsaknes skaitli sadala pilnos kvadrātos, bet divas saknes
apvieno zem vienas. Summai tā nav - to parāda √(9 + 16).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā izvilkt sakni no reizinājuma?"

MERKIS = ("Lietosim reizinājuma saknes īpašību izteiksmju "
          "pārveidojumos.")

SATURS = [
    Sakums("√(4 · 9) - kā rēķināt?",
           zimejums=restis([["4 · 9 = 36", "√36", "6"],
                            ["√4 · √9", "2 · 3", "6"]]),
           paraksts="Abi ceļi dod vienu un to pašu rezultātu.",
           fakti=["√(ab) = √a · √b, ja a ≥ 0 un b ≥ 0.",
                  "Sakni no reizinājuma var vilkt pa daļām.",
                  "Otrādi arī der: √2 · √8 = √16 = 4."]),

    Doma("Reizinājuma sakne",
         "Reizinājuma sakne ir reizinātāju sakņu reizinājums.",
         soli=[
             "Sadali zemsaknes skaitli pilnos kvadrātos: √(16 · 25) = 4 · 5 = "
             "20.",
             "Reizinot saknes, apvieno tās zem vienas: √3 · √12 = √36 = 6.",
             "Pārbaudi, vai zem saknes nav summas.",
         ],
         pieze="Summai īpašība neder: √(9 + 16) = √25 = 5, bet √9 + √16 = 7."),

    Paraugs("Pa daļām un kopā",
            uzd="Aprēķini √(0,49 · 144) un √2 · √32.",
            soli=[
                ("√(0,49 · 144) = √(0,49) · √144", "Katram reizinātājam sava "
                                                   "sakne."),
                ("= 0,7 · 12 = 8,4", "Abi ir pilni kvadrāti."),
                ("√2 · √32 = √64 = 8", "Apvieno zem vienas saknes."),
            ],
            atbilde="8,4 un 8"),

    Ievadi("Aprēķini", [
        {"jaut": "√(25 · 36) = ?", "atb": ["30"], "padoms": "5 · 6."},
        {"jaut": "√(0,04 · 900) = ?", "atb": ["6"], "padoms": "0,2 · 30."},
        {"jaut": "√5 · √45 = ?", "atb": ["15"], "padoms": "√225."},
        {"jaut": "√7 · √28 = ?", "atb": ["14"], "padoms": "√196."},
        {"jaut": "√(16 · 81) = ?", "atb": ["36"], "padoms": "4 · 9."},
        {"jaut": "√10 · √40 = ?", "atb": ["20"], "padoms": "√400."},
    ], pamats=4),

    Varianti("Kur ir kļūda?", [
        {"jaut": "√(9 + 16) = ?",
         "opcijas": ["5", "7", "25", "√7"],
         "pareizi": 0, "padoms": "Vispirms saskaita: √25."},
        {"jaut": "Kura vienādība ir pareiza?",
         "opcijas": ["√(4 · 25) = 10", "√(4 + 25) = 7", "√4 + √25 = √29",
                     "√(4 · 25) = 50"],
         "pareizi": 0, "padoms": "2 · 5 = 10."},
        {"jaut": "√3 · √3 = ?",
         "opcijas": ["3", "9", "√6", "6"],
         "pareizi": 0, "padoms": "√9."},
    ]),

    Pasaule("Kvadrātveida laukumi",
            Ievadi("", [
                {"jaut": "Kvadrātveida laukumā ir 16 flīzes, katra 0,25 m². "
                         "Cik m ir laukuma mala?",
                 "atb": ["2"], "padoms": "√(16 · 0,25) = 4 · 0,5."},
                {"jaut": "Kvadrātveida dārza laukums ir 9 · 144 m². Cik m ir "
                         "dārza mala?",
                 "atb": ["36"], "padoms": "3 · 12."},
                {"jaut": "Cik m sētas vajag ap šo dārzu?",
                 "atb": ["144"], "padoms": "4 · 36."},
                {"jaut": "Taisnstūri 2 m × 8 m pārveido par tāda paša laukuma "
                         "kvadrātu. Cik m ir mala?",
                 "atb": ["4"], "padoms": "√2 · √8 = √16."},
            ]),
            pavediens="maja",
            konteksts="Kvadrāta mala ir laukuma kvadrātsakne. Ja laukums "
                      "dots kā reizinājums, sakni var vilkt pa daļām.",
            kapec="Tā lielu sakni izrēķina bez kalkulatora."),

    Kopsavilkums([
        "Izvelku sakni no reizinājuma pa daļām.",
        "Reizinu saknes, apvienojot tās zem vienas saknes.",
        "Zinu, ka summai šī īpašība neder.",
    ]),

    Majas([
        "Aprēķini: √(36 · 49), √(0,01 · 64), √2 · √50.",
        "Ar piemēru parādi, ka √(a + b) nav √a + √b.",
        "Atrodi mājās kvadrātveida virsmu un aprēķini tās malu no laukuma.",
    ]),
]
