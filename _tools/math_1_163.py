# -*- coding: utf-8 -*-
"""1. klase, 163. stunda: «Cik kociņu vajag kubam?»

Kuba karkasam vajag 12 kociņu (šķautnes) un 8 plastilīna bumbiņas
(virsotnes). Kubam ir 6 skaldnes. Saskaita pa daļām: apakšā 4, augšā 4,
stateniski 4.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule,
                         Petijums, Sakums, Varianti, kermenis)

TEMA = "Cik kociņu vajag kubam?"

MERKIS = ("Šodien noteiksim, cik kociņu un savienojumu vajag kuba modelim, "
          "un lietosim vārdus virsotne un šķautne.")

SATURS = [
    Sakums("Cik kociņu vajag kuba karkasam?",
           zimejums=kermenis("kubs"),
           paraksts="Apakšā 4, augšā 4, stateniski 4 - kopā 12.",
           fakti=["Kociņi - šķautnes: 12.",
                  "Savienojumi - virsotnes: 8.",
                  "Sienas - skaldnes: 6."]),

    Doma("Kuba daļas",
         "Šķautne - mala, kur satiekas divas skaldnes; virsotne - stūris.",
         soli=[
             "Apakšējais kvadrāts - 4 šķautnes, 4 virsotnes.",
             "Augšējais kvadrāts - vēl 4 šķautnes, 4 virsotnes.",
             "Stateniskās šķautnes - 4.",
             "Kopā: 12 šķautnes, 8 virsotnes.",
         ]),

    Ievadi("Saskaiti", [
        {"jaut": "Cik šķautņu ir kubam?", "zim": kermenis("kubs"),
         "atb": ["12"], "padoms": "4 + 4 + 4."},
        {"jaut": "Cik virsotņu ir kubam?", "atb": ["8"],
         "padoms": "4 apakšā, 4 augšā."},
        {"jaut": "Cik skaldņu ir kubam?", "atb": ["6"],
         "padoms": "Kā kauliņam - 6 puses."},
        {"jaut": "Cik kociņu vajag 2 atsevišķiem kubiem?", "atb": ["24"],
         "padoms": "12 + 12."},
    ]),

    Varianti("Kas tas ir?", [
        {"jaut": "Kuba stūris, kur satiekas kociņi, ir...",
         "opcijas": ["virsotne", "šķautne", "skaldne"], "pareizi": 0,
         "padoms": "Stūris - virsotne."},
        {"jaut": "Kuba mala - kociņš - ir...",
         "opcijas": ["šķautne", "virsotne", "skaldne"], "pareizi": 0,
         "padoms": "Mala - šķautne."},
    ]),

    Petijums("Kuba karkass", [
        "Paņem 12 vienāda garuma kociņus un 8 plastilīna bumbiņas.",
        "Saliec apakšējo kvadrātu.",
        "Iesprauž 4 stateniskus kociņus.",
        "Saliec augšējo kvadrātu. Vai pietika?",
    ], vajag="12 kociņi, plastilīns"),

    Pasaule("Rotaļu kaste",
            Ievadi("", [
                {"jaut": "Kuba formas kastes malas aplīmē ar lenti. Cik "
                         "šķautnēm vajag lenti?", "atb": ["12"],
                 "padoms": "Visām šķautnēm."},
            ]),
            pavediens="maja",
            konteksts="Kasti ar mantām izrotā ar lenti.",
            kapec="Šķautņu skaits pasaka, cik lentes gabalu."),

    Kopsavilkums([
        "Zinu, ka kubam ir 12 šķautnes un 8 virsotnes.",
        "Zinu, ka kubam ir 6 skaldnes.",
        "Uzbūvēju kuba karkasu.",
    ]),

    Majas([
        "Atrodi mājās kubu (kauliņš, kaste).",
        "Saskaiti tā virsotnes un šķautnes.",
        "Uzbūvē kubu no zobu bakstāmajiem un plastilīna.",
    ]),
]
