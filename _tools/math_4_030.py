# -*- coding: utf-8 -*-
"""4. klase, 30. stunda: «Kā modelēt dalīšanu?»

Dalīšanas modelis ir sadalīšana vienādās daļās: 48 : 4 - četri draugi dala
4 desmitniekus un 8 vienniekus. Katram tiek viens desmitnieks un divi
viennieki. Shēma ar joslu, kas sadalīta vienādās daļās, noderēs līdz pat
daļskaitļiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, dala, restis)

TEMA = "Kā modelēt dalīšanu?"

MERKIS = ("Modelēsim divciparu skaitļa dalījumu ar viencipara skaitli un "
          "attēlosim to shematiski.")

SATURS = [
    Sakums("Kā 4 draugiem godīgi sadalīt 48 €?",
           zimejums=restis([["draugs", "10 €", "1 €", "1 €"],
                            ["1.", "10", "1", "1"],
                            ["2.", "10", "1", "1"],
                            ["3.", "10", "1", "1"],
                            ["4.", "10", "1", "1"]],
                           "katram 12 €"),
           paraksts="4 desmitnieki - pa vienam; 8 viennieki - pa diviem.",
           fakti=["Dalot vienādās daļās, katram tiek tikpat.",
                  "Desmitniekus un vienniekus var dalīt atsevišķi."]),

    Doma("Dalīt nozīmē sadalīt vienādās daļās",
         "a : b - a sadala b vienādās daļās; dalījums ir vienas daļas "
         "lielums.",
         soli=[
             "Sadali dalāmo desmitos un vienos: 48 = 40 + 8.",
             "Izdali desmitus: 40 : 4 = 10.",
             "Izdali vienus: 8 : 4 = 2.",
             "Saskaiti: 10 + 2 = 12.",
         ],
         pieze="Dalīšanu var saprast arī kā «cik reižu ietilpst»: 48 : 4 - "
               "cik četrinieku ir skaitlī 48? Arī 12."),

    Zimejums("Josla, sadalīta 4 daļās",
             dala(4, 1, "48 : 4 = 12", "viss - 48"),
             paskaidro="Viena iekrāsotā daļa ir tieši ceturtā daļa no 48.",
             ievads="Shēmā viss ir josla, daļas - vienādi gabali."),

    Paraugs("Modelē 36 : 3",
            uzd="Trīs bērni sadala 36 konfektes. Cik katram?",
            soli=[
                ("36 = 30 + 6", None),
                ("30 : 3 = 10", "Katram pa desmitam."),
                ("6 : 3 = 2", "Katram pa diviem."),
                ("10 + 2 = 12", None),
            ],
            atbilde="12 konfektes"),

    Ievadi("Sadali", [
        {"jaut": "48 : 4 = ?", "atb": ["12"], "padoms": "40 : 4 + 8 : 4."},
        {"jaut": "69 : 3 = ?", "atb": ["23"], "padoms": "60 : 3 + 9 : 3."},
        {"jaut": "84 : 2 = ?", "atb": ["42"], "padoms": "80 : 2 + 4 : 2."},
        {"jaut": "55 : 5 = ?", "atb": ["11"], "padoms": "50 : 5 + 5 : 5."},
        {"jaut": "66 : 6 = ?", "atb": ["11"], "padoms": "60 : 6 + 6 : 6."},
        {"jaut": "96 : 3 = ?", "atb": ["32"], "padoms": "90 : 3 + 6 : 3."},
    ], pamats=4),

    Varianti("Kura shēma der?", [
        {"jaut": "«24 zīmuļi sadalīti 4 kastītēs vienādi.» Ko meklē?",
         "opcijas": ["cik vienā kastītē", "cik pavisam", "cik kastīšu",
                     "cik atlika"], "pareizi": 0,
         "padoms": "Vienas daļas lielums."},
        {"jaut": "«24 zīmuļi, katrā kastītē 4.» Ko meklē?",
         "opcijas": ["cik kastīšu", "cik vienā kastītē", "cik pavisam"],
         "pareizi": 0, "padoms": "Cik reižu 4 ietilpst 24."},
        {"jaut": "Kurš rēķins atbilst abām situācijām?",
         "opcijas": ["24 : 4", "24 · 4", "24 − 4", "24 + 4"], "pareizi": 0,
         "padoms": "Abos gadījumos dala."},
    ]),

    Pasaule("Dabas pētnieku nometne",
            Ievadi("", [
                {"jaut": "84 bērni sadalās 4 vienādās grupās. Cik bērnu "
                         "grupā?",
                 "atb": ["21"], "padoms": "80 : 4 + 4 : 4."},
                {"jaut": "Grupa atrada 63 čiekurus un sadala tos 3 "
                         "vienādās kaudzēs. Cik katrā?",
                 "atb": ["21"], "padoms": "60 : 3 + 3 : 3."},
                {"jaut": "48 putnu būrīšus izvieto 4 mežmalās vienādi. Cik "
                         "katrā mežmalā?",
                 "atb": ["12"], "padoms": "40 : 4 + 8 : 4."},
                {"jaut": "Laivā sēž 2 bērni. Cik laivu vajag 42 bērniem?",
                 "atb": ["21"], "padoms": "42 : 2."},
            ]),
            pavediens="daba",
            konteksts="Nometnē viss tiek dalīts godīgi - grupas, uzdevumi un "
                      "atradumi.",
            kapec="Dalīšana ir godīga sadalīšana - katram vienādi."),

    Kopsavilkums([
        "Modelēju dalīšanu kā sadalīšanu vienādās daļās.",
        "Dalu desmitus un vienus atsevišķi.",
        "Attēloju dalīšanu ar joslu.",
    ]),

    Majas([
        "Sadali 36 zirņus (vai pogas) 3 kaudzītēs un pārbaudi, cik katrā.",
        "Uzzīmē joslu 60 : 3 un izrēķini.",
        "Atrodi mājās kaut ko, ko var sadalīt ģimenei vienādi.",
    ]),
]
