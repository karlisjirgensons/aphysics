# -*- coding: utf-8 -*-
"""7. klase, 64. stunda: «Funkcija aug vai dilst?»

Lineāra funkcija ir augoša, ja k > 0 (grafiks kāpj uz augšu no kreisās uz
labo), un dilstoša, ja k < 0. Ja k = 0 - funkcija ir konstanta. Stunda to
atklāj ar grafikiem un saista ar dzīves procesiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Slidnis, Varianti, plakne)

TEMA = "Funkcija aug vai dilst?"

MERKIS = ("Noteiksim, vai funkcija ir augoša vai dilstoša, un saistīsim to "
          "ar koeficientu k.")


def _k(k, uzr):
    return plakne(grafiki=[(k, 1, uzr)], no_x=-4, lidz_x=4, no_y=-4,
                  lidz_y=5, solis=1)


SATURS = [
    Sakums("Kalnā vai lejā?",
           zimejums=plakne(grafiki=[(1, 0, "augoša"), (-1, 0, "dilstoša")],
                           no_x=-4, lidz_x=4, no_y=-4, lidz_y=4, solis=1),
           paraksts="Lasa no kreisās uz labo - kā tekstu.",
           fakti=["Augoša: jo lielāks x, jo lielāks y.",
                  "Dilstoša: jo lielāks x, jo mazāks y."]),

    Doma("k nosaka virzienu",
         "Lineāra funkcija y = kx + b ir augoša, ja k > 0, un dilstoša, ja "
         "k < 0. Ja k = 0, funkcija ir konstanta.",
         soli=[
             "Atrodi k - skaitli pie x.",
             "k > 0: argumentam pieaugot, vērtība pieaug.",
             "k < 0: argumentam pieaugot, vērtība samazinās.",
             "Jo lielāks |k|, jo stāvāka taisne.",
         ],
         pieze="b virzienu neietekmē - tas tikai pārbīda taisni uz augšu "
               "vai leju."),

    Slidnis("Maini k", [
        {"v": "k = 2", "teksts": "Augoša, stāva", "zim": _k(2, "y = 2x + 1")},
        {"v": "k = 0,5", "teksts": "Augoša, lēzena",
         "zim": _k(0.5, "y = 0,5x + 1")},
        {"v": "k = 0", "teksts": "Konstanta", "zim": _k(0, "y = 1")},
        {"v": "k = −0,5", "teksts": "Dilstoša, lēzena",
         "zim": _k(-0.5, "y = −0,5x + 1")},
        {"v": "k = −2", "teksts": "Dilstoša, stāva",
         "zim": _k(-2, "y = −2x + 1")},
    ], ievads="b = 1 visur; mainās tikai k."),

    Paraugs("Pamato",
            uzd="Vai funkcija y = 7 − 3x ir augoša vai dilstoša? Pamato.",
            soli=[
                ("y = −3x + 7", "Pārraksta standarta formā."),
                ("k = −3 < 0", "Nosaka k."),
                ("Pārbaude: x = 0 - y = 7; x = 1 - y = 4", "Samazinās."),
                ("Dilstoša", "Secinājums."),
            ],
            atbilde="Dilstoša, jo k = −3 < 0"),

    Varianti("Augoša vai dilstoša?", [
        {"jaut": "y = 0,1x − 100",
         "opcijas": ["Augoša", "Dilstoša", "Konstanta"],
         "pareizi": 0, "jaukt": False, "padoms": "k = 0,1 > 0."},
        {"jaut": "y = 5 − x",
         "opcijas": ["Augoša", "Dilstoša", "Konstanta"],
         "pareizi": 1, "jaukt": False, "padoms": "k = −1."},
        {"jaut": "y = −8",
         "opcijas": ["Augoša", "Dilstoša", "Konstanta"],
         "pareizi": 2, "jaukt": False, "padoms": "k = 0."},
        {"jaut": "y = −{x|4} + 2",
         "opcijas": ["Augoša", "Dilstoša", "Konstanta"],
         "pareizi": 1, "jaukt": False, "padoms": "k = −{1|4}."},
    ], pamats=4),

    Ievadi("Salīdzini vērtības", [
        {"jaut": "y = 3x + 1 ir augoša. Kura lielāka - f(2) vai f(5)? "
                 "Raksti argumentu.",
         "atb": ["5"], "padoms": "Augošai - lielākam x lielāks y."},
        {"jaut": "y = −2x + 1. Kura lielāka - f(2) vai f(5)? Raksti "
                 "argumentu.",
         "atb": ["2"], "padoms": "Dilstošai - mazākam x lielāks y."},
        {"jaut": "Par cik mainās y = −2x + 1, ja x pieaug par 3?",
         "atb": ["−6", "-6"], "padoms": "3 · (−2)."},
    ]),

    Pasaule("Dzīves procesi",
            Varianti("", [
                {"jaut": "Lidmašīna nolaižas: augstums atkarībā no laika.",
                 "opcijas": ["Dilstoša", "Augoša", "Konstanta"],
                 "pareizi": 0, "jaukt": False,
                 "padoms": "Augstums samazinās."},
                {"jaut": "Krājkonts: katru mēnesi +20 €.",
                 "opcijas": ["Augoša", "Dilstoša", "Konstanta"],
                 "pareizi": 0, "jaukt": False,
                 "padoms": "Summa pieaug."},
                {"jaut": "Kruīza kontrole: ātrums atkarībā no laika.",
                 "opcijas": ["Konstanta", "Augoša", "Dilstoša"],
                 "pareizi": 0, "jaukt": False,
                 "padoms": "Ātrums nemainās."},
            ]),
            pavediens="celojums",
            konteksts="Jebkuru procesu var raksturot vienā vārdā: aug, dilst "
                      "vai nemainās.",
            kapec="k zīme ir procesa «virziens»."),

    Kopsavilkums([
        "Zinu, ka k > 0 - augoša, k < 0 - dilstoša, k = 0 - konstanta.",
        "Pamatoju atbildi ar k zīmi.",
        "Zinu, ka |k| nosaka slīpumu.",
        "Salīdzinu vērtības, zinot, ka funkcija aug vai dilst.",
    ]),

    Majas([
        "Uzraksti 2 augošas un 2 dilstošas funkcijas.",
        "Atrodi dzīvē augošu, dilstošu un konstantu procesu.",
        "Uzzīmē y = 3x − 2 un y = −3x − 2 vienā plaknē.",
    ]),
]
