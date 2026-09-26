# -*- coding: utf-8 -*-
"""7. klase, 6. stunda: «Vai esam uzskaitījuši visas apakškopas?»

Uzskaitīt visas apakškopas nejaušā secībā nozīmē kādu aizmirst. Stunda
iemāca sistēmu - pēc elementu skaita un ar jautājumu «ņemt vai neņemt» -
un parāda, ka ar katru jaunu elementu apakškopu skaits dubultojas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, koks, restis)

TEMA = "Vai esam uzskaitījuši visas apakškopas?"

MERKIS = ("Iemācīsimies sistemātiski uzskaitīt visas kopas apakškopas un "
          "pamatot, ka citu nav.")

SATURS = [
    Sakums("Picas piedevas: cik dažādu picu?",
           fakti=["Piedevas: sēnes, olīvas, siers.",
                  "Katru var ņemt vai neņemt - arī visas vai nevienu.",
                  "Katra pica ir piedevu kopas apakškopa."]),

    Doma("Katram elementam - «ņemt» vai «neņemt»",
         "Katra apakškopa rodas, katram elementam izlemjot - ņemt vai "
         "neņemt. Tāpēc kopai ar n elementiem ir 2 · 2 · ... · 2 = 2ⁿ "
         "apakškopu.",
         soli=[
             "Sāc ar tukšo kopu ∅.",
             "Tad visas ar vienu elementu.",
             "Tad visas ar diviem - pa pāriem, pēc kārtas.",
             "... līdz pašai kopai.",
             "Pārbaudi skaitu: tam jābūt 2ⁿ.",
         ],
         pieze="Kārtība pēc elementu skaita ir pamatojums: katrā grupā "
               "redzams, ka neviens pāris nav izlaists."),

    Zimejums("Ņemt (+) vai neņemt (−)",
             koks([["+", "−"], ["+", "−"], ["+", "−"]]),
             ievads="Sēnes, olīvas, siers - katrā solī divi zari.",
             paskaidro="2 · 2 · 2 = 8 zaru gali - 8 apakškopas. Pēdējā "
                       "«−−−» ir pica bez piedevām, ∅."),

    Paraugs("Visas {a; b; c} apakškopas",
            uzd="Uzskaiti visas kopas {a; b; c} apakškopas.",
            soli=[
                ("0 elementu: ∅", "Viena."),
                ("1 elements: {a}, {b}, {c}", "Trīs."),
                ("2 elementi: {a; b}, {a; c}, {b; c}",
                 "Pāri pēc kārtas: a ar katru nākamo, tad b ar c."),
                ("3 elementi: {a; b; c}", "Viena."),
                ("1 + 3 + 3 + 1 = 8 = 2³", "Skaits sakrīt ar 2³."),
            ],
            atbilde="8 apakškopas"),

    Zimejums("Apakškopu skaits",
             restis([["elementu", "1", "2", "3", "4", "5"],
                     ["apakškopu", "2", "4", "8", "16", "32"]]),
             paskaidro="Katrs jauns elements apakškopu skaitu dubulto."),

    Ievadi("Cik apakškopu?", [
        {"jaut": "Cik apakškopu ir kopai ar 4 elementiem?",
         "atb": ["16"], "padoms": "2⁴."},
        {"jaut": "Cik apakškopu ir kopai {x}?",
         "atb": ["2"], "padoms": "∅ un {x}."},
        {"jaut": "Cik {1; 2; 3; 4} apakškopu satur tieši 2 elementus?",
         "atb": ["6"], "padoms": "12, 13, 14, 23, 24, 34."},
        {"jaut": "Cik {a; b; c} apakškopu satur elementu a?",
         "atb": ["4"], "padoms": "{a}, {a; b}, {a; c}, {a; b; c}."},
        {"jaut": "Cik apakškopu ir tukšajai kopai?",
         "atb": ["1"], "padoms": "Tikai pati ∅. 2⁰ = 1."},
        {"jaut": "Cik apakškopu ir kopai ar 6 elementiem?",
         "atb": ["64"], "padoms": "2⁶."},
    ], pamats=4),

    Varianti("Vai saraksts ir pilns?", [
        {"jaut": "Toms uzskaitīja {1; 2} apakškopas: {1}, {2}, {1; 2}. "
                 "Kas trūkst?",
         "opcijas": ["∅", "{0}", "{3}", "Nekas netrūkst"],
         "pareizi": 0,
         "padoms": "Arī tukšā kopa ir apakškopa."},
        {"jaut": "Kopai ir 32 apakškopas. Cik tajā ir elementu?",
         "opcijas": ["5", "16", "6", "32"],
         "pareizi": 0,
         "padoms": "2 · 2 · 2 · 2 · 2 = 32."},
        {"jaut": "Kāpēc kārtība pēc elementu skaita palīdz?",
         "opcijas": ["Katrā grupā var pārbaudīt, ka neviena nav izlaista",
                     "Tā ir ātrāka rakstīšana",
                     "Tā ir vienīgā pareizā secība",
                     "Tā samazina apakškopu skaitu"],
         "pareizi": 0,
         "padoms": "Sistēma ir pamatojums."},
    ]),

    Pasaule("Cik dažādu picu var pasūtīt?",
            Ievadi("", [
                {"jaut": "Picērijā ir 5 piedevas; katru var ņemt vai "
                         "neņemt. Cik dažādu picu (arī bez piedevām)?",
                 "atb": ["32"], "padoms": "2⁵."},
                {"jaut": "Pievieno sesto piedevu. Cik picu tagad?",
                 "atb": ["64"], "padoms": "Divreiz vairāk."},
                {"jaut": "Cik picu ar 5 piedevām ir ar vismaz vienu "
                         "piedevu?",
                 "atb": ["31"], "padoms": "32 − 1 (bez piedevām)."},
            ]),
            pavediens="virtuve",
            konteksts="Reklāma sola «vairāk nekā 60 dažādu picu» - tikai ar "
                      "sešām piedevām.",
            kapec="Ar katru piedevu izvēle dubultojas."),

    Kopsavilkums([
        "Uzskaitu apakškopas pēc elementu skaita.",
        "Zinu, ka kopai ar n elementiem ir 2ⁿ apakškopu.",
        "Neaizmirstu ∅ un pašu kopu.",
        "Pamatoju, ka saraksts ir pilns.",
    ]),

    Majas([
        "Uzskaiti visas {1; 2; 3; 4} apakškopas un saskaiti.",
        "Cik apakškopu ar 3 elementiem ir kopai ar 4 elementiem?",
        "Izdomā savu «picas» uzdevumu ar 4 izvēlēm.",
    ]),
]
