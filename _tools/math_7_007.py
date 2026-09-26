# -*- coding: utf-8 -*-
"""7. klase, 7. stunda: «Kā informāciju parādīt pārskatāmi?»

Vieni un tie paši dati var būt tabulā, grafā vai Venna diagrammā. Katram
veidam ir sava stiprā puse: tabula - precīzi skaitļi, grafs - kas ar ko
saistīts, Venna diagramma - kas pieder kurai grupai. Stunda māca izvēlēties.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija,
                         restis, venna)

TEMA = "Kā informāciju parādīt pārskatāmi?"

MERKIS = ("Iemācīsimies attēlot informāciju tabulā, grafā un Venna "
          "diagrammā un izvēlēties piemērotāko veidu.")

_DRAUGI = geometrija(
    [("A", 0, 2), ("B", 3, 4), ("C", 6, 2), ("D", 3, 0), ("E", 9, 4)],
    nogriezni=["AB", "AD", "BC", "BD", "CE"])

SATURS = [
    Sakums("Kas ir kopīgs metro kartei un sociālajam tīklam?",
           zimejums=_DRAUGI,
           paraksts="Grafs: punkti ir cilvēki, līnijas - draudzība.",
           fakti=["Metro karte ir grafs: stacijas un ceļi starp tām.",
                  "Sociālais tīkls ir grafs: cilvēki un draudzības.",
                  "Grafā svarīgs ir tikai tas, kas ar ko savienots."]),

    Doma("Katram jautājumam - savs attēls",
         "Informāciju attēlo tā, lai atbilde uz jautājumu būtu redzama "
         "uzreiz: tabula - skaitļiem, grafs - saitēm, Venna diagramma - "
         "piederībai grupām.",
         soli=[
             "Jautā: ko gribam uzzināt?",
             "«Cik?» - tabula.",
             "«Kas ar ko saistīts?» - grafs (punkti un līnijas).",
             "«Kurš kurai grupai pieder?» - Venna diagramma.",
         ],
         pieze="Grafā punktus sauc par virsotnēm, līnijas - par šķautnēm. "
               "Virsotnes pakāpe ir no tās izejošo šķautņu skaits."),

    Paraugs("Nolasi grafu",
            uzd="Grafā A, B, C, D, E ir skolēni, līnija - «ir draugi "
                "sociālajā tīklā» (skat. sākuma attēlu). Kuram ir visvairāk "
                "draugu? Cik šķautņu ir grafā?",
            soli=[
                ("A: B, D - 2; B: A, C, D - 3", "Skaita līnijas."),
                ("C: B, E - 2; D: A, B - 2; E: C - 1", "Katram."),
                ("Visvairāk - B (3 draugi)", "Lielākā pakāpe."),
                ("(2 + 3 + 2 + 2 + 1) : 2 = 5 šķautnes",
                 "Katra līnija saskaitīta divos galos."),
            ],
            atbilde="B; grafā ir 5 šķautnes."),

    Zimejums("Tie paši dati tabulā",
             restis([["", "A", "B", "C", "D", "E"],
                     ["draugi", "2", "3", "2", "2", "1"]]),
             paskaidro="Tabulā redz skaitu, bet neredz, kurš ar kuru ir "
                       "draugs. Grafā redz abus."),

    Varianti("Kuru attēlu izvēlēties?", [
        {"jaut": "Jāparāda, kuri skolēni ir gan korī, gan deju kolektīvā.",
         "opcijas": ["Venna diagramma", "Grafs", "Tabula ar temperatūru",
                     "Laika ass"],
         "pareizi": 0,
         "padoms": "Piederība divām grupām."},
        {"jaut": "Jāparāda autobusu maršruti starp pilsētām.",
         "opcijas": ["Grafs", "Venna diagramma", "Sektoru diagramma",
                     "Skaitļu taisne"],
         "pareizi": 0,
         "padoms": "Kas ar ko savienots."},
        {"jaut": "Jāparāda katras dienas nokrišņu daudzums mēnesī.",
         "opcijas": ["Tabula vai stabiņu diagramma", "Grafs",
                     "Venna diagramma", "Iespēju koks"],
         "pareizi": 0,
         "padoms": "Precīzi skaitļi."},
        {"jaut": "Grafā ir 4 virsotnes, katras pakāpe ir 3. Cik šķautņu?",
         "opcijas": ["6", "12", "4", "3"],
         "pareizi": 0,
         "padoms": "4 · 3 : 2."},
    ], pamats=4),

    Ievadi("Nolasi un aprēķini", [
        {"jaut": "Grafā ir 6 virsotnes, katras pakāpe ir 2. Cik šķautņu?",
         "atb": ["6"], "padoms": "6 · 2 : 2."},
        {"jaut": "Venna diagrammā: tikai korī 7, tikai dejās 5, abos 3. "
                 "Cik ir korī kopā?",
         "atb": ["10"], "padoms": "7 + 3."},
        {"jaut": "Tajā pašā diagrammā: cik skolēnu ir kaut vienā?",
         "atb": ["15"], "padoms": "7 + 5 + 3."},
        {"jaut": "Grafā pakāpes ir 1; 2; 2; 3. Cik šķautņu?",
         "atb": ["4"], "padoms": "(1 + 2 + 2 + 3) : 2."},
    ]),

    Pasaule("Lidojumu karte",
            Ievadi("", [
                {"jaut": "Rīga savienota ar Oslo, Berlīni, Londonu un "
                         "Viļņu; Viļņa - ar Berlīni; Oslo - ar Londonu. "
                         "Cik ir tiešo maršrutu?",
                 "atb": ["6"], "padoms": "4 + 1 + 1."},
                {"jaut": "Cik ir Berlīnes virsotnes pakāpe?",
                 "atb": ["2"], "padoms": "Rīga un Viļņa."},
                {"jaut": "No Viļņas uz Oslo jālido ar pārsēšanos. Kāds ir "
                         "mazākais lidojumu skaits?",
                 "atb": ["2"], "padoms": "Viļņa - Rīga - Oslo."},
            ]),
            pavediens="celojums",
            konteksts="Lidostu kartes zīmē kā grafu: pilsēta ir virsotne, "
                      "tiešais reiss - šķautne.",
            kapec="Grafā uzreiz redz, kur vajag pārsēsties."),

    Zimejums("Kori un dejas",
             venna(["7"], ["5"], ["3"], ("koris", "dejas")),
             paskaidro="Venna diagrammā grupu pārklājums redzams uzreiz."),

    Kopsavilkums([
        "Attēloju informāciju tabulā, grafā un Venna diagrammā.",
        "Izvēlos attēlu pēc tā, ko gribu uzzināt.",
        "Nolasu grafā virsotņu pakāpes.",
        "Zinu: šķautņu skaits ir pakāpju summa, dalīta ar 2.",
    ]),

    Majas([
        "Uzzīmē grafu: tava ģimene, līnija - «dzīvo vienā mājā».",
        "Uzzīmē grafu tuvākajām pilsētām un ceļiem starp tām.",
        "Kāpēc pakāpju summa vienmēr ir pāra skaitlis?",
    ]),
]
