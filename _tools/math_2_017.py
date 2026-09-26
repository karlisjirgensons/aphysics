# -*- coding: utf-8 -*-
"""2. klase, 17. stunda: «Kā izmērīt to, kas nav taisns?»

Lineāls ir taisns, bet upe uz kartes vai čūskas ceļš - līkumains. Tādu
garumu mēra netieši: pārliek pa līkni auklu, iztaisno to un izmēra ar
lineālu. Lauztai līnijai garums ir visu posmu summa.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, linijas)

TEMA = "Kā izmērīt to, kas nav taisns?"

MERKIS = ("Šodien izmērīsim līklīnijas garumu ar auklu un lauztas līnijas "
          "garumu, saskaitot tās posmus.")

_LAUZTA = linijas([(0, 0, 3, 3), (3, 3, 7, 3), (7, 3, 9, 0)],
                  uzraksti=[(1.1, 2, "4 cm"), (5, 3.8, "4 cm"),
                            (8.8, 2, "4 cm")],
                  punkti=[(0, 0), (3, 3), (7, 3), (9, 0)], platums=10,
                  augstums=4)

SATURS = [
    Sakums("Cik gara ir Daugava uz kartes, ja tā visu laiku līkumo?",
           fakti=["Līkni ar lineālu nevar izmērīt uzreiz.",
                  "Pa līkni noliek auklu, tad to iztaisno.",
                  "Iztaisnotu auklu izmēra ar lineālu."]),

    Doma("Mēra netieši",
         "Līkumainu līniju pārvērš taisnā un tad izmēra.",
         soli=[
             "Noliec auklu precīzi pa visu līniju.",
             "Atzīmē vietu, kur līnija beidzas.",
             "Iztaisno auklu gar lineālu.",
             "Nolasi garumu līdz atzīmei.",
         ],
         pieze="Lauztai līnijai aukla nav vajadzīga - izmēri katru posmu un "
               "saskaiti."),

    Ievadi("Lauztas līnijas garums", [
        {"jaut": "Cik gara ir visa lauztā līnija?", "zim": _LAUZTA,
         "atb": ["12"], "mers": "cm", "padoms": "4 + 4 + 4."},
        {"jaut": "Lauztai līnijai ir posmi 5 cm, 2 cm un 6 cm. Cik gara "
                 "ir visa līnija?", "atb": ["13"], "mers": "cm",
         "padoms": "5 + 2 + 6."},
        {"jaut": "Posmi 10 cm, 10 cm un 7 cm. Cik gara ir līnija?",
         "atb": ["27"], "mers": "cm", "padoms": "10 + 10 + 7."},
        {"jaut": "Aukla pa līkni bija 34 cm. Otrā līkne par 8 cm garāka. "
                 "Cik gara otrā?", "atb": ["42"], "mers": "cm",
         "padoms": "34 + 8."},
    ]),

    Varianti("Kā mērīt?", [
        {"jaut": "Kā izmērīt pudeles apkārtmēru?",
         "opcijas": ["Apliek auklu vai mērlenti apkārt",
                     "Ar taisnu lineālu", "Tas nav iespējams"],
         "pareizi": 0, "padoms": "Vajag kaut ko, kas liecas."},
        {"jaut": "Kura līnija ir garāka - taisna no A līdz B vai līkumaina "
                 "no A līdz B?",
         "opcijas": ["līkumainā", "taisnā", "vienādas"], "pareizi": 0,
         "padoms": "Taisnā ir īsākais ceļš."},
    ]),

    Petijums("Izmēri līkni", [
        "Uzzīmē uz lapas līkumainu upi.",
        "Pirms mērīšanas uzmini, cik tā gara.",
        "Noliec pa to auklu un atzīmē galu.",
        "Iztaisno auklu un izmēri. Cik tuvu bija tavs minējums?",
    ], vajag="aukla vai diegs, lineāls, flomāsteris"),

    Pasaule("Cik tāls ceļš uz parku?",
            Ievadi("", [
                {"jaut": "Ceļš uz parku: 30 m līdz krustojumam, 25 m gar "
                         "veikalu, 40 m līdz vārtiem. Cik tas ir kopā?",
                 "atb": ["95"], "mers": "m", "padoms": "30 + 25 + 40."},
                {"jaut": "Taisni pāri laukumam būtu 60 m. Par cik īsāks ir "
                         "šis ceļš?", "atb": ["35"], "mers": "m",
                 "padoms": "95 − 60."},
            ]),
            pavediens="celojums",
            konteksts="Pa ielām ceļš ir lauzta līnija - ar pagriezieniem.",
            kapec="Ceļš pa līkumiem vienmēr ir garāks par taisnu."),

    Kopsavilkums([
        "Mēru līklīniju ar auklu un lineālu.",
        "Aprēķinu lauztas līnijas garumu kā posmu summu.",
        "Zinu, ka taisna līnija ir īsākais ceļš.",
    ]),

    Majas([
        "Ar diegu izmēri krūzes apkārtmēru.",
        "Ar diegu izmēri sava pirksta apkārtmēru.",
        "Kurš ir garāks - krūzes apkārtmērs vai tās augstums?",
    ]),
]
