# -*- coding: utf-8 -*-
"""6. klase, 148. stunda: «Kāda zīme būs rezultātam?»

Otra puse likumam: divu negatīvu skaitļu reizinājums. To izsecina no
virknes, tāpat kā atņemšanu iepriekšējā tematā - virkne turpinās vienmērīgi,
un citāda atbilde to salauztu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāda zīme būs rezultātam?"

MERKIS = ("Formulēsim likumu par reizinājuma zīmi un noteiksim to pirms "
          "aprēķina.")

SATURS = [
    Sakums("Virkne, kas neļauj kļūdīties",
           zimejums=restis([["3 · (−4)", "2 · (−4)", "1 · (−4)", "0 · (−4)",
                             "(−1) · (−4)"],
                            ["−12", "−8", "−4", "0", "4"]]),
           paraksts="Katrs nākamais reizinājums ir par 4 lielāks. Virkne "
                    "neapstājas pie nulles.",
           fakti=["Divu negatīvu skaitļu reizinājums ir pozitīvs.",
                  "Vienādas zīmes dod plusu, dažādas - mīnusu.",
                  "Zīmi var pateikt pirms rēķina."]),

    Doma("Vienādas zīmes - pluss, dažādas - mīnuss",
         "Reizinājuma zīmi nosaka reizinātāju zīmes: vienādas dod pozitīvu "
         "rezultātu, dažādas - negatīvu.",
         soli=[
             "Salīdzini abu reizinātāju zīmes.",
             "Ja tās sakrīt, rezultāts būs pozitīvs.",
             "Ja atšķiras, rezultāts būs negatīvs.",
             "Sareizini moduļus.",
             "Pieliec noteikto zīmi.",
         ],
         pieze="Dalīšanai likums ir tas pats: vienādas zīmes dod plusu, "
               "dažādas - mīnusu. Tāpēc abas darbības mācās kopā."),

    Paraugs("Vispirms zīme, tad moduļi",
            uzd="Cik ir (−4) · (−7) un (−4) · 7?",
            soli=[
                ("(−4) · (−7): abas zīmes ir mīnusi",
                 "Vienādas - rezultāts pozitīvs."),
                ("Moduļi: 4 · 7 = 28",
                 "Rezultāts 28."),
                ("(−4) · 7: zīmes atšķiras",
                 "Rezultāts negatīvs."),
                ("Moduļi: 4 · 7 = 28, zīme mīnus",
                 "Rezultāts −28."),
            ],
            atbilde="28 un −28"),

    Ievadi("Nosaki zīmi un izrēķini", [
        {"jaut": "Cik ir (−4) · (−7)?",
         "atb": ["28"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir (−4) · 7?",
         "atb": ["-28", "−28"], "padoms": "Dažādas zīmes."},
        {"jaut": "Cik ir (−5) · (−5)?",
         "atb": ["25"], "padoms": "Abas zīmes mīnusi."},
        {"jaut": "Cik ir 6 · (−9)?",
         "atb": ["-54", "−54"], "padoms": "6 · 9, zīme mīnus."},
        {"jaut": "Cik ir (−12) · (−1)?",
         "atb": ["12"], "padoms": "Vienādas zīmes."},
        {"jaut": "Cik ir (−8) · 0?",
         "atb": ["0"], "padoms": "Reizinājums ar nulli."},
    ], pamats=4,
        ievads="Vispirms pasaki zīmi, tikai tad reizini moduļus."),

    Petijums("Turpini virkni pats",
             vajag="burtnīca",
             soli=[
                 "Pieraksti virkni 3 · (−5); 2 · (−5); 1 · (−5); 0 · (−5).",
                 "Izrēķini katru reizinājumu.",
                 "Pieraksti, par cik aug katrs nākamais.",
                 "Turpini virkni ar (−1) · (−5) un (−2) · (−5).",
                 "Formulē likumu par zīmi.",
             ],
             secinajums="Lai virkne turpinātos vienmērīgi, (−1) · (−5) ir "
                        "jābūt 5 - tāpēc divu negatīvu reizinājums ir "
                        "pozitīvs."),

    Varianti("Kāda būs zīme?", [
        {"jaut": "Divu negatīvu skaitļu reizinājums ir...",
         "opcijas": ["pozitīvs", "negatīvs", "nulle", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Vienādas zīmes."},
        {"jaut": "Pozitīva un negatīva skaitļa reizinājums ir...",
         "opcijas": ["negatīvs", "pozitīvs", "nulle", "nevar zināt"],
         "pareizi": 0,
         "padoms": "Dažādas zīmes."},
        {"jaut": "(−3) · (−3) ir vienāds ar...",
         "opcijas": ["9", "−9", "6", "−6"],
         "pareizi": 0,
         "padoms": "Vienādas zīmes, moduļi 3 un 3."},
        {"jaut": "Dalīšanai zīmju likums ir...",
         "opcijas": ["tāds pats kā reizināšanai", "pretējs",
                     "cits", "nav likuma"],
         "pareizi": 0,
         "padoms": "Abas darbības mācās kopā."},
    ], pamats=4),

    Pasaule("Cik bija pirms tam?",
            Ievadi("", [
                {"jaut": "Katru dienu konts sarūk par 15 €. Cik eiro bija "
                         "pirms 4 dienām salīdzinājumā ar šodienu?",
                 "atb": ["60"], "padoms": "(−4) · (−15)."},
                {"jaut": "Temperatūra krīt par 2 grādiem stundā. Par cik "
                         "grādiem siltāks bija pirms 5 stundām?",
                 "atb": ["10"], "padoms": "(−5) · (−2)."},
                {"jaut": "Cik grādu aukstāks būs pēc 5 stundām?",
                 "atb": ["-10", "−10"], "padoms": "5 · (−2)."},
                {"jaut": "Zonde nolaižas par 3 m minūtē. Cik metru augstāk "
                         "tā bija pirms 6 minūtēm?",
                 "atb": ["18"], "padoms": "(−6) · (−3)."},
            ]),
            pavediens="planeta",
            konteksts="«Pirms» ir negatīvs laiks, un krišana ir negatīva "
                      "izmaiņa - tāpēc rezultāts sanāk pozitīvs.",
            kapec="Divi negatīvi virzieni kopā dod pozitīvu rezultātu."),

    Kopsavilkums([
        "Nosaku reizinājuma zīmi pirms aprēķina.",
        "Zinu: vienādas zīmes dod plusu, dažādas - mīnusu.",
        "Pamatoju likumu ar virkni.",
        "Lietoju to pašu likumu arī dalīšanai.",
    ]),

    Majas([
        "Nosaki zīmi un izrēķini (−6) · (−8); 6 · (−8); (−6) · 8.",
        "Turpini virkni 4 · (−3); 3 · (−3); ... līdz (−2) · (−3).",
        "Pieraksti likumu saviem vārdiem.",
    ]),
]
