# -*- coding: utf-8 -*-
"""3. klase, 102. stunda: «Kāda daļa no stundas ir 15 minūtes?»

Apgrieztais uzdevums 101. stundai: daļa nav dota, tā jāatrod. Pulkstenis te
ir ērtākais modelis, jo veselais - 60 minūtes - dalās ļoti daudzos veidos, un
atbilde vienmēr iznāk glīta.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, rinkis)

TEMA = "Kāda daļa no stundas ir 15 minūtes?"

MERKIS = ("Ar pulksteņa modeli noteiksim, kāda daļa no stundas ir dotais "
          "minūšu skaits.")

SATURS = [
    Sakums("Kāda daļa no stundas ir viena mācību stunda?",
           zimejums=rinkis(sektors=240, virsraksts="40 minūtes",
                           paraksts="2/3 stundas"),
           fakti=["Mācību stunda ir 40 minūtes no 60.",
                  "40 minūtes ir tieši {2|3} stundas."]),

    Doma("Dali veselo ar daļas lielumu",
         "Lai uzzinātu, kāda daļa ir 15 minūtes no 60, dali: 60 : 15 = 4, "
         "tātad tā ir {1|4}.",
         soli=[
             "Izdali veselo ar doto daļu: 60 : 15 = 4.",
             "Iegūtais skaitlis ir saucējs.",
             "Ja daļu ir vairākas, saskaiti, cik reižu tā ietilpst.",
             "Pieraksti daļu un pārbaudi ar reizināšanu.",
         ],
         pieze="Ja dalījums nav vesels, daļu meklē citādi: 40 minūtes ir "
               "divas reizes pa 20, un 20 ir {1|3} stundas, tātad 40 ir "
               "{2|3}."),

    Paraugs("Kāda daļa no stundas ir 40 minūtes?",
            uzd="Nosaki, kāda daļa no stundas ir 40 minūtes.",
            soli=[
                ("60 : 40 nav vesels skaitlis",
                 "Tāpēc meklē mazāku daļu, kas ietilpst abos."),
                ("60 : 3 = 20",
                 "Viena trešdaļa stundas ir 20 minūtes."),
                ("40 : 20 = 2",
                 "40 minūtes ir divas trešdaļas."),
            ],
            atbilde="{2|3} stundas"),

    Ievadi("Kāda daļa no stundas?", [
        {"jaut": "15 minūtes no 60 - kāds ir daļas saucējs?", "atb": ["4"],
         "padoms": "60 : 15."},
        {"jaut": "30 minūtes no 60 - kāds ir daļas saucējs?", "atb": ["2"],
         "padoms": "60 : 30."},
        {"jaut": "20 minūtes no 60 - kāds ir daļas saucējs?", "atb": ["3"],
         "padoms": "60 : 20."},
        {"jaut": "10 minūtes no 60 - kāds ir daļas saucējs?", "atb": ["6"],
         "padoms": "60 : 10."},
        {"jaut": "45 minūtes ir {3|4} stundas. Cik minūšu ir viena "
                 "ceturtdaļa?",
         "atb": ["15"], "padoms": "45 : 3."},
        {"jaut": "40 minūtes ir {2|3} stundas. Cik minūšu ir viena trešdaļa?",
         "atb": ["20"], "padoms": "40 : 2."},
    ], pamats=4),

    Zimejums("Puse stundas",
             rinkis(sektors=180, virsraksts="30 minūtes",
                    paraksts="1/2 stundas"),
             paskaidro="Trīsdesmit minūtes aizņem tieši pusi ciparnīcas.",
             ievads="Tā izskatās {1|2} stundas."),

    Varianti("Kāda daļa tā ir?", [
        {"jaut": "Kāda daļa no stundas ir 15 minūtes?",
         "opcijas": ["{1|4}", "{1|2}", "{1|3}", "{1|15}"],
         "pareizi": 0, "padoms": "60 : 15 = 4."},
        {"jaut": "Kāda daļa no stundas ir 12 minūtes?",
         "opcijas": ["{1|5}", "{1|4}", "{1|6}", "{1|12}"],
         "pareizi": 0, "padoms": "60 : 12 = 5."},
        {"jaut": "Kāda daļa no stundas ir 45 minūtes?",
         "opcijas": ["{3|4}", "{1|4}", "{2|3}", "{4|5}"],
         "pareizi": 0, "padoms": "Trīs reizes pa 15."},
        {"jaut": "Kāpēc 60 ir ērts skaitlis?",
         "opcijas": ["Tas dalās ar daudziem skaitļiem",
                     "Tas ir liels", "Tas ir pāra skaitlis",
                     "Tas beidzas ar nulli"],
         "pareizi": 0, "padoms": "2, 3, 4, 5, 6, 10, 12, 15, 20, 30."},
    ], pamats=4),

    Pasaule("Cik ilgi strādā veikals?",
            Ievadi("", [
                {"jaut": "Veikals atvērts no 8 līdz 20. Cik stundas tas "
                         "strādā?",
                 "atb": ["12"], "padoms": "20 − 8."},
                {"jaut": "Kāda daļa no diennakts tas ir? Ieraksti saucēju.",
                 "atb": ["2"], "padoms": "24 : 12."},
                {"jaut": "Pusdienu pārtraukums ilgst 30 minūtes. Kāda daļa "
                         "no stundas tā ir? Ieraksti saucēju.",
                 "atb": ["2"], "padoms": "60 : 30."},
                {"jaut": "Cik minūšu veikals strādā vienā dienā?",
                 "atb": ["720"], "padoms": "12 · 60."},
            ]),
            pavediens="veikals",
            konteksts="Darba laiku raksta stundās, bet pārtraukumus - "
                      "minūtēs; abi ir daļas no diennakts.",
            kapec="Daļa uzreiz pasaka, cik liela ir darba diena."),

    Kopsavilkums([
        "Nosaku, kāda daļa no stundas ir dotais minūšu skaits.",
        "Dalu veselo ar daļas lielumu, lai atrastu saucēju.",
        "Meklēju daļu arī tad, kad dalījums nav vesels.",
        "Pārbaudu atbildi ar reizināšanu.",
    ]),

    Majas([
        "Nosaki, kāda daļa no stundas ir 5, 20 un 50 minūtes.",
        "Izmēri, cik ilgi ēd brokastis, un pasaki, kāda daļa no stundas tā "
        "ir.",
        "Uzzīmē ciparnīcu un iekrāso tajā {1|3} stundas.",
    ]),
]
