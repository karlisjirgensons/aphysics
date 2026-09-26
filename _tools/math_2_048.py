# -*- coding: utf-8 -*-
"""2. klase, 48. stunda: «Kā uzdevumu pārvērst zīmējumā?»

Shematisks zīmējums - divas sloksnes vai «visa un daļas» josla - parāda,
kura darbība vajadzīga, pirms vēl kaut ko rēķina. Tas ir pirmais solis
teksta uzdevumu risināšanā, ko lietos līdz 9. klasei.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, restis, sloksnes)

TEMA = "Kā uzdevumu pārvērst zīmējumā?"

MERKIS = ("Šodien veidosim shematisku zīmējumu situācijai ar saskaitīšanu "
          "vai atņemšanu 100 apjomā.")

SATURS = [
    Sakums("Kā zīmējums palīdz izvēlēties darbību?",
           zimejums=sloksnes([("Anna", 12, "34"), ("Jānis", 8, "?")]),
           paraksts="Jānim ir par 13 mazāk nekā Annai.",
           fakti=["Garāka sloksne - vairāk.",
                  "Iekrāsotā daļa - par cik vairāk.",
                  "Zīmējumā redz, ka jāatņem: 34 − 13."]),

    Doma("Zīmē, tad rēķini",
         "Katru lielumu attēlo ar sloksni un atzīmē, kas zināms un kas nav.",
         soli=[
             "Izlasi un atrodi, ko jautā.",
             "Uzzīmē sloksni katram lielumam.",
             "Uzraksti zināmos skaitļus un «?».",
             "Pēc zīmējuma izvēlies darbību.",
         ]),

    Slidnis("Divi zīmējumu veidi", [
        {"v": "visa un daļas",
         "teksts": "Klasē 28 bērni, 13 zēni. Cik meiteņu? 28 − 13.",
         "zim": restis([["13 zēni", "? meitenes"], ["28 bērni", ""]])},
        {"v": "salīdzināšana",
         "teksts": "Annai 34, Jānim par 13 mazāk. 34 − 13.",
         "zim": sloksnes([("Anna", 12, "34"), ("Jānis", 8, "?")])},
    ]),

    Varianti("Kura darbība?", [
        {"jaut": "Plauktā 45 grāmatas, 18 paņēma. Cik palika?",
         "opcijas": ["45 − 18", "45 + 18"], "jaukt": False, "pareizi": 0,
         "padoms": "Paņēma - kļūst mazāk."},
        {"jaut": "Zēniem 27 bumbas, meitenēm par 9 vairāk. Cik meitenēm?",
         "opcijas": ["27 + 9", "27 − 9"], "jaukt": False, "pareizi": 0,
         "padoms": "Vairāk - garāka sloksne."},
        {"jaut": "Mārītei 52 uzlīmes, tas ir par 15 vairāk nekā Artim. Cik "
                 "Artim?", "opcijas": ["52 − 15", "52 + 15"],
         "jaukt": False, "pareizi": 0,
         "padoms": "Uzzīmē: Mārītes sloksne garāka."},
        {"jaut": "Sarkanas 36 rozes, baltas 29. Cik kopā?",
         "opcijas": ["36 + 29", "36 − 29"], "jaukt": False, "pareizi": 0,
         "padoms": "Visa = daļa + daļa."},
    ]),

    Ievadi("Uzzīmē un izrēķini", [
        {"jaut": "Plauktā 45 grāmatas, 18 paņēma. Cik palika?",
         "atb": ["27"], "padoms": "45 − 18."},
        {"jaut": "Zēniem 27 bumbas, meitenēm par 9 vairāk. Cik meitenēm?",
         "atb": ["36"], "padoms": "27 + 9."},
        {"jaut": "Mārītei 52 uzlīmes - par 15 vairāk nekā Artim. Cik "
                 "Artim?", "atb": ["37"], "padoms": "52 − 15."},
        {"jaut": "Sarkanas 36 rozes, baltas 29. Cik kopā?", "atb": ["65"],
         "padoms": "36 + 29."},
    ]),

    Pasaule("Cik ābolu savāca?",
            Ievadi("", [
                {"jaut": "Tētis savāca 48 ābolus, tu - par 19 mazāk. Cik tu?",
                 "atb": ["29"], "padoms": "Tava sloksne īsāka: 48 − 19."},
                {"jaut": "Cik abi kopā?", "atb": ["77"],
                 "padoms": "48 + 29."},
            ]),
            pavediens="daba",
            konteksts="Rudenī dārzā vāc ābolus.",
            kapec="Zīmējums pasaka, ka jāatņem, nevis jāsaskaita."),

    Kopsavilkums([
        "Uzzīmēju situāciju ar sloksnēm.",
        "Atzīmēju, kas zināms un kas nav.",
        "Pēc zīmējuma izvēlos darbību.",
    ]),

    Majas([
        "Izdomā uzdevumu par sevi un brāli vai draugu.",
        "Uzzīmē to ar sloksnēm.",
        "Lai mājinieks pēc zīmējuma pasaka darbību.",
    ]),
]
