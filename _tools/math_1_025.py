# -*- coding: utf-8 -*-
"""1. klase, 25. stunda: «Kurš skaitlis slēpjas?»

Daļēji aizpildītā mājiņā trūkst skaitļa - jumtā vai stāvā. Jumts: abas
daļas kopā. Stāvs: cik vēl līdz jumtam. Pārbauda ar ripiņām vai
pirkstiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         bildes, majina)

TEMA = "Kurš skaitlis slēpjas?"

MERKIS = ("Šodien atradīsim mājiņā paslēpto skaitli un pārbaudīsim to.")

SATURS = [
    Sakums("Mājiņas jumts nokritis - kas tajā bija?",
           zimejums=majina(None, [(2, 6), (5, 3)]),
           paraksts="2 un 6 ir 8, 5 un 3 arī ir 8.",
           fakti=["Jumtā - abas daļas kopā.",
                  "Stāvā - cik vēl līdz jumtam.",
                  "Pārbaudi ar ripiņām."]),

    Doma("Kur slēpjas?",
         "Ja slēpjas jumts - saliec daļas kopā; ja daļa - skaiti no zināmās "
         "līdz jumtam.",
         soli=[
             "Paskaties, kur ir «?».",
             "Jumtā? Saskaiti abas daļas.",
             "Stāvā? Skaiti no zināmās daļas līdz jumtam.",
             "Pārbaudi ar ripiņām.",
         ]),

    Ievadi("Atrodi paslēpto", [
        {"jaut": "Kas ir jumtā?", "zim": majina(None, [(4, 3)]),
         "atb": ["7"], "padoms": "4 un 3."},
        {"jaut": "Kas slēpjas?", "zim": majina(9, [(6, None)]),
         "atb": ["3"], "padoms": "No 6 līdz 9."},
        {"jaut": "Kas slēpjas?", "zim": majina(10, [(None, 2)]),
         "atb": ["8"], "padoms": "Cik un 2 ir 10?"},
        {"jaut": "Kas ir jumtā?", "zim": majina(None, [(5, 5)]),
         "atb": ["10"], "padoms": "5 un 5."},
        {"jaut": "Kas slēpjas?", "zim": majina(7, [(0, None)]),
         "atb": ["7"], "padoms": "0 un cik ir 7?"},
        {"jaut": "Kas slēpjas?", "zim": majina(6, [(None, 1)]),
         "atb": ["5"], "padoms": "Cik un 1 ir 6?"},
    ], pamats=4),

    Pasaule("Paslēptās pogas",
            Ievadi("", [
                {"jaut": "Kopā 8 pogas. Uz galda redzamas 5, pārējās zem "
                         "krūzes. Cik zem krūzes?",
                 "zim": bildes([[("ripina", 5), None]]), "atb": ["3"],
                 "padoms": "No 5 līdz 8."},
                {"jaut": "Kopā 10 pogas, redzamas 4. Cik paslēptas?",
                 "atb": ["6"], "padoms": "4 un cik ir 10?"},
            ]),
            pavediens="speles",
            konteksts="Spēle: daļu pogu paslēpj zem krūzes, bet kopējo "
                      "skaitu pasaka.",
            kapec="Skaitļa sastāvs ļauj uzzināt, kas paslēpts."),

    Kopsavilkums([
        "Atrodu paslēpto skaitli mājiņā.",
        "Zinu: jumts - abas daļas kopā.",
        "Pārbaudu ar ripiņām vai pirkstiem.",
    ]),

    Majas([
        "Spēlē mājās «paslēptās pogas» ar 10 pogām.",
        "Uzzīmē mājiņu ar tukšu jumtu un palūdz kādam aizpildīt.",
        "Paslēp dažus pirkstus aiz muguras: cik paslēpi no 10?",
    ]),
]
