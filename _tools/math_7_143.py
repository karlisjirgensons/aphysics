# -*- coding: utf-8 -*-
"""7. klase, 143. stunda: «Kā izteikt vienu lielumu ar otru?»

No proporcijas vai formulas var izteikt jebkuru lielumu: no {s|t} = v
iegūst s = vt un t = {s|v}. Stunda iemāca to darīt ar tām pašām
ekvivalentajām pārveidošanām, ko lieto vienādojumiem.
"""

from math_saturs import (Doma, Ievadi, Kopsavilkums, Majas, Paraugs,
                         Pasaule, Sakums, Varianti, Zimejums, restis)

TEMA = "Kā izteikt vienu lielumu ar otru?"

MERKIS = ("Izteiksim vienu lielumu ar otru no proporcijas un skaidrosim "
          "pierakstu.")

SATURS = [
    Sakums("Viena formula - trīs jautājumi",
           zimejums=restis([["zināms", "meklē", "formula"],
                            ["s, t", "v", "v = s : t"],
                            ["v, t", "s", "s = vt"],
                            ["s, v", "t", "t = s : v"]]),
           fakti=["Ātrums, ceļš un laiks - viena sakarība.",
                  "Izsakot vajadzīgo lielumu, formula kļūst ērta.",
                  "Tas ir vienādojuma risināšana ar burtiem."]),

    Doma("Izsaki kā nezināmo vienādojumā",
         "Lai no formulas izteiktu kādu lielumu, uzskata to par nezināmo un "
         "lieto ekvivalentās pārveidošanas: reizina, dala, pārnes - līdz tas "
         "paliek viens vienā pusē.",
         soli=[
             "Nosaki, kuru lielumu izteikt.",
             "Ja tas ir saucējā - reizini abas puses ar saucēju.",
             "Ja tam ir koeficients - dali ar to.",
             "Pārbaudi ar skaitļiem.",
         ],
         pieze="No proporcijas {a|b} = {c|d}: a = {bc|d}, d = {bc|a} - tas pats "
               "krustiskais reizinājums."),

    Paraugs("Izsaki laiku",
            uzd="No v = {s|t} izsaki t.",
            soli=[
                ("vt = s", "(abas puses · t)"),
                ("t = {s|v}", "(abas puses : v)"),
                ("Pārbaude: s = 100, v = 20 ⇒ t = 5", "20 = 100 : 5 ✓"),
            ],
            atbilde="t = {s|v}"),

    Varianti("Izsaki", [
        {"jaut": "P = 4a. Izsaki a.",
         "opcijas": ["a = {P|4}", "a = 4P", "a = P − 4", "a = {4|P}"],
         "pareizi": 0, "padoms": "Dala ar 4."},
        {"jaut": "S = ab. Izsaki b.",
         "opcijas": ["b = {S|a}", "b = Sa", "b = S − a", "b = {a|S}"],
         "pareizi": 0, "padoms": "Dala ar a."},
        {"jaut": "{a|b} = {c|d}. Izsaki c.",
         "opcijas": ["c = {ad|b}", "c = {ab|d}", "c = {bd|a}", "c = abd"],
         "pareizi": 0, "padoms": "ad = bc."},
        {"jaut": "y = 2x + 3. Izsaki x.",
         "opcijas": ["x = {y − 3|2}", "x = {y|2} − 3", "x = 2y − 3",
                     "x = {y + 3|2}"],
         "pareizi": 0, "padoms": "Vispirms − 3, tad : 2."},
    ], pamats=4),

    Ievadi("Aprēķini pēc izteiktās formulas", [
        {"jaut": "t = {s|v}. s = 240 km, v = 80 km/h. t (h)?",
         "atb": ["3"], "padoms": "240 : 80."},
        {"jaut": "a = {P|4}. P = 26 cm. a (cm)?",
         "atb": ["6,5"], "padoms": "26 : 4."},
        {"jaut": "x = {y − 3|2}. y = 15. x?",
         "atb": ["6"], "padoms": "12 : 2."},
    ]),

    Pasaule("Temperatūras pārvēršana",
            Ievadi("", [
                {"jaut": "F = 1,8C + 32. Izsaki C: C = (F − 32) : 1,8. Cik °C "
                         "ir 212 °F?",
                 "atb": ["100"], "padoms": "180 : 1,8."},
                {"jaut": "Cik °C ir 50 °F?",
                 "atb": ["10"], "padoms": "18 : 1,8."},
                {"jaut": "Cik °C ir 32 °F?",
                 "atb": ["0"], "padoms": "0 : 1,8."},
            ]),
            pavediens="planeta",
            konteksts="ASV laika prognozes ir °F - ceļotājam jāizsaka °C.",
            kapec="Izteikta formula - ātrs pārrēķins."),

    Kopsavilkums([
        "Izsaku lielumu no formulas ar ekvivalentām darbībām.",
        "Izsaku locekli no proporcijas.",
        "Pārbaudu izteikto formulu ar skaitļiem.",
        "Lietoju izteikto formulu aprēķiniem.",
    ]),

    Majas([
        "No S = {a · h|2} izsaki h.",
        "No P = 2(a + b) izsaki b.",
        "Pārvērt savas pilsētas temperatūru uz °F.",
    ]),
]
