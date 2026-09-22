# -*- coding: utf-8 -*-
"""6. klase, 109. stunda: «Kāda likumsakarība ir virknē?»

Tagad solis vairs nav dots. Virknē tas jāatrod pašam, un tas ne vienmēr ir
saskaitīšana: mēdz būt arī reizināšana vai mainīgs solis. Tas ir uzdevums,
kas trenē domāšanu, nevis rēķināšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Petijums, Sakums, Varianti, Zimejums,
                         restis)

TEMA = "Kāda likumsakarība ir virknē?"

MERKIS = ("Turpināsim virkni un skaidrosim saskatīto likumsakarību.")

SATURS = [
    Sakums("Vispirms atrodi likumu, tad skaitli",
           zimejums=restis([["−1", "−2", "−4", "−8", "?"]],
                           "kāds ir nākamais?"),
           paraksts="Katrs nākamais ir divreiz lielāks pēc moduļa - tātad "
                    "nākamais ir −16.",
           fakti=["Solis var būt saskaitīšana vai reizināšana.",
                  "Dažreiz solis pats mainās pēc likuma.",
                  "Likumu pārbauda uz vairākiem locekļiem, ne uz viena."]),

    Doma("Salīdzini blakus locekļus",
         "Virknes likumu meklē, salīdzinot blakus locekļus: vispirms "
         "pārbauda starpību, tad dalījumu, tad starpību starpības.",
         soli=[
             "Pieraksti starpības starp blakus locekļiem.",
             "Ja tās ir vienādas, likums ir saskaitīšana.",
             "Ja ne, pārbaudi dalījumus - varbūt likums ir reizināšana.",
             "Ja arī tie atšķiras, paskaties, vai pašas starpības veido "
             "virkni.",
             "Pārbaudi likumu uz visiem dotajiem locekļiem.",
         ],
         pieze="Viens loceklis var sakrist nejauši. Likumu uzskata par "
               "atrastu tikai tad, kad tas der visiem dotajiem locekļiem - "
               "tāpēc pārbauda vismaz trīs."),

    Paraugs("Atrodi likumu",
            uzd="Kāds ir nākamais loceklis virknē −1; −2; −4; −8?",
            soli=[
                ("Starpības: −1; −2; −4",
                 "Tās nav vienādas."),
                ("Dalījumi: 2; 2; 2",
                 "Katrs nākamais ir divreiz lielāks pēc moduļa."),
                ("Likums: reizināt ar 2",
                 "Zīme paliek negatīva."),
                ("−8 · 2 = −16",
                 "Nākamais loceklis."),
            ],
            atbilde="−16"),

    Ievadi("Turpini virkni", [
        {"jaut": "−1; −2; −4; −8; ... Kāds ir nākamais?",
         "atb": ["-16", "−16"], "padoms": "Reizina ar 2."},
        {"jaut": "−20; −17; −14; ... Kāds ir nākamais?",
         "atb": ["-11", "−11"], "padoms": "Solis 3."},
        {"jaut": "10; 5; 0; −5; ... Kāds ir nākamais?",
         "atb": ["-10", "−10"], "padoms": "Solis −5."},
        {"jaut": "−1; −3; −6; −10; ... Kāds ir nākamais?",
         "atb": ["-15", "−15"], "padoms": "Starpības aug: 2, 3, 4, 5."},
        {"jaut": "−100; −50; −25; ... Kāds ir nākamais?",
         "atb": ["-12,5", "−12,5", "-12.5"], "padoms": "Dala ar 2."},
        {"jaut": "3; −3; 3; −3; ... Kāds ir nākamais?",
         "atb": ["3"], "padoms": "Zīme mainās pēc kārtas."},
    ], pamats=4,
        ievads="Vispirms pieraksti starpības - tikai tad meklē citu likumu."),

    Petijums("Izpēti virkni līdz galam",
             vajag="burtnīca",
             soli=[
                 "Paņem virkni −2; −5; −9; −14.",
                 "Pieraksti starpības starp blakus locekļiem.",
                 "Pieraksti starpības starp starpībām.",
                 "Formulē likumu un pieraksti nākamos divus locekļus.",
                 "Pārbaudi likumu uz visiem dotajiem locekļiem.",
             ],
             secinajums="Starpības aug par vienu: 3, 4, 5, 6 - tāpēc nākamie "
                        "locekļi ir −20 un −27."),

    Varianti("Kāds te ir likums?", [
        {"jaut": "Virknē −4; −8; −12 likums ir...",
         "opcijas": ["atņemt 4", "reizināt ar 2",
                     "pieskaitīt 4", "dalīt ar 2"],
         "pareizi": 0,
         "padoms": "Starpība ir vienāda."},
        {"jaut": "Virknē −1; −2; −4; −8 likums ir...",
         "opcijas": ["reizināt ar 2", "atņemt 1",
                     "atņemt 2", "pieskaitīt −3"],
         "pareizi": 0,
         "padoms": "Dalījumi ir vienādi."},
        {"jaut": "Ko pārbauda vispirms?",
         "opcijas": ["Starpības starp blakus locekļiem",
                     "Pirmo locekli", "Pēdējo locekli",
                     "Locekļu skaitu"],
         "pareizi": 0,
         "padoms": "Visbiežāk likums ir saskaitīšana."},
        {"jaut": "Cik locekļus vajag, lai pārbaudītu likumu?",
         "opcijas": ["Vismaz trīs", "Vienu", "Divus", "Desmit"],
         "pareizi": 0,
         "padoms": "Divi var sakrist nejauši."},
    ], pamats=4),

    Pasaule("Kā krīt temperatūra?",
            Ievadi("", [
                {"jaut": "Mērījumi: 6; 2; −2; −6 °C. Kāds ir nākamais?",
                 "atb": ["-10", "−10"], "padoms": "Solis −4."},
                {"jaut": "Cik grādu ir starpība starp blakus mērījumiem?",
                 "atb": ["4"], "padoms": "Attālums uz taisnes."},
                {"jaut": "Pēc cik mērījumiem temperatūra sasniedza nulli, "
                         "sākot no 6 °C?",
                 "atb": ["1,5", "1.5"], "padoms": "6 : 4."},
                {"jaut": "Citi mērījumi: −1; −2; −4; −8 °C. Kāds ir "
                         "nākamais?",
                 "atb": ["-16", "−16"], "padoms": "Reizina ar 2."},
            ]),
            pavediens="planeta",
            konteksts="Mērījumu virkne pasaka ne tikai to, kas bija, bet arī "
                      "to, kas būs nākamajā mērījumā.",
            kapec="Likumsakarība ļauj paredzēt, nevis tikai aprakstīt."),

    Zimejums("Divas dažādas virknes",
             restis([["−4", "−8", "−12", "−16"],
                     ["−1", "−2", "−4", "−8"]]),
             paskaidro="Augšējā virknē likums ir saskaitīšana, apakšējā - "
                       "reizināšana. Sākums izskatās līdzīgs, bet turpinājums "
                       "ir pavisam cits.",
             ievads="Līdzīgs sākums nenozīmē vienādu likumu."),

    Kopsavilkums([
        "Atrodu virknes likumu, salīdzinot blakus locekļus.",
        "Pārbaudu gan starpības, gan dalījumus.",
        "Turpinu virkni un pamatoju savu atbildi.",
        "Pārbaudu likumu uz visiem dotajiem locekļiem.",
    ]),

    Majas([
        "Turpini virkni −3; −6; −12; ... ar diviem locekļiem.",
        "Izdomā savu virkni ar negatīviem skaitļiem un likumu.",
        "Iedod to kādam mājās un palūdz atrast likumu.",
    ]),
]
