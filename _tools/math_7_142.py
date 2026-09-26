# -*- coding: utf-8 -*-
"""7. klase, 142. stunda: «Kur proporcija noder?»

Mērogs, receptes, cenas un ātrums - visur, kur lielumi ir tieši
proporcionāli, nezināmo atrod ar proporciju. Stunda iemāca uzrakstīt
proporciju, saglabājot atbilstošo lielumu secību.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kur proporcija noder?"

MERKIS = ("Lietosim proporciju uzdevumos par mērogu, recepti un cenām.")

SATURS = [
    Sakums("Karte 1 : 50 000",
           zimejums=restis([["kartē", "dabā"],
                            ["1 cm", "50 000 cm = 500 m"],
                            ["6 cm", "? m"]]),
           paraksts="1 : 500 = 6 : x ⇒ x = 3000 m.",
           fakti=["Mērogs ir attiecība.",
                  "Proporcija dod attālumu dabā.",
                  "Tā pati metode - receptēm un cenām."]),

    Doma("Tabula → proporcija",
         "Lai uzrakstītu proporciju, lielumus sakārto tabulā: vienā kolonnā - "
         "viena veida lielumi, otrā - otra. Proporciju raksta pa kolonnām "
         "vai pa rindām, bet vienā secībā.",
         soli=[
             "Uzraksti tabulu: zināmais pāris un pāris ar x.",
             "Pārbaudi: vai lielumi ir tieši proporcionāli?",
             "Uzraksti proporciju pēc tabulas.",
             "Atrisini un pārbaudi, vai atbilde ir reāla.",
         ],
         pieze="Mērvienībām abos pāros jābūt vienādām: nevar vienā pusē "
               "grami, otrā - kilogrami."),

    Paraugs("Recepte",
            uzd="Kūkai 4 porcijām vajag 180 g cukura. Cik g vajag 10 "
                "porcijām?",
            soli=[
                ("4 porc. - 180 g; 10 porc. - x g", "Tabula."),
                ("4 : 180 = 10 : x", "Proporcija."),
                ("4x = 1800, x = 450", "Atrisina."),
            ],
            atbilde="450 g"),

    Ievadi("Aprēķini", [
        {"jaut": "Mērogs 1 : 50 000. Kartē 6 cm. Cik km dabā?",
         "atb": ["3"], "padoms": "300 000 cm = 3 km."},
        {"jaut": "3 kg ābolu maksā 4,50 €. Cik € par 5 kg?",
         "atb": ["7,5"], "padoms": "3 : 4,5 = 5 : x."},
        {"jaut": "Auto 100 km patērē 6 l. Cik l 350 km?",
         "atb": ["21"], "padoms": "100 : 6 = 350 : x."},
        {"jaut": "Mērogs 1 : 200. Istaba 5 m. Cik cm plānā?",
         "atb": ["2,5"], "padoms": "500 : 200."},
    ]),

    Varianti("Pareizā proporcija", [
        {"jaut": "5 klades maksā 3 €. Cik maksā 8? Kura proporcija?",
         "opcijas": ["5 : 3 = 8 : x", "5 : 8 = x : 3", "3 : 5 = 8 : x",
                     "5 : x = 3 : 8"],
         "pareizi": 0, "padoms": "Klades : € = klades : €."},
        {"jaut": "Kurā situācijā proporcija NEder?",
         "opcijas": ["Vecums un augums",
                     "Litri un cena", "Porcijas un milti",
                     "Kartes cm un dabas km"],
         "pareizi": 0, "padoms": "Nav tieši proporcionāli."},
    ]),

    Pasaule("Zīmēšana mērogā",
            Ievadi("", [
                {"jaut": "Futbola laukums 105 m × 68 m. Plānā mērogā "
                         "1 : 1000. Garums plānā (cm)?",
                 "atb": ["10,5"], "padoms": "10 500 cm : 1000."},
                {"jaut": "Platums plānā (cm)?",
                 "atb": ["6,8"], "padoms": "6800 : 1000."},
                {"jaut": "Plānā vārti 0,73 cm. Cik m dabā?",
                 "atb": ["7,3"], "padoms": "0,73 · 1000 cm."},
            ]),
            pavediens="sports",
            konteksts="Treneri zīmē taktiku uz laukuma plāna mērogā - "
                      "visi attālumi proporcionāli.",
            kapec="Mērogs = proporcija."),

    Kopsavilkums([
        "Sakārtoju lielumus tabulā.",
        "Uzrakstu proporciju vienā secībā.",
        "Lietoju proporciju mērogam, receptēm un cenām.",
        "Pārbaudu mērvienības.",
    ]),

    Majas([
        "Izmēri kartē attālumu līdz tuvākajai pilsētai un pārrēķini.",
        "Pārrēķini recepti ģimenei ar 6 cilvēkiem.",
        "Uzzīmē savu istabu mērogā 1 : 50.",
    ]),
]
