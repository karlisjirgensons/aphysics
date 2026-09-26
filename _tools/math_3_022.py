# -*- coding: utf-8 -*-
"""3. klase, 22. stunda: «Kā pārbaudīt dalījumu?»

Pārbaude ar pretējo darbību ir prasme, kas der visam kursam. Te to iemāca uz
dalīšanas, jo dalot kļūda visbiežāk paliek nepamanīta: atbilde izskatās
kārtīga arī tad, kad tā nav. Pārbaude to atklāj vienā rēķinā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pārbaudīt dalījumu?"

MERKIS = ("Iemācīsimies pārbaudīt dalīšanu ar reizināšanu un skaidrot savu "
          "pierakstu.")

SATURS = [
    Sakums("Kā pamanīt kļūdu, kas izskatās pareiza?",
           zimejums=restis([["54 : 6 = 8", "8 · 6 = 48", "nepareizi"],
                            ["54 : 6 = 9", "9 · 6 = 54", "pareizi"]],
                           "pārbaude ar reizināšanu"),
           paraksts="Abas atbildes izskatās ticamas - izšķir tikai pārbaude.",
           fakti=["Dalīšanu pārbauda ar reizināšanu.",
                  "Ja reizinājums nesakrīt ar dalāmo, atbilde ir nepareiza."]),

    Doma("Pārbaude ir pretējā darbība",
         "Ja a : b = c, tad c · b jābūt tieši a - citādi kaut kur ir kļūda.",
         soli=[
             "Izrēķini dalījumu.",
             "Reizini iegūto atbildi ar dalītāju.",
             "Salīdzini rezultātu ar dalāmo.",
             "Ja skaitļi nesakrīt, meklē kļūdu un rēķini vēlreiz.",
         ],
         pieze="Ja dalīšana bija ar atlikumu, pārbaudē pie reizinājuma "
               "jāpieskaita atlikums: 50 : 7 = 7 (atl. 1), jo 7 · 7 + 1 = 50."),

    Paraugs("Vai 72 : 8 = 9?",
            uzd="Izrēķini 72 : 8 un pārbaudi savu atbildi.",
            soli=[
                ("8 · ? = 72",
                 "Dalījumu lasa kā reizinājumu ar trūkstošu skaitli."),
                ("72 : 8 = 9",
                 "Astotnieku rindā 72 ir devītais skaitlis."),
                ("9 · 8 = 72",
                 "Pārbaude: reizinājums sakrīt ar dalāmo - atbilde pareiza."),
            ],
            atbilde="9; pārbaude 9 · 8 = 72"),

    Ievadi("Izrēķini un pārbaudi", [
        {"jaut": "63 : 7 = ?", "atb": ["9"], "padoms": "Pārbaude: 9 · 7."},
        {"jaut": "48 : 8 = ?", "atb": ["6"], "padoms": "Pārbaude: 6 · 8."},
        {"jaut": "42 : 6 = ?", "atb": ["7"], "padoms": "Pārbaude: 7 · 6."},
        {"jaut": "Ar kādu reizinājumu pārbaudīt 56 : 7 = 8?",
         "atb": ["8·7", "8 · 7", "56", "7·8", "7 · 8"],
         "padoms": "Atbildi reizina ar dalītāju.", "tastatura": "text"},
        {"jaut": "81 : 9 = ?", "atb": ["9"], "padoms": "Pārbaude: 9 · 9."},
        {"jaut": "Cik ir 7 · 7 + 1, ja 50 : 7 = 7 un atlikums 1?",
         "atb": ["50"], "padoms": "Pārbaude ar atlikumu."},
    ], pamats=4),

    Zimejums("Pārbaude ar atlikumu",
             restis([["50 : 7", "= 7", "atl. 1"],
                     ["7 · 7", "= 49", "+ 1 = 50"]],
                    "reizinājums un atlikums kopā dod dalāmo"),
             paskaidro="Ja atlikums ir, pārbaudē to pieskaita - tikai tad "
                       "sanāk sākotnējais skaitlis.",
             ievads="Skaties, kā abas rindas satiekas pie 50."),

    Varianti("Kur ir kļūda?", [
        {"jaut": "Skolēns uzrakstīja 45 : 5 = 8. Kā to pamanīt?",
         "opcijas": ["8 · 5 = 40, nevis 45", "Atbilde ir par mazu",
                     "45 nedalās ar 5", "Kļūdas nav"],
         "pareizi": 0, "padoms": "Pārbaudi ar reizināšanu."},
        {"jaut": "Ar ko pārbauda 36 : 4 = 9?",
         "opcijas": ["9 · 4", "36 · 4", "9 : 4", "36 + 4"],
         "pareizi": 0, "padoms": "Atbildi reizina ar dalītāju."},
        {"jaut": "40 : 6 = 6 un atlikums 4. Vai tas ir pareizi?",
         "opcijas": ["Jā, jo 6 · 6 + 4 = 40", "Nē, atlikums ir par lielu",
                     "Nē, jo 40 nedalās ar 6", "Jā, bet atlikums ir 2"],
         "pareizi": 0, "padoms": "36 + 4 = 40, un 4 < 6."},
        {"jaut": "Kāds atlikums nevar būt, dalot ar 5?",
         "opcijas": ["5", "4", "3", "0"],
         "pareizi": 0, "padoms": "Atlikums ir mazāks par dalītāju."},
    ], pamats=4),

    Pasaule("Vai recepte tika sadalīta pareizi?",
            Ievadi("", [
                {"jaut": "54 pankūkas sadalīja 6 šķīvjos. Cik pankūku ir "
                         "vienā šķīvī?",
                 "atb": ["9"], "padoms": "54 : 6."},
                {"jaut": "Pārbaudi: cik pankūku ir 6 šķīvjos pa 9?",
                 "atb": ["54"], "padoms": "6 · 9."},
                {"jaut": "40 pankūkas liek šķīvjos pa 6. Cik pilnu šķīvju "
                         "sanāks?",
                 "atb": ["6"], "padoms": "36 ≤ 40, bet 42 > 40."},
                {"jaut": "Cik pankūku paliks pāri?",
                 "atb": ["4"], "padoms": "40 − 36."},
            ]),
            pavediens="virtuve",
            konteksts="Pavārs vienmēr pārskaita gatavo ēdienu - citādi kāds "
                      "šķīvis paliek tukšāks par citiem.",
            kapec="Pārbaude aizņem dažas sekundes un pasargā no pārtaisīšanas."),

    Kopsavilkums([
        "Pārbaudu dalīšanu ar reizināšanu.",
        "Pārbaudē ar atlikumu pieskaitu arī atlikumu.",
        "Zinu, ka atlikums vienmēr ir mazāks par dalītāju.",
        "Paskaidroju savu pierakstu ar vārdiem.",
    ]),

    Majas([
        "Izrēķini piecus dalījumus un katru pārbaudi ar reizināšanu.",
        "Atrodi kļūdu rēķinā 56 : 8 = 6 un izlabo to.",
        "Sadali 50 lietas mājās pa 8 un pārbaudi atlikumu.",
    ]),
]
