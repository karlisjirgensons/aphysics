# -*- coding: utf-8 -*-
"""4. klase, 34. stunda: «Kā pārbaudīt dalīšanu ar atlikumu?»

Pārbaudes vienādība: dalāmais = dalītājs · dalījums + atlikums. Tā
apvieno visus četrus skaitļus un ļauj atrast arī nezināmo dalāmo - «kāds
skaitlis, dalot ar 7, dod 5 un atlikumu 3?». Tas ir 5. klases dalāmības
un 7. klases algebras priekšvēstnesis.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā pārbaudīt dalīšanu ar atlikumu?"

MERKIS = ("Pārbaudīsim dalīšanu ar atlikumu ar vienādību: dalāmais ir "
          "dalītāja un dalījuma reizinājums plus atlikums.")

SATURS = [
    Sakums("Vai kasiere nav kļūdījusies?",
           zimejums=restis([["dalāmais", "=", "dalītājs · dalījums",
                             "+", "atlikums"],
                            ["47", "=", "6 · 7", "+", "5"]],
                           "pārbaudes vienādība"),
           paraksts="42 + 5 = 47 - sakrīt.",
           fakti=["Katru dalīšanu var pārbaudīt ar reizināšanu un "
                  "saskaitīšanu.",
                  "Pārbaudē jābūt arī atlikumam < dalītājs."]),

    Doma("Dalāmais = dalītājs · dalījums + atlikums",
         "Sareizini dalījumu ar dalītāju, pieskaiti atlikumu - jāsanāk "
         "dalāmajam.",
         soli=[
             "Sareizini dalītāju un dalījumu.",
             "Pieskaiti atlikumu.",
             "Salīdzini ar dalāmo.",
             "Pārbaudi arī: atlikums < dalītājs.",
         ],
         pieze="Tā var atrast arī dalāmo: ja 7 · 5 + 3, tad dalāmais ir 38."),

    Paraugs("Pārbaudi 59 : 8 = 7 (atl. 3)",
            uzd="Vai 59 : 8 = 7 (atl. 3) ir pareizi?",
            soli=[
                ("8 · 7 = 56", None),
                ("56 + 3 = 59", "Sakrīt ar dalāmo."),
                ("3 < 8", "Atlikums mazāks par dalītāju."),
            ],
            atbilde="pareizi"),

    Ievadi("Pārbaudi vai atrodi", [
        {"jaut": "Kāds skaitlis, dalot ar 7, dod 5 un atlikumu 3?",
         "atb": ["38"], "padoms": "7 · 5 + 3."},
        {"jaut": "Kāds skaitlis, dalot ar 4, dod 9 un atlikumu 2?",
         "atb": ["38"], "padoms": "4 · 9 + 2."},
        {"jaut": "6 · 8 + 5 = ? (dalāmais)", "atb": ["53"],
         "padoms": "48 + 5."},
        {"jaut": "Kāds skaitlis, dalot ar 9, dod 6 un atlikumu 8?",
         "atb": ["62"], "padoms": "54 + 8."},
    ]),

    Varianti("Pareizi vai aplami?", [
        {"jaut": "43 : 5 = 8 (atl. 3)",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "5 · 8 + 3 = 43."},
        {"jaut": "43 : 5 = 7 (atl. 8)",
         "opcijas": ["aplami", "pareizi"], "pareizi": 0,
         "padoms": "5 · 7 + 8 = 43, bet 8 > 5 - atlikums par lielu."},
        {"jaut": "30 : 4 = 7 (atl. 3)",
         "opcijas": ["aplami", "pareizi"], "pareizi": 0,
         "padoms": "4 · 7 + 3 = 31, nevis 30."},
        {"jaut": "65 : 9 = 7 (atl. 2)",
         "opcijas": ["pareizi", "aplami"], "pareizi": 0,
         "padoms": "63 + 2 = 65."},
    ], pamats=4),

    Zimejums("Četri skaitļi vienā bildē",
             restis([["7", "7", "7", "7", "7", "7", "7", "7", "3"]],
                    "59 = 8 · 7 + 3"),
             paskaidro="Astoņas grupas pa 7 un vēl 3. Tās pašas rūtiņas var "
                       "salasīt kā 59 : 8 = 7 (atl. 3).",
             ievads="Dalīšana ar atlikumu ir grupas un astes gals."),

    Pasaule("Kalendāra noslēpums",
            Ievadi("", [
                {"jaut": "Gadā ir 365 dienas. Cik pilnu nedēļu? (7 · 52 = "
                         "364)",
                 "atb": ["52"], "padoms": "365 : 7."},
                {"jaut": "Cik dienu paliek pāri?",
                 "atb": ["1"], "padoms": "365 − 364."},
                {"jaut": "Šodien ir pirmdiena. Kāda nedēļas diena būs pēc 30 "
                         "dienām? Kāds ir atlikums, dalot 30 ar 7?",
                 "atb": ["2"], "padoms": "7 · 4 = 28."},
                {"jaut": "Pārbaude: 7 · 4 + 2 = ?",
                 "atb": ["30"], "padoms": "28 + 2."},
            ]),
            pavediens="skola",
            konteksts="Tāpēc dzimšanas diena katru gadu iekrīt par vienu "
                      "nedēļas dienu vēlāk - pāri paliek 1 diena.",
            kapec="Atlikums pasaka, kura nedēļas diena būs pēc daudzām "
                  "dienām."),

    Kopsavilkums([
        "Pārbaudu dalīšanu ar atlikumu ar vienādību.",
        "Atrodu dalāmo, ja zinu dalītāju, dalījumu un atlikumu.",
        "Pamanu, ja atlikums ir par lielu.",
    ]),

    Majas([
        "Izrēķini, kura nedēļas diena būs pēc 100 dienām no šodienas.",
        "Izdomā dalīšanu ar atlikumu un palūdz kādu to pārbaudīt.",
        "Uzraksti pārbaudes vienādību savam dzimšanas datumam: diena : 7.",
    ]),
]
