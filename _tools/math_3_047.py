# -*- coding: utf-8 -*-
"""3. klase, 47. stunda: «Kā samaksāt vajadzīgo summu?»

Nauda ir pirmais lielums, ko skolēns tiešām lieto. Uzdevums «samaksā 35 ct»
nav viens rēķins, bet vairāki risinājumi, un tieši tas ir vērtīgi: bērns
redz, ka pareizu atbilžu var būt daudz un tās var sakārtot pēc sistēmas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kā samaksāt vajadzīgo summu?"

MERKIS = ("Ar naudas modeļiem atradīsim pēc iespējas vairāk veidu, kā "
          "samaksāt doto summu.")

SATURS = [
    Sakums("Cik dažādi var samaksāt 35 centus?",
           zimejums=restis([["20 + 10 + 5"],
                            ["20 + 5 + 5 + 5"],
                            ["10 + 10 + 10 + 5"],
                            ["10 + 10 + 5 + 5 + 5"]],
                           "četri veidi no daudziem"),
           paraksts="Summa ir viena, monētu komplekti - dažādi.",
           fakti=["Eiro centu monētas ir 1, 2, 5, 10, 20 un 50.",
                  "Vienu summu gandrīz vienmēr var samaksāt vairākos veidos."]),

    Doma("Sāc ar lielāko monētu",
         "Ja katru reizi ņem lielāko monētu, kas vēl ietilpst, monētu skaits "
         "sanāk vismazākais.",
         soli=[
             "Paskaties, kura lielākā monēta vēl ietilpst summā.",
             "Paņem to un atņem no summas.",
             "Atkārto ar atlikumu.",
             "Beidz, kad atlikums ir nulle.",
         ],
         pieze="Citi veidi arī ir pareizi - tikai monētu būs vairāk. "
               "Veikalā tas mēdz noderēt: ar sīknaudu atlikumu var izvairīties."),

    Paraugs("Kā samaksāt 47 centus ar vismazāk monētām?",
            uzd="Samaksā 47 ct, izmantojot pēc iespējas mazāk monētu.",
            soli=[
                ("47 − 20 = 27",
                 "Lielākā monēta, kas ietilpst, ir 20 ct."),
                ("27 − 20 = 7",
                 "Vēl viena divdesmitcentu monēta."),
                ("7 − 5 = 2",
                 "Nākamā lielākā, kas ietilpst, ir 5 ct."),
                ("2 − 2 = 0",
                 "Pēdējā monēta ir 2 ct; kopā četras monētas."),
            ],
            atbilde="20 + 20 + 5 + 2 - četras monētas"),

    Ievadi("Saskaiti monētas", [
        {"jaut": "20 + 10 + 5 = ? ct", "atb": ["35"], "padoms": "30 + 5."},
        {"jaut": "50 + 20 + 2 = ? ct", "atb": ["72"], "padoms": "70 + 2."},
        {"jaut": "Cik monētu vajag 40 ct, ja ņem tikai 20 ct monētas?",
         "atb": ["2"], "padoms": "40 : 20."},
        {"jaut": "Cik monētu vajag 40 ct, ja ņem tikai 5 ct monētas?",
         "atb": ["8"], "padoms": "40 : 5."},
        {"jaut": "Cik centu ir 3 monētas pa 20 ct un 1 pa 5 ct?",
         "atb": ["65"], "padoms": "60 + 5."},
        {"jaut": "Cik centu vēl trūkst līdz 80 ct, ja ir 50 + 20 ct?",
         "atb": ["10"], "padoms": "80 − 70."},
    ], pamats=4),

    Petijums("Atrodi visus veidus",
             vajag="monētu modeļi vai uzzīmēti apļi",
             soli=[
                 "Izvēlies summu: 30 ct.",
                 "Atrodi veidu ar vismazāk monētām.",
                 "Atrodi veidu ar visvairāk monētām.",
                 "Pieraksti vēl trīs veidus pa vidu.",
             ],
             secinajums="Ar vienu summu var būt daudz komplektu - bet mazākais "
                        "monētu skaits ir tikai viens."),

    Zimejums("Monētu vērtības",
             restis([[1, 2, 5, 10, 20, 50]],
                    "eiro centu monētas"),
             paskaidro="Katra nākamā ir apmēram divas vai divarpus reizes "
                       "lielāka - tāpēc summas saliek ērti.",
             ievads="Šīs sešas monētas ir viss, kas vajadzīgs."),

    Varianti("Kurš komplekts der?", [
        {"jaut": "Kurš komplekts dod tieši 55 ct?",
         "opcijas": ["50 + 5", "20 + 20 + 20", "50 + 10", "20 + 10 + 5 + 5"],
         "pareizi": 0, "padoms": "Saskaiti katru variantu."},
        {"jaut": "Cik vismazāk monētu vajag 65 ct?",
         "opcijas": ["3", "4", "5", "2"],
         "pareizi": 0, "padoms": "50 + 10 + 5."},
        {"jaut": "Kuru summu *nevar* samaksāt bez 1 ct monētām?",
         "opcijas": ["33 ct", "35 ct", "40 ct", "55 ct"],
         "pareizi": 0, "padoms": "33 nebeidzas ne ar 0, ne ar 5."},
        {"jaut": "Cik centu ir 2 monētas pa 50 ct?",
         "opcijas": ["100", "52", "70", "150"],
         "pareizi": 0, "padoms": "Tas ir viens eiro."},
    ], pamats=4),

    Pasaule("Kā samaksāt bez atlikuma?",
            Ievadi("", [
                {"jaut": "Prece maksā 45 ct. Cik vismazāk monētu vajag?",
                 "atb": ["3"], "padoms": "20 + 20 + 5."},
                {"jaut": "Prece maksā 72 ct. Cik vismazāk monētu vajag?",
                 "atb": ["4"], "padoms": "50 + 20 + 2."},
                {"jaut": "Iedeva 1 eiro (100 ct) par preci, kas maksā 65 ct. "
                         "Cik centu jāatdod atpakaļ?",
                 "atb": ["35"], "padoms": "100 − 65."},
                {"jaut": "Cik vismazāk monētu vajag 35 ct atlikumam?",
                 "atb": ["3"], "padoms": "20 + 10 + 5."},
            ]),
            pavediens="veikals",
            konteksts="Kasē atlikumu vienmēr izdod ar vismazāko monētu "
                      "skaitu - citādi kase paliktu tukša.",
            kapec="Tāpēc, maksājot ar precīzu summu, rinda kustas ātrāk."),

    Kopsavilkums([
        "Zinu eiro centu monētu vērtības.",
        "Samaksāju doto summu vairākos veidos.",
        "Atrodu veidu ar vismazāko monētu skaitu.",
        "Izrēķinu atlikumu no lielākas naudas zīmes.",
    ]),

    Majas([
        "Atrodi mājās monētas un saliec ar tām 65 ct divos veidos.",
        "Izrēķini, cik atlikuma saņemsi no 1 eiro par 38 ct preci.",
        "Pastāsti mājiniekiem, kāpēc kasē izdod vismazāko monētu skaitu.",
    ]),
]
