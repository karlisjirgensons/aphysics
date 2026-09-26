# -*- coding: utf-8 -*-
"""7. klase, 73. stunda: «Kurš maršruts ir īsāks?»

Trijstūra nevienādība ikdienā nozīmē: taisns ceļš vienmēr ir īsāks par
apkārtceļu caur trešo punktu. Stunda to lieto kartēs, piegādēs un
pamato secinājumu ar nevienādību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, geometrija)

TEMA = "Kurš maršruts ir īsāks?"

MERKIS = ("Lietosim trijstūra nevienādību reālā kontekstā un pamatosim "
          "secinājumu.")

_KARTE = geometrija([("M", 0, 0), ("S", 8, 0), ("V", 3, 4)],
                    nogriezni=["MS"], izcelti=["MV", "VS"],
                    malas=[("MS", "2,4 km"), ("MV", "1,5 km"),
                           ("VS", "1,8 km")])

SATURS = [
    Sakums("Uz skolu - taisni vai caur veikalu?",
           zimejums=_KARTE,
           paraksts="M - mājas, S - skola, V - veikals.",
           fakti=["Taisni: 2,4 km.",
                  "Caur veikalu: 1,5 + 1,8 = 3,3 km.",
                  "Apkārtceļš ir garāks - vienmēr."]),

    Doma("Taisns ceļš ir īsākais",
         "Attālums starp diviem punktiem vienmēr ir mazāks par ceļu caur "
         "trešo punktu, ja tas nav uz nogriežņa: MS < MV + VS. Tā ir "
         "trijstūra nevienādība.",
         soli=[
             "Uzzīmē trīs punktus un savieno tos.",
             "Uzraksti nevienādību garākajam «tiešajam» ceļam.",
             "Aprēķini starpību - cik garāks ir apkārtceļš.",
             "Pamato secinājumu ar nevienādību.",
         ],
         pieze="Vienādība MS = MV + VS ir tikai tad, ja V atrodas uz "
               "nogriežņa MS - tad apkārtceļa nav."),

    Paraugs("Pamato",
            uzd="No Rīgas līdz Jelgavai 42 km, no Jelgavas līdz Bauskai "
                "40 km. Vai no Rīgas līdz Bauskai taisnā līnijā var būt 90 "
                "km?",
            soli=[
                ("RB < RJ + JB", "Trijstūra nevienādība."),
                ("RB < 42 + 40 = 82 (km)", "Ievieto."),
                ("90 > 82", "Neiespējami."),
            ],
            atbilde="Nē - taisnā līnijā mazāk par 82 km (patiesībā ~60 km)."),

    Ievadi("Aprēķini", [
        {"jaut": "Sākuma kartē: par cik km garāks ceļš caur veikalu?",
         "atb": ["0,9"], "padoms": "3,3 − 2,4."},
        {"jaut": "Attālums A-B 5 km, B-C 3 km. Lielākais iespējamais A-C "
                 "(km)?",
         "atb": ["8"], "padoms": "Ja B ir uz AC."},
        {"jaut": "Attālums A-B 5 km, B-C 3 km. Mazākais iespējamais A-C?",
         "atb": ["2"], "padoms": "Ja C ir uz AB."},
        {"jaut": "Kurjers: noliktava-klients 6 km. Pa ceļam uz degvielas "
                 "staciju: 4 + 3 km. Cik km lieki?",
         "atb": ["1"], "padoms": "7 − 6."},
    ]),

    Varianti("Pamato secinājumu", [
        {"jaut": "Navigācija rāda 12 km ceļu, bet taisnā līnijā ir 8 km. "
                 "Kāpēc?",
         "opcijas": ["Ceļi nav taisni - tie iet apkārt",
                     "Navigācija kļūdās",
                     "Taisnā līnija ir garāka",
                     "Tas nav iespējams"],
         "pareizi": 0,
         "padoms": "Apkārtceļš ir garāks."},
        {"jaut": "Vai ceļš caur trešo punktu var būt īsāks par taisno?",
         "opcijas": ["Nē, nekad", "Jā, ja ceļš ir labs",
                     "Jā, naktī", "Tikai laivā"],
         "pareizi": 0,
         "padoms": "Nevienādība."},
        {"jaut": "Kad ceļš caur V ir tieši tikpat garš kā taisni?",
         "opcijas": ["Ja V ir uz nogriežņa MS",
                     "Ja V ir tālu", "Nekad", "Vienmēr"],
         "pareizi": 0,
         "padoms": "Tad trijstūris saplok."},
    ]),

    Pasaule("Glābšanas laiva",
            Ievadi("", [
                {"jaut": "Cilvēks ūdenī ir 30 m no krasta, 40 m pa labi no "
                         "glābēja. Taisni līdz viņam - 50 m. Ceļš «40 m gar "
                         "krastu, tad 30 m peldus» - cik m kopā?",
                 "atb": ["70"], "padoms": "40 + 30 > 50, kā jābūt."},
                {"jaut": "Peldot taisni 50 m ar 1 m/s - cik s?",
                 "atb": ["50"], "padoms": "50 : 1."},
                {"jaut": "Skrienot 40 m ar 5 m/s un peldot 30 m ar 1 m/s - "
                         "cik s?",
                 "atb": ["38"], "padoms": "8 + 30."},
            ]),
            pavediens="sports",
            konteksts="Glābēji zina: īsākais ceļš ne vienmēr ir ātrākais, ja "
                      "ātrumi atšķiras.",
            kapec="Nevienādība - par garumu, nevis laiku."),

    Kopsavilkums([
        "Lietoju trijstūra nevienādību maršrutiem.",
        "Pamatoju, ka taisns ceļš ir īsākais.",
        "Novērtēju attāluma robežas.",
        "Atšķiru īsāko ceļu no ātrākā.",
    ]),

    Majas([
        "Kartē salīdzini taisno un ceļa attālumu līdz 3 vietām.",
        "Pamato, ka triju pilsētu attālumi 10, 20 un 40 km nav iespējami.",
        "Izdomā maršruta uzdevumu savai apkaimei.",
    ]),
]
