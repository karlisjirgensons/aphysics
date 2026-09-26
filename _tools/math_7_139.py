# -*- coding: utf-8 -*-
"""7. klase, 139. stunda: «Kā pārbaudīt sakni?»

Sakni pārbauda, ievietojot to SĀKOTNĒJĀ vienādojumā (ne pēdējā
pārveidojumā - tur kļūda jau var būt «iebūvēta»). Stunda iemāca
pārbaudes pierakstu un to, kā ar to atrast kļūdas vietu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pārbaudīt sakni?"

MERKIS = ("Pārbaudīsim atrisinājumu, ievietojot to sākotnējā "
          "vienādojumā.")

SATURS = [
    Sakums("Pārbaude pēdējā rindā nepalīdz",
           fakti=["Ja kļūda ir 2. solī, x der 3. solim - bet ne sākumam.",
                  "Tāpēc sakni ievieto pirmajā vienādojumā.",
                  "Kreisā puse un labā puse - atsevišķi."]),

    Doma("Pārbaude - sākotnējā vienādojumā",
         "Lai pārbaudītu sakni, to ievieto sākotnējā vienādojumā un atsevišķi "
         "aprēķina kreiso un labo pusi. Ja tās vienādas - sakne pareiza.",
         soli=[
             "Pieraksti: Pārbaude, x = ...",
             "Kreisā puse: aprēķini līdz skaitlim.",
             "Labā puse: aprēķini līdz skaitlim.",
             "Salīdzini: KP = LP.",
         ],
         pieze="Ja KP ≠ LP, pārbaudi katru risinājuma rindu ar šo pašu x - "
               "rinda, kurā vienādība pārstāj būt patiesa, satur kļūdu."),

    Paraugs("Pārbaude",
            uzd="Atrisināja 3(x + 2) − x = 14 un ieguva x = 4. Pārbaudi.",
            soli=[
                ("KP: 3(4 + 2) − 4 = 18 − 4 = 14", "Kreisā puse."),
                ("LP: 14", "Labā puse."),
                ("14 = 14", "Sakrīt."),
            ],
            atbilde="x = 4 ir sakne."),

    Ievadi("Pārbaudi", [
        {"jaut": "5x − 3 = 2x + 9, x = 4. KP = ?",
         "atb": ["17"], "padoms": "20 − 3."},
        {"jaut": "Tai pašai LP = ?",
         "atb": ["17"], "padoms": "8 + 9."},
        {"jaut": "{x + 2|3} = 4, x = 10. Vai sakne pareiza? Raksti «jā» vai "
                 "«nē».",
         "atb": ["jā", "ja"], "padoms": "12 : 3 = 4."},
        {"jaut": "2(x − 1) = x + 5, Toms ieguva x = 6. Vai pareizi?",
         "atb": ["nē", "ne"], "padoms": "KP 10, LP 11."},
    ]),

    Varianti("Atrodi kļūdas vietu", [
        {"jaut": "Toms: 2(x − 1) = x + 5 → 2x − 1 = x + 5 → x = 6. Kurā "
                 "solī kļūda?",
         "opcijas": ["Atverot iekavas: jābūt 2x − 2",
                     "Pārnesot", "Dalot", "Kļūdas nav"],
         "pareizi": 0, "padoms": "2 · 1 = 2."},
        {"jaut": "Kāda ir pareizā sakne?",
         "opcijas": ["7", "6", "5", "3"],
         "pareizi": 0, "padoms": "2x − 2 = x + 5."},
    ]),

    Pasaule("Rēķina kontrole",
            Ievadi("", [
                {"jaut": "Grāmatvedis aprēķināja: 4 datori pa x € un 300 € "
                         "programmas = 3500 €, x = 800. Pārbaudi: KP (€)?",
                 "atb": ["3500"], "padoms": "3200 + 300."},
                {"jaut": "Cits: 3 printeri pa y € un 90 € piegāde = 540 €, "
                         "y = 160. KP (€)?",
                 "atb": ["570"], "padoms": "480 + 90."},
                {"jaut": "Kāda ir pareizā y vērtība?",
                 "atb": ["150"], "padoms": "3y = 450."},
            ]),
            pavediens="dati",
            konteksts="Grāmatvedībā katru aprēķinu pārbauda ar sākotnējiem "
                      "datiem - kļūda maksā naudu.",
            kapec="Pārbaude atklāj kļūdu, kamēr tā vēl ir lēta."),

    Kopsavilkums([
        "Pārbaudu sakni sākotnējā vienādojumā.",
        "Aprēķinu KP un LP atsevišķi.",
        "Atrodu kļūdas vietu ar to pašu skaitli.",
        "Izlaboju un pārbaudu vēlreiz.",
    ]),

    Majas([
        "Atrisini un pārbaudi: 4(x − 3) = 2x + 6.",
        "Atrodi kļūdu savā iepriekšējā darbā ar pārbaudi.",
        "Izdomā risinājumu ar apzinātu kļūdu draugam.",
    ]),
]
