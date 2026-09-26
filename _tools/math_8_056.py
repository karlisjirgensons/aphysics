# -*- coding: utf-8 -*-
"""8. klase, 56. stunda: «Kā salīdzināt saknes?»

Bloka noslēgums: salīdzina un sakārto dažādi pierakstītus reālus skaitļus.
Galvenais paņēmiens - visu ienest zem saknes: 3√2 = √18, un tad salīdzina
zemsaknes skaitļus. Tas sagatavo reizinātāja iznešanu nākamajā blokā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, taisne)

TEMA = "Kā salīdzināt saknes?"

MERKIS = ("Salīdzināsim dažādā veidā pierakstītus reālus skaitļus un "
          "sakārtosim tos.")

SATURS = [
    Sakums("Kurš lielāks: 3√2 vai 2√3?",
           zimejums=taisne(3, 5, 0.5, [(3.464, "2√3"), (4.243, "3√2")],
                           sikas=5),
           paraksts="3√2 = √18, 2√3 = √12 - tātad 3√2 ir lielāks.",
           fakti=["Lielāka zemsaknes izteiksme - lielāka sakne.",
                  "Reizinātāju var ienest zem saknes kvadrātā.",
                  "Tad salīdzina tikai zemsaknes skaitļus."]),

    Doma("Salīdzināšanas paņēmieni",
         "Pozitīvus skaitļus salīdzina, salīdzinot to kvadrātus: ja a > b > 0, "
         "tad a^2 > b^2.",
         soli=[
             "Divas saknes: salīdzina zemsaknes skaitļus: √11 < √13.",
             "Sakne un skaitlis: 4 = √16, tātad √15 < 4.",
             "Reizinātājs pirms saknes: 3√2 = √(9 · 2) = √18.",
             "Daudzi skaitļi: pārveido visus par tuvinājumiem vai kvadrātiem.",
         ]),

    Paraugs("Sakārto",
            uzd="Sakārto augošā secībā: 5, 2√6, √26, 4,9.",
            soli=[
                ("5 = √25; 2√6 = √24; √26; 4,9 = √(24,01)",
                 "Visi zem saknes."),
                ("24 < 24,01 < 25 < 26", "Salīdzina zemsaknes."),
                ("2√6 < 4,9 < 5 < √26", "Secība."),
            ],
            atbilde="2√6; 4,9; 5; √26"),

    Varianti("Kurš lielāks?", [
        {"jaut": "√30 vai 5,5?",
         "opcijas": ["5,5 (= √(30,25))", "√30", "Vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "5,5^2 = 30,25."},
        {"jaut": "2√5 vai √19?",
         "opcijas": ["2√5 (= √20)", "√19", "Vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "4 · 5 = 20."},
        {"jaut": "4√3 vai 3√5?",
         "opcijas": ["3√5 (= √45)", "4√3 (= √48)", "Vienādi",
                     "Nevar noteikt"],
         "pareizi": 1, "padoms": "48 > 45."},
        {"jaut": "−√10 vai −3?",
         "opcijas": ["−3", "−√10", "Vienādi", "Nevar noteikt"],
         "pareizi": 0, "padoms": "Negatīviem - otrādi."},
    ]),

    Ievadi("Ienes zem saknes", [
        {"jaut": "2√7 = √?", "atb": ["28"], "padoms": "4 · 7."},
        {"jaut": "5√2 = √?", "atb": ["50"], "padoms": "25 · 2."},
        {"jaut": "10√(0,3) = √?", "atb": ["30"], "padoms": "100 · 0,3."},
        {"jaut": "Lielākais vesels skaitlis, mazāks par 3√11?",
         "atb": ["9"], "padoms": "√99; 9^2 = 81, 10^2 = 100."},
    ]),

    Pasaule("Kurš ekrāns lielāks?",
            Ievadi("", [
                {"jaut": "Kvadrātveida planšete ar laukumu 450 cm². Mala "
                         "15√2 cm. Pieraksti kā √? cm",
                 "atb": ["450"], "padoms": "225 · 2."},
                {"jaut": "Otras malas 21 cm. Kuras mala garāka? (1 - "
                         "pirmās, 2 - otrās)",
                 "atb": ["1"], "padoms": "21 = √441, bet 15√2 = √450, un "
                                         "441 < 450."},
                {"jaut": "Par cik cm² lielāks ir lielākās planšetes laukums?",
                 "atb": ["9"], "padoms": "450 − 441."},
            ]),
            pavediens="tehnika",
            konteksts="Ražotāji raksta izmērus dažādi - ar saknēm, collām, "
                      "centimetriem. Salīdzināt palīdz kvadrāti.",
            kapec="Salīdzinot kvadrātus, saknes nav jāizrēķina."),

    Kopsavilkums([
        "Salīdzinu saknes pēc zemsaknes skaitļiem.",
        "Ienesu reizinātāju zem saknes.",
        "Sakārtoju reālus skaitļus dažādos pierakstos.",
    ]),

    Majas([
        "Sakārto: 3√3, 5, √24, 2√7.",
        "Salīdzini 6√2 un 2√18.",
        "Atrodi 3 dažādus pierakstus skaitlim √50.",
    ]),
]
