# -*- coding: utf-8 -*-
"""7. klase, 2. stunda: «Kā kopu var aprakstīt?»

Kopu var uzdot divējādi: uzskaitot visus elementus vai nosakot īpašību,
kas tos visus vieno. Uzskaitīšana der mazām kopām, īpašība - lielām un
bezgalīgām. Stundā pāriet no viena veida uz otru abos virzienos.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, taisne)

TEMA = "Kā kopu var aprakstīt?"

MERKIS = ("Iemācīsimies uzdot kopu, uzskaitot elementus vai nosakot to "
          "raksturīgo īpašību.")

SATURS = [
    Sakums("Kā aprakstīt visus pāra skaitļus?",
           fakti=["Pāra skaitļu ir bezgalīgi daudz - tos nevar uzskaitīt.",
                  "Bet tos var aprakstīt ar vienu īpašību: dalās ar 2.",
                  "Tāpat bibliotēka apraksta «visas grāmatas par kosmosu»."]),

    Doma("Uzskaiti vai apraksti ar īpašību",
         "Kopu var uzdot, uzskaitot visus tās elementus vai nosakot "
         "raksturīgo īpašību - noteikumu, kas der visiem kopas elementiem un "
         "neder nevienam citam.",
         soli=[
             "Mazu kopu var uzskaitīt: A = {1; 2; 3; 4}.",
             "Lielai kopai raksta īpašību: A - naturālie skaitļi, mazāki "
             "nekā 5.",
             "Pārbaudi īpašību: vai tā der katram elementam?",
             "Pārbaudi otrādi: vai nav lieku elementu, kam tā arī der?",
         ],
         pieze="Naturālo skaitļu kopu apzīmē ar N = {1; 2; 3; ...}. "
               "Daudzpunkte nozīmē «un tā tālāk bez gala»."),

    Paraugs("No īpašības uz sarakstu",
            uzd="Kopa K - naturālie skaitļi, kas ir 24 dalītāji un lielāki "
                "nekā 5. Uzskaiti tās elementus.",
            soli=[
                ("24 dalītāji: 1; 2; 3; 4; 6; 8; 12; 24",
                 "Meklē pa pāriem: 1 · 24, 2 · 12, 3 · 8, 4 · 6."),
                ("Lielāki nekā 5: 6; 8; 12; 24",
                 "Atmet 1; 2; 3; 4."),
                ("K = {6; 8; 12; 24}",
                 "Četri elementi."),
            ],
            atbilde="K = {6; 8; 12; 24}"),

    Zimejums("Kopa uz skaitļu taisnes",
             taisne(0, 10, 1, [(3, "3"), (6, "6"), (9, "9")]),
             ievads="Kopa {3; 6; 9} - naturālie skaitļi līdz 10, kas dalās "
                    "ar 3.",
             paskaidro="Īpašība «dalās ar 3» izvēlas tieši trīs punktus."),

    Varianti("Kura īpašība der?", [
        {"jaut": "Kura īpašība apraksta kopu {5; 10; 15; 20}?",
         "opcijas": ["Naturālie skaitļi līdz 20, kas dalās ar 5",
                     "Skaitļi, kas dalās ar 5",
                     "Divciparu skaitļi, kas dalās ar 5",
                     "Nepāra skaitļi līdz 20"],
         "pareizi": 0,
         "padoms": "Īpašība nedrīkst ielaist liekus elementus, piemēram, 25."},
        {"jaut": "Kopa - viencipara pirmskaitļi. Kā to uzskaitīt?",
         "opcijas": ["{2; 3; 5; 7}", "{1; 3; 5; 7}", "{3; 5; 7; 9}",
                     "{2; 3; 5; 7; 9}"],
         "pareizi": 0,
         "padoms": "1 nav pirmskaitlis, 9 = 3 · 3."},
        {"jaut": "Kopa {1; 4; 9; 16; 25} ir...",
         "opcijas": ["naturālo skaitļu kvadrāti līdz 25",
                     "nepāra skaitļi līdz 25",
                     "skaitļi, kas dalās ar 4",
                     "pirmskaitļi līdz 25"],
         "pareizi": 0,
         "padoms": "1 = 1², 4 = 2², 9 = 3², ..."},
        {"jaut": "Kurai kopai elementus nevar visus uzskaitīt?",
         "opcijas": ["Visi pāra skaitļi", "Pāra skaitļi līdz 100",
                     "Mēneši ar 31 dienu", "Latvijas novadu centri"],
         "pareizi": 0,
         "padoms": "Kurai kopai nav gala?"},
    ], pamats=4),

    Ievadi("Uzskaiti un saskaiti", [
        {"jaut": "Cik elementu ir kopā - naturālie skaitļi, mazāki nekā 8?",
         "atb": ["7"], "padoms": "1; 2; ...; 7."},
        {"jaut": "Cik elementu ir kopā - 36 dalītāji?",
         "atb": ["9"], "padoms": "1; 2; 3; 4; 6; 9; 12; 18; 36."},
        {"jaut": "Cik elementu ir kopā - divciparu skaitļi, kuru ciparu "
                 "summa ir 3?",
         "atb": ["3"], "padoms": "12; 21; 30."},
        {"jaut": "Cik elementu ir kopā - mēneši, kuros ir 30 dienu?",
         "atb": ["4"], "padoms": "Aprīlis, jūnijs, septembris, novembris."},
        {"jaut": "Cik elementu ir kopā - naturālie skaitļi no 10 līdz 50, "
                 "kas dalās ar 10?",
         "atb": ["5"], "padoms": "10; 20; 30; 40; 50."},
        {"jaut": "Cik elementu ir kopā - 13 dalītāji?",
         "atb": ["2"], "padoms": "13 ir pirmskaitlis."},
    ], pamats=4),

    Pasaule("Filtrs internetveikalā",
            Ievadi("", [
                {"jaut": "Austiņu cenas (€): 19; 35; 48; 52; 27; 60. "
                         "Filtrs rāda cenas no 25 līdz 50 €. Cik austiņu "
                         "ir šajā kopā?",
                 "atb": ["3"], "padoms": "35; 48; 27."},
                {"jaut": "Kāda ir lētākā cena šajā kopā (€)?",
                 "atb": ["27"], "padoms": "No 35; 48; 27."},
                {"jaut": "Filtru nomaina uz «līdz 30 €». Cik austiņu tagad?",
                 "atb": ["2"], "padoms": "19 un 27."},
            ]),
            pavediens="veikals",
            konteksts="Veikala filtrs ir kopas īpašība: tas no visām precēm "
                      "atlasa tās, kam īpašība der.",
            kapec="Filtrs ir raksturīgā īpašība - dators pats uzskaita "
                  "elementus."),

    Kopsavilkums([
        "Uzdodu kopu, uzskaitot elementus.",
        "Uzdodu kopu ar raksturīgo īpašību.",
        "Pārbaudu, vai īpašība neielaiž liekus elementus.",
        "Zinu, ka N = {1; 2; 3; ...} ir naturālo skaitļu kopa.",
    ]),

    Majas([
        "Uzraksti kopu {2; 4; 8; 16} ar īpašību.",
        "Uzskaiti kopu - 30 dalītāji.",
        "Izdomā filtru savam telefonam: kuras lietotnes tas atlasītu?",
    ]),
]
