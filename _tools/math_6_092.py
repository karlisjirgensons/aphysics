# -*- coding: utf-8 -*-
"""6. klase, 92. stunda: «Kā pierakstīt problēmas risinājumu?»

Pēdējais mikrotemats tematā - procentu problēmas. Te vairs nepietiek ar
atbildi: jāpieraksta ceļš, pa kuru tā iegūta. Nezināmais dabū burtu, un tas
ir pirmais solis uz vienādojumiem 7. klasē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pierakstīt problēmas risinājumu?"

MERKIS = ("Iemācīsimies pierakstīt situācijas risinājumu ar izteiksmi vai "
          "vienādību, kas satur nezināmo.")

SATURS = [
    Sakums("Nezināmajam dod vārdu",
           fakti=["Ja nezināmo apzīmē ar burtu, uzdevumu var pierakstīt.",
                  "Pieraksts «0,3 · x = 18» aizstāj trīs teikumus.",
                  "No pieraksta redzams, kura darbība ir vajadzīga."]),

    Doma("Vispirms apzīmē, tad pieraksti",
         "Problēmas risinājumu pieraksta trijos soļos: apzīmē nezināmo ar "
         "burtu, uzraksti izteiksmi vai vienādību un tikai tad rēķini.",
         soli=[
             "Izlasi uzdevumu un pasvītro, ko meklē.",
             "Apzīmē to ar burtu un pieraksti, ko tas nozīmē.",
             "Pieraksti sakarību starp zināmo un nezināmo.",
             "Atrisini un pieraksti atbildi ar mērvienību.",
             "Pārbaudi, vai atbilde iederas uzdevuma tekstā.",
         ],
         pieze="Apzīmējumu raksta ar vārdiem: «x - sākotnējā cena eiro». Bez "
               "tā pieraksts neko nepasaka ne skolotājam, ne pašam pēc "
               "nedēļas."),

    Paraugs("Pieraksti un atrisini",
            uzd="Pēc 30 % atlaides prece maksā 42 €. Cik tā maksāja sākumā?",
            soli=[
                ("x - sākotnējā cena eiro",
                 "Apzīmējums ar vārdiem."),
                ("Pēc atlaides maksā 70 % no x",
                 "100 % − 30 %."),
                ("0,7 · x = 42",
                 "Vienādība ar nezināmo."),
                ("x = 42 : 0,7 = 60",
                 "Atrisina."),
                ("Pārbaude: 70 % no 60 ir 42",
                 "Sakrīt ar doto."),
            ],
            atbilde="60 €"),

    Ievadi("Pieraksti un izrēķini", [
        {"jaut": "0,7 · x = 42. Cik ir x?",
         "atb": ["60"], "padoms": "42 : 0,7."},
        {"jaut": "0,25 · x = 15. Cik ir x?",
         "atb": ["60"], "padoms": "15 : 0,25."},
        {"jaut": "Pēc 20 % atlaides maksā 64 €. Cik maksāja sākumā?",
         "atb": ["80"], "padoms": "0,8 · x = 64."},
        {"jaut": "Pēc 40 % atlaides maksā 36 €. Cik maksāja sākumā?",
         "atb": ["60"], "padoms": "0,6 · x = 36."},
        {"jaut": "35 % no x ir 21. Cik ir x?",
         "atb": ["60"], "padoms": "21 : 0,35."},
        {"jaut": "x pieauga par 10 % un kļuva 44. Cik bija x?",
         "atb": ["40"], "padoms": "1,1 · x = 44."},
    ], pamats=4,
        ievads="Vispirms pieraksti vienādību, tikai tad rēķini."),

    Varianti("Kurš pieraksts ir pareizs?", [
        {"jaut": "«Pēc 30 % atlaides maksā 42 €.» Kurš pieraksts der?",
         "opcijas": ["0,7 · x = 42", "0,3 · x = 42",
                     "x + 42 = 30", "x : 0,3 = 42"],
         "pareizi": 0,
         "padoms": "Maksā atlikušos procentus."},
        {"jaut": "«25 % no skaitļa ir 15.» Kurš pieraksts der?",
         "opcijas": ["0,25 · x = 15", "x : 0,25 = 15",
                     "25 · x = 15", "x − 25 = 15"],
         "pareizi": 0,
         "padoms": "Procenti no nezināmā."},
        {"jaut": "Ko obligāti pieraksta pie burta?",
         "opcijas": ["Ko tas nozīmē un mērvienību", "Tikai burtu",
                     "Atbildi", "Neko"],
         "pareizi": 0,
         "padoms": "«x - cena eiro»."},
        {"jaut": "«Skaitlis pieauga par 10 % un kļuva 44.» Kurš pieraksts "
                 "der?",
         "opcijas": ["1,1 · x = 44", "0,9 · x = 44",
                     "x + 10 = 44", "0,1 · x = 44"],
         "pareizi": 0,
         "padoms": "110 % no sākotnējā."},
    ], pamats=4),

    Pasaule("Cik bija sākumā?",
            Ievadi("", [
                {"jaut": "Pēc 15 % atlaides biļete maksā 34 €. Cik eiro tā "
                         "maksāja sākumā?",
                 "atb": ["40"], "padoms": "0,85 · x = 34."},
                {"jaut": "Cik eiro bija atlaide?",
                 "atb": ["6"], "padoms": "40 − 34."},
                {"jaut": "Grupā skolēnu skaits pieauga par 20 % un kļuva 36. "
                         "Cik bija sākumā?",
                 "atb": ["30"], "padoms": "1,2 · x = 36."},
                {"jaut": "Par cik skolēniem tas pieauga?",
                 "atb": ["6"], "padoms": "36 − 30."},
            ]),
            pavediens="celojums",
            konteksts="Ceļojuma cenas mainās vairākas reizes - lai saprastu, "
                      "vai piedāvājums ir izdevīgs, jāzina sākotnējā cena.",
            kapec="Vienādība ar nezināmo pieraksta visu uzdevumu vienā "
                  "rindā."),

    Kopsavilkums([
        "Apzīmēju nezināmo ar burtu un pierakstu, ko tas nozīmē.",
        "Veidoju izteiksmi vai vienādību no uzdevuma teksta.",
        "Atrisinu to un pierakstu atbildi ar mērvienību.",
        "Pārbaudu, vai atbilde iederas uzdevuma tekstā.",
    ]),

    Majas([
        "Pieraksti ar vienādību: «pēc 25 % atlaides maksā 45 €».",
        "Atrisini to un pārbaudi atbildi.",
        "Izdomā savu uzdevumu un pieraksti tā vienādību.",
    ]),
]
