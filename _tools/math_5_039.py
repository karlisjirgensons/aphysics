# -*- coding: utf-8 -*-
"""5. klase, 39. stunda: «Kā atrast mazāko kopīgo dalāmo?»

Divi paņēmieni vienam uzdevumam: virkņu uzrakstīšana un salikšana no
pirmreizinātājiem. Stundas jēga ir tos salīdzināt - pirmais ir drošs un lēns,
otrs ātrs, bet prasa 34. stundas prasmi. Izvēle atkal paliek skolēnam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā atrast mazāko kopīgo dalāmo?"

MERKIS = ("Iemācīsimies noteikt mazāko kopīgo dalāmo ar diviem paņēmieniem "
          "un salīdzināt tos.")

SATURS = [
    Sakums("Divi ceļi līdz mazākajam kopīgajam dalāmajam",
           fakti=["8 un 12: var uzrakstīt abas virknes un meklēt sakritību.",
                  "Var arī salikt to no pirmreizinātājiem.",
                  "Abi ceļi dod 24 - bet ne vienādi ātri."]),

    Doma("Ņem katru pirmreizinātāju tik reižu, cik daudz to ir",
         "Mazākais kopīgais dalāmais satur visus abu skaitļu "
         "pirmreizinātājus - katru tik reižu, cik daudz to ir vairāk.",
         soli=[
             "Sadali abus skaitļus pirmreizinātājos.",
             "Paskaties, cik reižu katrs pirmskaitlis parādās katrā "
             "sadalījumā.",
             "No katra pirmskaitļa paņem lielāko skaitu.",
             "Sareizini paņemtos - tas ir mazākais kopīgais dalāmais.",
         ],
         pieze="8 = 2 · 2 · 2 un 12 = 2 · 2 · 3. Divnieku vairāk ir "
               "astotniekā - trīs; trijnieks ir viens. Tātad 2 · 2 · 2 · 3 = "
               "24."),

    Paraugs("Divi paņēmieni skaitļiem 8 un 12",
            uzd="Atrodi 8 un 12 mazāko kopīgo dalāmo divos veidos.",
            soli=[
                ("1. ceļš: 8, 16, 24 un 12, 24",
                 "Virknes sakrīt pie 24."),
                ("2. ceļš: 8 = 2 · 2 · 2, 12 = 2 · 2 · 3",
                 "Sadalām pirmreizinātājos."),
                ("Ņemam trīs divniekus un vienu trijnieku",
                 "No katra pirmskaitļa - lielāko skaitu."),
                ("2 · 2 · 2 · 3 = 24",
                 "Tāda pati atbilde kā pirmajā ceļā."),
            ],
            atbilde="24"),

    Ievadi("Atrodi mazāko kopīgo dalāmo", [
        {"jaut": "8 un 12. Kāds ir mazākais kopīgais dalāmais?",
         "atb": ["24"], "padoms": "2 · 2 · 2 · 3."},
        {"jaut": "6 un 10?", "atb": ["30"], "padoms": "2 · 3 · 5."},
        {"jaut": "9 un 12?", "atb": ["36"], "padoms": "2 · 2 · 3 · 3."},
        {"jaut": "4 un 5?", "atb": ["20"],
         "padoms": "Kopīgu dalītāju nav, tāpēc 4 · 5."},
        {"jaut": "10 un 15?", "atb": ["30"], "padoms": "2 · 3 · 5."},
        {"jaut": "6 un 18?", "atb": ["18"],
         "padoms": "18 jau dalās ar 6."},
        {"jaut": "14 un 21?", "atb": ["42"], "padoms": "2 · 3 · 7."},
        {"jaut": "2, 3 un 4 - visiem trim kopā?", "atb": ["12"],
         "padoms": "2 · 2 · 3."},
    ], pamats=4,
        ievads="Izvēlies paņēmienu pats - abi dod vienu atbildi."),

    Varianti("Kurš paņēmiens kad ir labāks?", [
        {"jaut": "Kad ērtāk rakstīt virknes?",
         "opcijas": ["Kad skaitļi ir mazi", "Vienmēr",
                     "Kad skaitļi ir lieli", "Nekad"],
         "pareizi": 0,
         "padoms": "6 un 8 virknes ir īsas."},
        {"jaut": "Kad ērtāk lietot pirmreizinātājus?",
         "opcijas": ["Kad skaitļi ir lieli", "Kad skaitļi ir mazi",
                     "Kad viens ir pirmskaitlis", "Nekad"],
         "pareizi": 0,
         "padoms": "36 un 48 virknes būtu garas."},
        {"jaut": "Kāpēc 8 un 12 mazākais kopīgais dalāmais nav 96?",
         "opcijas": ["96 ir kopīgais dalāmais, bet ne mazākais",
                     "96 nedalās ar 8",
                     "96 nedalās ar 12",
                     "96 vispār nav kopīgais dalāmais"],
         "pareizi": 0,
         "padoms": "8 · 12 = 96, bet 24 arī derēja."},
        {"jaut": "Kad divu skaitļu mazākais kopīgais dalāmais ir lielākais no "
                 "tiem?",
         "opcijas": ["Kad viens dalās ar otru, piemēram 6 un 18",
                     "Nekad", "Kad abi ir pāra", "Kad abi ir pirmskaitļi"],
         "pareizi": 0,
         "padoms": "18 jau dalās ar 6."},
    ], pamats=4),

    Pasaule("Kad abi reisi sākas vienlaikus?",
            Ievadi("", [
                {"jaut": "Viens autobuss iet ik pēc 8 minūtēm, otrs ik pēc "
                         "12. Pēc cik minūtēm abi sakritīs?",
                 "atb": ["24"], "padoms": "8 un 12 mazākais kopīgais "
                                          "dalāmais."},
                {"jaut": "Lidmašīnas ceļo ik pēc 6 un ik pēc 10 dienām. Pēc "
                         "cik dienām abas būs vienā dienā?",
                 "atb": ["30"], "padoms": "2 · 3 · 5."},
                {"jaut": "Vilciens ik pēc 9 stundām, prāmis ik pēc "
                         "12 stundām. Pēc cik stundām abi sakritīs?",
                 "atb": ["36"], "padoms": "2 · 2 · 3 · 3."},
                {"jaut": "Ja abi reisi iet ik pēc 6 un ik pēc 18 stundām, pēc "
                         "cik stundām tie sakrīt?",
                 "atb": ["18"], "padoms": "18 jau dalās ar 6."},
            ]),
            pavediens="celojums",
            konteksts="Sarakstos laiki atkārtojas, un ceļotājam svarīgi "
                      "zināt, kad abi savienojumi ir vienā brīdī.",
            kapec="Mazākais kopīgais dalāmais ir pirmā sakritība."),

    Kopsavilkums([
        "Atrodu mazāko kopīgo dalāmo, uzrakstot dalāmo virknes.",
        "Atrodu to arī no sadalījuma pirmreizinātājos.",
        "Salīdzinu abus paņēmienus un izvēlos piemērotāko.",
        "Zinu, kad mazākais kopīgais dalāmais ir viens no pašiem skaitļiem.",
    ]),

    Majas([
        "Atrodi 12 un 18 mazāko kopīgo dalāmo abos veidos.",
        "Izmēri, kurš ceļš tev bija ātrāks.",
        "Atrodi divus skaitļus, kuriem mazākais kopīgais dalāmais ir 60.",
    ]),
]
