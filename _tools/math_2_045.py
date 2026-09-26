# -*- coding: utf-8 -*-
"""2. klase, 45. stunda: «Kurš skaitlis paslēpts?»

Nezināmais darbības loceklis: ? + 25 = 60, 70 − ? = 32. Skaitļa mājiņa rāda
sakarību - ja zināms viss skaitlis un viena daļa, otru daļu atrod ar
atņemšanu; ja zināmas abas daļas - ar saskaitīšanu.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, majina)

TEMA = "Kurš skaitlis paslēpts?"

MERKIS = ("Šodien noteiksim nezināmo darbības locekli vienādībā 100 "
          "apjomā.")

SATURS = [
    Sakums("Zem kartītes paslēpts skaitlis: ? + 25 = 60. Kāds?",
           zimejums=majina(60, [(None, 25)]),
           paraksts="60 ir visa mājiņa, 25 - viena daļa.",
           fakti=["Trūkstošo daļu atrod ar atņemšanu.",
                  "60 − 25 = 35.",
                  "Pārbaude: 35 + 25 = 60."]),

    Doma("Daļa un viss",
         "Ja zini visu un vienu daļu - atņem. Ja zini abas daļas - saskaiti.",
         soli=[
             "? + 25 = 60: nezināma daļa. 60 − 25 = 35.",
             "70 − ? = 32: nezināms, cik atņēma. 70 − 32 = 38.",
             "? − 18 = 40: nezināms viss. 40 + 18 = 58.",
             "Pārbaudi, ieliekot skaitli vietā.",
         ]),

    Slidnis("Viena mājiņa - trīs uzdevumi", [
        {"v": "? + 25 = 60", "teksts": "60 − 25 = 35.",
         "zim": majina(60, [(None, 25)])},
        {"v": "60 − ? = 35", "teksts": "60 − 35 = 25.",
         "zim": majina(60, [(35, None)])},
        {"v": "? − 25 = 35", "teksts": "35 + 25 = 60.",
         "zim": majina(None, [(35, 25)])},
    ]),

    Ievadi("Atrodi paslēpto", [
        {"jaut": "? + 34 = 80", "atb": ["46"], "padoms": "80 − 34."},
        {"jaut": "45 + ? = 72", "atb": ["27"], "padoms": "72 − 45."},
        {"jaut": "90 − ? = 55", "atb": ["35"], "padoms": "90 − 55."},
        {"jaut": "? − 26 = 48", "atb": ["74"], "padoms": "48 + 26."},
        {"jaut": "63 − ? = 29", "atb": ["34"], "padoms": "63 − 29."},
        {"jaut": "? + 58 = 100", "atb": ["42"], "padoms": "100 − 58."},
    ], pamats=4),

    Varianti("Kura darbība?", [
        {"jaut": "Kā atrast ? vienādībā ? − 30 = 45?",
         "opcijas": ["45 + 30", "45 − 30", "30 − 45"], "pareizi": 0,
         "padoms": "Nezināms viss - saskaiti daļas."},
        {"jaut": "Kā atrast ? vienādībā 50 − ? = 12?",
         "opcijas": ["50 − 12", "50 + 12", "12 − 50"], "pareizi": 0,
         "padoms": "Viss mīnus daļa."},
    ]),

    Pasaule("Cik bija sākumā?",
            Ievadi("", [
                {"jaut": "Paciņā bija konfektes. Apēda 16, palika 29. Cik "
                         "bija sākumā?", "atb": ["45"],
                 "padoms": "? − 16 = 29."},
                {"jaut": "Krājkasītē bija 38 €, vecmāmiņa ielika vēl. Tagad "
                         "ir 65 €. Cik ielika?", "atb": ["27"], "mers": "€",
                 "padoms": "38 + ? = 65."},
            ]),
            pavediens="maja",
            konteksts="Dažreiz zinām beigas, bet ne sākumu.",
            kapec="Paslēpto skaitli atrod ar pretējo darbību."),

    Kopsavilkums([
        "Atrodu nezināmu saskaitāmo ar atņemšanu.",
        "Atrodu nezināmu mazināmo ar saskaitīšanu.",
        "Pārbaudu, ieliekot skaitli vienādībā.",
    ]),

    Majas([
        "Paslēp zem monētas vienu skaitli vienādībā un lai mājinieks "
        "atrod.",
        "Tad mājinieks paslēpj - tu atrodi.",
        "Pieraksti 3 uzdevumus ar «?».",
    ]),
]
