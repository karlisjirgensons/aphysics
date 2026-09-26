# -*- coding: utf-8 -*-
"""2. klase, 30. stunda: «Vai atbilde ir ticama?»

Divi pārbaudes veidi: pēc jēgas (vai rezultāts var būt tāds?) un ar pretējo
darbību (saskaitīšanu pārbauda ar atņemšanu un otrādi). Pirmais noķer
lielas kļūdas, otrais - arī mazas.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Vai atbilde ir ticama?"

MERKIS = ("Šodien pārbaudīsim rezultātu ar pretējo darbību un novērtēsim, "
          "vai tas ir ticams.")

_TIC = ["ticama", "neticama"]

SATURS = [
    Sakums("Kalkulators rāda: 9 + 8 = 98. Vai tam ticēt?",
           fakti=["Divu viencipara skaitļu summa nevar būt 98.",
                  "Kāds nospieda nepareizu pogu!",
                  "Pārbaude: 17 − 8 = 9. Tātad pareizi ir 17."]),

    Doma("Pretējā darbība",
         "Saskaitīšanu pārbauda ar atņemšanu, atņemšanu - ar saskaitīšanu.",
         soli=[
             "Vispirms padomā: vai rezultāts var būt tāds?",
             "9 + 8 = 17 - pārbaude: 17 − 8 = 9. Sakrīt!",
             "15 − 6 = 9 - pārbaude: 9 + 6 = 15. Sakrīt!",
             "Ja nesakrīt, meklē kļūdu.",
         ]),

    Paraugs("Pārbaudi 14 − 5 = 8",
            uzd="Vai 14 − 5 = 8 ir pareizi?",
            soli=[("8 + 5 = 13", "Pretējā darbība."),
                  ("13 nav 14", "Nesakrīt - kļūda."),
                  ("14 − 5 = 9", "Pārbaude: 9 + 5 = 14.")],
            atbilde="nav pareizi, jābūt 9"),

    Varianti("Ticama vai neticama?", [
        {"jaut": "7 + 6 = 31", "opcijas": _TIC, "jaukt": False,
         "pareizi": 1, "padoms": "Divu mazu skaitļu summa nevar būt 31."},
        {"jaut": "18 − 9 = 9", "opcijas": _TIC, "jaukt": False,
         "pareizi": 0, "padoms": "9 + 9 = 18."},
        {"jaut": "12 − 4 = 16", "opcijas": _TIC, "jaukt": False,
         "pareizi": 1, "padoms": "Atņemot nevar sanākt vairāk."},
        {"jaut": "5 + 9 = 14", "opcijas": _TIC, "jaukt": False,
         "pareizi": 0, "padoms": "14 − 9 = 5."},
    ]),

    Ievadi("Pārbaudes darbība", [
        {"jaut": "Pārbaudi 8 + 7 = 15. Cik ir 15 − 7?", "atb": ["8"],
         "padoms": "Jāsanāk pirmajam skaitlim."},
        {"jaut": "Pārbaudi 16 − 9 = 7. Cik ir 7 + 9?", "atb": ["16"],
         "padoms": "Jāsanāk skaitlim, no kura atņēma."},
        {"jaut": "Izlabo: 13 − 7 = 5. Cik ir pareizi?", "atb": ["6"],
         "padoms": "6 + 7 = 13."},
        {"jaut": "Izlabo: 9 + 9 = 19. Cik ir pareizi?", "atb": ["18"],
         "padoms": "18 − 9 = 9."},
    ]),

    Pasaule("Vai kasiere nekļūdījās?",
            Varianti("", [
                {"jaut": "Tev bija 20 €, nopirki par 13 €. Kasiere izdeva "
                         "5 €. Vai pareizi?",
                 "opcijas": ["Nē, vajag 7 €", "Jā"], "jaukt": False,
                 "pareizi": 0, "padoms": "13 + 5 = 18, nevis 20."},
                {"jaut": "Tev bija 15 €, nopirki par 8 €, izdeva 7 €. Vai "
                         "pareizi?", "opcijas": ["Jā", "Nē"],
                 "jaukt": False, "pareizi": 0, "padoms": "8 + 7 = 15."},
            ]),
            pavediens="veikals",
            konteksts="Pārbaudi atlikumu ar saskaitīšanu: cena + atlikums = "
                      "iedotā nauda.",
            kapec="Tā pārbauda arī pieaugušie."),

    Kopsavilkums([
        "Novērtēju, vai rezultāts var būt tāds.",
        "Pārbaudu saskaitīšanu ar atņemšanu un otrādi.",
        "Atrodu un izlaboju kļūdu.",
    ]),

    Majas([
        "Izrēķini 4 piemērus un pārbaudi katru ar pretējo darbību.",
        "Mājinieks lai ieraksta vienu kļūdu - atrodi to.",
        "Veikalā pārbaudi, vai atlikums pareizs.",
    ]),
]
