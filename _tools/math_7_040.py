# -*- coding: utf-8 -*-
"""7. klase, 40. stunda: «Kas situācijā mainās un kas ne?»

Katrā situācijā ir lielumi, kas mainās (mainīgie), un tādi, kas paliek
nemainīgi (konstantes). Taksometra braucienā mainās attālums un cena,
bet nemainās tarifs par kilometru. Stunda iemāca tos atšķirt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas situācijā mainās un kas ne?"

MERKIS = ("Noteiksim, kuri lielumi situācijā mainās un kuri ir nemainīgi, "
          "un raksturosim tos.")

SATURS = [
    Sakums("Taksometra skaitītājs",
           zimejums=restis([["km", "0", "2", "4", "6"],
                            ["€", "2", "3,6", "5,2", "6,8"]]),
           paraksts="Iekāpšana 2 €, katrs km 0,80 €.",
           fakti=["Brauciena laikā mainās kilometri un summa.",
                  "Iekāpšanas maksa un cena par km nemainās.",
                  "Nemainīgie ir «noteikumi», mainīgie - «stāvoklis»."]),

    Doma("Mainīgie un nemainīgie lielumi",
         "Lielumu, kas situācijā var pieņemt dažādas vērtības, sauc par "
         "mainīgu lielumu. Lielumu, kas paliek viens un tas pats, sauc par "
         "nemainīgu lielumu jeb konstanti.",
         soli=[
             "Uzskaiti visus lielumus situācijā.",
             "Katram jautā: vai tas mainās, kad situācija turpinās?",
             "Mainīgos apzīmē ar burtiem: t, s, x.",
             "Nemainīgos raksta ar skaitļiem vai burtiem, kas nemainās.",
         ],
         pieze="Viens un tas pats lielums vienā situācijā var būt "
               "mainīgs, citā - nemainīgs: ātrums braucienā pa pilsētu "
               "mainās, uz automaģistrāles ar kruīza kontroli - nē."),

    Paraugs("Vannas piepildīšana",
            uzd="Vannā ietek 12 litri minūtē. Vannas tilpums 180 l. Kuri "
                "lielumi mainās, kuri - nē?",
            soli=[
                ("Mainās: laiks t (min) un ūdens daudzums V (l)",
                 "Tie aug līdz ar procesu."),
                ("Nemainās: ātrums 12 l/min un tilpums 180 l",
                 "Tie ir noteikumi."),
                ("Pēc 5 min: V = 12 · 5 = 60 (l)",
                 "Mainīgo vērtības saista nemainīgais."),
            ],
            atbilde="Mainīgie: t un V; nemainīgie: 12 l/min, 180 l"),

    Varianti("Mainīgs vai nemainīgs?", [
        {"jaut": "Lidmašīnas lidojumā: attālums līdz galamērķim",
         "opcijas": ["Mainīgs", "Nemainīgs"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Tas samazinās."},
        {"jaut": "Mobilā tarifā: mēneša maksa 9,99 €",
         "opcijas": ["Mainīgs", "Nemainīgs"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Tā ir fiksēta."},
        {"jaut": "Augot: bērna augums",
         "opcijas": ["Mainīgs", "Nemainīgs"],
         "pareizi": 0, "jaukt": False,
         "padoms": "Tas pieaug."},
        {"jaut": "Riņķa līnijai: garuma attiecība pret diametru (π)",
         "opcijas": ["Mainīgs", "Nemainīgs"],
         "pareizi": 1, "jaukt": False,
         "padoms": "Visām riņķa līnijām π ≈ 3,14."},
    ], pamats=4),

    Ievadi("Aprēķini ar nemainīgo", [
        {"jaut": "Taksometrs: 2 € + 0,80 € par km. Cik € maksā 10 km?",
         "atb": ["10"], "padoms": "2 + 0,8 · 10."},
        {"jaut": "Vannā ietek 12 l minūtē. Cik litru pēc 8 min?",
         "atb": ["96"], "padoms": "12 · 8."},
        {"jaut": "Vanna ir 180 l. Pēc cik minūtēm tā būs pilna?",
         "atb": ["15"], "padoms": "180 : 12."},
        {"jaut": "Taksometrā samaksāja 6 €. Cik km brauca?",
         "atb": ["5"], "padoms": "(6 − 2) : 0,8."},
    ]),

    Pasaule("Telefona akumulators",
            Ievadi("", [
                {"jaut": "Lādējot telefons iegūst 2 % minūtē. Sākumā 14 %. "
                         "Cik % būs pēc 20 min?",
                 "atb": ["54"], "padoms": "14 + 2 · 20."},
                {"jaut": "Kurš lielums te ir nemainīgs - «ātrums» vai "
                         "«uzlādes līmenis»?",
                 "atb": ["ātrums", "atrums"], "padoms": "2 % minūtē.",
                 "tastatura": "text"},
                {"jaut": "Pēc cik minūtēm būs 100 %?",
                 "atb": ["43"], "padoms": "(100 − 14) : 2."},
            ]),
            pavediens="dati",
            konteksts="Uzlādes ekrāns rāda mainīgo - procentus; lādētāja "
                      "jauda ir nemainīga.",
            kapec="Nemainīgais ļauj prognozēt mainīgo."),

    Zimejums("Uzlāde soli pa solim",
             restis([["min", "0", "10", "20", "30"],
                     ["%", "14", "34", "54", "74"]]),
             paskaidro="Katras 10 minūtes pievieno tos pašus 20 %."),

    Kopsavilkums([
        "Atšķiru mainīgus un nemainīgus lielumus.",
        "Apzīmēju mainīgos ar burtiem.",
        "Izmantoju nemainīgo, lai aprēķinātu mainīgo.",
        "Zinu, ka tas pats lielums dažādās situācijās var būt citāds.",
    ]),

    Majas([
        "Apraksti vienu procesu mājās un uzskaiti mainīgos un nemainīgos.",
        "Izveido tabulu savam telefona uzlādes procesam.",
        "Izdomā situāciju, kurā ātrums ir mainīgs lielums.",
    ]),
]
