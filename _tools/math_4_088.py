# -*- coding: utf-8 -*-
"""4. klase, 88. stunda: «Kā zīmējums palīdz saprast uzdevumu?»

Shēmas trīs veidi vienā uzdevumā: «tik reižu vairāk», «kopā», «atlika».
Saliktam uzdevumam zīmē vienu shēmu ar visiem lielumiem, un no tās izlasa
darbību secību. Tas ir pamats 4.8. temata kustības un pirkumu uzdevumiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā zīmējums palīdz saprast uzdevumu?"

MERKIS = ("Veidosim shematisku zīmējumu situācijām ar «tik reižu vairāk», "
          "«kopā» un «atlika».")

SATURS = [
    Sakums("Kaķim 4 kg, sunim 5 reizes vairāk. Cik kopā?",
           zimejums=restis([["kaķis", "4", "", "", "", ""],
                            ["suns", "4", "4", "4", "4", "4"]],
                           "kopā: 6 vienādi gabali"),
           paraksts="4 + 4 · 5 = 4 · 6 = 24 kg.",
           fakti=["Shēmā redz: kopā ir 6 vienādi gabali.",
                  "Tas ir ātrāk nekā divi atsevišķi rēķini."]),

    Doma("Viena shēma - visa situācija",
         "Uzzīmē vienu shēmu, kurā redzami visi lielumi; no tās izlasi, kuras "
         "darbības vajag un kādā secībā.",
         soli=[
             "Zīmē mazāko lielumu kā vienu joslu.",
             "«Tik reižu vairāk» - tik vienādas joslas.",
             "«Kopā» - figūriekava ap visu; «atlika» - nosvītro daļu.",
             "Pieraksti izteiksmi pēc shēmas.",
         ],
         pieze="Ja zināms «kopā» un «tik reižu vairāk», shēma parāda: dali "
               "kopējo ar gabalu skaitu."),

    Paraugs("Atrodi mazāko",
            uzd="Tēvs un dēls kopā 48 gadi; tēvs 3 reizes vecāks. Cik gadu "
                "dēlam?",
            soli=[
                ("dēls - 1 gabals, tēvs - 3 gabali", "Shēma."),
                ("kopā 4 gabali = 48", None),
                ("48 : 4 = 12", "Viens gabals - dēls."),
            ],
            atbilde="dēlam 12 gadi (tēvam 36)"),

    Zimejums("Shēma: kopā un reizes",
             restis([["dēls", "?", "", ""],
                     ["tēvs", "?", "?", "?"],
                     ["kopā", "48", "", ""]],
                    "4 vienādi gabali = 48"),
             paskaidro="Katrs «?» ir tas pats skaitlis - 12.",
             ievads="Vienāda izmēra rūtiņas - vienādi lielumi."),

    Ievadi("Zīmē un rēķini", [
        {"jaut": "Ābolu 6 kg, bumbieru 4 reizes vairāk. Cik kg kopā?",
         "atb": ["30"], "padoms": "6 · 5."},
        {"jaut": "Kopā 60 lappuses, otrā grāmata 2 reizes biezāka. Cik "
                 "lappušu plānākajā?", "atb": ["20"], "padoms": "60 : 3."},
        {"jaut": "Bija 100 €, iztērēja 3 reizes vairāk nekā palika. Cik "
                 "palika?", "atb": ["25"],
         "padoms": "Palika 1 gabals, iztērēja 3 - kopā 4: 100 : 4."},
        {"jaut": "Pa 8 kg - 5 kastes, vienu aizveda. Cik kg atlika?",
         "atb": ["32"], "padoms": "8 · 4."},
    ]),

    Varianti("Kura shēma der?", [
        {"jaut": "«Anna 7 gadi, Juris 3 reizes vecāks.»",
         "opcijas": ["1 josla un 3 joslas", "1 josla un josla + 3",
                     "3 joslas un 7 joslas"], "pareizi": 0,
         "padoms": "Reizes - vienādas joslas."},
        {"jaut": "«Kopā 40, viens ir 4 reizes lielāks.» Cik gabalu?",
         "opcijas": ["5", "4", "40", "8"], "pareizi": 0,
         "padoms": "1 + 4."},
        {"jaut": "Cik ir mazākais, ja kopā 40 un 5 gabali?",
         "opcijas": ["8", "10", "4", "35"], "pareizi": 0,
         "padoms": "40 : 5."},
    ]),

    Pasaule("Dzīvnieku patversme",
            Ievadi("", [
                {"jaut": "Patversmē kaķu ir 3 reizes vairāk nekā suņu; kopā "
                         "48 dzīvnieki. Cik suņu?",
                 "atb": ["12"], "padoms": "48 : 4."},
                {"jaut": "Cik kaķu?", "atb": ["36"], "padoms": "12 · 3."},
                {"jaut": "Paņēma mājās 9 kaķus. Cik kaķu atlika?",
                 "atb": ["27"], "padoms": "36 − 9."},
                {"jaut": "Barība sunim 300 g dienā. Cik g dienā visiem 12 "
                         "suņiem?", "atb": ["3600"], "padoms": "300 · 12."},
            ]),
            pavediens="daba",
            konteksts="Patversme plāno barību un vietas - un attiecības "
                      "starp dzīvnieku skaitiem ir redzamas shēmā.",
            kapec="Shēma pārvērš sarežģītu tekstu vienkāršā zīmējumā."),

    Kopsavilkums([
        "Zīmēju shēmu situācijām ar «tik reižu», «kopā» un «atlika».",
        "Atrodu mazāko lielumu, dalot kopējo ar gabalu skaitu.",
        "Pierakstu izteiksmi pēc shēmas.",
    ]),

    Majas([
        "Izdomā uzdevumu «kopā un reizes» par savu ģimeni un uzzīmē shēmu.",
        "Atrisini: kopā 56 konfektes, Ievai 3 reizes vairāk nekā Jurim.",
        "Paskaidro kādam, kā shēma palīdz.",
    ]),
]
