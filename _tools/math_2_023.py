# -*- coding: utf-8 -*-
"""2. klase, 23. stunda: «Cik kopā un par cik garāks?»

Ar garumiem rēķina tāpat kā ar skaitļiem, tikai mērvienība iet līdzi: 30 cm
+ 25 cm = 55 cm. Jautājums «par cik garāks?» ir atņemšana. Sloksnes zīmējums
parāda, kura darbība vajadzīga.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, sloksnes)

TEMA = "Cik kopā un par cik garāks?"

MERKIS = ("Šodien saskaitīsim un atņemsim garumus vienās mērvienībās un "
          "noteiksim, par cik viens objekts ir garāks.")

SATURS = [
    Sakums("Cik garš ir rotaļu vilciens - lokomotīve un vagons kopā?",
           zimejums=sloksnes([("lokomotīve", 18, "18 cm"),
                              ("vagons", 15, "15 cm")]),
           fakti=["Kopējais garums ir visu daļu summa.",
                  "«Par cik garāks» - atņem mazāko no lielākā.",
                  "Mērvienība paliek: cm + cm = cm."]),

    Doma("Garumu darbības",
         "Saskaita un atņem tikai garumus vienā mērvienībā.",
         soli=[
             "«Cik kopā?» - saskaiti.",
             "«Par cik garāks / īsāks?» - atņem.",
             "Pārbaudi, vai abi garumi ir vienā mērvienībā.",
             "Atbildē uzraksti mērvienību.",
         ]),

    Paraugs("Par cik garāks?",
            uzd="Zīmulis ir 17 cm, pildspalva - 14 cm. Par cik zīmulis "
                "garāks?",
            soli=[("17 cm − 14 cm = 3 cm", "Atņem īsāko no garākā.")],
            atbilde="par 3 cm"),

    Ievadi("Rēķini ar garumiem", [
        {"jaut": "35 cm + 20 cm = ?", "atb": ["55"], "mers": "cm",
         "padoms": "35 + 20."},
        {"jaut": "Lente 60 cm, nogrieza 25 cm. Cik palika?", "atb": ["35"],
         "mers": "cm", "padoms": "60 − 25."},
        {"jaut": "Galds 80 cm, krēsls 45 cm augsts. Par cik galds augstāks?",
         "atb": ["35"], "mers": "cm", "padoms": "80 − 45."},
        {"jaut": "Divas sloksnes: 24 cm un 38 cm. Cik garas kopā?",
         "atb": ["62"], "mers": "cm", "padoms": "24 + 38."},
        {"jaut": "Grāmata 26 cm, burtnīca par 5 cm īsāka. Cik gara "
                 "burtnīca?", "atb": ["21"], "mers": "cm",
         "padoms": "Īsāka - atņem."},
        {"jaut": "Upe 7 m plata, tilts par 3 m garāks. Cik garš tilts?",
         "atb": ["10"], "mers": "m", "padoms": "Garāks - pieskaiti."},
    ], pamats=4),

    Varianti("Kura darbība?", [
        {"jaut": "Sloksne bija 50 cm, to pagarināja par 10 cm. Cik gara?",
         "opcijas": ["50 + 10", "50 − 10"], "jaukt": False, "pareizi": 0,
         "padoms": "Pagarināja - kļuva garāka."},
        {"jaut": "Anna ir 1 m 28 cm, brālis 1 m 20 cm. Par cik Anna garāka?",
         "opcijas": ["28 − 20", "28 + 20"], "jaukt": False, "pareizi": 0,
         "padoms": "Par cik - atņem."},
    ]),

    Pasaule("Cik garš būs vilciens?",
            Ievadi("", [
                {"jaut": "Rotaļu lokomotīve ir 18 cm, vagons - 15 cm. Cik "
                         "gara lokomotīve ar vienu vagonu?", "atb": ["33"],
                 "mers": "cm", "padoms": "18 + 15."},
                {"jaut": "Pievieno vēl vienu vagonu. Cik garš vilciens?",
                 "atb": ["48"], "mers": "cm", "padoms": "33 + 15."},
                {"jaut": "Plaukts ir 60 cm. Par cik cm plaukts garāks nekā "
                         "vilciens?", "atb": ["12"], "mers": "cm",
                 "padoms": "60 − 48."},
            ]),
            pavediens="tehnika",
            konteksts="Rotaļu vilcienu grib nolikt plauktā.",
            kapec="Pirms pirkt vēl vagonu, der aprēķināt, vai ietilps."),

    Kopsavilkums([
        "Saskaitu garumus vienā mērvienībā.",
        "Atņemot atrodu, par cik viens garāks.",
        "Atbildē rakstu mērvienību.",
    ]),

    Majas([
        "Izmēri divas karotes un saskaiti to garumus.",
        "Par cik viena garāka nekā otra?",
        "Izdomā vienu uzdevumu mājiniekam.",
    ]),
]
