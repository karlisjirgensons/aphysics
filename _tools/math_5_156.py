# -*- coding: utf-8 -*-
"""5. klase, 156. stunda: «Kā atliek punktu koordinātu plaknē?»

Pēdējā temata pirmā stunda. Koordinātu plakne ir divas skaitļu taisnes, kas
krustojas, un punkts tajā ir divu skaitļu pāris. Vienīgais, ko te var
sajaukt, ir secība: pirmais skaitlis vienmēr ir pa labi, otrs - uz augšu.
Tāpēc stunda sākas ar secību, ne ar zīmēšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, plakne)

TEMA = "Kā atliek punktu koordinātu plaknē?"

MERKIS = ("Iemācīsimies atlikt un nolasīt punktus koordinātu plaknē, "
          "ievērojot izvēlēto vienību.")

SATURS = [
    Sakums("Divi skaitļi - viens punkts",
           zimejums=plakne(punkti=[(3, 2, "A")], no_x=0, lidz_x=6, no_y=0,
                           lidz_y=5, virsraksts="Punkts A(3; 2)"),
           paraksts="Pirmais skaitlis - pa labi, otrais - uz augšu.",
           fakti=["Koordinātu plaknē ir divas asis.",
                  "Horizontālā ass ir x, vertikālā - y.",
                  "Punktu apzīmē ar diviem skaitļiem: A(3; 2)."]),

    Doma("Vispirms pa labi, tad uz augšu",
         "Punkta vieta koordinātu plaknē ir divu skaitļu pāris: pirmais rāda "
         "attālumu pa x asi, otrais - pa y asi.",
         soli=[
             "Sāc no punkta, kur asis krustojas.",
             "Ej pa labi tik vienību, cik rāda pirmais skaitlis.",
             "Ej uz augšu tik vienību, cik rāda otrais skaitlis.",
             "Atzīmē punktu un pieraksti tam burtu.",
             "Nolasot dari to pašu pretējā secībā.",
         ],
         pieze="A(3; 2) un A(2; 3) ir divi dažādi punkti. Tāpēc secība nav "
               "izvēles jautājums: pirmais skaitlis vienmēr ir pa x asi."),

    Paraugs("Atliec punktu A(3; 2)",
            uzd="Kur koordinātu plaknē atrodas šis punkts?",
            soli=[
                ("Sākums ir asu krustpunktā",
                 "Tur abas koordinātas ir 0."),
                ("Trīs vienības pa labi",
                 "Pirmais skaitlis."),
                ("Divas vienības uz augšu",
                 "Otrais skaitlis."),
                ("Atzīmē punktu un raksti A",
                 "Punkts atrasts."),
            ],
            atbilde="A(3; 2) ir trīs pa labi un divas uz augšu"),

    Ievadi("Nolasi koordinātas", [
        {"jaut": "Punkts A(3; 2). Kāda ir tā pirmā koordināta?",
         "atb": ["3"], "padoms": "Pa x asi."},
        {"jaut": "Punkts A(3; 2). Kāda ir tā otrā koordināta?",
         "atb": ["2"], "padoms": "Pa y asi."},
        {"jaut": "Punkts B(5; 1). Cik vienību jāiet pa labi?",
         "atb": ["5"], "padoms": "Pirmais skaitlis."},
        {"jaut": "Punkts B(5; 1). Cik vienību jāiet uz augšu?",
         "atb": ["1"], "padoms": "Otrais skaitlis."},
        {"jaut": "Punkts C(0; 4). Cik vienību jāiet pa labi?",
         "atb": ["0"], "padoms": "Punkts ir uz y ass."},
        {"jaut": "Vai A(3; 2) un A(2; 3) ir viens punkts? Raksti «jā» vai "
                 "«nē».",
         "atb": ["nē", "ne"], "padoms": "Secība ir svarīga."},
        {"jaut": "Punkts atrodas 4 pa labi un 3 uz augšu. Kāda ir tā pirmā "
                 "koordināta?",
         "atb": ["4"], "padoms": "Pa x asi."},
        {"jaut": "Kāda ir asu krustpunkta pirmā koordināta?",
         "atb": ["0"], "padoms": "Sākumpunkts."},
    ], pamats=4,
        ievads="Pirmais skaitlis pa labi, otrais uz augšu - vienmēr."),

    Zimejums("Trīs punkti plaknē",
             plakne(punkti=[(1, 1, "A"), (4, 2, "B"), (2, 4, "C")],
                    no_x=0, lidz_x=6, no_y=0, lidz_y=5,
                    virsraksts="A(1; 1), B(4; 2), C(2; 4)"),
             paskaidro="B un C atšķiras tikai ar koordinātu secību, bet "
                       "plaknē tie ir divās dažādās vietās.",
             ievads="Katram punktam savs skaitļu pāris."),

    Varianti("Kur ir punkts?", [
        {"jaut": "Ko rāda pirmā koordināta?",
         "opcijas": ["Attālumu pa x asi", "Attālumu pa y asi",
                     "Punkta nosaukumu", "Vienību"],
         "pareizi": 0,
         "padoms": "Pa labi."},
        {"jaut": "Vai A(3; 2) un A(2; 3) ir viens punkts?",
         "opcijas": ["Nē, tie ir divi dažādi", "Jā", "Tikai uz asīm",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "Secība ir svarīga."},
        {"jaut": "Punkts C(0; 4) atrodas...",
         "opcijas": ["Uz y ass", "Uz x ass", "Krustpunktā", "Ārpus plaknes"],
         "pareizi": 0,
         "padoms": "Pa labi neiet nemaz."},
        {"jaut": "Kā sauc horizontālo asi?",
         "opcijas": ["x ass", "y ass", "Vienības ass", "Punktu ass"],
         "pareizi": 0,
         "padoms": "Pirmā koordināta."},
        {"jaut": "Kādas koordinātas ir asu krustpunktam?",
         "opcijas": ["(0; 0)", "(1; 1)", "(0; 1)", "(1; 0)"],
         "pareizi": 0,
         "padoms": "Sākumpunkts."},
        {"jaut": "Punkts D(5; 0) atrodas...",
         "opcijas": ["Uz x ass", "Uz y ass", "Krustpunktā", "Plaknes vidū"],
         "pareizi": 0,
         "padoms": "Uz augšu neiet nemaz."},
    ], pamats=4),

    Pasaule("Kur atrodas skolas vieta kartē?",
            Ievadi("", [
                {"jaut": "Kartē skola ir 3 rūtiņas pa labi un 2 uz augšu. "
                         "Kāda ir pirmā koordināta?",
                 "atb": ["3"], "padoms": "Pa labi."},
                {"jaut": "Kāda ir otrā koordināta?",
                 "atb": ["2"], "padoms": "Uz augšu."},
                {"jaut": "Veikals ir punktā (5; 1). Cik rūtiņas pa labi?",
                 "atb": ["5"], "padoms": "Pirmais skaitlis."},
                {"jaut": "Māja ir punktā (0; 3). Cik rūtiņas uz augšu?",
                 "atb": ["3"], "padoms": "Otrais skaitlis."},
            ]),
            pavediens="skola",
            konteksts="Kartē un spēļu laukumā vietu nosaka tieši tāpat - ar "
                      "diviem skaitļiem.",
            kapec="Divi skaitļi pietiek, lai atrastu vienu vienīgu punktu."),

    Kopsavilkums([
        "Atlieku punktu koordinātu plaknē pēc diviem skaitļiem.",
        "Nolasu punkta koordinātas no zīmējuma.",
        "Zinu, ka pirmā koordināta ir pa x asi, otrā - pa y asi.",
        "Zinu, ka koordinātu secība ir svarīga.",
    ]),

    Majas([
        "Uzzīmē koordinātu plakni un atliec punktus A(2; 5), B(5; 2) un "
        "C(0; 3).",
        "Pieraksti, ar ko atšķiras A un B.",
        "Atrodi kartē kādu vietu un pieraksti tās koordinātas.",
    ]),
]
