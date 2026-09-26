# -*- coding: utf-8 -*-
"""7. klase, 52. stunda: «Kad sakarība ir funkcija?»

Funkcija ir sakarība, kurā katrai argumenta vērtībai atbilst tieši viena
funkcijas vērtība. Automāts, kas par katru pogu izdod vienu dzērienu, ir
funkcija; automāts, kas par vienu pogu reizēm dod tēju, reizēm kafiju, - nē.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, restis)

TEMA = "Kad sakarība ir funkcija?"

MERKIS = ("Iemācīsimies lietot funkcijas definīciju, lai noteiktu, vai "
          "sakarība ir funkcija.")

SATURS = [
    Sakums("Dzērienu automāts",
           zimejums=restis([["poga", "A1", "A2", "B1", "B2"],
                            ["dzēriens", "ūdens", "sula", "tēja", "tēja"]]),
           paraksts="Katra poga - viens noteikts dzēriens.",
           fakti=["Divām pogām var būt viens dzēriens (B1 un B2) - tas ir "
                  "labi.",
                  "Bet vienai pogai nedrīkst būt divi dažādi dzērieni.",
                  "Tāds automāts ir funkcija."]),

    Doma("Katram x - tieši viens y",
         "Sakarību starp mainīgajiem x un y sauc par funkciju, ja katrai x "
         "vērtībai atbilst tieši viena y vērtība. Raksta y = f(x).",
         soli=[
             "Paņem katru x vērtību pēc kārtas.",
             "Paskaties, cik y tai atbilst.",
             "Ja kādai x atbilst divas vai vairāk y - nav funkcija.",
             "Ja kādai x neatbilst neviena y - arī nav funkcija (šajā "
             "kopā).",
         ],
         pieze="Dažādiem x drīkst būt vienāds y: y = x² dod 4 gan x = 2, gan "
               "x = −2. Tā joprojām ir funkcija."),

    Paraugs("Pārbaudi tabulu",
            uzd="x: 1; 2; 3; 2. y: 5; 7; 9; 8. Vai y ir x funkcija?",
            soli=[
                ("x = 2 parādās divreiz", "Pārbauda atkārtojumus."),
                ("x = 2 atbilst y = 7 un y = 8", "Divas dažādas vērtības."),
                ("Nav funkcija", "Pārkāpts «tieši viens»."),
            ],
            atbilde="Nav funkcija, jo x = 2 atbilst divas y vērtības."),

    Varianti("Funkcija vai nē?", [
        {"jaut": "Katram skolēnam - viņa dzimšanas diena.",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Katram cilvēkam - tieši viena dzimšanas diena."},
        {"jaut": "Katrai dzimšanas dienai - skolēns, kuram tā ir.",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Vienā dienā var būt dzimuši vairāki."},
        {"jaut": "x: 1; 2; 3; 4. y: 3; 3; 3; 3.",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Katram x viens y - tas pats."},
        {"jaut": "Katram skaitlim x - skaitlis, kura kvadrāts ir x.",
         "opcijas": ["Funkcija", "Nav funkcija"],
         "pareizi": 1, "jaukt": False,
         "padoms": "x = 9: gan 3, gan −3."},
    ], pamats=4),

    Zimejums("Bultu shēma",
             restis([["x", "→", "y"],
                     ["1", "→", "5"],
                     ["2", "→", "7"],
                     ["3", "→", "7"]]),
             paskaidro="No katra x iziet tieši viena bulta - funkcija."),

    Varianti("Atrodi pareizo", [
        {"jaut": "Kurš apgalvojums par funkciju ir patiess?",
         "opcijas": ["Dažādiem x var būt vienāds y",
                     "Vienam x var būt divi y",
                     "Katram y jābūt citam x",
                     "Funkcijai vienmēr ir formula"],
         "pareizi": 0,
         "padoms": "Ierobežojums ir tikai x pusē."},
        {"jaut": "Kas funkcijai jāzina, lai atrastu y?",
         "opcijas": ["x vērtība", "y vērtība", "Grafika krāsa",
                     "Nekas"],
         "pareizi": 0,
         "padoms": "Arguments nosaka vērtību."},
    ]),

    Pasaule("Skolas kods",
            Varianti("", [
                {"jaut": "Katram skolēnam e-klasē ir personas kods. Vai "
                         "«skolēns → kods» ir funkcija?",
                 "opcijas": ["Jā - katram skolēnam viens kods",
                             "Nē", "Tikai 7. klasē", "Nevar zināt"],
                 "pareizi": 0,
                 "padoms": "Tieši viens."},
                {"jaut": "Vai «klase → audzinātājs» ir funkcija, ja katrai "
                         "klasei ir viens audzinātājs?",
                 "opcijas": ["Jā", "Nē"],
                 "pareizi": 0, "jaukt": False,
                 "padoms": "Viena klase - viens audzinātājs."},
                {"jaut": "Vai «audzinātājs → klase» ir funkcija, ja viens "
                         "skolotājs audzina 2 klases?",
                 "opcijas": ["Nē", "Jā"],
                 "pareizi": 0, "jaukt": False,
                 "padoms": "Vienam divas vērtības."},
            ]),
            pavediens="skola",
            konteksts="Datubāzēs katram ierakstam ir unikāls kods - tā ir "
                      "funkcija no ieraksta uz kodu.",
            kapec="Funkcija nozīmē «nav šaubu, kura vērtība»."),

    Kopsavilkums([
        "Zinu funkcijas definīciju: katram x - tieši viens y.",
        "Pārbaudu tabulu uz atkārtotiem x.",
        "Zinu, ka dažādiem x drīkst būt vienāds y.",
        "Atrodu piemērus no dzīves.",
    ]),

    Majas([
        "Atrodi 2 sakarības no dzīves, kas ir funkcijas, un 2, kas nav.",
        "Uzzīmē bultu shēmu, kas nav funkcija.",
        "Paskaidro, kāpēc «cilvēks → vecums» ir funkcija.",
    ]),
]
