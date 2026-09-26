# -*- coding: utf-8 -*-
"""8. klase, 51. stunda: «Kurus skaitļus var izvilkt precīzi?»

Precīzi sakni var izvilkt no pilniem kvadrātiem - arī no daļām un
decimāldaļām, kuru skaitītājs un saucējs ir kvadrāti. Kvadrātu tabula līdz
20^2 ir rīks, ko lieto līdz pat eksāmenam.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kurus skaitļus var izvilkt precīzi?"

MERKIS = ("Noteiksim kvadrātsaknes precīzo vērtību, ja zemsaknes izteiksme "
          "ir pilns kvadrāts.")

SATURS = [
    Sakums("Kvadrātu tabula",
           zimejums=restis([["11²", "12²", "13²", "14²", "15²"],
                            ["121", "144", "169", "196", "225"],
                            ["16²", "17²", "18²", "19²", "20²"],
                            ["256", "289", "324", "361", "400"]]),
           paraksts="Ja skaitlis ir tabulā, sakni var izvilkt precīzi.",
           fakti=["Pilns kvadrāts - naturāla skaitļa kvadrāts.",
                  "√196 = 14, jo 14² = 196.",
                  "√200 nav tabulā - precīzi to neizvilkt."]),

    Doma("Kad sakne ir precīza?",
         "Sakne ir racionāls skaitlis tikai tad, ja zemsaknes skaitlis ir "
         "racionāla skaitļa kvadrāts.",
         soli=[
             "Veselie: tabulā vai sadalot pirmreizinātājos pāros.",
             "Decimāldaļa: aiz komata pāra skaits ciparu (0,49; 1,44).",
             "Daļa: skaitītājs un saucējs - kvadrāti: √{9|25} = {3|5}.",
             "Lieli skaitļi ar nullēm: √2500 = 50, √(0,0004) = 0,02.",
         ],
         pieze="Pēdējais cipars palīdz: kvadrāts nekad nebeidzas ar 2, 3, "
               "7 vai 8 - tāpēc √(2023) noteikti nav vesels."),

    Paraugs("Sadali pāros",
            uzd="Izvelc √576.",
            soli=[
                ("576 = 2^6 · 3^2", "Pirmreizinātāji."),
                ("= (2^3 · 3)^2", "Pāros - puse kāpinātāju."),
                ("√576 = 8 · 3 = 24", "Pārbaude: 24 · 24 = 576."),
            ],
            atbilde="24"),

    Ievadi("Izvelc precīzi", [
        {"jaut": "√169", "atb": ["13"], "padoms": "Tabula."},
        {"jaut": "√(1,44)", "atb": ["1,2", "1.2"], "padoms": "12^2 = 144."},
        {"jaut": "√{25|64} - atbildi raksti kā a/b",
         "atb": ["{5|8}", "5/8"], "padoms": "{5|8}."},
        {"jaut": "√4900", "atb": ["70"], "padoms": "√49 · √100."},
        {"jaut": "√(0,0016)", "atb": ["0,04", "0.04"],
         "padoms": "0,04^2."},
        {"jaut": "√324", "atb": ["18"], "padoms": "Tabula."},
    ], pamats=4),

    Varianti("Vai var izvilkt precīzi?", [
        {"jaut": "√(0,9)",
         "opcijas": ["Nē", "Jā, 0,3", "Jā, 0,03", "Jā, 0,45"],
         "pareizi": 0, "padoms": "0,3^2 = 0,09."},
        {"jaut": "√{36|50}",
         "opcijas": ["Nē (50 nav kvadrāts)", "Jā, {6|5}", "Jā, {6|7}",
                     "Jā, {18|25}"],
         "pareizi": 0, "padoms": "Saīsini: {18|25} - 18 nav kvadrāts."},
        {"jaut": "Kurš skaitlis noteikti nav pilns kvadrāts?",
         "opcijas": ["2027", "2025", "1024", "1600"],
         "pareizi": 0, "padoms": "Beidzas ar 7."},
    ]),

    Pasaule("Futbola laukums",
            Ievadi("", [
                {"jaut": "Kvadrātveida treniņu laukums 1600 m². Cik m gara "
                         "mala?",
                 "atb": ["40"], "padoms": "√1600."},
                {"jaut": "Cik metru ir apkārt laukumam?",
                 "atb": ["160"], "padoms": "4 · 40."},
                {"jaut": "Kvadrātveida mini laukums ir 4 reizes mazāks "
                         "(400 m²). Cik reižu īsāka mala?",
                 "atb": ["2"], "padoms": "√400 = 20."},
            ]),
            pavediens="sports",
            konteksts="Laukumu plāno pēc platības, bet līnijas velk pēc "
                      "malas garuma.",
            kapec="4 reizes mazāks laukums - tikai 2 reizes īsāka mala."),

    Kopsavilkums([
        "Zinu kvadrātus līdz 20^2.",
        "Izvelku sakni no pilna kvadrāta, daļas un decimāldaļas.",
        "Nosaku, kad sakne nav izvelkama precīzi.",
    ]),

    Majas([
        "Izvelc: √256, √(0,81), √{49|100}, √(360 000).",
        "Sadali pirmreizinātājos un izvelc √784.",
        "Pārbaudi: vai √(2025) ir vesels skaitlis?",
    ]),
]
