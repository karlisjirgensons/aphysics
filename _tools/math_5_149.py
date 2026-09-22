# -*- coding: utf-8 -*-
"""5. klase, 149. stunda: «Vai procentus var salīdzināt?»

Mikrotemata noslēgums, un tas ir 79. stundas jautājums procentu valodā: ja
veselie ir dažādi, tad vienādi procenti nozīmē dažādas summas. 20 % no 50 €
un 20 % no 500 € ir viens un tas pats procents, bet desmitkārt atšķirīga
nauda - tieši to skolēni pamana visgrūtāk.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, kolonnas)

TEMA = "Vai procentus var salīdzināt?"

MERKIS = ("Mācīsimies spriest par procentu salīdzināšanu, ja veselie ir "
          "dažādi lielumi.")

SATURS = [
    Sakums("Divas reizes divdesmit procenti",
           zimejums=kolonnas([("50 €", 10), ("500 €", 100)]),
           paraksts="20 % abām precēm, bet atlaide 10 € un 100 €.",
           fakti=["Abās reizēs atlaide ir 20 %.",
                  "Bet cenas atšķiras desmitkārt.",
                  "Tāpēc arī ietaupījums atšķiras desmitkārt."]),

    Doma("Procenti ir no kaut kā",
         "Vienādus procentus var salīdzināt tikai tad, ja veselie ir vienādi; "
         "ja veselie atšķiras, jāsalīdzina procentu skaitliskās vērtības.",
         soli=[
             "Nosaki, no kā ņemti procenti katrā gadījumā.",
             "Ja veselie ir vienādi, salīdzini procentus.",
             "Ja veselie atšķiras, aprēķini katra procenta vērtību.",
             "Salīdzini iegūtās vērtības.",
             "Formulē secinājumu vārdiem.",
         ],
         pieze="«Kuram bija lielāka atlaide?» un «kurš ietaupīja vairāk?» ir "
               "divi dažādi jautājumi. Uz pirmo atbild procenti, uz otro - "
               "eiro."),

    Paraugs("20 % no 50 € un 20 % no 500 €",
            uzd="Vai abas atlaides ir vienādas?",
            soli=[
                ("Procenti abās reizēs ir 20 %",
                 "Kā daļa - vienādi."),
                ("50 : 5 = 10 (€)",
                 "Pirmā atlaide."),
                ("500 : 5 = 100 (€)",
                 "Otrā atlaide."),
                ("10 € un 100 €",
                 "Naudā atšķirība ir desmitkārtīga."),
                ("Procenti vienādi, vērtības - nē",
                 "Jo veselie ir dažādi."),
            ],
            atbilde="Procenti vienādi, bet ietaupījums atšķiras"),

    Ievadi("Salīdzini procentus un vērtības", [
        {"jaut": "Cik eiro ir 20 % no 50 €?",
         "atb": ["10"], "padoms": "50 : 5."},
        {"jaut": "Cik eiro ir 20 % no 500 €?",
         "atb": ["100"], "padoms": "500 : 5."},
        {"jaut": "Cik eiro ir 10 % no 200 €?",
         "atb": ["20"], "padoms": "200 : 10."},
        {"jaut": "Cik eiro ir 50 % no 30 €?",
         "atb": ["15"], "padoms": "Puse."},
        {"jaut": "Kurš ietaupa vairāk - 10 % no 200 € vai 50 % no 30 €? "
                 "Ieraksti summu eiro.",
         "atb": ["20"], "padoms": "20 € pret 15 €."},
        {"jaut": "Cik eiro ir 25 % no 40 €?",
         "atb": ["10"], "padoms": "40 : 4."},
        {"jaut": "Cik eiro ir 5 % no 400 €?",
         "atb": ["20"], "padoms": "400 : 100 · 5."},
        {"jaut": "Kurš ietaupa vairāk - 25 % no 40 € vai 5 % no 400 €? "
                 "Ieraksti summu eiro.",
         "atb": ["20"], "padoms": "20 € pret 10 €."},
    ], pamats=4,
        ievads="Procentu skaits vien neko nepasaka - jāzina arī veselais."),

    Zimejums("Vienādi procenti, dažādas summas",
             kolonnas([("10 €", 10), ("100 €", 100)]),
             paskaidro="Abas atlaides ir 20 %, bet stabiņi atšķiras "
                       "desmitkārt, jo cenas bija 50 € un 500 €.",
             ievads="Naudā vienādi procenti izskatās pavisam dažādi."),

    Varianti("Ko procenti pasaka un ko ne?", [
        {"jaut": "Kad vienādus procentus var salīdzināt tieši?",
         "opcijas": ["Kad veselie ir vienādi", "Vienmēr", "Nekad",
                     "Kad procenti ir apaļi"],
         "pareizi": 0,
         "padoms": "Procenti ir no kaut kā."},
        {"jaut": "20 % no 50 € un 20 % no 500 € - vai atlaides ir vienādas?",
         "opcijas": ["Procenti vienādi, summas nē", "Jā, pilnīgi vienādas",
                     "Nē, procenti atšķiras", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "10 € pret 100 €."},
        {"jaut": "Uz kuru jautājumu atbild procenti?",
         "opcijas": ["Cik liela daļa no cenas", "Cik eiro ietaupīts",
                     "Cik maksā prece", "Cik preču nopirkts"],
         "pareizi": 0,
         "padoms": "Daļa, ne summa."},
        {"jaut": "10 % no 200 € vai 50 % no 30 € - kurš ietaupa vairāk?",
         "opcijas": ["10 % no 200 €", "50 % no 30 €", "Vienādi",
                     "To nevar zināt"],
         "pareizi": 0,
         "padoms": "20 € pret 15 €."},
        {"jaut": "Vai lielāks procents vienmēr nozīmē lielāku summu?",
         "opcijas": ["Nē, ja veselie atšķiras", "Jā, vienmēr",
                     "Tikai ar naudu", "To nevar zināt"],
         "pareizi": 0,
         "padoms": "50 % no 30 ir mazāk par 10 % no 200."},
        {"jaut": "Ko vajag zināt, lai salīdzinātu ietaupījumu?",
         "opcijas": ["Gan procentus, gan veselo", "Tikai procentus",
                     "Tikai veselo", "Neko"],
         "pareizi": 0,
         "padoms": "Procentu vērtība nāk no abiem."},
    ], pamats=4),

    Pasaule("Kur atlaide ir izdevīgāka?",
            Ievadi("", [
                {"jaut": "Jaka maksā 60 €, atlaide 25 %. Cik eiro ietaupa?",
                 "atb": ["15"], "padoms": "60 : 4."},
                {"jaut": "Cepure maksā 20 €, atlaide 50 %. Cik eiro ietaupa?",
                 "atb": ["10"], "padoms": "Puse."},
                {"jaut": "Kur ietaupījums ir lielāks? Ieraksti summu eiro.",
                 "atb": ["15"], "padoms": "15 € pret 10 €."},
                {"jaut": "Kura atlaide ir lielāka procentos? Ieraksti "
                         "skaitli.",
                 "atb": ["50"], "padoms": "50 % pret 25 %."},
            ]),
            pavediens="veikals",
            konteksts="Lielāka atlaide procentos ne vienmēr nozīmē lielāku "
                      "ietaupījumu eiro.",
            kapec="Tieši uz to reklāma arī paļaujas."),

    Kopsavilkums([
        "Zinu, ka procenti vienmēr ir no kāda veselā.",
        "Salīdzinu procentus tieši tikai tad, ja veselie ir vienādi.",
        "Aprēķinu procentu vērtības, ja veselie atšķiras.",
        "Atšķiru jautājumu par procentiem no jautājuma par summu.",
    ]),

    Majas([
        "Salīdzini 30 % no 40 € un 15 % no 100 €.",
        "Atrodi divas reklāmas ar dažādām atlaidēm un salīdzini ietaupījumu.",
        "Uzraksti, kāpēc lielāks procents ne vienmēr ir izdevīgāks.",
    ]),
]
