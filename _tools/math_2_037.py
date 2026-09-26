# -*- coding: utf-8 -*-
"""2. klase, 37. stunda: «Kā pārbaudīt savu rezultātu?»

Trīs pārbaudes: novērtējums (vai tuvu?), atņemšana (summa − saskaitāmais =
otrs saskaitāmais) un otrāds risinājums - saskaitāmos samaina vietām vai
rēķina citā veidā un salīdzina ar klasesbiedru.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, stabins)

TEMA = "Kā pārbaudīt savu rezultātu?"

MERKIS = ("Šodien pārbaudīsim summu, salīdzinot ar klasesbiedra rezultātu "
          "vai risinot citādi.")

SATURS = [
    Sakums("Divi bērni rēķināja 36 + 47. Viens ieguva 83, otrs 73. Kuram "
           "taisnība?",
           zimejums=stabins(36, 47, virs="1"),
           fakti=["Ja rezultāti atšķiras, kāds kļūdījies.",
                  "Otrā risinājumā kļūdu var atrast.",
                  "Pareizi: 83 - otrs aizmirsa pārnesto desmitu."]),

    Doma("Pārbaudes veidi",
         "Summu pārbauda ar citu ceļu - ja abi ceļi dod vienu skaitli, "
         "tas ir pareizs.",
         soli=[
             "Samaini saskaitāmos: 47 + 36 - summai jābūt tai pašai.",
             "Atņem: 83 − 47 = 36.",
             "Rēķini citā veidā: 36 + 40 + 7.",
             "Salīdzini ar klasesbiedru.",
         ]),

    Paraugs("Pārbaudi 58 + 24 = 82",
            uzd="Pārbaudi ar atņemšanu.",
            soli=[("82 − 24 = 58", "Atņem vienu saskaitāmo."),
                  ("58 = 58", "Sanāca otrs - pareizi.")],
            atbilde="pareizi"),

    Ievadi("Pārbaudes darbība", [
        {"jaut": "Pārbaudi 45 + 27 = 72: cik ir 72 − 27?", "atb": ["45"],
         "padoms": "Jāsanāk 45."},
        {"jaut": "Pārbaudi 39 + 16 = 55: cik ir 16 + 39?", "atb": ["55"],
         "padoms": "Samaini vietām."},
        {"jaut": "Izlabo: 64 + 19 = 73. Cik pareizi?", "atb": ["83"],
         "padoms": "4 + 9 = 13, pārnes 1."},
        {"jaut": "Izlabo: 28 + 28 = 46. Cik pareizi?", "atb": ["56"],
         "padoms": "8 + 8 = 16."},
    ]),

    Varianti("Kura pārbaude der?", [
        {"jaut": "Kā pārbaudīt 35 + 48 = 83?",
         "opcijas": ["83 − 48 = 35", "83 + 48", "35 − 48"], "pareizi": 0,
         "padoms": "Summa mīnus viens saskaitāmais."},
        {"jaut": "Anna: 26 + 37 = 63. Maija: 37 + 26 = 63. Ko tas "
                 "nozīmē?", "opcijas": ["Visticamāk, pareizi",
                                         "Noteikti nepareizi",
                                         "Neko nevar teikt"],
         "pareizi": 0, "padoms": "Divi ceļi dod vienu skaitli."},
    ]),

    Pasaule("Klases ekskursijas kase",
            Ievadi("", [
                {"jaut": "Biļetes 46 €, autobuss 38 €. Kasiere saka: 74 €. "
                         "Cik ir pareizi?", "atb": ["84"], "mers": "€",
                 "padoms": "6 + 8 = 14."},
                {"jaut": "Pārbaudi: 84 − 38 = ?", "atb": ["46"],
                 "mers": "€", "padoms": "Jāsanāk biļešu cenai."},
            ]),
            pavediens="skola",
            konteksts="Klase krāj naudu ekskursijai uz muzeju.",
            kapec="Pārbaudīta summa - nekādu pārsteigumu."),

    Kopsavilkums([
        "Pārbaudu summu ar atņemšanu.",
        "Samainu saskaitāmos vai rēķinu citā veidā.",
        "Salīdzinu ar klasesbiedru un atrodu kļūdu.",
    ]),

    Majas([
        "Izrēķini 3 summas un pārbaudi katru divos veidos.",
        "Lai mājinieks atrisina tās pašas - vai sakrīt?",
        "Kur bija kļūda, ja nesakrita?",
    ]),
]
