# -*- coding: utf-8 -*-
"""1. klase, 131. stunda: «Ko iekļaut iepirkumu sarakstā?»

Iepirkumu saraksts kā tabula: prece, daudzums, cena. No tabulas saskaita
kopējo summu. Daudzums «2 gab. pa 3 €» - saskaita 3 + 3.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Ko iekļaut iepirkumu sarakstā?"

MERKIS = ("Šodien veidosim iepirkumu sarakstu tabulā ar daudzumu un cenu.")

_SARAKSTS = restis([["prece", "cik", "cena"], ["maize", 1, "2 €"],
                    ["piens", 2, "1 €"], ["āboli", 1, "3 €"]])

SATURS = [
    Sakums("Kas jānopērk vakariņām?",
           zimejums=_SARAKSTS,
           paraksts="Katrai precei - daudzums un cena.",
           fakti=["Tabulā: prece, cik, cena.",
                  "2 pieni pa 1 € - 1 € + 1 €.",
                  "Saskaiti visu - zini, cik ņemt līdzi."]),

    Doma("Saraksts tabulā",
         "Kārtīgs saraksts pasaka, ko pirkt, cik un par cik.",
         soli=[
             "Uzraksti preces.",
             "Blakus - cik gabalu.",
             "Tad - cenu par vienu.",
             "Saskaiti kopējo summu.",
         ]),

    Ievadi("Aprēķini", [
        {"jaut": "Cik maksā 2 pieni?", "zim": _SARAKSTS, "atb": ["2"],
         "padoms": "1 € + 1 €."},
        {"jaut": "Cik maksā viss saraksts (€)?", "zim": _SARAKSTS,
         "atb": ["7"], "padoms": "2 + 2 + 3."},
        {"jaut": "Tev 10 €. Cik paliks (€)?", "zim": _SARAKSTS,
         "atb": ["3"], "padoms": "10 − 7."},
    ]),

    Varianti("Kas sarakstā vajadzīgs?", [
        {"jaut": "Ko obligāti rakstīt iepirkumu sarakstā?",
         "opcijas": ["preci un daudzumu", "veikala adresi",
                     "pārdevēja vārdu"], "pareizi": 0,
         "padoms": "Ko un cik."},
        {"jaut": "Kāpēc noder cena sarakstā?",
         "opcijas": ["lai zinātu, vai pietiks naudas", "lai skaisti",
                     "nav vajadzīga"], "pareizi": 0,
         "padoms": "Iepriekš saskaiti."},
    ]),

    Petijums("Mans saraksts", [
        "Izdomā ēdienu (piem., pankūkas).",
        "Uzraksti tabulā, kas jānopērk.",
        "Pieraksti daudzumu un cenu (no reklāmas).",
        "Saskaiti kopējo summu.",
    ], vajag="lapa, lineāls, veikala reklāma"),

    Pasaule("Pikniks",
            Ievadi("", [
                {"jaut": "Piknikam: 3 bulciņas pa 1 €, sula 2 €. Cik kopā?",
                 "atb": ["5"], "padoms": "1 + 1 + 1 + 2."},
            ]),
            pavediens="veikals",
            konteksts="Ģimene gatavojas piknikam.",
            kapec="Saraksts palīdz neko neaizmirst un nepārtērēt."),

    Kopsavilkums([
        "Veidoju iepirkumu sarakstu tabulā.",
        "Ierakstu daudzumu un cenu.",
        "Saskaitu kopējo summu.",
    ]),

    Majas([
        "Uzraksti ģimenes nedēļas iepirkumu sarakstu.",
        "Veikalā atzīmē cenas.",
        "Saskaiti kopā.",
    ]),
]
