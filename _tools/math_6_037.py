# -*- coding: utf-8 -*-
"""6. klase, 37. stunda: «Kur tas noder dzīvē?»

Temata pēdējā mācību stunda pirms pārbaudes darba. Te nav jaunu likumu - ir
uzdevumi, kuros pašam jāizlemj, kura darbība vajadzīga. Tieši izvēle, nevis
rēķināšana, ir tas, ko pārbaudes darbs vērtē.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Kustiba, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti)

TEMA = "Kur tas noder dzīvē?"

MERKIS = ("Risināsim situāciju uzdevumus, kuru risinājumā jāreizina vai "
          "jādala daļas.")

SATURS = [
    Sakums("Grūtākais ir izvēlēties darbību",
           fakti=["«Daļa no» nozīmē reizināšanu.",
                  "«Cik reižu pietiks» nozīmē dalīšanu.",
                  "«Cik ir kopā» nozīmē saskaitīšanu - arī tā gadās."]),

    Doma("Vispirms izlem, tad rēķini",
         "Uzdevuma atslēga ir jautājums: vai meklē daļu no lieluma, vai "
         "skaita, cik reižu viens ietilpst otrā.",
         soli=[
             "Izlasi jautājumu un pasvītro, ko meklē.",
             "Pārbaudi, vai vārds «no» tekstā parādās - tad reizini.",
             "Pārbaudi, vai jautā «cik reižu» vai «cik porciju» - tad dali.",
             "Novērtē atbildi, pirms rēķini.",
             "Izrēķini, pārbaudi un pieraksti ar mērvienību.",
         ],
         pieze="Viens un tas pats teikums var prasīt abas darbības: «{2|3} "
               "no 12 l sadala {1|4} l pudelēs» ir vispirms reizināšana, "
               "tad dalīšana."),

    Paraugs("Divi soļi vienā uzdevumā",
            uzd="Tvertnē ir 12 l. Izlej {2|3} no tā un sadala {1|4} l "
                "pudelēs. Cik pudeļu sanāks?",
            soli=[
                ("{2|3} · 12 = 8 l",
                 "Vispirms daļa no lieluma - reizināšana."),
                ("8 : {1|4}",
                 "Tagad jautā, cik reižu pietiek - dalīšana."),
                ("8 · 4 = 32",
                 "Dalīšana ar daļu ir reizināšana ar apgriezto."),
                ("Novērtējums: no 8 litriem ceturtdaļlitra pudeļu ir daudz",
                 "32 ir ticams skaitlis."),
            ],
            atbilde="32 pudeles"),

    Ievadi("Izvēlies darbību un izrēķini", [
        {"jaut": "{3|4} no 20 kg. Cik kilogramu?",
         "atb": ["15"], "padoms": "«No» nozīmē reizināt."},
        {"jaut": "6 l sadala {1|3} l glāzēs. Cik glāžu?",
         "atb": ["18"], "padoms": "«Cik glāžu» nozīmē dalīt."},
        {"jaut": "{2|5} no 45 min. Cik minūšu?",
         "atb": ["18"], "padoms": "45 : 5 · 2."},
        {"jaut": "4{1|2} m auduma griež {3|4} m gabalos. Cik gabalu?",
         "atb": ["6"], "padoms": "{9|2} · {4|3}."},
        {"jaut": "{5|6} no 42 €. Cik eiro?",
         "atb": ["35"], "padoms": "42 : 6 · 5."},
        {"jaut": "3 kg riekstu fasē {1|8} kg maisiņos. Cik maisiņu?",
         "atb": ["24"], "padoms": "3 · 8."},
    ], pamats=4),

    Pasaule("Cik tālu tiks ekspedīcija?",
            Kustiba("", [
                {"jaut": "Maršruts ir 60 km. Pirmajā dienā veic {1|3}. Cik "
                         "km tas ir?",
                 "atb": 20, "beigas": 60, "iedala": 10, "mers": "kilometri",
                 "merkis": "1. diena", "objekts": "Grupa",
                 "padoms": "60 : 3."},
                {"jaut": "Otrajā dienā veic {1|2} no atlikuma. Cik km kopā "
                         "no starta?",
                 "atb": 40, "beigas": 60, "iedala": 10, "mers": "kilometri",
                 "merkis": "2. diena", "objekts": "Grupa",
                 "padoms": "Atlikums 40 km, puse ir 20; 20 + 20."},
                {"jaut": "Trešajā dienā veic {3|4} no jaunā atlikuma. Cik km "
                         "kopā no starta?",
                 "atb": 55, "beigas": 60, "iedala": 10, "mers": "kilometri",
                 "merkis": "3. diena", "objekts": "Grupa",
                 "padoms": "Atlikums 20 km, {3|4} ir 15; 40 + 15."},
                {"jaut": "Ceturtajā dienā jāveic viss atlikušais. Cik km "
                         "kopā būs no starta?",
                 "atb": 60, "beigas": 60, "iedala": 10, "mers": "kilometri",
                 "merkis": "finišs", "objekts": "Grupa",
                 "padoms": "Viss maršruts."},
            ]),
            pavediens="celojums",
            konteksts="Katru dienu daļu rēķina nevis no visa maršruta, bet "
                      "no tā, kas vēl palicis.",
            kapec="Tieši šī atšķirība ir uzdevuma grūtākā vieta."),

    Varianti("Kura darbība te der?", [
        {"jaut": "«Cik porciju sanāks no 3 kg?» - kura darbība?",
         "opcijas": ["Dalīšana", "Reizināšana", "Saskaitīšana",
                     "Atņemšana"],
         "pareizi": 0,
         "padoms": "Jautā, cik reižu pietiek."},
        {"jaut": "«Cik ir {2|3} no 15?» - kura darbība?",
         "opcijas": ["Reizināšana", "Dalīšana", "Atņemšana",
                     "Kāpināšana"],
         "pareizi": 0,
         "padoms": "«No» nozīmē reizināt."},
        {"jaut": "Pirmajā dienā veica {1|3} no 60 km. Cik km palika?",
         "opcijas": ["40", "20", "30", "60"],
         "pareizi": 0,
         "padoms": "60 − 20."},
        {"jaut": "Otrajā dienā veica {1|2} no *atlikuma*. Cik km tas ir?",
         "opcijas": ["20", "30", "10", "40"],
         "pareizi": 0,
         "padoms": "Puse no 40, nevis no 60."},
    ], pamats=4),

    Petijums("Sagatavojies pārbaudes darbam",
             vajag="burtnīca un šīs tēmas uzdevumi",
             soli=[
                 "Izvēlies trīs uzdevumus, kuros iepriekš kļūdījies.",
                 "Atrisini tos no jauna, pierakstot visus soļus.",
                 "Pie katra pieraksti, kura darbība bija jāizvēlas un kāpēc.",
                 "Pārbaudi katru atbildi ar pretējo darbību.",
             ],
             secinajums="Kļūdas parasti atkārtojas vienā vietā - tieši tur, "
                        "kur jāizvēlas darbība."),

    Kopsavilkums([
        "Izvēlos darbību pēc uzdevuma jautājuma, ne pēc skaitļiem.",
        "Risinu uzdevumus, kuros vajadzīgi divi soļi.",
        "Ievēroju, no kā tiek ņemta daļa: no visa vai no atlikuma.",
        "Novērtēju un pārbaudu savu atbildi.",
    ]),

    Majas([
        "Izdomā uzdevumu, kurā vajag gan reizināšanu, gan dalīšanu ar daļu.",
        "Atrisini to un iedod kādam mājās pārbaudīt.",
        "Pieraksti trīs vārdus, kas uzdevumā norāda uz dalīšanu.",
    ]),
]
