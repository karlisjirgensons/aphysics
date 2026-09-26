# -*- coding: utf-8 -*-
"""1. klase, 113. stunda: «Kā sakārtot pēc lieluma?»

Otrreiz par kārtošanu (pirmoreiz 66. stundā) - tagad ar lielumiem un
«par cik»: sakārto augošā/dilstošā secībā un pamato ar starpībām.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, kolonnas)

TEMA = "Kā sakārtot pēc lieluma?"

MERKIS = ("Šodien sakārtosim lielumus augošā un dilstošā secībā un "
          "pamatosim kārtību.")

_AUGI = kolonnas([("tulpe", 14), ("roze", 19), ("margrietiņa", 8),
                  ("saulgrieze", 20)], " cm")

SATURS = [
    Sakums("Kurš zieds visgarākais? Sakārto!",
           zimejums=_AUGI,
           paraksts="8 cm, 14 cm, 19 cm, 20 cm - augošā secībā.",
           fakti=["Augošā - no mazākā uz lielāko.",
                  "Dilstošā - no lielākā uz mazāko.",
                  "Pamato: katrs nākamais par tik lielāks."]),

    Doma("Kārto un pamato",
         "Katru reizi paņem mazāko no atlikušajiem - un pasaki, par cik "
         "nākamais lielāks.",
         soli=[
             "Atrodi mazāko: 8 cm.",
             "Nākamais: 14 cm - par 6 cm lielāks.",
             "Turpini, līdz visi sakārtoti.",
         ]),

    Ievadi("Nolasi un sakārto", [
        {"jaut": "Kurš augs ir pirmais augošā secībā? Cik cm?",
         "zim": _AUGI, "atb": ["8"], "padoms": "Mazākais."},
        {"jaut": "Kurš ir trešais augošā secībā? Cik cm?", "zim": _AUGI,
         "atb": ["19"], "padoms": "8, 14, ..."},
        {"jaut": "Par cik cm saulgrieze garāka nekā tulpe?", "zim": _AUGI,
         "atb": ["6"], "padoms": "20 − 14."},
        {"jaut": "Dilstošā secībā - pēdējais? Cik cm?", "zim": _AUGI,
         "atb": ["8"], "padoms": "Mazākais pēdējais."},
    ]),

    Varianti("Vai pareizi sakārtots?", [
        {"jaut": "Augošā: 5, 9, 7, 12",
         "opcijas": ["Nē", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "7 < 9."},
        {"jaut": "Dilstošā: 18, 15, 11, 3",
         "opcijas": ["Jā", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "Katrs mazāks."},
    ]),

    Pasaule("Lēkšana tālumā",
            Ievadi("", [
                {"jaut": "Lēcieni: Ēriks 12 pēdas, Rasa 15, Kārlis 9. Kurš "
                         "uzvarēja? (pēdas)", "atb": ["15"],
                 "padoms": "Lielākais."},
                {"jaut": "Par cik uzvarētājs pārspēja otro vietu?",
                 "atb": ["3"], "padoms": "15 − 12."},
            ]),
            pavediens="sports",
            konteksts="Sporta stundā mēra lēcienu garumu pēdās.",
            kapec="Kārtošana nosaka vietas sacensībās."),

    Kopsavilkums([
        "Kārtoju lielumus augošā un dilstošā secībā.",
        "Pamatoju ar starpībām.",
        "Nolasu datus no diagrammas.",
    ]),

    Majas([
        "Sakārto 4 ģimenes locekļus pēc auguma.",
        "Par cik garākais pārspēj īsāko?",
        "Uzzīmē stabiņu diagrammu.",
    ]),
]
