# -*- coding: utf-8 -*-
"""3. klase, 46. stunda: «Kāds teksts der šai izteiksmei?»

Mikrotemata noslēgums un 40. stundas otrs virziens: tagad dota izteiksme, un
jāizdomā situācija. Iekavas te kļūst par stāsta daļu - (20 + 4) · 3 un
20 + 4 · 3 ir divi pilnīgi dažādi notikumi.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāds teksts der šai izteiksmei?"

MERKIS = ("Veidosim situācijas aprakstu, kas atbilst dotai vairākdarbību "
          "izteiksmei.")

SATURS = [
    Sakums("Kādu stāstu stāsta izteiksme (20 + 4) · 3?",
           zimejums=restis([["(20 + 4) · 3", "vispirms saskaita"],
                            ["20 + 4 · 3", "vispirms reizina"]],
                           "divas izteiksmes, divi stāsti"),
           paraksts="Pirmajā visi kopā dara vienu; otrajā - tikai daži.",
           fakti=["Iekavas stāstā nozīmē: vispirms kaut kas apvienojas.",
                  "Bez iekavām darbība attiecas tikai uz daļu."]),

    Doma("Iekavas stāstā nozīmē «vispirms kopā»",
         "Ja izteiksmē ir iekavas, tad stāstā vispirms kaut ko saliek kopā un "
         "tikai tad ar to kaut ko dara.",
         soli=[
             "Paskaties, kura darbība ir pirmā.",
             "Izdomā, ko šī darbība nozīmē stāstā.",
             "Izdomā, ko ar iegūto rezultātu dara tālāk.",
             "Uzraksti jautājumu, uz kuru atbild visa izteiksme.",
         ],
         pieze="Pārbaudi sevi: atrisini savu stāstu no jauna un salīdzini ar "
               "izteiksmes vērtību. Ja tās atšķiras, stāsts neder."),

    Paraugs("Kāds stāsts der izteiksmei 50 − 4 · 8?",
            uzd="Izdomā situāciju, kurā jāizrēķina 50 − 4 · 8.",
            soli=[
                ("Pirmā darbība ir 4 · 8",
                 "Tātad stāstā vispirms kaut kas notiek četras reizes pa "
                 "astoņi."),
                ("«Kabatā bija 50 ct, nopirka 4 preces pa 8 ct.»",
                 "Situācija, kurā abi skaitļi ir dabiski."),
                ("«Cik naudas palika?»",
                 "Jautājums, uz kuru atbild visa izteiksme; 50 − 32 = 18."),
            ],
            atbilde="18 ct"),

    Ievadi("Atrisini stāstu", [
        {"jaut": "«Kabatā 50 ct, nopirka 4 preces pa 8 ct. Cik palika?»",
         "atb": ["18"], "padoms": "50 − 32."},
        {"jaut": "«20 zēni un 4 meitenes, katram 3 grāmatas. Cik grāmatu?»",
         "atb": ["72"], "padoms": "(20 + 4) · 3."},
        {"jaut": "«20 zēniem un vēl 4 meitenēm pa 3 grāmatām. Cik grāmatu "
                 "kopā, ja zēniem katram viena?»",
         "atb": ["32"], "padoms": "20 + 4 · 3."},
        {"jaut": "«36 ābolus sadala 6 bērniem, katrs apēd 2. Cik katram "
                 "palika?»",
         "atb": ["4"], "padoms": "36 : 6 − 2."},
        {"jaut": "«7 kastes pa 6 olām, 5 saplīsa. Cik palika?»",
         "atb": ["37"], "padoms": "7 · 6 − 5."},
        {"jaut": "«(15 + 5) bērni 4 grupās. Cik vienā grupā?»",
         "atb": ["5"], "padoms": "20 : 4."},
    ], pamats=4),

    Petijums("Uzraksti stāstu izteiksmei",
             vajag="lapa un zīmulis",
             soli=[
                 "Izvēlies vienu izteiksmi: (12 + 8) · 4 vai 12 + 8 · 4.",
                 "Uzraksti situāciju, kurā tā rodas.",
                 "Atrisini savu stāstu un salīdzini ar izteiksmes vērtību.",
                 "Iedod stāstu klasesbiedram un lūdz uzrakstīt izteiksmi.",
             ],
             secinajums="Ja klasesbiedrs uzrakstīja to pašu izteiksmi, stāsts "
                        "ir skaidrs."),

    Zimejums("Divi stāsti vienai formai",
             restis([["(20 + 4) · 3", "visiem 24 bērniem pa 3 grāmatām"],
                     ["20 + 4 · 3", "20 grāmatas un vēl 4 bērniem pa 3"]],
                    "iekavas maina stāstu"),
             paskaidro="Pirmajā stāstā reizina visu grupu, otrajā - tikai tās "
                       "daļu.",
             ievads="Salīdzini abus stāstus."),

    Varianti("Kurš teksts der izteiksmei?", [
        {"jaut": "Kurš teksts der izteiksmei (30 − 6) : 4?",
         "opcijas": ["No 30 ābolu 6 apēda, pārējos sadalīja 4 bērniem",
                     "30 ābolus sadalīja 6 bērniem, katrs apēda 4",
                     "30 ābolu bija 6 kastēs pa 4",
                     "30 ābolu un vēl 6 sadalīja 4 bērniem"],
         "pareizi": 0, "padoms": "Vispirms atņem, tad dala."},
        {"jaut": "Kurš teksts der izteiksmei 5 · 8 + 3?",
         "opcijas": ["5 kastes pa 8 olām un vēl 3 olas",
                     "5 kastes pa 11 olām", "5 kastes pa 8, no katras 3 izņēma",
                     "8 kastes pa 5 olām mīnus 3"],
         "pareizi": 0, "padoms": "Vispirms reizina, tad pieskaita."},
        {"jaut": "Kurš teksts der izteiksmei 5 · (8 − 3)?",
         "opcijas": ["5 kastēs bija pa 8 olām, no katras izņēma 3",
                     "5 kastes pa 8 olām, 3 izņēma",
                     "5 olas un vēl 8 mīnus 3", "8 kastes pa 5 olām"],
         "pareizi": 0, "padoms": "Iekavas attiecas uz vienu kasti."},
        {"jaut": "Kā pārbaudīt savu stāstu?",
         "opcijas": ["Atrisināt to un salīdzināt ar izteiksmes vērtību",
                     "Pārlasīt to skaļi", "Pārrakstīt skaistāk",
                     "Nekā"],
         "pareizi": 0, "padoms": "Vērtībām jāsakrīt."},
    ], pamats=4),

    Pasaule("Uzraksti stāstu par atmiņu",
            Ievadi("", [
                {"jaut": "«Telefonā 64 MB brīvi, lejupielādēja 3 failus pa "
                         "8 MB. Cik palika?»",
                 "atb": ["40"], "padoms": "64 − 24."},
                {"jaut": "«(12 + 8) MB sadalīja 4 mapēs. Cik vienā mapē?»",
                 "atb": ["5"], "padoms": "20 : 4."},
                {"jaut": "«6 mapes, katrā bija 10 MB, no katras dzēsa 3 MB. "
                         "Cik palika kopā?»",
                 "atb": ["42"], "padoms": "6 · (10 − 3)."},
                {"jaut": "«6 mapes pa 10 MB, kopā dzēsa 3 MB. Cik palika?»",
                 "atb": ["57"], "padoms": "6 · 10 − 3."},
            ]),
            pavediens="dati",
            konteksts="Pēdējie divi stāsti izskatās gandrīz vienādi, bet "
                      "atbildes atšķiras par 15 MB.",
            kapec="Tieši tāpēc uzdevumā katrs vārds ir svarīgs."),

    Kopsavilkums([
        "Veidoju situācijas aprakstu dotai izteiksmei.",
        "Zinu, ko stāstā nozīmē iekavas.",
        "Pārbaudu savu stāstu, salīdzinot atbildes.",
        "Atpazīstu, kura izteiksme atbilst dotajam tekstam.",
    ]),

    Majas([
        "Uzraksti stāstu izteiksmei 40 − 3 · 9.",
        "Uzraksti stāstu izteiksmei (40 − 3) · 2.",
        "Iedod abus mājiniekiem un pārbaudi, vai viņi uzrakstīja tās pašas "
        "izteiksmes.",
    ]),
]
