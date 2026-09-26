# -*- coding: utf-8 -*-
"""3. klase, 152. stunda: «Cik tālu ir kilometrs?»

Novērtēšana bez mērinstrumenta. Skolēns iegūst savus atskaites lielumus -
savs solis, savas rokas izplētiens, litra pudele - un ar tiem novērtē citus
lielumus. Pēc tam novērtējumu pārbauda ar mērījumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Cik tālu ir kilometrs?"

MERKIS = ("Novērtēsim attālumu, masu un tilpumu aptuveni un pārbaudīsim "
          "novērtējumu.")

SATURS = [
    Sakums("Cik soļu ir viens kilometrs?",
           zimejums=restis([["lielums", "atskaites punkts"],
                            ["1 m", "liels solis"],
                            ["1 km", "apmēram 1300 soļu"],
                            ["1 kg", "litrs ūdens"]],
                           "savi atskaites lielumi"),
           paraksts="Ar saviem soļiem var izmērīt jebkuru attālumu.",
           fakti=["Viens liels solis ir apmēram 1 metrs.",
                  "Litrs ūdens sver apmēram 1 kilogramu."]),

    Doma("Novērtē ar savu atskaites lielumu",
         "Izvēlies kaut ko, kā lielumu zini droši, un salīdzini ar to.",
         soli=[
             "Izvēlies atskaites lielumu: solis, plauksta vai pudele.",
             "Novērtē, cik reižu tas ietilpst mērāmajā.",
             "Reizini atskaites lielumu ar šo skaitu.",
             "Pārbaudi novērtējumu ar īstu mērījumu.",
         ],
         pieze="Novērtējums nekad nav precīzs - bet, ja tas atšķiras no "
               "mērījuma desmit reižu, kaut kas ir pārprasts."),

    Petijums("Izmēri savu soli",
             vajag="mērlente un brīva vieta",
             soli=[
                 "Nomēri 10 m garu ceļu.",
                 "Noej to ar parastiem soļiem un saskaiti tos.",
                 "Izdali 10 m ar soļu skaitu - tas ir viena soļa garums.",
                 "Izrēķini, cik tavu soļu ir vienā kilometrā.",
             ],
             secinajums="Zinot sava soļa garumu, jebkuru attālumu var "
                        "novērtēt, to vienkārši noejot."),

    Paraugs("Cik soļu ir kilometrā?",
            uzd="Viens solis ir 50 cm. Cik soļu ir 1 kilometrā?",
            soli=[
                ("1 km = 1000 m",
                 "Vispirms vienā mērvienībā."),
                ("1000 m = 100 000 cm",
                 "Pārvērš centimetros."),
                ("100 000 : 50 = 2000",
                 "Tik soļu pa 50 cm ietilpst kilometrā."),
            ],
            atbilde="2000 soļu"),

    Ievadi("Novērtē lielumus", [
        {"jaut": "Cik metru ir 1 km?", "atb": ["1000"],
         "padoms": "Tūkstotis."},
        {"jaut": "Solis ir 50 cm. Cik metru ir 100 soļu?", "atb": ["50"],
         "padoms": "100 · 50 cm = 5000 cm."},
        {"jaut": "Cik soļu pa 50 cm ir 1 kilometrā?", "atb": ["2000"],
         "padoms": "1000 m : 0,5 m."},
        {"jaut": "Litrs ūdens sver 1 kg. Cik kilogramu sver 5 litri?",
         "atb": ["5"], "padoms": "5 · 1."},
        {"jaut": "Cik gramu sver 1 litrs ūdens?", "atb": ["1000"],
         "padoms": "1 kg."},
        {"jaut": "Cik litru ūdens sver 3 kg?", "atb": ["3"],
         "padoms": "Katrs litrs ir kilograms."},
    ], pamats=4),

    Zimejums("Atskaites lielumi",
             restis([["lielums", "apmēram"],
                     ["durvju augstums", "2 m"],
                     ["klases garums", "8 m"],
                     ["ceļš uz veikalu", "500 m"]],
                    "ar ko salīdzināt"),
             paskaidro="Ja zini dažus lielumus no galvas, pārējos var "
                       "novērtēt, tos salīdzinot.",
             ievads="Trīs noderīgi atskaites punkti."),

    Varianti("Vai novērtējums ir saprātīgs?", [
        {"jaut": "Cik apmēram ir durvju augstums?",
         "opcijas": ["2 m", "20 cm", "20 m", "2 km"],
         "pareizi": 0, "padoms": "Nedaudz vairāk par cilvēka augumu."},
        {"jaut": "Cik apmēram sver ābols?",
         "opcijas": ["150 g", "15 g", "1,5 kg", "15 kg"],
         "pareizi": 0, "padoms": "Mazliet mazāk par pusi litra ūdens."},
        {"jaut": "Cik apmēram ir klases garums?",
         "opcijas": ["8 m", "80 m", "80 cm", "8 km"],
         "pareizi": 0, "padoms": "Apmēram astoņi soļi."},
        {"jaut": "Cik apmēram ietilpst glāzē?",
         "opcijas": ["250 ml", "25 ml", "2,5 l", "25 l"],
         "pareizi": 0, "padoms": "Ceturtdaļa litra."},
    ], pamats=4),

    Pasaule("Cik tālu ir skolas stadions?",
            Ievadi("", [
                {"jaut": "Stadiona aplis ir 400 m. Cik apļu ir 1 kilometrā "
                         "un cik metru paliek pāri? Ieraksti apļu skaitu.",
                 "atb": ["2"], "padoms": "2 · 400 = 800."},
                {"jaut": "Cik metru paliek pāri?", "atb": ["200"],
                 "padoms": "1000 − 800."},
                {"jaut": "Cik metru ir 5 apļi?", "atb": ["2000"],
                 "padoms": "5 · 400."},
                {"jaut": "Cik kilometru tas ir?", "atb": ["2"],
                 "padoms": "2000 : 1000."},
            ]),
            pavediens="skola",
            konteksts="Stadiona aplis ir 400 m - tāpēc divarpus apļi ir tieši "
                      "kilometrs.",
            kapec="Zinot vienu atskaites lielumu, pārējo var izrēķināt."),

    Kopsavilkums([
        "Novērtēju attālumu, masu un tilpumu aptuveni.",
        "Izmantoju savus atskaites lielumus.",
        "Pārbaudu novērtējumu ar mērījumu.",
        "Pamanu novērtējumu, kas atšķiras desmit reižu.",
    ]),

    Majas([
        "Izmēri sava soļa garumu.",
        "Novērtē ar soļiem attālumu līdz tuvākajam veikalam.",
        "Pārbaudi novērtējumu kartē vai lietotnē.",
    ]),
]
