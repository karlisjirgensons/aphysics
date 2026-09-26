# -*- coding: utf-8 -*-
"""4. klase, 46. stunda: «Tik reižu vairāk vai par tik vairāk?»

Divi teikumi, kurus bieži sajauc: «par 3 vairāk» (+ 3) un «3 reizes
vairāk» (· 3). Shēmā tie izskatās pavisam citādi: pirmajā josla ir
pagarināta par gabalu, otrajā - atkārtota trīs reizes.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Tik reižu vairāk vai par tik vairāk?"

MERKIS = ("Attēlosim shematiski situācijas ar «tik reižu vairāk» un «par tik "
          "vairāk» un risināsim tās.")

SATURS = [
    Sakums("Kaķis sver 4 kg. Suns - 3 reizes vairāk. Cik?",
           zimejums=restis([["kaķis", "4", "", ""],
                            ["suns", "4", "4", "4"],
                            ["zaķis", "4", "+ 3", ""]],
                           "3 reizes vairāk vai par 3 vairāk"),
           paraksts="Suns: 4 · 3 = 12 kg. Zaķis «par 3 vairāk»: 4 + 3 = 7 kg.",
           fakti=["«Reizes» - reizina vai dala.",
                  "«Par» - saskaita vai atņem."]),

    Doma("«Reizes» - reizina, «par» - saskaita",
         "«Tik reižu vairāk» nozīmē atkārtot tik reizes; «par tik vairāk» - "
         "pielikt tik klāt.",
         soli=[
             "5 reizes vairāk nekā 8: 8 · 5 = 40.",
             "Par 5 vairāk nekā 8: 8 + 5 = 13.",
             "5 reizes mazāk nekā 40: 40 : 5 = 8.",
             "Par 5 mazāk nekā 40: 40 − 5 = 35.",
         ],
         pieze="Uzzīmē shēmu - «reizes» shēmā ir vairākas vienādas joslas."),

    Paraugs("Divi jautājumi vienā",
            uzd="Rīgā 120 bērnu pulciņā, Cēsīs 4 reizes mazāk. Cik Cēsīs? "
                "Par cik vairāk Rīgā?",
            soli=[
                ("120 : 4 = 30", "«4 reizes mazāk» - dala."),
                ("120 − 30 = 90", "«Par cik» - atņem."),
            ],
            atbilde="Cēsīs 30; Rīgā par 90 vairāk"),

    Zimejums("Divas shēmas",
             restis([["reizes:", "6", "6", "6", "= 18"],
                     ["par:", "6", "+ 3", "", "= 9"]],
                    "6 · 3 un 6 + 3"),
             paskaidro="Augšā tā pati josla trīs reizes, apakšā - viena josla "
                       "un mazs gabals.",
             ievads="Tā izskatās atšķirība."),

    Varianti("Kura darbība?", [
        {"jaut": "«7 reizes vairāk nekā 6»",
         "opcijas": ["6 · 7", "6 + 7", "7 − 6", "42 : 6"], "pareizi": 0,
         "padoms": "Reizes - reizina."},
        {"jaut": "«Par 7 vairāk nekā 6»",
         "opcijas": ["6 + 7", "6 · 7", "7 − 6", "6 : 7"], "pareizi": 0,
         "padoms": "Par - saskaita."},
        {"jaut": "«4 reizes mazāk nekā 28»",
         "opcijas": ["28 : 4", "28 − 4", "28 · 4", "28 + 4"], "pareizi": 0,
         "padoms": "Reizes mazāk - dala."},
        {"jaut": "«Par 4 mazāk nekā 28»",
         "opcijas": ["28 − 4", "28 : 4", "28 + 4", "4 · 28"], "pareizi": 0,
         "padoms": "Par mazāk - atņem."},
        {"jaut": "Cik reižu 60 ir lielāks nekā 12?",
         "opcijas": ["5", "48", "72", "6"], "pareizi": 0,
         "padoms": "60 : 12."},
        {"jaut": "Par cik 60 ir lielāks nekā 12?",
         "opcijas": ["48", "5", "72", "4"], "pareizi": 0,
         "padoms": "60 − 12."},
    ], pamats=4),

    Ievadi("Izrēķini", [
        {"jaut": "9 reizes vairāk nekā 8", "atb": ["72"], "padoms": "8 · 9."},
        {"jaut": "Par 9 vairāk nekā 8", "atb": ["17"], "padoms": "8 + 9."},
        {"jaut": "6 reizes mazāk nekā 54", "atb": ["9"], "padoms": "54 : 6."},
        {"jaut": "Cik reižu 350 lielāks par 70?", "atb": ["5"],
         "padoms": "350 : 70 = 35 : 7."},
    ]),

    Pasaule("Dzīvnieku rekordi",
            Ievadi("", [
                {"jaut": "Zilonis sver 6000 kg, žirafe - 5 reizes mazāk. "
                         "Cik kg sver žirafe?",
                 "atb": ["1200"], "padoms": "6000 : 5."},
                {"jaut": "Par cik kg zilonis smagāks nekā žirafe?",
                 "atb": ["4800"], "padoms": "6000 − 1200."},
                {"jaut": "Gepards skrien 110 km/h, cilvēks 10 km/h. Cik "
                         "reižu gepards ātrāks?",
                 "atb": ["11"], "padoms": "110 : 10."},
                {"jaut": "Par cik km/h gepards ātrāks nekā cilvēks?",
                 "atb": ["100"], "padoms": "110 − 10."},
            ]),
            pavediens="daba",
            konteksts="Dabas rekordos salīdzina gan «reizes», gan «par cik» - "
                      "un tās ir dažādas atbildes.",
            kapec="Viens vārds - «reizes» vai «par» - maina visu rēķinu."),

    Kopsavilkums([
        "Atšķiru «tik reižu vairāk» no «par tik vairāk».",
        "Zīmēju shēmas abām situācijām.",
        "Atrodu, cik reižu un par cik viens skaitlis lielāks.",
    ]),

    Majas([
        "Salīdzini savu un pieaugušā vecumu: cik reižu un par cik?",
        "Izdomā vienu «reizes» un vienu «par» uzdevumu par dzīvniekiem.",
        "Uzzīmē abas shēmas skaitlim 5 un 4.",
    ]),
]
