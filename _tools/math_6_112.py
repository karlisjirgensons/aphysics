# -*- coding: utf-8 -*-
"""6. klase, 112. stunda: «Kā iekārto koordinātu plakni?»

Tagad plakni zīmē pats skolēns. Grūtākais nav asis, bet vienības izvēle:
pārāk lielas, un dati neietilpst; pārāk mazas, un grafiks kļūst par svītru.
Tāpēc te vingrina tieši šo izvēli.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         plakne)

TEMA = "Kā iekārto koordinātu plakni?"

MERKIS = ("Iekārtosim koordinātu plakni, nosauksim asis un izvēlēsimies "
          "vienības.")

SATURS = [
    Sakums("Divas asis un četri kvadranti",
           zimejums=plakne(no_x=-4, lidz_x=4, no_y=-4, lidz_y=4, solis=1),
           paraksts="Horizontālā ass ir x, vertikālā - y. To krustpunkts ir "
                    "koordinātu sākumpunkts.",
           fakti=["Asis krustojas nulles punktā un sadala plakni četrās "
                  "daļās.",
                  "Uz abām asīm vienību izvēlas vienādu, ja vien nav "
                  "iemesla citādi.",
                  "Bultiņa rāda, kurā virzienā skaitļi aug."]),

    Doma("Vispirms asis, tad vienības",
         "Koordinātu plakni iekārto četros soļos: uzzīmē abas asis, atzīmē "
         "sākumpunktu, izvēlas vienības un pieraksta asu nosaukumus.",
         soli=[
             "Uzzīmē horizontālo asi un pieraksti tai bultiņu pa labi.",
             "Uzzīmē vertikālo asi ar bultiņu uz augšu.",
             "Krustpunktā atzīmē nulli.",
             "Izvēlies vienību tā, lai visi dati ietilptu lapā.",
             "Pieraksti asu nosaukumus un mērvienības.",
         ],
         pieze="Vienību izvēlas pēc lielākās vērtības: ja dati ir līdz 40, "
               "viena rūtiņa var būt 5 vienības. Ja dati ir līdz 4, viena "
               "rūtiņa ir viena vienība."),

    Paraugs("Izvēlies vienību",
            uzd="Dati ir no −30 līdz 40. Kādu vienību izvēlēties, ja lapā ir "
                "20 rūtiņas augstumā?",
            soli=[
                ("Diapazons: no −30 līdz 40",
                 "Kopā 70 vienības."),
                ("Lapā ir 20 rūtiņas",
                 "70 : 20 ir mazliet vairāk par 3."),
                ("Izvēlas vienu rūtiņu = 5 vienības",
                 "Ērts skaitlis, un viss ietilpst."),
                ("40 : 5 = 8 rūtiņas uz augšu; 30 : 5 = 6 uz leju",
                 "Kopā 14 rūtiņas - ietilpst."),
            ],
            atbilde="viena rūtiņa = 5 vienības"),

    Ievadi("Izvēlies vienību", [
        {"jaut": "Dati no 0 līdz 40, lapā 8 rūtiņas. Cik vienību ir viena "
                 "rūtiņa?",
         "atb": ["5"], "padoms": "40 : 8."},
        {"jaut": "Dati no −10 līdz 10, lapā 20 rūtiņas. Cik vienību ir viena "
                 "rūtiņa?",
         "atb": ["1"], "padoms": "20 : 20."},
        {"jaut": "Viena rūtiņa ir 5 vienības. Cik rūtiņu ir līdz 35?",
         "atb": ["7"], "padoms": "35 : 5."},
        {"jaut": "Viena rūtiņa ir 2 vienības. Cik rūtiņu ir līdz −12?",
         "atb": ["6"], "padoms": "12 : 2."},
        {"jaut": "Cik kvadrantu ir koordinātu plaknē?",
         "atb": ["4"], "padoms": "Asis sadala plakni."},
        {"jaut": "Kādas koordinātas ir sākumpunktam? Ieraksti pirmo "
                 "koordinātu.",
         "atb": ["0"], "padoms": "Punkts (0; 0)."},
    ], pamats=4),

    Petijums("Iekārto plakni saviem datiem",
             vajag="rūtiņu lapa, lineāls",
             soli=[
                 "Savāc piecus datus, kuros ir arī negatīvas vērtības.",
                 "Atrodi lielāko un mazāko vērtību.",
                 "Izvēlies vienību tā, lai visi dati ietilptu lapā.",
                 "Uzzīmē asis, atzīmē iedaļas un pieraksti nosaukumus.",
                 "Atliec savus datus un pārbaudi, vai viss ietilpst.",
             ],
             secinajums="Vienību izvēlas pirms zīmēšanas, ne pēc - citādi "
                        "plakne jāpārzīmē."),

    Varianti("Kas ir kas plaknē?", [
        {"jaut": "Horizontālo asi apzīmē ar...",
         "opcijas": ["x", "y", "z", "0"],
         "pareizi": 0,
         "padoms": "Vertikālā ir y."},
        {"jaut": "Asu krustpunktu sauc par...",
         "opcijas": ["koordinātu sākumpunktu", "kvadrantu",
                     "vienību", "asi"],
         "pareizi": 0,
         "padoms": "Tur abas koordinātas ir nulle."},
        {"jaut": "Kāpēc vienību izvēlas pirms zīmēšanas?",
         "opcijas": ["Lai visi dati ietilptu lapā",
                     "Lai ass būtu taisna",
                     "Tā prasa likums", "Nav iemesla"],
         "pareizi": 0,
         "padoms": "Citādi plakne jāpārzīmē."},
        {"jaut": "Ja dati ir no −100 līdz 100, ērta vienība ir...",
         "opcijas": ["10 vai 20", "1", "0,5", "100"],
         "pareizi": 0,
         "padoms": "Lai rūtiņu skaits būtu saprātīgs."},
    ], pamats=4),

    Pasaule("Kā uzzīmēt nedēļas grafiku?",
            Ievadi("", [
                {"jaut": "Nedēļas temperatūras no −8 °C līdz 6 °C. Kāds ir "
                         "diapazons grādos?",
                 "atb": ["14"], "padoms": "8 + 6."},
                {"jaut": "Lapā ir 14 rūtiņas. Cik grādu ir viena rūtiņa?",
                 "atb": ["1"], "padoms": "14 : 14."},
                {"jaut": "Cik rūtiņu vajag zem ass?",
                 "atb": ["8"], "padoms": "Līdz −8."},
                {"jaut": "Cik dienu ir uz horizontālās ass?",
                 "atb": ["7"], "padoms": "Nedēļā."},
            ]),
            pavediens="planeta",
            konteksts="Nedēļas laika grafiku zīmē tieši tā: vispirms "
                      "diapazons, tad vienība, tad punkti.",
            kapec="Pareizi izvēlēta vienība padara grafiku lasāmu."),

    Zimejums("Plakne ar vienību 5",
             plakne(punkti=[(2, 3, "(2; 3)")], no_x=-3, lidz_x=3, no_y=-3,
                    lidz_y=3, solis=1),
             paskaidro="Katra rūtiņa ir viena vienība. Punkts (2; 3) ir divi "
                       "soļi pa labi un trīs uz augšu.",
             ievads="Tā izskatās gatava plakne ar vienu punktu."),

    Kopsavilkums([
        "Iekārtoju koordinātu plakni ar abām asīm un sākumpunktu.",
        "Nosaucu asis un pierakstu mērvienības.",
        "Izvēlos vienību pēc datu diapazona.",
        "Pārbaudu, vai visi dati ietilpst lapā.",
    ]),

    Majas([
        "Uzzīmē koordinātu plakni no −5 līdz 5 abās asīs.",
        "Atzīmē uz tās trīs punktus, no kuriem viens ir negatīvajā daļā.",
        "Pieraksti, kādu vienību izvēlētos datiem no −50 līdz 50.",
    ]),
]
