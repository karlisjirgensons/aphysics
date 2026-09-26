# -*- coding: utf-8 -*-
"""7. klase, 12. stunda: «Cik nogriežņu var novilkt?»

Ģeometrijā pilnā pārlase skaita nogriežņus, trijstūrus un diagonāles.
Nogrieznis AB ir tas pats, kas BA, tāpēc n punktiem nogriežņu ir
n · (n − 1) : 2 - tas pats rēķins, kas rokasspiedieniem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Cik nogriežņu var novilkt?"

MERKIS = ("Iemācīsimies saskaitīt nogriežņus, starus un diagonāles, "
          "izmantojot pilno pārlasi un spriedumu.")

_PIECI = geometrija(
    [("A", 0, 2), ("B", 2.6, 4), ("C", 5.2, 2), ("D", 4.2, -1),
     ("E", 1, -1)],
    nogriezni=["AB", "AC", "AD", "AE", "BC", "BD", "BE", "CD", "CE", "DE"])

SATURS = [
    Sakums("Pieci punkti - cik līniju?",
           zimejums=_PIECI,
           paraksts="Katrs punkts savienots ar katru.",
           fakti=["No katra punkta iziet 4 nogriežņi.",
                  "5 · 4 = 20, bet katrs nogrieznis saskaitīts divreiz.",
                  "Tātad nogriežņu ir 10."]),

    Doma("AB un BA ir viens nogrieznis",
         "Ja nekādi trīs punkti neatrodas uz vienas taisnes, tad n punktus "
         "savieno n · (n − 1) : 2 nogriežņi: no katra punkta iziet (n − 1) "
         "nogriežņi, un katrs saskaitīts divos galos.",
         soli=[
             "Saskaiti, cik nogriežņu iziet no viena punkta.",
             "Sareizini ar punktu skaitu.",
             "Izdali ar 2, jo AB = BA.",
             "Mazam skaitam pārbaudi, uzzīmējot.",
         ],
         pieze="Tas pats rēķins, kas rokasspiedieniem - matemātikā viens "
               "modelis der daudzām situācijām."),

    Paraugs("Daudzstūra diagonāles",
            uzd="Cik diagonāļu ir sešstūrim?",
            soli=[
                ("Nogriežņu starp 6 virsotnēm: 6 · 5 : 2 = 15",
                 "Visi savienojumi."),
                ("No tiem 6 ir malas", "Blakus virsotnes."),
                ("15 − 6 = 9", "Pārējie ir diagonāles."),
            ],
            atbilde="9 diagonāles"),

    Zimejums("Uz vienas taisnes",
             geometrija([("A", 0, 0), ("B", 2, 0), ("C", 5, 0), ("D", 7, 0)],
                        nogriezni=["AD"]),
             ievads="Ja punkti ir uz vienas taisnes, nogriežņi pārklājas, "
                    "bet tik un tā ir dažādi.",
             paskaidro="AB, AC, AD, BC, BD, CD - joprojām 4 · 3 : 2 = 6 "
                       "nogriežņi."),

    Ievadi("Saskaiti", [
        {"jaut": "Cik nogriežņu savieno 4 punktus (katru ar katru)?",
         "atb": ["6"], "padoms": "4 · 3 : 2."},
        {"jaut": "Cik nogriežņu savieno 8 punktus?",
         "atb": ["28"], "padoms": "8 · 7 : 2."},
        {"jaut": "Cik diagonāļu ir piecstūrim?",
         "atb": ["5"], "padoms": "10 − 5."},
        {"jaut": "Cik diagonāļu ir astoņstūrim?",
         "atb": ["20"], "padoms": "28 − 8."},
        {"jaut": "Cik trijstūru var izveidot ar virsotnēm 4 punktos (nekādi "
                 "trīs nav uz vienas taisnes)?",
         "atb": ["4"], "padoms": "Katru reizi atmet vienu punktu."},
        {"jaut": "Uz taisnes ir 5 punkti. Cik nogriežņu ar galiem šajos "
                 "punktos?",
         "atb": ["10"], "padoms": "5 · 4 : 2."},
    ], pamats=4),

    Varianti("Spried", [
        {"jaut": "Punktu skaitu divkāršo no 5 uz 10. Nogriežņu skaits...",
         "opcijas": ["pieaug vairāk nekā divas reizes (10 → 45)",
                     "divkāršojas (10 → 20)",
                     "nemainās", "pieaug par 5"],
         "pareizi": 0,
         "padoms": "10 · 9 : 2."},
        {"jaut": "Cik staru ar sākumu punktā A iet caur 3 citiem punktiem "
                 "(nekādi divi ar A nav uz vienas taisnes)?",
         "opcijas": ["3", "6", "4", "1"],
         "pareizi": 0,
         "padoms": "Viens stars caur katru punktu."},
        {"jaut": "Kurš daudzstūris ir vienīgais bez diagonālēm?",
         "opcijas": ["Trijstūris", "Četrstūris", "Kvadrāts", "Piecstūris"],
         "pareizi": 0,
         "padoms": "Visas virsotnes ir blakus."},
    ]),

    Pasaule("Optisko kabeļu tīkls",
            Ievadi("", [
                {"jaut": "6 pilsētas jāsavieno ar kabeli tieši katru ar "
                         "katru. Cik kabeļu līniju?",
                 "atb": ["15"], "padoms": "6 · 5 : 2."},
                {"jaut": "Viena līnija maksā 2 miljonus eiro. Cik "
                         "miljonus maksā viss tīkls?",
                 "atb": ["30"], "padoms": "15 · 2."},
                {"jaut": "Lētāk: visas pilsētas savieno tikai ar centru. "
                         "Cik līniju vajag?",
                 "atb": ["5"], "padoms": "Katra no 5 pārējām - ar centru."},
            ]),
            pavediens="dati",
            konteksts="Interneta tīklus plāno kā grafus: pilsētas ir punkti, "
                      "kabeļi - nogriežņi.",
            kapec="«Katrs ar katru» ir drošs, bet dārgs; «zvaigzne» - lēta."),

    Kopsavilkums([
        "Saskaitu nogriežņus: n · (n − 1) : 2.",
        "Atrodu daudzstūra diagonāļu skaitu.",
        "Pamatoju, kāpēc dala ar 2.",
        "Redzu, ka viens modelis der daudzām situācijām.",
    ]),

    Majas([
        "Uzzīmē 6 punktus un savieno katru ar katru. Saskaiti.",
        "Cik diagonāļu ir desmitstūrim?",
        "Kā mainītos atbilde, ja nogrieznis AB un BA būtu dažādi?",
    ]),
]
