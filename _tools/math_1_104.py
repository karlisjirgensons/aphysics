# -*- coding: utf-8 -*-
"""1. klase, 104. stunda: «Kur paslēpusies kļūda?»

Dotā risinājumā atrod kļūdu un izskaidro, kā to labot. Biežākās kļūdas:
aizmirsts desmits (7 + 5 = 2), sajaukta zīme, nepareizi sadalīts skaitlis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti)

TEMA = "Kur paslēpusies kļūda?"

MERKIS = ("Šodien atradīsim kļūdas dotos risinājumos un izskaidrosim, kā "
          "tās izlabot.")

SATURS = [
    Sakums("Toms raksta 7 + 5 = 2. Kas notika?",
           fakti=["7 + 5 = 12 - Toms aizmirsa desmitu.",
                  "Kļūdas ir normālas - svarīgi tās atrast.",
                  "Pārbaude ar pretējo darbību palīdz."]),

    Doma("Kļūdu meklētājs",
         "Pārbaudi katru soli - kļūda vienmēr ir kādā solī.",
         soli=[
             "Pārbaudi rezultātu ar pretējo darbību.",
             "Ja nesakrīt - pārbaudi katru soli.",
             "Atrodi soli ar kļūdu un izlabo.",
         ]),

    Varianti("Kāda kļūda?", [
        {"jaut": "7 + 5 = 2",
         "opcijas": ["aizmirsts desmits", "sajaukta zīme", "viss pareizi"],
         "pareizi": 0, "padoms": "Jābūt 12."},
        {"jaut": "15 − 3 = 18",
         "opcijas": ["saskaitīja, nevis atņēma", "aizmirsts desmits",
                     "viss pareizi"], "pareizi": 0,
         "padoms": "15 + 3 = 18."},
        {"jaut": "9 + 4 = 9 + 1 + 4 = 14",
         "opcijas": ["4 sadalīts nepareizi", "sajaukta zīme",
                     "viss pareizi"], "pareizi": 0,
         "padoms": "4 = 1 + 3."},
    ]),

    Ievadi("Izlabo", [
        {"jaut": "7 + 5 = ?", "atb": ["12"], "padoms": "7 + 3 + 2."},
        {"jaut": "15 − 3 = ?", "atb": ["12"], "padoms": "5 − 3."},
        {"jaut": "9 + 4 = ?", "atb": ["13"], "padoms": "9 + 1 + 3."},
        {"jaut": "Anna: 16 − 9 = 8. Pareizi ir ...", "atb": ["7"],
         "padoms": "9 + 7 = 16."},
    ]),

    Pasaule("Kļūda čekā",
            Ievadi("", [
                {"jaut": "Čekā: 8 € + 7 € = 16 €. Cik jābūt?", "atb": ["15"],
                 "padoms": "8 + 2 + 5."},
                {"jaut": "Par cik € čekā par daudz?", "atb": ["1"],
                 "padoms": "16 − 15."},
            ]),
            pavediens="veikals",
            konteksts="Arī kasē var kļūdīties.",
            kapec="Kas pārbauda, tas nepārmaksā."),

    Kopsavilkums([
        "Atrodu kļūdu risinājumā.",
        "Nosaucu kļūdas veidu.",
        "Izlaboju un pārbaudu.",
    ]),

    Majas([
        "Uzraksti mājiniekam 3 piemērus - vienā ar apzinātu kļūdu.",
        "Vai viņš atrada kļūdu?",
        "Pārbaudi savu mājasdarbu ar pretējo darbību.",
    ]),
]
