# -*- coding: utf-8 -*-
"""7. klase, 50. stunda: «Vai starp lielumiem vispār ir sakarība?»

Ne visi lielumi ir saistīti ar formulu. Dažreiz dati izkaisīti bez
likumsakarības, dažreiz ir tendence, bet ne precīza formula. Stunda iemāca
no izkliedes grafika izvērtēt, vai sakarība ir un vai to var aprakstīt
matemātiski.
"""

from math_saturs import (Doma, Kopsavilkums, Majas, Paraugs, Pasaule,
                         Petijums, Sakums, Varianti, Zimejums, plakne)

TEMA = "Vai starp lielumiem vispār ir sakarība?"

MERKIS = ("Izvērtēsim, vai lielumus raksturojošos datus saista sakarība, "
          "ko var aprakstīt matemātiski.")

SATURS = [
    Sakums("Vai garāki cilvēki ātrāk skrien?",
           zimejums=plakne(punkti=[(150, 9.8), (155, 9.1), (160, 9.5),
                                   (165, 8.6), (170, 9.2), (175, 8.4),
                                   (180, 8.9), (185, 8.1)],
                           no_x=145, lidz_x=190, no_y=7, lidz_y=11,
                           solis=5, solis_y=0.5, x_nos="cm", y_nos="s"),
           paraksts="60 m laiks pret augumu: tendence ir, formulas - nav.",
           fakti=["Punkti kopumā iet uz leju - garākie mazliet ātrāki.",
                  "Bet tie nav uz vienas līnijas.",
                  "Sakarība ir aptuvena, nevis precīza."]),

    Doma("Precīza sakarība, tendence vai nekā",
         "Datus attēlo izkliedes grafikā. Ja punkti ir tieši uz līnijas - "
         "ir precīza sakarība ar formulu. Ja tie izkaisīti ap līniju - ir "
         "tendence. Ja izkaisīti pa visu plakni - sakarības nav.",
         soli=[
             "Atzīmē katru datu pāri kā punktu.",
             "Paskaties: vai punkti veido līniju vai joslu?",
             "Līnija - formula; josla - tendence; mākonis - nav sakarības.",
             "Padomā: vai sakarību var izskaidrot ar cēloni?",
         ],
         pieze="Pat ja sakarība ir, tā var būt nejauša: saldējuma pārdošana "
               "un saules apdegumi aug kopā, bet viens neizraisa otru - "
               "abus izraisa saule."),

    Zimejums("Nekādas sakarības",
             plakne(punkti=[(1, 7), (2, 3), (3, 8), (4, 2), (5, 6), (6, 9),
                            (7, 4), (8, 5), (9, 2)],
                    no_x=0, lidz_x=10, no_y=0, lidz_y=10, solis=1),
             paskaidro="Dzimšanas diena mēnesī pret atzīmi matemātikā - "
                       "punkti izkaisīti pa visu plakni."),

    Paraugs("Izvērtē datus",
            uzd="Temperatūra (°C): 15, 20, 25, 30; pārdotas saldējuma "
                "porcijas: 40, 62, 79, 101. Vai ir sakarība?",
            soli=[
                ("Pieaugums: +22, +17, +22", "Katri 5 °C - aptuveni +20."),
                ("Punkti gandrīz uz taisnes", "Tendence ir skaidra."),
                ("Nav precīzi vienāds pieaugums", "Precīzas formulas nav."),
                ("Tendence: siltāks - vairāk saldējuma", "Secinājums."),
            ],
            atbilde="Ir tendence (aptuvena sakarība), bet ne precīza formula."),

    Varianti("Kāda sakarība?", [
        {"jaut": "Kvadrāta mala un perimetrs",
         "opcijas": ["Precīza (formula)", "Tendence", "Nav sakarības"],
         "pareizi": 0, "jaukt": False,
         "padoms": "P = 4a."},
        {"jaut": "Mācīšanās laiks un testa rezultāts",
         "opcijas": ["Precīza (formula)", "Tendence", "Nav sakarības"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Parasti vairāk - labāk, bet ne vienmēr."},
        {"jaut": "Mājas numurs un iedzīvotāja augums",
         "opcijas": ["Precīza (formula)", "Tendence", "Nav sakarības"],
         "pareizi": 2, "jaukt": False,
         "padoms": "Nav cēloņa."},
        {"jaut": "Laiks un ceļš vienmērīgā kustībā",
         "opcijas": ["Precīza (formula)", "Tendence", "Nav sakarības"],
         "pareizi": 0, "jaukt": False,
         "padoms": "s = vt."},
    ], pamats=4),

    Petijums("Klases dati",
             ["Katrs klasē izmēra savu augumu un plaukstas platumu (cm).",
              "Visus datus ieraksta tabulā.",
              "Atzīmē punktus: x - augums, y - plaukstas platums.",
              "Izvērtē: formula, tendence vai nav sakarības?"],
             vajag="mērlente, tabula",
             secinajums="Parasti redz tendenci: garākiem cilvēkiem plaukstas "
                         "platākas, bet ne precīzi pēc formulas."),

    Pasaule("Viedpulksteņa dati",
            Varianti("", [
                {"jaut": "Pulkstenis mēra soļus un sadedzinātās kalorijas. "
                         "Punkti ir gandrīz uz taisnes. Ko secina?",
                 "opcijas": ["Ir cieša sakarība - vairāk soļu, vairāk kaloriju",
                             "Sakarības nav",
                             "Kalorijas izraisa soļus",
                             "Dati ir nepareizi"],
                 "pareizi": 0,
                 "padoms": "Punkti gar līniju."},
                {"jaut": "Miega stundas un nākamās dienas soļu skaits - "
                         "punkti izkaisīti pa visu plakni. Ko secina?",
                 "opcijas": ["Šajos datos sakarība nav redzama",
                             "Vairāk miega - vairāk soļu",
                             "Mazāk miega - vairāk soļu",
                             "Formula ir s = 1000t"],
                 "pareizi": 0,
                 "padoms": "Mākonis."},
                {"jaut": "Kāpēc pulksteņa kaloriju sakarība nav ideāla "
                         "taisne?",
                 "opcijas": ["Soļi var būt ātrāki vai lēnāki, kalnup vai "
                             "lejup",
                             "Pulkstenis ir salūzis",
                             "Kalorijas nav skaitlis",
                             "Tā ir ideāla taisne"],
                 "pareizi": 0,
                 "padoms": "Ir arī citi faktori."},
            ]),
            pavediens="sports",
            konteksts="Sporta lietotnes zīmē izkliedes grafikus un meklē "
                      "sakarības tavos datos.",
            kapec="Ne katrs grafiks nozīmē formulu."),

    Kopsavilkums([
        "Attēloju datus izkliedes grafikā.",
        "Atšķiru precīzu sakarību, tendenci un sakarības trūkumu.",
        "Pamatoju secinājumu ar punktu izvietojumu.",
        "Zinu, ka kopā augoši lielumi var nebūt cēlonis un sekas.",
    ]),

    Majas([
        "Nedēļu pieraksti miega stundas un garastāvokli (1-10).",
        "Attēlo datus grafikā un izvērtē.",
        "Atrodi piemēru, kur divi lielumi aug kopā, bet viens neizraisa "
        "otru.",
    ]),
]
