# -*- coding: utf-8 -*-
"""3. klase, 151. stunda: «Milimetri, metri vai kilometri?»

Mērvienības izvēlas pēc tā, ko mēra: zīmuļa resnumu milimetros, istabu
metros, ceļu kilometros. Salīdzināt garumus var tikai tad, kad tie izteikti
vienā vienībā - tā ir šīs stundas galvenā prasme.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Milimetri, metri vai kilometri?"

MERKIS = ("Salīdzināsim garumus, kas izteikti mm, cm, m un km, un "
          "pārveidosim tos.")

SATURS = [
    Sakums("Kurā vienībā mērīt ceļu uz skolu?",
           zimejums=restis([["mm", "zīmuļa resnums"],
                            ["cm", "burtnīcas platums"],
                            ["m", "istabas garums"],
                            ["km", "ceļš uz skolu"]],
                           "katram savs mērs"),
           paraksts="Vienību izvēlas tā, lai skaitlis būtu ērts.",
           fakti=["1 cm = 10 mm, 1 m = 100 cm, 1 km = 1000 m.",
                  "Salīdzināt var tikai vienā vienībā izteiktus garumus."]),

    Doma("Vispirms pārveido, tad salīdzini",
         "Divus garumus var salīdzināt tikai tad, kad abi izteikti vienā un "
         "tajā pašā mērvienībā.",
         soli=[
             "Izvēlies vienu mērvienību abiem garumiem.",
             "Pārveido abus uz to.",
             "Salīdzini skaitļus.",
             "Atbildi pieraksti sākotnējā vienībā.",
         ],
         pieze="Ērtāk pārveidot uz mazāko vienību: tad skaitļi ir veseli un "
               "komatu nevajag."),

    Paraugs("Kurš garums ir lielāks?",
            uzd="Kurš ir garāks: 2 m vai 150 cm?",
            soli=[
                ("2 m = 200 cm",
                 "Pārveido uz centimetriem."),
                ("200 > 150",
                 "Tagad skaitļus var salīdzināt."),
                ("2 m ir garāks",
                 "Par 50 cm."),
            ],
            atbilde="2 m, par 50 cm garāks"),

    Ievadi("Pārveido un salīdzini", [
        {"jaut": "Cik centimetru ir 2 m?", "atb": ["200"],
         "padoms": "2 · 100."},
        {"jaut": "Cik metru ir 1 km?", "atb": ["1000"],
         "padoms": "Tūkstotis."},
        {"jaut": "Cik milimetru ir 8 cm?", "atb": ["80"],
         "padoms": "8 · 10."},
        {"jaut": "Cik metru ir 3 km 500 m?", "atb": ["3500"],
         "padoms": "3000 + 500."},
        {"jaut": "Kurš ir garāks: 2 m vai 150 cm? Ieraksti garumu "
                 "centimetros.",
         "atb": ["200"], "padoms": "2 m = 200 cm."},
        {"jaut": "Par cik centimetriem 2 m ir garāks par 150 cm?",
         "atb": ["50"], "padoms": "200 − 150."},
    ], pamats=4),

    Zimejums("Garuma mērvienību kāpnes",
             restis([["mm", "cm", "m", "km"],
                     ["· 10", "· 100", "· 1000", ""]],
                    "no mazākās uz lielāko"),
             paskaidro="No milimetra līdz centimetram ir 10, no centimetra "
                       "līdz metram 100, no metra līdz kilometram 1000.",
             ievads="Šīs kāpnes vērts iemācīties."),

    Varianti("Kurā vienībā mērīt?", [
        {"jaut": "Kurā vienībā mēra ceļu starp pilsētām?",
         "opcijas": ["km", "m", "cm", "mm"],
         "pareizi": 0, "padoms": "Skaitlim jābūt ērtam."},
        {"jaut": "Kurā vienībā mēra zīmuļa resnumu?",
         "opcijas": ["mm", "cm", "m", "km"],
         "pareizi": 0, "padoms": "Ļoti mazs garums."},
        {"jaut": "Kurš garums ir vislielākais?",
         "opcijas": ["1 km", "900 m", "5000 cm", "10 000 mm"],
         "pareizi": 0, "padoms": "Pārvērt visu metros."},
        {"jaut": "Cik metru ir 2 km 300 m?",
         "opcijas": ["2300", "230", "23 000", "2003"],
         "pareizi": 0, "padoms": "2000 + 300."},
    ], pamats=4),

    Pasaule("Cik tālu ir ceļš uz skolu?",
            Ievadi("", [
                {"jaut": "Ceļš uz skolu ir 1 km 200 m. Cik metru tas ir?",
                 "atb": ["1200"], "padoms": "1000 + 200."},
                {"jaut": "Cik metru ir turp un atpakaļ?", "atb": ["2400"],
                 "padoms": "2 · 1200."},
                {"jaut": "Cik metru sanāk nedēļā, ja skolā iet 5 dienas?",
                 "atb": ["12000", "12 000"], "padoms": "5 · 2400."},
                {"jaut": "Cik kilometru tas ir?", "atb": ["12"],
                 "padoms": "12 000 : 1000."},
            ]),
            pavediens="skola",
            konteksts="Ceļu uz skolu saka kilometros, bet soļu skaitītājs "
                      "rāda metrus - abi apraksta vienu ceļu.",
            kapec="Nedēļā sanāk 12 km - to pamana tikai tad, kad saskaita."),

    Kopsavilkums([
        "Izvēlos mērvienību pēc tā, ko mēru.",
        "Pārveidoju mm, cm, m un km.",
        "Salīdzinu garumus, izteiktus dažādās vienībās.",
        "Pierakstu atbildi ērtākajā vienībā.",
    ]),

    Majas([
        "Izmēri ceļu no savas istabas līdz virtuvei metros.",
        "Noskaidro, cik kilometru ir tavs ceļš uz skolu.",
        "Izsaki to metros.",
    ]),
]
