# -*- coding: utf-8 -*-
"""9. klase, 110. stunda: «Kad sistēmai nav atrisinājuma?»

Divas taisnes var krustoties (1 atrisinājums), būt paralēlas (0) vai
sakrist (bezgalīgi daudz). To redz jau no slīpumiem: dažādi k - krustojas,
vienādi k un dažādi b - paralēlas, viss vienāds - sakrīt.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Slidnis, Varianti, plakne, restis)

TEMA = "Kad sistēmai nav atrisinājuma?"

MERKIS = ("Analizēsim gadījumus, kad taisnes ir paralēlas vai sakrīt.")

_PLAKNE = dict(no_x=-2, lidz_x=6, no_y=-3, lidz_y=7)

SATURS = [
    Sakums("Divi vilcieni uz paralēlām sliedēm",
           zimejums=plakne(grafiki=[(1, 2, "y = x + 2"),
                                    (1, -1, "y = x − 1")], **_PLAKNE),
           paraksts="Vienāds slīpums, dažāds sākums - nekad nesatiksies.",
           fakti=["Paralēlām taisnēm kopīgu punktu nav.",
                  "Sistēmai nav atrisinājuma.",
                  "Pazīme: vienāds k, dažāds b."]),

    Slidnis("Trīs iespējas", [
        {"v": "1", "teksts": "Dažādi slīpumi - krustojas: viens atrisinājums",
         "zim": plakne(grafiki=[(1, 2, "y = x + 2"), (-1, 4, "y = −x + 4")],
                       punkti=[(1, 3, "(1; 3)")], **_PLAKNE)},
        {"v": "0", "teksts": "Vienāds k, dažāds b - paralēlas: nav "
                             "atrisinājuma",
         "zim": plakne(grafiki=[(1, 2, "y = x + 2"), (1, -1, "y = x − 1")],
                       **_PLAKNE)},
        {"v": "∞", "teksts": "Vienāds k un b - sakrīt: bezgalīgi daudz",
         "zim": plakne(grafiki=[(1, 2, "y = x + 2 un 2y = 2x + 4")],
                       **_PLAKNE)},
    ]),

    Doma("Atrisinājumu skaits",
         "Izsaki abos y = kx + b un salīdzini: k dažādi - 1 atrisinājums; k "
         "vienādi, b dažādi - 0; k un b vienādi - bezgalīgi daudz.",
         soli=[
             "Pārveido abus vienādojumus formā y = kx + b.",
             "Salīdzini slīpumus k.",
             "Ja k vienādi - salīdzini b.",
             "Analītiski: 0 = 5 nozīmē «nav», 0 = 0 - «bezgalīgi».",
         ]),

    Varianti("Cik atrisinājumu?", [
        {"jaut": "y = 3x + 1 un y = 3x − 2",
         "opcijas": ["0", "1", "bezgalīgi daudz", "2"],
         "pareizi": 0, "padoms": "Paralēlas."},
        {"jaut": "y = 2x un y = −2x",
         "opcijas": ["1", "0", "bezgalīgi daudz", "2"],
         "pareizi": 0, "padoms": "Dažādi slīpumi."},
        {"jaut": "x + y = 3 un 2x + 2y = 6",
         "opcijas": ["bezgalīgi daudz", "0", "1", "2"],
         "pareizi": 0, "padoms": "Otrais = pirmais · 2."},
        {"jaut": "x + y = 3 un x + y = 5",
         "opcijas": ["0", "1", "bezgalīgi daudz", "2"],
         "pareizi": 0, "padoms": "Summa nevar būt gan 3, gan 5."},
    ]),

    Ievadi("Izvēlies parametru", [
        {"jaut": "y = 4x + 1 un y = kx + 7 ir paralēlas. k = ?", "atb": ["4"],
         "padoms": "Vienādi slīpumi."},
        {"jaut": "y = 2x + b un y = 2x + 5 sakrīt. b = ?", "atb": ["5"],
         "padoms": "Viss vienāds."},
        {"jaut": "x + 2y = 4 un 3x + 6y = c: bezgalīgi daudz. c = ?",
         "atb": ["12"], "padoms": "Reizināts ar 3."},
    ]),

    Pasaule("Divi krājkonti",
            Ievadi("", [
                {"jaut": "Anna ir sakrājusi 50 € un katru mēnesi krāj 20 €; "
                         "Juris ir sakrājis 30 € un krāj 20 €. Cik € ir "
                         "starpība pēc 10 mēnešiem?", "atb": ["20"],
                 "padoms": "Starpība visu laiku 20 € - taisnes paralēlas."},
                {"jaut": "Cik € mēnesī Jurim jākrāj, lai pēc 10 mēnešiem "
                         "summas būtu vienādas?", "atb": ["22"],
                 "padoms": "30 + 10x = 50 + 200."},
            ]),
            pavediens="veikals",
            konteksts="Ja abi krāj vienādi, tas, kuram sākumā ir mazāk, nekad "
                      "nepanāks otru.",
            kapec="Vienāds slīpums - nav krustpunkta.",
            zimejums=restis([["mēnesis", "0", "5", "10"],
                             ["Anna", "50", "150", "250"],
                             ["Juris", "30", "130", "230"]])),

    Kopsavilkums([
        "Nosaku atrisinājumu skaitu pēc slīpumiem.",
        "Atpazīstu paralēlas un sakrītošas taisnes.",
        "Saprotu «0 = 5» un «0 = 0» nozīmi.",
    ]),

    Majas([
        "Nosaki atrisinājumu skaitu: 2x − y = 1 un 4x − 2y = 3.",
        "Izdomā sistēmu ar bezgalīgi daudz atrisinājumiem.",
        "Uzzīmē visus trīs gadījumus vienā lapā.",
    ]),
]
