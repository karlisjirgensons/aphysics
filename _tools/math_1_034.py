# -*- coding: utf-8 -*-
"""1. klase, 34. stunda: «Kuras summas jau zini no galvas?»

Katrs atlasa summas un starpības, ko jau zina no galvas (+1, +0, dubultie,
desmita draugi), un pārējās trenē pārī. Zināmās kļūst par «tiltiņiem» uz
nezināmajām: 5 + 6 ir 5 + 5 un vēl 1.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Pasaule, Sakums,
                         Varianti, ramis)

TEMA = "Kuras summas jau zini no galvas?"

MERKIS = ("Šodien atradīsim summas, ko jau zinām no galvas, un ar tām "
          "izrēķināsim jaunas.")

SATURS = [
    Sakums("Kuras summas tu zini uzreiz?",
           zimejums=ramis(10, otra=5),
           paraksts="5 + 5 = 10 - to zina gandrīz visi.",
           fakti=["+ 1 - nākamais skaitlis.",
                  "Dubultie: 2 + 2, 3 + 3, 4 + 4, 5 + 5.",
                  "Desmita draugi: 7 + 3, 6 + 4, 8 + 2."]),

    Doma("No zināmā uz jauno",
         "Ja zini 4 + 4 = 8, tad 4 + 5 ir par 1 vairāk: 9.",
         soli=[
             "Atrodi tuvāko summu, ko zini.",
             "Paskaties, par cik jaunā atšķiras.",
             "Pieliec vai atņem starpību.",
         ]),

    Ievadi("Zināmās", [
        {"jaut": "6 + 1 = ?", "atb": ["7"], "padoms": "Nākamais."},
        {"jaut": "3 + 3 = ?", "atb": ["6"], "padoms": "Dubultais."},
        {"jaut": "8 + 2 = ?", "atb": ["10"], "padoms": "Desmita draugi."},
        {"jaut": "9 + 0 = ?", "atb": ["9"], "padoms": "Plus nekas."},
    ]),

    Ievadi("No zināmā uz jauno", [
        {"jaut": "4 + 4 = 8. Cik ir 4 + 5?", "atb": ["9"],
         "padoms": "Par 1 vairāk."},
        {"jaut": "5 + 5 = 10. Cik ir 5 + 4?", "atb": ["9"],
         "padoms": "Par 1 mazāk."},
        {"jaut": "3 + 3 = 6. Cik ir 3 + 4?", "atb": ["7"],
         "padoms": "Par 1 vairāk."},
        {"jaut": "7 + 3 = 10. Cik ir 10 − 3?", "atb": ["7"],
         "padoms": "Tā pati ģimene."},
        {"jaut": "2 + 2 = 4. Cik ir 2 + 3?", "atb": ["5"],
         "padoms": "Par 1 vairāk."},
        {"jaut": "6 + 4 = 10. Cik ir 10 − 6?", "atb": ["4"],
         "padoms": "Tā pati ģimene."},
    ], pamats=4),

    Varianti("Kura summa palīdz?", [
        {"jaut": "Kura zināmā summa palīdz izrēķināt 5 + 6?",
         "opcijas": ["5 + 5", "2 + 2", "7 + 3"], "pareizi": 0,
         "padoms": "Tuvākais dubultais."},
        {"jaut": "Kura palīdz izrēķināt 10 − 2?",
         "opcijas": ["8 + 2", "5 + 5", "1 + 1"], "pareizi": 0,
         "padoms": "Tā pati ģimene."},
    ]),

    Pasaule("Kartītes pārī",
            Ievadi("", [
                {"jaut": "Tu zini 4 summas no 10. Cik vēl jātrenē?",
                 "atb": ["6"], "padoms": "10 − 4."},
            ]),
            pavediens="skola",
            konteksts="Pārī katrs sašķiro kartītes: «zinu» un «jātrenē».",
            kapec="Tā redz, kas vēl jāmācās."),

    Kopsavilkums([
        "Zinu no galvas + 1, dubultos un desmita draugus.",
        "No zināmās summas izrēķinu jaunu.",
        "Atlasu, ko vēl jātrenē.",
    ]),

    Majas([
        "Uztaisi 10 kartītes ar summām un sašķiro: zinu / jātrenē.",
        "Katru dienu atkārto 3 kartītes no «jātrenē».",
        "Pēc nedēļas saskaiti, cik jau zini.",
    ]),
]
