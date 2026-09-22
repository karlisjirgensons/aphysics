# -*- coding: utf-8 -*-
"""5. klase, 77. stunda: «Kā attēlot trīs sastāvdaļas?»

Mikrotemata noslēgums. Ar vienu daļu pietiek ar joslu, bet, kad sastāvdaļu
ir trīs, shēmu vairs nevar uzzīmēt uz labu laimi: visām daļām jāietilpst
vienā iedaļā. Tāpēc te atkal parādās kopsaucējs - šoreiz nevis rēķinā, bet
zīmējumā, un atlikumu izrēķina, nevis uzzīmē uz aci.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā attēlot trīs sastāvdaļas?"

MERKIS = ("Mācīsimies veidot shematisku zīmējumu situācijai, kurā ar daļām "
          "raksturotas vairākas sastāvdaļas.")

SATURS = [
    Sakums("Viena josla, trīs gabali",
           zimejums=restis([["3/6", "2/6", "1/6"]],
                           virsraksts="Ceļš, naktsmītne, ēdiens"),
           paraksts="{1|2} + {1|3} + {1|6} = 1 - visa budžeta josla aizpildīta.",
           fakti=["Budžets sadalās trīs daļās ar dažādiem saucējiem.",
                  "Vienā zīmējumā iedaļa var būt tikai viena.",
                  "Tāpēc visas daļas pārraksta ar kopsaucēju."]),

    Doma("Viena iedaļa visām sastāvdaļām",
         "Shēmā visas daļas pārraksta ar kopsaucēju, sadala joslu tik daļās "
         "un katrai sastāvdaļai atvēl tik daļu, cik rāda tās skaitītājs.",
         soli=[
             "Izraksti visu sastāvdaļu daļas.",
             "Atrodi tām kopsaucēju.",
             "Sadali joslu tik vienādās daļās, cik rāda kopsaucējs.",
             "Iezīmē katru sastāvdaļu ar savu skaitītāju.",
             "Atlikumu izrēķini: no 1 atņem visu pārējo.",
         ],
         pieze="Pārbaude ir viena: visu sastāvdaļu daļām kopā jādod tieši "
               "viens vesels. Ja iznāk mazāk, kaut kas nav uzskaitīts; ja "
               "vairāk - kaut kas saskaitīts divreiz."),

    Paraugs("Ceļojuma budžets trīs daļās",
            uzd="Ceļam aiziet {1|2} naudas, naktsmītnei {1|3}, pārējais - "
                "ēdienam. Uzzīmē shēmu un nosaki ēdiena daļu.",
            soli=[
                ("Kopsaucējs ir 6",
                 "6 dalās ar 2 un 3."),
                ("{1|2} = {3|6} un {1|3} = {2|6}",
                 "Abas daļas ar vienu saucēju."),
                ("{3|6} + {2|6} = {5|6}",
                 "Tik aizņem ceļš un naktsmītne kopā."),
                ("1 - {5|6} = {1|6}",
                 "Atlikums ēdienam."),
                ("Josla: 3 daļas, 2 daļas, 1 daļa",
                 "Shēma no sešām vienādām daļām."),
            ],
            atbilde="Ēdienam paliek {1|6} budžeta"),

    Ievadi("Cik paliek atlikumā?", [
        {"jaut": "{1|2} + {1|3} = ? Atbildi raksti kā a/b.",
         "atb": ["5/6"], "padoms": "{3|6} + {2|6}."},
        {"jaut": "Cik paliek atlikumā no viena vesela? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/6"], "padoms": "1 - {5|6}."},
        {"jaut": "{1|4} + {1|2} = ? Atbildi raksti kā a/b.",
         "atb": ["3/4"], "padoms": "{1|4} + {2|4}."},
        {"jaut": "Cik paliek atlikumā no viena vesela? Atbildi raksti kā "
                 "a/b.",
         "atb": ["1/4"], "padoms": "1 - {3|4}."},
        {"jaut": "{2|5} + {3|10} = ? Atbildi raksti kā a/b.",
         "atb": ["7/10"], "padoms": "{4|10} + {3|10}."},
        {"jaut": "Cik paliek atlikumā no viena vesela? Atbildi raksti kā "
                 "a/b.",
         "atb": ["3/10"], "padoms": "1 - {7|10}."},
        {"jaut": "Cik daļās jāsadala josla, ja sastāvdaļas ir {1|2}, {1|3} "
                 "un {1|6}?",
         "atb": ["6"], "padoms": "Kopsaucējs."},
        {"jaut": "Cik daļās jāsadala josla, ja sastāvdaļas ir {1|2}, {1|4} "
                 "un {1|8}?",
         "atb": ["8"], "padoms": "8 dalās ar 2, 4 un 8."},
    ], pamats=4,
        ievads="Vispirms kopsaucējs, tad shēma, un atlikumu vienmēr "
               "izrēķina."),

    Zimejums("Kas paliek ēdienam",
             dala(6, 5, "5/6 jau izlietotas"),
             paskaidro="Piecas sestdaļas aizņem ceļš un naktsmītne; tukšā "
                       "sestdaļa ir ēdiena daļa.",
             ievads="Atlikumu shēmā redz kā tukšo gabalu."),

    Varianti("Kā veido shēmu?", [
        {"jaut": "Cik daļās sadala joslu, ja sastāvdaļas ir {1|2}, {1|3} un "
                 "atlikums?",
         "opcijas": ["6", "5", "3", "2"],
         "pareizi": 0,
         "padoms": "Kopsaucējs saucējiem 2 un 3."},
        {"jaut": "Visu sastāvdaļu daļām kopā jādod...",
         "opcijas": ["Viens vesels", "Kopsaucējs", "Nulle", "Divi"],
         "pareizi": 0,
         "padoms": "Visa josla ir viens."},
        {"jaut": "Kā aprēķina atlikumu?",
         "opcijas": ["No 1 atņem pārējo daļu summu",
                     "Saskaita visas daļas",
                     "Izvēlas lielāko daļu",
                     "Uzzīmē uz aci"],
         "pareizi": 0,
         "padoms": "Atlikums ir tas, kas nav uzskaitīts."},
        {"jaut": "Sastāvdaļas ir {1|4}, {1|4} un {1|4}. Cik ir atlikums?",
         "opcijas": ["{1|4}", "{3|4}", "0", "1"],
         "pareizi": 0,
         "padoms": "1 - {3|4}."},
        {"jaut": "Ja daļu summa iznāk lielāka par 1, tas nozīmē...",
         "opcijas": ["Kaut kas saskaitīts divreiz", "Viss ir pareizi",
                     "Kopsaucējs par mazu", "Josla par īsu"],
         "pareizi": 0,
         "padoms": "Vairāk par veselo nevar būt."},
        {"jaut": "Kāpēc shēmā iedaļa var būt tikai viena?",
         "opcijas": ["Citādi gabalus nevar salīdzināt",
                     "Citādi zīmējums ir liels",
                     "Citādi trūkst vietas",
                     "Var būt arī vairākas"],
         "pareizi": 0,
         "padoms": "Vienāda iedaļa - vienādi gabali."},
    ], pamats=4),

    Pasaule("Kur aiziet ceļojuma nauda?",
            Ievadi("", [
                {"jaut": "Ceļam {1|3}, naktsmītnei {1|4}, pārējais ēdienam. "
                         "Kāds ir kopsaucējs?",
                 "atb": ["12"], "padoms": "12 dalās ar 3 un 4."},
                {"jaut": "Cik divpadsmitdaļu aizņem ceļš un naktsmītne kopā?",
                 "atb": ["7"], "padoms": "{4|12} + {3|12}."},
                {"jaut": "Cik divpadsmitdaļu paliek ēdienam?",
                 "atb": ["5"], "padoms": "12 - 7."},
                {"jaut": "Viss budžets ir 240 €. Cik eiro paliek ēdienam?",
                 "atb": ["100"], "padoms": "240 : 12 · 5."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojuma budžetu plāno pa daļām, un atlikums ir tas, "
                      "par ko ēd.",
            kapec="Shēma uzreiz parāda, vai kādai sastāvdaļai naudas "
                  "nepietiek."),

    Kopsavilkums([
        "Atrodu visām sastāvdaļām kopsaucēju.",
        "Sadalu shēmas joslu tik daļās, cik rāda kopsaucējs.",
        "Iezīmēju katru sastāvdaļu ar savu skaitītāju.",
        "Aprēķinu atlikumu, atņemot pārējo daļu summu no viena.",
    ]),

    Majas([
        "Uzzīmē shēmu dienai: {1|3} miegam, {1|4} skolai, pārējais brīvs.",
        "Aprēķini brīvā laika daļu un pārbaudi, vai summa ir 1.",
        "Atrodi mājās situāciju ar trim daļām un uzzīmē tai shēmu.",
    ]),
]
