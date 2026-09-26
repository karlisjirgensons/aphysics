# -*- coding: utf-8 -*-
"""3. klase, 91. stunda: «Kā salīdzināt uz skaitļu taisnes?»

Skaitļu taisne ir vienīgais modelis, kas der jebkurām divām daļām - arī tad,
kad ne saucēji, ne skaitītāji nesakrīt. Salīdzināšana kļūst par vienkāršu
noteikumu: kas ir pa labi, tas ir lielāks.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā salīdzināt uz skaitļu taisnes?"

MERKIS = ("Izmantosim skaitļu taisni daļu salīdzināšanai un pierakstīsim "
          "salīdzinājumu ar «<» vai «>».")

SATURS = [
    Sakums("Kā salīdzināt {2|3} un {3|4}?",
           zimejums=taisne(0, 1, 1, [(0.667, "2/3"), (0.75, "3/4")]),
           paraksts="Kas uz taisnes ir tālāk pa labi, tas ir lielāks.",
           fakti=["Uz skaitļu taisnes katrai daļai ir sava vieta.",
                  "Lielāka ir tā daļa, kas atrodas tālāk no nulles."]),

    Doma("Tālāk pa labi nozīmē lielāks",
         "Uzliec abas daļas uz vienas taisnes un paskaties, kura ir tuvāk "
         "vieniniekam.",
         soli=[
             "Uzzīmē posmu no 0 līdz 1.",
             "Atzīmē pirmo daļu pēc tās saucēja.",
             "Atzīmē otro daļu pēc tās saucēja.",
             "Salīdzini punktu vietas un pieraksti ar «<» vai «>».",
         ],
         pieze="Vienai un tai pašai taisnei drīkst likt daļas ar dažādiem "
               "saucējiem - vieta uz taisnes nav atkarīga no pieraksta."),

    Paraugs("Kura daļa ir lielāka?",
            uzd="Salīdzini {2|3} un {3|4}, izmantojot skaitļu taisni.",
            soli=[
                ("{2|3} - posmu dala trīs daļās, skaita divas",
                 "Punkts ir nedaudz aiz vidus."),
                ("{3|4} - posmu dala četrās daļās, skaita trīs",
                 "Punkts ir tuvāk vieniniekam."),
                ("{2|3} < {3|4}",
                 "Otrā daļa ir tālāk pa labi."),
            ],
            atbilde="{3|4} ir lielāka"),

    Zimejums("Puse un citas daļas",
             taisne(0, 1, 1, [(0.5, "1/2"), (0.333, "1/3"),
                              (0.8, "4/5")]),
             paskaidro="Visas trīs daļas ir uz vienas taisnes, tāpēc tās var "
                       "salīdzināt ar aci.",
             ievads="Trīs daļas, viena taisne."),

    Ievadi("Salīdzini uz taisnes", [
        {"jaut": "Kura daļa ir tuvāk 1: {2|3} vai {3|4}? Ieraksti saucēju.",
         "atb": ["4"], "padoms": "{3|4} ir tālāk pa labi."},
        {"jaut": "Kura daļa ir tuvāk 0: {1|5} vai {1|3}? Ieraksti saucēju.",
         "atb": ["5"], "padoms": "{1|5} ir mazāka."},
        {"jaut": "Cik astotdaļu ir līdz {1|2}?", "atb": ["4"],
         "padoms": "8 : 2."},
        {"jaut": "Vai {5|8} ir lielāks par {1|2}? Raksti «jā» vai «nē».",
         "atb": ["jā", "ja"], "padoms": "{4|8} ir puse.",
         "tastatura": "text"},
        {"jaut": "Vai {3|8} ir lielāks par {1|2}? Raksti «jā» vai «nē».",
         "atb": ["nē", "ne"], "padoms": "3 < 4.",
         "tastatura": "text"},
        {"jaut": "Cik desmitdaļu ir līdz {1|2}?", "atb": ["5"],
         "padoms": "10 : 2."},
    ], pamats=4),

    Varianti("Kura daļa ir lielāka?", [
        {"jaut": "Kura daļa atrodas tālāk pa labi?",
         "opcijas": ["{3|4}", "{1|2}", "{1|4}", "{1|8}"],
         "pareizi": 0, "padoms": "Vistuvāk vieniniekam."},
        {"jaut": "Ar ko der salīdzināt jebkuru daļu?",
         "opcijas": ["Ar {1|2}", "Ar 0", "Ar 10", "Ar saucēju"],
         "pareizi": 0, "padoms": "Puse ir ērts atskaites punkts."},
        {"jaut": "Vai {4|7} ir lielāks par pusi?",
         "opcijas": ["Jā, jo 4 ir vairāk par pusi no 7",
                     "Nē", "Tieši puse", "To nevar pateikt"],
         "pareizi": 0, "padoms": "Puse no 7 būtu 3,5."},
        {"jaut": "Kura daļa ir vistuvāk nullei?",
         "opcijas": ["{1|10}", "{1|3}", "{1|2}", "{2|3}"],
         "pareizi": 0, "padoms": "Vismazākā daļa."},
    ], pamats=4),

    Pasaule("Kurš dzīvnieks noskrējis tālāk?",
            Ievadi("", [
                {"jaut": "Zaķis noskrēja {3|4} no ceļa, stirna {2|3}. Kurš "
                         "tālāk? Ieraksti saucēju.",
                 "atb": ["4"], "padoms": "{3|4} > {2|3}."},
                {"jaut": "Ceļš ir 120 m. Cik metru ir {3|4}?",
                 "atb": ["90"], "padoms": "120 : 4 = 30; 3 · 30."},
                {"jaut": "Cik metru ir {2|3}?", "atb": ["80"],
                 "padoms": "120 : 3 = 40; 2 · 40."},
                {"jaut": "Par cik metriem zaķis ir priekšā?",
                 "atb": ["10"], "padoms": "90 − 80."},
            ]),
            pavediens="daba",
            konteksts="Dzīvnieku ceļu bieži mēra daļās no visa attāluma - tā "
                      "var salīdzināt dažāda garuma maršrutus.",
            kapec="Pārrēķinot metros, salīdzinājumu var arī pārbaudīt."),

    Kopsavilkums([
        "Salīdzinu daļas uz skaitļu taisnes.",
        "Zinu, ka tālāk pa labi nozīmē lielāks.",
        "Pierakstu salīdzinājumu ar «<» vai «>».",
        "Salīdzinu daļu ar pusi kā atskaites punktu.",
    ]),

    Majas([
        "Uzzīmē skaitļu taisni un atzīmē tajā {1|2}, {2|3} un {3|4}.",
        "Pasaki, kura daļa ir vislielākā.",
        "Atrodi divas daļas, kas atrodas ļoti tuvu viena otrai.",
    ]),
]
