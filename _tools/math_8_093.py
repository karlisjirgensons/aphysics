# -*- coding: utf-8 -*-
"""8. klase, 93. stunda: «Kā klasificēt četrstūrus?»

Četrstūrus šķiro pēc paralēlo malu pāru skaita: 0 - vispārīgs vai
deltoīds, 1 - trapece, 2 - paralelograms. Paralelogramus tālāk: rombs,
taisnstūris, kvadrāts (abu kopīgā daļa - Venna diagrammā).
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, Zimejums, restis, venna)

TEMA = "Kā klasificēt četrstūrus?"

MERKIS = ("Klasificēsim četrstūrus pēc paralēlo malu pāru skaita un pēc "
          "pašu izvēlētām pazīmēm.")

SATURS = [
    Sakums("Cik paralēlu malu pāru?",
           zimejums=restis([["0 pāru", "deltoīds u. c."],
                            ["1 pāris", "trapece"],
                            ["2 pāri", "paralelograms"]]),
           paraksts="Paralēlo malu pāru skaits sadala četrstūrus trīs grupās.",
           fakti=["Četrstūrus šķiro pēc paralēlo malu pāru skaita.",
                  "Trapecei ir viens paralēlu malu pāris.",
                  "Paralelogramam - divi pāri."]),

    Doma("Klasifikācija",
         "Katra nākamā grupa ir iepriekšējās daļa ar papildu pazīmi.",
         soli=[
             "Saskaiti paralēlo malu pārus.",
             "Divi pāri - paralelograms; tālāk skaties malas un leņķus.",
             "Visas malas vienādas - rombs; visi leņķi taisni - taisnstūris.",
             "Abas pazīmes kopā - kvadrāts.",
         ],
         pieze="Var šķirot arī pēc citām pazīmēm: simetrijas asu skaita, "
               "vienādu malu skaita, diagonālēm."),

    Zimejums("Rombi un taisnstūri",
             venna(["rombs"], ["taisnstūris"], ["kvadrāts"],
                   ("Malas vienādas", "Leņķi taisni")),
             paskaidro="Kvadrāts ir abās kopās: tas ir gan rombs, gan "
                       "taisnstūris."),

    Varianti("Spried", [
        {"jaut": "Kurā grupā ir kvadrāts?",
         "opcijas": ["Gan rombos, gan taisnstūros", "Tikai rombos",
                     "Tikai taisnstūros", "Trapecēs"],
         "pareizi": 0, "padoms": "Skaties Venna diagrammu."},
        {"jaut": "Cik paralēlu malu pāru ir trapecei?",
         "opcijas": ["1", "2", "0", "4"],
         "pareizi": 0, "padoms": "Pamati."},
        {"jaut": "Vai katrs taisnstūris ir paralelograms?",
         "opcijas": ["Jā", "Nē", "Tikai kvadrāts", "Tikai garš"],
         "pareizi": 0, "padoms": "Divi paralēlu malu pāri."},
        {"jaut": "Vai katrs paralelograms ir taisnstūris?",
         "opcijas": ["Nē", "Jā", "Tikai rombs", "Tikai kvadrāts"],
         "pareizi": 0, "padoms": "Leņķi var nebūt taisni."},
    ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik no šiem ir paralelogrami: kvadrāts, rombs, trapece, "
                 "taisnstūris, deltoīds?", "atb": ["3"],
         "padoms": "Kvadrāts, rombs, taisnstūris."},
        {"jaut": "Cik paralēlu malu pāru ir kvadrātam?", "atb": ["2"],
         "padoms": "Tas ir paralelograms."},
        {"jaut": "Cik simetrijas asu ir kvadrātam?", "atb": ["4"],
         "padoms": "2 diagonāles un 2 viduslīnijas."},
        {"jaut": "Cik simetrijas asu ir rombam, kas nav kvadrāts?",
         "atb": ["2"], "padoms": "Diagonāles."},
    ]),

    Pasaule("Flīžu raksts",
            Ievadi("", [
                {"jaut": "Grīdā ir 12 kvadrātu, 8 rombu (ne kvadrātu) un "
                         "6 trapeču flīzes. Cik flīzēm ir divi paralēlu malu "
                         "pāri?",
                 "atb": ["20"], "padoms": "12 + 8."},
                {"jaut": "Cik flīzēm visas malas vienādas?", "atb": ["20"],
                 "padoms": "Kvadrāti un rombi."},
                {"jaut": "Cik flīzēm visi leņķi taisni?", "atb": ["12"],
                 "padoms": "Tikai kvadrāti."},
            ]),
            pavediens="maja",
            konteksts="Flīžu rakstos izmanto dažādus četrstūrus; šķirošana "
                      "palīdz pasūtīt pareizo skaitu.",
            kapec="Kvadrāts pieder gan rombiem, gan taisnstūriem."),

    Kopsavilkums([
        "Klasificēju četrstūrus pēc paralēlo malu pāru skaita.",
        "Zinu, kā saistīti paralelograms, rombs, taisnstūris un kvadrāts.",
        "Izdomāju savu klasifikācijas pazīmi.",
    ]),

    Majas([
        "Uzzīmē shēmu «četrstūri → paralelogrami → rombi, taisnstūri → "
        "kvadrāti».",
        "Atrodi mājās katra veida četrstūri.",
        "Klasificē četrstūrus pēc simetrijas asu skaita.",
    ]),
]
