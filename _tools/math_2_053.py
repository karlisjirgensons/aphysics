# -*- coding: utf-8 -*-
"""2. klase, 53. stunda: «Kur lētāk?»

Tēmas noslēgums - mazs pētījums: vienas preces cena divos veikalos,
starpība un kopējā cena vairākām precēm. Secinājumu pamato ar skaitļiem,
nevis ar «man liekas».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, restis)

TEMA = "Kur lētāk?"

MERKIS = ("Šodien veiksim nelielu pētījumu par cenu atšķirībām un "
          "pamatosim secinājumu ar aprēķiniem.")

_CENAS = restis([["prece", "veikals A", "veikals B"],
                 ["penālis", "8 €", "6 €"],
                 ["burtnīcas", "5 €", "7 €"],
                 ["mugursoma", "35 €", "29 €"]])

SATURS = [
    Sakums("Vienas un tās pašas lietas divos veikalos maksā dažādi. Kur "
           "iepirkties?",
           zimejums=_CENAS,
           fakti=["Salīdzina katras preces cenu.",
                  "Tad saskaita visu, ko vajag nopirkt.",
                  "Lētākais veikals nav vienmēr lētāks visā."]),

    Doma("Cenu pētījums",
         "Secinājums balstās uz aprēķinu, nevis minējumu.",
         soli=[
             "Pieraksti cenas tabulā.",
             "Katrai precei atrodi, par cik lētāk.",
             "Saskaiti kopējo cenu katrā veikalā.",
             "Salīdzini un pamato: «B ir lētāks par ... €».",
         ]),

    Ievadi("Rēķini", [
        {"jaut": "Par cik € penālis veikalā B lētāks?", "zim": _CENAS,
         "atb": ["2"], "mers": "€", "padoms": "8 − 6."},
        {"jaut": "Par cik € mugursoma veikalā B lētāka?", "zim": _CENAS,
         "atb": ["6"], "mers": "€", "padoms": "35 − 29."},
        {"jaut": "Cik maksā visas trīs preces veikalā A?", "zim": _CENAS,
         "atb": ["48"], "mers": "€", "padoms": "8 + 5 + 35."},
        {"jaut": "Cik maksā visas trīs preces veikalā B?", "zim": _CENAS,
         "atb": ["42"], "mers": "€", "padoms": "6 + 7 + 29."},
        {"jaut": "Par cik € viss veikalā B lētāk?", "zim": _CENAS,
         "atb": ["6"], "mers": "€", "padoms": "48 − 42."},
        {"jaut": "Cik maksātu, ja katru preci pērk tur, kur lētāk?",
         "zim": _CENAS, "atb": ["40"], "mers": "€",
         "padoms": "6 + 5 + 29."},
    ], pamats=4),

    Varianti("Secinājums", [
        {"jaut": "Kurš apgalvojums ir patiess?", "zim": _CENAS,
         "opcijas": ["Burtnīcas lētākas veikalā A",
                     "Veikalā B viss ir lētāks",
                     "Penālis lētāks veikalā A"], "pareizi": 0,
         "padoms": "5 € un 7 €."},
    ]),

    Petijums("Mūsu cenu pētījums", [
        "Izvēlies 3 preces, ko bieži pērk ģimene.",
        "Pieraksti to cenas divos veikalos vai internetā.",
        "Aprēķini starpību un kopējo summu.",
        "Pastāsti klasei, kur un par cik lētāk.",
    ], vajag="tabula, zīmulis, pieaugušā palīdzība"),

    Pasaule("Skolas somas iepirkums",
            Ievadi("", [
                {"jaut": "Mammai ir 45 €. Cik paliks, ja visu nopirks "
                         "veikalā B?", "zim": _CENAS, "atb": ["3"],
                 "mers": "€", "padoms": "45 − 42."},
            ]),
            pavediens="veikals",
            konteksts="Pirms 1. septembra ģimene pērk skolas lietas.",
            kapec="Salīdzinot cenas, var ietaupīt."),

    Kopsavilkums([
        "Salīdzinu cenas divos veikalos.",
        "Aprēķinu starpību un kopējo summu.",
        "Pamatoju secinājumu ar skaitļiem.",
    ]),

    Majas([
        "Kopā ar pieaugušo salīdzini piena cenu divos veikalos.",
        "Par cik centiem atšķiras?",
        "Pastāsti klasei savu atradumu.",
    ]),
]
