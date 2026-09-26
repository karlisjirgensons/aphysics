# -*- coding: utf-8 -*-
"""2. klase, 166. stunda: «Kā uzrakstīt uzdevumu izteiksmei?»

Apgrieztais uzdevums ar reizināšanu un dalīšanu: dota izteiksme (4 · 5,
20 : 4, 3 · 5 + 2), jāizdomā situācija. «·» - vienādas grupas, «:» -
dalīšana vienādās daļās vai pa tik.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti)

TEMA = "Kā uzrakstīt uzdevumu izteiksmei?"

MERKIS = ("Šodien izdomāsim situāciju, kas atbilst dotai izteiksmei ar "
          "reizināšanu vai dalīšanu.")

_DER = ["der", "neder"]

SATURS = [
    Sakums("Kāds stāsts slēpjas aiz 4 · 5?",
           fakti=["4 grozi pa 5 āboliem.",
                  "4 bērni, katram 5 konfektes.",
                  "5 € katrā no 4 dienām."]),

    Doma("Stāsts izteiksmei",
         "«·» - vairākas vienādas grupas; «:» - dalīšana.",
         soli=[
             "4 · 5: izdomā 4 vienādas grupas pa 5.",
             "20 : 4: izdomā, ka 20 dala 4 vienādās daļās.",
             "Vai: 20 dala pa 4 - cik daļu?",
             "Beigās uzdod jautājumu.",
         ]),

    Varianti("Vai stāsts der?", [
        {"jaut": "3 · 6: «3 bērni, katram 6 uzlīmes. Cik kopā?»",
         "opcijas": _DER, "jaukt": False, "pareizi": 0,
         "padoms": "3 grupas pa 6."},
        {"jaut": "3 · 6: «3 zēni un 6 meitenes. Cik kopā?»",
         "opcijas": _DER, "jaukt": False, "pareizi": 1,
         "padoms": "Tas ir 3 + 6."},
        {"jaut": "20 : 4: «20 zīmuļi 4 bērniem vienādi. Cik katram?»",
         "opcijas": _DER, "jaukt": False, "pareizi": 0,
         "padoms": "Dala 4 daļās."},
        {"jaut": "20 : 4: «20 zīmuļi, 4 pazaudēja. Cik palika?»",
         "opcijas": _DER, "jaukt": False, "pareizi": 1,
         "padoms": "Tas ir 20 − 4."},
    ]),

    Ievadi("Izrēķini stāstu", [
        {"jaut": "«3 bērni, katram 6 uzlīmes. Cik kopā?»", "atb": ["18"],
         "padoms": "3 · 6."},
        {"jaut": "«20 zīmuļi 4 bērniem vienādi. Cik katram?»", "atb": ["5"],
         "padoms": "20 : 4."},
        {"jaut": "«3 kastes pa 5 kūkām un vēl 2 kūkas. Cik kūku?»",
         "atb": ["17"], "padoms": "3 · 5 + 2."},
        {"jaut": "«30 € sadala 5 dienām. Cik katrai dienai?»", "atb": ["6"],
         "mers": "€", "padoms": "30 : 5."},
    ]),

    Petijums("Mans stāsts", [
        "Izvēlies izteiksmi: 5 · 4, 24 : 3 vai 2 · 5 + 3.",
        "Uzraksti stāstu ar jautājumu.",
        "Nolasi to klasesbiedram.",
        "Vai viņš uzminēja izteiksmi?",
    ], vajag="burtnīca"),

    Pasaule("Uzdevums klases avīzei",
            Varianti("", [
                {"jaut": "Izteiksme 4 · 3 − 2. Kurš stāsts der?",
                 "opcijas": ["4 galdi pa 3 krēsliem, 2 krēslus aiznesa. "
                             "Cik palika?",
                             "4 krēsli, 3 galdi, 2 bērni.",
                             "4 galdi, pienesa 3 un vēl 2 krēslus."],
                 "pareizi": 0, "padoms": "4 grupas pa 3, tad − 2."},
            ]),
            pavediens="skola",
            konteksts="Klases avīzē ir sadaļa «Atrisini mīklu».",
            kapec="Kas prot izdomāt stāstu, saprot izteiksmi."),

    Kopsavilkums([
        "Izdomāju stāstu izteiksmei ar «·» un «:».",
        "Zinu, kas atbilst reizināšanai un dalīšanai.",
        "Pārbaudu, vai stāsts atbilst izteiksmei.",
    ]),

    Majas([
        "Izdomā stāstu izteiksmei 5 · 3.",
        "Izdomā stāstu izteiksmei 18 : 2.",
        "Nolasi tos mājiniekam.",
    ]),
]
