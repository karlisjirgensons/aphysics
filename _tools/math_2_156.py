# -*- coding: utf-8 -*-
"""2. klase, 156. stunda: «Kā pārbaudīt dalīšanu?»

Dalīšanu pārbauda ar reizināšanu: dalījums · dalītājs = dalāmais. Ja
32 : 4 = 8, tad 8 · 4 jābūt 32. Tā pati ideja, ko 2.3. tematā lietoja
atņemšanai.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti)

TEMA = "Kā pārbaudīt dalīšanu?"

MERKIS = ("Šodien pārbaudīsim dalījumu ar reizināšanu.")

_PN = ["pareizi", "nepareizi"]

SATURS = [
    Sakums("Kā pārliecināties, ka 32 : 4 = 8?",
           fakti=["Pārbaude: 8 · 4 = 32. Sakrīt!",
                  "Dalījums · dalītājs = dalāmais.",
                  "Tāpat kā atņemšanu pārbauda ar saskaitīšanu."]),

    Doma("Pārbaude ar reizināšanu",
         "Dalījumu reizina ar dalītāju - jāsanāk dalāmajam.",
         soli=[
             "Izrēķini: 35 : 5 = 7.",
             "Reizini: 7 · 5.",
             "Ja sanāk 35 - pareizi.",
             "Ja nesanāk - meklē kļūdu.",
         ],
         pieze="Dalāmais - ko dala, dalītājs - ar ko dala, dalījums - "
               "rezultāts."),

    Paraugs("Pārbaudi 24 : 3 = 6",
            uzd="Vai pareizi?",
            soli=[("6 · 3 = 18", "Pārbaude."),
                  ("18 nav 24", "Kļūda!"),
                  ("24 : 3 = 8, jo 8 · 3 = 24", "Pareizi.")],
            atbilde="nepareizi, jābūt 8"),

    Varianti("Pareizi vai nē?", [
        {"jaut": "40 : 5 = 8", "opcijas": _PN, "jaukt": False,
         "pareizi": 0, "padoms": "8 · 5 = 40."},
        {"jaut": "28 : 4 = 6", "opcijas": _PN, "jaukt": False,
         "pareizi": 1, "padoms": "6 · 4 = 24."},
        {"jaut": "27 : 3 = 9", "opcijas": _PN, "jaukt": False,
         "pareizi": 0, "padoms": "9 · 3 = 27."},
        {"jaut": "45 : 5 = 8", "opcijas": _PN, "jaukt": False,
         "pareizi": 1, "padoms": "8 · 5 = 40."},
    ]),

    Ievadi("Pārbaudi un izlabo", [
        {"jaut": "Pārbaude 36 : 4 = 9. Cik ir 9 · 4?", "atb": ["36"],
         "padoms": "Jāsanāk 36."},
        {"jaut": "Izlabo: 28 : 4 = 6. Pareizi ir?", "atb": ["7"],
         "padoms": "7 · 4 = 28."},
        {"jaut": "Izlabo: 45 : 5 = 8. Pareizi ir?", "atb": ["9"],
         "padoms": "9 · 5 = 45."},
        {"jaut": "Izlabo: 21 : 3 = 6. Pareizi ir?", "atb": ["7"],
         "padoms": "7 · 3 = 21."},
    ]),

    Pasaule("Vai kastes pareizi saskaitītas?",
            Varianti("", [
                {"jaut": "Noliktavā 30 bumbas saliktas kastēs pa 5. "
                         "Strādnieks saka: 5 kastes. Vai pareizi?",
                 "opcijas": ["Nē - 5 · 5 = 25, vajag 6 kastes", "Jā"],
                 "jaukt": False, "pareizi": 0, "padoms": "Pārbaudi."},
            ]),
            pavediens="veikals",
            konteksts="Sporta veikala noliktavā bumbas glabā kastēs.",
            kapec="Pārbaude pasargā no kļūdām pasūtījumā."),

    Kopsavilkums([
        "Pārbaudu dalīšanu ar reizināšanu.",
        "Zinu vārdus: dalāmais, dalītājs, dalījums.",
        "Atrodu un izlaboju kļūdu.",
    ]),

    Majas([
        "Izrēķini 4 dalījumus un pārbaudi katru.",
        "Mājinieks lai uzraksta vienu kļūdainu - atrodi.",
        "Paskaidro, kā pārbaudīji.",
    ]),
]
