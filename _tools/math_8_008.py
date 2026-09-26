# -*- coding: utf-8 -*-
"""8. klase, 8. stunda: «Kas ir moda un amplitūda?»

Moda atbild uz «kas visbiežāk?», amplitūda - uz «cik plaši dati izkliedēti?».
Moda der arī vārdiem (visbiežākā krāsa), vidējais un mediāna - tikai
skaitļiem. Punktu diagramma uz skaitļu taisnes parāda abus uzreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Sakums, Varianti, Zimejums, kolonnas, taisne)

TEMA = "Kas ir moda un amplitūda?"

MERKIS = ("Noteiksim datu kopas modu un amplitūdu un sapratīsim, ko tās "
          "parāda.")

SATURS = [
    Sakums("Kādu izmēru apavus pasūtīt?",
           zimejums=kolonnas([("37", 3), ("38", 7), ("39", 12), ("40", 9),
                              ("41", 5), ("42", 2)]),
           paraksts="Pārdoto sporta apavu izmēri mēnesī.",
           fakti=["Visbiežāk pērk izmēru 39 - tā ir moda.",
                  "Izmēri ir no 37 līdz 42 - amplitūda 5.",
                  "Veikals pasūta visvairāk modas izmēra."]),

    Doma("Moda un amplitūda",
         "Moda ir vērtība, kas datu kopā sastopama visbiežāk. Amplitūda ir "
         "starpība starp lielāko un mazāko vērtību.",
         soli=[
             "Moda: saskaiti, cik reižu parādās katra vērtība.",
             "Modu var būt vairākas - vai nebūt nevienas.",
             "Amplitūda = lielākā − mazākā vērtība.",
             "Liela amplitūda - dati izkliedēti plaši.",
         ],
         pieze="Moda der arī datiem, kas nav skaitļi: visbiežākā krāsa, "
               "vārds vai transporta veids."),

    Paraugs("Viena kopa - četri rādītāji",
            uzd="Atzīmes: 6, 8, 7, 8, 9, 5, 8, 7. Atrodi modu, amplitūdu, "
                "mediānu un vidējo.",
            soli=[
                ("5; 6; 7; 7; 8; 8; 8; 9", "Sakārto."),
                ("Moda 8 (trīs reizes)", "Visbiežāk."),
                ("Amplitūda 9 − 5 = 4", "Lielākā − mazākā."),
                ("Mediāna (7 + 8) : 2 = 7,5", "n = 8."),
                ("Vidējais 58 : 8 = 7,25", "Summa : skaits."),
            ],
            atbilde="8; 4; 7,5; 7,25"),

    Zimejums("Punktu diagramma",
             taisne(4, 10, 1, [(5, "•"), (6, "•"), (7, "••"), (8, "•••"),
                               (9, "•")]),
             paskaidro="Augstākā kaudzīte ir moda (8); attālums no pirmā "
                       "līdz pēdējam punktam ir amplitūda (4)."),

    Ievadi("Atrodi modu un amplitūdu", [
        {"jaut": "3, 5, 5, 6, 9, 5, 2. Moda?",
         "atb": ["5"], "padoms": "5 ir trīs reizes."},
        {"jaut": "Tai pašai kopai - amplitūda?",
         "atb": ["7"], "padoms": "9 − 2."},
        {"jaut": "Temperatūras: −4, 2, −1, 3, −4 °C. Amplitūda?",
         "atb": ["7", "7 °C"], "padoms": "3 − (−4)."},
        {"jaut": "12, 15, 12, 18, 15, 20. Cik modu šai kopai?",
         "atb": ["2"], "padoms": "12 un 15 - pa divi."},
        {"jaut": "Amplitūda 15, mazākā vērtība 23. Lielākā?",
         "atb": ["38"], "padoms": "23 + 15."},
        {"jaut": "Kopā 4, 7, x ir moda 7. Kāds ir x?",
         "atb": ["7"], "padoms": "7 jāparādās biežāk."},
    ], pamats=4),

    Varianti("Kurš rādītājs der?", [
        {"jaut": "Kafejnīca grib zināt, kuru dzērienu pērk visbiežāk.",
         "opcijas": ["Modu", "Vidējo", "Amplitūdu", "Mediānu"],
         "pareizi": 0, "padoms": "Dati ir nosaukumi."},
        {"jaut": "Cik ļoti atšķiras dienas temperatūra un nakts temperatūra?",
         "opcijas": ["Amplitūdu", "Modu", "Mediānu", "Vidējo"],
         "pareizi": 0, "padoms": "Starpība."},
        {"jaut": "Kopā 2, 4, 6, 8 moda...",
         "opcijas": ["nav", "ir 5", "ir 8", "ir 2"],
         "pareizi": 0, "padoms": "Katra vērtība vienreiz."},
    ]),

    Pasaule("Sporta apavu pasūtījums",
            Ievadi("", [
                {"jaut": "Diagrammā: cik pāru pārdeva kopā?",
                 "atb": ["38"], "padoms": "3 + 7 + 12 + 9 + 5 + 2."},
                {"jaut": "Kāda daļa procentos ir modas izmērs? Noapaļo līdz "
                         "veseliem.",
                 "atb": ["32", "32 %", "32%"], "padoms": "12 : 38 ≈ 0,316."},
                {"jaut": "Nākamajā mēnesī pasūtīs 100 pārus tādās pašās "
                         "daļās. Cik pāru izmēra 39?",
                 "atb": ["32"], "padoms": "32 % no 100."},
            ]),
            pavediens="veikals",
            konteksts="Veikals pasūta preci pēc pārdošanas datiem: moda "
                      "pasaka, kā vajag visvairāk.",
            kapec="Pareizs pasūtījums - mazāk nepārdotu apavu noliktavā."),

    Kopsavilkums([
        "Atrodu modu, arī tad, ja to ir vairākas vai nav nevienas.",
        "Aprēķinu amplitūdu.",
        "Izvēlos piemērotu rādītāju situācijai.",
    ]),

    Majas([
        "Pajautā 10 cilvēkiem mīļāko krāsu un atrodi modu.",
        "Pieraksti nedēļas maksimālās temperatūras un atrodi amplitūdu.",
        "Izdomā kopu, kurai moda, mediāna un vidējais ir vienādi.",
    ]),
]
