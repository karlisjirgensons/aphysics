# -*- coding: utf-8 -*-
"""4. klase, 20. stunda: «Kādus jautājumus var uzdot?»

Datu lasīšanas otra puse - uzdot jautājumus. No tabulas var uzzināt
vairāk, nekā tajā uzrakstīts: summu, starpību, vislielāko, izmaiņu. Bet
dažus jautājumus no tās atbildēt nevar - un to arī jāprot pateikt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas,
                         restis)

TEMA = "Kādus jautājumus var uzdot?"

MERKIS = ("Formulēsim secinājumus un jautājumus par tabulā vai diagrammā "
          "doto informāciju.")

SATURS = [
    Sakums("Kas notiek skolas ēdnīcā?",
           zimejums=restis([["diena", "zupa", "pica", "salāti"],
                            ["pirmd.", 120, 340, 85],
                            ["otrd.", 150, 290, 110],
                            ["trešd.", 90, 410, 95]],
                           "pārdotās porcijas"),
           fakti=["No tabulas var uzzināt vairāk, nekā tajā rakstīts.",
                  "Bet ne visu - piemēram, vai pica bija garšīga."]),

    Doma("Labs jautājums ir tāds, uz kuru dati atbild",
         "No datiem var jautāt par lielāko, mazāko, summu, starpību un "
         "izmaiņu.",
         soli=[
             "Kurš ir lielākais vai mazākais? (salīdzina)",
             "Cik pavisam? (saskaita)",
             "Par cik vairāk? (atņem)",
             "Kā mainījās? (salīdzina dienas vai mēnešus)",
         ],
         pieze="«Kāpēc trešdien zupu ēda maz?» - uz to tabula neatbild, "
               "tas ir jāuzzina citur."),

    Paraugs("Viena tabula - trīs atbildes",
            uzd="Cik picas porciju pārdeva trijās dienās kopā?",
            soli=[
                ("340 + 290 + 410", "Jautājums «cik pavisam» - summa."),
                ("340 + 290 + 410 = 1040", None),
            ],
            atbilde="1040 porcijas"),

    Ievadi("Atbildi no tabulas", [
        {"jaut": "Cik zupas porciju pārdeva otrdien un trešdien kopā?",
         "atb": ["240"], "padoms": "150 + 90."},
        {"jaut": "Par cik trešdien picu pārdeva vairāk nekā otrdien?",
         "atb": ["120"], "padoms": "410 − 290."},
        {"jaut": "Cik porciju pavisam pārdeva pirmdien?",
         "atb": ["545"], "padoms": "120 + 340 + 85."},
        {"jaut": "Cik salātu porciju pārdeva trijās dienās?",
         "atb": ["290"], "padoms": "85 + 110 + 95."},
    ]),

    Varianti("Vai tabula atbild?", [
        {"jaut": "«Kurā dienā pārdeva visvairāk picas?»",
         "opcijas": ["jā, atbild", "nē, neatbild"], "pareizi": 0,
         "padoms": "Salīdzini picu kolonnu."},
        {"jaut": "«Kura skolēna mīļākais ēdiens ir zupa?»",
         "opcijas": ["nē, neatbild", "jā, atbild"], "pareizi": 0,
         "padoms": "Tabulā nav vārdu."},
        {"jaut": "«Cik maksā viena pica?»",
         "opcijas": ["nē, neatbild", "jā, atbild"], "pareizi": 0,
         "padoms": "Cenu tabulā nav."},
        {"jaut": "«Vai salātus otrdien pārdeva vairāk nekā pirmdien?»",
         "opcijas": ["jā, atbild", "nē, neatbild"], "pareizi": 0,
         "padoms": "110 > 85."},
    ], pamats=4),

    Zimejums("Picas pa dienām",
             kolonnas([("pirmd.", 340), ("otrd.", 290), ("trešd.", 410)]),
             paskaidro="Diagrammā uzreiz redz, ka trešdiena bija rekords, "
                       "bet otrdiena - vājākā.",
             ievads="Tā pati informācija - tikai attēlā."),

    Pasaule("Ēdnīcas pavāra jautājumi",
            Varianti("", [
                {"jaut": "Pavārs grib zināt, cik picu pagatavot ceturtdien. "
                         "Kurš dati visvairāk palīdz?",
                 "opcijas": ["picu skaits iepriekšējās dienās",
                             "zupas skaits pirmdien",
                             "salātu skaits otrdien"],
                 "pareizi": 0, "padoms": "Vajag tieši picu datus."},
                {"jaut": "Kurš secinājums pareizs?",
                 "opcijas": ["Picu katru dienu pārdod vairāk nekā zupu",
                             "Salātus ēd visvairāk",
                             "Zupu nepērk neviens"],
                 "pareizi": 0, "padoms": "Salīdzini katru rindu."},
                {"jaut": "Kurš jautājums *nav* atbildams no tabulas?",
                 "opcijas": ["Cik skolēnu ēda brokastis?",
                             "Cik zupas porciju pārdeva otrdien?",
                             "Kurā dienā pārdeva mazāk salātu?"],
                 "pareizi": 0, "padoms": "Par brokastīm datu nav."},
            ]),
            pavediens="skola",
            konteksts="Ēdnīca plāno produktus pēc tā, ko pārdeva "
                      "iepriekšējās dienās.",
            kapec="Labi jautājumi pārvērš skaitļus lēmumos."),

    Kopsavilkums([
        "Formulēju jautājumus, uz kuriem dati atbild.",
        "Pamanu jautājumus, uz kuriem dati neatbild.",
        "Izdaru secinājumu no tabulas vai diagrammas.",
    ]),

    Majas([
        "Pieraksti trīs dienas, ko ēdi vakariņās, un uzdod divus jautājumus "
        "par to.",
        "Izdomā vienu jautājumu, uz kuru tava tabula neatbild.",
        "Paprasi mājiniekiem, kā viņi izlemj, ko pirkt veikalā.",
    ]),
]
