# -*- coding: utf-8 -*-
"""6. klase, 1. stunda: «Ko nozīmē «divi pret trīs»?»

Gada pirmā stunda. Attiecība nāk nevis no definīcijas, bet no teksta, kādu
skolēns tiešām redz - uz krāsas bundžas, receptē, būvlaukumā. Šeit vēl nekas
netiek dalīts; vienīgais uzdevums ir saprast, ko pieraksts pasaka par diviem
lielumiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Ko nozīmē «divi pret trīs»?"

MERKIS = ("Mācīsimies izlasīt tekstu, kurā ir attiecība, un izstāstīt saviem "
          "vārdiem, ko tā pasaka par abiem lielumiem.")

SATURS = [
    Sakums("Kas rakstīts uz krāsas bundžas?",
           fakti=["«Krāsu un ūdeni maisa attiecībā 2 pret 3.»",
                  "Tur nav pateikts, cik daudz krāsas ņemt.",
                  "Toties pateikts, cik ūdens jāņem katrai krāsas daļai."]),

    Doma("Attiecība stāsta par daļām, ne par daudzumu",
         "«2 pret 3» nozīmē: uz katrām 2 vienas lieluma daļām nāk 3 otra "
         "daļas.",
         soli=[
             "Atrodi tekstā abus lielumus - kas ar ko tiek salīdzināts.",
             "Nosaki, cik daļu pienākas katram.",
             "Izstāsti to ar vārdiem «uz katrām ... nāk ...».",
             "Pārbaudi, vai secība nav apmainīta: 2 pret 3 nav 3 pret 2.",
         ],
         pieze="Tieši tāpēc attiecība der jebkuram daudzumam: ar to pašu "
               "pierakstu var pagatavot gan spaini, gan mucu krāsas - mainās "
               "daļas lielums, ne attiecība."),

    Paraugs("Izlasi tekstu",
            uzd="«Javu gatavo, cementu un smiltis ņemot attiecībā 1 pret 4.» "
                "Ko tas nozīmē?",
            soli=[
                ("Salīdzina cementu un smiltis",
                 "Vispirms - kuri divi lielumi te satiekas."),
                ("Cementam 1 daļa, smiltīm 4 daļas",
                 "Skaitļu secība atbilst vārdu secībai."),
                ("Uz katru cementa spaini nāk 4 spaiņi smilšu",
                 "Daļa var būt spainis, kauss vai tonna - galvenais, ka viena "
                 "un tā pati mērtrauka."),
            ],
            atbilde="smilšu ņem četrreiz vairāk nekā cementa"),

    Ievadi("Ko pasaka attiecība?", [
        {"jaut": "Krāsu un ūdeni maisa 2 pret 3. Ņem 4 l krāsas. Cik litru "
                 "ūdens?",
         "atb": ["6"], "padoms": "Krāsas divreiz vairāk nekā 2, tātad arī "
                                 "ūdens divreiz vairāk nekā 3."},
        {"jaut": "Tā pati attiecība. Ņem 10 l krāsas. Cik litru ūdens?",
         "atb": ["15"], "padoms": "10 ir pieci pāri; 3 · 5."},
        {"jaut": "Cementu un smiltis ņem 1 pret 4. Ņem 3 spaiņus cementa. "
                 "Cik spaiņu smilšu?",
         "atb": ["12"], "padoms": "4 · 3."},
        {"jaut": "Tā pati attiecība. Ir 20 spaiņi smilšu. Cik spaiņu "
                 "cementa?",
         "atb": ["5"], "padoms": "20 : 4."},
        {"jaut": "Attiecībā 2 pret 3 - cik daļu ir kopā?",
         "atb": ["5"], "padoms": "2 + 3."},
        {"jaut": "Attiecībā 1 pret 4 - cik daļu ir kopā?",
         "atb": ["5"], "padoms": "1 + 4."},
    ], pamats=4,
        ievads="Attiecība paliek tā pati - mainās tikai daļas lielums."),

    Varianti("Vai saproti tekstu?", [
        {"jaut": "«Sulu un ūdeni maisa 1 pret 5.» Kā to pateikt saviem "
                 "vārdiem?",
         "opcijas": ["Uz 1 glāzi sulas nāk 5 glāzes ūdens",
                     "Uz 5 glāzēm sulas nāk 1 glāze ūdens",
                     "Sulas un ūdens ir vienādi daudz",
                     "Kopā jābūt 6 glāzēm"],
         "pareizi": 0,
         "padoms": "Skaitļu secība seko vārdu secībai."},
        {"jaut": "Vai attiecība 2 pret 3 ir tas pats, kas 3 pret 2?",
         "opcijas": ["Nē, secība maina nozīmi",
                     "Jā, tas ir viens un tas pats",
                     "Jā, ja skaitļi ir mazi",
                     "Nē, jo 3 ir lielāks"],
         "pareizi": 0,
         "padoms": "Vienā gadījumā vairāk ir viena, otrā - otra."},
        {"jaut": "Kāpēc uz bundžas neraksta, cik litru krāsas ņemt?",
         "opcijas": ["Attiecība der jebkuram daudzumam",
                     "Litri nav svarīgi",
                     "To aizmirsa uzrakstīt",
                     "Krāsu vienmēr ņem 2 litrus"],
         "pareizi": 0,
         "padoms": "Vienam vajag spaini, citam mucu."},
        {"jaut": "«Skolā uz 3 meitenēm ir 2 zēni.» Kuru attiecību tas "
                 "apraksta?",
         "opcijas": ["Meitenes pret zēniem 3 pret 2",
                     "Zēni pret meitenēm 3 pret 2",
                     "Meitenes pret visiem 3 pret 2",
                     "Zēni pret visiem 2 pret 3"],
         "pareizi": 0,
         "padoms": "Vispirms nosauc to, par ko teikums sākas."},
    ], pamats=4),

    Pasaule("Cik daudz materiāla vajag?",
            Ievadi("", [
                {"jaut": "Java: cements un smiltis 1 pret 4. Cementa ir "
                         "2 maisi. Cik maisu smilšu?",
                 "atb": ["8"], "padoms": "4 · 2."},
                {"jaut": "Flīžu līme: pulveris un ūdens 3 pret 1. Pulvera "
                         "9 kg. Cik kilogramu ūdens?",
                 "atb": ["3"], "padoms": "9 : 3."},
                {"jaut": "Krāsa un šķīdinātājs 5 pret 1. Krāsas 10 l. Cik "
                         "litru šķīdinātāja?",
                 "atb": ["2"], "padoms": "10 : 5."},
                {"jaut": "Betons: cements, smiltis, grants 1 pret 2 pret 4. "
                         "Cementa 3 spaiņi. Cik spaiņu grants?",
                 "atb": ["12"], "padoms": "4 · 3."},
            ]),
            pavediens="maja",
            konteksts="Uz katra maisa un bundžas ir attiecība, nevis recepte "
                      "konkrētam istabas lielumam.",
            kapec="Attiecība pasaka, cik daļu katram - daļas lielumu izvēlies "
                  "pats."),

    Kopsavilkums([
        "Izlasu tekstu ar attiecību un izstāstu to saviem vārdiem.",
        "Zinu, ka attiecība runā par daļām, nevis par daudzumu.",
        "Ievēroju secību: 2 pret 3 nav tas pats, kas 3 pret 2.",
        "Aprēķinu otro lielumu, ja zinu vienu un attiecību.",
    ]),

    Majas([
        "Atrodi mājās iepakojumu, uz kura rakstīta attiecība, un pieraksti "
        "to.",
        "Izstāsti kādam, ko tā nozīmē, nelietojot vārdu «attiecība».",
        "Padomā, kas notiktu, ja abus skaitļus samainītu vietām.",
    ]),
]
