# -*- coding: utf-8 -*-
"""7. klase, 21. stunda: «Kā definē staru un nogriezni?»

Staru un nogriezni definē ar jau zināmiem jēdzieniem - punktu, taisni un
«atrodas starp». Stunda iemāca definīcijas uzbūvi: vispārīgais jēdziens un
pazīme, kas atšķir definējamo no citiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kā definē staru un nogriezni?"

MERKIS = ("Veidosim nogriežņa un stara definīcijas, izmantojot jau "
          "definētus jēdzienus.")

SATURS = [
    Sakums("Lāzers, diegs un lineāls",
           zimejums=geometrija([("A", 0, 1), ("B", 5, 1), ("O", 0, -1),
                                ("C", 5, -1)],
                               nogriezni=["AB"], stari=["OC"]),
           paraksts="Nogrieznis AB - divi gali; stars OC - viens gals.",
           fakti=["Lāzera stars sākas ierīcē un iet tālu prom - kā stars.",
                  "Lineāls ir ar diviem galiem - kā nogrieznis."]),

    Doma("Definīcija = vispārīgais jēdziens + atšķirīgā pazīme",
         "Nogrieznis AB ir taisnes daļa, kas sastāv no punktiem A, B un "
         "visiem punktiem starp tiem. Stars OC ir taisnes daļa, kas sastāv "
         "no punkta O un visiem taisnes punktiem, kas atrodas tajā pašā pusē "
         "no O, kur punkts C.",
         soli=[
             "Nosauc vispārīgāko jēdzienu: «taisnes daļa».",
             "Pasaki, ar ko šī daļa atšķiras: divi gali vai viens gals.",
             "Lieto tikai jau zināmus vārdus.",
             "Pārbaudi: vai definīcijai atbilst tikai definējamā figūra?",
         ],
         pieze="Nogriezni AB var saukt arī par BA. Staru OC nevar saukt par "
               "CO - pirmais burts ir stara sākumpunkts."),

    Paraugs("Divi stari uz vienas taisnes",
            uzd="Uz taisnes secīgi atzīmēti punkti A, O, B. Cik staru ar "
                "sākumpunktu O ir? Kāds ir staru OA un OB šķēlums?",
            soli=[
                ("Stars OA un stars OB", "Divi stari uz pretējām pusēm."),
                ("Tie ir papildstari", "Kopā tie veido visu taisni."),
                ("OA ∩ OB = {O}", "Kopīgs ir tikai sākumpunkts."),
            ],
            atbilde="Divi stari; šķēlums ir punkts O."),

    Zimejums("Papildstari",
             geometrija([("A", 0, 0), ("O", 4, 0), ("B", 8, 0)],
                        stari=["OA", "OB"]),
             paskaidro="Stari OA un OB kopā veido taisni AB."),

    Varianti("Nogrieznis vai stars?", [
        {"jaut": "Gaisma no bākas uguns",
         "opcijas": ["Stars", "Nogrieznis", "Taisne", "Punkts"],
         "pareizi": 0,
         "padoms": "Sākums ir, gala - nav."},
        {"jaut": "Tilts starp diviem krastiem",
         "opcijas": ["Nogrieznis", "Stars", "Taisne", "Punkts"],
         "pareizi": 0,
         "padoms": "Divi gali."},
        {"jaut": "Kurš pieraksts apzīmē staru ar sākumu punktā K?",
         "opcijas": ["Stars KM", "Stars MK", "Nogrieznis KM",
                     "Nogrieznis MK"],
         "pareizi": 0,
         "padoms": "Sākumpunktu raksta pirmo."},
        {"jaut": "Kurā definīcijā ir kļūda?",
         "opcijas": ["Nogrieznis ir stars ar diviem galiem",
                     "Nogrieznis AB - punkti A, B un visi starp tiem",
                     "Stars - taisnes daļa ar vienu galapunktu",
                     "Taisne - pamatjēdziens"],
         "pareizi": 0,
         "padoms": "Staram ir tikai viens gals."},
    ], pamats=4),

    Ievadi("Saskaiti", [
        {"jaut": "Uz taisnes ir 3 punkti. Cik nogriežņu ar galiem šajos "
                 "punktos?",
         "atb": ["3"], "padoms": "AB, AC, BC."},
        {"jaut": "Uz taisnes ir 3 punkti. Cik staru ar sākumu kādā no "
                 "šiem punktiem (dažādus starus)?",
         "atb": ["6"], "padoms": "No katra punkta 2 stari."},
        {"jaut": "Uz taisnes ir punkti A, B, C (šādā secībā). Cik no "
                 "stariem AB, AC, BA, CA ir vienādi ar staru AB?",
         "atb": ["2"], "padoms": "AB un AC - viens un tas pats stars."},
    ]),

    Pasaule("Lāzera attālummērs",
            Ievadi("", [
                {"jaut": "Lāzers no ierīces līdz sienai veido nogriezni "
                         "4,2 m. Gaisma iet 300 000 km/s. Vai nogriezni tā "
                         "veic acumirklī? Raksti «jā» vai «nē».",
                 "atb": ["jā", "ja"], "padoms": "Miljardās sekundes daļās."},
                {"jaut": "Attālummērs mēra līdz sienai un atpakaļ: 8,4 m. "
                         "Cik garš ir nogrieznis līdz sienai (m)?",
                 "atb": ["4,2"], "padoms": "8,4 : 2."},
                {"jaut": "Ja sienas nav, lāzers iet bezgalīgi tālu. Kāda "
                         "figūra ir tā ceļš?",
                 "atb": ["stars"], "padoms": "Viens gals.",
                 "tastatura": "text"},
            ]),
            pavediens="tehnika",
            konteksts="Lāzera mērītājs mēra laiku, kurā gaisma aiziet līdz "
                      "sienai un atpakaļ.",
            kapec="Stars kļūst par nogriezni, kad tam rodas otrs gals."),

    Kopsavilkums([
        "Definēju nogriezni un staru ar punktu un taisni.",
        "Zinu, ka definīcijā ir vispārīgais jēdziens un pazīme.",
        "Pareizi pierakstu staru: sākumpunkts pirmais.",
        "Zinu, kas ir papildstari.",
    ]),

    Majas([
        "Atrodi 3 staru un 3 nogriežņu modeļus dzīvē.",
        "Uzraksti savu nogriežņa definīciju un salīdzini ar klases.",
        "Uzzīmē 4 punktus uz taisnes un saskaiti visus nogriežņus.",
    ]),
]
