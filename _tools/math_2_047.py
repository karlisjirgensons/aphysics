# -*- coding: utf-8 -*-
"""2. klase, 47. stunda: «Cik veikli atņem?»

Atņemšanas mikrotemata noslēgums: patstāvīgs treniņš ar pārbaudi. Jaukti
piemēri ar un bez desmita sadalīšanas, «cik pietrūkst» un paslēptais
skaitlis - tas viss vienā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas,
                         Pasaule, Sakums, Varianti, stabins)

TEMA = "Cik veikli atņem?"

MERKIS = ("Šodien patstāvīgi atņemsim divciparu skaitļus un pārbaudīsim "
          "rezultātu.")

SATURS = [
    Sakums("Vai vari atņemt tikpat veikli kā saskaitīt?",
           zimejums=stabins(82, 47, "-", virs="10"),
           fakti=["Vispirms paskaties uz vieniem - vai pietiek?",
                  "Ja nē - sadali desmitu.",
                  "Beigās pārbaudi ar saskaitīšanu."]),

    Doma("Mans plāns",
         "Katram piemēram: vieni pietiek? - rēķini - pārbaudi.",
         soli=[
             "Salīdzini vienus.",
             "Ja vajag, sadali desmitu.",
             "Atņem vienus, tad desmitus.",
             "Pārbaudi: starpība + atņēmējs.",
         ]),

    Ievadi("Treniņš", [
        {"jaut": "68 − 25 = ?", "atb": ["43"], "padoms": "Vieni pietiek."},
        {"jaut": "72 − 38 = ?", "atb": ["34"], "padoms": "12 − 8, 6 − 3."},
        {"jaut": "90 − 54 = ?", "atb": ["36"], "padoms": "10 − 4, 8 − 5."},
        {"jaut": "47 − 19 = ?", "atb": ["28"], "padoms": "47 − 20 + 1."},
        {"jaut": "85 − 43 = ?", "atb": ["42"], "padoms": "Vieni pietiek."},
        {"jaut": "61 − 27 = ?", "atb": ["34"], "padoms": "11 − 7, 5 − 2."},
        {"jaut": "100 − 36 = ?", "atb": ["64"], "padoms": "4 + 60."},
        {"jaut": "53 − 48 = ?", "atb": ["5"], "padoms": "No 48 līdz 53."},
    ], pamats=6),

    Kustiba("Zemūdene nirst", [
        {"jaut": "Zemūdene bija 85 m dziļumā un pacēlās par 37 m. Cik "
                 "dziļi tā ir?", "atb": 48, "beigas": 100, "iedala": 10,
         "mers": "m", "objekts": "zemūdene", "merkis": "85 − 37",
         "padoms": "15 − 7, 7 − 3."},
        {"jaut": "No 64 m pacēlās par 29 m. Cik dziļi?", "atb": 35,
         "beigas": 100, "iedala": 10, "mers": "m", "objekts": "zemūdene",
         "merkis": "64 − 29", "padoms": "14 − 9, 5 − 2."},
    ], ievads="Ieraksti dziļumu metros."),

    Varianti("Pārbaudi sevi", [
        {"jaut": "Kurai starpībai jāsadala desmits?",
         "opcijas": ["74 − 36", "74 − 32", "74 − 34"], "pareizi": 0,
         "padoms": "No 4 nevar atņemt 6."},
        {"jaut": "Kura starpība ir 25?",
         "opcijas": ["62 − 37", "62 − 47", "52 − 37"], "pareizi": 0,
         "padoms": "25 + 37 = 62."},
    ]),

    Pasaule("Cik punktu pietrūka?",
            Ievadi("", [
                {"jaut": "Datorspēlē nākamajam līmenim vajag 100 punktu. "
                         "Tev ir 73. Cik pietrūkst?", "atb": ["27"],
                 "padoms": "7 + 20."},
                {"jaut": "Draugam ir 91 punkts, tev 73. Par cik viņam "
                         "vairāk?", "atb": ["18"], "padoms": "91 − 73."},
            ]),
            pavediens="speles",
            konteksts="Spēlē punkti krājas līdz nākamajam līmenim.",
            kapec="Spēlētāji atņem ātrāk, nekā paši pamana."),

    Kopsavilkums([
        "Patstāvīgi atņemu divciparu skaitļus.",
        "Izvēlos, vai sadalīt desmitu.",
        "Pārbaudu katru starpību.",
    ]),

    Majas([
        "Izrēķini 6 starpības no uzdevumu krājuma.",
        "Pārbaudi tās ar saskaitīšanu.",
        "Atzīmē, kas vēl jātrenē.",
    ]),
]
