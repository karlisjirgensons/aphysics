# -*- coding: utf-8 -*-
"""2. klase, 127. stunda: «Kā iegaumēt reizinājumus?»

Iegaumēšana ar kartītēm un trenēšanos pārī: vienā pusē 7 · 2, otrā - 14.
Kartītes, kuras zina uzreiz, liek vienā kaudzē; pārējās trenē vēlreiz. Triki:
reizināt ar 2 - tas pats, kas dubultot.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kā iegaumēt reizinājumus?"

MERKIS = ("Šodien izveidosim kartītes un vingrināsimies pārī, lai "
          "iegaumētu reizinājumus un dalījumus ar 2.")

SATURS = [
    Sakums("Kā atcerēties 10 reizinājumus uz visu mūžu?",
           zimejums=restis([["7 · 2", "→", "14"], ["14 : 2", "→", "7"]]),
           paraksts="Kartītes priekšpuse un aizmugure.",
           fakti=["Atkārtošana palīdz atcerēties.",
                  "Kartītes, ko zini, - malā.",
                  "Pārējās - vēlreiz, līdz zini."]),

    Doma("Kartīšu metode",
         "Trenē tās kartītes, ko vēl nezini.",
         soli=[
             "Uzraksti kartītes: priekšpusē uzdevums, aizmugurē atbilde.",
             "Pārī: viens rāda, otrs atbild.",
             "Zināmās liek kaudzē «zinu», pārējās - «trenēt».",
             "Trenē, līdz visas ir «zinu».",
         ],
         pieze="Reizināt ar 2 - tas pats, kas dubultot: 8 · 2 = 8 + 8."),

    Ievadi("Ātrā kārta", [
        {"jaut": "4 · 2 = ?", "atb": ["8"], "padoms": "4 + 4."},
        {"jaut": "7 · 2 = ?", "atb": ["14"], "padoms": "7 + 7."},
        {"jaut": "18 : 2 = ?", "atb": ["9"], "padoms": "9 + 9 = 18."},
        {"jaut": "9 · 2 = ?", "atb": ["18"], "padoms": "9 + 9."},
        {"jaut": "12 : 2 = ?", "atb": ["6"], "padoms": "6 + 6."},
        {"jaut": "6 · 2 = ?", "atb": ["12"], "padoms": "6 + 6."},
        {"jaut": "16 : 2 = ?", "atb": ["8"], "padoms": "8 + 8."},
        {"jaut": "3 · 2 = ?", "atb": ["6"], "padoms": "3 + 3."},
    ], pamats=6),

    Petijums("Kartītes pārī", [
        "Izgriez 10 kartītes un uzraksti 1 · 2 ... 10 · 2.",
        "Otrā pusē - atbildes.",
        "Trenējieties pārī 5 minūtes.",
        "Cik kartīšu ir kaudzē «zinu»?",
    ], vajag="biezs papīrs, šķēres, flomāsteris"),

    Varianti("Kurš triks?", [
        {"jaut": "Kā ātri atrast 8 · 2?",
         "opcijas": ["dubulto: 8 + 8", "skaiti pa 1", "atņem 2"],
         "pareizi": 0, "padoms": "Reizināt ar 2 = dubultot."},
        {"jaut": "Kā ātri atrast 14 : 2?",
         "opcijas": ["puse no 14", "14 − 2", "14 + 2"], "pareizi": 0,
         "padoms": "Dalīt ar 2 = atrast pusi."},
    ]),

    Pasaule("Viktorīna",
            Ievadi("", [
                {"jaut": "Viktorīnā par katru pareizo atbildi 2 punkti. Anna "
                         "atbildēja pareizi uz 9. Cik punktu?",
                 "atb": ["18"], "padoms": "9 · 2."},
                {"jaut": "Toms ieguva 14 punktus. Cik pareizu atbilžu?",
                 "atb": ["7"], "padoms": "14 : 2."},
            ]),
            pavediens="speles",
            konteksts="Klases viktorīnā punktus skaita pa 2.",
            kapec="Kas zina reizinājumus, skaita punktus uzreiz."),

    Kopsavilkums([
        "Trenēju reizinājumus ar kartītēm.",
        "Zinu, ka reizināt ar 2 - dubultot.",
        "Zinu, ka dalīt ar 2 - atrast pusi.",
    ]),

    Majas([
        "Trenējies ar kartītēm katru vakaru 3 minūtes.",
        "Pieraksti, cik kartīšu zini katru dienu.",
        "Vai pēc nedēļas zini visas?",
    ]),
]
