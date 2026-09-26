# -*- coding: utf-8 -*-
"""3. klase, 141. stunda: «Kā pārbaudīt savu darbu?»

Mikrotemata noslēgums. Summu var pārbaudīt trijos veidos: ar atņemšanu, ar
saskaitāmo maiņu vietām un ar aptuveno vērtību. Katrs no tiem ķer savu kļūdu
veidu, tāpēc skolēns iemācās izvēlēties.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pārbaudīt savu darbu?"

MERKIS = ("Pārbaudīsim summu ar pretējo darbību vai citu paņēmienu.")

SATURS = [
    Sakums("Trīs veidi, kā pārbaudīt vienu summu",
           zimejums=restis([["pārbaude", "rēķins"],
                            ["atņemšana", "683 − 415 = 268"],
                            ["maiņa vietām", "415 + 268 = 683"],
                            ["aptuveni", "300 + 400 = 700"]],
                           "268 + 415 = 683"),
           paraksts="Katra pārbaude ķer savu kļūdu veidu.",
           fakti=["Summu pārbauda ar atņemšanu.",
                  "Var arī saskaitīt vēlreiz, mainot saskaitāmos vietām."]),

    Doma("Izvēlies pārbaudi pēc kļūdas veida",
         "Atņemšana ķer aritmētikas kļūdu, maiņa vietām - pārrakstīšanos, "
         "aptuvenā vērtība - rupju kļūdu.",
         soli=[
             "Izrēķini summu.",
             "Atņem no summas vienu saskaitāmo - jāsanāk otram.",
             "Vai arī saskaiti vēlreiz, sākot ar otru skaitli.",
             "Novērtē summu aptuveni un salīdzini.",
         ],
         pieze="Pārrēķināt tāpat, kā rēķināji pirmo reizi, nav pārbaude - "
               "to pašu kļūdu izdarīsi otrreiz."),

    Paraugs("Vai 268 + 415 = 683?",
            uzd="Pārbaudi summu 268 + 415 = 683 divos veidos.",
            soli=[
                ("683 − 415 = 268",
                 "Pretējā darbība dod otru saskaitāmo."),
                ("415 + 268 = 683",
                 "Saskaitīšana otrā secībā dod to pašu summu."),
                ("Abas pārbaudes sakrīt",
                 "Atbilde ir pareiza."),
            ],
            atbilde="683 ir pareizi"),

    Ievadi("Izrēķini un pārbaudi", [
        {"jaut": "268 + 415 = ?", "atb": ["683"], "padoms": "Stabiņā."},
        {"jaut": "Pārbaude: 683 − 415 = ?", "atb": ["268"],
         "padoms": "Ja sanāk 268, summa ir pareiza."},
        {"jaut": "347 + 256 = ?", "atb": ["603"], "padoms": "Stabiņā."},
        {"jaut": "Pārbaude: 603 − 256 = ?", "atb": ["347"],
         "padoms": "Pretējā darbība."},
        {"jaut": "519 + 284 = ?", "atb": ["803"], "padoms": "Stabiņā."},
        {"jaut": "Pārbaude: 803 − 284 = ?", "atb": ["519"],
         "padoms": "Pretējā darbība."},
    ], pamats=4),

    Zimejums("Kura pārbaude ko atrod",
             restis([["kļūda", "pārbaude"],
                     ["aizmirsts pārnesums", "atņemšana"],
                     ["pārrakstīts cipars", "maiņa vietām"],
                     ["desmit reižu kļūda", "aptuvenā vērtība"]],
                    "trīs kļūdas, trīs pārbaudes"),
             paskaidro="Tāpēc vērts lietot vismaz divas pārbaudes, nevis "
                       "vienu.",
             ievads="Šī tabula der visam gadam."),

    Varianti("Kura pārbaude der?", [
        {"jaut": "Ar ko pārbauda summu 250 + 175 = 425?",
         "opcijas": ["425 − 175", "425 + 175", "425 · 175", "250 − 175"],
         "pareizi": 0, "padoms": "Pretējā darbība."},
        {"jaut": "Kāpēc nepietiek pārrēķināt tāpat?",
         "opcijas": ["To pašu kļūdu var atkārtot", "Tas ir par ilgu",
                     "Tas ir aizliegts", "Tas pietiek"],
         "pareizi": 0, "padoms": "Vajag citu ceļu."},
        {"jaut": "Skolēns uzrakstīja 268 + 415 = 583. Kura pārbaude to "
                 "atklāj?",
         "opcijas": ["583 − 415 = 168, nevis 268", "Aptuvenā vērtība",
                     "Maiņa vietām", "Nekura"],
         "pareizi": 0, "padoms": "Atņemšana dod citu skaitli."},
        {"jaut": "Cik ir 436 + 287?",
         "opcijas": ["723", "713", "733", "623"],
         "pareizi": 0, "padoms": "Ar divām pārejām."},
    ], pamats=4),

    Pasaule("Vai maršruta summa ir pareiza?",
            Ievadi("", [
                {"jaut": "Posmi 268, 415 un 137 km. Cik ir pirmo divu summa?",
                 "atb": ["683"], "padoms": "268 + 415."},
                {"jaut": "Cik ir visu trīs summa?", "atb": ["820"],
                 "padoms": "683 + 137."},
                {"jaut": "Pārbaude: 820 − 137 = ?", "atb": ["683"],
                 "padoms": "Pretējā darbība."},
                {"jaut": "Cik apmēram ir visu trīs summa? (Noapaļo līdz "
                         "simtiem.)",
                 "atb": ["800"], "padoms": "300 + 400 + 100."},
            ]),
            pavediens="celojums",
            konteksts="Maršruta kopgarumu pārbauda vienmēr - no tā atkarīgs "
                      "gan laiks, gan degviela.",
            kapec="Divas pārbaudes aizņem minūti un pasargā no gara "
                  "apļa."),

    Kopsavilkums([
        "Pārbaudu summu ar atņemšanu.",
        "Pārbaudu summu, mainot saskaitāmos vietām.",
        "Pārbaudu summu ar aptuveno vērtību.",
        "Zinu, ka pārrēķināt tāpat nav pārbaude.",
    ]),

    Majas([
        "Izrēķini piecas summas un pārbaudi katru divos veidos.",
        "Atrodi kļūdu rēķinā 356 + 248 = 504 un izlabo to.",
        "Pārbaudi mājas čeka kopsummu.",
    ]),
]
