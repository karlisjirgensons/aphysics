# -*- coding: utf-8 -*-
"""4. klase, 22. stunda: «Kāds uzdevums der šim zīmējumam?»

4.1. temata pēdējā stunda pirms PD. Parasti skolēns saņem tekstu un zīmē
shēmu; te ir otrādi - ir shēma, jāizdomā teksts. Tā pārbauda, vai
«par tik vairāk», «kopā» un «atlika» ir saprasti, nevis iegaumēti.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kāds uzdevums der šim zīmējumam?"

MERKIS = ("Veidosim uzdevuma tekstu shematiskam zīmējumam, lietojot "
          "«par tik vairāk», «kopā» un «atlika».")

SATURS = [
    Sakums("Kāds stāsts slēpjas šajā shēmā?",
           zimejums=restis([["Anna", "1200", ""],
                            ["Juris", "1200", "+ 350"]],
                           "soļi uz skolu"),
           paraksts="Jurim ir tikpat, cik Annai, un vēl 350.",
           fakti=["Shēma ir uzdevums bez vārdiem.",
                  "Vārdus var izdomāt dažādus - matemātika paliek tā pati."]),

    Doma("Trīs shēmas - trīs darbības",
         "Kopā - saskaita daļas; atlika - no visa atņem daļu; par tik "
         "vairāk - pie mazākā pieliek starpību.",
         soli=[
             "Divas daļas un jautājums par visu → «kopā», saskaitīšana.",
             "Viss un viena daļa, jautājums par otru → «atlika», atņemšana.",
             "Divas joslas, viena garāka → «par tik vairāk/mazāk».",
             "Izdomā tekstu un pārbaudi: vai tā darbība atbilst shēmai?",
         ],
         pieze="Juris: 1200 + 350 = 1550 soļu. Jautājums varētu būt: «Cik "
               "soļu līdz skolai ir Jurim?»"),

    Paraugs("Izdomā uzdevumu",
            uzd="Shēma: viss 5000, viena daļa 3200, otra - ?",
            soli=[
                ("viss un daļa", "Tā ir «atlika» shēma."),
                ("«Krājkasītē bija 5000 ct, iztērēja 3200 ct. Cik "
                 "atlika?»", "Viens iespējamais teksts."),
                ("5000 − 3200 = 1800", "Atrisinājums."),
            ],
            atbilde="1800 ct atlika"),

    Varianti("Kurš teksts der shēmai?", [
        {"jaut": "Shēma: 2400 un 1300, jautājums par visu.",
         "opcijas": ["Pirmdien 2400 soļu, otrdien 1300. Cik kopā?",
                     "Bija 2400, iztērēja 1300. Cik atlika?",
                     "Par cik 2400 vairāk nekā 1300?"], "pareizi": 0,
         "padoms": "«Viss» - saskaita."},
        {"jaut": "Shēma: viss 900, daļa 450, jautājums par otru daļu.",
         "opcijas": ["Grāmatā 900 lpp., izlasītas 450. Cik atlika?",
                     "Grāmatā 900 lpp., citā 450. Cik kopā?",
                     "900 lpp. ir par 450 vairāk. Cik ir otrā?"],
         "pareizi": 0, "padoms": "«Atlika» - atņem."},
        {"jaut": "Shēma: josla 600 un garāka josla 600 + 200.",
         "opcijas": ["Kaķis sver 600 g, suns par 200 g vairāk.",
                     "Kaķis 600 g un suns 200 g. Cik kopā?",
                     "Bija 600 g, paliek 200 g."], "pareizi": 0,
         "padoms": "Viena josla garāka par tik."},
        {"jaut": "Kurš vārds liecina par atņemšanu?",
         "opcijas": ["atlika", "kopā", "pavisam", "vēl pielika"],
         "pareizi": 0, "padoms": "Kas atlika pēc tam, kad paņēma."},
    ], pamats=4),

    Zimejums("Par tik mazāk",
             restis([["Rīga-Cēsis", "90 km", ""],
                     ["Rīga-Sigulda", "90 km", "− 38"]],
                    "attālumi pa ceļu"),
             paskaidro="Siguldas josla ir īsāka: 90 − 38 = 52 km. Izdomā "
                       "savu jautājumu šai shēmai.",
             ievads="Tā pati shēma var runāt arī par «mazāk»."),

    Ievadi("Atrisini savu uzdevumu", [
        {"jaut": "Shēma «kopā»: 1850 un 2150. Kāda ir atbilde?",
         "atb": ["4000"], "padoms": "1850 + 2150."},
        {"jaut": "Shēma «atlika»: viss 7000, daļa 2650. Atbilde?",
         "atb": ["4350"], "padoms": "7000 − 2650."},
        {"jaut": "Shēma «par tik vairāk»: 3400 un vēl 800. Atbilde?",
         "atb": ["4200"], "padoms": "3400 + 800."},
        {"jaut": "Shēma «par tik mazāk»: 5000 un par 1250 mazāk. Atbilde?",
         "atb": ["3750"], "padoms": "5000 − 1250."},
    ]),

    Pasaule("Sporta shēmas",
            Ievadi("", [
                {"jaut": "Skrējiena trase ir 5000 m, noskrieti 3250 m. "
                         "Cik m atlika? (shēma «atlika»)",
                 "atb": ["1750"], "padoms": "5000 − 3250."},
                {"jaut": "10 km skrējiens ir 10 000 m, bērnu skrējiens - "
                         "2500 m. Par cik 10 km skrējiens garāks?",
                 "atb": ["7500"], "padoms": "10 000 − 2500."},
                {"jaut": "Stafetē 4 posmi pa 400 m. Cik m kopā?",
                 "atb": ["1600"], "padoms": "400 + 400 + 400 + 400."},
                {"jaut": "Pēc 2 posmiem noskrieti 800 m. Cik vēl atlika?",
                 "atb": ["800"], "padoms": "1600 − 800."},
            ]),
            pavediens="sports",
            konteksts="Skrējiena trase ir dzīva shēma: noskrietais un "
                      "atlikušais kopā ir visa distance.",
            kapec="Kas redz shēmu, tas zina darbību vēl pirms rēķina."),

    Kopsavilkums([
        "Atpazīstu shēmas «kopā», «atlika» un «par tik vairāk».",
        "Izdomāju uzdevuma tekstu dotai shēmai.",
        "Izvēlos darbību pēc shēmas.",
        "Esmu gatavs 4.1. temata pārbaudes darbam.",
    ]),

    Majas([
        "Uzzīmē shēmu savam ceļam uz skolu un atpakaļ un izdomā uzdevumu.",
        "Izdomā vienu «atlika» uzdevumu par naudu un atrisini.",
        "Atkārto: šķiras, salīdzināšana, stabiņš, aptuvenā vērtība.",
    ], ievads="Nākamajā stundā - pārbaudes darbs par 4.1. tematu."),
]
