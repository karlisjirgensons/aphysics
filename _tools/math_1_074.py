# -*- coding: utf-8 -*-
"""1. klase, 74. stunda: «Kā izmērīt, ja objekts garāks par lineālu?»

Garāku priekšmetu mēra pa daļām: liek lineālu, atzīmē galu, pārceļ. Garumu
izsaka decimetros un centimetros: 14 cm = 1 dm 4 cm.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, lineals)

TEMA = "Kā izmērīt, ja objekts garāks par lineālu?"

MERKIS = ("Šodien mērīsim garākus priekšmetus un izteiksim garumu "
          "decimetros un centimetros.")

SATURS = [
    Sakums("14 cm - cik decimetru un centimetru?",
           zimejums=lineals(20, [(0, 14, "14 cm")]),
           paraksts="14 cm = 1 dm 4 cm.",
           fakti=["Pilnos 10 cm saskaita kā decimetrus.",
                  "Atlikušie - centimetri.",
                  "Garu lietu mēra, lineālu pārceļot."]),

    Doma("Pa daļām",
         "Ja lineāls par īsu, atzīmē tā galu un mēri tālāk no atzīmes.",
         soli=[
             "Noliec lineālu no priekšmeta sākuma.",
             "Atzīmē vietu pie 20 cm.",
             "Pārceļ lineālu - 0 pie atzīmes.",
             "Saskaiti: 20 cm + 15 cm = 35 cm = 3 dm 5 cm.",
         ]),

    Ievadi("Pārveido", [
        {"jaut": "14 cm = 1 dm ? cm", "atb": ["4"], "padoms": "14 = 10 + 4."},
        {"jaut": "27 cm = ? dm 7 cm", "atb": ["2"], "padoms": "20 = 2 dm."},
        {"jaut": "3 dm 5 cm = ? cm", "atb": ["35"], "padoms": "30 + 5."},
        {"jaut": "1 dm 9 cm = ? cm", "atb": ["19"], "padoms": "10 + 9."},
        {"jaut": "20 cm + 15 cm = ? cm", "atb": ["35"],
         "padoms": "Divas lineāla daļas."},
    ]),

    Varianti("Kas vienāds?", [
        {"jaut": "Kas ir tas pats, kas 42 cm?",
         "opcijas": ["4 dm 2 cm", "2 dm 4 cm", "42 dm"], "pareizi": 0,
         "padoms": "4 desmiti, 2 vieni."},
        {"jaut": "Kas garāks: 5 dm vai 45 cm?",
         "opcijas": ["5 dm", "45 cm"], "jaukt": False, "pareizi": 0,
         "padoms": "5 dm = 50 cm."},
    ]),

    Petijums("Izmēri solu", [
        "Mēri sola garumu ar 20 cm lineālu.",
        "Katru reizi atzīmē ar zīmuli.",
        "Saskaiti daļas.",
        "Pieraksti dm un cm.",
    ], vajag="lineāls, zīmulis"),

    Pasaule("Aizkaru stienis",
            Ievadi("", [
                {"jaut": "Tētis mēra logu ar 30 cm lineālu: 30 cm, 30 cm un "
                         "vēl 12 cm. Cik cm?", "atb": ["72"],
                 "padoms": "30 + 30 + 12."},
                {"jaut": "Cik tas ir decimetros un centimetros? Cik dm?",
                 "atb": ["7"], "padoms": "72 = 7 dm 2 cm."},
            ]),
            pavediens="maja",
            konteksts="Loga platumu mēra, lai nopirktu stieni.",
            kapec="Pa daļām var izmērīt jebko."),

    Kopsavilkums([
        "Mēru garas lietas pa daļām.",
        "Izsaku garumu dm un cm.",
        "Pārveidoju dm un cm centimetros.",
    ]),

    Majas([
        "Izmēri gultu ar lineālu pa daļām.",
        "Pieraksti rezultātu dm un cm.",
        "Pārbaudi ar mērlenti, ja mājās ir.",
    ]),
]
