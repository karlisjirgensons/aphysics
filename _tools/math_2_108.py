# -*- coding: utf-8 -*-
"""2. klase, 108. stunda: «Vai visi gadījumi ir apskatīti?»

Kombinatorikas stunda: visus gadījumus (līdz 12) uzskaita pārskatāmi -
tabulā vai sarakstā pēc noteiktas kārtības. Tā var būt drošs, ka neviens
nav aizmirsts un neviens nav divreiz.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, restis)

TEMA = "Vai visi gadījumi ir apskatīti?"

MERKIS = ("Šodien aplūkosim visus iespējamos gadījumus, ja to skaits "
          "nepārsniedz 12, un pierakstīsim tos pārskatāmi.")

_TERPI = restis([["", "zilas bikses", "melnas bikses"],
                 ["balts krekls", "balts + zilas", "balts + melnas"],
                 ["sarkans krekls", "sarkans + zilas", "sarkans + melnas"],
                 ["zaļš krekls", "zaļš + zilas", "zaļš + melnas"]])

SATURS = [
    Sakums("Cik dažādos tērpos var iziet, ja ir 3 krekli un 2 bikses?",
           zimejums=_TERPI,
           paraksts="Tabulā katram pārim sava rūtiņa: 6 tērpi.",
           fakti=["Katrs krekls der ar katrām biksēm.",
                  "Tabula nepieļauj aizmirst nevienu.",
                  "3 rindas pa 2 - 6 gadījumi."]),

    Doma("Pēc kārtības",
         "Gadījumus uzskaita sistemātiski - ar tabulu vai sarakstu.",
         soli=[
             "Paņem pirmo iespēju un savieno ar visām otrajām.",
             "Tad nākamo pirmo - atkal ar visām otrajām.",
             "Turpini, līdz pirmās beidzas.",
             "Saskaiti visus pārus.",
         ]),

    Ievadi("Cik gadījumu?", [
        {"jaut": "3 krekli un 2 bikses. Cik tērpu?", "zim": _TERPI,
         "atb": ["6"], "padoms": "Saskaiti rūtiņas tabulā."},
        {"jaut": "2 saldējumi (vaniļa, šokolāde) un 2 trauciņi (vafele, "
                 "glāze). Cik iespēju?", "atb": ["4"],
         "padoms": "Katrs ar katru: 2 + 2."},
        {"jaut": "Cik divciparu skaitļu var uzrakstīt ar cipariem 1 un 2 "
                 "(var atkārtot)?", "atb": ["4"],
         "padoms": "11, 12, 21, 22."},
        {"jaut": "4 zupas un 3 deserti. Cik pusdienu komplektu?",
         "atb": ["12"], "padoms": "Katrai zupai 3 deserti: 3 + 3 + 3 + 3."},
    ]),

    Varianti("Vai visi uzskaitīti?", [
        {"jaut": "Cipari 3, 5, 7 - divciparu skaitļi bez atkārtošanas: "
                 "35, 37, 53, 57, 73. Vai visi?",
         "opcijas": ["Nē, trūkst 75", "Jā"], "jaukt": False, "pareizi": 0,
         "padoms": "Katram pirmajam ciparam 2 iespējas."},
        {"jaut": "Anna, Toms, Līva - kā viņi var nostāties rindā pa 2 "
                 "(Anna-Toms, Toms-Anna, ...)? Cik veidu?",
         "opcijas": ["6", "3", "9"], "pareizi": 0,
         "padoms": "Katram 2 kaimiņi, un kārtība svarīga."},
    ]),

    Pasaule("Kafejnīcas ēdienkarte",
            Ievadi("", [
                {"jaut": "Kafejnīcā: 3 dzērieni un 4 kūkas. Cik dažādu "
                         "komplektu «dzēriens + kūka»?", "atb": ["12"],
                 "padoms": "4 + 4 + 4."},
                {"jaut": "Tev negaršo viena kūka. Cik komplektu tev der?",
                 "atb": ["9"], "padoms": "3 kūkas katram dzērienam."},
            ]),
            pavediens="virtuve",
            konteksts="Ēdienkartē izvēlas vienu no katras grupas.",
            kapec="Tabula parāda visas iespējas vienā skatā."),

    Kopsavilkums([
        "Uzskaitu visus gadījumus pēc kārtības.",
        "Izmantoju tabulu vai sarakstu.",
        "Pārbaudu, ka neviens nav aizmirsts vai atkārtots.",
    ]),

    Majas([
        "Cik veidos var apģērbties ar 2 cepurēm un 3 šallēm?",
        "Uzzīmē tabulu.",
        "Pārbaudi, izmēģinot ar īstām drēbēm.",
    ]),
]
