# -*- coding: utf-8 -*-
"""3. klase, 169. stunda: «Cik droši zinu reizināšanas tabulu?»

Gada noslēguma pirmā stunda. Reizināšanas tabula ir prasme, uz kuras stāv
visa 4. klase, tāpēc to pārbauda vispirms - un rezultāts ir nevis atzīme, bet
saraksts, ko trenēt vasarā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Cik droši zinu reizināšanas tabulu?"

MERKIS = ("Formatīvi pārbaudīsim reizināšanas tabulu un dalīšanu; atzīmēsim, "
          "kas vēl jātrenē.")

SATURS = [
    Sakums("Kas no tabulas paliks atmiņā pēc vasaras?",
           zimejums=restis([["6 · 7", "7 · 8", "8 · 9", "9 · 6"],
                            [42, 56, 72, 54]],
                           "četri grūtākie"),
           paraksts="Ja šos zini droši, tabula ir tava.",
           fakti=["Reizināšanas tabula noder katrā 4. klases tematā.",
                  "Vasarā aizmirstas tieši tie reizinājumi, kas bija vāji."]),

    Doma("Pārbaudi tabulu sajauktā secībā",
         "Rindā skaitot, atbildi var uzminēt; sajauktā secībā redz, kas "
         "tiešām ir atmiņā.",
         soli=[
             "Izdari uzdevumus sajauktā secībā.",
             "Atzīmē tos, kuros vajadzēja padomāt ilgāk.",
             "Atzīmē arī tos, kuros kļūdījies.",
             "Uzraksti šos reizinājumus uz vasaras kartītēm.",
         ],
         pieze="Pieci reizinājumi, atkārtoti reizi nedēļā, vasaru pārdzīvo; "
               "visa tabula, atkārtota vienu reizi, - ne."),

    Paraugs("Kā pārbaudīt aizmirstu reizinājumu?",
            uzd="Cik ir 8 · 7, ja šo reizinājumu neatceries?",
            soli=[
                ("4 · 7 = 28",
                 "Četrinieku rindu zina vienmēr."),
                ("28 + 28 = 56",
                 "Dubulto - tas dod astotnieku."),
                ("Pārbaude: 56 : 7 = 8",
                 "Dalījums sakrīt, tātad atbilde pareiza."),
            ],
            atbilde="56"),

    Ievadi("Visa tabula sajauktā secībā", [
        {"jaut": "6 · 7 = ?", "atb": ["42"], "padoms": "35 + 7."},
        {"jaut": "8 · 9 = ?", "atb": ["72"], "padoms": "80 − 8."},
        {"jaut": "7 · 8 = ?", "atb": ["56"], "padoms": "49 + 7."},
        {"jaut": "9 · 6 = ?", "atb": ["54"], "padoms": "60 − 6."},
        {"jaut": "56 : 8 = ?", "atb": ["7"], "padoms": "8 · 7 = 56."},
        {"jaut": "72 : 9 = ?", "atb": ["8"], "padoms": "9 · 8 = 72."},
        {"jaut": "6 · 6 = ?", "atb": ["36"], "padoms": "30 + 6."},
        {"jaut": "63 : 7 = ?", "atb": ["9"], "padoms": "7 · 9 = 63."},
    ], pamats=6),

    Zimejums("Vasaras kartītes",
             restis([["reizinājums", "atkārtot"],
                     ["7 · 8", "jā"],
                     ["6 · 9", "jā"],
                     ["5 · 4", "nē"]],
                    "ko ņemt līdzi vasarā"),
             paskaidro="Kartīšu kaudzītei jābūt mazai - tikai tad to tiešām "
                       "atkārtos.",
             ievads="Tā izskatās gatavs saraksts."),

    Varianti("Kā saglabāt prasmi?", [
        {"jaut": "Kāpēc tabulu pārbauda sajauktā secībā?",
         "opcijas": ["Rindā atbildi var uzminēt", "Tā ir ātrāk",
                     "Tā ir grūtāk", "Tā prasa skolotājs"],
         "pareizi": 0, "padoms": "Ritms palīdz, atmiņa - ne vienmēr."},
        {"jaut": "Cik reizinājumu vērts ņemt līdzi vasarā?",
         "opcijas": ["Tos, kas nepadodas", "Visus 100",
                     "Nevienu", "Tikai vieglos"],
         "pareizi": 0, "padoms": "Maza kaudzīte tiešām tiek atkārtota."},
        {"jaut": "Cik ir 9 · 9?",
         "opcijas": ["81", "72", "99", "90"],
         "pareizi": 0, "padoms": "90 − 9."},
        {"jaut": "Cik ir 48 : 6?",
         "opcijas": ["8", "6", "7", "9"],
         "pareizi": 0, "padoms": "6 · 8 = 48."},
    ], pamats=4),

    Pasaule("Kur tabula noder vasarā?",
            Ievadi("", [
                {"jaut": "Ogu kastītē 8 rindas pa 7 ogām. Cik ogu?",
                 "atb": ["56"], "padoms": "8 · 7."},
                {"jaut": "54 ogas sadala 6 traukos. Cik ogu vienā?",
                 "atb": ["9"], "padoms": "54 : 6."},
                {"jaut": "Velosipēdā 7 pārnesumi, katrā 6 zobrati. Cik "
                         "zobratu?",
                 "atb": ["42"], "padoms": "7 · 6."},
                {"jaut": "72 km sadala 8 vienādos posmos. Cik kilometru ir "
                         "viens posms?",
                 "atb": ["9"], "padoms": "72 : 8."},
            ]),
            pavediens="daba",
            konteksts="Vasarā tabula noder ogu lasīšanā, riteņbraukšanā un "
                      "jebkurā darbā ar vienādām grupām.",
            kapec="Prasme, ko lieto, neaizmirstas."),

    Kopsavilkums([
        "Zinu reizināšanas tabulu sajauktā secībā.",
        "Atrodu dalījumu, domājot par reizinājumu.",
        "Zinu paņēmienus, kā iegūt aizmirstu reizinājumu.",
        "Esmu atzīmējis, ko trenēt vasarā.",
    ]),

    Majas([
        "Uzraksti piecas kartītes ar reizinājumiem, kas vēl nepadodas.",
        "Paņem tās līdzi vasarā.",
        "Atkārto tās reizi nedēļā.",
    ]),
]
