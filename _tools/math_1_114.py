# -*- coding: utf-8 -*-
"""1. klase, 114. stunda: «Kā uzdevumu pārvērst zīmējumā?»

Uzdevumu, kurā salīdzina divus lielumus, uzzīmē ar sloksnēm: katram
lielumam sava josla, abas no viena sākuma. Nezināmo atzīmē ar «?».
Zīmējums pasaka, kura darbība vajadzīga.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Slidnis, Varianti, sloksnes)

TEMA = "Kā uzdevumu pārvērst zīmējumā?"

MERKIS = ("Šodien uzzīmēsim shematisku zīmējumu situācijai, kurā "
          "salīdzināti divi lielumi.")

SATURS = [
    Sakums("Martai 7 zīmuļi, Ilzei par 5 vairāk. Kā to uzzīmēt?",
           zimejums=sloksnes([("Marta", 7), ("Ilze", 12, "?")]),
           paraksts="Ilzes josla - tikpat kā Martai un vēl 5.",
           fakti=["Katram - sava josla.",
                  "Abas sākas vienā vietā.",
                  "Nezināmo atzīmē ar «?»."]),

    Slidnis("Zīmējam soli pa solim", [
        {"v": "1", "teksts": "Martas josla: 7",
         "zim": sloksnes([("Marta", 7)], starpiba=False)},
        {"v": "2", "teksts": "Ilzei - tikpat",
         "zim": sloksnes([("Marta", 7), ("Ilze", 7, "")],
                         starpiba=False)},
        {"v": "3", "teksts": "... un vēl 5. Cik kopā? - ?",
         "zim": sloksnes([("Marta", 7), ("Ilze", 12, "?")])},
    ]),

    Doma("No teksta uz zīmējumu",
         "Zīmējumā redz, kurš ir lielāks un par cik - tad darbību izvēlēties "
         "ir viegli.",
         soli=[
             "Uzzīmē zināmā lieluma joslu.",
             "Uzzīmē otru: garāku vai īsāku.",
             "Atzīmē «?» un starpību.",
             "Izvēlies darbību.",
         ]),

    Ievadi("Nolasi zīmējumu", [
        {"jaut": "Cik zīmuļu Ilzei?",
         "zim": sloksnes([("Marta", 7), ("Ilze", 12, "?")]), "atb": ["12"],
         "padoms": "7 + 5."},
        {"jaut": "Toms 14, Juris par 6 mazāk. Cik Jurim?",
         "zim": sloksnes([("Toms", 14), ("Juris", 8, "?")]), "atb": ["8"],
         "padoms": "14 − 6."},
    ]),

    Varianti("Kurš zīmējums der?", [
        {"jaut": "Anna 9, Ieva par 3 mazāk.",
         "zim": sloksnes([("Anna", 9), ("Ieva", 6, "?")]),
         "opcijas": ["der", "neder"], "jaukt": False, "pareizi": 0,
         "padoms": "Ievas josla īsāka par 3."},
        {"jaut": "Pēteris 5, Kaspars par 4 vairāk.",
         "zim": sloksnes([("Pēteris", 5), ("Kaspars", 3, "?")]),
         "opcijas": ["der", "neder"], "jaukt": False, "pareizi": 1,
         "padoms": "Kasparam jābūt garākam."},
    ]),

    Petijums("Zīmē pats", [
        "Izlasi: «Kaķim 4 kaķēni, sunim par 3 vairāk kucēnu.»",
        "Uzzīmē divas joslas.",
        "Atzīmē «?».",
        "Aprēķini un pārbaudi zīmējumā.",
    ], vajag="rūtiņu burtnīca, krāsu zīmuļi"),

    Pasaule("Burkāni dārzā",
            Ievadi("", [
                {"jaut": "Vienā dobē 11 burkānu, otrā par 4 mazāk. Cik otrā?",
                 "zim": sloksnes([("1. dobe", 11), ("2. dobe", 7, "?")]),
                 "atb": ["7"], "padoms": "11 − 4."},
            ]),
            pavediens="daba",
            konteksts="Skolas dārzā divas burkānu dobes.",
            kapec="Zīmējums parāda, ka otrā dobē ir mazāk."),

    Kopsavilkums([
        "Pārvēršu uzdevumu zīmējumā ar joslām.",
        "Atzīmēju nezināmo ar «?».",
        "No zīmējuma izvēlos darbību.",
    ]),

    Majas([
        "Uzzīmē joslas: tev 7 gadi, mammai par 26 vairāk (bez rēķina).",
        "Uzzīmē uzdevumu par savām rotaļlietām.",
        "Palūdz kādu uzminēt uzdevumu pēc zīmējuma.",
    ]),
]
