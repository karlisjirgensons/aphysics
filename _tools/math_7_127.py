# -*- coding: utf-8 -*-
"""7. klase, 127. stunda: «Kā izteiksme apraksta dzīves situāciju?»

Izteiksme ir modelis: tā apraksta cenu, attālumu vai laiku vienā rindā.
Stunda veido izteiksmi no teksta, vienkāršo to un aprēķina - ceļojuma
budžets, piegāde, taksometrs.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izteiksme apraksta dzīves situāciju?"

MERKIS = ("Veidosim un vienkāršosim izteiksmi praktiskai situācijai ar "
          "cenām vai attālumiem.")

SATURS = [
    Sakums("Klases ekskursijas budžets",
           zimejums=restis([["izdevumi", "izteiksme"],
                            ["autobuss (kopā)", "240"],
                            ["biļete katram", "8n"],
                            ["pusdienas katram", "6n"],
                            ["kopā", "14n + 240"]]),
           paraksts="n - skolēnu skaits.",
           fakti=["Viena izteiksme jebkuram skolēnu skaitam.",
                  "Katram: (14n + 240) : n.",
                  "Jo vairāk skolēnu, jo lētāk katram."]),

    Doma("No teksta uz modeli",
         "Dzīves situāciju apraksta ar izteiksmi: nosaka mainīgo, "
         "fiksētās izmaksas un izmaksas par vienību, uzraksta izteiksmi un "
         "vienkāršo to.",
         soli=[
             "Nosaki mainīgo (skolēnu skaits, km, dienas).",
             "Atrodi fiksētās izmaksas - tās nereizina.",
             "Atrodi izmaksas par vienu - tās reizina ar mainīgo.",
             "Uzraksti summu un savelc.",
         ]),

    Paraugs("Ekskursija",
            uzd="Autobuss 240 €, biļete 8 €, pusdienas 6 € katram. Cik "
                "jāmaksā katram, ja brauc 24 skolēni?",
            soli=[
                ("Kopā: 240 + 8n + 6n = 14n + 240", "Izteiksme."),
                ("n = 24: 14 · 24 + 240 = 576 (€)", "Visiem."),
                ("576 : 24 = 24 (€)", "Katram."),
            ],
            atbilde="24 € katram"),

    Ievadi("Aprēķini", [
        {"jaut": "Ja brauc 30 skolēni, cik € maksā katrs?",
         "atb": ["22"], "padoms": "(420 + 240) : 30."},
        {"jaut": "Piegāde: 3 € + 0,5 € par km. Izteiksme 3 + 0,5d. Cik € "
                 "par 12 km?",
         "atb": ["9"], "padoms": "3 + 6."},
        {"jaut": "Velosipēda noma: 5 € + 2 € stundā. Cik € par 4 h?",
         "atb": ["13"], "padoms": "5 + 8."},
        {"jaut": "Noma: 5 + 2t = 21. Cik stundas?",
         "atb": ["8"], "padoms": "2t = 16."},
    ]),

    Varianti("Kura izteiksme?", [
        {"jaut": "Telefona tarifs: 6 € mēnesī un 0,1 € par katru minūti m.",
         "opcijas": ["6 + 0,1m", "6,1m", "0,1 + 6m", "6m + 0,1"],
         "pareizi": 0, "padoms": "Fiksēts + par vienību."},
        {"jaut": "Brauciens: benzīns 0,12 € par km un autostāvvieta 5 €, "
                 "turp un atpakaļ d km katrā virzienā.",
         "opcijas": ["0,24d + 5", "0,12d + 5", "0,12d + 10", "2(0,12d + 5)"],
         "pareizi": 0, "padoms": "2d km, stāvvieta vienreiz."},
    ]),

    Pasaule("Kafejnīcas bizness",
            Ievadi("", [
                {"jaut": "Kafija maksā 3 €, izejvielas - 0,8 € par tasi, "
                         "īre 900 € mēnesī. Peļņa: 3n − 0,8n − 900 = ?n − "
                         "900. Koeficients?",
                 "atb": ["2,2"], "padoms": "3 − 0,8."},
                {"jaut": "Peļņa, ja pārdod 1000 tases (€)?",
                 "atb": ["1300"], "padoms": "2200 − 900."},
                {"jaut": "Cik tasēm peļņa ir 0? (Noapaļo uz augšu.)",
                 "atb": ["410"], "padoms": "900 : 2,2 ≈ 409,1."},
            ]),
            pavediens="veikals",
            konteksts="Katrs mazais uzņēmums sāk ar šo izteiksmi: ienākumi "
                      "mīnus izmaksas.",
            kapec="Izteiksme parāda, cik jāpārdod, lai nezaudētu."),

    Kopsavilkums([
        "Veidoju izteiksmi no teksta.",
        "Atšķiru fiksētas izmaksas un izmaksas par vienību.",
        "Vienkāršoju un aprēķinu.",
        "Izmantoju izteiksmi lēmumam.",
    ]),

    Majas([
        "Uzraksti izteiksmi ģimenes ceļojumam ar n dienām.",
        "Aprēķini peļņu citai biznesa idejai.",
        "Salīdzini divu nomas vietu cenas ar izteiksmēm.",
    ]),
]
