# -*- coding: utf-8 -*-
"""4. klase, 47. stunda: «Kura izteiksme lielāka?»

4.2. temata pēdējā stunda pirms PD. Salīdzināt divu darbību izteiksmes,
spriežot par reizinātājiem, dalītājiem un saskaitāmajiem - bez precīza
rēķina. Tas ir 2. stundas spriedums, tikai tagad ar reizināšanu un
dalīšanu: lielāks dalītājs - mazāks dalījums.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, restis)

TEMA = "Kura izteiksme lielāka?"

MERKIS = ("Salīdzināsim divu darbību izteiksmes spriežot, neaprēķinot "
          "precīzās vērtības.")

SATURS = [
    Sakums("Kas ir vairāk: 48 · 7 vai 48 · 6 + 50?",
           zimejums=restis([["48 · 7", "=", "48 · 6", "+", "48"],
                            ["48 · 6 + 50", "=", "48 · 6", "+", "50"]],
                           "salīdzini tikai atšķirīgo"),
           paraksts="48 < 50 - tātad otrā izteiksme lielāka.",
           fakti=["Nerēķinot var salīdzināt, ja pamana kopīgo daļu.",
                  "Kopīgā daļa: 48 · 6."]),

    Doma("Atrodi kopīgo, salīdzini atšķirīgo",
         "Reizinājumā lielāks reizinātājs - lielāks reizinājums; dalījumā "
         "lielāks dalītājs - mazāks dalījums.",
         soli=[
             "Reizinājumi: 37 · 8 > 37 · 7, jo 8 > 7.",
             "Dalījumi: 840 : 4 > 840 : 5, jo dalot ar 4, daļas lielākas.",
             "Pārveido, lai redzētu kopīgo: 25 · 9 = 25 · 8 + 25.",
             "Salīdzini tikai to, kas atšķiras.",
         ],
         pieze="Dalot to pašu picu 4 daļās, gabali ir lielāki nekā 5 daļās."),

    Paraugs("600 : 3 un 600 : 4",
            uzd="Salīdzini 600 : 3 un 600 : 4, nerēķinot.",
            soli=[
                ("600 = 600", "Dalāmie vienādi."),
                ("3 < 4", "Pirmajā dala mazākās daļās."),
                ("600 : 3 > 600 : 4", "Mazāk daļu - lielākas daļas."),
            ],
            atbilde="600 : 3 > 600 : 4"),

    Slidnis("Dalītājs aug - dalījums sarūk",
            soli=[
                {"v": "120 : 2 = 60", "teksts": "Divas daļas - lielas.", "josla": 100},
                {"v": "120 : 3 = 40", "teksts": "Trīs daļas.", "josla": 67},
                {"v": "120 : 4 = 30", "teksts": "Četras daļas.", "josla": 50},
                {"v": "120 : 6 = 20", "teksts": "Sešas daļas.", "josla": 33},
                {"v": "120 : 12 = 10", "teksts": "Divpadsmit mazas daļas.", "josla": 17},
            ],
            ievads="Tas pats 120 - dalīts arvien vairāk daļās."),

    Varianti("Liec zīmi, nerēķinot", [
        {"jaut": "37 · 8 ☐ 37 · 9", "opcijas": ["<", ">", "="],
         "pareizi": 0, "padoms": "8 < 9."},
        {"jaut": "720 : 8 ☐ 720 : 9", "opcijas": [">", "<", "="],
         "pareizi": 0, "padoms": "Dalot ar mazāku, dalījums lielāks."},
        {"jaut": "25 · 4 ☐ 4 · 25", "opcijas": ["=", "<", ">"],
         "pareizi": 0, "padoms": "Reizinātājus drīkst mainīt vietām."},
        {"jaut": "56 · 5 + 56 ☐ 56 · 6", "opcijas": ["=", "<", ">"],
         "pareizi": 0, "padoms": "56 · 5 + 56 = 56 · 6."},
        {"jaut": "300 : 5 · 2 ☐ 300 : 5 · 3", "opcijas": ["<", ">", "="],
         "pareizi": 0, "padoms": "Tas pats 60, reizināts ar 2 un ar 3."},
        {"jaut": "99 · 7 ☐ 100 · 7", "opcijas": ["<", ">", "="],
         "pareizi": 0, "padoms": "99 < 100."},
    ], pamats=4),

    Ievadi("Par cik atšķiras?", [
        {"jaut": "Par cik 48 · 7 lielāks nekā 48 · 6?", "atb": ["48"],
         "padoms": "Viens 48 vairāk."},
        {"jaut": "Par cik 25 · 10 lielāks nekā 25 · 8?", "atb": ["50"],
         "padoms": "Divi 25 vairāk."},
        {"jaut": "Par cik 100 · 7 lielāks nekā 99 · 7?", "atb": ["7"],
         "padoms": "Viens 7 vairāk."},
        {"jaut": "Par cik 400 : 4 lielāks nekā 400 : 5?", "atb": ["20"],
         "padoms": "100 − 80."},
    ]),

    Pasaule("Kurš piedāvājums izdevīgāks?",
            Varianti("", [
                {"jaut": "Pica 24 € dalīta uz 3 vai tā pati pica uz 4 "
                         "draugiem. Kur katram jāmaksā mazāk?",
                 "opcijas": ["uz 4", "uz 3", "vienādi"], "pareizi": 0,
                 "padoms": "24 : 4 < 24 : 3."},
                {"jaut": "Veikals A: 6 pudeles pa 89 ct. Veikals B: 6 "
                         "pudeles pa 95 ct. Kur lētāk?",
                 "opcijas": ["A", "B", "vienādi"], "pareizi": 0,
                 "padoms": "89 < 95."},
                {"jaut": "Abonements: 12 mēneši pa 9 € vai 11 mēneši pa 9 € "
                         "un vēl 10 €?",
                 "opcijas": ["pirmais lētāks", "otrais lētāks", "vienādi"],
                 "pareizi": 0, "padoms": "9 < 10."},
            ]),
            pavediens="veikals",
            konteksts="Veikalā lētāko var atrast bez kalkulatora - ja "
                      "salīdzina gudri.",
            kapec="Spriedums ir ātrāks par rēķinu un tikpat drošs."),

    Kopsavilkums([
        "Salīdzinu izteiksmes, atrodot kopīgo daļu.",
        "Zinu: lielāks dalītājs - mazāks dalījums.",
        "Pārveidoju izteiksmi, lai to būtu viegli salīdzināt.",
        "Esmu gatavs 4.2. temata pārbaudes darbam.",
    ]),

    Majas([
        "Izdomā divas izteiksmes, kuras var salīdzināt nerēķinot.",
        "Pajautā mājiniekiem: kas lielāks - 1000 : 8 vai 1000 : 9?",
        "Atkārto: reizināšana stabiņā, dalīšana stūrītī, atlikums.",
    ], ievads="Nākamajā stundā - pārbaudes darbs par 4.2. tematu."),
]
