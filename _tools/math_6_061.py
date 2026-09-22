# -*- coding: utf-8 -*-
"""6. klase, 61. stunda: «Kā ķermeni aprakstīt precīzi?»

Jēdzienu stunda. Skaldne, šķautne un virsotne ir trīs vārdi, bez kuriem
visu turpmāko tematu var tikai rādīt ar pirkstu. Tie tiek nevis uzskaitīti,
bet saskaitīti - uz īsta ķermeņa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kermenis,
                         restis)

TEMA = "Kā ķermeni aprakstīt precīzi?"

MERKIS = ("Iemācīsimies raksturot daudzskaldni, lietojot jēdzienus skaldne, "
          "šķautne un virsotne.")

SATURS = [
    Sakums("Trīs vārdi, kas apraksta jebkuru kasti",
           zimejums=kermenis("kvadrs"),
           paraksts="Skaldne ir plakne, šķautne - divu skaldņu robeža, "
                    "virsotne - punkts, kur satiekas šķautnes.",
           fakti=["Kubam ir 6 skaldnes, 12 šķautnes un 8 virsotnes.",
                  "Šie skaitļi nemainās, kaut arī kubu izstiepj par kvadru."]),

    Doma("Skaldne, šķautne, virsotne",
         "Daudzskaldni raksturo trīs skaitļi: cik tam ir skaldņu, šķautņu un "
         "virsotņu.",
         soli=[
             "Saskaiti skaldnes - tās ir plakanās daļas.",
             "Saskaiti šķautnes - līnijas, kur satiekas divas skaldnes.",
             "Saskaiti virsotnes - punktus, kur satiekas šķautnes.",
             "Pieraksti visus trīs skaitļus.",
             "Pārbaudi ar zināmu ķermeni: kubam tie ir 6, 12 un 8.",
         ],
         pieze="Skaitīt ir vieglāk pa grupām: kubam skaldnes ir 2 apakšā un "
               "augšā plus 4 sānos; šķautnes - 4 apakšā, 4 augšā un 4 "
               "vertikālas."),

    Zimejums("Kubs skaitļos",
             restis([["skaldnes", "šķautnes", "virsotnes"],
                     ["6", "12", "8"]]),
             paskaidro="Šie trīs skaitļi ir viena kuba «pase». Kvadram tie "
                       "ir tieši tādi paši.",
             ievads="Ķermeni var aprakstīt ar trim skaitļiem."),

    Paraugs("Saskaiti trīsstūra prizmai",
            uzd="Cik skaldņu, šķautņu un virsotņu ir trīsstūra prizmai?",
            soli=[
                ("Divas trīsstūra skaldnes - apakšā un augšā",
                 "Tās ir vienādas."),
                ("Trīs taisnstūra skaldnes sānos",
                 "Kopā 5 skaldnes."),
                ("Šķautnes: 3 apakšā, 3 augšā, 3 vertikālas",
                 "Kopā 9 šķautnes."),
                ("Virsotnes: 3 apakšā un 3 augšā",
                 "Kopā 6 virsotnes."),
            ],
            atbilde="5 skaldnes, 9 šķautnes, 6 virsotnes"),

    Ievadi("Saskaiti elementus", [
        {"jaut": "Cik skaldņu ir kubam?",
         "atb": ["6"], "padoms": "Pa vienai katrā pusē.",
         "zim": kermenis("kubs")},
        {"jaut": "Cik šķautņu ir kubam?",
         "atb": ["12"], "padoms": "4 apakšā, 4 augšā, 4 vertikālas."},
        {"jaut": "Cik virsotņu ir kubam?",
         "atb": ["8"], "padoms": "4 apakšā un 4 augšā."},
        {"jaut": "Cik skaldņu ir trīsstūra prizmai?",
         "atb": ["5"], "padoms": "2 trīsstūri un 3 taisnstūri.",
         "zim": kermenis("prizma")},
        {"jaut": "Cik virsotņu ir četrstūra piramīdai?",
         "atb": ["5"], "padoms": "4 pamatā un 1 virsotnē.",
         "zim": kermenis("piramida")},
        {"jaut": "Cik šķautņu ir četrstūra piramīdai?",
         "atb": ["8"], "padoms": "4 pamatā un 4 sānos."},
    ], pamats=4),

    Varianti("Kas ir kas?", [
        {"jaut": "Kas ir šķautne?",
         "opcijas": ["Līnija, kur satiekas divas skaldnes",
                     "Ķermeņa plakanā daļa",
                     "Punkts, kur satiekas līnijas",
                     "Ķermeņa augstums"],
         "pareizi": 0,
         "padoms": "Divu skaldņu robeža."},
        {"jaut": "Kas ir virsotne?",
         "opcijas": ["Punkts, kur satiekas šķautnes",
                     "Ķermeņa augšējā skaldne",
                     "Garākā šķautne", "Ķermeņa vidus"],
         "pareizi": 0,
         "padoms": "Punkts, ne plakne."},
        {"jaut": "Kāda ir atšķirība starp kubu un kvadru?",
         "opcijas": ["Kubam visas šķautnes ir vienādas",
                     "Kvadram ir vairāk skaldņu",
                     "Kubam ir mazāk virsotņu",
                     "Atšķirības nav"],
         "pareizi": 0,
         "padoms": "Elementu skaits abiem sakrīt."},
        {"jaut": "Cik skaldņu satiekas vienā kuba virsotnē?",
         "opcijas": ["3", "2", "4", "6"],
         "pareizi": 0,
         "padoms": "Stūrī satiekas trīs plaknes."},
    ], pamats=4),

    Pasaule("Kā aprakstīt iepakojumu?",
            Ievadi("", [
                {"jaut": "Kastei ir kvadra forma. Cik skaldņu jālīmē?",
                 "atb": ["6"], "padoms": "Visas kvadra skaldnes."},
                {"jaut": "Cik šķautņu jāsalīmē, salokot kasti?",
                 "atb": ["12"], "padoms": "Kvadra šķautņu skaits."},
                {"jaut": "Cik stūru ir kastei?",
                 "atb": ["8"], "padoms": "Virsotņu skaits."},
                {"jaut": "Cik skaldnes ir vienādas kastei 20 x 20 x 30 cm?",
                 "atb": ["2"], "padoms": "Divas kvadrātveida skaldnes."},
            ]),
            pavediens="maja",
            konteksts="Kastes ražotājs runā tieši šajos vārdos: skaldnes "
                      "jāizgriež, šķautnes jāsaloka, virsotnes jāstiprina.",
            kapec="Precīzs apraksts ļauj pasūtīt pareizo iepakojumu."),

    Kopsavilkums([
        "Lietoju jēdzienus skaldne, šķautne un virsotne.",
        "Saskaitu ķermeņa elementus pa grupām.",
        "Raksturoju kubu, kvadru, prizmu un piramīdu ar trim skaitļiem.",
        "Salīdzinu ķermeņus pēc to elementiem.",
    ]),

    Majas([
        "Atrodi mājās kvadra formas priekšmetu un saskaiti tā elementus.",
        "Uzzīmē trīsstūra prizmu un apzīmē vienu skaldni, šķautni un "
        "virsotni.",
        "Pieraksti, cik elementu ir trīsstūra piramīdai.",
    ]),
]
