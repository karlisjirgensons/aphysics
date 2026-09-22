# -*- coding: utf-8 -*-
"""5. klase, 153. stunda: «Ko diagramma stāsta un ko ne?»

Zīmēt diagrammu skolēns jau prot; te viņš kļūst par lasītāju un kritiķi.
Sektoru diagramma parāda daļas, bet nekad - skaitu: no tās nevar uzzināt,
vai aptaujāti 20 vai 2000 cilvēku. Tieši šo robežu stunda arī iezīmē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, rinkis)

TEMA = "Ko diagramma stāsta un ko ne?"

MERKIS = ("Mācīsimies nolasīt informāciju no sektoru diagrammas, formulēt "
          "secinājumus un atrast kļūdas attēlojumos.")

SATURS = [
    Sakums("Puse riņķa - bet cik cilvēku?",
           zimejums=rinkis(sektors=180, virsraksts="50 % izvēlējās futbolu"),
           paraksts="Diagramma nepasaka, vai tie ir 10 vai 1000 cilvēku.",
           fakti=["Sektors rāda daļu no visiem.",
                  "Skaitu tas nerāda nemaz.",
                  "Tāpēc pie diagrammas vienmēr raksta kopskaitu."]),

    Doma("Diagramma rāda daļas, ne skaitu",
         "No sektoru diagrammas var nolasīt, kura daļa ir lielāka un cik "
         "procentu tā ir; aptaujāto skaitu no tās uzzināt nevar.",
         soli=[
             "Paskaties, kurš sektors ir lielākais.",
             "Novērtē katra sektora daļu: ceturtdaļa, puse, vairāk vai mazāk.",
             "Pārbaudi, vai visi procenti kopā dod 100 %.",
             "Ja dots kopskaits, aprēķini katras daļas vērtību.",
             "Neizdari secinājumus par skaitu, ja kopskaits nav dots.",
         ],
         pieze="Divas diagrammas var izskatīties vienādas, bet aiz tām var "
               "stāvēt 20 un 2000 cilvēku. Tāpēc godīga diagramma vienmēr "
               "nosauc, cik cilvēku aptaujāti."),

    Paraugs("Ko var un ko nevar uzzināt",
            uzd="Diagrammā: futbols 50 %, basketbols 25 %, volejbols 25 %. "
                "Kādus secinājumus var izdarīt?",
            soli=[
                ("Futbolu izvēlējās vislielākā daļa",
                 "Puse no visiem."),
                ("Basketbolu un volejbolu - vienāda daļa",
                 "Abiem 25 %."),
                ("Futbolu izvēlējās tikpat, cik abus pārējos kopā",
                 "50 % pret 25 % + 25 %."),
                ("Cik cilvēku - nezinām",
                 "Diagramma to nerāda."),
            ],
            atbilde="Par daļām - varam; par skaitu - nevaram"),

    Ievadi("Nolasi no diagrammas", [
        {"jaut": "Sektori ir 50 %, 25 % un 25 %. Cik procentu ir lielākais?",
         "atb": ["50"], "padoms": "Puse riņķa."},
        {"jaut": "Vai visu sektoru procentiem kopā jādod 100? Raksti «jā» "
                 "vai «nē».",
         "atb": ["jā", "ja"], "padoms": "Viss riņķis."},
        {"jaut": "Sektori ir 40 % un 35 %. Cik procentu ir trešais?",
         "atb": ["25"], "padoms": "100 - 75."},
        {"jaut": "Aptaujāti 20 cilvēki, futbolu izvēlējās 50 %. Cik cilvēku "
                 "tas ir?",
         "atb": ["10"], "padoms": "20 : 2."},
        {"jaut": "Aptaujāti 200 cilvēki, futbolu izvēlējās 50 %. Cik cilvēku?",
         "atb": ["100"], "padoms": "200 : 2."},
        {"jaut": "Vai no diagrammas var uzzināt aptaujāto skaitu, ja tas nav "
                 "uzrakstīts? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "Sektori rāda tikai daļas."},
        {"jaut": "Diagrammā sektori ir 60 %, 30 % un 20 %. Vai tas ir "
                 "iespējams?",
         "atb": ["nē", "ne"], "padoms": "Summa ir 110."},
        {"jaut": "Aptaujāti 40 cilvēki, 25 % izvēlējās šahu. Cik cilvēku?",
         "atb": ["10"], "padoms": "40 : 4."},
    ], pamats=4,
        ievads="Vispirms pārbaudi, vai procenti kopā dod 100."),

    Zimejums("Tā pati diagramma, cits kopskaits",
             rinkis(sektors=180, virsraksts="50 % - bet no cik?"),
             paskaidro="Šis sektors var nozīmēt 10 cilvēkus no 20 vai 1000 "
                       "no 2000. Bez kopskaita abas nozīmes ir vienlīdz "
                       "iespējamas.",
             ievads="Viena un tā pati bilde, divas dažādas nozīmes."),

    Varianti("Kur diagramma maldina?", [
        {"jaut": "Ko sektoru diagramma rāda?",
         "opcijas": ["Daļas no visiem", "Cilvēku skaitu",
                     "Laiku", "Naudu"],
         "pareizi": 0,
         "padoms": "Procentus, ne skaitu."},
        {"jaut": "Diagrammā sektori ir 60 %, 30 % un 20 %. Kas nav labi?",
         "opcijas": ["Summa ir 110 %", "Sektoru ir par daudz",
                     "Krāsas ir vienādas", "Viss ir labi"],
         "pareizi": 0,
         "padoms": "Vairāk par veselo nevar būt."},
        {"jaut": "Kas obligāti jāraksta pie diagrammas?",
         "opcijas": ["Aptaujāto skaits", "Zīmētāja vārds",
                     "Datums", "Nekas"],
         "pareizi": 0,
         "padoms": "Citādi daļas neko nepasaka par skaitu."},
        {"jaut": "Divas diagrammas izskatās vienādas. Vai aptaujāto skaits "
                 "ir vienāds?",
         "opcijas": ["Ne vienmēr", "Jā", "Nē, nekad", "To vienmēr zina"],
         "pareizi": 0,
         "padoms": "Daļas var sakrist."},
        {"jaut": "Aptaujāti 40, 25 % izvēlējās šahu. Cik cilvēku?",
         "opcijas": ["10", "25", "4", "15"],
         "pareizi": 0,
         "padoms": "40 : 4."},
        {"jaut": "Kurš secinājums no diagrammas ir pamatots?",
         "opcijas": ["Futbolu izvēlējās lielākā daļa",
                     "Futbolu izvēlējās 100 cilvēki",
                     "Aptauja notika skolā",
                     "Basketbols kļūst populārāks"],
         "pareizi": 0,
         "padoms": "Tikai par daļām."},
    ], pamats=4),

    Pasaule("Ko rāda skolas aptauja?",
            Ievadi("", [
                {"jaut": "Aptaujāti 60 skolēni, 50 % brauc ar autobusu. Cik "
                         "skolēnu?",
                 "atb": ["30"], "padoms": "60 : 2."},
                {"jaut": "25 % nāk kājām. Cik skolēnu tas ir?",
                 "atb": ["15"], "padoms": "60 : 4."},
                {"jaut": "Cik procentu izmanto citu veidu?",
                 "atb": ["25"], "padoms": "100 - 75."},
                {"jaut": "Cik skolēnu tas ir?",
                 "atb": ["15"], "padoms": "60 : 4."},
            ]),
            pavediens="skola",
            konteksts="Pie skolas sienas diagramma izskatās pārliecinoši, "
                      "bet bez kopskaita tā neko nepasaka par cilvēkiem.",
            kapec="Lasīt diagrammu nozīmē zināt arī to, ko tā noklusē."),

    Kopsavilkums([
        "Nolasu no sektoru diagrammas, kura daļa ir lielākā.",
        "Pārbaudu, vai visi procenti kopā dod 100 %.",
        "Aprēķinu daļas vērtību, ja dots kopskaits.",
        "Zinu, ka aptaujāto skaitu no diagrammas uzzināt nevar.",
    ]),

    Majas([
        "Atrodi diagrammu avīzē vai internetā un pieraksti divus "
        "secinājumus.",
        "Pieraksti vienu lietu, ko no tās uzzināt nevar.",
        "Pārbaudi, vai tās procenti kopā dod 100 %.",
    ]),
]
