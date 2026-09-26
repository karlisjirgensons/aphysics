# -*- coding: utf-8 -*-
"""2. klase, 94. stunda: «Kur algoritms kļūdās?»

Kļūdu meklēšana algoritmā (programmētāji to sauc par atkļūdošanu): izpilda
soli pa solim ar konkrētu skaitli un salīdzina ar gaidīto. Kur rezultāts
novirzās - tur ir kļūda.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, algoritms, celjs)

TEMA = "Kur algoritms kļūdās?"

MERKIS = ("Šodien atradīsim kļūdu dotā algoritmā un izlabosim to.")

SATURS = [
    Sakums("Robotam jānonāk pie ābola, bet tas atsitas pret sienu. Kāpēc?",
           zimejums=celjs(5, 4, (0, 3), (4, 0), "→→↑↑↑→→",
                          skersli=[(2, 1), (2, 2)]),
           paraksts="Pelēkās rūtiņas - siena.",
           fakti=["Algoritms bija uzrakstīts pirms sienas.",
                  "Kļūdu atrod, izpildot soli pa solim.",
                  "Programmētāji to sauc par atkļūdošanu."]),

    Doma("Atkļūdošana",
         "Izpildi algoritmu ar piemēru un salīdzini katru soli ar gaidīto.",
         soli=[
             "Izvēlies piemēru, kuram zini pareizo atbildi.",
             "Izpildi pirmo soli - vai sakrīt?",
             "Turpini, līdz kaut kas nesakrīt.",
             "Izlabo šo soli un pārbaudi vēlreiz.",
         ]),

    Varianti("Atrodi kļūdaino soli", [
        {"jaut": "Algoritmam jāpalielina skaitlis par 10. Kur kļūda?",
         "zim": algoritms(["Paņem skaitli", "Pieskaiti 15", "Atņem 3"]),
         "opcijas": ["jāatņem 5, nevis 3", "jāpieskaita 10",
                     "viss pareizi"], "pareizi": 0,
         "padoms": "+ 15 − 3 = + 12."},
        {"jaut": "Lieliem skaitļiem (virs 50) jāatņem 20, pārējiem "
                 "jāpieskaita 20. Kur kļūda?",
         "zim": algoritms(["Paņem skaitli",
                           ("Vai lielāks nekā 50?", "Pieskaiti 20",
                            "Atņem 20")]),
         "opcijas": ["zari samainīti", "jautājums nepareizs",
                     "viss pareizi"], "pareizi": 0,
         "padoms": "Pie «jā» jāatņem."},
    ]),

    Ievadi("Pārbaudi ar piemēru", [
        {"jaut": "Algoritms: + 15, − 3. Skaitlis 20 - kāds rezultāts?",
         "atb": ["32"], "padoms": "35 − 3."},
        {"jaut": "Bet vajadzēja 20 + 10. Par cik rezultāts par lielu?",
         "atb": ["2"], "padoms": "32 − 30."},
    ]),

    Pasaule("Kafijas automāts",
            Varianti("", [
                {"jaut": "Automāts: ja iemet 2 €, izdod kakao. Tu iemet 2 €, "
                         "bet tas izdod atpakaļ 1 € un neko citu. Kas "
                         "algoritmā varētu būt nepareizi?",
                 "opcijas": ["nosacījumā pārbauda 1 €, nevis 2 €",
                             "kakao ir par dārgu", "viss kārtībā"],
                 "pareizi": 0, "padoms": "Nosacījums nesakrīt ar cenu."},
            ]),
            pavediens="tehnika",
            konteksts="Automāti darbojas pēc algoritma.",
            kapec="Viena kļūda algoritmā - un mašīna strādā aplami."),

    Kopsavilkums([
        "Izpildu algoritmu soli pa solim ar piemēru.",
        "Atrodu kļūdaino soli.",
        "Izlaboju un pārbaudu vēlreiz.",
    ]),

    Majas([
        "Uzraksti algoritmu ar vienu apzinātu kļūdu.",
        "Lai mājinieks to atrod.",
        "Izlabojiet kopā.",
    ]),
]
