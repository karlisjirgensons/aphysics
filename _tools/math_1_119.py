# -*- coding: utf-8 -*-
"""1. klase, 119. stunda: «Kāds stāsts der šim zīmējumam?»

Otrādi nekā 114. stundā: dots shematisks zīmējums (sloksnes vai mājiņa),
skolēns izdomā stāstu, kas tam der, un izrēķina «?».
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, majina, sloksnes)

TEMA = "Kāds stāsts der šim zīmējumam?"

MERKIS = ("Šodien izdomāsim situāciju, kas atbilst dotam shematiskam "
          "zīmējumam.")

_Z1 = sloksnes([("A", 10), ("B", 6, "?")])

SATURS = [
    Sakums("Kāds stāsts der šim zīmējumam?",
           zimejums=_Z1,
           paraksts="Piemēram: Annai 10 uzlīmes, Bertai par 4 mazāk.",
           fakti=["Nolasi: kas zināms, kas «?».",
                  "Izdomā, ko joslas nozīmē.",
                  "Izrēķini «?»."]),

    Doma("No zīmējuma uz stāstu",
         "Zīmējums pasaka skaitļus un darbību - tu izdomā, par ko tas ir.",
         soli=[
             "Kas ir joslas vai mājiņas daļas?",
             "Izvēlies lietas: uzlīmes, āboli, bērni.",
             "Uzraksti stāstu un jautājumu.",
         ]),

    Varianti("Kurš stāsts der?", [
        {"jaut": "Kurš stāsts der?", "zim": _Z1,
         "opcijas": ["Annai 10 uzlīmes, Bertai par 4 mazāk",
                     "Annai 10, Bertai par 4 vairāk",
                     "Annai 6, Bertai 10"], "pareizi": 0,
         "padoms": "B josla īsāka."},
        {"jaut": "Kurš stāsts der?", "zim": majina(13, [(8, None)]),
         "opcijas": ["Kopā 13 bērnu, 8 zēni. Cik meiteņu?",
                     "8 zēni un 13 meitenes. Cik kopā?",
                     "13 zēni, 8 aizgāja"], "pareizi": 0,
         "padoms": "13 ir viss."},
    ]),

    Ievadi("Izrēķini «?»", [
        {"jaut": "Cik ir «?»", "zim": _Z1, "atb": ["6"], "padoms": "10 − 4."},
        {"jaut": "Cik ir «?»", "zim": majina(13, [(8, None)]), "atb": ["5"],
         "padoms": "13 − 8."},
        {"jaut": "Cik ir «?»",
         "zim": sloksnes([("A", 7), ("B", 16, "?")]), "atb": ["16"],
         "padoms": "Saskaiti rūtiņas."},
    ]),

    Petijums("Stāstu kartes", [
        "Paņem kartīti ar zīmējumu.",
        "Izdomā stāstu par savu dzīvi.",
        "Pastāsti klasei - vai zīmējums der?",
    ], vajag="kartītes ar sloksnēm un mājiņām"),

    Pasaule("Stāsts par dzīvniekiem",
            Ievadi("", [
                {"jaut": "Zīmējums: kaķi 5, suņi par 7 vairāk. Cik suņu?",
                 "zim": sloksnes([("kaķi", 5), ("suņi", 12, "?")]),
                 "atb": ["12"], "padoms": "5 + 7."},
            ]),
            pavediens="daba",
            konteksts="Patversmē ir kaķi un suņi.",
            kapec="Zīmējums un stāsts - viens uzdevums divās valodās."),

    Kopsavilkums([
        "Izdomāju stāstu zīmējumam.",
        "Atrodu, kas ir «?».",
        "Pārbaudu, vai stāsts der.",
    ]),

    Majas([
        "Uzzīmē joslas un palūdz mājiniekam izdomāt stāstu.",
        "Izdomā stāstu mājiņai 20: 12 un ?.",
        "Atrisini to.",
    ]),
]
