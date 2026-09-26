# -*- coding: utf-8 -*-
"""2. klase, 149. stunda: «Cik kopā maksā pieci vienādi pirkumi?»

Sadzīves uzdevumi ar reizināšanu ar 4 un 5: vienādu preču cena, iepakojumi
pa 4 vai 5. Bieži vajag vēl otru soli - atlikumu no samaksātā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, restis)

TEMA = "Cik kopā maksā pieci vienādi pirkumi?"

MERKIS = ("Šodien risināsim sadzīves uzdevumus, kuros jāreizina ar 4 vai "
          "5.")

_CENAS = restis([["prece", "cena"], ["jogurts", "1 €"], ["maize", "2 €"],
                 ["siers", "4 €"], ["zivs", "5 €"]])

SATURS = [
    Sakums("Cik maksā 5 jogurti un 4 sieri?",
           zimejums=_CENAS,
           paraksts="5 · 1 + 4 · 4 = 5 + 16 = 21 €.",
           fakti=["Vienādus pirkumus reizina.",
                  "Dažādus - saskaita.",
                  "Beigās var aprēķināt atlikumu."]),

    Doma("Pirkumu aprēķins",
         "Katrai precei: skaits · cena. Tad visu saskaita.",
         soli=[
             "Atrodi cenu tabulā.",
             "Reizini ar gabalu skaitu.",
             "Ja preces dažādas - saskaiti.",
             "Atlikums: samaksāts − kopā.",
         ]),

    Paraugs("5 zivis",
            uzd="Zivs maksā 5 €. Cik maksā 5 zivis? Cik atlikums no 50 €?",
            soli=[("5 · 5 = 25 €", "Kopējā cena."),
                  ("50 − 25 = 25 €", "Atlikums.")],
            atbilde="25 € un atlikums 25 €"),

    Ievadi("Rēķini", [
        {"jaut": "4 maizes?", "zim": _CENAS, "atb": ["8"], "mers": "€",
         "padoms": "4 · 2."},
        {"jaut": "7 sieri?", "zim": _CENAS, "atb": ["28"], "mers": "€",
         "padoms": "7 · 4."},
        {"jaut": "9 zivis?", "zim": _CENAS, "atb": ["45"], "mers": "€",
         "padoms": "9 · 5."},
        {"jaut": "5 sieri, samaksā ar 50 €. Atlikums?", "zim": _CENAS,
         "atb": ["30"], "mers": "€", "padoms": "50 − 20."},
        {"jaut": "3 zivis un 4 maizes. Kopā?", "zim": _CENAS, "atb": ["23"],
         "mers": "€", "padoms": "15 + 8."},
        {"jaut": "8 sieri, samaksā ar 40 €. Atlikums?", "zim": _CENAS,
         "atb": ["8"], "mers": "€", "padoms": "40 − 32."},
    ], pamats=4),

    Varianti("Vai pietiks?", [
        {"jaut": "Tev 20 €. Vai pietiks 6 sieriem?", "zim": _CENAS,
         "opcijas": ["Nē, vajag 24 €", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "6 · 4."},
        {"jaut": "Tev 30 €. Vai pietiks 6 zivīm?", "zim": _CENAS,
         "opcijas": ["Jā, tieši 30 €", "Nē"], "jaukt": False, "pareizi": 0,
         "padoms": "6 · 5."},
    ]),

    Pasaule("Iepakojumi pa 4",
            Ievadi("", [
                {"jaut": "Jogurtus pārdod iepakojumā pa 4. Nopirka 5 "
                         "iepakojumus. Cik jogurtu?", "atb": ["20"],
                 "padoms": "5 · 4."},
                {"jaut": "Cik maksā, ja jogurts 1 €?", "zim": _CENAS,
                 "atb": ["20"], "mers": "€", "padoms": "20 · 1."},
            ]),
            pavediens="veikals",
            konteksts="Lielveikalā preces bieži pārdod iepakojumos.",
            kapec="Reizināšana ātri pasaka, cik saņemsi."),

    Kopsavilkums([
        "Aprēķinu vienādu pirkumu cenu ar reizināšanu.",
        "Saskaitu dažādu preču cenas.",
        "Aprēķinu atlikumu.",
    ]),

    Majas([
        "Paskaties uz cenām veikalā vai reklāmā.",
        "Aprēķini, cik maksā 4 vai 5 vienādas preces.",
        "Pārbaudi ar kalkulatoru.",
    ]),
]
