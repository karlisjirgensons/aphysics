# -*- coding: utf-8 -*-
"""1. klase, 140. stunda: «Kā izveidot savu metramēru?»

No 10 decimetru sloksnēm salīmē metramēru ar decimetru iedaļām un mēra
klasē: galds - 7 dm, durvis - 2 m. Iedaļas skaita pa 10 cm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, vienibas)

TEMA = "Kā izveidot savu metramēru?"

MERKIS = ("Šodien izveidosim metramēru ar decimetru iedaļām un izmērīsim "
          "priekšmetus klasē.")

SATURS = [
    Sakums("10 decimetri - viens metrs",
           zimejums=vienibas(10, "1 m = 10 dm"),
           paraksts="Katra rūtiņa - 1 dm = 10 cm.",
           fakti=["10 dm = 1 m.",
                  "Iedaļas skaita: 10, 20, 30 ... 100 cm.",
                  "Ar metramēru mēra lielas lietas."]),

    Petijums("Metramērs no papīra", [
        "Izgriez 10 sloksnes pa 10 cm (1 dm).",
        "Salīmē tās vienā garā sloksnē.",
        "Uz katras salīmējuma vietas uzraksti 10, 20, 30 ... 100.",
        "Izmēri solu, tāfeli un durvis.",
    ], vajag="papīrs, lineāls, šķēres, līme"),

    Doma("Mērīšana ar metramēru",
         "Skaiti, cik decimetru ietilpst - un cik vēl pāri.",
         soli=[
             "Pieliec metramēra sākumu pie priekšmeta gala.",
             "Skaiti decimetrus.",
             "Ja garāks par metru - pārceļ.",
         ]),

    Ievadi("Nolasi", [
        {"jaut": "Galds 7 decimetru garumā. Cik cm?", "atb": ["70"],
         "padoms": "7 desmiti."},
        {"jaut": "Sols 12 dm = 1 m un ? dm",
         "atb": ["2"], "padoms": "12 = 10 + 2."},
        {"jaut": "Durvis 2 m. Cik dm?", "atb": ["20"], "padoms": "10 + 10."},
    ]),

    Varianti("Ar ko mērīt?", [
        {"jaut": "Klases garums", "opcijas": ["ar metramēru",
                                             "ar skolas lineālu"],
         "jaukt": False, "pareizi": 0, "padoms": "Garš."},
        {"jaut": "Dzēšgumija", "opcijas": ["ar skolas lineālu",
                                          "ar metramēru"],
         "jaukt": False, "pareizi": 0, "padoms": "Maza."},
    ]),

    Pasaule("Jauna gulta",
            Ievadi("", [
                {"jaut": "Gulta 2 m gara. Istabā pie sienas vieta 18 dm. Cik "
                         "dm gultai pietrūkst?", "atb": ["2"],
                 "padoms": "20 − 18."},
            ]),
            pavediens="maja",
            konteksts="Pirms pirkt gultu, izmēra istabu.",
            kapec="Metramērs palīdz izvēlēties pareizo izmēru."),

    Kopsavilkums([
        "Izveidoju metramēru.",
        "Mēru decimetros.",
        "Zinu, ka 10 dm = 1 m.",
    ]),

    Majas([
        "Izmēri ar metramēru savu gultu.",
        "Izmēri durvju platumu.",
        "Pieraksti dm un cm.",
    ]),
]
