# -*- coding: utf-8 -*-
"""2. klase, 171. stunda: «Kā risinu uzdevumu ar diviem soļiem?»

Gada noslēgums, 3. stunda: divu soļu uzdevums no sākuma līdz beigām -
izlasīt, uzzīmēt, izvēlēties darbības, pierakstīt izteiksmi, aprēķināt,
pārbaudīt un atbildēt. Skolēns stāsta savu risinājumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, algoritms)

TEMA = "Kā risinu uzdevumu ar diviem soļiem?"

MERKIS = ("Šodien risināsim divu soļu uzdevumu, pierakstīsim to ar "
          "izteiksmi un paskaidrosim risinājumu.")

_PLANS = algoritms(["Izlasi un atrodi jautājumu",
                    "Uzzīmē sloksnes vai shēmu",
                    ("Vai uzreiz var atbildēt?", "Rēķini", "Atrodi 1. soli"),
                    "Pieraksti izteiksmi un aprēķini",
                    "Pārbaudi un atbildi"])

SATURS = [
    Sakums("Kāds ir tavs plāns, ja uzdevums izskatās grūts?",
           zimejums=_PLANS,
           fakti=["Grūtu uzdevumu sadala soļos.",
                  "Zīmējums parāda, kas jāaprēķina.",
                  "Pārbaude pasaka, vai atbilde ticama."]),

    Doma("Risinājuma ceļš",
         "Vispirms saproti, tad rēķini, beigās pārbaudi.",
         soli=[
             "Ko jautā? Ko zinu?",
             "Ko jāuzzina vispirms?",
             "Pieraksti izteiksmi ar abām darbībām.",
             "Aprēķini, pārbaudi, uzraksti atbildi teikumā.",
         ]),

    Paraugs("Ābolu pīrāgi",
            uzd="Vienam pīrāgam vajag 4 ābolus. Mamma cep 6 pīrāgus un vēl "
                "5 ābolus apēd. Cik ābolu vajag?",
            soli=[("1) 6 · 4 = 24", "Āboli pīrāgiem."),
                  ("2) 24 + 5 = 29", "Plus apēstie."),
                  ("6 · 4 + 5 = 29", "Viena izteiksme.")],
            atbilde="29 āboli"),

    Ievadi("Atrisini", [
        {"jaut": "Plauktā 5 rindas pa 8 grāmatām. 12 izņēma. Cik palika?",
         "atb": ["28"], "padoms": "5 · 8 − 12."},
        {"jaut": "Annai 15 €, Jānim 2 reizes vairāk. Cik abiem?",
         "atb": ["45"], "mers": "€", "padoms": "30 + 15."},
        {"jaut": "36 bērni brauc 4 autobusos vienādi. Katrā vēl 2 "
                 "skolotāji. Cik cilvēku vienā autobusā?", "atb": ["11"],
         "padoms": "36 : 4 + 2."},
        {"jaut": "Bija 80 €. Nopirka 3 bumbas pa 5 € un tīklu par 20 €. "
                 "Cik palika?", "atb": ["45"], "mers": "€",
         "padoms": "80 − 15 − 20."},
    ]),

    Varianti("Kurš ir pirmais solis?", [
        {"jaut": "«7 kastēs pa 5 zīmuļiem, 9 iedeva klasei. Cik palika?»",
         "opcijas": ["7 · 5", "35 − 9", "7 + 5"], "pareizi": 0,
         "padoms": "Vispirms, cik bija."},
        {"jaut": "Kāds ir otrais solis tam pašam uzdevumam?",
         "opcijas": ["35 − 9", "7 · 9", "35 + 9"], "pareizi": 0,
         "padoms": "Iedeva - atņem."},
    ]),

    Pasaule("Vasaras nometne",
            Ievadi("", [
                {"jaut": "Nometnē 4 teltis pa 5 bērniem un 3 vadītāji. Cik "
                         "cilvēku kopā?", "atb": ["23"],
                 "padoms": "4 · 5 + 3."},
                {"jaut": "Vakariņām katram 2 desiņas. Cik desiņu vajag?",
                 "atb": ["46"], "padoms": "23 · 2 = 23 + 23."},
            ]),
            pavediens="celojums",
            konteksts="Vasarā bērni dodas nometnē pie ezera.",
            kapec="Katrs solis sagatavo nākamo."),

    Kopsavilkums([
        "Sadalu uzdevumu soļos.",
        "Pierakstu izteiksmi ar divām darbībām.",
        "Paskaidroju un pārbaudu savu risinājumu.",
    ]),

    Majas([
        "Izdomā divu soļu uzdevumu par vasaru.",
        "Atrisini to pēc plāna.",
        "Izstāsti risinājumu mājiniekam.",
    ]),
]
