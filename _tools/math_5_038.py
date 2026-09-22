# -*- coding: utf-8 -*-
"""5. klase, 38. stunda: «Kas ir kopīgais dalāmais?»

Divas dalāmo virknes blakus - un vietas, kur tās sakrīt. Kopīgos dalāmos te
vēl meklē ar acīm, uzrakstot abas virknes; paņēmiens, kas strādā arī ar
lieliem skaitļiem, nāk nākamajā stundā.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kas ir kopīgais dalāmais?"

MERKIS = ("Mācīsimies noteikt divu un trīs skaitļu kopīgos dalāmos.")

SATURS = [
    Sakums("Kur abas virknes satiekas?",
           zimejums=restis([[4, 8, 12, 16, 20, 24],
                            [6, 12, 18, 24, 30, 36]]),
           paraksts="Augšā - skaitļa 4 dalāmie, apakšā - skaitļa 6 dalāmie.",
           fakti=["Abās rindās parādās 12 un 24.",
                  "Tos sauc par kopīgajiem dalāmajiem."]),

    Doma("Kopīgais dalāmais dalās ar abiem skaitļiem",
         "Skaitlis ir divu skaitļu kopīgais dalāmais, ja tas dalās gan ar "
         "vienu, gan ar otru.",
         soli=[
             "Uzraksti pirmā skaitļa dalāmos pēc kārtas.",
             "Uzraksti otrā skaitļa dalāmos.",
             "Atrodi skaitļus, kas parādās abās virknēs.",
             "Pārbaudi katru: vai tas tiešām dalās ar abiem?",
         ],
         pieze="Kopīgo dalāmo ir bezgalīgi daudz: 12, 24, 36, 48... Katrs "
               "nākamais ir par 12 lielāks - un tieši 12 ir mazākais no "
               "tiem."),

    Zimejums("Trīs skaitļu dalāmie",
             restis([[2, 4, 6, 8, 10, 12],
                     [3, 6, 9, 12, 15, 18],
                     [4, 8, 12, 16, 20, 24]]),
             paskaidro="Skaitļi 2, 3 un 4. Visās trijās rindās ir tikai 12.",
             ievads="Ar trim skaitļiem viss notiek tāpat."),

    Paraugs("Atrodi 4 un 6 kopīgos dalāmos",
            uzd="Kuri skaitļi līdz 40 dalās gan ar 4, gan ar 6?",
            soli=[
                ("4 dalāmie: 4, 8, 12, 16, 20, 24, 28, 32, 36, 40",
                 "Katrs nākamais par 4 lielāks."),
                ("6 dalāmie: 6, 12, 18, 24, 30, 36",
                 "Katrs nākamais par 6 lielāks."),
                ("Abās virknēs: 12, 24, 36",
                 "Tie ir kopīgie dalāmie."),
                ("Mazākais no tiem ir 12",
                 "Pārējie ir tā dalāmie: 24 = 12 · 2, 36 = 12 · 3."),
            ],
            atbilde="12, 24 un 36"),

    Ievadi("Atrodi kopīgos dalāmos", [
        {"jaut": "Kurš ir mazākais skaitlis, kas dalās gan ar 4, gan ar 6?",
         "atb": ["12"], "padoms": "Abās virknēs pirmais sakritušais."},
        {"jaut": "Kurš ir nākamais 4 un 6 kopīgais dalāmais pēc 12?",
         "atb": ["24"], "padoms": "12 · 2."},
        {"jaut": "Kurš ir mazākais skaitlis, kas dalās gan ar 3, gan ar 5?",
         "atb": ["15"], "padoms": "3 · 5."},
        {"jaut": "Kurš ir mazākais skaitlis, kas dalās gan ar 2, gan ar 3, "
                 "gan ar 4?",
         "atb": ["12"], "padoms": "Skaties visās trijās virknēs."},
        {"jaut": "Cik 4 un 6 kopīgo dalāmo ir līdz 50?", "atb": ["4"],
         "padoms": "12, 24, 36, 48."},
        {"jaut": "Kurš ir mazākais skaitlis, kas dalās gan ar 6, gan ar 8?",
         "atb": ["24"], "padoms": "6, 12, 18, 24 un 8, 16, 24."},
        {"jaut": "Kurš ir mazākais skaitlis, kas dalās gan ar 5, gan ar 10?",
         "atb": ["10"], "padoms": "10 jau dalās ar 5."},
        {"jaut": "Kurš ir mazākais skaitlis, kas dalās gan ar 7, gan ar 3?",
         "atb": ["21"], "padoms": "7 · 3."},
    ], pamats=4,
        ievads="Uzraksti abas virknes un meklē sakritības."),

    Varianti("Ko par kopīgajiem dalāmajiem var pateikt?", [
        {"jaut": "Cik ir divu skaitļu kopīgo dalāmo?",
         "opcijas": ["Bezgalīgi daudz", "Tieši viens", "Tieši divi",
                     "Nav neviena"],
         "pareizi": 0,
         "padoms": "Pēc 12 nāk 24, tad 36..."},
        {"jaut": "Kas ir visi pārējie kopīgie dalāmie attiecībā pret "
                 "mazāko?",
         "opcijas": ["Tā dalāmie", "Tā dalītāji", "Pirmskaitļi",
                     "Nesaistīti skaitļi"],
         "pareizi": 0,
         "padoms": "24 un 36 ir 12 dalāmie."},
        {"jaut": "Kad divu skaitļu mazākais kopīgais dalāmais ir to "
                 "reizinājums?",
         "opcijas": ["Kad tiem nav kopīgu dalītāju, piemēram 3 un 5",
                     "Vienmēr", "Kad abi ir pāra",
                     "Kad viens dalās ar otru"],
         "pareizi": 0,
         "padoms": "3 · 5 = 15, un mazāka kopīgā dalāmā nav."},
        {"jaut": "Kāds ir 5 un 10 mazākais kopīgais dalāmais?",
         "opcijas": ["10", "50", "5", "15"],
         "pareizi": 0,
         "padoms": "10 jau dalās ar 5."},
    ], pamats=4),

    Pasaule("Kad abas ekskursijas sakrīt?",
            Ievadi("", [
                {"jaut": "Viena ekskursija brauc ik pēc 4 dienām, otra ik "
                         "pēc 6. Pēc cik dienām abas brauks vienā dienā?",
                 "atb": ["12"], "padoms": "4 un 6 kopīgais dalāmais."},
                {"jaut": "Un pēc cik dienām tas notiks otro reizi?",
                 "atb": ["24"], "padoms": "12 · 2."},
                {"jaut": "Prāmis iet ik pēc 3 stundām, vilciens ik pēc 5. Pēc "
                         "cik stundām abi atkal sakritīs?",
                 "atb": ["15"], "padoms": "3 · 5."},
                {"jaut": "Autobuss iet ik pēc 10 minūtēm, tramvajs ik pēc 15. "
                         "Pēc cik minūtēm abi būs pieturā kopā?",
                 "atb": ["30"], "padoms": "10, 20, 30 un 15, 30."},
            ]),
            pavediens="celojums",
            konteksts="Saraksti atkārtojas ik pēc sava laika, un reizēm tie "
                      "sakrīt - tieši kopīgajos dalāmajos.",
            kapec="Sakritība notiek tur, kur abas virknes satiekas."),

    Kopsavilkums([
        "Uzrakstu skaitļa dalāmo virkni.",
        "Atrodu divu un trīs skaitļu kopīgos dalāmos.",
        "Zinu, ka kopīgo dalāmo ir bezgalīgi daudz.",
        "Pamanu, ka visi pārējie ir mazākā kopīgā dalāmā dalāmie.",
    ]),

    Majas([
        "Uzraksti 6 un 9 dalāmos līdz 60 un atrodi kopīgos.",
        "Atrodi divus skaitļus, kuru mazākais kopīgais dalāmais ir 24.",
        "Atrodi divus skaitļus, kuriem mazākais kopīgais dalāmais ir viens no "
        "tiem pašiem.",
    ]),
]
