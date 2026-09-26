# -*- coding: utf-8 -*-
"""1. klase, 32. stunda: «Kā no viena piemēra dabūt četrus?»

No viena skaitļa sastāva (5 = 3 + 2) izriet divas summas un divas
starpības: 3 + 2 = 5, 2 + 3 = 5, 5 − 2 = 3, 5 − 3 = 2. Saskaitīšana un
atņemšana ir viena ģimene.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, majina)

TEMA = "Kā no viena piemēra dabūt četrus?"

MERKIS = ("Šodien no viena skaitļa sastāva uzrakstīsim divas summas un divas "
          "starpības.")

SATURS = [
    Sakums("Viena mājiņa - četri piemēri",
           zimejums=majina(5, [(3, 2)]),
           paraksts="3 + 2 = 5, 2 + 3 = 5, 5 − 2 = 3, 5 − 3 = 2.",
           fakti=["Visos četros ir tie paši trīs skaitļi.",
                  "Divas summas un divas starpības.",
                  "Saskaitīšana un atņemšana ir viena ģimene."]),

    Doma("Skaitļu ģimene",
         "Ja zini, ka 3 un 2 ir 5, tu zini arī, cik paliek, ja no 5 atņem 2.",
         soli=[
             "Daļa + daļa = viss (divos veidos).",
             "Viss − viena daļa = otra daļa.",
             "Viss − otra daļa = pirmā daļa.",
         ]),

    Ievadi("Pabeidz ģimeni 7 = 4 + 3", [
        {"jaut": "4 + 3 = ?", "zim": majina(7, [(4, 3)]), "atb": ["7"],
         "padoms": "Mājiņas jumts."},
        {"jaut": "3 + 4 = ?", "atb": ["7"], "padoms": "Vietām samainīti."},
        {"jaut": "7 − 3 = ?", "atb": ["4"], "padoms": "Paliek otra daļa."},
        {"jaut": "7 − 4 = ?", "atb": ["3"], "padoms": "Paliek otra daļa."},
    ]),

    Ievadi("Cita ģimene: 9, 6, 3", [
        {"jaut": "9 − 6 = ?", "zim": majina(9, [(6, 3)]), "atb": ["3"],
         "padoms": "Mājiņā: 6 un 3."},
        {"jaut": "9 − 3 = ?", "atb": ["6"], "padoms": "Otra daļa."},
        {"jaut": "Ja 8 − 5 = 3, tad 3 + 5 = ?", "atb": ["8"],
         "padoms": "Tā pati ģimene."},
        {"jaut": "Ja 6 + 4 = 10, tad 10 − 4 = ?", "atb": ["6"],
         "padoms": "Tā pati ģimene."},
    ]),

    Varianti("Vai no tās pašas ģimenes?", [
        {"jaut": "Kurš piemērs ir no ģimenes 8 = 5 + 3?",
         "opcijas": ["8 − 3 = 5", "8 − 2 = 6", "5 + 5 = 10"],
         "pareizi": 0, "padoms": "Tikai skaitļi 8, 5, 3."},
        {"jaut": "Cik piemēru var uzrakstīt ģimenei 10, 7, 3?",
         "opcijas": ["4", "2", "1"], "pareizi": 0,
         "padoms": "Divas summas, divas starpības."},
    ]),

    Pasaule("Zīmuļi penālī",
            Ievadi("", [
                {"jaut": "Penālī 6 zīmuļi: 4 krāsaini, pārējie parastie. Cik "
                         "parasto?", "atb": ["2"], "padoms": "6 − 4."},
                {"jaut": "Cik krāsaino, ja parastie ir 2?", "atb": ["4"],
                 "padoms": "6 − 2."},
            ]),
            pavediens="skola",
            konteksts="Penālī ir krāsaini un parastie zīmuļi.",
            kapec="Viena ģimene atbild uz visiem jautājumiem par penāli."),

    Kopsavilkums([
        "No viena sastāva uzrakstu četrus piemērus.",
        "Zinu, ka saskaitīšana un atņemšana ir saistītas.",
        "Lietoju summu, lai atrastu starpību.",
    ]),

    Majas([
        "Uzraksti četrus piemērus ģimenei 10, 6, 4.",
        "Izdomā savu ģimeni un palūdz kādam uzrakstīt četrus piemērus.",
        "Kurš piemērs tev šķiet vieglākais?",
    ]),
]
