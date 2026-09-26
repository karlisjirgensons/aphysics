# -*- coding: utf-8 -*-
"""4. klase, 128. stunda: «Kā aprēķina citi?»

Vienu daļas uzdevumu var atrisināt vairākos ceļos: dali-tad-reizini,
reizini-tad-dali, ar zīmējumu vai ar papildinājumu. Skolēns lasa un
komentē svešus risinājumus - tā viņš iemācās saprast citu domu gaitu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Sakums, Varianti, restis)

TEMA = "Kā aprēķina citi?"

MERKIS = ("Lasīsim un komentēsim dažādus risinājumus daļas vērtības "
          "aprēķināšanai.")

SATURS = [
    Sakums("Trīs skolēni - trīs ceļi: {3|4} no 40",
           zimejums=restis([["Anna", "40 : 4 = 10, 10 · 3 = 30"],
                            ["Juris", "40 · 3 = 120, 120 : 4 = 30"],
                            ["Ieva", "40 − 40 : 4 = 30"]],
                           "visiem 30"),
           fakti=["Visi trīs ceļi ir pareizi.",
                  "Ieva atrada {1|4} un atņēma to no visa."]),

    Doma("Pareizu ceļu ir vairāki",
         "Daļas vērtību var atrast, dalot un reizinot jebkurā secībā vai "
         "atņemot papildinājumu no veselā.",
         soli=[
             "Dali, tad reizini: 40 : 4 · 3 - mazāki skaitļi.",
             "Reizini, tad dali: 40 · 3 : 4 - der, ja dalīšana nesanāk gludi.",
             "Papildinājums: 40 − {1|4} no 40 - ja daļa tuvu veselajam.",
             "Izvēlies ceļu, kas konkrētajiem skaitļiem ir ērtākais.",
         ],
         pieze="{9|10} no 70: ērtāk 70 − 7 = 63 nekā 70 : 10 · 9."),

    Varianti("Kurš risinājums pareizs?", [
        {"jaut": "Marta: {2|3} no 27 = 27 : 2 · 3. Pareizi?",
         "opcijas": ["nē, jādala ar 3", "jā", "jāreizina ar 27"],
         "pareizi": 0, "padoms": "Dala ar saucēju: 27 : 3 · 2 = 18."},
        {"jaut": "Kārlis: {5|6} no 36 = 36 − 6 = 30. Pareizi?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "{1|6} no 36 = 6; 36 − 6 = 30."},
        {"jaut": "Līga: {3|5} no 25 = 25 · 3 : 5 = 15. Pareizi?",
         "opcijas": ["jā", "nē"], "pareizi": 0,
         "padoms": "75 : 5 = 15."},
        {"jaut": "Kurš ceļš ērtākais: {7|8} no 80?",
         "opcijas": ["80 − 10 = 70", "80 · 7 : 8", "80 : 7 · 8"],
         "pareizi": 0, "padoms": "{1|8} no 80 ir 10."},
    ], pamats=4),

    Ievadi("Izvēlies savu ceļu", [
        {"jaut": "{9|10} no 70 = ?", "atb": ["63"], "padoms": "70 − 7."},
        {"jaut": "{3|4} no 48 = ?", "atb": ["36"], "padoms": "48 − 12."},
        {"jaut": "{2|3} no 27 = ?", "atb": ["18"], "padoms": "9 · 2."},
        {"jaut": "{5|6} no 36 = ?", "atb": ["30"], "padoms": "36 − 6."},
    ]),

    Pasaule("Veikala atlaides",
            Ievadi("", [
                {"jaut": "Džemperis 40 €, jāmaksā {3|4} cenas. Cik €?",
                 "atb": ["30"], "padoms": "40 − 10."},
                {"jaut": "Kurpes 60 €, jāmaksā {2|3}. Cik €?", "atb": ["40"],
                 "padoms": "60 : 3 · 2."},
                {"jaut": "Mugursoma 50 €, jāmaksā {4|5}. Cik €?",
                 "atb": ["40"], "padoms": "50 − 10."},
                {"jaut": "Cik € ietaupīts uz visām trim precēm?",
                 "atb": ["40"], "padoms": "10 + 20 + 10."},
            ]),
            pavediens="veikals",
            konteksts="Atlaižu dienās cena ir daļa no sākotnējās - un gudrs "
                      "pircējs izvēlas ātrāko ceļu to izrēķināt.",
            kapec="Dažādi ceļi, viena atbilde - izvēlies ērtāko."),

    Kopsavilkums([
        "Lasu un saprotu citu risinājumus.",
        "Zinu vairākus ceļus daļas aprēķināšanai.",
        "Izvēlos ērtāko ceļu konkrētiem skaitļiem.",
    ]),

    Majas([
        "Atrisini {4|5} no 45 divos veidos.",
        "Palūdz kādam atrisināt {3|4} no 60 - kādu ceļu viņš izvēlējās?",
        "Atrodi reklāmā atlaidi un izrēķini jauno cenu.",
    ]),
]
