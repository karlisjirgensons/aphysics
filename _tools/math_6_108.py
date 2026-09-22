# -*- coding: utf-8 -*-
"""6. klase, 108. stunda: «Kā izveidot virkni ar vienādu soli?»

Virkne ir tas pats, ko skolēni jau darīja, skaitot ar soli - tikai tagad to
pieraksta un turpina abos virzienos. Negatīvie skaitļi te parādās paši no
sevis, kad virkne šķērso nulli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis,
                         taisne)

TEMA = "Kā izveidot virkni ar vienādu soli?"

MERKIS = ("Veidosim negatīvu skaitļu virkni ar dotu attālumu starp blakus "
          "skaitļiem.")

SATURS = [
    Sakums("Soļi, kas iet caur nulli",
           zimejums=restis([["−12", "−9", "−6", "−3", "0", "3"]],
                           "solis 3"),
           paraksts="Katrs nākamais skaitlis ir par 3 lielāks. Nulle ir "
                    "viens no virknes locekļiem.",
           fakti=["Virkni nosaka sākuma skaitlis un solis.",
                  "Solis var būt gan pozitīvs, gan negatīvs.",
                  "Ja solis ir negatīvs, virkne iet pa kreisi."]),

    Doma("Sākums un solis nosaka visu virkni",
         "Virkni ar vienādu soli veido, katram loceklim pieskaitot vienu un "
         "to pašu skaitli; negatīvs solis nozīmē virzienu pa kreisi.",
         soli=[
             "Pieraksti sākuma skaitli.",
             "Nosaki soli un tā zīmi.",
             "Pieskaiti soli un pieraksti nākamo locekli.",
             "Atkārto, cik reižu vajag.",
             "Pārbaudi: visām starpībām jābūt vienādām.",
         ],
         pieze="Virkni var turpināt arī atpakaļ: no sākuma skaitļa atņem "
               "soli. Tā iegūst locekļus, kas ir pirms dotā - un tie mēdz "
               "būt negatīvi."),

    Paraugs("Izveido virkni",
            uzd="Sāc no −12 ar soli 3 un pieraksti sešus locekļus.",
            soli=[
                ("Sākums: −12",
                 "Pirmais loceklis."),
                ("−12 + 3 = −9",
                 "Otrais."),
                ("−9 + 3 = −6; −6 + 3 = −3",
                 "Trešais un ceturtais."),
                ("−3 + 3 = 0; 0 + 3 = 3",
                 "Piektais un sestais."),
                ("Starpība vienmēr ir 3",
                 "Pārbaude."),
            ],
            atbilde="−12; −9; −6; −3; 0; 3"),

    Ievadi("Turpini virkni", [
        {"jaut": "Virkne −12; −9; −6; ... Kāds ir nākamais?",
         "atb": ["-3", "−3"], "padoms": "Solis 3."},
        {"jaut": "Virkne 5; 1; −3; ... Kāds ir nākamais?",
         "atb": ["-7", "−7"], "padoms": "Solis −4."},
        {"jaut": "Virkne −20; −15; −10; ... Kāds ir nākamais?",
         "atb": ["-5", "−5"], "padoms": "Solis 5."},
        {"jaut": "Virkne −1; −3; −5; ... Kāds ir nākamais?",
         "atb": ["-7", "−7"], "padoms": "Solis −2."},
        {"jaut": "Virkne sākas ar −8, solis 4. Kāds ir ceturtais loceklis?",
         "atb": ["4"], "padoms": "−8, −4, 0, 4."},
        {"jaut": "Virkne sākas ar 6, solis −3. Kāds ir piektais loceklis?",
         "atb": ["-6", "−6"], "padoms": "6, 3, 0, −3, −6."},
    ], pamats=4),

    Varianti("Kāds ir solis?", [
        {"jaut": "Virknē −10; −7; −4 solis ir...",
         "opcijas": ["3", "−3", "7", "−7"],
         "pareizi": 0,
         "padoms": "Katrs nākamais lielāks."},
        {"jaut": "Virknē 4; 0; −4 solis ir...",
         "opcijas": ["−4", "4", "0", "8"],
         "pareizi": 0,
         "padoms": "Skaitļi sarūk."},
        {"jaut": "Ja solis ir negatīvs, virkne...",
         "opcijas": ["sarūk", "aug", "nemainās", "lec"],
         "pareizi": 0,
         "padoms": "Kustība pa kreisi."},
        {"jaut": "Kā pārbaudīt, vai virknei ir vienāds solis?",
         "opcijas": ["Salīdzināt visas blakus starpības",
                     "Paskatīties uz pirmo locekli",
                     "Saskaitīt locekļus", "Pārbaudīt nevar"],
         "pareizi": 0,
         "padoms": "Visām starpībām jāsakrīt."},
    ], pamats=4),

    Pasaule("Kā dzesē paraugu?",
            Ievadi("", [
                {"jaut": "Temperatūra sākas ar 8 °C un krīt par 4 grādiem "
                         "stundā. Cik grādu ir pēc trim stundām?",
                 "atb": ["-4", "−4"], "padoms": "8, 4, 0, −4."},
                {"jaut": "Cik grādu ir pēc piecām stundām?",
                 "atb": ["-12", "−12"], "padoms": "Vēl divi soļi."},
                {"jaut": "Pēc cik stundām temperatūra sasniedz 0 °C?",
                 "atb": ["2"], "padoms": "8 : 4."},
                {"jaut": "Cits paraugs sākas ar −20 °C un silst par 5 "
                         "grādiem stundā. Cik grādu ir pēc četrām stundām?",
                 "atb": ["0"], "padoms": "−20, −15, −10, −5, 0."},
            ]),
            pavediens="planeta",
            konteksts="Laboratorijā temperatūru maina vienmērīgi, tāpēc "
                      "mērījumi veido virkni ar vienādu soli.",
            kapec="Zinot sākumu un soli, var paredzēt jebkuru mērījumu."),

    Zimejums("Virkne uz skaitļu taisnes",
             taisne(-12, 3, 3, [(-12, "1."), (-6, "3."), (0, "5.")]),
             paskaidro="Katri divi blakus locekļi ir vienādā attālumā - "
                       "tieši tas padara virkni par virkni.",
             ievads="Uz taisnes vienāds solis ir redzams uzreiz."),

    Kopsavilkums([
        "Veidoju virkni ar dotu sākumu un soli.",
        "Turpinu virkni abos virzienos.",
        "Nosaku soli no diviem blakus locekļiem.",
        "Pārbaudu, vai visas starpības ir vienādas.",
    ]),

    Majas([
        "Izveido virkni no −15 ar soli 5 un pieraksti sešus locekļus.",
        "Izveido virkni no 10 ar soli −4.",
        "Pieraksti, pēc cik soļiem katra virkne šķērso nulli.",
    ]),
]
