# -*- coding: utf-8 -*-
"""2. klase, 2. stunda: «Kas visiem ir kopīgs?»

No viena priekšmeta pāriet uz kopu: kopīga pazīme ir īpašība, kas ir katram
kopas priekšmetam. Tad to izmanto pārbaudei - vai jaunais priekšmets der
grupā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, bildes)

TEMA = "Kas visiem ir kopīgs?"

MERKIS = ("Šodien atradīsim kopīgo pazīmi priekšmetu grupai un pārbaudīsim, "
          "vai jauns priekšmets tajā iederas.")

_JA_NE = ["Jā", "Nē"]

SATURS = [
    Sakums("Kas kopīgs bumbai, ābolam un ripiņai?",
           zimejums=bildes([["bumba", "abols", "ripina", "aplis"]]),
           paraksts="Visi ir apaļi.",
           fakti=["Kopīga pazīme ir katram grupas priekšmetam.",
                  "Ja kaut vienam tās nav, pazīme nav kopīga."]),

    Doma("Kopīgā pazīme",
         "Pazīme ir kopīga, ja to var pateikt par katru grupas priekšmetu.",
         soli=[
             "Nosauc pirmā priekšmeta īpašības.",
             "Pārbaudi, kuras no tām ir arī otrajam, trešajam...",
             "Kas palika visiem - tā ir kopīgā pazīme.",
             "Jauns priekšmets der grupā, ja tam arī ir šī pazīme.",
         ]),

    Varianti("Kas kopīgs?", [
        {"jaut": "Kas kopīgs šīm figūrām?",
         "zim": bildes([["trijsturis", "kvadrats", "trijsturis",
                         "kvadrats"]]),
         "opcijas": ["Visām ir stūri", "Visas ir apaļas",
                     "Visām ir 4 stūri"], "pareizi": 0,
         "padoms": "Trijstūrim ir 3 stūri, kvadrātam 4."},
        {"jaut": "Kas kopīgs: ābols, zivs, maize, siers?",
         "opcijas": ["Visus var ēst", "Visi aug kokā", "Visi ir sarkani"],
         "pareizi": 0, "padoms": "Zivs kokā neaug."},
        {"jaut": "Kas kopīgs skaitļiem 20, 40, 60, 80?",
         "opcijas": ["Beidzas ar 0", "Visi mazāki nekā 50",
                     "Viencipara skaitļi"], "pareizi": 0,
         "padoms": "Paskaties pēdējo ciparu."},
        {"jaut": "Kas kopīgs: suns, putns, zivs, kaķis?",
         "opcijas": ["Visi ir dzīvnieki", "Visiem ir 4 kājas",
                     "Visi peld"], "pareizi": 0,
         "padoms": "Putnam ir 2 kājas."},
        {"jaut": "Kas kopīgs skaitļiem 15, 25, 35, 45?",
         "opcijas": ["Beidzas ar 5", "Sākas ar 5", "Visi lielāki nekā 20"],
         "pareizi": 0, "padoms": "15 nav lielāks nekā 20."},
        {"jaut": "Kas kopīgs: krēsls, galds, gulta, skapis?",
         "opcijas": ["Tās ir mēbeles", "Tās ir no koka", "Tās ir mazas"],
         "pareizi": 0, "padoms": "Mēbeles var būt arī no metāla."},
    ], pamats=4),

    Varianti("Vai der grupā?", [
        {"jaut": "Grupa: skaitļi, kas beidzas ar 0. Vai 70 der?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 0,
         "padoms": "70 beidzas ar 0."},
        {"jaut": "Grupa: skaitļi, kas mazāki nekā 20. Vai 21 der?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 1,
         "padoms": "21 ir lielāks nekā 20."},
        {"jaut": "Grupa: figūras bez stūriem. Vai kvadrāts der?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 1,
         "padoms": "Kvadrātam ir 4 stūri."},
        {"jaut": "Grupa: dzīvnieki, kas lido. Vai putns der?",
         "opcijas": _JA_NE, "jaukt": False, "pareizi": 0,
         "padoms": "Putni lido."},
    ]),

    Ievadi("Cik der grupā?", [
        {"jaut": "Cik no šiem skaitļiem beidzas ar 0: 10, 25, 30, 44, 50, "
                 "60?", "atb": ["4"], "padoms": "10, 30, 50, 60."},
        {"jaut": "Cik priekšmetiem ir stūri?",
         "zim": bildes([["kvadrats", "aplis", "trijsturis", "bumba",
                         "kvadrats"]]),
         "atb": ["3"], "padoms": "Bumbai un aplim stūru nav."},
    ]),

    Pasaule("Kas ielikts šķirošanas kastē?",
            Varianti("", [
                {"jaut": "Kastē ir avīze, kartona kaste un burtnīca. Kas "
                         "tiem kopīgs?",
                 "opcijas": ["Visi ir no papīra", "Visi ir no stikla",
                             "Visi ir ēdami"], "pareizi": 0,
                 "padoms": "Kartons arī ir papīrs."},
                {"jaut": "Kurš priekšmets der šajā kastē?",
                 "opcijas": ["Veca grāmata", "Stikla burka",
                             "Plastmasas pudele"], "pareizi": 0,
                 "padoms": "Meklē papīru."},
            ]),
            pavediens="planeta",
            konteksts="Atkritumus šķiro pēc tā, no kā tie ir izgatavoti.",
            kapec="Šķirošana ir grupēšana pēc kopīgas pazīmes."),

    Kopsavilkums([
        "Atrodu pazīmi, kas ir kopīga visiem grupas priekšmetiem.",
        "Pārbaudu, vai jauns priekšmets der grupā.",
        "Zinu: ja vienam pazīmes nav, tā nav kopīga.",
    ]),

    Majas([
        "Atrodi mājās 4 priekšmetus ar kopīgu pazīmi.",
        "Lai mājinieks uzmin, kāda ir pazīme.",
        "Palīdzi sašķirot atkritumus un nosauc katras kastes pazīmi.",
    ]),
]
