# -*- coding: utf-8 -*-
"""3. klase, 50. stunda: «Vai atbilde atbilst situācijai?»

Pēdējais solis katrā uzdevumā, kuru visbiežāk izlaiž. Skaitlis var būt
izrēķināts pareizi un tomēr nederēt: 2,5 autobusi, 30 bērnu klasē no 24 vai
atlikums, kas lielāks par sākotnējo summu. Šī stunda māca to pamanīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Vai atbilde atbilst situācijai?"

MERKIS = ("Pārliecināsimies, ka rezultāts ir ticams un atbilst reālajai "
          "situācijai.")

SATURS = [
    Sakums("Vai var būt divarpus autobusi?",
           zimejums=restis([["atbilde", "vai der?"],
                            ["2,5 autobusi", "nē"],
                            ["3 autobusi", "jā"],
                            ["30 bērni no 24", "nē"]],
                           "skaitlis un dzīve"),
           paraksts="Rēķins var būt pareizs, bet atbilde - neiespējama.",
           fakti=["Dažus lielumus skaita tikai veselos skaitļos.",
                  "Daļa nevar būt lielāka par veselo."]),

    Doma("Pēdējais solis ir pārbaude dzīvē",
         "Pēc rēķina pajautā sev: vai tāds skaitlis šajā situācijā vispār ir "
         "iespējams?",
         soli=[
             "Paskaties, ko skaitlis nozīmē - cilvēkus, kastes vai naudu.",
             "Pārbaudi, vai tas ir vesels skaitlis, ja tam jābūt veselam.",
             "Pārbaudi, vai daļa nav lielāka par veselo.",
             "Pārbaudi, vai atbilde nav pārāk liela vai maza.",
         ],
         pieze="Ja autobusā ietilpst 40 bērni un braukt grib 45, atbilde ir "
               "2 autobusi, nevis 1 un ceturtdaļa - cilvēkus nedala."),

    Paraugs("Cik autobusu vajag?",
            uzd="Ekskursijā brauc 45 bērni. Autobusā ietilpst 40. Cik "
                "autobusu vajag?",
            soli=[
                ("45 : 40 = 1, atlikums 5",
                 "Viens autobuss būs pilns, 5 bērni paliks."),
                ("5 bērni arī jāaizved",
                 "Viņus nevar atstāt, tāpēc vajag vēl vienu autobusu."),
                ("Vajag 2 autobusus",
                 "Atbildi noapaļo uz augšu, jo autobusu skaits ir vesels."),
            ],
            atbilde="2 autobusi"),

    Ievadi("Cik vajag pavisam?", [
        {"jaut": "50 bērni, autobusā 40 vietas. Cik autobusu vajag?",
         "atb": ["2"], "padoms": "Viens nepietiek."},
        {"jaut": "50 cepumi, kastē ietilpst 8. Cik kastu vajag?",
         "atb": ["7"], "padoms": "6 kastes ir 48 - divi cepumi paliek."},
        {"jaut": "26 bērni, galdā 6 vietas. Cik galdu vajag?",
         "atb": ["5"], "padoms": "4 galdi ir 24 vietas."},
        {"jaut": "35 grāmatas, plauktā 10. Cik plauktu vajag?",
         "atb": ["4"], "padoms": "Trīs plaukti ir 30."},
        {"jaut": "60 bērni, autobusā 40 vietas. Cik autobusu vajag?",
         "atb": ["2"], "padoms": "Viens nepietiek, divi pietiek."},
        {"jaut": "81 ola, kastē 6. Cik kastu vajag?",
         "atb": ["14"], "padoms": "13 kastes ir 78."},
    ], pamats=4,
        ievads="Šajos uzdevumos atlikums nozīmē, ka vajag vēl vienu."),

    Zimejums("Kad noapaļo uz augšu",
             restis([["situācija", "atbilde"],
                     ["cik autobusu vajag", "uz augšu"],
                     ["cik pilnu kastu sanāk", "uz leju"],
                     ["cik naudas palika", "precīzi"]],
                    "jautājums nosaka atbildi"),
             paskaidro="Viens un tas pats dalījums dod dažādas atbildes - "
                       "izšķir uzdevuma jautājums.",
             ievads="Trīs jautājumi, trīs noapaļošanas veidi."),

    Varianti("Vai atbilde der?", [
        {"jaut": "Uzdevuma atbilde sanāca «3,5 bērni». Ko tas nozīmē?",
         "opcijas": ["Kaut kur ir kļūda", "Atbilde ir pareiza",
                     "Jāapaļo uz leju", "Jāapaļo uz augšu"],
         "pareizi": 0, "padoms": "Bērnus nedala."},
        {"jaut": "Klasē 24 bērni, atbilde sanāca 30. Ko tas nozīmē?",
         "opcijas": ["Atbilde nevar būt lielāka par visu klasi",
                     "Atbilde ir pareiza", "Jāpieskaita vēl 6",
                     "Jāatņem 24"],
         "pareizi": 0, "padoms": "Daļa nevar būt lielāka par veselo."},
        {"jaut": "«Cik pilnu kastu sanāks no 50 cepumiem pa 8?»",
         "opcijas": ["6", "7", "6,25", "8"],
         "pareizi": 0, "padoms": "Pilnu kastu - noapaļo uz leju."},
        {"jaut": "«Cik kastu vajag 50 cepumiem pa 8?»",
         "opcijas": ["7", "6", "6,25", "8"],
         "pareizi": 0, "padoms": "Visiem cepumiem jāietilpst."},
    ], pamats=4),

    Pasaule("Vai pirkums ir iespējams?",
            Ievadi("", [
                {"jaut": "Kabatā 50 ct, prece maksā 12 ct. Cik preču var "
                         "nopirkt?",
                 "atb": ["4"], "padoms": "4 · 12 = 48."},
                {"jaut": "Cik centu paliks pāri?",
                 "atb": ["2"], "padoms": "50 − 48."},
                {"jaut": "Vai atlikums var būt lielāks par preces cenu? "
                         "Raksti «jā» vai «nē».",
                 "atb": ["nē", "ne"],
                 "padoms": "Tad varēja nopirkt vēl vienu.",
                 "tastatura": "text"},
                {"jaut": "80 ct, prece 25 ct. Cik preču un cik paliks pāri? "
                         "Ieraksti atlikumu.",
                 "atb": ["5"], "padoms": "3 · 25 = 75; 80 − 75."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā atbilde vienmēr ir vesela prece un vesela "
                      "nauda - pusi zīmuļa nepārdod.",
            kapec="Pārbaude dzīvē atklāj kļūdas, kuras rēķins nepamana."),

    Kopsavilkums([
        "Pārbaudu, vai atbilde ir iespējama dotajā situācijā.",
        "Zinu, kad atbildi noapaļo uz augšu un kad uz leju.",
        "Pamanu atbildi, kas ir lielāka par veselo.",
        "Pasaku, ko atbilde nozīmē dzīvē.",
    ]),

    Majas([
        "Izrēķini, cik autobusu vajag 90 bērniem, ja vienā ietilpst 40.",
        "Atrodi uzdevumu, kurā atbildi noapaļo uz leju.",
        "Pastāsti mājiniekiem, kāpēc atbilde «2,5 autobusi» neder.",
    ]),
]
