# -*- coding: utf-8 -*-
"""1. klase, 92. stunda: «Vai vari izdomāt uzdevumu draugam?»

Skolēns pats izdomā saskaitīšanas uzdevumu pēc nosacījuma (summa 20
apjomā, ar desmita pāriešanu), un draugs to atrisina. Tad autors pārbauda
drauga risinājumu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti)

TEMA = "Vai vari izdomāt uzdevumu draugam?"

MERKIS = ("Šodien izdomāsim saskaitīšanas uzdevumu pēc nosacījuma un "
          "pārbaudīsim drauga risinājumu.")

SATURS = [
    Sakums("Izdomā uzdevumu, kura atbilde ir 14!",
           fakti=["Nosacījums: summa 14, ar pāriešanu.",
                  "Piemēram: 8 + 6, 9 + 5, 7 + 7.",
                  "Uzraksti arī stāstu."]),

    Doma("Labs uzdevums",
         "Labā uzdevumā ir skaidrs jautājums un tieši viena atbilde.",
         soli=[
             "Izvēlies atbildi (piem., 14).",
             "Sadali to divos skaitļos (8 un 6).",
             "Izdomā stāstu un jautājumu.",
             "Pārbaudi drauga atbildi.",
         ]),

    Varianti("Vai der nosacījumam?", [
        {"jaut": "Nosacījums: summa 14, ar pāriešanu. Vai der 9 + 5?",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "9 + 5 = 14, pāri 10."},
        {"jaut": "Vai der 10 + 4?", "opcijas": ["Nē - bez pāriešanas",
                                                "Jā"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Desmits jau gatavs."},
        {"jaut": "Vai der 7 + 6?", "opcijas": ["Nē - summa 13", "Jā"],
         "jaukt": False, "pareizi": 0, "padoms": "7 + 6 = 13."},
    ]),

    Ievadi("Atrisini drauga uzdevumu", [
        {"jaut": "Marta: «Man bija 8 uzlīmes, uzdāvināja 6. Cik tagad?»",
         "atb": ["14"], "padoms": "8 + 6."},
        {"jaut": "Kārlis: «Plauktā 9 grāmatas, ieliku 7. Cik?»",
         "atb": ["16"], "padoms": "9 + 1 + 6."},
        {"jaut": "Ieva: «Dārzā 5 tulpes un 8 narcises. Cik puķu?»",
         "atb": ["13"], "padoms": "8 + 5."},
    ]),

    Petijums("Uzdevumu apmaiņa", [
        "Izvēlies atbildi no 11 līdz 18.",
        "Izdomā stāstu ar saskaitīšanu, kas dod šo atbildi.",
        "Uzraksti uzdevumu uz lapiņas un iedod draugam.",
        "Pārbaudi drauga atbildi un pastāsti, kā risināji tu.",
    ], vajag="lapiņas, zīmulis"),

    Pasaule("Klases avīze",
            Varianti("", [
                {"jaut": "Tavs uzdevums nonāks klases avīzē. Kas tajā "
                         "obligāti jābūt?",
                 "opcijas": ["jautājums", "zīmējums", "tavs vārds"],
                 "pareizi": 0, "padoms": "Bez jautājuma nav ko risināt."},
            ]),
            pavediens="skola",
            konteksts="Klasē veido avīzi ar bērnu uzdevumiem.",
            kapec="Kas izdomā uzdevumu, to saprot vislabāk."),

    Kopsavilkums([
        "Izdomāju uzdevumu pēc nosacījuma.",
        "Uzdodu skaidru jautājumu.",
        "Pārbaudu drauga risinājumu.",
    ]),

    Majas([
        "Izdomā uzdevumu mājiniekam ar atbildi 15.",
        "Pārbaudi, vai viņš atrisināja pareizi.",
        "Palūdz, lai viņš izdomā uzdevumu tev.",
    ]),
]
