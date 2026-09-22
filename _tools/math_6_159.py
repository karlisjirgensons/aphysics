# -*- coding: utf-8 -*-
"""6. klase, 159. stunda: «Kad pāriet uz viena veida daļskaitļiem?»

Stunda par izvēli, kas izšķir rēķina garumu. Ja izteiksmē ir gan daļas, gan
decimāldaļas, vispirms jāizvēlas viens pieraksts - un izvēle nav vienalga:
{1|3} decimālpierakstā nav precīzs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kad pāriet uz viena veida daļskaitļiem?"

MERKIS = ("Izvēlēsimies vienotu daļskaitļu pierakstu aprēķinam un pamatosim "
          "izvēli.")

SATURS = [
    Sakums("Viens pieraksts visai izteiksmei",
           zimejums=restis([["1/2", "1/4", "1/5", "1/3"],
                            ["0,5", "0,25", "0,2", "nav precīzs"]]),
           paraksts="Trīs pirmās daļas decimālpierakstā ir precīzas, "
                    "ceturtā - nav.",
           fakti=["Ja saucējā ir tikai 2 un 5, decimāldaļa ir precīza.",
                  "Ja saucējā ir 3, 6, 7 vai 9, tā nav precīza.",
                  "Tad visu izteiksmi rēķina parastajās daļās."]),

    Doma("Skaties uz saucējiem",
         "Pieraksta izvēli nosaka saucēji: ja visus var paplašināt līdz 10, "
         "100 vai 1000, ērtāk ir decimāldaļas; ja ne - parastās daļas.",
         soli=[
             "Pieraksti visu daļu saucējus.",
             "Pārbaudi, vai katrā ir tikai reizinātāji 2 un 5.",
             "Ja jā - pārej uz decimāldaļām.",
             "Ja nē - pārej uz parastajām daļām.",
             "Pārveido visus skaitļus izvēlētajā pierakstā.",
         ],
         pieze="Reizināšanai un dalīšanai parastās daļas ir ērtākas gandrīz "
               "vienmēr, jo tur var saīsināt. Decimāldaļas uzvar "
               "saskaitīšanā un salīdzināšanā."),

    Paraugs("Izvēlies pierakstu",
            uzd="Kurā pierakstā rēķināt {1|4} + 0,3 un {1|3} · 0,6?",
            soli=[
                ("{1|4} = 0,25 - precīzi",
                 "Saucējā tikai divnieki."),
                ("0,25 + 0,3 = 0,55",
                 "Decimāldaļās ērtāk."),
                ("{1|3} decimālpierakstā nav precīzs",
                 "Saucējā ir trijnieks."),
                ("0,6 = {3|5}; {1|3} · {3|5} = {1|5}",
                 "Parastajās daļās precīzi."),
            ],
            atbilde="0,55 un {1|5}"),

    Ievadi("Izrēķini ērtākajā pierakstā", [
        {"jaut": "Cik ir {1|4} + 0,3?",
         "atb": ["0,55", "0.55"], "padoms": "0,25 + 0,3."},
        {"jaut": "Cik ir {1|3} · 0,6? Atbildi raksti kā a/b.",
         "atb": ["1/5", "3/15"], "padoms": "{1|3} · {3|5}."},
        {"jaut": "Cik ir {1|2} + 0,25?",
         "atb": ["0,75", "0.75"], "padoms": "0,5 + 0,25."},
        {"jaut": "Cik ir {2|3} : 0,5?",
         "atb": ["4/3", "1 1/3"], "padoms": "{2|3} · 2."},
        {"jaut": "Cik ir 0,8 − {1|5}?",
         "atb": ["0,6", "0.6"], "padoms": "{1|5} = 0,2."},
        {"jaut": "Cik ir {1|6} · 0,3? Atbildi raksti kā a/b.",
         "atb": ["1/20", "3/60"], "padoms": "{1|6} · {3|10}."},
    ], pamats=4,
        ievads="Vispirms paskaties uz saucējiem."),

    Varianti("Kurš pieraksts te der?", [
        {"jaut": "Izteiksmē ar {1|3} ērtāk rēķināt...",
         "opcijas": ["parastajās daļās", "decimāldaļās",
                     "procentos", "jebkurā"],
         "pareizi": 0,
         "padoms": "{1|3} decimālpierakstā nav precīzs."},
        {"jaut": "Izteiksmē ar {1|4} un 0,3 ērtāk rēķināt...",
         "opcijas": ["decimāldaļās", "parastajās daļās",
                     "procentos", "jebkurā"],
         "pareizi": 0,
         "padoms": "{1|4} = 0,25 precīzi."},
        {"jaut": "Kuru daļu decimālpierakstā var izteikt precīzi?",
         "opcijas": ["{3|8}", "{1|3}", "{1|6}", "{2|7}"],
         "pareizi": 0,
         "padoms": "Saucējā tikai divnieki."},
        {"jaut": "Reizināšanai un dalīšanai parasti ērtākas ir...",
         "opcijas": ["parastās daļas", "decimāldaļas",
                     "procenti", "veseli skaitļi"],
         "pareizi": 0,
         "padoms": "Tur var saīsināt."},
    ], pamats=4),

    Pasaule("Cik sanāk kopā?",
            Ievadi("", [
                {"jaut": "Recepte: {1|4} l piena un 0,3 l ūdens. Cik litru "
                         "kopā?",
                 "atb": ["0,55", "0.55"], "padoms": "0,25 + 0,3."},
                {"jaut": "{1|3} no 0,9 kg miltu. Cik kilogramu tas ir?",
                 "atb": ["0,3", "0.3"], "padoms": "0,9 : 3."},
                {"jaut": "{1|2} kg cukura un 0,25 kg sāls. Cik kg kopā?",
                 "atb": ["0,75", "0.75"], "padoms": "0,5 + 0,25."},
                {"jaut": "{2|5} no 1,5 l sulas. Cik litru tas ir?",
                 "atb": ["0,6", "0.6"], "padoms": "1,5 : 5 · 2."},
            ]),
            pavediens="virtuve",
            konteksts="Receptēs daļas un decimāldaļas ir sajauktas - bet "
                      "rēķināt var tikai vienā pierakstā.",
            kapec="Pareiza izvēle padara rēķinu precīzu un īsu."),

    Kopsavilkums([
        "Izvēlos vienotu pierakstu pirms rēķināšanas.",
        "Pārbaudu saucējus: vai daļu var precīzi izteikt decimālpierakstā.",
        "Pārveidoju visus skaitļus izvēlētajā pierakstā.",
        "Pamatoju savu izvēli.",
    ]),

    Majas([
        "Izvēlies pierakstu un izrēķini {3|4} + 0,2 un {1|6} · 0,4.",
        "Pieraksti, kāpēc katram izvēlējies tieši to pierakstu.",
        "Atrodi daļu, kuru decimālpierakstā nevar izteikt precīzi.",
    ]),
]
